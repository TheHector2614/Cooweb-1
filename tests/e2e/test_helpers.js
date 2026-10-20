/**
 * Test Helpers & Shared Infrastructure for UltraRacha E2E Test Suite
 * Project: Ultracem UltraRacha CRM
 */

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const { pathToFileURL } = require('url');

const PROJECT_ROOT = path.resolve(__dirname, '../..');
const INDEX_HTML_PATH = path.join(PROJECT_ROOT, 'index.html');
const SERVER_JS_PATH = path.join(PROJECT_ROOT, 'server.js');

let sharedBrowser = null;

// Comprehensive Unicode Emoji regular expression covering all Unicode standard blocks
const EMOJI_REGEX = /(?:[\u{1F600}-\u{1F64F}]|[\u{1F300}-\u{1F5FF}]|[\u{1F680}-\u{1F6FF}]|[\u{1F700}-\u{1F77F}]|[\u{1F780}-\u{1F7FF}]|[\u{1F800}-\u{1F8FF}]|[\u{1F900}-\u{1F9FF}]|[\u{1FA00}-\u{1FA6F}]|[\u{1FA70}-\u{1FAFF}]|[\u{2600}-\u{26FF}]|[\u{2700}-\u{27BF}]|[\u{2300}-\u{23FF}]|[\u{2B50}\u{2B55}]|[\u{203C}\u{2049}]|[\u{25AA}\u{25AB}\u{25B6}\u{25C0}\u{25FB}-\u{25FE}]|[\u{00A9}\u{00AE}]|[\u{2122}\u{2139}]|[\u{1F1E6}-\u{1F1FF}])/gu;

// CSS Gradient patterns strictly prohibited by R1 & Project rules
const GRADIENT_PATTERNS = [
  /linear-gradient\s*\(/i,
  /radial-gradient\s*\(/i,
  /conic-gradient\s*\(/i,
  /bg-gradient-to-[a-z]+/i,
  /bg-gradient-/i
];

function readIndexHtml() {
  return fs.readFileSync(INDEX_HTML_PATH, 'utf-8');
}

function readServerJs() {
  return fs.readFileSync(SERVER_JS_PATH, 'utf-8');
}

function findEmojis(text) {
  const matches = [];
  const lines = text.split('\n');
  lines.forEach((line, idx) => {
    const found = line.match(EMOJI_REGEX);
    if (found) {
      found.forEach(char => {
        matches.push({ line: idx + 1, char, codePoint: char.codePointAt(0).toString(16) });
      });
    }
  });
  return matches;
}

function findGradients(text) {
  const matches = [];
  const lines = text.split('\n');
  lines.forEach((line, idx) => {
    GRADIENT_PATTERNS.forEach(pat => {
      const found = line.match(pat);
      if (found) {
        matches.push({ line: idx + 1, pattern: pat.toString(), match: found[0], snippet: line.trim() });
      }
    });
  });
  return matches;
}

async function getBrowser() {
  if (!sharedBrowser) {
    sharedBrowser = await chromium.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
    });
  }
  return sharedBrowser;
}

async function closeBrowser() {
  if (sharedBrowser) {
    await sharedBrowser.close();
    sharedBrowser = null;
  }
}

async function createPage(options = {}) {
  const browser = await getBrowser();
  const context = await browser.newContext({
    viewport: options.viewport || { width: 1280, height: 800 },
    userAgent: options.userAgent || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) UltraRacha-E2E-Tester',
    ...(options.contextOptions || {})
  });
  const page = await context.newPage();
  
  const fileUrl = pathToFileURL(INDEX_HTML_PATH).href;
  await page.goto(fileUrl, { waitUntil: 'load' });
  return { page, context };
}

async function runTest(testName, fn) {
  const t0 = Date.now();
  try {
    await fn();
    return { name: testName, passed: true, durationMs: Date.now() - t0 };
  } catch (err) {
    return {
      name: testName,
      passed: false,
      durationMs: Date.now() - t0,
      error: err.message || String(err),
      stack: err.stack
    };
  }
}

module.exports = {
  PROJECT_ROOT,
  INDEX_HTML_PATH,
  SERVER_JS_PATH,
  EMOJI_REGEX,
  GRADIENT_PATTERNS,
  readIndexHtml,
  readServerJs,
  findEmojis,
  findGradients,
  getBrowser,
  closeBrowser,
  createPage,
  runTest
};
