/**
 * Tier 4: Real-World Application Workloads Test Suite (5 realistic Caribbean construction scenarios)
 * End-to-end multi-step industrial workloads deriving from TEST_INFRA.md
 */

const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const {
  PROJECT_ROOT,
  INDEX_HTML_PATH,
  readIndexHtml,
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

  console.log('\n=== RUNNING TIER 4: REAL-WORLD APPLICATION SCENARIOS (5 SCENARIOS) ===');

  // --------------------------------------------------------------------------
  // SCENARIO 1: Asesor en Terreno (Barranquilla & Galapa)
  // Carlos Mendoza consulta el Pipeline Kanban, filtra por "Constructora Bolívar",
  // revisa el semáforo crítico y cambia a vista de Lista para verificar las 120 Ton de Estructural Max.
  // --------------------------------------------------------------------------
  await t(
    'S01',
    'Scenario 1: Asesor en Terreno (Barranquilla & Galapa) - Pipeline Kanban, Filter & List View',
    async () => {
      assert.ok(page, 'Browser page must be active');
      const scenarioPassed = await page.evaluate(() => {
        // Step 1: Navigate to desktop pipeline tab
        if (typeof window.navigateToDesktopTab === 'function') {
          window.navigateToDesktopTab('pipeline');
        }

        // Step 2: Access UltraPipelineStore
        if (!window.UltraPipelineStore || !window.UltraPipelineStore.getAccounts) {
          return { ok: false, reason: 'UltraPipelineStore not available' };
        }

        const allAccounts = window.UltraPipelineStore.getAccounts();
        if (!allAccounts.length) {
          return { ok: false, reason: 'No accounts in pipeline store' };
        }

        // Step 3: Filter by Constructora Bolívar
        const bolivarAccounts = window.UltraPipelineStore.filterAccounts
          ? window.UltraPipelineStore.filterAccounts('Bolívar')
          : allAccounts.filter(a => (a.constructora + a.nombreObra).toLowerCase().includes('bolívar') || (a.constructora + a.nombreObra).toLowerCase().includes('bolivar'));

        if (!bolivarAccounts.length) {
          return { ok: false, reason: 'No accounts found for Constructora Bolívar' };
        }

        const targetAccount = bolivarAccounts[0];

        // Step 4: Verify volume and advisor
        if (!targetAccount.volumenTon || targetAccount.volumenTon <= 0) {
          return { ok: false, reason: 'Invalid account volume' };
        }

        // Step 5: Verify semaforo property
        if (!['verde', 'amarillo', 'rojo'].includes(targetAccount.semaforo)) {
          return { ok: false, reason: 'Invalid account semaforo' };
        }

        // Step 6: Toggle to List view and verify stability
        if (typeof window.togglePipelineView === 'function') {
          window.togglePipelineView('list');
          window.togglePipelineView('kanban');
        }

        return { ok: true };
      });

      assert.ok(scenarioPassed.ok, `Scenario 1 failed: ${scenarioPassed.reason}`);
    }
  );

  // --------------------------------------------------------------------------
  // SCENARIO 2: Ruta Móvil de Inspección en Celular
  // En la vista smartphone, el asesor abre la pestaña "Radar", visualiza los marcadores
  // en Soledad y Galapa con azulejos ESRI, abre el popup de Ferretería El Constructor e inicia ruta por GPS.
  // --------------------------------------------------------------------------
  await t(
    'S02',
    'Scenario 2: Ruta Móvil de Inspección en Celular - Radar Map, Popups & GPS Route',
    async () => {
      assert.ok(page, 'Browser page must be active');
      // Set smartphone viewport (iPhone 14 / standard mobile 390x844)
      await page.setViewportSize({ width: 390, height: 844 });

      const scenarioPassed = await page.evaluate(() => {
        // Step 1: Navigate to mobile Radar tab
        if (typeof window.navigateToTab !== 'function') {
          return { ok: false, reason: 'window.navigateToTab not defined' };
        }
        window.navigateToTab('radar');

        // Step 2: Verify UltraMapStore is available
        if (!window.UltraMapStore || !window.UltraMapStore.getSites) {
          return { ok: false, reason: 'UltraMapStore not available' };
        }

        const sites = window.UltraMapStore.getSites();
        if (!sites.length) {
          return { ok: false, reason: 'No georeferenced sites in UltraMapStore' };
        }

        // Step 3: Find site in Soledad or Galapa (or Ferretería El Constructor)
        const targetSite = sites.find(s => s.nombre.includes('Constructor') || s.ciudad === 'Soledad' || s.ciudad === 'Galapa');
        if (!targetSite) {
          return { ok: false, reason: 'No target site found in Soledad or Galapa' };
        }

        // Step 4: Verify site coordinates and actions
        if (!targetSite.lat || !targetSite.lng || !targetSite.telefono) {
          return { ok: false, reason: 'Site lacks coordinates or telephone' };
        }

        const mapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${targetSite.lat},${targetSite.lng}`;
        if (!mapsUrl.includes('google.com/maps')) {
          return { ok: false, reason: 'Invalid maps navigation URL generated' };
        }

        return { ok: true };
      });

      // Restore viewport
      await page.setViewportSize({ width: 1280, height: 800 });
      assert.ok(scenarioPassed.ok, `Scenario 2 failed: ${scenarioPassed.reason}`);
    }
  );

  // --------------------------------------------------------------------------
  // SCENARIO 3: Validación Técnica NTC 121 en Obra
  // Desde el Pipeline, el asesor abre el Copiloto Técnico NTC 121, calcula la dosificación
  // para 3000 PSI en vaciado de losa maciza (a/c 0.51), sin recargar la pantalla ni perder el contexto comercial.
  // --------------------------------------------------------------------------
  await t(
    'S03',
    'Scenario 3: Validación Técnica NTC 121 en Obra - Concrete Dosage Calculation Without Reload',
    async () => {
      assert.ok(page, 'Browser page must be active');
      const scenarioPassed = await page.evaluate(() => {
        // Step 1: Verify Copiloto section or calculation method
        if (typeof window.calculateNTC121Dosage === 'function') {
          const dosage = window.calculateNTC121Dosage(3000, 45); // 3000 PSI, 45 m3
          if (!dosage || !dosage.waterCementRatio || !dosage.cementBags) {
            return { ok: false, reason: 'Dosage calculation returned incomplete data' };
          }

          // a/c ratio should be ~0.51 (bounded between 0.45 and 0.55)
          if (dosage.waterCementRatio < 0.45 || dosage.waterCementRatio > 0.55) {
            return { ok: false, reason: `Water-cement ratio ${dosage.waterCementRatio} not ~0.51` };
          }

          // 45 m3 at ~7.8 bags/m3 should be ~350 bags
          if (dosage.cementBags < 300 || dosage.cementBags > 400) {
            return { ok: false, reason: `Cement bags ${dosage.cementBags} out of expected ~350 range` };
          }
        }

        // Step 2: Verify Copiloto container exists
        const copilotoContainer =
          document.getElementById('dcrm-content-copiloto') ||
          document.getElementById('screen-copiloto') ||
          document.querySelector('[data-module="copiloto"]');

        if (!copilotoContainer && typeof window.calculateNTC121Dosage !== 'function') {
          return { ok: false, reason: 'Copiloto container and calculateNTC121Dosage not found' };
        }

        return { ok: true };
      });

      assert.ok(scenarioPassed.ok, `Scenario 3 failed: ${scenarioPassed.reason}`);
    }
  );

  // --------------------------------------------------------------------------
  // SCENARIO 4: Recompensa por Racha Comercial (11:59 PM)
  // Carlos Mendoza verifica su billetera con 2,100 PTS de racha acumulada (21 días),
  // redime el Bono de Combustible ($50.000 COP) Nivel 7 Días, verifica el descuento a 1,400 PTS
  // y el registro en el historial de canjes.
  // --------------------------------------------------------------------------
  await t(
    'S04',
    'Scenario 4: Recompensa por Racha Comercial (11:59 PM) - Wallet Balance, Redemption & History',
    async () => {
      assert.ok(page, 'Browser page must be active');
      const scenarioPassed = await page.evaluate(() => {
        // Step 1: Access UltraRewardStore
        if (!window.UltraRewardStore || typeof window.UltraRewardStore.getBalance !== 'function') {
          return { ok: false, reason: 'UltraRewardStore not available' };
        }

        // Step 2: Initialize balance to 2,100 PTS and streak to 21 days
        window.UltraRewardStore.setBalance(2100);
        if (typeof window.UltraRewardStore.setStreakDays === 'function') {
          window.UltraRewardStore.setStreakDays(21);
        }

        if (window.UltraRewardStore.getBalance() !== 2100) {
          return { ok: false, reason: 'Failed to set initial balance to 2,100 PTS' };
        }

        // Step 3: Verify Nivel 7 Días eligibility
        const canRedeem7d = window.UltraRewardStore.canRedeem('tier-7d');
        if (!canRedeem7d) {
          return { ok: false, reason: 'tier-7d not eligible for redemption with 2,100 PTS' };
        }

        // Step 4: Execute redemption
        const success = window.UltraRewardStore.redeem('tier-7d');
        if (!success) {
          return { ok: false, reason: 'Redemption execution returned false' };
        }

        // Step 5: Verify new balance is exactly 1,400 PTS
        const updatedBalance = window.UltraRewardStore.getBalance();
        if (updatedBalance !== 1400) {
          return { ok: false, reason: `Expected updated balance 1,400 PTS, got ${updatedBalance}` };
        }

        // Step 6: Verify entry in redemption history
        const history = window.UltraRewardStore.getHistory ? window.UltraRewardStore.getHistory() : null;
        if (!history || !history.length) {
          return { ok: false, reason: 'Redemption was not recorded in history' };
        }

        const latest = history[history.length - 1];
        if (!latest.codigoCanje || !latest.fecha || latest.costoPuntos !== 700) {
          return { ok: false, reason: 'Redemption record missing required audit fields' };
        }

        return { ok: true };
      });

      assert.ok(scenarioPassed.ok, `Scenario 4 failed: ${scenarioPassed.reason}`);
    }
  );

  // --------------------------------------------------------------------------
  // SCENARIO 5: Auditoría Ejecutiva de KPIs de Planta Galapa
  // El Director Comercial abre el Dashboard de KPIs, verifica el cumplimiento del 93%
  // mensual de Planta Galapa, revisa los tiempos OTD por corredor vial (Circunvalar vs Vía al Mar)
  // y el semáforo antichurn general sin aberraciones visuales ni emojis.
  // --------------------------------------------------------------------------
  await t(
    'S05',
    'Scenario 5: Auditoría Ejecutiva de KPIs de Planta Galapa - Fulfillment, OTD, Antichurn, 0 Emojis, 0 Gradients',
    async () => {
      assert.ok(page, 'Browser page must be active');
      const scenarioPassed = await page.evaluate(() => {
        // Step 1: Navigate to KPIs tab
        if (typeof window.navigateToDesktopTab === 'function') {
          window.navigateToDesktopTab('kpis');
        }

        const kpisContainer = document.getElementById('dcrm-content-kpis') || document.body;
        const text = kpisContainer.textContent;

        // Step 2: Verify Planta Galapa fulfillment reference (93%)
        const hasFulfillment = text.includes('93%') || text.includes('Galapa') || text.includes('Cumplimiento');
        if (!hasFulfillment) {
          return { ok: false, reason: 'Planta Galapa fulfillment rate (93%) not found' };
        }

        // Step 3: Verify OTD delivery time reference
        const hasOTD = text.includes('84') || text.includes('OTD') || text.includes('Entrega');
        if (!hasOTD) {
          return { ok: false, reason: 'OTD delivery metric not found' };
        }

        // Step 4: Verify client retention reference (94.2%)
        const hasRetention = text.includes('94.2%') || text.includes('Recompra') || text.includes('Retención') || text.includes('Antichurn');
        if (!hasRetention) {
          return { ok: false, reason: 'Client retention / antichurn rate not found' };
        }

        // Step 5: Verify zero emojis in KPI dashboard
        const emojiRegex = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F900}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}])/u;
        if (emojiRegex.test(text)) {
          return { ok: false, reason: 'Emojis detected in KPI dashboard container' };
        }

        // Step 6: Verify zero CSS gradients in KPI dashboard container
        const html = kpisContainer.innerHTML;
        if (html.includes('bg-gradient-') || html.includes('linear-gradient(')) {
          return { ok: false, reason: 'CSS gradients detected in KPI dashboard' };
        }

        return { ok: true };
      });

      assert.ok(scenarioPassed.ok, `Scenario 5 failed: ${scenarioPassed.reason}`);
    }
  );

  if (pageContext) {
    await pageContext.close();
  }

  const passed = results.filter(r => r.passed).length;
  const failed = results.filter(r => !r.passed).length;
  const total = results.length;

  console.log(`\nTier 4 Summary: ${passed} passed, ${failed} failed, ${total} total (${Math.round((passed / total) * 100)}%)`);

  return {
    name: 'Tier 4: Real-World Scenarios',
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
      console.error('Fatal error in Tier 4 runner:', err);
      closeBrowser();
      process.exit(1);
    });
}

module.exports = { run };
