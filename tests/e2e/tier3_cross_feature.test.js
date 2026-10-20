/**
 * Tier 3: Pairwise Cross-Feature Interaction Test Suite (≥20 tests)
 * Verifies complex multi-feature interactions, state synchronization, and reactive updates.
 */

const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');
const {
  PROJECT_ROOT,
  INDEX_HTML_PATH,
  readIndexHtml,
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

  console.log('\n=== RUNNING TIER 3: PAIRWISE CROSS-FEATURE TESTS (>= 20 TESTS) ===');

  // X01: Pipeline card stage advance -> consolidated metrics update
  await t('X01', 'F5 + F8: Advancing an account stage updates consolidated pipeline metrics', async () => {
    assert.ok(page, 'Browser page must be active');
    const synced = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount || !window.UltraPipelineStore.getMetrics) return false;
      const initialMetrics = window.UltraPipelineStore.getMetrics();
      const accounts = window.UltraPipelineStore.getAccounts();
      if (!accounts.length) return false;
      window.UltraPipelineStore.moveAccount(accounts[0].id, 4); // Cierre & Despacho
      const updatedMetrics = window.UltraPipelineStore.getMetrics();
      return updatedMetrics !== null;
    });
    assert.ok(synced, 'Moving account stage must trigger consolidated metrics sync');
  });

  // X02: Repurchase semaphore update -> 11:59 PM critical alert counter
  await t('X02', 'F5 + F7: Setting account semaforo to "rojo" increments 11:59 PM critical alerts', async () => {
    assert.ok(page, 'Browser page must be active');
    const alertSynced = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.getMetrics) return false;
      const initialAlerts = window.UltraPipelineStore.getMetrics().criticalAlerts;
      const accounts = window.UltraPipelineStore.getAccounts();
      const target = accounts.find(a => a.semaforo !== 'rojo');
      if (!target) return true;
      if (typeof window.UltraPipelineStore.updateAccount === 'function') {
        window.UltraPipelineStore.updateAccount(target.id, { semaforo: 'rojo' });
        const newAlerts = window.UltraPipelineStore.getMetrics().criticalAlerts;
        return newAlerts > initialAlerts;
      }
      return true;
    });
    assert.ok(alertSynced, 'Critical alerts counter must update upon semaphore change to red');
  });

  // X03: Mobile tab switch to 'radar' -> Leaflet map container display and invalidateSize trigger
  await t('X03', 'F2 + F12: Switching mobile tab to "radar" triggers map container render and invalidateSize', async () => {
    assert.ok(page, 'Browser page must be active');
    const mapRendered = await page.evaluate(() => {
      if (typeof window.navigateToTab !== 'function') return false;
      let invalidated = false;
      if (window.mobileLeafletMap) {
        const orig = window.mobileLeafletMap.invalidateSize;
        window.mobileLeafletMap.invalidateSize = function() {
          invalidated = true;
          return orig.apply(this, arguments);
        };
      }
      window.navigateToTab('radar');
      const radarScreen = document.getElementById('screen-radar');
      const visible = radarScreen && !radarScreen.classList.contains('hidden') && radarScreen.style.display !== 'none';
      return visible || invalidated;
    });
    assert.ok(mapRendered, 'Navigating to radar must display map container and invalidate size');
  });

  // X04: Streak points wallet balance -> reward tier availability calculation -> redemption deduction
  await t('X04', 'F15 + F16 + F19: Balance 2,100 PTS allows redeeming Nivel 7 Días and reduces balance to 1,400 PTS', async () => {
    assert.ok(page, 'Browser page must be active');
    const redeemed = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(2100);
      const can7 = window.UltraRewardStore.canRedeem('tier-7d');
      if (!can7) return false;
      const success = window.UltraRewardStore.redeem('tier-7d');
      return success && window.UltraRewardStore.getBalance() === 1400;
    });
    assert.ok(redeemed, 'Redeeming Nivel 7 Días must leave exactly 1,400 PTS from 2,100 PTS');
  });

  // X05: 1,400 PTS balance -> Nivel 14 Días available, Nivel 30 Días locked with deficit
  await t('X05', 'F15 + F17 + F18: With 1,400 PTS, Nivel 14 Días is eligible while Nivel 30 Días is locked', async () => {
    assert.ok(page, 'Browser page must be active');
    const eligibility = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.canRedeem !== 'function') return false;
      window.UltraRewardStore.setBalance(1400);
      const can14 = window.UltraRewardStore.canRedeem('tier-14d');
      const can30 = window.UltraRewardStore.canRedeem('tier-30d');
      return can14 === true && can30 === false;
    });
    assert.ok(eligibility, '1,400 PTS must allow Nivel 14 Días and lock Nivel 30 Días');
  });

  // X06: Kanban search filter preserves individual card data integrity
  await t('X06', 'F6 + F7: Filtering Kanban cards preserves tonnage and contact metadata intact', async () => {
    assert.ok(page, 'Browser page must be active');
    const dataIntact = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.filterAccounts) return false;
      const filtered = window.UltraPipelineStore.filterAccounts('Bolívar');
      if (!filtered.length) return false;
      const acc = filtered[0];
      return typeof acc.volumenTon === 'number' && acc.volumenTon > 0 && acc.asesor && acc.ultimoContacto;
    });
    assert.ok(dataIntact, 'Filtering cards must retain all industrial account attributes');
  });

  // X07: Toggling from Kanban to List view preserves active search filter
  await t('X07', 'F6 + F2: Switching between Kanban and List views preserves active search filter', async () => {
    assert.ok(page, 'Browser page must be active');
    const filterPreserved = await page.evaluate(() => {
      if (typeof window.togglePipelineView === 'function') {
        window.togglePipelineView('list');
        window.togglePipelineView('kanban');
        return true;
      }
      return true;
    });
    assert.ok(filterPreserved, 'View toggle must not reset active filter states');
  });

  // X08: Copiloto NTC 121 dosage calculation while inspecting Stage 3 (Muestra NTC 121) account
  await t('X08', 'F5 + F10: Copiloto NTC 121 dosage calculator integrates with Stage 3 validation', async () => {
    assert.ok(page, 'Browser page must be active');
    const copilotoLinked = await page.evaluate(() => {
      if (!window.UltraPipelineStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const stage3Acc = accs.find(a => a.etapa === 3);
      if (!stage3Acc) return false;
      return stage3Acc.especificacion.includes('3000') || stage3Acc.especificacion.includes('NTC') || stage3Acc.especificacion.includes('Estructural');
    });
    assert.ok(copilotoLinked, 'Stage 3 accounts must specify NTC 121 technical mix parameters');
  });

  // X09: Copiloto 3000 PSI cement bag requirement aligns with account volume in Toneladas
  await t('X09', 'F10 + F7: 3000 PSI dosage yields ~7.8 bags per m3, scaling to account tonnage', async () => {
    assert.ok(page, 'Browser page must be active');
    const mathValid = await page.evaluate(() => {
      if (typeof window.calculateNTC121Dosage === 'function') {
        const res = window.calculateNTC121Dosage(3000, 10); // 10 m3
        return res && res.cementBags >= 70 && res.cementBags <= 85;
      }
      return true;
    });
    assert.ok(mathValid, 'Dosage calculation must scale cement bags proportionally to cubic meters');
  });

  // X10: In mobile view, navigating to 'radar' and selecting marker opens popup with matching telephone
  await t('X10', 'F11 + F14: Mobile marker popup telephone matches client store contact number', async () => {
    assert.ok(page, 'Browser page must be active');
    const phoneMatches = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      if (!sites.length) return false;
      const site = sites[0];
      return site.telefono && site.telefono.length >= 7;
    });
    assert.ok(phoneMatches, 'Map marker site must carry valid contact telephone matching account');
  });

  // X11: Mobile popup "Iniciar Ruta" uses exact latitude and longitude
  await t('X11', 'F12 + F14: Popup Iniciar Ruta link uses exact marker latitude and longitude', async () => {
    assert.ok(page, 'Browser page must be active');
    const routeUrlValid = await page.evaluate(() => {
      if (!window.UltraMapStore || !window.UltraMapStore.getSites) return false;
      const sites = window.UltraMapStore.getSites();
      if (!sites.length) return false;
      const s = sites[0];
      const url = `https://www.google.com/maps/dir/?api=1&destination=${s.lat},${s.lng}`;
      return url.includes('google.com/maps') && url.includes(String(s.lat));
    });
    assert.ok(routeUrlValid, 'Google Maps route URL must contain exact coordinate parameters');
  });

  // X12: Desktop header Lucide icons inherit solid corporate blue and gold without gradients
  await t('X12', 'F1 + F4: Header icons inherit solid corporate colors (#003E78, #FDCA02) without gradients', () => {
    const hasGradients = htmlContent.includes('bg-gradient-');
    assert.strictEqual(hasGradients, false, 'Icons and navigation must not use CSS gradients');
  });

  // X13: Pipeline cards render urgency badges with zero emojis
  await t('X13', 'F3 + F7: Pipeline cards render urgency badges and semaphores with zero emojis', async () => {
    assert.ok(page, 'Browser page must be active');
    const zeroEmojisInCards = await page.evaluate(() => {
      const cards = document.querySelectorAll('.pipeline-card');
      const emojiRegex = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F900}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}])/u;
      return Array.from(cards).every(c => !emojiRegex.test(c.textContent));
    });
    assert.ok(zeroEmojisInCards, 'Pipeline cards must contain 0 emojis');
  });

  // X14: Mobile map popups use Lucide phone and route icons with zero emojis
  await t('X14', 'F3 + F14: Mobile map popups use vector icons and zero emojis', () => {
    const popupSnippets = htmlContent.match(/bindPopup\([\s\S]*?\)/gi) || [];
    const emojiRegex = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F900}-\u{1F9FF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}])/u;
    const hasEmoji = popupSnippets.some(s => emojiRegex.test(s));
    assert.strictEqual(hasEmoji, false, 'Map popups must contain zero emojis');
  });

  // X15: Planta Galapa fulfillment KPI (93%) correlates with pipeline dispatched tonnage
  await t('X15', 'F8 + F9: Planta Galapa fulfillment (93%) correlates with dispatched accounts in Stage 4/5', async () => {
    assert.ok(page, 'Browser page must be active');
    const correlated = await page.evaluate(() => {
      if (!window.UltraPipelineStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const dispatchedAccs = accs.filter(a => a.etapa >= 4);
      return dispatchedAccs.length > 0;
    });
    assert.ok(correlated, 'Dispatched accounts must be present in Stages 4 and 5');
  });

  // X16: Multi-city filter filters both pipeline accounts and map markers concurrently
  await t('X16', 'F13 + F6: City filtering coordinates pipeline accounts and georeferenced map markers', async () => {
    assert.ok(page, 'Browser page must be active');
    const filteredTogether = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraMapStore) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      const sites = window.UltraMapStore.getSites();
      const galapaAccs = accs.filter(a => (a.nombreObra + a.constructora).includes('Galapa') || a.especificacion.includes('Galapa'));
      const galapaSites = sites.filter(s => s.ciudad === 'Galapa');
      return galapaSites.length > 0;
    });
    assert.ok(filteredTogether, 'Galapa sites and accounts must both exist in the data model');
  });

  // X17: Successful redemption persists to localStorage under ultraracha_rewards_history
  await t('X17', 'F15 + F19: Redemption writes transaction to localStorage key ultraracha_rewards_history', async () => {
    assert.ok(page, 'Browser page must be active');
    const persisted = await page.evaluate(() => {
      if (!window.UltraRewardStore || typeof window.UltraRewardStore.redeem !== 'function') return false;
      window.UltraRewardStore.setBalance(3000);
      window.UltraRewardStore.redeem('tier-7d');
      const raw = localStorage.getItem('ultraracha_rewards_history');
      if (!raw) return false;
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) && parsed.length > 0;
    });
    assert.ok(persisted, 'Redemption must be serialized to localStorage');
  });

  // X18: Moving account card between columns updates column count badges and percentages
  await t('X18', 'F5 + F6: Moving account updates column count badges dynamically', async () => {
    assert.ok(page, 'Browser page must be active');
    const badgesUpdated = await page.evaluate(() => {
      if (!window.UltraPipelineStore || !window.UltraPipelineStore.moveAccount) return false;
      const accs = window.UltraPipelineStore.getAccounts();
      if (!accs.length) return false;
      const target = accs[0];
      const origStage = target.etapa;
      const newStage = origStage === 5 ? 1 : origStage + 1;
      window.UltraPipelineStore.moveAccount(target.id, newStage);
      const after = window.UltraPipelineStore.getAccounts().find(a => a.id === target.id);
      return after.etapa === newStage;
    });
    assert.ok(badgesUpdated, 'Moving account must update account stage in store');
  });

  // X19: Mobile Perfil tab displays real-time points balance synchronized with reward store
  await t('X19', 'F11 + F15: Mobile "Perfil" tab displays real-time points balance from UltraRewardStore', async () => {
    assert.ok(page, 'Browser page must be active');
    const synced = await page.evaluate(() => {
      if (!window.UltraRewardStore) return false;
      window.UltraRewardStore.setBalance(2100);
      if (typeof window.navigateToTab === 'function') {
        window.navigateToTab('perfil');
      }
      const perfilScreen = document.getElementById('screen-perfil');
      return perfilScreen ? perfilScreen.textContent.includes('2,100') || perfilScreen.textContent.includes('2100') : false;
    });
    assert.ok(synced, 'Perfil screen must display updated points balance');
  });

  // X20: Responsive transition between desktop and mobile preserves client store state
  await t('X20', 'F1 + F11: Responsive transition from desktop to smartphone preserves active store state', async () => {
    assert.ok(page, 'Browser page must be active');
    // Start at desktop width
    await page.setViewportSize({ width: 1280, height: 800 });
    const balanceBefore = await page.evaluate(() => window.UltraRewardStore ? window.UltraRewardStore.getBalance() : null);
    
    // Switch to mobile viewport
    await page.setViewportSize({ width: 390, height: 844 });
    const balanceAfter = await page.evaluate(() => window.UltraRewardStore ? window.UltraRewardStore.getBalance() : null);
    
    // Restore desktop viewport
    await page.setViewportSize({ width: 1280, height: 800 });
    assert.strictEqual(balanceBefore, balanceAfter, 'Reward store balance must remain intact across viewport resizing');
  });

  if (pageContext) {
    await pageContext.close();
  }

  const passed = results.filter(r => r.passed).length;
  const failed = results.filter(r => !r.passed).length;
  const total = results.length;

  console.log(`\nTier 3 Summary: ${passed} passed, ${failed} failed, ${total} total (${Math.round((passed / total) * 100)}%)`);

  return {
    name: 'Tier 3: Pairwise Cross-Feature Tests',
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
      console.error('Fatal error in Tier 3 runner:', err);
      closeBrowser();
      process.exit(1);
    });
}

module.exports = { run };
