#!/usr/bin/env node
/**
 * Master E2E Test Suite Runner for UltraRacha CRM (Ultracem S.A.S.)
 *
 * Executes the complete 4-tier test infrastructure:
 * - Tier 1: Feature Coverage (>= 100 tests)
 * - Tier 2: Boundary & Corner Cases (>= 100 tests)
 * - Tier 3: Pairwise Cross-Feature Tests (>= 20 tests)
 * - Tier 4: Real-World Caribbean Construction Scenarios (5 scenarios)
 * Total: >= 225 test cases
 *
 * Exit code 0 if all executed tests pass.
 * Exit code 1 if any test fails.
 */

const { closeBrowser } = require('./test_helpers');
const tier1 = require('./tier1_feature_coverage.test');
const tier2 = require('./tier2_boundary_corner.test');
const tier3 = require('./tier3_cross_feature.test');
const tier4 = require('./tier4_application.test');

async function main() {
  const args = process.argv.slice(2);
  const tierArg = args.find(a => a.startsWith('--tier='));
  const targetTier = tierArg ? parseInt(tierArg.split('=')[1], 10) : null;
  const verbose = !args.includes('--quiet') && !args.includes('--summary-only');
  const jsonOutput = args.includes('--json');

  const startTime = Date.now();

  console.log('========================================================================');
  console.log('   ULTRARACHA CRM (ULTRACEM S.A.S.) — AUTOMATED E2E TEST RUNNER');
  console.log('   Test Methodology: 4-Tier Category-Partition + BVA + Pairwise + Workloads');
  console.log(`   Execution Time: ${new Date().toISOString()}`);
  console.log(`   Node.js Version: ${process.version} | Platform: ${process.platform}`);
  console.log('========================================================================\n');

  const tierSuites = [
    { num: 1, name: 'Tier 1: Feature Coverage', runner: tier1.run },
    { num: 2, name: 'Tier 2: Boundary & Corner Cases', runner: tier2.run },
    { num: 3, name: 'Tier 3: Pairwise Cross-Feature', runner: tier3.run },
    { num: 4, name: 'Tier 4: Real-World Scenarios', runner: tier4.run }
  ];

  const suitesToRun = targetTier
    ? tierSuites.filter(s => s.num === targetTier)
    : tierSuites;

  if (suitesToRun.length === 0) {
    console.error(`Error: Unknown tier ${targetTier}. Choose from 1, 2, 3, or 4.`);
    process.exit(1);
  }

  const tierSummaries = [];
  let grandTotal = 0;
  let grandPassed = 0;
  let grandFailed = 0;

  for (const suite of suitesToRun) {
    const tierStart = Date.now();
    try {
      const summary = await suite.runner({ verbose });
      summary.durationMs = Date.now() - tierStart;
      tierSummaries.push(summary);
      grandTotal += summary.total;
      grandPassed += summary.passed;
      grandFailed += summary.failed;
    } catch (err) {
      console.error(`\nFatal error running ${suite.name}:`, err);
      tierSummaries.push({
        name: suite.name,
        total: 0,
        passed: 0,
        failed: 1,
        durationMs: Date.now() - tierStart,
        error: err.message
      });
      grandFailed += 1;
    }
  }

  await closeBrowser();

  const totalDuration = ((Date.now() - startTime) / 1000).toFixed(2);
  const grandPassRate = grandTotal > 0 ? Math.round((grandPassed / grandTotal) * 100) : 0;

  console.log('\n========================================================================');
  console.log('                       E2E TEST EXECUTION SUMMARY                       ');
  console.log('========================================================================');
  console.log('Tier                                Total    Passed    Failed    Pass Rate    Time');
  console.log('----------------------------------------------------------------------------');

  tierSummaries.forEach(s => {
    const rate = s.total > 0 ? `${Math.round((s.passed / s.total) * 100)}%` : '0%';
    const timeStr = `${(s.durationMs / 1000).toFixed(2)}s`;
    console.log(
      `${s.name.padEnd(35)} ${String(s.total).padStart(5)}   ${String(s.passed).padStart(7)}   ${String(s.failed).padStart(7)}   ${rate.padStart(9)}   ${timeStr.padStart(6)}`
    );
  });

  console.log('----------------------------------------------------------------------------');
  console.log(
    `OVERALL TOTAL                       ${String(grandTotal).padStart(5)}   ${String(grandPassed).padStart(7)}   ${String(grandFailed).padStart(7)}   ${`${grandPassRate}%`.padStart(9)}   ${`${totalDuration}s`.padStart(6)}`
  );
  console.log('============================================================================');

  if (grandFailed === 0 && grandTotal >= 225) {
    console.log('\x1b[32m✔ SUCCESS: 100% of E2E tests passed! Acceptance criteria fully verified.\x1b[0m\n');
  } else if (grandFailed === 0) {
    console.log(`\x1b[32m✔ SUCCESS: All ${grandTotal} executed tests passed.\x1b[0m\n`);
  } else {
    console.log(`\x1b[33mℹ NOTICE: ${grandFailed} tests failed. (Expected during implementation phase; workers are executing milestones).\x1b[0m\n`);
  }

  if (jsonOutput) {
    console.log(JSON.stringify({ grandTotal, grandPassed, grandFailed, grandPassRate, tierSummaries }, null, 2));
  }

  process.exit(grandFailed > 0 ? 1 : 0);
}

main().catch(err => {
  console.error('Fatal crash in test runner:', err);
  closeBrowser().finally(() => process.exit(1));
});
