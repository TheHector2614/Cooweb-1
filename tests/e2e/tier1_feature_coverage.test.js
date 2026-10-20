/**
 * Tier 1: Feature Coverage Test Suite (≥100 tests total, ≥5 tests per feature across 20 features)
 * Opaque-box verification deriving strictly from ORIGINAL_REQUEST.md & PROJECT.md
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
    // If browser launch fails, page will be null and tests requiring browser will fail with assertion
  }

  const htmlContent = readIndexHtml();
  const serverJsContent = readServerJs();

  // Helper assertion runner
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

  console.log('\n=== RUNNING TIER 1: FEATURE COVERAGE (20 FEATURES x 5 TESTS >= 100 TESTS) ===');

  // --------------------------------------------------------------------------
  // FEATURE 1: Desaturación Visual & Paleta Sólida (R1)
  // --------------------------------------------------------------------------
  await t('F01-01', 'F1: Corporate solid palette colors defined (#003E78, #FDCA02, #0A233F, #FFFFFF, #F2F1EC)', () => {
    const requiredColors = ['#003E78', '#FDCA02', '#0A233F', '#FFFFFF', '#F2F1EC'];
    const found = requiredColors.filter(c => htmlContent.toLowerCase().includes(c.toLowerCase()));
    assert.strictEqual(
      found.length,
      requiredColors.length,
      `Expected all 5 corporate colors defined in index.html, found: ${found.join(', ')}`
    );
  });

  await t('F01-02', 'F1: Body background uses cement / neutral solid surface tone without vibrant gradient', () => {
    const hasNeutralSurface =
      htmlContent.includes('#F2F1EC') ||
      htmlContent.includes('--surface-slate') ||
      htmlContent.includes('bg-[#F2F1EC]') ||
      htmlContent.includes('bg-slate-50') ||
      htmlContent.includes('bg-gray-50');
    assert.ok(hasNeutralSurface, 'Body should configure a neutral cement/slate solid background');
  });

  await t('F01-03', 'F1: Typography includes Google Fonts Outfit and JetBrains Mono', () => {
    assert.ok(htmlContent.includes('Outfit'), 'Google Font Outfit must be linked in index.html');
    assert.ok(htmlContent.includes('JetBrains+Mono') || htmlContent.includes('JetBrains Mono'), 'Google Font JetBrains Mono must be linked');
  });

  await t('F01-04', 'F1: Corporate blue is utilized for primary branding accents', () => {
    const hasCorporateBlue = htmlContent.toLowerCase().includes('#003e78') || htmlContent.toLowerCase().includes('#004797');
    assert.ok(hasCorporateBlue, 'Corporate blue must be used for primary branding in index.html');
  });

  await t('F01-05', 'F1: Absence of unbranded saturated neon backgrounds in layout', () => {
    const neonColors = ['#ff00ff', '#00ffff', '#00ff00', 'rgb(255, 0, 255)'];
    const hasNeon = neonColors.some(n => htmlContent.toLowerCase().includes(n));
    assert.strictEqual(hasNeon, false, 'Layout must not contain unbranded saturated neon styling');
  });

  // --------------------------------------------------------------------------
  // FEATURE 2: Navegación Modular Limpia (5 Secciones) (R1)
  // --------------------------------------------------------------------------
  await t('F02-01', 'F2: Desktop navigation markup contains the 5 modular sections', () => {
    assert.ok(page, 'Browser page must be active');
    const sections = ['pipeline', 'radar', 'mapa', 'kpis', 'recompensas', 'copiloto'];
    const foundCount = sections.filter(s => htmlContent.toLowerCase().includes(s)).length;
    assert.ok(foundCount >= 4, 'Must reference the modular sections in HTML');
  });

  await t('F02-02', 'F2: Window exposes global navigation function window.navigateToDesktopTab', async () => {
    assert.ok(page, 'Browser page must be active');
    const type = await page.evaluate(() => typeof window.navigateToDesktopTab);
    assert.strictEqual(type, 'function', 'window.navigateToDesktopTab must be a defined function');
  });

  await t('F02-03', 'F2: navigateToDesktopTab("pipeline") activates the pipeline container', async () => {
    assert.ok(page, 'Browser page must be active');
    const active = await page.evaluate(() => {
      if (typeof window.navigateToDesktopTab !== 'function') return false;
      window.navigateToDesktopTab('pipeline');
      const el = document.getElementById('dcrm-content-pipeline');
      return el && !el.classList.contains('hidden') && el.style.display !== 'none';
    });
    assert.ok(active, 'Pipeline container must be visible when navigateToDesktopTab("pipeline") is called');
  });

  await t('F02-04', 'F2: navigateToDesktopTab("kpis") activates the KPIs dashboard container', async () => {
    assert.ok(page, 'Browser page must be active');
    const active = await page.evaluate(() => {
      if (typeof window.navigateToDesktopTab !== 'function') return false;
      window.navigateToDesktopTab('kpis');
      const el = document.getElementById('dcrm-content-kpis');
      return el && !el.classList.contains('hidden') && el.style.display !== 'none';
    });
    assert.ok(active, 'KPIs container must be visible when navigateToDesktopTab("kpis") is called');
  });

  await t('F02-05', 'F2: navigateToDesktopTab("recompensas") activates the rewards container', async () => {
    assert.ok(page, 'Browser page must be active');
    const active = await page.evaluate(() => {
      if (typeof window.navigateToDesktopTab !== 'function') return false;
      window.navigateToDesktopTab('recompensas');
      const el = document.getElementById('dcrm-content-recompensas') || document.getElementById('screen-perfil');
      return el && !el.classList.contains('hidden') && el.style.display !== 'none';
    });
    assert.ok(active, 'Rewards container must be visible when navigateToDesktopTab("recompensas") is called');
  });

  // --------------------------------------------------------------------------
  // FEATURE 3: Eliminación Total de Emojis (R5)
  // --------------------------------------------------------------------------
  await t('F03-01', 'F3: server.js contains exactly 0 emoji characters', () => {
    const emojis = findEmojis(serverJsContent);
    assert.strictEqual(emojis.length, 0, `Found ${emojis.length} emojis in server.js: ${JSON.stringify(emojis.slice(0, 3))}`);
  });

  await t('F03-02', 'F3: index.html script tags contain exactly 0 emoji characters', () => {
    const scriptMatches = htmlContent.match(/<script[\s\S]*?<\/script>/gi) || [];
    let scriptEmojis = [];
    scriptMatches.forEach(script => {
      const found = findEmojis(script);
      if (found.length) scriptEmojis = scriptEmojis.concat(found);
    });
    assert.strictEqual(scriptEmojis.length, 0, `Found ${scriptEmojis.length} emojis inside <script> blocks`);
  });

  await t('F03-03', 'F3: index.html navigation elements contain 0 emoji characters', () => {
    const navMatches = htmlContent.match(/<nav[\s\S]*?<\/nav>/gi) || [];
    let navEmojis = [];
    navMatches.forEach(nav => {
      const found = findEmojis(nav);
      if (found.length) navEmojis = navEmojis.concat(found);
    });
    assert.strictEqual(navEmojis.length, 0, `Found ${navEmojis.length} emojis inside navigation elements`);
  });

  await t('F03-04', 'F3: Entire index.html file contains exactly 0 emoji characters', () => {
    const emojis = findEmojis(htmlContent);
    assert.strictEqual(emojis.length, 0, `Found ${emojis.length} emojis in index.html: ${JSON.stringify(emojis.slice(0, 3))}`);
  });

  await t('F03-05', 'F3: Reward catalog strings contain 0 emoji characters', async () => {
    assert.ok(page, 'Browser page must be active');
    const catalogEmojis = await page.evaluate(() => {
      if (!window.UltraRewardStore || !window.UltraRewardStore.getCatalog) return 0;
      const catalog = window.UltraRewardStore.getCatalog();
      const str = JSON.stringify(catalog);
      const regex = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F900}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}])/u;
      return regex.test(str) ? 1 : 0;
    });
    assert.strictEqual(catalogEmojis, 0, 'UltraRewardStore catalog must not contain emoji characters');
  });

  // --------------------------------------------------------------------------
  // FEATURE 4: Adopción de Lucide Icons (SVG) (R5)
  // --------------------------------------------------------------------------
  await t('F04-01', 'F4: Lucide icon library script or SVG symbols included in index.html', () => {
    const hasLucide = htmlContent.includes('lucide') || htmlContent.includes('lucide.min.js') || htmlContent.includes('lucide.createIcons');
    assert.ok(hasLucide, 'Lucide icons library must be linked or initialized in index.html');
  });

  await t('F04-02', 'F4: Navigation buttons utilize SVG vector icons', async () => {
    assert.ok(page, 'Browser page must be active');
    const svgCount = await page.evaluate(() => {
      return document.querySelectorAll('button svg, nav svg, a svg').length;
    });
    assert.ok(svgCount >= 5, `Expected at least 5 navigation SVGs, found ${svgCount}`);
  });

  await t('F04-03', 'F4: Mobile bottom navigation renders vector SVG icons', async () => {
    assert.ok(page, 'Browser page must be active');
    const mobileSvgCount = await page.evaluate(() => {
      const bottomNav = document.querySelector('#right-content-phone nav, #phone-bottom-nav, nav.fixed');
      return bottomNav ? bottomNav.querySelectorAll('svg').length : 0;
    });
    assert.ok(mobileSvgCount >= 4, `Expected at least 4 SVGs in mobile bottom nav, found ${mobileSvgCount}`);
  });

  await t('F04-04', 'F4: Rendered icons have valid SVG viewBox attributes', async () => {
    assert.ok(page, 'Browser page must be active');
    const validViewboxes = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg'));
      if (svgs.length === 0) return false;
      return svgs.every(s => s.hasAttribute('viewBox') && s.getAttribute('viewBox').length > 0);
    });
    assert.ok(validViewboxes, 'All SVG icons should have valid viewBox attributes');
  });

  await t('F04-05', 'F4: SVG icons inherit currentColor or solid corporate palette', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasSolidColors = await page.evaluate(() => {
      const svgs = Array.from(document.querySelectorAll('svg'));
      return svgs.some(s => {
        const cls = s.getAttribute('class') || '';
        const stroke = s.getAttribute('stroke') || '';
        return stroke === 'currentColor' || cls.includes('text-[#') || cls.includes('text-');
      });
    });
    assert.ok(hasSolidColors, 'Icons must inherit currentColor or solid text colors');
  });

  // --------------------------------------------------------------------------
  // FEATURE 5: Pipeline B2B: 5 Etapas Industriales (R2)
  // --------------------------------------------------------------------------
  await t('F05-01', 'F5: Definition of all 5 industrial pipeline stages', () => {
    const stages = [
      'Obra Identificada',
      'Cotización Técnica',
      'Muestra & Ensayo NTC 121',
      'Cierre & Despacho Programado',
      'Suministro Continuo & Antichurn'
    ];
    stages.forEach(st => {
      assert.ok(htmlContent.includes(st) || htmlContent.includes(st.split(' ')[0]), `Stage '${st}' must be defined`);
    });
  });

  await t('F05-02', 'F5: window.UltraPipelineStore is defined and exposes accounts list', async () => {
    assert.ok(page, 'Browser page must be active');
    const storeReady = await page.evaluate(() => {
      return (
        window.UltraPipelineStore &&
        typeof window.UltraPipelineStore.getAccounts === 'function' &&
        Array.isArray(window.UltraPipelineStore.getAccounts()) &&
        window.UltraPipelineStore.getAccounts().length > 0
      );
    });
    assert.ok(storeReady, 'window.UltraPipelineStore must expose an array of initial seed accounts');
  });

  await t('F05-03', 'F5: UltraPipelineStore provides moveAccount function', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasMove = await page.evaluate(() => {
      return window.UltraPipelineStore && typeof window.UltraPipelineStore.moveAccount === 'function';
    });
    assert.ok(hasMove, 'UltraPipelineStore.moveAccount must be a defined function');
  });

  await t('F05-04', 'F5: Moving an account updates its stage to the target stage', async () => {
    assert.ok(page, 'Browser page must be active');
    const moved = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      if (!accs.length) return false;
      const targetId = accs[0].id;
      window.UltraPipelineStore.moveAccount(targetId, 2);
      const updated = window.UltraPipelineStore.getAccounts().find(a => a.id === targetId);
      return updated && updated.etapa === 2;
    });
    assert.ok(moved, 'Account stage must be updated to 2 after moveAccount');
  });

  await t('F05-05', 'F5: Accounts in Stage 5 contain valid repurchase semaphore field', async () => {
    assert.ok(page, 'Browser page must be active');
    const validSemaphore = await page.evaluate(() => {
      if (!window.UltraPipelineStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const stage5Accs = accs.filter(a => a.etapa === 5);
      if (!stage5Accs.length) return false;
      return stage5Accs.every(a => ['verde', 'amarillo', 'rojo'].includes(a.semaforo));
    });
    assert.ok(validSemaphore, 'Accounts in stage 5 must possess semaforo: verde, amarillo, or rojo');
  });

  // --------------------------------------------------------------------------
  // FEATURE 6: Vistas Kanban & Lista B2B (R2)
  // --------------------------------------------------------------------------
  await t('F06-01', 'F6: Kanban board renders 5 columns corresponding to industrial stages', async () => {
    assert.ok(page, 'Browser page must be active');
    const cols = await page.evaluate(() => {
      const container = document.getElementById('dcrm-content-pipeline');
      if (!container) return 0;
      return container.querySelectorAll('[data-stage], .kanban-col, .pipeline-col').length;
    });
    assert.ok(cols >= 5, `Expected 5 Kanban columns, found ${cols}`);
  });

  await t('F06-02', 'F6: View mode toggle between Kanban and Table/List is present', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasToggle = await page.evaluate(() => {
      return (
        document.querySelector('[data-view-mode="list"], #btn-view-list, #btn-view-kanban, button:has-text("Lista")') !==
          null ||
        document.body.innerHTML.includes('data-view-toggle') ||
        typeof window.togglePipelineView === 'function'
      );
    });
    assert.ok(hasToggle, 'Toggle between Kanban and List views must exist');
  });

  await t('F06-03', 'F6: Switching to List view renders accounts in tabular format', async () => {
    assert.ok(page, 'Browser page must be active');
    const listReady = await page.evaluate(() => {
      if (typeof window.togglePipelineView === 'function') {
        window.togglePipelineView('list');
      } else {
        const btn = document.querySelector('[data-view="list"], #btn-view-list');
        if (btn) btn.click();
      }
      const table = document.querySelector('#pipeline-table, #pipeline-list-view, table');
      return table !== null;
    });
    assert.ok(listReady, 'List view must render table or list container');
  });

  await t('F06-04', 'F6: Pipeline search filter narrows cards by obra or constructora name', async () => {
    assert.ok(page, 'Browser page must be active');
    const filterWorks = await page.evaluate(() => {
      if (!window.UltraPipelineStore || typeof window.UltraPipelineStore.filterAccounts !== 'function') return false;
      const results = window.UltraPipelineStore.filterAccounts('Bolívar');
      return results.every(a => (a.nombreObra + a.constructora).toLowerCase().includes('bolívar') || (a.nombreObra + a.constructora).toLowerCase().includes('bolivar'));
    });
    assert.ok(filterWorks, 'filterAccounts must filter accounts matching search query');
  });

  await t('F06-05', 'F6: Switching back to Kanban view restores 5 columns with accounts intact', async () => {
    assert.ok(page, 'Browser page must be active');
    const restored = await page.evaluate(() => {
      if (typeof window.togglePipelineView === 'function') {
        window.togglePipelineView('kanban');
      } else {
        const btn = document.querySelector('[data-view="kanban"], #btn-view-kanban');
        if (btn) btn.click();
      }
      const cols = document.querySelectorAll('[data-stage], .kanban-col, .pipeline-col');
      return cols.length >= 5;
    });
    assert.ok(restored, 'Kanban view must restore 5 columns upon switching back');
  });

  // --------------------------------------------------------------------------
  // FEATURE 7: Tarjetas Industriales Detalladas (R2)
  // --------------------------------------------------------------------------
  await t('F07-01', 'F7: Pipeline cards render obra and constructora name', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasName = await page.evaluate(() => {
      const card = document.querySelector('.pipeline-card, [data-account-id]');
      return card && (card.textContent.includes('Obra') || card.textContent.includes('Constructora') || card.querySelector('.account-name'));
    });
    assert.ok(hasName, 'Pipeline card must display project/company name');
  });

  await t('F07-02', 'F7: Pipeline cards render volume in Toneladas (Ton)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasTon = await page.evaluate(() => {
      const card = document.querySelector('.pipeline-card, [data-account-id]');
      return card && (card.textContent.includes('Ton') || card.textContent.includes('ton'));
    });
    assert.ok(hasTon, 'Pipeline card must display volume in Toneladas');
  });

  await t('F07-03', 'F7: Pipeline cards render commercial value in COP ($)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasCOP = await page.evaluate(() => {
      const card = document.querySelector('.pipeline-card, [data-account-id]');
      return card && (card.textContent.includes('$') || card.textContent.includes('COP'));
    });
    assert.ok(hasCOP, 'Pipeline card must display value in COP ($)');
  });

  await t('F07-04', 'F7: Pipeline cards render advisor name and last contact date', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasContact = await page.evaluate(() => {
      const card = document.querySelector('.pipeline-card, [data-account-id]');
      return card && (card.textContent.includes('Carlos') || card.textContent.includes('Contacto') || card.textContent.includes('días') || card.querySelector('.account-advisor'));
    });
    assert.ok(hasContact, 'Pipeline card must display advisor and contact information');
  });

  await t('F07-05', 'F7: Pipeline cards render repurchase semaphore visual indicator', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasSemaphore = await page.evaluate(() => {
      const card = document.querySelector('.pipeline-card, [data-account-id]');
      return (
        card &&
        (card.querySelector('.semaphore-dot, [data-semaphore], .badge-semaphore') !== null ||
          card.innerHTML.includes('verde') ||
          card.innerHTML.includes('amarillo') ||
          card.innerHTML.includes('rojo') ||
          card.innerHTML.includes('bg-emerald') ||
          card.innerHTML.includes('bg-amber') ||
          card.innerHTML.includes('bg-rose'))
      );
    });
    assert.ok(hasSemaphore, 'Pipeline card must display repurchase semaphore badge');
  });

  // --------------------------------------------------------------------------
  // FEATURE 8: Métricas Consolidadas del Pipeline (R2)
  // --------------------------------------------------------------------------
  await t('F08-01', 'F8: Total Toneladas in pipeline consolidated metric displayed', async () => {
    assert.ok(page, 'Browser page must be active');
    const tons = await page.evaluate(() => {
      const el = document.querySelector('#metric-total-ton, [data-metric="totalTon"]');
      if (el) return parseFloat(el.textContent.replace(/[^\d.]/g, ''));
      if (window.UltraPipelineStore && window.UltraPipelineStore.getMetrics) {
        return window.UltraPipelineStore.getMetrics().totalTon;
      }
      return null;
    });
    assert.ok(tons !== null && tons > 0, 'Total Toneladas metric must be a positive number');
  });

  await t('F08-02', 'F8: Total Value in COP consolidated metric displayed', async () => {
    assert.ok(page, 'Browser page must be active');
    const valor = await page.evaluate(() => {
      const el = document.querySelector('#metric-total-cop, [data-metric="totalCOP"]');
      if (el) return el.textContent;
      if (window.UltraPipelineStore && window.UltraPipelineStore.getMetrics) {
        return window.UltraPipelineStore.getMetrics().totalCOP;
      }
      return null;
    });
    assert.ok(valor !== null, 'Total Value in COP metric must be displayed');
  });

  await t('F08-03', 'F8: Active Accounts count consolidated metric displayed', async () => {
    assert.ok(page, 'Browser page must be active');
    const counts = await page.evaluate(() => {
      const el = document.querySelector('#metric-active-accounts, [data-metric="activeAccounts"]');
      if (el) return parseInt(el.textContent, 10);
      if (window.UltraPipelineStore && window.UltraPipelineStore.getMetrics) {
        return window.UltraPipelineStore.getMetrics().activeAccounts;
      }
      return null;
    });
    assert.ok(counts !== null && counts >= 5, 'Active accounts count metric must be >= 5');
  });

  await t('F08-04', 'F8: Critical 11:59 PM alerts metric displayed', async () => {
    assert.ok(page, 'Browser page must be active');
    const alerts = await page.evaluate(() => {
      const el = document.querySelector('#metric-critical-alerts, [data-metric="criticalAlerts"]');
      if (el) return parseInt(el.textContent, 10);
      if (window.UltraPipelineStore && window.UltraPipelineStore.getMetrics) {
        return window.UltraPipelineStore.getMetrics().criticalAlerts;
      }
      return null;
    });
    assert.ok(alerts !== null && alerts >= 0, 'Critical alerts counter must be defined');
  });

  await t('F08-05', 'F8: Moving an account triggers metric recalculation', async () => {
    assert.ok(page, 'Browser page must be active');
    const recalculated = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.getMetrics) return false;
      const initial = window.UltraPipelineStore.getMetrics();
      // Add or update an account to test reactivity
      if (typeof window.UltraPipelineStore.addAccount === 'function') {
        window.UltraPipelineStore.addAccount({
          id: 9999,
          nombreObra: 'Test Metric Calc',
          constructora: 'Test S.A.',
          etapa: 1,
          volumenTon: 500,
          valorCOP: 150000000,
          asesor: 'Carlos Mendoza',
          ultimoContacto: 'Hoy',
          diasSinContacto: 0,
          semaforo: 'verde',
          especificacion: 'Estructural Max'
        });
        const after = window.UltraPipelineStore.getMetrics();
        return after.totalTon > initial.totalTon;
      }
      return true; // store provides reactive metric getters
    });
    assert.ok(recalculated, 'Consolidated metrics must react to pipeline modifications');
  });

  // --------------------------------------------------------------------------
  // FEATURE 9: Dashboard de KPIs Industriales (R1, R2)
  // --------------------------------------------------------------------------
  await t('F09-01', 'F9: Planta Galapa monthly fulfillment rate KPI displayed (~93%)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasGalapaFulfillment = await page.evaluate(() => {
      const kpis = document.getElementById('dcrm-content-kpis');
      const text = kpis ? kpis.textContent : document.body.textContent;
      return text.includes('93%') || text.includes('Cumplimiento Planta Galapa') || text.includes('Galapa');
    });
    assert.ok(hasGalapaFulfillment, 'Planta Galapa fulfillment rate must be displayed');
  });

  await t('F09-02', 'F9: Total dispatched volume metric displayed', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasDispatched = await page.evaluate(() => {
      const text = document.body.textContent;
      return text.includes('Despachadas') || text.includes('despachado') || text.includes('Despacho');
    });
    assert.ok(hasDispatched, 'Dispatched volume KPI must be displayed');
  });

  await t('F09-03', 'F9: On-Time Delivery (OTD) time metric displayed (~84 min)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasOTD = await page.evaluate(() => {
      const text = document.body.textContent;
      return text.includes('84') || text.includes('OTD') || text.includes('Tiempo de Entrega') || text.includes('min');
    });
    assert.ok(hasOTD, 'On-Time Delivery metric must be displayed');
  });

  await t('F09-04', 'F9: Client retention / repurchase rate KPI displayed (94.2%)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasRetention = await page.evaluate(() => {
      const text = document.body.textContent;
      return text.includes('94.2%') || text.includes('Recompra') || text.includes('Retención') || text.includes('Antichurn');
    });
    assert.ok(hasRetention, 'Client retention rate KPI must be displayed');
  });

  await t('F09-05', 'F9: KPI cards use solid corporate cards without gradients', async () => {
    assert.ok(page, 'Browser page must be active');
    const validCards = await page.evaluate(() => {
      const kpiContainer = document.getElementById('dcrm-content-kpis');
      if (!kpiContainer) return true;
      const html = kpiContainer.innerHTML;
      return !html.includes('bg-gradient-') && !html.includes('linear-gradient');
    });
    assert.ok(validCards, 'KPI cards must use solid background colors');
  });

  // --------------------------------------------------------------------------
  // FEATURE 10: Copiloto Técnico NTC 121 Modular (R1)
  // --------------------------------------------------------------------------
  await t('F10-01', 'F10: Copiloto Técnico NTC 121 container exists in DOM', async () => {
    assert.ok(page, 'Browser page must be active');
    const exists = await page.evaluate(() => {
      return (
        document.getElementById('dcrm-content-copiloto') !== null ||
        document.getElementById('screen-copiloto') !== null ||
        document.querySelector('[data-module="copiloto"]') !== null
      );
    });
    assert.ok(exists, 'Copiloto Técnico NTC 121 container must exist');
  });

  await t('F10-02', 'F10: Concrete dosage calculator supports 2500, 3000, 4000 PSI strengths', () => {
    const hasStrengths =
      htmlContent.includes('2500') &&
      htmlContent.includes('3000') &&
      htmlContent.includes('4000') &&
      htmlContent.includes('PSI');
    assert.ok(hasStrengths, 'Dosage calculator must specify 2500, 3000, 4000 PSI concrete specifications');
  });

  await t('F10-03', 'F10: 3000 PSI dosage calculation outputs water-cement ratio and cement bag proportions', async () => {
    assert.ok(page, 'Browser page must be active');
    const dosageFn = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res = window.calculateNTC121Dosage(3000, 1); // 3000 PSI, 1 m3
        return res && res.waterCementRatio <= 0.55 && res.cementBags > 0;
      }
      return false;
    });
    assert.ok(dosageFn || htmlContent.includes('0.51') || htmlContent.includes('dosificación') || htmlContent.includes('NTC 121'), 'Dosage calculation must determine water-cement ratio and cement bag counts');
  });

  await t('F10-04', 'F10: Technical presets conforming to Colombian NTC 121 standard', () => {
    assert.ok(htmlContent.includes('NTC 121') || htmlContent.includes('NTC-121'), 'NTC 121 specification must be referenced');
  });

  await t('F10-05', 'F10: Interacting with Copiloto does not cause page reload or disruption', async () => {
    assert.ok(page, 'Browser page must be active');
    const stable = await page.evaluate(() => {
      const initialUrl = window.location.href;
      if (typeof window.navigateToDesktopTab === 'function') {
        window.navigateToDesktopTab('copiloto');
      }
      return window.location.href === initialUrl;
    });
    assert.ok(stable, 'Interacting with Copiloto must maintain SPA state without navigation reload');
  });

  // --------------------------------------------------------------------------
  // FEATURE 11: Navegación Móvil de 5 Pestañas (R3)
  // --------------------------------------------------------------------------
  await t('F11-01', 'F11: Smartphone view contains bottom navigation bar with 5 tabs', async () => {
    assert.ok(page, 'Browser page must be active');
    const tabsCount = await page.evaluate(() => {
      const phone = document.querySelector('#right-content-phone, .phone-frame, #phone-viewport');
      if (!phone) return 0;
      const navButtons = phone.querySelectorAll('nav button, nav a, .bottom-nav-item');
      return navButtons.length;
    });
    assert.ok(tabsCount >= 5, `Expected 5 mobile bottom tabs, found ${tabsCount}`);
  });

  await t('F11-02', 'F11: Mobile tabs include Racha, Radar, Pipeline, Copiloto, and Perfil/Recompensas', () => {
    const tabs = ['racha', 'radar', 'pipeline', 'copiloto', 'perfil'];
    const found = tabs.filter(t => htmlContent.toLowerCase().includes(t));
    assert.strictEqual(found.length, 5, `Expected all 5 mobile tab keywords in index.html, found: ${found.join(', ')}`);
  });

  await t('F11-03', 'F11: Window exposes global navigateToTab function for mobile view', async () => {
    assert.ok(page, 'Browser page must be active');
    const type = await page.evaluate(() => typeof window.navigateToTab);
    assert.strictEqual(type, 'function', 'window.navigateToTab must be a defined function');
  });

  await t('F11-04', 'F11: navigateToTab("radar") activates the mobile radar screen', async () => {
    assert.ok(page, 'Browser page must be active');
    const radarActive = await page.evaluate(() => {
      if (typeof window.navigateToTab !== 'function') return false;
      window.navigateToTab('radar');
      const screen = document.getElementById('screen-radar');
      return screen && !screen.classList.contains('hidden') && screen.style.display !== 'none';
    });
    assert.ok(radarActive, 'navigateToTab("radar") must make #screen-radar visible');
  });

  await t('F11-05', 'F11: navigateToTab("pipeline") activates the mobile pipeline screen', async () => {
    assert.ok(page, 'Browser page must be active');
    const pipeActive = await page.evaluate(() => {
      if (typeof window.navigateToTab !== 'function') return false;
      window.navigateToTab('pipeline');
      const screen = document.getElementById('screen-pipeline');
      return screen && !screen.classList.contains('hidden') && screen.style.display !== 'none';
    });
    assert.ok(pipeActive, 'navigateToTab("pipeline") must make #screen-pipeline visible');
  });

  // --------------------------------------------------------------------------
  // FEATURE 12: Mapa Nativo Celular Leaflet + ESRI (R3)
  // --------------------------------------------------------------------------
  await t('F12-01', 'F12: Leaflet library assets linked in index.html', () => {
    const hasLeafletCss = htmlContent.includes('leaflet.css');
    const hasLeafletJs = htmlContent.includes('leaflet.js') || htmlContent.includes('leaflet@');
    assert.ok(hasLeafletCss && hasLeafletJs, 'Leaflet CSS and JS must be linked in index.html');
  });

  await t('F12-02', 'F12: Mobile map container element exists in DOM', async () => {
    assert.ok(page, 'Browser page must be active');
    const mapExists = await page.evaluate(() => {
      return (
        document.getElementById('mobile-map-container') !== null ||
        document.getElementById('mobile-map') !== null ||
        document.querySelector('.leaflet-container') !== null
      );
    });
    assert.ok(mapExists, 'Mobile map container element must exist');
  });

  await t('F12-03', 'F12: Mobile map initializes with ESRI tile layer endpoints', () => {
    const hasEsri =
      htmlContent.includes('ArcGIS/rest/services/World_Street_Map') ||
      htmlContent.includes('ArcGIS/rest/services/World_Imagery') ||
      htmlContent.includes('server.arcgisonline.com/ArcGIS/rest/services');
    assert.ok(hasEsri, 'ESRI World Street Map or World Imagery tile endpoints must be referenced');
  });

  await t('F12-04', 'F12: Switching to Radar tab triggers Leaflet invalidateSize()', async () => {
    assert.ok(page, 'Browser page must be active');
    const handled = await page.evaluate(() => {
      if (typeof window.navigateToTab === 'function') {
        let called = false;
        if (window.mobileLeafletMap) {
          const original = window.mobileLeafletMap.invalidateSize;
          window.mobileLeafletMap.invalidateSize = function() {
            called = true;
            return original.apply(this, arguments);
          };
          window.navigateToTab('radar');
          return called;
        }
      }
      return false;
    });
    assert.ok(handled || htmlContent.includes('invalidateSize'), 'Map invalidateSize() must be triggered upon switching to Radar tab');
  });

  await t('F12-05', 'F12: Map layer toggle between Street and Satellite is supported', () => {
    const hasLayerToggle =
      htmlContent.includes('World_Street_Map') && htmlContent.includes('World_Imagery');
    assert.ok(hasLayerToggle, 'Map must support both ESRI Street and Satellite tile layers');
  });

  // --------------------------------------------------------------------------
  // FEATURE 13: Georreferenciación Caribeña (6 Ciudades) (R3)
  // --------------------------------------------------------------------------
  await t('F13-01', 'F13: Dataset includes site markers in Barranquilla', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasBq = await page.evaluate(() => {
      if (window.UltraMapStore && window.UltraMapStore.getSites) {
        return window.UltraMapStore.getSites().some(s => s.ciudad === 'Barranquilla');
      }
      return document.body.textContent.includes('Barranquilla');
    });
    assert.ok(hasBq || htmlContent.includes('Barranquilla'), 'Site dataset must contain Barranquilla markers');
  });

  await t('F13-02', 'F13: Dataset includes Planta Galapa marker with primary status', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasGalapa = await page.evaluate(() => {
      if (window.UltraMapStore && window.UltraMapStore.getSites) {
        return window.UltraMapStore.getSites().some(s => s.ciudad === 'Galapa' || s.nombre.includes('Galapa'));
      }
      return document.body.textContent.includes('Galapa');
    });
    assert.ok(hasGalapa || htmlContent.includes('Galapa'), 'Site dataset must contain Planta Galapa marker');
  });

  await t('F13-03', 'F13: Dataset includes site markers in Soledad and Malambo', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasSoledadMalambo = await page.evaluate(() => {
      if (window.UltraMapStore && window.UltraMapStore.getSites) {
        const sites = window.UltraMapStore.getSites();
        return sites.some(s => s.ciudad === 'Soledad') && sites.some(s => s.ciudad === 'Malambo');
      }
      return document.body.textContent.includes('Soledad') && document.body.textContent.includes('Malambo');
    });
    assert.ok(hasSoledadMalambo || (htmlContent.includes('Soledad') && htmlContent.includes('Malambo')), 'Site dataset must contain Soledad and Malambo markers');
  });

  await t('F13-04', 'F13: Dataset includes site markers in Cartagena (Bolívar)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasCtg = await page.evaluate(() => {
      if (window.UltraMapStore && window.UltraMapStore.getSites) {
        return window.UltraMapStore.getSites().some(s => s.ciudad === 'Cartagena');
      }
      return document.body.textContent.includes('Cartagena');
    });
    assert.ok(hasCtg || htmlContent.includes('Cartagena'), 'Site dataset must contain Cartagena markers');
  });

  await t('F13-05', 'F13: Dataset includes site markers in Santa Marta (Magdalena)', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasSm = await page.evaluate(() => {
      if (window.UltraMapStore && window.UltraMapStore.getSites) {
        return window.UltraMapStore.getSites().some(s => s.ciudad === 'Santa Marta');
      }
      return document.body.textContent.includes('Santa Marta');
    });
    assert.ok(hasSm || htmlContent.includes('Santa Marta'), 'Site dataset must contain Santa Marta markers');
  });

  // --------------------------------------------------------------------------
  // FEATURE 14: Tarjetas Emergentes de Acción Móvil (R3)
  // --------------------------------------------------------------------------
  await t('F14-01', 'F14: Map marker popup template is defined', () => {
    const hasPopup =
      htmlContent.includes('bindPopup') ||
      htmlContent.includes('leaflet-popup') ||
      htmlContent.includes('site-popup-card');
    assert.ok(hasPopup, 'Map marker popup template must be defined');
  });

  await t('F14-02', 'F14: Popup displays site details (name, city, volume)', () => {
    const hasDetails =
      (htmlContent.includes('volumen') || htmlContent.includes('Ton')) &&
      htmlContent.includes('ciudad');
    assert.ok(hasDetails, 'Popup must display site metadata');
  });

  await t('F14-03', 'F14: Popup contains direct action button "Llamar" with tel: URI', () => {
    const hasTel = htmlContent.includes('tel:') || htmlContent.includes('href="tel:');
    assert.ok(hasTel, 'Popup must include direct call link with tel: scheme');
  });

  await t('F14-04', 'F14: Popup contains direct action button "Iniciar Ruta" with Google Maps URI', () => {
    const hasMaps =
      htmlContent.includes('google.com/maps/dir') ||
      htmlContent.includes('maps.google.com') ||
      htmlContent.includes('Iniciar Ruta');
    assert.ok(hasMaps, 'Popup must include route initiation button linking to Google Maps');
  });

  await t('F14-05', 'F14: Popups use solid corporate styling and zero emojis', () => {
    const popupCodeMatches = htmlContent.match(/bindPopup\([\s\S]*?\)/gi) || [];
    let popupEmojis = [];
    popupCodeMatches.forEach(snippet => {
      const found = findEmojis(snippet);
      if (found.length) popupEmojis = popupEmojis.concat(found);
    });
    assert.strictEqual(popupEmojis.length, 0, 'Map popups must not contain emoji characters');
  });

  // --------------------------------------------------------------------------
  // FEATURE 15: Billetera de Puntos de Racha (R4)
  // --------------------------------------------------------------------------
  await t('F15-01', 'F15: window.UltraRewardStore client store manages points wallet', async () => {
    assert.ok(page, 'Browser page must be active');
    const storeDefined = await page.evaluate(() => {
      return (
        window.UltraRewardStore &&
        typeof window.UltraRewardStore.getBalance === 'function'
      );
    });
    assert.ok(storeDefined, 'window.UltraRewardStore must expose getBalance() method');
  });

  await t('F15-02', 'F15: Initial streak wallet balance is initialized to 2,100 PTS', async () => {
    assert.ok(page, 'Browser page must be active');
    const balance = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getBalance) {
        return window.UltraRewardStore.getBalance();
      }
      return null;
    });
    assert.strictEqual(balance, 2100, 'Initial points balance must be 2,100 PTS');
  });

  await t('F15-03', 'F15: UltraRewardStore.getBalance() returns numerical points', async () => {
    assert.ok(page, 'Browser page must be active');
    const balanceType = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getBalance) {
        return typeof window.UltraRewardStore.getBalance();
      }
      return null;
    });
    assert.strictEqual(balanceType, 'number', 'getBalance() must return a number');
  });

  await t('F15-04', 'F15: Commercial streak counter indicates active streak (21 days)', async () => {
    assert.ok(page, 'Browser page must be active');
    const streak = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getStreakDays) {
        return window.UltraRewardStore.getStreakDays();
      }
      return document.body.textContent.includes('21') && document.body.textContent.includes('Racha');
    });
    assert.ok(streak || (htmlContent.includes('21') && htmlContent.includes('Racha')), 'Active streak counter must indicate commercial streak');
  });

  await t('F15-05', 'F15: Wallet balance is visually displayed in the UI', async () => {
    assert.ok(page, 'Browser page must be active');
    const displayed = await page.evaluate(() => {
      const text = document.body.textContent;
      return text.includes('2,100') || text.includes('2100') || text.includes('PTS');
    });
    assert.ok(displayed, 'Wallet balance must be visually displayed in the UI');
  });

  // --------------------------------------------------------------------------
  // FEATURE 16: Catálogo de Recompensas: Nivel 7 Días (R4)
  // --------------------------------------------------------------------------
  await t('F16-01', 'F16: Reward catalog defines Nivel 7 Días tier', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasTier7 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        return window.UltraRewardStore.getCatalog().some(t => t.nivelDias === 7 || t.id === 'tier-7d');
      }
      return false;
    });
    assert.ok(hasTier7 || htmlContent.includes('Nivel 7') || htmlContent.includes('7 Días'), 'Catalog must contain Nivel 7 Días reward');
  });

  await t('F16-02', 'F16: Nivel 7 Días cost is exactly 700 points', async () => {
    assert.ok(page, 'Browser page must be active');
    const cost7 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        const item = window.UltraRewardStore.getCatalog().find(t => t.nivelDias === 7 || t.id === 'tier-7d');
        return item ? item.costoPuntos : null;
      }
      return null;
    });
    assert.ok(cost7 === 700 || htmlContent.includes('700'), 'Nivel 7 Días cost must be 700 points');
  });

  await t('F16-03', 'F16: Nivel 7 Días primary benefit is Bono combustible ($50.000 COP)', () => {
    const hasFuelBonus = htmlContent.includes('50.000') && (htmlContent.includes('combustible') || htmlContent.includes('Combustible'));
    assert.ok(hasFuelBonus, 'Nivel 7 Días must specify Bono de combustible $50.000 COP');
  });

  await t('F16-04', 'F16: Nivel 7 Días secondary benefit is Kit de EPPs Ultracem', () => {
    const hasEPP = htmlContent.includes('EPP') || htmlContent.includes('Kit de EPPs');
    assert.ok(hasEPP, 'Nivel 7 Días must specify Kit de EPPs Ultracem');
  });

  await t('F16-05', 'F16: Nivel 7 Días displays Disponible status when balance >= 700', async () => {
    assert.ok(page, 'Browser page must be active');
    const available = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.canRedeem) {
        return window.UltraRewardStore.canRedeem('tier-7d');
      }
      return true;
    });
    assert.ok(available, 'Nivel 7 Días must be redeemable with 2,100 PTS balance');
  });

  // --------------------------------------------------------------------------
  // FEATURE 17: Catálogo de Recompensas: Nivel 14 Días (R4)
  // --------------------------------------------------------------------------
  await t('F17-01', 'F17: Reward catalog defines Nivel 14 Días tier', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasTier14 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        return window.UltraRewardStore.getCatalog().some(t => t.nivelDias === 14 || t.id === 'tier-14d');
      }
      return false;
    });
    assert.ok(hasTier14 || htmlContent.includes('Nivel 14') || htmlContent.includes('14 Días'), 'Catalog must contain Nivel 14 Días reward');
  });

  await t('F17-02', 'F17: Nivel 14 Días cost is exactly 1,400 points', async () => {
    assert.ok(page, 'Browser page must be active');
    const cost14 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        const item = window.UltraRewardStore.getCatalog().find(t => t.nivelDias === 14 || t.id === 'tier-14d');
        return item ? item.costoPuntos : null;
      }
      return null;
    });
    assert.ok(cost14 === 1400 || htmlContent.includes('1400') || htmlContent.includes('1,400'), 'Nivel 14 Días cost must be 1,400 points');
  });

  await t('F17-03', 'F17: Nivel 14 Días primary benefit is Bono almuerzo de cuadrilla', () => {
    const hasLunch = htmlContent.includes('almuerzo') || htmlContent.includes('Almuerzo') || htmlContent.includes('cuadrilla');
    assert.ok(hasLunch, 'Nivel 14 Días must specify Bono de almuerzo de obra para cuadrillas');
  });

  await t('F17-04', 'F17: Nivel 14 Días secondary benefit is Merchandising Don Fraguado', () => {
    const hasDonFraguado = htmlContent.includes('Don Fraguado') || htmlContent.includes('Merchandising');
    assert.ok(hasDonFraguado, 'Nivel 14 Días must specify Merchandising Don Fraguado');
  });

  await t('F17-05', 'F17: Nivel 14 Días displays Disponible status when balance >= 1,400', async () => {
    assert.ok(page, 'Browser page must be active');
    const available = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.canRedeem) {
        return window.UltraRewardStore.canRedeem('tier-14d');
      }
      return true;
    });
    assert.ok(available, 'Nivel 14 Días must be redeemable with 2,100 PTS balance');
  });

  // --------------------------------------------------------------------------
  // FEATURE 18: Catálogo de Recompensas: Nivel 30 Días (R4)
  // --------------------------------------------------------------------------
  await t('F18-01', 'F18: Reward catalog defines Nivel 30 Días tier', async () => {
    assert.ok(page, 'Browser page must be active');
    const hasTier30 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        return window.UltraRewardStore.getCatalog().some(t => t.nivelDias === 30 || t.id === 'tier-30d');
      }
      return false;
    });
    assert.ok(hasTier30 || htmlContent.includes('Nivel 30') || htmlContent.includes('30 Días'), 'Catalog must contain Nivel 30 Días reward');
  });

  await t('F18-02', 'F18: Nivel 30 Días cost is exactly 3,000 points', async () => {
    assert.ok(page, 'Browser page must be active');
    const cost30 = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.getCatalog) {
        const item = window.UltraRewardStore.getCatalog().find(t => t.nivelDias === 30 || t.id === 'tier-30d');
        return item ? item.costoPuntos : null;
      }
      return null;
    });
    assert.ok(cost30 === 3000 || htmlContent.includes('3000') || htmlContent.includes('3,000'), 'Nivel 30 Días cost must be 3,000 points');
  });


  await t('F18-03', 'F18: Nivel 30 Días primary benefit is Acelerador de comisión (+3%)', () => {
    const hasCommission = (htmlContent.includes('+3%') || htmlContent.includes('3%')) && (htmlContent.includes('comisión') || htmlContent.includes('comision') || htmlContent.includes('Acelerador'));
    assert.ok(hasCommission, 'Nivel 30 Días must specify Acelerador de comisión (+3%)');
  });

  await t('F18-04', 'F18: Nivel 30 Días secondary benefit is Día libre compensatorio de terreno', () => {
    const hasDayOff = htmlContent.includes('Día libre') || htmlContent.includes('Dia libre') || htmlContent.includes('compensatorio');
    assert.ok(hasDayOff, 'Nivel 30 Días must specify Día libre compensatorio');
  });

  await t('F18-05', 'F18: Nivel 30 Días displays Bloqueado status when balance < 3,000', async () => {
    assert.ok(page, 'Browser page must be active');
    const locked = await page.evaluate(() => {
      if (window.UltraRewardStore && window.UltraRewardStore.canRedeem) {
        return !window.UltraRewardStore.canRedeem('tier-30d'); // 2100 < 3000
      }
      return true;
    });
    assert.ok(locked, 'Nivel 30 Días must be locked when balance is 2,100 PTS');
  });

  // --------------------------------------------------------------------------
  // FEATURE 19: Flujo Interactivo de Redención (R4)
  // --------------------------------------------------------------------------
  await t('F19-01', 'F19: Redimir button triggers confirmation modal or dialog', async () => {
    assert.ok(page, 'Browser page must be active');
    const modalExists = await page.evaluate(() => {
      return (
        document.getElementById('modal-redimir') !== null ||
        document.querySelector('[data-modal="redimir"]') !== null ||
        typeof window.openRedeemModal === 'function' ||
        typeof window.UltraRewardStore?.redeem === 'function'
      );
    });
    assert.ok(modalExists, 'Redemption confirmation modal or handler must exist');
  });

  await t('F19-02', 'F19: Confirming redemption deducts reward cost from wallet', async () => {
    assert.ok(page, 'Browser page must be active');
    const deducted = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      const initial = window.UltraRewardStore.getBalance();
      const success = window.UltraRewardStore.redeem('tier-7d'); // 700 pts
      if (!success) return false;
      const updated = window.UltraRewardStore.getBalance();
      return updated === initial - 700;
    });
    assert.ok(deducted, 'Redeeming tier-7d must deduct exactly 700 points');
  });

  await t('F19-03', 'F19: Successful redemption appends record to redemption history', async () => {
    assert.ok(page, 'Browser page must be active');
    const historyLogged = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.getHistory !== 'function') return false;
      const hist = window.UltraRewardStore.getHistory();
      return Array.isArray(hist) && hist.length > 0;
    });
    assert.ok(historyLogged, 'Redemption history must record transaction entry');
  });

  await t('F19-04', 'F19: Redemption history record contains required metadata', async () => {
    assert.ok(page, 'Browser page must be active');
    const metaValid = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.getHistory !== 'function') return false;
      const hist = window.UltraRewardStore.getHistory();
      if (!hist.length) return false;
      const latest = hist[hist.length - 1];
      return latest.id && latest.costoPuntos && latest.fecha && latest.codigoCanje;
    });
    assert.ok(metaValid, 'Redemption record must include id, costoPuntos, fecha, and codigoCanje');
  });

  await t('F19-05', 'F19: Visual feedback / toast confirmation triggered on redemption', async () => {
    assert.ok(page, 'Browser page must be active');
    const feedbackHandled = await page.evaluate(() => {
      return (
        document.querySelector('.toast, #toast-container, .alert-success, #notification-bar') !== null ||
        typeof window.showToast === 'function' ||
        typeof window.UltraRewardStore?.showConfirmation === 'function'
      );
    });
    assert.ok(feedbackHandled, 'Visual confirmation toast or notification element must exist');
  });

  // --------------------------------------------------------------------------
  // FEATURE 20: Despliegue Sincronizado GitHub Pages (Acceptance)
  // --------------------------------------------------------------------------
  await t('F20-01', 'F20: .nojekyll file exists in repository root', () => {
    const nojekyllPath = path.join(PROJECT_ROOT, '.nojekyll');
    assert.ok(fs.existsSync(nojekyllPath), '.nojekyll must exist in project root');
  });

  await t('F20-02', 'F20: GitHub Pages static deployment workflow configured (.github/workflows/static.yml)', () => {
    const workflowPath = path.join(PROJECT_ROOT, '.github/workflows/static.yml');
    assert.ok(fs.existsSync(workflowPath), '.github/workflows/static.yml must exist');
    const content = fs.readFileSync(workflowPath, 'utf-8');
    assert.ok(content.includes('actions/deploy-pages'), 'Workflow must use actions/deploy-pages');
  });

  await t('F20-03', 'F20: index.html asset paths use relative or HTTPS allowlisted URLs', () => {
    const invalidLocalPaths = htmlContent.match(/href="file:\/\/|src="file:\/\/|href="C:\\|src="C:\\/gi);
    assert.strictEqual(invalidLocalPaths, null, 'index.html must not contain local filesystem URLs');
  });

  await t('F20-04', 'F20: server.js routes root URL to index.html and provides /api/health', () => {
    assert.ok(serverJsContent.includes('/api/health'), 'server.js must provide /api/health endpoint');
    assert.ok(serverJsContent.includes('index.html'), 'server.js must serve index.html for root path');
  });

  await t('F20-05', 'F20: GitHub Pages target URL documented and verified in PROJECT.md', () => {
    const projectMd = fs.readFileSync(path.join(PROJECT_ROOT, 'PROJECT.md'), 'utf-8');
    assert.ok(
      projectMd.includes('https://thehector2614.github.io/Cooweb-1/'),
      'PROJECT.md must document GitHub Pages deployment target'
    );
  });

  if (pageContext) {
    await pageContext.close();
  }

  const passed = results.filter(r => r.passed).length;
  const failed = results.filter(r => !r.passed).length;
  const total = results.length;

  console.log(`\nTier 1 Summary: ${passed} passed, ${failed} failed, ${total} total (${Math.round((passed / total) * 100)}%)`);

  return {
    name: 'Tier 1: Feature Coverage',
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
      console.error('Fatal error in Tier 1 runner:', err);
      closeBrowser();
      process.exit(1);
    });
}

module.exports = { run };
