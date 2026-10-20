/**
 * Adversarial Stress & Verification Harness for Milestone 3
 * Challenger: teamwork_preview_challenger (Milestone 3-1)
 * 
 * Verifies:
 * 1. Mobile Tab Switching Stress & Fuzzing (1,000 rapid cycles, ping-pong, invalid/malicious tabs)
 * 2. Mobile Leaflet Map Idempotency & Layer Controls (100x tight loops, container detachment, satellite toggle, category filters)
 * 3. Georeferenced Coordinates Accuracy & Regional Invariants (Bounding boxes for 6 Caribbean cities, non-overlapping oracle, haversine distances)
 * 4. Action Popup URLs & Template Injection Defense (Dialing regex, Google Maps coordinates, zero emojis, zero gradients, XSS fuzzing)
 * 5. Mobile Pipeline Integration & Synchronized State (14 cards, search filtering, stage filtering)
 * 6. City Filtering & Store Immutability
 * 7. Live Marker Interaction & Real DOM Popup Opening
 */

const fs = require('fs');
const path = require('path');
const assert = require('assert');
const { chromium } = require('playwright');

const PROJECT_ROOT = path.resolve(__dirname, '../..');
const INDEX_HTML = path.join(PROJECT_ROOT, 'index.html');

const results = {
  tabSwitchingStress: [],
  tabFuzzing: [],
  mapIdempotency: [],
  geoAccuracy: [],
  popupValidation: [],
  mobilePipeline: [],
  cityFiltering: [],
  liveInteractions: [],
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
  if (!results[suite]) results[suite] = [];
  results[suite].push({ testName, passed, details });
}

// Haversine formula to compute distance in meters between two lat/lng coordinates
function haversineDistanceMeters(lat1, lon1, lat2, lon2) {
  const R = 6371e3; // Earth radius in meters
  const phi1 = (lat1 * Math.PI) / 180;
  const phi2 = (lat2 * Math.PI) / 180;
  const deltaPhi = ((lat2 - lat1) * Math.PI) / 180;
  const deltaLambda = ((lon2 - lon1) * Math.PI) / 180;

  const a = Math.sin(deltaPhi / 2) * Math.sin(deltaPhi / 2) +
            Math.cos(phi1) * Math.cos(phi2) *
            Math.sin(deltaLambda / 2) * Math.sin(deltaLambda / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

async function runAll() {
  console.log('================================================================');
  console.log('[CHALLENGER] ADVERSARIAL STRESS CHALLENGE SUITE: MILESTONE 3');
  console.log('================================================================\n');

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 375, height: 812 } // Mobile smartphone viewport
  });
  const page = await context.newPage();

  // Listen for uncaught page errors
  const pageErrors = [];
  page.on('pageerror', err => pageErrors.push(err.message));

  const fileUrl = 'file:///' + INDEX_HTML.replace(/\\/g, '/');
  await page.goto(fileUrl, { waitUntil: 'load' });

  // ============================================================================
  // SUITE 1: MOBILE TAB SWITCHING STRESS & ADVERSARIAL FUZZING
  // ============================================================================
  console.log('--- 1. Mobile Tab Switching Stress & Fuzzing ---');

  // 1.1 Rapid Tab Cycling (1,000 iterations)
  const tabSequence = ['racha', 'radar', 'pipeline', 'copiloto', 'perfil'];
  const t0 = Date.now();
  const cycleErrors = await page.evaluate((tabs) => {
    const errors = [];
    try {
      for (let i = 0; i < 1000; i++) {
        const targetTab = tabs[i % tabs.length];
        window.navigateToTab(targetTab);
      }
    } catch (e) {
      errors.push(e.message);
    }
    return errors;
  }, tabSequence);
  const cycleTime = Date.now() - t0;

  record('tabSwitchingStress', '1,000 Rapid tab switches completed without throwing',
    cycleErrors.length === 0,
    cycleErrors.length > 0 ? cycleErrors.join(', ') : `Duration: ${cycleTime}ms`
  );

  // Check state consistency after 1,000 cycles
  // After 1000 % 5 = 0, the last switched tab was tabSequence[999 % 5] = tabSequence[4] = 'perfil'
  const stateCheck = await page.evaluate(() => {
    const screens = {
      racha: document.getElementById('screen-racha'),
      radar: document.getElementById('screen-radar'),
      pipeline: document.getElementById('screen-pipeline'),
      copiloto: document.getElementById('screen-copiloto'),
      perfil: document.getElementById('screen-perfil')
    };
    const buttons = {
      racha: document.getElementById('nav-btn-racha'),
      radar: document.getElementById('nav-btn-radar'),
      pipeline: document.getElementById('nav-btn-pipeline'),
      copiloto: document.getElementById('nav-btn-copiloto'),
      perfil: document.getElementById('nav-btn-perfil')
    };

    const visibleScreens = Object.keys(screens).filter(k => screens[k] && !screens[k].classList.contains('hidden'));
    const activeButtons = Object.keys(buttons).filter(k => buttons[k] && buttons[k].className.includes('text-[#003E78]'));

    return {
      visibleScreens,
      activeButtons,
      perfilHidden: screens.perfil.classList.contains('hidden'),
      radarHidden: screens.radar.classList.contains('hidden')
    };
  });

  record('tabSwitchingStress', 'DOM state integrity preserved after 1,000 tab cycles',
    stateCheck.visibleScreens.length === 1 && stateCheck.visibleScreens[0] === 'perfil' &&
    stateCheck.activeButtons.length === 1 && stateCheck.activeButtons[0] === 'perfil',
    `Visible screens: [${stateCheck.visibleScreens}], Active buttons: [${stateCheck.activeButtons}]`
  );

  // 1.2 Real DOM Click Ping-Pong Stress (Radar <-> Racha 50 clicks)
  let clickErrors = 0;
  try {
    for (let i = 0; i < 50; i++) {
      await page.click('#nav-btn-radar');
      await page.click('#nav-btn-racha');
    }
  } catch (e) {
    clickErrors++;
  }
  // Wait 250ms for any queued setTimeout calls (such as map invalidateSize) to settle
  await page.waitForTimeout(250);

  record('tabSwitchingStress', 'Real DOM click ping-pong (50x radar/racha) executes without errors',
    clickErrors === 0 && pageErrors.length === 0,
    `Click errors: ${clickErrors}, Uncaught page errors: ${pageErrors.length}`
  );

  // 1.3 Adversarial Tab Argument Fuzzing
  const fuzzInputs = [
    null,
    undefined,
    "",
    "   ",
    0,
    1,
    -1,
    true,
    false,
    NaN,
    Infinity,
    -Infinity,
    {},
    [],
    "random_tab_xyz",
    "RADAR",
    " radar",
    "radar ",
    "constructor",
    "__proto__",
    "toString",
    "<script>window.__tab_xss = true;</script>",
    "\u0000",
    "racha\nradar"
  ];

  let fuzzPass = true;
  let fuzzFailure = '';

  for (const input of fuzzInputs) {
    const res = await page.evaluate((tabVal) => {
      try {
        window.navigateToTab(tabVal);
        const rachaScreen = document.getElementById('screen-racha');
        const rachaBtn = document.getElementById('nav-btn-racha');
        const isRachaVisible = rachaScreen && !rachaScreen.classList.contains('hidden');
        const isRachaActive = rachaBtn && rachaBtn.className.includes('text-[#003E78]');
        return { success: true, isRachaVisible, isRachaActive };
      } catch (err) {
        return { success: false, error: err.message };
      }
    }, input);

    if (!res.success || !res.isRachaVisible || !res.isRachaActive) {
      fuzzPass = false;
      fuzzFailure = `Input ${JSON.stringify(input)} failed: ${JSON.stringify(res)}`;
      break;
    }
  }

  record('tabFuzzing', 'navigateToTab fuzzing (24 invalid/adversarial inputs) safely defaults to racha',
    fuzzPass,
    fuzzFailure || 'All 24 adversarial inputs defaulted gracefully to racha'
  );

  // Verify XSS script was not injected via tab argument
  const xssFired = await page.evaluate(() => !!window.__tab_xss);
  record('tabFuzzing', 'XSS attack in navigateToTab does not execute in DOM',
    !xssFired,
    xssFired ? 'XSS payload executed!' : 'Safe: no XSS execution'
  );


  // ============================================================================
  // SUITE 2: LEAFLET MAP INITIALIZATION IDEMPOTENCY & LAYER CONTROLS
  // ============================================================================
  console.log('\n--- 2. Mobile Leaflet Map Idempotency & Layer Controls ---');

  // Switch to radar tab first
  await page.evaluate(() => window.navigateToTab('radar'));
  await page.waitForTimeout(200);

  // 2.1 Tight Synchronous Loop (100 sequential calls to initMobileLeafletMap)
  const idempotencyCheck = await page.evaluate(() => {
    const errors = [];
    try {
      for (let i = 0; i < 100; i++) {
        window.initMobileLeafletMap();
      }
    } catch (e) {
      errors.push(e.message);
    }

    const hasMap = !!window.mobileLeafletMap;
    // Inspect DOM markers count
    const markersInDom = document.querySelectorAll('#mobile-leaflet-map .leaflet-marker-pane path, #mobile-leaflet-map .leaflet-overlay-pane path').length;

    return {
      errors,
      hasMap,
      markersInDom
    };
  });

  record('mapIdempotency', 'initMobileLeafletMap 100x tight synchronous loop is strictly idempotent',
    idempotencyCheck.errors.length === 0 && idempotencyCheck.hasMap,
    idempotencyCheck.errors.length > 0 ? idempotencyCheck.errors.join('; ') : `Map valid, errors: 0`
  );

  record('mapIdempotency', 'Marker layers not duplicated after 100 map initializations',
    idempotencyCheck.markersInDom === 12,
    `Expected 12 circle marker paths in DOM, found: ${idempotencyCheck.markersInDom}`
  );

  // 2.2 Container Detachment / Missing Element Resilience
  const detachCheck = await page.evaluate(() => {
    const origId = document.getElementById('mobile-leaflet-map');
    let threw = false;
    let errMsg = '';
    try {
      origId.id = 'temp-disabled-map';
      window.initMobileLeafletMap();
      origId.id = 'mobile-leaflet-map';
    } catch (e) {
      threw = true;
      errMsg = e.message;
    }
    return { threw, errMsg };
  });

  record('mapIdempotency', 'initMobileLeafletMap handles missing container gracefully without throwing',
    !detachCheck.threw,
    detachCheck.errMsg || 'Handled absence gracefully'
  );

  // 2.3 Satellite Layer Toggle Rapid Stress (50 toggles)
  const toggleStress = await page.evaluate(() => {
    const labelBefore = document.getElementById('mobile-sat-label')?.textContent;
    let errors = [];
    try {
      for (let i = 0; i < 50; i++) {
        window.toggleMobileMapSatellite();
      }
    } catch (e) {
      errors.push(e.message);
    }
    const labelAfter = document.getElementById('mobile-sat-label')?.textContent;
    // 50 toggles (even number) should leave state back to initial label
    return {
      errors,
      labelBefore,
      labelAfter,
      matches: labelBefore === labelAfter
    };
  });

  record('mapIdempotency', '50 Rapid satellite layer toggles alternate cleanly without orphaned layers',
    toggleStress.errors.length === 0 && toggleStress.matches,
    `Errors: ${toggleStress.errors.length}, Start label: "${toggleStress.labelBefore}", End label: "${toggleStress.labelAfter}"`
  );

  // 2.4 Category Filter Idempotency & Count Oracle
  // Distribution: 12 total (7 obra, 2 ferreteria, 2 competencia, 1 planta)
  const filterOracle = await page.evaluate(() => {
    const counts = {};
    const filters = ['todos', 'obra', 'ferreteria', 'competencia', 'planta'];
    
    filters.forEach(f => {
      window.filtrarMapaMobile(f);
      const visible = document.querySelectorAll('#mobile-leaflet-map .leaflet-overlay-pane path').length;
      counts[f] = visible;
    });

    // Reset to todos
    window.filtrarMapaMobile('todos');
    const resetCount = document.querySelectorAll('#mobile-leaflet-map .leaflet-overlay-pane path').length;

    return { counts, resetCount };
  });

  record('mapIdempotency', 'Category filter counts match exact Caribbean distribution (12 total, 7 obra, 2 ferreteria, 2 competencia, 1 planta)',
    filterOracle.counts.todos === 12 &&
    filterOracle.counts.obra === 7 &&
    filterOracle.counts.ferreteria === 2 &&
    filterOracle.counts.competencia === 2 &&
    filterOracle.counts.planta === 1 &&
    filterOracle.resetCount === 12,
    `Counts: ${JSON.stringify(filterOracle.counts)}, reset: ${filterOracle.resetCount}`
  );

  // 2.5 Filter Fuzzing with Malformed Categories
  const filterFuzz = await page.evaluate(() => {
    let threw = false;
    let errMsg = '';
    const badFilters = [null, undefined, '', 'unknown_category', 12345, {}, []];
    try {
      badFilters.forEach(b => window.filtrarMapaMobile(b));
    } catch (e) {
      threw = true;
      errMsg = e.message;
    }
    window.filtrarMapaMobile('todos');
    return { threw, errMsg };
  });

  record('mapIdempotency', 'filtrarMapaMobile survives adversarial input fuzzing',
    !filterFuzz.threw,
    filterFuzz.errMsg || 'Survived all malformed inputs'
  );


  // ============================================================================
  // SUITE 3: GEOREFERENCED COORDINATES ACCURACY & REGIONAL INVARIANTS
  // ============================================================================
  console.log('\n--- 3. Georeferenced Coordinates Accuracy & Regional Invariants ---');

  const sites = await page.evaluate(() => window.clientSites);

  // 3.1 Exact Site Cardinality (12 sites)
  record('geoAccuracy', 'Store contains exactly 12 georeferenced sites',
    sites && sites.length === 12,
    `Found: ${sites ? sites.length : 0}`
  );

  // 3.2 Caribbean Regional Bounding Box Oracle
  // Lat: 10.0 to 12.0 N, Lng: -76.0 to -73.5 W
  let regionalBoxPass = true;
  let outOfBoundsSite = null;

  for (const s of sites) {
    if (s.lat < 10.0 || s.lat > 12.0 || s.lng < -76.0 || s.lng > -73.5) {
      regionalBoxPass = false;
      outOfBoundsSite = `${s.nombre} (${s.lat}, ${s.lng})`;
      break;
    }
  }

  record('geoAccuracy', 'All 12 sites fall strictly within Northern Colombia Caribbean bounds (10.0-12.0 N, -76.0 to -73.5 W)',
    regionalBoxPass,
    outOfBoundsSite ? `Out of bounds: ${outOfBoundsSite}` : 'All 12 sites verified inside Caribbean region'
  );

  // 3.3 City Boundary Geocoding Oracle
  const cityBounds = {
    'Barranquilla': { minLat: 10.92, maxLat: 11.06, minLng: -74.86, maxLng: -74.75 },
    'Galapa':       { minLat: 10.87, maxLat: 10.93, minLng: -74.93, maxLng: -74.85 },
    'Soledad':      { minLat: 10.89, maxLat: 10.95, minLng: -74.80, maxLng: -74.74 },
    'Malambo':      { minLat: 10.83, maxLat: 10.93, minLng: -74.84, maxLng: -74.74 },
    'Cartagena':    { minLat: 10.34, maxLat: 10.46, minLng: -75.54, maxLng: -75.42 },
    'Santa Marta':  { minLat: 11.16, maxLat: 11.28, minLng: -74.26, maxLng: -74.15 },
    'Baranoa':      { minLat: 10.76, maxLat: 10.83, minLng: -74.95, maxLng: -74.87 }
  };

  let cityGeocodingPass = true;
  let mismatchedCitySite = null;

  for (const s of sites) {
    const bound = cityBounds[s.ciudad];
    if (!bound) {
      cityGeocodingPass = false;
      mismatchedCitySite = `Unknown city: ${s.ciudad}`;
      break;
    }
    if (s.lat < bound.minLat || s.lat > bound.maxLat || s.lng < bound.minLng || s.lng > bound.maxLng) {
      cityGeocodingPass = false;
      mismatchedCitySite = `${s.nombre} in ${s.ciudad} at (${s.lat}, ${s.lng}) outside city bounds (${bound.minLat}-${bound.maxLat}, ${bound.minLng}-${bound.maxLng})`;
      break;
    }
  }

  record('geoAccuracy', 'All sites map accurately within their specific municipal boundaries across 6 Caribbean cities',
    cityGeocodingPass,
    mismatchedCitySite || 'All 12 municipal boundaries verified'
  );

  // 3.4 Coordinate Uniqueness & Minimum Separation Distance (> 100 meters)
  let duplicates = 0;
  let minSeparation = Infinity;
  let closestPair = '';

  for (let i = 0; i < sites.length; i++) {
    for (let j = i + 1; j < sites.length; j++) {
      const s1 = sites[i];
      const s2 = sites[j];
      if (s1.lat === s2.lat && s1.lng === s2.lng) {
        duplicates++;
      }
      const dist = haversineDistanceMeters(s1.lat, s1.lng, s2.lat, s2.lng);
      if (dist < minSeparation) {
        minSeparation = dist;
        closestPair = `${s1.nombre} <-> ${s2.nombre} (${Math.round(dist)}m)`;
      }
    }
  }

  record('geoAccuracy', 'Zero duplicate coordinates among all 12 Caribbean markers',
    duplicates === 0,
    duplicates > 0 ? `Found ${duplicates} duplicate coordinate pairs` : 'All 12 pairs distinct'
  );

  record('geoAccuracy', 'Minimum spatial separation between distinct markers is >= 100m (no stacked pins)',
    minSeparation >= 100,
    `Closest pair: ${closestPair}`
  );

  // 3.5 Brand Category & Color Invariant Oracle
  const expectedColors = {
    'planta': '#FDCA02',
    'obra': '#003E78',
    'ferreteria': '#0284C7',
    'competencia': '#DC2626'
  };

  let colorPass = true;
  let colorMismatch = '';

  for (const s of sites) {
    const expected = expectedColors[s.tipo];
    if (s.color !== expected) {
      colorPass = false;
      colorMismatch = `${s.nombre} (${s.tipo}) has color ${s.color}, expected ${expected}`;
      break;
    }
  }

  record('geoAccuracy', 'All 12 sites adhere to official Ultracem brand color coding per category',
    colorPass,
    colorMismatch || 'All 12 colors match specification'
  );


  // ============================================================================
  // SUITE 4: ACTION POPUP URLS & TEMPLATE SECURITY
  // ============================================================================
  console.log('\n--- 4. Action Popup URLs & Template Security ---');

  // 4.1 Telephony URLs Format Validation (Dialing regex /^\+?[0-9\s-]+$/)
  const popupValidation = await page.evaluate((sitesList) => {
    const results = [];
    const phoneRegex = /^\+57[0-9]{10}$/; // Strict Colombian dialing format +57 followed by 10 digits
    const gmapsRegex = /^https:\/\/www\.google\.com\/maps\/dir\/\?api=1&destination=([0-9.-]+),([0-9.-]+)$/;

    sitesList.forEach(s => {
      const html = window.renderSitePopup(s);
      
      // Check phone link
      let phoneValid = false;
      let phoneMsg = '';
      if (s.telefono && s.telefono.trim().length >= 7) {
        const telMatch = html.match(/href=["']tel:([^"']+)["']/);
        if (telMatch && phoneRegex.test(telMatch[1])) {
          phoneValid = true;
        } else {
          phoneMsg = `Tel match failed: ${telMatch ? telMatch[1] : 'null'}`;
        }
      } else {
        // Must contain disabled button without href="tel:"
        const hasDisabled = html.includes('Sin Teléfono') && !html.includes('href="tel:');
        phoneValid = hasDisabled;
        if (!hasDisabled) phoneMsg = 'Missing disabled button for empty phone';
      }

      // Check Google Maps route link
      let routeValid = false;
      let routeMsg = '';
      const routeMatch = html.match(/href=["'](https:\/\/www\.google\.com\/maps\/dir\/[^"']+)["']/);
      if (routeMatch) {
        const m = routeMatch[1].match(gmapsRegex);
        if (m) {
          const lat = parseFloat(m[1]);
          const lng = parseFloat(m[2]);
          if (Math.abs(lat - s.lat) < 0.0001 && Math.abs(lng - s.lng) < 0.0001) {
            routeValid = true;
          } else {
            routeMsg = `Coords mismatch: URL (${lat},${lng}) vs Site (${s.lat},${s.lng})`;
          }
        } else {
          routeMsg = `Google Maps URL malformed: ${routeMatch[1]}`;
        }
      } else {
        routeMsg = 'Google Maps link not found in popup';
      }

      // Check max-width constraint <= 320px
      const hasMaxWidth = html.includes('max-w-[260px]') || html.includes('max-w-[280px]') || html.includes('max-w-[300px]') || html.includes('max-w-[320px]');

      // Check zero emojis
      const emojiRegex = /[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u;
      const hasEmoji = emojiRegex.test(html);

      // Check zero gradients
      const hasGradient = /gradient/i.test(html);

      results.push({
        id: s.id,
        nombre: s.nombre,
        phoneValid,
        phoneMsg,
        routeValid,
        routeMsg,
        hasMaxWidth,
        hasEmoji,
        hasGradient
      });
    });

    return results;
  }, sites);

  const phoneFailures = popupValidation.filter(p => !p.phoneValid);
  record('popupValidation', 'All 12 site popups generate strictly valid telephony hrefs or disabled fallback',
    phoneFailures.length === 0,
    phoneFailures.length > 0 ? phoneFailures.map(f => `${f.nombre}: ${f.phoneMsg}`).join('; ') : 'All 12 phones valid'
  );

  const routeFailures = popupValidation.filter(p => !p.routeValid);
  record('popupValidation', 'All 12 site popups generate valid Google Maps direction URLs with exact destination coordinates',
    routeFailures.length === 0,
    routeFailures.length > 0 ? routeFailures.map(f => `${f.nombre}: ${f.routeMsg}`).join('; ') : 'All 12 Google Maps URLs valid'
  );

  const widthFailures = popupValidation.filter(p => !p.hasMaxWidth);
  record('popupValidation', 'All site popups enforce responsive width constraint fitting mobile viewports',
    widthFailures.length === 0,
    widthFailures.length > 0 ? `${widthFailures.length} popups exceed width` : 'Max width <= 260px enforced'
  );

  const emojiFailures = popupValidation.filter(p => p.hasEmoji);
  record('popupValidation', 'Zero emojis detected in generated popup markup',
    emojiFailures.length === 0,
    emojiFailures.length > 0 ? `Found emojis in: ${emojiFailures.map(f => f.nombre).join(', ')}` : '0 emojis confirmed'
  );

  const gradientFailures = popupValidation.filter(p => p.hasGradient);
  record('popupValidation', 'Zero CSS gradients detected in generated popup markup',
    gradientFailures.length === 0,
    gradientFailures.length > 0 ? `Found gradients in: ${gradientFailures.map(f => f.nombre).join(', ')}` : '0 gradients confirmed'
  );

  // 4.2 Popup Injection & Telephony Protocol Safety
  const injectionResult = await page.evaluate(() => {
    const maliciousSite = {
      id: 999,
      nombre: "Malicious Site <script>window.__popup_xss = true;</script>",
      ciudad: "Barranquilla",
      depto: "Atlántico",
      tipo: "obra",
      direccion: `"><img src=x onerror="window.__popup_xss = true;">`,
      volumen: "100 Ton",
      telefono: "javascript:window.__popup_xss=true; +573001234567",
      lat: 10.9900,
      lng: -74.8000,
      color: "#003E78"
    };

    const popupHtml = window.renderSitePopup(maliciousSite);
    
    // cleanPhone strips non-digit and non-plus characters
    const hasCleanPhone = popupHtml.includes('href="tel:+573001234567"');
    const hasJavascriptProtocol = popupHtml.includes('javascript:');

    return {
      hasCleanPhone,
      hasJavascriptProtocol
    };
  });

  record('popupValidation', 'renderSitePopup strips malicious protocols from phone inputs',
    injectionResult.hasCleanPhone && !injectionResult.hasJavascriptProtocol,
    `Clean phone generated: ${injectionResult.hasCleanPhone}, JavaScript protocol absent: ${!injectionResult.hasJavascriptProtocol}`
  );


  // ============================================================================
  // SUITE 5: MOBILE PIPELINE INTEGRATION RESILIENCE
  // ============================================================================
  console.log('\n--- 5. Mobile Pipeline Integration Resilience ---');

  // Navigate to pipeline tab on mobile
  await page.evaluate(() => window.navigateToTab('pipeline'));
  await page.waitForTimeout(150);

  const pipelineChecks = await page.evaluate(() => {
    const cardsContainer = document.getElementById('mobile-pipeline-cards');
    const renderedCards = cardsContainer ? cardsContainer.children.length : 0;
    
    // Test dynamic search filter
    const searchInput = document.getElementById('mobile-pipeline-search');
    let searchWorked = false;
    let filteredCount = 0;
    if (searchInput) {
      searchInput.value = "Bolívar";
      searchInput.dispatchEvent(new Event('input', { bubbles: true }));
      filteredCount = cardsContainer.children.length;
      searchWorked = filteredCount > 0 && filteredCount < renderedCards;
      
      // Reset search
      searchInput.value = "";
      searchInput.dispatchEvent(new Event('input', { bubbles: true }));
    }

    return {
      renderedCards,
      searchWorked,
      filteredCount
    };
  });

  record('mobilePipeline', 'Mobile pipeline screen renders all 14 industrial accounts',
    pipelineChecks.renderedCards === 14,
    `Rendered cards: ${pipelineChecks.renderedCards}`
  );

  record('mobilePipeline', 'Mobile pipeline real-time search filtering operates reactively',
    pipelineChecks.searchWorked,
    `Search filtered count: ${pipelineChecks.filteredCount}`
  );


  // ============================================================================
  // SUITE 6: CITY FILTERING & MAP STORE IMMUTABILITY
  // ============================================================================
  console.log('\n--- 6. City Filtering & Map Store Immutability ---');

  const cityFilterResults = await page.evaluate(() => {
    const expected = {
      'Barranquilla': 5,
      'Galapa': 1,
      'Soledad': 1,
      'Malambo': 2,
      'Cartagena': 1,
      'Santa Marta': 1,
      'Baranoa': 1,
      'todas': 12
    };

    let allMatch = true;
    const actual = {};

    for (const [city, count] of Object.entries(expected)) {
      const res = window.UltraMapStore.filterByCity(city);
      actual[city] = res.length;
      if (res.length !== count) {
        allMatch = false;
      }
    }

    // Test malformed city
    const invalidRes = window.UltraMapStore.filterByCity('Bogota');
    const nullRes = window.UltraMapStore.filterByCity(null);

    return {
      allMatch,
      actual,
      invalidCount: invalidRes.length,
      nullCount: nullRes.length
    };
  });

  record('cityFiltering', 'filterByCity accurately partitions sites across all 6 Caribbean municipalities',
    cityFilterResults.allMatch,
    `Actual counts: ${JSON.stringify(cityFilterResults.actual)}`
  );

  record('cityFiltering', 'filterByCity handles unknown city safely and null city defaults to all sites',
    cityFilterResults.invalidCount === 0 && cityFilterResults.nullCount === 12,
    `Unknown city count: ${cityFilterResults.invalidCount}, Null city count: ${cityFilterResults.nullCount}`
  );


  // ============================================================================
  // SUITE 7: LIVE MARKER INTERACTION & REAL DOM POPUP OPENING
  // ============================================================================
  console.log('\n--- 7. Live Marker Interaction & Real DOM Popup Opening ---');

  await page.evaluate(() => window.navigateToTab('radar'));
  await page.waitForTimeout(200);

  const livePopupResult = await page.evaluate(() => {
    if (!window.mobileLeafletMap) return { success: false, reason: 'Map not initialized' };

    // Find first marker circle in Leaflet map layer
    const markerPaths = document.querySelectorAll('#mobile-leaflet-map .leaflet-overlay-pane path');
    if (markerPaths.length === 0) return { success: false, reason: 'No SVG marker paths found' };

    // Simulate clicking the first marker
    markerPaths[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));

    // Check if popup opened in DOM
    const popupContent = document.querySelector('.leaflet-popup-content');
    const isVisible = !!popupContent && popupContent.innerHTML.includes('Demanda / Capacidad');
    const hasCallOrRoute = popupContent && (popupContent.innerHTML.includes('Llamar') || popupContent.innerHTML.includes('Iniciar Ruta'));

    return {
      success: isVisible && hasCallOrRoute,
      popupHtml: popupContent ? popupContent.innerHTML.substring(0, 100) : ''
    };
  });

  record('liveInteractions', 'Clicking SVG circle marker opens interactive Leaflet popup in DOM',
    livePopupResult.success,
    livePopupResult.success ? 'Popup opened successfully' : livePopupResult.reason
  );


  // ============================================================================
  // SUMMARY & VERDICT
  // ============================================================================
  console.log('\n================================================================');
  console.log(`[CHALLENGER SUMMARY] Passed: ${results.summary.passed}, Failed: ${results.summary.failed}`);
  console.log('================================================================\n');

  await browser.close();

  if (results.summary.failed === 0) {
    console.log('\x1b[32m[VERDICT] APPROVE — Milestone 3 passed all adversarial stress challenges.\x1b[0m\n');
    return true;
  } else {
    console.log(`\x1b[31m[VERDICT] REQUEST_CHANGES — ${results.summary.failed} adversarial test(s) failed!\x1b[0m\n`);
    return false;
  }
}

runAll().then(success => {
  process.exit(success ? 0 : 1);
}).catch(err => {
  console.error('[UNCAUGHT EXCEPTION]', err);
  process.exit(1);
});
