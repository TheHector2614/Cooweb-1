const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function capture() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const fileUrl = 'http://localhost:3000/';
  console.log(`Navigating to: ${fileUrl}`);

  const artifactScreenshotsDir = path.resolve('C:/Users/HP 14/.gemini/antigravity/brain/86e577bd-2a1d-484f-8081-c1d72b940ae4/screenshots');
  if (!fs.existsSync(artifactScreenshotsDir)) {
    fs.mkdirSync(artifactScreenshotsDir, { recursive: true });
  }
  const localScreenshotsDir = path.resolve(__dirname, '../screenshots');
  if (!fs.existsSync(localScreenshotsDir)) {
    fs.mkdirSync(localScreenshotsDir, { recursive: true });
  }

  function saveCopy(filename, buffer) {
    const p1 = path.join(localScreenshotsDir, filename);
    const p2 = path.join(artifactScreenshotsDir, filename);
    fs.writeFileSync(p1, buffer);
    fs.writeFileSync(p2, buffer);
    console.log(`Saved screenshot: ${filename} (Local + Brain Artifact)`);
  }

  // 1. DUAL SPLIT: CRM ESCRITORIO + CELULAR MÓVIL (1720x1050)
  console.log('Capturing Dual Split: CRM Escritorio + Celular...');
  await page.setViewportSize({ width: 1720, height: 1050 });
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  await page.evaluate(() => {
    changeViewMode('dual-crm-phone');
    switchDesktopCrmTab('racha');
  });
  await page.waitForTimeout(600);

  let buf = await page.screenshot({ fullPage: false });
  saveCopy('ultracem_dual_crm_phone.png', buf);

  // 2. DUAL SPLIT: PRD MAESTRO + CELULAR AL LADO (1720x1050)
  console.log('Capturing Dual Split: PRD Maestro + Celular...');
  await page.evaluate(() => {
    changeViewMode('dual-prd-phone');
  });
  await page.waitForTimeout(600);
  buf = await page.screenshot({ fullPage: false });
  saveCopy('ultracem_dual_prd_phone.png', buf);

  // 3. DUAL SPLIT: CRM ESCRITORIO + PRD MAESTRO (1720x1050)
  console.log('Capturing Dual Split: CRM Escritorio + PRD Maestro...');
  await page.evaluate(() => {
    changeViewMode('dual-crm-prd');
  });
  await page.waitForTimeout(600);
  buf = await page.screenshot({ fullPage: false });
  saveCopy('ultracem_dual_crm_prd.png', buf);

  // 4. MAPA CARTOGRAFÍA CON CARTODB VOYAGER (NO 403 ERROR!)
  console.log('Capturing Desktop Map with CartoDB Voyager...');
  await page.evaluate(() => {
    changeViewMode('desktop');
    switchDesktopCrmTab('mapa');
  });
  await page.waitForTimeout(1200);
  buf = await page.screenshot({ fullPage: false });
  saveCopy('ultracem_mapa_cartodb.png', buf);

  // 5. PRD MAESTRO FULL CANVAS VIEW (1280x1200)
  console.log('Capturing PRD Maestro Full View...');
  await page.setViewportSize({ width: 1280, height: 1200 });
  await page.evaluate(() => {
    changeViewMode('prd');
  });
  await page.waitForTimeout(600);
  buf = await page.screenshot({ fullPage: false });
  saveCopy('ultracem_prd_comprehensive.png', buf);

  await browser.close();
  console.log('All screenshots captured successfully!');
}

capture().catch(err => {
  console.error('Error capturing screenshots:', err);
  process.exit(1);
});
