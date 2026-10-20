/**
 * Adversarial Stress & Verification Harness for Milestone 1
 * Challenger: teamwork_preview_challenger (Milestone 1-1)
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const { chromium } = require('playwright');

const PROJECT_ROOT = path.resolve(__dirname, '../..');
const INDEX_HTML = path.join(PROJECT_ROOT, 'index.html');
const SERVER_JS = path.join(PROJECT_ROOT, 'server.js');

const htmlContent = fs.readFileSync(INDEX_HTML, 'utf8');
const serverContent = fs.readFileSync(SERVER_JS, 'utf8');

const results = {
  emojiScans: [],
  gradientScans: [],
  paletteScans: [],
  navigationFuzzing: [],
  summary: { passed: 0, failed: 0 }
};

function record(suite, testName, passed, details) {
  if (passed) {
    results.summary.passed++;
    console.log(`  \x1b[32m[PASS]\x1b[0m [${suite}] ${testName}`);
  } else {
    results.summary.failed++;
    console.log(`  \x1b[31m[FAIL]\x1b[0m [${suite}] ${testName} - ${details}`);
  }
  results[suite].push({ testName, passed, details });
}

async function runAll() {
  console.log('================================================================');
  console.log('[CHALLENGER] ADVERSARIAL CHALLENGER SUITE: MILESTONE 1');
  console.log('================================================================\n');

  // ============================================================================
  // 1. EXHAUSTIVE UNICODE & ESCAPED EMOJI SCANNER
  // ============================================================================
  console.log('--- 1. Exhaustive Unicode & Escaped Emoji Scans ---');

  // Comprehensive Regex including all emoji planes, modifiers, keycaps, and dingbats
  const ADVERSARIAL_EMOJI_REGEX = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F700}-\u{1F77F}]|[\u{1F780}-\u{1F7FF}]|[\u{1F800}-\u{1F8FF}]|[\u{1F900}-\u{1F9FF}]|[\u{1FA00}-\u{1FA6F}]|[\u{1FA70}-\u{1FAFF}]|[\u{1FB00}-\u{1FBFF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]|[\u{2300}-\u{23FF}]|[\u{2B50}\u{2B55}]|[\u{203C}\u{2049}]|[\u{25AA}\u{25AB}\u{25B6}\u{25C0}\u{25FB}-\u{25FE}]|[\u{00A9}\u{00AE}]|[\u{2122}\u{2139}]|[\u{1F1E6}-\u{1F1FF}]|[\u{1F000}-\u{1F02F}]|[\u{1F0A0}-\u{1F0FF}]|[\u{FE0E}\u{FE0F}]|[\u{E0020}-\u{E007F}])/gu;

  // 1.1 Direct unicode emojis in index.html
  const rawHtmlEmojis = (htmlContent.match(ADVERSARIAL_EMOJI_REGEX) || []).filter(ch => {
    // Exclude copyright / registered if legitimate or check specific code points
    const cp = ch.codePointAt(0);
    // Flag any actual emoji pictographs
    return (cp >= 0x1F300 && cp <= 0x1FAFF) || (cp >= 0x2600 && cp <= 0x27BF) || (cp >= 0x1F600 && cp <= 0x1F64F) || (cp === 0x2B50 || cp === 0x2B55);
  });
  record('emojiScans', 'Zero raw unicode emoji pictographs in index.html', rawHtmlEmojis.length === 0, `Found: ${rawHtmlEmojis.length} (${rawHtmlEmojis.slice(0, 5).join(', ')})`);

  // 1.2 Direct unicode emojis in server.js
  const rawServerEmojis = (serverContent.match(ADVERSARIAL_EMOJI_REGEX) || []).filter(ch => {
    const cp = ch.codePointAt(0);
    return (cp >= 0x1F300 && cp <= 0x1FAFF) || (cp >= 0x2600 && cp <= 0x27BF) || (cp >= 0x1F600 && cp <= 0x1F64F);
  });
  record('emojiScans', 'Zero raw unicode emoji pictographs in server.js', rawServerEmojis.length === 0, `Found: ${rawServerEmojis.length}`);

  // 1.3 Escaped unicode sequences in index.html (e.g. \uD83D\uDE00, \u{1F600}, etc.)
  const escapedUnicodeRegex = /\\u[dD][89a-fA-F][0-9a-fA-F]{2}\\u[dD][c-fC-F][0-9a-fA-F]{2}|\\u\{1[fF][0-9a-fA-F]{3,4}\}/g;
  const escapedMatches = htmlContent.match(escapedUnicodeRegex) || [];
  record('emojiScans', 'Zero escaped unicode surrogate/code point emojis in index.html', escapedMatches.length === 0, `Found: ${escapedMatches.length} (${escapedMatches.slice(0, 5).join(', ')})`);

  // 1.4 HTML entities for emojis (&#128512;, &#x1F600;, etc.)
  const htmlDecimalEntityRegex = /&#(12[89][0-9]{3}|13[0-9]{4});/g;
  const htmlHexEntityRegex = /&#x(1[fF][0-9a-fA-F]{3}|26[0-9a-fA-F]{2}|27[0-9a-fA-F]{2});/gi;
  const decEntities = htmlContent.match(htmlDecimalEntityRegex) || [];
  const hexEntities = htmlContent.match(htmlHexEntityRegex) || [];
  record('emojiScans', 'Zero HTML decimal emoji entities in index.html', decEntities.length === 0, `Found: ${decEntities.length} (${decEntities.slice(0, 5).join(', ')})`);
  record('emojiScans', 'Zero HTML hex emoji entities in index.html', hexEntities.length === 0, `Found: ${hexEntities.length} (${hexEntities.slice(0, 5).join(', ')})`);

  // 1.5 CSS content pseudo-elements containing emojis (content: '...'; or content: "\...")
  const cssContentRegex = /content\s*:\s*['"]([^'"]+)['"]/gi;
  let cssEmojiCount = 0;
  let match;
  while ((match = cssContentRegex.exec(htmlContent)) !== null) {
    const val = match[1];
    if (ADVERSARIAL_EMOJI_REGEX.test(val)) {
      cssEmojiCount++;
    }
  }
  record('emojiScans', 'Zero emojis in CSS content pseudo-elements in index.html', cssEmojiCount === 0, `Found: ${cssEmojiCount}`);

  // 1.6 URL-encoded emojis (%F0%9F...)
  const urlEncodedEmojiRegex = /%F0%9F%[0-9A-Fa-f]{2}%[0-9A-Fa-f]{2}/gi;
  const urlEncodedEmojis = htmlContent.match(urlEncodedEmojiRegex) || [];
  record('emojiScans', 'Zero URL-encoded emoji percent-escapes in index.html', urlEncodedEmojis.length === 0, `Found: ${urlEncodedEmojis.length}`);

  // ============================================================================
  // 2. ADVERSARIAL CSS GRADIENT & COLOR PALETTE SCANNER
  // ============================================================================
  console.log('\n--- 2. Adversarial CSS Gradient & Color Palette Scans ---');

  // 2.1 CSS gradient functions
  const linearGradients = htmlContent.match(/linear-gradient\s*\(/gi) || [];
  const radialGradients = htmlContent.match(/radial-gradient\s*\(/gi) || [];
  const conicGradients = htmlContent.match(/conic-gradient\s*\(/gi) || [];
  const repeatingGradients = htmlContent.match(/repeating-(?:linear|radial)-gradient\s*\(/gi) || [];
  record('gradientScans', 'Zero linear-gradient expressions in index.html', linearGradients.length === 0, `Found: ${linearGradients.length}`);
  record('gradientScans', 'Zero radial-gradient expressions in index.html', radialGradients.length === 0, `Found: ${radialGradients.length}`);
  record('gradientScans', 'Zero conic-gradient expressions in index.html', conicGradients.length === 0, `Found: ${conicGradients.length}`);
  record('gradientScans', 'Zero repeating gradient expressions in index.html', repeatingGradients.length === 0, `Found: ${repeatingGradients.length}`);

  // 2.2 Tailwind gradient classes
  const tailwindGradients = htmlContent.match(/bg-gradient-[a-z0-9-]+/gi) || [];
  record('gradientScans', 'Zero Tailwind bg-gradient-* utility classes in index.html', tailwindGradients.length === 0, `Found: ${tailwindGradients.length}`);

  // 2.3 Off-palette legacy colors: #004797 and #142C47
  const legacyColor1 = (htmlContent.match(/004797/gi) || []).length;
  const legacyColor2 = (htmlContent.match(/142C47/gi) || []).length;
  record('paletteScans', 'Zero occurrences of non-corporate blue #004797 in index.html', legacyColor1 === 0, `Found: ${legacyColor1}`);
  record('paletteScans', 'Zero occurrences of non-corporate navy #142C47 in index.html', legacyColor2 === 0, `Found: ${legacyColor2}`);

  // 2.4 Verify official corporate palette presence
  const officialColors = ['#003E78', '#FDCA02', '#0A233F', '#FFFFFF', '#F2F1EC'];
  const missingOfficial = officialColors.filter(c => !htmlContent.toLowerCase().includes(c.toLowerCase()));
  record('paletteScans', 'All 5 official corporate colors actively referenced in index.html', missingOfficial.length === 0, `Missing: ${missingOfficial.join(', ')}`);

  // ============================================================================
  // 3. NAVIGATION FUZZING & STRESS TESTING WITH PLAYWRIGHT
  // ============================================================================
  console.log('\n--- 3. Navigation Fuzzing & Stress Testing (Playwright) ---');

  let browser;
  try {
    browser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
    });
    const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
    const page = await context.newPage();

    // Listen to uncaught page errors
    const pageErrors = [];
    page.on('pageerror', err => pageErrors.push(err.message));
    page.on('console', msg => {
      if (msg.type() === 'error') {
        // Log console errors for review
      }
    });

    const fileUrl = 'file:///' + INDEX_HTML.replace(/\\/g, '/');
    await page.goto(fileUrl, { waitUntil: 'load' });

    // 3.1 Check presence of window.navigateToDesktopTab
    const hasNavFn = await page.evaluate(() => typeof window.navigateToDesktopTab === 'function');
    record('navigationFuzzing', 'window.navigateToDesktopTab is defined and callable', hasNavFn, 'Function missing');

    // 3.2 Fuzz with invalid primitives: null, undefined, numbers, booleans, objects, arrays
    const fuzzPrimitivesResult = await page.evaluate(() => {
      const results = [];
      const testCases = [
        null,
        undefined,
        '',
        '   ',
        0,
        1,
        -1,
        NaN,
        Infinity,
        true,
        false,
        {},
        { tab: 'pipeline' },
        [],
        ['pipeline'],
        () => 'pipeline'
      ];

      for (const tc of testCases) {
        try {
          window.navigateToDesktopTab(tc);
          results.push({ input: String(tc), success: true });
        } catch (e) {
          results.push({ input: String(tc), success: false, error: e.message });
        }
      }
      return results;
    });

    const failedPrimitives = fuzzPrimitivesResult.filter(r => !r.success);
    record('navigationFuzzing', 'Fuzzing with 16 invalid primitives does not throw uncaught exceptions', failedPrimitives.length === 0, `Failed on: ${JSON.stringify(failedPrimitives)}`);

    // 3.3 Fuzz with malicious payloads (XSS, path traversal, SQL injection, buffer length)
    const fuzzMaliciousResult = await page.evaluate(() => {
      const maliciousCases = [
        '<script>window.__xss_leaked=true;</script>',
        '"><img src=x onerror=window.__xss_leaked=true;>',
        'javascript:alert(1)',
        '../../../../etc/passwd',
        "' OR '1'='1",
        'A'.repeat(10000),
        '__proto__',
        'constructor',
        'prototype',
        'toString',
        'valueOf'
      ];
      const results = [];
      for (const payload of maliciousCases) {
        try {
          window.navigateToDesktopTab(payload);
          results.push({ payload: payload.slice(0, 20), success: true });
        } catch (e) {
          results.push({ payload: payload.slice(0, 20), success: false, error: e.message });
        }
      }
      return { results, xssLeaked: window.__xss_leaked === true };
    });

    const failedMalicious = fuzzMaliciousResult.results.filter(r => !r.success);
    record('navigationFuzzing', 'Fuzzing with malicious XSS/injection payloads does not throw or execute XSS', failedMalicious.length === 0 && !fuzzMaliciousResult.xssLeaked, `XSS leaked: ${fuzzMaliciousResult.xssLeaked}, Errors: ${JSON.stringify(failedMalicious)}`);

    // 3.4 Valid navigation switching verification
    const validTabs = ['pipeline', 'mapa', 'kpis', 'recompensas', 'copiloto'];
    const validSwitchResults = await page.evaluate((tabs) => {
      const switchSummary = [];
      const containerMap = {
        'pipeline': 'dcrm-content-pipeline',
        'mapa': 'dcrm-content-mapa',
        'kpis': 'dcrm-content-kpis',
        'recompensas': 'dcrm-content-recompensas',
        'copiloto': 'dcrm-content-copiloto'
      };

      for (const tab of tabs) {
        window.navigateToDesktopTab(tab);
        const containerId = containerMap[tab];
        const container = document.getElementById(containerId);
        const isVisible = container && !container.classList.contains('hidden') && container.style.display !== 'none';
        
        // Also check that all OTHER containers are hidden
        const otherTabs = tabs.filter(t => t !== tab);
        const othersHidden = otherTabs.every(ot => {
          const oc = document.getElementById(containerMap[ot]);
          return !oc || oc.classList.contains('hidden') || oc.style.display === 'none';
        });

        // Check active button highlighting
        const activeBtn = document.getElementById(`dcrm-tab-btn-${tab}`);
        const hasActiveClass = activeBtn && activeBtn.classList.contains('bg-[#FDCA02]');

        switchSummary.push({ tab, isVisible, othersHidden, hasActiveClass });
      }
      return switchSummary;
    }, validTabs);

    const badSwitches = validSwitchResults.filter(s => !s.isVisible || !s.othersHidden || !s.hasActiveClass);
    record('navigationFuzzing', 'All 5 valid tabs properly toggle visibility and active highlight', badSwitches.length === 0, `Issues on: ${JSON.stringify(badSwitches)}`);

    // 3.5 High-frequency rapid switching stress test (2,000 rapid switches)
    const rapidStressResult = await page.evaluate(() => {
      const tabs = ['pipeline', 'mapa', 'kpis', 'recompensas', 'copiloto', 'invalid_tab', null, ''];
      const startTime = performance.now();
      for (let i = 0; i < 2000; i++) {
        const target = tabs[i % tabs.length];
        window.navigateToDesktopTab(target);
      }
      const duration = performance.now() - startTime;
      
      // Finally return to pipeline and verify state
      window.navigateToDesktopTab('pipeline');
      const pipelineEl = document.getElementById('dcrm-content-pipeline');
      const isPipelineActive = pipelineEl && !pipelineEl.classList.contains('hidden');

      return {
        duration,
        isPipelineActive,
        domIntact: document.body !== null
      };
    });

    record('navigationFuzzing', '2,000 rapid sequential tab switches complete with DOM stability', rapidStressResult.isPipelineActive && rapidStressResult.domIntact, `Duration: ${rapidStressResult.duration.toFixed(2)}ms`);

    // 3.6 Check for any uncaught page errors throughout browser test
    record('navigationFuzzing', 'Zero unhandled page exceptions recorded during execution', pageErrors.length === 0, `Page errors: ${pageErrors.join('; ')}`);

    await browser.close();
  } catch (err) {
    record('navigationFuzzing', 'Browser execution harness exception', false, err.stack || err.message);
    if (browser) await browser.close();
  }

  // ============================================================================
  // SUMMARY
  // ============================================================================
  console.log('\n================================================================');
  console.log(`TOTAL ADVERSARIAL CHECKS: ${results.summary.passed + results.summary.failed}`);
  console.log(`PASSED: ${results.summary.passed}`);
  console.log(`FAILED: ${results.summary.failed}`);
  console.log(`VERDICT: ${results.summary.failed === 0 ? '\x1b[32mAPPROVE\x1b[0m' : '\x1b[31mREQUEST_CHANGES\x1b[0m'}`);
  console.log('================================================================\n');

  return results;
}

runAll().then(res => {
  const exitCode = res.summary.failed === 0 ? 0 : 1;
  process.exit(exitCode);
}).catch(err => {
  console.error('Fatal crash in challenger suite:', err);
  process.exit(1);
});
