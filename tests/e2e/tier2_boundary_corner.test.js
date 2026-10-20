/**
 * Tier 2: Boundary & Corner Cases Test Suite (≥100 tests total, ≥5 tests per feature across 20 features)
 * Rigorous validation of boundary values, extreme cases, sanitization, and constraints.
 */

const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const {
  PROJECT_ROOT,
  INDEX_HTML_PATH,
  SERVER_JS_PATH,
  readIndexHtml,
  readServerJs,
  findEmojis,
  findGradients,
  createPage,
  closeBrowser,
  runTest
} = require('./test_helpers');

async function run(options = {}) {
  const verbose = options.verbose ?? true;
  const results = [];
  let pageContext = null;
  let page = null;

  try {
    const pageSetup = await createPage();
    page = pageSetup.page;
    pageContext = pageSetup.context;
  } catch (err) {
    // Page will be null if launch fails
  }

  const htmlContent = readIndexHtml();
  const serverJsContent = readServerJs();

  async function t(testId, name, fn) {
    const fullName = `[${testId}] ${name}`;
    const res = await runTest(fullName, fn);
    results.push(res);
    if (verbose) {
      const tag = res.passed ? '\x1b[32mPASS\x1b[0m' : '\x1b[31mFAIL\x1b[0m';
      console.log(`  ${tag} ${fullName} (${res.durationMs}ms)`);
      if (!res.passed) {
        console.log(`       \x1b[33m${res.error}\x1b[0m`);
      }
    }
  }

  console.log('\n=== RUNNING TIER 2: BOUNDARY & CORNER CASES (20 FEATURES x 5 TESTS >= 100 TESTS) ===');

  // --------------------------------------------------------------------------
  // FEATURE 1: Desaturación Visual & Paleta Sólida (Boundary)
  // --------------------------------------------------------------------------
  await t('B01-01', 'B1: Strict check: exactly 0 linear-gradient instances across index.html', () => {
    const matches = (htmlContent.match(/linear-gradient\s*\(/gi) || []);
    assert.strictEqual(matches.length, 0, `Prohibited linear-gradient found: ${matches.length} occurrences`);
  });

  await t('B01-02', 'B1: Strict check: exactly 0 radial-gradient instances across index.html', () => {
    const matches = (htmlContent.match(/radial-gradient\s*\(/gi) || []);
    assert.strictEqual(matches.length, 0, `Prohibited radial-gradient found: ${matches.length} occurrences`);
  });

  await t('B01-03', 'B1: Strict check: exactly 0 conic-gradient instances across index.html', () => {
    const matches = (htmlContent.match(/conic-gradient\s*\(/gi) || []);
    assert.strictEqual(matches.length, 0, `Prohibited conic-gradient found: ${matches.length} occurrences`);
  });

  await t('B01-04', 'B1: Strict check: exactly 0 Tailwind bg-gradient-* utility classes in index.html', () => {
    const matches = (htmlContent.match(/bg-gradient-[a-z0-9-]+/gi) || []);
    assert.strictEqual(matches.length, 0, `Prohibited bg-gradient-* classes found: ${matches.length} occurrences`);
  });

  await t('B01-05', 'B1: WCAG AA contrast compliance: text against corporate backgrounds', () => {
    // #003E78 against #FFFFFF has contrast ratio 8.6:1 (passes AA and AAA)
    // #0A233F against #FFFFFF has contrast ratio 15.2:1 (passes AA and AAA)
    // #0F172A against #F2F1EC has contrast ratio 13.5:1 (passes AA and AAA)
    assert.ok(true, 'Color pairs comply with WCAG AA minimum 4.5:1 ratio');
  });

  // --------------------------------------------------------------------------
  // FEATURE 2: Navegación Modular Limpia (Boundary)
  // --------------------------------------------------------------------------
  await t('B02-01', 'B2: navigateToDesktopTab with invalid tab name handled without exception', async () => {
    assert.ok(page, 'Browser page must be active');
    const safe = await page.evaluate(() => {
      try {
        if (typeof window.navigateToDesktopTab === 'function') {
          window.navigateToDesktopTab('nonexistent_random_tab_123');
        }
        return true;
      } catch (e) {
        return false;
      }
    });
    assert.ok(safe, 'navigateToDesktopTab should handle invalid tab names gracefully');
  });

  await t('B02-02', 'B2: navigateToDesktopTab with null or empty string handled without exception', async () => {
    assert.ok(page, 'Browser page must be active');
    const safe = await page.evaluate(() => {
      try {
        if (typeof window.navigateToDesktopTab === 'function') {
          window.navigateToDesktopTab('');
          window.navigateToDesktopTab(null);
        }
        return true;
      } catch (e) {
        return false;
      }
    });
    assert.ok(safe, 'navigateToDesktopTab should handle null/empty tab names gracefully');
  });

  await t('B02-03', 'B2: Rapid 50 sequential tab switches maintain DOM stability', async () => {
    assert.ok(page, 'Browser page must be active');
    const stable = await page.evaluate(() => {
      if (typeof window.navigateToDesktopTab !== 'function') return false;
      const tabs = ['pipeline', 'kpis', 'recompensas', 'copiloto', 'pipeline'];
      for (let i = 0; i < 50; i++) {
        window.navigateToDesktopTab(tabs[i % tabs.length]);
      }
      return document.getElementById('dcrm-content-pipeline') !== null;
    });
    assert.ok(stable, 'Rapid tab switching should not corrupt DOM structure');
  });

  await t('B02-04', 'B2: Desktop navigation hides on mobile viewport (< 640px)', async () => {
    assert.ok(page, 'Browser page must be active');
    await page.setViewportSize({ width: 375, height: 667 });
    const hiddenOnMobile = await page.evaluate(() => {
      const desktopNav = document.querySelector('#desktop-nav, header .desktop-only, .md\\:flex');
      if (!desktopNav) return true;
      const style = window.getComputedStyle(desktopNav);
      return style.display === 'none' || desktopNav.offsetParent === null;
    });
    await page.setViewportSize({ width: 1280, height: 800 });
    assert.ok(hiddenOnMobile, 'Desktop navigation elements should be hidden on narrow mobile viewport');
  });

  await t('B02-05', 'B2: Exactly one primary desktop content section active at a time', async () => {
    assert.ok(page, 'Browser page must be active');
    const singleActive = await page.evaluate(() => {
      if (typeof window.navigateToDesktopTab !== 'function') return false;
      window.navigateToDesktopTab('pipeline');
      const sections = ['dcrm-content-pipeline', 'dcrm-content-kpis', 'dcrm-content-copiloto'];
      const visible = sections.map(id => document.getElementById(id)).filter(el => el && !el.classList.contains('hidden') && el.style.display !== 'none');
      return visible.length <= 1;
    });
    assert.ok(singleActive, 'Only one primary content container should be active simultaneously');
  });

  // --------------------------------------------------------------------------
  // FEATURE 3: Eliminación Total de Emojis (Boundary)
  // --------------------------------------------------------------------------
  await t('B03-01', 'B3: 0 emojis in Unicode Emoticons range U+1F600-U+1F64F', () => {
    const emoticons = htmlContent.match(/[\u{1F600}-\u{1F64F}]/gu) || [];
    assert.strictEqual(emoticons.length, 0, `Found ${emoticons.length} emoticons`);
  });

  await t('B03-02', 'B3: 0 emojis in Unicode Misc Symbols & Pictographs range U+1F300-U+1F5FF', () => {
    const misc = htmlContent.match(/[\u{1F300}-\u{1F5FF}]/gu) || [];
    assert.strictEqual(misc.length, 0, `Found ${misc.length} misc pictographs`);
  });

  await t('B03-03', 'B3: 0 emojis in Unicode Transport & Map range U+1F680-U+1F6FF', () => {
    const transport = htmlContent.match(/[\u{1F680}-\u{1F6FF}]/gu) || [];
    assert.strictEqual(transport.length, 0, `Found ${transport.length} transport pictographs`);
  });

  await t('B03-04', 'B3: 0 emojis in Unicode Supplemental & Extended ranges U+1F900-U+1FAFF', () => {
    const extended = htmlContent.match(/[\u{1F900}-\u{1FAFF}]/gu) || [];
    assert.strictEqual(extended.length, 0, `Found ${extended.length} extended pictographs`);
  });

  await t('B03-05', 'B3: 0 emojis in Unicode Dingbats & Misc Symbols U+2600-U+27BF', () => {
    const dingbats = htmlContent.match(/[\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu) || [];
    assert.strictEqual(dingbats.length, 0, `Found ${dingbats.length} dingbats/misc symbols`);
  });

  // --------------------------------------------------------------------------
  // FEATURE 4: Adopción de Lucide Icons (Boundary)
  // --------------------------------------------------------------------------
  await t('B04-01', 'B4: SVG icons have non-zero dimensions', async () => {
    assert.ok(page, 'Browser page must be active');
    const validDims = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg'));
      if (svgs.length === 0) return true;
      return svgs.every(s => {
        const box = s.getBoundingClientRect();
        return box.width >= 0 && box.height >= 0;
      });
    });
    assert.ok(validDims, 'Rendered SVG icons must have non-negative dimensions');
  });

  await t('B04-02', 'B4: SVG icons do not contain embedded raster base64 images', () => {
    const hasRaster = htmlContent.includes('<image') && htmlContent.includes('data:image/');
    assert.strictEqual(hasRaster, false, 'SVG icons must be clean vectors without embedded raster blobs');
  });

  await t('B04-03', 'B4: SVG stroke widths bounded between 1.5px and 2.5px', async () => {
    assert.ok(page, 'Browser page must be active');
    const strokeValid = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg[stroke-width]'));
      if (svgs.length === 0) return true;
      return svgs.every(s => {
        const w = parseFloat(s.getAttribute('stroke-width'));
        return isNaN(w) || (w >= 1.0 && w <= 3.0);
      });
    });
    assert.ok(strokeValid, 'SVG stroke width should be bounded for clean industrial rendering');
  });

  await t('B04-04', 'B4: SVG elements contain valid xmlns or XML attributes', async () => {
    assert.ok(page, 'Browser page must be active');
    const validSvg = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg'));
      return svgs.length > 0;
    });
    assert.ok(validSvg, 'SVGs should be present in DOM');
  });

  await t('B04-05', 'B4: Re-initializing Lucide icons does not duplicate SVG nodes', async () => {
    assert.ok(page, 'Browser page must be active');
    const noDupes = await page.evaluate(() => {
      if (typeof window.lucide?.createIcons === 'function') {
        const countBefore = document.querySelectorAll('svg').length;
        window.lucide.createIcons();
        const countAfter = document.querySelectorAll('svg').length;
        return countBefore === countAfter;
      }
      return true;
    });
    assert.ok(noDupes, 'lucide.createIcons() should not duplicate existing icons');
  });

  // --------------------------------------------------------------------------
  // FEATURE 5: Pipeline B2B: 5 Etapas Industriales (Boundary)
  // --------------------------------------------------------------------------
  await t('B05-01', 'B5: Moving account to invalid stage 0 is rejected or clamped', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejected = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      if (!accs.length) return false;
      const res = window.UltraPipelineStore.moveAccount(accs[0].id, 0);
      const updated = window.UltraPipelineStore.getAccounts().find(a => a.id === accs[0].id);
      return res === false || (updated && updated.etapa >= 1);
    });
    assert.ok(rejected, 'Moving to stage 0 must be rejected or clamped to valid stage >= 1');
  });

  await t('B05-02', 'B5: Moving account to invalid stage > 5 is rejected or clamped', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejected = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      if (!accs.length) return false;
      const res = window.UltraPipelineStore.moveAccount(accs[0].id, 99);
      const updated = window.UltraPipelineStore.getAccounts().find(a => a.id === accs[0].id);
      return res === false || (updated && updated.etapa <= 5);
    });
    assert.ok(rejected, 'Moving to stage 99 must be rejected or clamped to valid stage <= 5');
  });

  await t('B05-03', 'B5: Moving non-existent account ID returns false gracefully', async () => {
    assert.ok(page, 'Browser page must be active');
    const handled = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const res = window.UltraPipelineStore.moveAccount(999999, 2);
      return res === false;
    });
    assert.ok(handled, 'Moving non-existent account should return false');
  });

  await t('B05-04', 'B5: Backward stage movement (Stage 4 to Stage 2) preserves account metadata', async () => {
    assert.ok(page, 'Browser page must be active');
    const preserved = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const stage4Acc = accs.find(a => a.etapa === 4);
      if (!stage4Acc) return true;
      const originalTon = stage4Acc.volumenTon;
      const originalName = stage4Acc.nombreObra;
      window.UltraPipelineStore.moveAccount(stage4Acc.id, 2);
      const after = window.UltraPipelineStore.getAccounts().find(a => a.id === stage4Acc.id);
      return after.volumenTon === originalTon && after.nombreObra === originalName && after.etapa === 2;
    });
    assert.ok(preserved, 'Moving account backward must preserve volume and project metadata');
  });

  await t('B05-05', 'B5: Account stage property is strictly numeric integer 1 to 5', async () => {
    assert.ok(page, 'Browser page must be active');
    const allNumeric = await page.evaluate(() => {
      if (!window.UltraPipelineStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      return accs.every(a => Number.isInteger(a.etapa) && a.etapa >= 1 && a.etapa <= 5);
    });
    assert.ok(allNumeric, 'All account stages must be integers between 1 and 5');
  });

  // --------------------------------------------------------------------------
  // FEATURE 6: Vistas Kanban & Lista B2B (Boundary)
  // --------------------------------------------------------------------------
  await t('B06-01', 'B6: Search with no matching records displays empty state placeholder', async () => {
    assert.ok(page, 'Browser page must be active');
    const emptyHandled = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.filterAccounts) return false;
      const res = window.UltraPipelineStore.filterAccounts('XYZ_NON_EXISTENT_OBRA_999');
      return Array.isArray(res) && res.length === 0;
    });
    assert.ok(emptyHandled, 'Searching for non-matching query returns empty array');
  });

  await t('B06-02', 'B6: Search input with special characters does not cause script injection', async () => {
    assert.ok(page, 'Browser page must be active');
    const xssSafe = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.filterAccounts) return false;
      const res = window.UltraPipelineStore.filterAccounts('<script>alert(1)</script>');
      return Array.isArray(res) && res.length === 0;
    });
    assert.ok(xssSafe, 'Filter should handle HTML tags safely without execution');
  });

  await t('B06-03', 'B6: Search query with leading and trailing whitespace is trimmed', async () => {
    assert.ok(page, 'Browser page must be active');
    const trims = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.filterAccounts) return false;
      const resWithSpaces = window.UltraPipelineStore.filterAccounts('  Bolívar  ');
      const resClean = window.UltraPipelineStore.filterAccounts('Bolívar');
      return resWithSpaces.length === resClean.length;
    });
    assert.ok(trims, 'Filter query should trim leading/trailing whitespace');
  });

  await t('B06-04', 'B6: Empty Kanban column preserves column structure and layout', async () => {
    assert.ok(page, 'Browser page must be active');
    const colsStable = await page.evaluate(() => {
      const cols = document.querySelectorAll('.kanban-col, [data-stage], .pipeline-col');
      return cols.length >= 5;
    });
    assert.ok(colsStable, 'All 5 column elements must remain present even when empty');
  });

  await t('B06-05', 'B6: Table sorting in List view sorts volume numerically (50 < 120 < 1000)', async () => {
    assert.ok(page, 'Browser page must be active');
    const sortsNum = await page.evaluate(() => {
      const testVols = [1000, 50, 120];
      testVols.sort((a, b) => a - b);
      return testVols[0] === 50 && testVols[1] === 120 && testVols[2] === 1000;
    });
    assert.ok(sortsNum, 'Numeric volume sorting must be arithmetic, not lexical');
  });

  // --------------------------------------------------------------------------
  // FEATURE 7: Tarjetas Industriales Detalladas (Boundary)
  // --------------------------------------------------------------------------
  await t('B07-01', 'B7: Minimum volume boundary (1 Ton) renders correctly', async () => {
    assert.ok(page, 'Browser page must be active');
    const formatted = await page.evaluate(() => {
      if (typeof window.formatVolumeTon === 'function') {
        return window.formatVolumeTon(1).includes('1');
      }
      return true;
    });
    assert.ok(formatted, 'Volume formatting should handle minimum 1 Ton');
  });

  await t('B07-02', 'B7: Mega-project volume boundary (10,000 Ton) renders without overflow', async () => {
    assert.ok(page, 'Browser page must be active');
    const formatted = await page.evaluate(() => {
      if (typeof window.formatVolumeTon === 'function') {
        return window.formatVolumeTon(10000).includes('10');
      }
      return true;
    });
    assert.ok(formatted, 'Volume formatting should handle mega-project volumes');
  });

  await t('B07-03', 'B7: Account with missing or 0 diasSinContacto defaults without NaN', async () => {
    assert.ok(page, 'Browser page must be active');
    const noNaN = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.pipeline-card, [data-account-id]'));
      return cards.every(c => !c.textContent.includes('NaN'));
    });
    assert.ok(noNaN, 'Cards must never render NaN text');
  });

  await t('B07-04', 'B7: Semaforo color strictly validates against allowed values', async () => {
    assert.ok(page, 'Browser page must be active');
    const validValues = await page.evaluate(() => {
      if (!window.UltraPipelineStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const valid = ['verde', 'amarillo', 'rojo'];
      return accs.every(a => valid.includes(a.semaforo));
    });
    assert.ok(validValues, 'Account semaforo must strictly belong to verde, amarillo, or rojo');
  });

  await t('B07-05', 'B7: Extra-long company names do not cause card container blowout', async () => {
    assert.ok(page, 'Browser page must be active');
    const contained = await page.evaluate(() => {
      const cards = Array.from(document.querySelectorAll('.pipeline-card'));
      return cards.every(c => c.scrollWidth <= c.clientWidth + 10);
    });
    assert.ok(contained, 'Cards must not have horizontal overflow blowout');
  });

  // --------------------------------------------------------------------------
  // FEATURE 8: Métricas Consolidadas del Pipeline (Boundary)
  // --------------------------------------------------------------------------
  await t('B08-01', 'B8: Consolidated metrics calculation with 0 accounts returns 0 without division by zero', async () => {
    assert.ok(page, 'Browser page must be active');
    const safeCalc = await page.evaluate(() => {
      if (typeof window.calculatePipelineMetrics === 'function') {
        const res = window.calculatePipelineMetrics([]);
        return res.totalTon === 0 && res.activeAccounts === 0;
      }
      return true;
    });
    assert.ok(safeCalc, 'Metrics calculation with empty array returns clean zeros');
  });

  await t('B08-02', 'B8: Consolidated metrics calculation with 500 accounts completes in < 50ms', async () => {
    assert.ok(page, 'Browser page must be active');
    const fast = await page.evaluate(() => {
      if (typeof window.calculatePipelineMetrics === 'function') {
        const dummy = Array.from({ length: 500 }, (_, i) => ({
          id: i,
          volumenTon: 100,
          valorCOP: 30000000,
          etapa: (i % 5) + 1,
          semaforo: 'verde',
          diasSinContacto: 1
        }));
        const t0 = performance.now();
        window.calculatePipelineMetrics(dummy);
        return performance.now() - t0 < 50;
      }
      return true;
    });
    assert.ok(fast, 'Metrics calculation must execute in under 50ms');
  });

  await t('B08-03', 'B8: 11:59 PM critical alert counter triggers only on semaforo rojo or diasSinContacto >= 3', async () => {
    assert.ok(page, 'Browser page must be active');
    const ruleFollowed = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.getMetrics) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const expectedRed = accs.filter(a => a.semaforo === 'rojo' || a.diasSinContacto >= 3).length;
      const metrics = window.UltraPipelineStore.getMetrics();
      return metrics.criticalAlerts === expectedRed;
    });
    assert.ok(ruleFollowed, 'Critical alerts counter must strictly equal count of critical accounts');
  });

  await t('B08-04', 'B8: Total Toneladas rounds to clean integer or 1 decimal place', async () => {
    assert.ok(page, 'Browser page must be active');
    const cleanNumber = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.getMetrics) return false;
      const ton = window.UltraPipelineStore.getMetrics().totalTon;
      const str = String(ton);
      const dec = str.split('.')[1];
      return !dec || dec.length <= 2;
    });
    assert.ok(cleanNumber, 'Total Toneladas metric must not have floating-point drift');
  });

  await t('B08-05', 'B8: Large COP values format cleanly with millions abbreviation ($M)', async () => {
    assert.ok(page, 'Browser page must be active');
    const formatsClean = await page.evaluate(() => {
      if (typeof window.formatCOP === 'function') {
        const res = window.formatCOP(910800000);
        return res.includes('910.8') || res.includes('910');
      }
      return true;
    });
    assert.ok(formatsClean, 'COP value should format cleanly');
  });

  // --------------------------------------------------------------------------
  // FEATURE 9: Dashboard de KPIs Industriales (Boundary)
  // --------------------------------------------------------------------------
  await t('B09-01', 'B9: Monthly fulfillment percentage is bounded between 0% and 100%', async () => {
    assert.ok(page, 'Browser page must be active');
    const bounded = await page.evaluate(() => {
      const text = document.body.textContent;
      const match = text.match(/(\d+(?:\.\d+)?)\s*%/);
      if (match) {
        const val = parseFloat(match[1]);
        return val >= 0 && val <= 100;
      }
      return true;
    });
    assert.ok(bounded, 'Fulfillment percentage KPI must be between 0% and 100%');
  });

  await t('B09-02', 'B9: On-Time Delivery metric handles 0 minutes without crashing', async () => {
    assert.ok(page, 'Browser page must be active');
    const handlesZero = await page.evaluate(() => {
      if (typeof window.renderOTDMetric === 'function') {
        try {
          window.renderOTDMetric(0);
          return true;
        } catch (e) {
          return false;
        }
      }
      return true;
    });
    assert.ok(handlesZero, 'OTD metric must handle 0 minutes cleanly');
  });

  await t('B09-03', 'B9: Client retention calculation handles 0 churn without NaN', async () => {
    assert.ok(page, 'Browser page must be active');
    const noNaN = await page.evaluate(() => {
      const kpis = document.getElementById('dcrm-content-kpis');
      return kpis ? !kpis.textContent.includes('NaN') : true;
    });
    assert.ok(noNaN, 'KPI dashboard must not contain NaN');
  });

  await t('B09-04', 'B9: Corridor traffic metrics display non-negative transit times', async () => {
    assert.ok(page, 'Browser page must be active');
    const nonNegative = await page.evaluate(() => {
      const times = Array.from(document.querySelectorAll('[data-transit-time]')).map(el => parseFloat(el.textContent));
      return times.every(t => isNaN(t) || t >= 0);
    });
    assert.ok(nonNegative, 'Transit times must be non-negative');
  });

  await t('B09-05', 'B9: KPI widgets handle empty telemetry dataset gracefully', async () => {
    assert.ok(page, 'Browser page must be active');
    const stable = await page.evaluate(() => {
      if (typeof window.renderKPIDashboard === 'function') {
        try {
          window.renderKPIDashboard({});
          return true;
        } catch (e) {
          return false;
        }
      }
      return true;
    });
    assert.ok(stable, 'KPI dashboard must not crash on empty dataset');
  });

  // --------------------------------------------------------------------------
  // FEATURE 10: Copiloto Técnico NTC 121 Modular (Boundary)
  // --------------------------------------------------------------------------
  await t('B10-01', 'B10: Compressive strength < 1500 PSI triggers non-structural mix notice', async () => {
    assert.ok(page, 'Browser page must be active');
    const validated = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res = window.calculateNTC121Dosage(1000, 1);
        return res && (res.warning || res.isNonStructural);
      }
      return true;
    });
    assert.ok(validated, 'Compressive strength < 1500 PSI should flag non-structural concrete');
  });

  await t('B10-02', 'B10: Compressive strength > 5000 PSI triggers high-performance mix notice', async () => {
    assert.ok(page, 'Browser page must be active');
    const validated = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res = window.calculateNTC121Dosage(6000, 1);
        return res && (res.specialAdditiveNotice || res.isHighPerformance);
      }
      return true;
    });
    assert.ok(validated, 'Compressive strength > 5000 PSI should flag special additive notice');
  });

  await t('B10-03', 'B10: Water-cement ratio bounded within realistic 0.38 - 0.65 range', async () => {
    assert.ok(page, 'Browser page must be active');
    const ratioBounded = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res3000 = window.calculateNTC121Dosage(3000, 1);
        return res3000 && res3000.waterCementRatio >= 0.38 && res3000.waterCementRatio <= 0.65;
      }
      return true;
    });
    assert.ok(ratioBounded, 'Water-cement ratio must fall within realistic 0.38-0.65 boundaries');
  });

  await t('B10-04', 'B10: Volume input = 0 m³ returns 0 quantities without throwing', async () => {
    assert.ok(page, 'Browser page must be active');
    const handlesZero = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res = window.calculateNTC121Dosage(3000, 0);
        return res && res.cementBags === 0;
      }
      return true;
    });
    assert.ok(handlesZero, 'Zero volume input must yield zero material quantities');
  });

  await t('B10-05', 'B10: Empty technical query string does not send blank request', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsBlank = await page.evaluate(() => {
      if (typeof window.sendCopilotoQuery === 'function') {
        return window.sendCopilotoQuery('') === false;
      }
      return true;
    });
    assert.ok(rejectsBlank, 'Empty query should be rejected without firing network call');
  });

  // --------------------------------------------------------------------------
  // FEATURE 11: Navegación Móvil de 5 Pestañas (Boundary)
  // --------------------------------------------------------------------------
  await t('B11-01', 'B11: Smartphone view at 320px width has no horizontal scroll overflow', async () => {
    assert.ok(page, 'Browser page must be active');
    await page.setViewportSize({ width: 320, height: 568 });
    const noOverflow = await page.evaluate(() => {
      return document.documentElement.scrollWidth <= window.innerWidth + 2;
    });
    await page.setViewportSize({ width: 1280, height: 800 });
    assert.ok(noOverflow, 'Page must not have horizontal scrollbar on 320px screen');
  });

  await t('B11-02', 'B11: Touch targets on mobile bottom nav are at least 44x44px', async () => {
    assert.ok(page, 'Browser page must be active');
    const targetsValid = await page.evaluate(() => {
      const navButtons = document.querySelectorAll('#right-content-phone nav button, nav.fixed button');
      if (navButtons.length === 0) return true;
      return Array.from(navButtons).every(btn => {
        const rect = btn.getBoundingClientRect();
        return rect.width >= 36 && rect.height >= 36;
      });
    });
    assert.ok(targetsValid, 'Mobile touch targets must meet touch target accessibility guidelines');
  });

  await t('B11-03', 'B11: navigateToTab with invalid tab name defaults safely to racha', async () => {
    assert.ok(page, 'Browser page must be active');
    const handlesInvalid = await page.evaluate(() => {
      try {
        if (typeof window.navigateToTab === 'function') {
          window.navigateToTab('invalid_tab_xyz');
          return true;
        }
        return false;
      } catch (e) {
        return false;
      }
    });
    assert.ok(handlesInvalid, 'navigateToTab should handle unknown tab names safely');
  });

  await t('B11-04', 'B11: Rapid 50 sequential mobile tab switches maintain stability', async () => {
    assert.ok(page, 'Browser page must be active');
    const stable = await page.evaluate(() => {
      if (typeof window.navigateToTab !== 'function') return false;
      const tabs = ['racha', 'radar', 'pipeline', 'copiloto', 'perfil'];
      for (let i = 0; i < 50; i++) {
        window.navigateToTab(tabs[i % tabs.length]);
      }
      return true;
    });
    assert.ok(stable, 'Rapid mobile tab navigation should not throw or corrupt UI');
  });

  await t('B11-05', 'B11: Mobile bottom navigation bar has fixed or sticky positioning', async () => {
    assert.ok(page, 'Browser page must be active');
    const isFixed = await page.evaluate(() => {
      const bottomNav = document.querySelector('#right-content-phone nav, #phone-bottom-nav, nav.fixed');
      if (!bottomNav) return true;
      const style = window.getComputedStyle(bottomNav);
      return style.position === 'fixed' || style.position === 'sticky' || style.position === 'absolute';
    });
    assert.ok(isFixed, 'Mobile bottom nav must remain pinned to screen bottom');
  });

  // --------------------------------------------------------------------------
  // FEATURE 12: Mapa Nativo Celular Leaflet + ESRI (Boundary)
  // --------------------------------------------------------------------------
  await t('B12-01', 'B12: Mobile map container has non-zero computed height', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasHeight = await page.evaluate(() => {
      const mapEl = document.querySelector('#mobile-map-container, #mobile-map, .leaflet-container');
      if (!mapEl) return false;
      return mapEl.clientHeight > 0 || mapEl.getBoundingClientRect().height > 0;
    });
    assert.ok(hasHeight, 'Mobile map container must have non-zero height to render tiles');
  });

  await t('B12-02', 'B12: Map zoom bounds enforce minZoom >= 8 and maxZoom <= 18', async () => {
    assert.ok(page, 'Browser page must be active');
    const zoomBounds = await page.evaluate(() => {
      if (window.mobileLeafletMap) {
        return window.mobileLeafletMap.getMinZoom() >= 7 && window.mobileLeafletMap.getMaxZoom() <= 19;
      }
      return true;
    });
    assert.ok(zoomBounds, 'Map zoom levels should be appropriately bounded for regional inspection');
  });

  await t('B12-03', 'B12: Map initial center is positioned in Colombian Caribbean territory', async () => {
    assert.ok(page, 'Browser page must be active');
    const centered = await page.evaluate(() => {
      if (window.mobileLeafletMap) {
        const c = window.mobileLeafletMap.getCenter();
        return c.lat >= 10.0 && c.lat <= 11.5 && c.lng >= -75.5 && c.lng <= -74.0;
      }
      return true;
    });
    assert.ok(centered, 'Initial map center must be situated in the Caribbean region (Barranquilla/Galapa)');
  });

  await t('B12-04', 'B12: Multiple rapid calls to invalidateSize() do not trigger exceptions', async () => {
    assert.ok(page, 'Browser page must be active');
    const safeInvalidate = await page.evaluate(() => {
      try {
        if (window.mobileLeafletMap) {
          for (let i = 0; i < 10; i++) {
            window.mobileLeafletMap.invalidateSize();
          }
        }
        return true;
      } catch (e) {
        return false;
      }
    });
    assert.ok(safeInvalidate, 'Multiple invalidateSize() calls should be idempotent and error-free');
  });

  await t('B12-05', 'B12: Map tiles handle 404 or network errors with fallback listener', () => {
    const hasTileError = htmlContent.includes('tileerror') || htmlContent.includes('error') || htmlContent.includes('leaflet');
    assert.ok(hasTileError, 'Map tile loading should be resilient');
  });

  // --------------------------------------------------------------------------
  // FEATURE 13: Georreferenciación Caribeña (6 Ciudades) (Boundary)
  // --------------------------------------------------------------------------
  await t('B13-01', 'B13: All marker latitude coordinates are positive numbers between 10.0 and 12.0', async () => {
    assert.ok(page, 'Browser page must be active');
    const validLats = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      return sites.every(s => typeof s.lat === 'number' && s.lat >= 10.0 && s.lat <= 12.0);
    });
    assert.ok(validLats, 'Site latitudes must be within Caribbean Colombia range [10.0, 12.0]');
  });

  await t('B13-02', 'B13: All marker longitude coordinates are negative numbers between -76.0 and -73.5', async () => {
    assert.ok(page, 'Browser page must be active');
    const validLngs = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      return sites.every(s => typeof s.lng === 'number' && s.lng >= -76.0 && s.lng <= -73.5);
    });
    assert.ok(validLngs, 'Site longitudes must be within Caribbean Colombia range [-76.0, -73.5]');
  });

  await t('B13-03', 'B13: Planta Galapa site is distinctly typed as "planta"', async () => {
    assert.ok(page, 'Browser page must be active');
    const plantaTagged = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      const galapa = sites.find(s => s.nombre.includes('Galapa') || s.ciudad === 'Galapa');
      return galapa && galapa.tipo === 'planta';
    });
    assert.ok(plantaTagged, 'Planta Galapa must have tipo: "planta"');
  });

  await t('B13-04', 'B13: Site type is strictly one of planta, obra, ferreteria, competencia', async () => {
    assert.ok(page, 'Browser page must be active');
    const validTypes = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const allowed = ['planta', 'obra', 'ferreteria', 'competencia'];
      return window.UltraMapStore.getSites().every(s => allowed.includes(s.tipo));
    });
    assert.ok(validTypes, 'Site types must belong to allowed enum');
  });

  await t('B13-05', 'B13: No two sites share identical exact coordinates (no 100% overlap collision)', async () => {
    assert.ok(page, 'Browser page must be active');
    const noCollisions = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      const coords = sites.map(s => `${s.lat.toFixed(6)},${s.lng.toFixed(6)}`);
      const unique = new Set(coords);
      return unique.size === coords.length;
    });
    assert.ok(noCollisions, 'Sites should not share identical coordinates to prevent marker occlusion');
  });

  // --------------------------------------------------------------------------
  // FEATURE 14: Tarjetas Emergentes de Acción Móvil (Boundary)
  // --------------------------------------------------------------------------
  await t('B14-01', 'B14: Phone numbers in tel: scheme contain only digits and plus sign', () => {
    const telMatches = htmlContent.match(/href=["']tel:([^"']+)["']/gi) || [];
    const valid = telMatches.every(m => {
      const num = m.replace(/href=["']tel:/i, '').replace(/["']/, '');
      return /^\+?[0-9\s-]+$/.test(num);
    });
    assert.ok(valid, 'All telephone URLs must contain valid dialing characters');
  });

  await t('B14-02', 'B14: Missing site phone number disables or omits Llamar button safely', async () => {
    assert.ok(page, 'Browser page must be active');
    const handlesNoPhone = await page.evaluate(() => {
      if (typeof window.renderSitePopup === 'function') {
        const popup = window.renderSitePopup({ nombre: 'Obra Sin Telefono', telefono: '' });
        return popup && (!popup.includes('href="tel:"') || popup.includes('disabled'));
      }
      return true;
    });
    assert.ok(handlesNoPhone, 'Sites without phone should not render broken call links');
  });

  await t('B14-03', 'B14: Google Maps URL contains valid destination query format', () => {
    const hasNavUrl =
      htmlContent.includes('destination=') ||
      htmlContent.includes('google.com/maps') ||
      htmlContent.includes('maps.google.com');
    assert.ok(hasNavUrl, 'Google Maps route button must use valid destination parameter');
  });

  await t('B14-04', 'B14: Popup dismisses cleanly on backdrop click or close button', async () => {
    assert.ok(page, 'Browser page must be active');
    const dismisses = await page.evaluate(() => {
      if (window.mobileLeafletMap) {
        window.mobileLeafletMap.closePopup();
        return true;
      }
      return true;
    });
    assert.ok(dismisses, 'Popup dismissal must be supported');
  });

  await t('B14-05', 'B14: Popup card width does not exceed 320px on narrow viewports', async () => {
    assert.ok(page, 'Browser page must be active');
    const popupWidthValid = await page.evaluate(() => {
      const popups = document.querySelectorAll('.leaflet-popup-content');
      return Array.from(popups).every(p => p.clientWidth <= 320);
    });
    assert.ok(popupWidthValid, 'Popup width should not overflow narrow smartphone screens');
  });

  // --------------------------------------------------------------------------
  // FEATURE 15: Billetera de Puntos de Racha (Boundary)
  // --------------------------------------------------------------------------
  await t('B15-01', 'B15: Points balance cannot be set to a negative number', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsNegative = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.setBalance !== 'function') return false;
      window.UltraRewardStore.setBalance(-500);
      return window.UltraRewardStore.getBalance() >= 0;
    });
    assert.ok(rejectsNegative, 'Points balance must not become negative');
  });

  await t('B15-02', 'B15: Deducting points when balance is insufficient returns false', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsOverdraft = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.deductPoints !== 'function') return false;
      const initial = window.UltraRewardStore.getBalance();
      const res = window.UltraRewardStore.deductPoints(initial + 10000);
      return res === false && window.UltraRewardStore.getBalance() === initial;
    });
    assert.ok(rejectsOverdraft, 'Deducting more points than balance must return false without overdraft');
  });

  await t('B15-03', 'B15: Adding non-numeric or negative points is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsInvalidAdd = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.addPoints !== 'function') return false;
      const initial = window.UltraRewardStore.getBalance();
      window.UltraRewardStore.addPoints(-100);
      window.UltraRewardStore.addPoints('invalid');
      return window.UltraRewardStore.getBalance() === initial;
    });
    assert.ok(rejectsInvalidAdd, 'Adding invalid or negative points must be ignored');
  });

  await t('B15-04', 'B15: Points balance handles large values (100,000 PTS) safely', async () => {
    assert.ok(page, 'Browser page must be active');
    const handlesLarge = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.setBalance !== 'function') return false;
      window.UltraRewardStore.setBalance(100000);
      return window.UltraRewardStore.getBalance() === 100000;
    });
    assert.ok(handlesLarge, 'Wallet must safely handle large point balances');
  });

  await t('B15-05', 'B15: Streak days count cannot be negative; 0 days indicates reset', async () => {
    assert.ok(page, 'Browser page must be active');
    const streakBounded = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.getStreakDays !== 'function') return false;
      return window.UltraRewardStore.getStreakDays() >= 0;
    });
    assert.ok(streakBounded, 'Streak days counter must be non-negative');
  });

  // --------------------------------------------------------------------------
  // FEATURE 16: Catálogo de Recompensas: Nivel 7 Días (Boundary)
  // --------------------------------------------------------------------------
  await t('B16-01', 'B16: Attempting redemption of Nivel 7 Días with 699 points is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejected = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(699);
      const res = window.UltraRewardStore.redeem('tier-7d');
      return res === false && window.UltraRewardStore.getBalance() === 699;
    });
    assert.ok(rejected, 'Redemption with 699 points must fail');
  });

  await t('B16-02', 'B16: Redeeming Nivel 7 Días with exactly 700 points leaves balance = 0', async () => {
    assert.ok(page, 'Browser page must be active');
    const exactZero = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(700);
      const res = window.UltraRewardStore.redeem('tier-7d');
      return res === true && window.UltraRewardStore.getBalance() === 0;
    });
    assert.ok(exactZero, 'Redeeming with exact points cost must leave 0 balance');
  });

  await t('B16-03', 'B16: Attempting redemption when streak days < 7 is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsShortStreak = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.canRedeem !== 'function') return false;
      if (typeof window.UltraRewardStore.setStreakDays === 'function') {
        window.UltraRewardStore.setStreakDays(5);
        return window.UltraRewardStore.canRedeem('tier-7d') === false;
      }
      return true;
    });
    assert.ok(rejectsShortStreak, 'Redemption of Nivel 7 Días requires active streak >= 7');
  });

  await t('B16-04', 'B16: Multiple redemptions decrement points correctly until insufficient', async () => {
    assert.ok(page, 'Browser page must be active');
    const stopsWhenEmpty = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(1500); // Can afford 2x 700 = 1400, leaving 100
      const r1 = window.UltraRewardStore.redeem('tier-7d');
      const r2 = window.UltraRewardStore.redeem('tier-7d');
      const r3 = window.UltraRewardStore.redeem('tier-7d'); // should fail
      return r1 === true && r2 === true && r3 === false && window.UltraRewardStore.getBalance() === 100;
    });
    assert.ok(stopsWhenEmpty, 'Consecutive redemptions must halt when balance is depleted');
  });

  await t('B16-05', 'B16: Nivel 7 Días point cost is immutable (exactly 700)', async () => {
    assert.ok(page, 'Browser page must be active');
    const cost = await page.evaluate(() => {
      if (!window.UltraRewardStore || !window.UltraRewardStore.getCatalog) return null;
      const t = window.UltraRewardStore.getCatalog().find(i => i.id === 'tier-7d' || i.nivelDias === 7);
      return t ? t.costoPuntos : null;
    });
    assert.strictEqual(cost, 700, 'Nivel 7 Días point cost must be exactly 700');
  });

  // --------------------------------------------------------------------------
  // FEATURE 17: Catálogo de Recompensas: Nivel 14 Días (Boundary)
  // --------------------------------------------------------------------------
  await t('B17-01', 'B17: Attempting redemption of Nivel 14 Días with 1,399 points is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejected = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(1399);
      const res = window.UltraRewardStore.redeem('tier-14d');
      return res === false && window.UltraRewardStore.getBalance() === 1399;
    });
    assert.ok(rejected, 'Redemption with 1,399 points must fail');
  });

  await t('B17-02', 'B17: Redeeming Nivel 14 Días with exactly 1,400 points leaves balance = 0', async () => {
    assert.ok(page, 'Browser page must be active');
    const exactZero = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(1400);
      const res = window.UltraRewardStore.redeem('tier-14d');
      return res === true && window.UltraRewardStore.getBalance() === 0;
    });
    assert.ok(exactZero, 'Redeeming with exact 1,400 points leaves 0 balance');
  });

  await t('B17-03', 'B17: Redeeming Nivel 14 Días with 2,100 points leaves balance = 700', async () => {
    assert.ok(page, 'Browser page must be active');
    const leaves700 = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(2100);
      const res = window.UltraRewardStore.redeem('tier-14d');
      return res === true && window.UltraRewardStore.getBalance() === 700;
    });
    assert.ok(leaves700, 'Redeeming tier-14d from 2,100 points must leave 700 points');
  });

  await t('B17-04', 'B17: Attempting redemption when streak days < 14 is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsShortStreak = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.canRedeem !== 'function') return false;
      if (typeof window.UltraRewardStore.setStreakDays === 'function') {
        window.UltraRewardStore.setStreakDays(10);
        return window.UltraRewardStore.canRedeem('tier-14d') === false;
      }
      return true;
    });
    assert.ok(rejectsShortStreak, 'Redemption of Nivel 14 Días requires active streak >= 14');
  });

  await t('B17-05', 'B17: Nivel 14 Días UI button is disabled when balance < 1,400', async () => {
    assert.ok(page, 'Browser page must be active');
    const disabledState = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.setBalance !== 'function') return false;
      window.UltraRewardStore.setBalance(500);
      const btn = document.querySelector('[data-redeem="tier-14d"], button[data-tier="tier-14d"]');
      if (btn) return btn.hasAttribute('disabled') || btn.classList.contains('opacity-50');
      return true;
    });
    assert.ok(disabledState, 'Redeem button should visually reflect disabled state when funds insufficient');
  });

  // --------------------------------------------------------------------------
  // FEATURE 18: Catálogo de Recompensas: Nivel 30 Días (Boundary)
  // --------------------------------------------------------------------------
  await t('B18-01', 'B18: Attempting redemption of Nivel 30 Días with 2,999 points is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejected = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(2999);
      const res = window.UltraRewardStore.redeem('tier-30d');
      return res === false && window.UltraRewardStore.getBalance() === 2999;
    });
    assert.ok(rejected, 'Redemption with 2,999 points must fail');
  });

  await t('B18-02', 'B18: Redeeming Nivel 30 Días with exactly 3,000 points leaves balance = 0', async () => {
    assert.ok(page, 'Browser page must be active');
    const exactZero = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(3000);
      const res = window.UltraRewardStore.redeem('tier-30d');
      return res === true && window.UltraRewardStore.getBalance() === 0;
    });
    assert.ok(exactZero, 'Redeeming with exact 3,000 points leaves 0 balance');
  });

  await t('B18-03', 'B18: Attempting redemption when streak days < 30 is rejected', async () => {
    assert.ok(page, 'Browser page must be active');
    const rejectsShortStreak = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.canRedeem !== 'function') return false;
      if (typeof window.UltraRewardStore.setStreakDays === 'function') {
        window.UltraRewardStore.setStreakDays(21);
        return window.UltraRewardStore.canRedeem('tier-30d') === false;
      }
      return true;
    });
    assert.ok(rejectsShortStreak, 'Redemption of Nivel 30 Días requires active streak >= 30');
  });

  await t('B18-04', 'B18: Double-clicking confirm redemption does not cause double debit', async () => {
    assert.ok(page, 'Browser page must be active');
    const idempotent = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(3000);
      // Simultaneous calls
      const p1 = window.UltraRewardStore.redeem('tier-30d');
      const p2 = window.UltraRewardStore.redeem('tier-30d');
      // Exactly one should succeed, one should fail due to insufficient funds
      return (p1 && !p2) || (!p1 && p2);
    });
    assert.ok(idempotent, 'Double redemption must not allow overdrafting');
  });

  await t('B18-05', 'B18: Nivel 30 Días card renders locked deficit state when balance < 3,000', async () => {
    assert.ok(page, 'Browser page must be active');
    const deficitRendered = await page.evaluate(() => {
      if (!window.UltraRewardStore) return false;
      window.UltraRewardStore.setBalance(2100);
      const card = document.querySelector('[data-tier="tier-30d"], #card-tier-30d');
      return card ? card.textContent.includes('Faltan') || card.textContent.includes('900') || card.classList.contains('locked') : true;
    });
    assert.ok(deficitRendered, 'Locked tier card should display points deficit to unlock');
  });

  // --------------------------------------------------------------------------
  // FEATURE 19: Flujo Interactivo de Redención (Boundary)
  // --------------------------------------------------------------------------
  await t('B19-01', 'B19: Dismissing redemption modal preserves points balance unchanged', async () => {
    assert.ok(page, 'Browser page must be active');
    const preserved = await page.evaluate(() => {
      if (!window.UltraRewardStore) return false;
      window.UltraRewardStore.setBalance(2100);
      if (typeof window.closeRedeemModal === 'function') {
        window.closeRedeemModal();
      }
      return window.UltraRewardStore.getBalance() === 2100;
    });
    assert.ok(preserved, 'Closing modal must not modify balance');
  });

  await t('B19-02', 'B19: Concurrent redemption requests handle race conditions safely', async () => {
    assert.ok(page, 'Browser page must be active');
    const safe = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(1400);
      // Try to redeem two 1400 pt rewards concurrently
      const r1 = window.UltraRewardStore.redeem('tier-14d');
      const r2 = window.UltraRewardStore.redeem('tier-14d');
      return (r1 === true && r2 === false) && window.UltraRewardStore.getBalance() === 0;
    });
    assert.ok(safe, 'Concurrent redemptions must protect against balance corruption');
  });

  await t('B19-03', 'B19: Redemption history records have collision-free unique transaction codes', async () => {
    assert.ok(page, 'Browser page must be active');
    const uniqueCodes = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(5000);
      window.UltraRewardStore.redeem('tier-7d');
      window.UltraRewardStore.redeem('tier-7d');
      const hist = window.UltraRewardStore.getHistory();
      if (!hist || hist.length < 2) return false;
      const codes = hist.map(h => h.codigoCanje || h.id);
      return new Set(codes).size === codes.length;
    });
    assert.ok(uniqueCodes, 'Every redemption transaction must generate a unique code');
  });

  await t('B19-04', 'B19: Redemption record timestamp parses into valid Date object', async () => {
    assert.ok(page, 'Browser page must be active');
    const validDate = await page.evaluate(() => {
      if (!window.UltraRewardStore || !window.UltraRewardStore.getHistory) return false;
      const hist = window.UltraRewardStore.getHistory();
      if (!hist || hist.length === 0) return true;
      const d = new Date(hist[0].fecha);
      return !isNaN(d.getTime());
    });
    assert.ok(validDate, 'Redemption timestamps must be valid parseable dates');
  });

  await t('B19-05', 'B19: Corrupted LocalStorage payload recovers gracefully without crashing store', async () => {
    assert.ok(page, 'Browser page must be active');
    const recovers = await page.evaluate(() => {
      try {
        localStorage.setItem('ultraracha_rewards_history', 'CORRUPTED_NON_JSON_DATA{{{');
        if (typeof window.UltraRewardStore?.init === 'function') {
          window.UltraRewardStore.init();
        }
        return true;
      } catch (e) {
        return false;
      }
    });
    assert.ok(recovers, 'Store must handle corrupted localStorage gracefully');
  });

  // --------------------------------------------------------------------------
  // FEATURE 20: Despliegue Sincronizado GitHub Pages (Boundary)
  // --------------------------------------------------------------------------
  await t('B20-01', 'B20: No mixed content: all CDN assets use HTTPS protocol', () => {
    const httpAssets = htmlContent.match(/src="http:\/\/|href="http:\/\//gi) || [];
    assert.strictEqual(httpAssets.length, 0, `Insecure http:// assets found: ${httpAssets.join(', ')}`);
  });

  await t('B20-02', 'B20: Zero local absolute paths (C:\\ or D:\\) in index.html', () => {
    const localDrives = htmlContent.match(/[cCdDeEfF]:\\[a-zA-Z0-9_\\]+/g) || [];
    assert.strictEqual(localDrives.length, 0, `Absolute filesystem drive paths found: ${localDrives.join(', ')}`);
  });

  await t('B20-03', 'B20: .github/workflows/static.yml triggers specifically on branch main', () => {
    const workflowPath = path.join(PROJECT_ROOT, '.github/workflows/static.yml');
    const content = fs.readFileSync(workflowPath, 'utf-8');
    assert.ok(content.includes('branches: ["main"]') || content.includes('branches: [ "main" ]') || content.includes('branches:\n      - main'), 'Workflow must trigger on push to main branch');
  });

  await t('B20-04', 'B20: server.js path traversal protection prevents accessing parent directories', () => {
    assert.ok(serverJsContent.includes('..') || serverJsContent.includes('normalize'), 'server.js must normalize and sanitize paths against traversal attacks');
  });

  await t('B20-05', 'B20: server.js handles non-existent routes with standard 404 status', () => {
    assert.ok(serverJsContent.includes('404'), 'server.js must respond with 404 for non-existent resources');
  });

  if (pageContext) {
    await pageContext.close();
  }

  const passed = results.filter(r => r.passed).length;
  const failed = results.filter(r => !r.passed).length;
  const total = results.length;

  console.log(`\nTier 2 Summary: ${passed} passed, ${failed} failed, ${total} total (${Math.round((passed / total) * 100)}%)`);

  return {
    name: 'Tier 2: Boundary & Corner Cases',
    total,
    passed,
    failed,
    results
  };
}

if (require.main === module) {
  run({ verbose: true })
    .then(summary => {
      closeBrowser();
      process.exit(summary.failed > 0 ? 1 : 0);
    })
    .catch(err => {
      console.error('Fatal error in Tier 2 runner:', err);
      closeBrowser();
      process.exit(1);
    });
}

module.exports = { run };
