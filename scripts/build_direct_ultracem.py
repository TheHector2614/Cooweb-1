# -*- coding: utf-8 -*-
"""
Ultracem Direct Compiler v2
Compiles index.html and brain artifact prototype directly and reliably.
1. 100% Pure Ultracem S.A.S. branding (0 Semillero, 0 CooWeb).
2. Desktop application with the same features and interactions as the mobile app.
3. Don Fraguado animated vector SVG mascot in Desktop header.
4. Leaflet map using CartoDB Voyager (0 403 errors, high reliability).
5. Comprehensive Master PRD & Brand Book with 7 extensive chapters.
6. Multi-option Flexible Split Screen system (CRM+Phone, PRD+Phone, CRM+PRD, Solo Desktop, Solo Mobile, Solo PRD, plus custom controls).
7. Primary Ultracem brand colors: Amarillo (#FDCA02), Azul Oscuro (#003E78 / #0A233F), Blanco (#FFFFFF).
8. 100% Solid colors only (0 gradients).
"""

import os
import re
import sys

from generate_ultracem_desktop_crm import get_ultracem_desktop_crm_html
from generate_prd_html import get_prd_html

def remove_gradients(html_str):
    """Replaces all gradient utility classes and CSS gradients with solid colors"""
    replacements = [
        (r'background:\s*linear-gradient\([^;]+\);', 'background: #003E78; border: 2px solid #FDCA02;'),
        (r'bg-gradient-to-r from-\[#0F172A\] via-\[#132A3E\] to-\[#0F172A\]', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-\[#0F172A\] via-\[#003E78\] to-\[#0F172A\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-\[#0033A0\] to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-900 to-\[#003E78\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-900 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-slate-900 via-slate-800 to-\[#004797\]', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-sky-900 via-\[#004797\] to-blue-950', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-amber-500 via-amber-600 to-orange-600', 'bg-[#FDCA02]'),
        (r'bg-gradient-to-r from-\[#002D80\] via-\[#003B99\] to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-600 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-teal-900 via-\[#0F172A\] to-slate-900', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-slate-900 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-\[#003E78\] to-\[#005AB5\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-b from-amber-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-slate-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-amber-50/40 to-white', 'bg-white'),
        (r'bg-gradient-to-[a-z0-9/\[\]#_-]+(?:\s+from-[a-z0-9/\[\]#_-]+)?(?:\s+via-[a-z0-9/\[\]#_-]+)?(?:\s+to-[a-z0-9/\[\]#_-]+)?', 'bg-[#003E78]'),
    ]
    for pattern, replacement in replacements:
        html_str = re.sub(pattern, replacement, html_str)
    return html_str

def sanitize_branding(html_str):
    """Replaces all Semillero / CooWeb mentions with Ultracem"""
    html_str = re.sub(r'(?i)semillero by cooweb', 'Ultracem', html_str)
    html_str = re.sub(r'(?i)by cooweb', '', html_str)
    html_str = re.sub(r'(?i)semillero', 'Ultracem', html_str)
    html_str = re.sub(r'(?i)cooweb', 'Ultracem', html_str)
    html_str = html_str.replace("Cuidar el potencial para hacerlo crecer", "Calidad, Resistencia y Rendimiento")
    return html_str

def main():
    print("Reading base64 logo...")
    base64_logo_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\assets\logo_base64.txt"
    with open(base64_logo_path, "r", encoding="utf-8") as f:
        logo_base64 = f.read().strip()

    print("Reading base template from build_duolingo_pro_v2.py...")
    with open("scripts/build_duolingo_pro_v2.py", "r", encoding="utf-8") as f:
        src = f.read()

    doc_start = src.find("<!DOCTYPE html>")
    doc_end = src.find("</html>") + 7
    base_html = src[doc_start:doc_end]

    # Convert python f-string escapes to real single curly braces and interpolate logo
    base_html = base_html.replace('{logo_base64}', logo_base64).replace('{{', '{').replace('}}', '}')

    # Extract phone canvas
    p_start = base_html.find("<!-- Phone Canvas Frame:")
    pos_sup = base_html.find("<!-- 2. VISTA SUPERVISOR WEB")
    phone_canvas_raw = base_html[p_start:pos_sup].strip()

    # Clean up phone canvas
    phone_canvas_raw = re.sub(
        r'<div id="activation-stage-card".*?</div>\s*</div>',
        '',
        phone_canvas_raw,
        flags=re.DOTALL
    )

    # Balance div hierarchy: strip the extra outer column closing div from phone_canvas_raw
    last_div_idx = phone_canvas_raw.rfind("</div>")
    if last_div_idx != -1:
        phone_canvas_raw = phone_canvas_raw[:last_div_idx].strip()

    print(f"Extracted phone canvas: {len(phone_canvas_raw)} characters")

    # Desktop CRM HTML
    desktop_crm_html = get_ultracem_desktop_crm_html().replace('{logo_base64}', logo_base64)
    print(f"Generated Desktop CRM HTML: {len(desktop_crm_html)} characters")

    # PRD HTML
    prd_html = get_prd_html().replace('{logo_base64}', logo_base64)
    print(f"Generated PRD HTML: {len(prd_html)} characters")

    # Header with Flexible Dropdown Selector
    new_header_html = f'''  <header class="w-full bg-[#003E78] border-b-4 border-[#FDCA02] shadow-sm sticky top-0 z-50">
    <div class="max-w-[1780px] mx-auto px-4 sm:px-6 py-2.5 flex items-center justify-between gap-4">
      
      <!-- Brand Logo Ultracem with White Badge & Yellow Accent -->
      <div class="flex items-center space-x-3 select-none">
        <div class="bg-white px-3 py-1 rounded-xl shadow-xs border-2 border-[#FDCA02]">
          <img src="data:image/png;base64,{logo_base64}" alt="Ultracem Cemento y Concreto" class="h-8 object-contain" />
        </div>
        <div class="hidden sm:block">
          <div class="flex items-center space-x-1.5">
            <span class="text-sm font-black tracking-wider uppercase text-white">UltraRacha CRM</span>
            <span class="text-[9px] bg-[#FDCA02] text-[#003E78] font-black px-2 py-0.2 rounded-full uppercase">Oficial</span>
          </div>
          <span class="text-[10px] text-blue-200 block">Ultracem S.A.S. • Planta Galapa, Atlántico</span>
        </div>
      </div>

      <!-- Controls: View Mode Dropdown, AI Setup, Time Simulator -->
      <div class="flex items-center space-x-2.5">
        
        <!-- View Mode Dropdown Selector -->
        <div class="flex items-center space-x-1.5 bg-[#0A233F] p-1 rounded-xl border border-blue-400/40 shadow-xs">
          <label for="view-mode-selector" class="text-[11px] font-bold text-amber-300 hidden md:inline ml-1.5">Vista:</label>
          <select id="view-mode-selector" onchange="changeViewMode(this.value)" class="bg-white text-[#003E78] font-bold text-xs rounded-lg px-2.5 py-1.5 cursor-pointer shadow-xs focus:outline-none border-2 border-[#FDCA02] hover:bg-amber-50 transition-colors">
            <option value="dual-crm-phone" selected>💻 CRM Escritorio + 📱 Celular al lado</option>
            <option value="dual-prd-phone">📑 PRD Maestro + 📱 Celular al lado</option>
            <option value="dual-crm-prd">💻 CRM Escritorio + 📑 PRD Maestro</option>
            <option value="desktop">💻 Solo CRM Escritorio (Completo)</option>
            <option value="mobile">📱 Solo Celular (Móvil en Terreno)</option>
            <option value="prd">📑 Solo PRD Maestro (Canvas Completo)</option>
          </select>
        </div>

        <!-- AI Settings Trigger -->
        <button onclick="openInPhoneAISettings()" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] shadow-xs transition-all" title="Configurar API Key de IA (NVIDIA, DeepSeek, Groq, OpenAI)">
          <span>⚙️</span>
          <span class="hidden lg:inline">IA (Groq / NVIDIA)</span>
        </button>

        <!-- Time Mode Simulation Pill -->
        <div class="hidden xl:flex items-center space-x-1 text-xs border border-blue-400/30 rounded-xl p-1 bg-[#0A233F]">
          <button id="btn-time-day" onclick="setTimeMode('day')" aria-label="Simular 10:00 AM" class="px-2.5 py-1 rounded-lg font-bold bg-white text-[#003E78] text-[11px] transition-all">
            ☀️ 10:00 AM
          </button>
          <button id="btn-time-night" onclick="setTimeMode('night')" aria-label="Simular 10:45 PM" class="px-2.5 py-1 rounded-lg font-semibold text-blue-200 hover:text-white text-[11px] transition-all">
            🌙 10:45 PM
          </button>
        </div>

      </div>
    </div>
  </header>'''

    # Main Workspace Container with Flexible Split Panels
    new_main_html = f'''  <main id="main-content" class="flex-1 w-full mx-auto px-3 sm:px-5 lg:px-6 py-4 transition-all bg-[#F2F1EC]">

    <!-- ============================================================== -->
    <!-- BARRA INTERACTIVA: SELECTOR LIBRE DE PANTALLAS DIVIDIDAS        -->
    <!-- Permite al usuario dividir las pantallas exactamente como desee -->
    <!-- ============================================================== -->
    <div id="split-screen-controller-bar" class="w-full max-w-[1780px] mx-auto mb-4 bg-[#0A233F] text-white rounded-2xl p-3 border-2 border-[#FDCA02] shadow-xs flex flex-wrap items-center justify-between gap-3 text-xs select-none">
      
      <!-- Panel Izquierdo Selector -->
      <div class="flex items-center space-x-2 flex-wrap gap-y-1.5">
        <span class="font-black text-[#FDCA02] uppercase tracking-wider text-[11px] flex items-center mr-1">
          <span class="mr-1">🎛️</span> Panel Izquierdo:
        </span>
        <button id="btn-split-l-crm" onclick="setSplitLeft('crm')" class="px-3 py-1.5 rounded-xl font-bold bg-[#FDCA02] text-[#003E78] shadow-xs transition-all">💻 CRM Escritorio</button>
        <button id="btn-split-l-prd" onclick="setSplitLeft('prd')" class="px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all">📑 PRD Maestro</button>
        <button id="btn-split-l-copiloto" onclick="setSplitLeft('copiloto')" class="px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all">🤖 Copiloto IA</button>
        <button id="btn-split-l-mapa" onclick="setSplitLeft('mapa')" class="px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all">🗺️ Radar B2B</button>
      </div>

      <!-- Panel Derecho Selector -->
      <div class="flex items-center space-x-2 flex-wrap gap-y-1.5">
        <span class="font-black text-[#FDCA02] uppercase tracking-wider text-[11px] flex items-center mr-1">
          Panel Derecho:
        </span>
        <button id="btn-split-r-phone" onclick="setSplitRight('phone')" class="px-3 py-1.5 rounded-xl font-bold bg-[#FDCA02] text-[#003E78] shadow-xs transition-all">📱 Celular Móvil</button>
        <button id="btn-split-r-prd" onclick="setSplitRight('prd')" class="px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all">📑 PRD Maestro</button>
        <button id="btn-split-r-crm" onclick="setSplitRight('crm')" class="px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all">💻 CRM Escritorio</button>
        <button id="btn-split-r-none" onclick="setSplitRight('none')" class="px-3 py-1.5 rounded-xl font-semibold text-rose-300 hover:text-white bg-rose-950/60 border border-rose-500/40 transition-all">❌ Ocultar (100%)</button>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- WORKSPACE PRINCIPAL CON CONTENEDORES DIVIDIDOS FLEXIBLES       -->
    <!-- ============================================================== -->
    <div id="split-workspace-container" class="w-full max-w-[1780px] mx-auto flex flex-col xl:flex-row gap-6 items-start justify-center">

      <!-- ============================================================ -->
      <!-- PANEL IZQUIERDO (PRINCIPAL / AMPLIO)                          -->
      <!-- ============================================================ -->
      <div id="left-split-pane" class="flex-1 w-full min-w-0">
        
        <!-- Contenido 1: CRM Escritorio Completo -->
        <div id="left-content-crm">
{desktop_crm_html}
        </div>

        <!-- Contenido 2: PRD Maestro en Canvas Blanco -->
        <div id="left-content-prd" class="hidden w-full bg-white rounded-3xl p-6 sm:p-10 border-2 border-slate-300 shadow-sm space-y-8 text-slate-800">
{prd_html}
        </div>

      </div>

      <!-- ============================================================ -->
      <!-- PANEL DERECHO (SECUNDARIO / MÓVIL STICKY O PRD AL LADO)       -->
      <!-- ============================================================ -->
      <aside id="right-split-pane" class="w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center">
        
        <!-- Subpanel 1: Celular en Terreno -->
        <div id="right-content-phone" class="w-full flex flex-col items-center">
          <div class="mb-2 text-center">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white border-2 border-[#FDCA02] shadow-xs">
              📱 Asesor Móvil en Terreno
            </span>
          </div>
{phone_canvas_raw}
        </div>

        <!-- Subpanel 2: PRD Maestro al lado -->
        <div id="right-content-prd" class="hidden w-full bg-white rounded-3xl p-5 sm:p-8 border-2 border-slate-300 shadow-sm space-y-6 text-slate-800 max-h-[85vh] overflow-y-auto">
{prd_html}
        </div>

        <!-- Subpanel 3: Mini-CRM Info -->
        <div id="right-content-crm" class="hidden w-full bg-white rounded-3xl p-5 border-2 border-slate-300 shadow-sm text-xs space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-3 h-3 rounded-full bg-[#FDCA02]"></span>
            <strong class="text-[#003E78] text-sm">Ultracem CRM en Panel Derecho</strong>
          </div>
          <p class="text-slate-600">El CRM está configurado actualmente en este panel. Puedes expandirlo al 100% o cambiarlo al panel izquierdo.</p>
          <button onclick="setSplitLeft('crm'); setSplitRight('phone');" class="w-full py-2 bg-[#003E78] text-white font-bold rounded-xl border-2 border-[#FDCA02]">Cambiar a CRM Principal + Celular</button>
        </div>

      </aside>

    </div>

  </main>'''

    # JavaScript Functions to manage Split Workspace, Don Fraguado Mascot, and Leaflet CartoDB Map
    new_js_logic = '''
    // ==============================================================
    // ULTRACEM SPLIT SCREEN CONTROLLER
    // ==============================================================
    let currentLeftView = 'crm';
    let currentRightView = 'phone';

    function setSplitLeft(type) {
      if (typeof playChime === 'function') playChime('click');
      currentLeftView = type;
      
      const crmLeft = document.getElementById('left-content-crm');
      const prdLeft = document.getElementById('left-content-prd');
      const leftPane = document.getElementById('left-split-pane');
      
      if (leftPane) leftPane.classList.remove('hidden');

      if (type === 'crm' || type === 'copiloto' || type === 'mapa') {
        if (crmLeft) crmLeft.classList.remove('hidden');
        if (prdLeft) prdLeft.classList.add('hidden');
        if (type === 'copiloto') switchDesktopCrmTab('copiloto');
        else if (type === 'mapa') switchDesktopCrmTab('mapa');
        else switchDesktopCrmTab('racha');
      } else if (type === 'prd') {
        if (crmLeft) crmLeft.classList.add('hidden');
        if (prdLeft) prdLeft.classList.remove('hidden');
      }

      applyPaneWidths();
      updateSplitToolbarButtons();
      syncDropdownWithSplit();
    }

    function setSplitRight(type) {
      if (typeof playChime === 'function') playChime('click');
      currentRightView = type;

      const rightPane = document.getElementById('right-split-pane');
      const rPhone = document.getElementById('right-content-phone');
      const rPrd = document.getElementById('right-content-prd');
      const rCrm = document.getElementById('right-content-crm');

      if (type === 'none') {
        if (rightPane) rightPane.classList.add('hidden');
      } else {
        if (rightPane) rightPane.classList.remove('hidden');
        if (rPhone) rPhone.classList.toggle('hidden', type !== 'phone');
        if (rPrd) rPrd.classList.toggle('hidden', type !== 'prd');
        if (rCrm) rCrm.classList.toggle('hidden', type !== 'crm');
      }

      applyPaneWidths();
      updateSplitToolbarButtons();
      syncDropdownWithSplit();
    }

    function applyPaneWidths() {
      const leftPane = document.getElementById('left-split-pane');
      const rightPane = document.getElementById('right-split-pane');
      if (!leftPane || !rightPane) return;

      if (currentRightView === 'none') {
        leftPane.className = "w-full max-w-6xl mx-auto min-w-0";
      } else if (currentRightView === 'phone') {
        leftPane.className = "flex-1 w-full min-w-0";
        rightPane.className = "w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center";
      } else {
        // 50% / 50% split for PRD or CRM on the right
        leftPane.className = "w-full xl:w-1/2 min-w-0";
        rightPane.className = "w-full xl:w-1/2 min-w-0 self-start max-h-[88vh] overflow-y-auto";
      }
    }

    function updateSplitToolbarButtons() {
      // Left buttons
      ['crm', 'prd', 'copiloto', 'mapa'].forEach(k => {
        const btn = document.getElementById(`btn-split-l-${k}`);
        if (!btn) return;
        if (currentLeftView === k) {
          btn.className = "px-3 py-1.5 rounded-xl font-bold bg-[#FDCA02] text-[#003E78] shadow-xs transition-all";
        } else {
          btn.className = "px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all";
        }
      });

      // Right buttons
      ['phone', 'prd', 'crm', 'none'].forEach(k => {
        const btn = document.getElementById(`btn-split-r-${k}`);
        if (!btn) return;
        if (currentRightView === k) {
          btn.className = "px-3 py-1.5 rounded-xl font-bold bg-[#FDCA02] text-[#003E78] shadow-xs transition-all";
        } else {
          if (k === 'none') {
            btn.className = "px-3 py-1.5 rounded-xl font-semibold text-rose-300 hover:text-white bg-rose-950/60 border border-rose-500/40 transition-all";
          } else {
            btn.className = "px-3 py-1.5 rounded-xl font-semibold text-slate-300 hover:text-white bg-[#142C47] transition-all";
          }
        }
      });
    }

    function syncDropdownWithSplit() {
      const selector = document.getElementById('view-mode-selector');
      if (!selector) return;
      if (currentLeftView === 'crm' && currentRightView === 'phone') selector.value = 'dual-crm-phone';
      else if (currentLeftView === 'prd' && currentRightView === 'phone') selector.value = 'dual-prd-phone';
      else if (currentLeftView === 'crm' && currentRightView === 'prd') selector.value = 'dual-crm-prd';
      else if (currentLeftView === 'crm' && currentRightView === 'none') selector.value = 'desktop';
      else if (currentLeftView === 'prd' && currentRightView === 'none') selector.value = 'prd';
    }

    function changeViewMode(mode) {
      if (typeof playChime === 'function') playChime('click');
      const selector = document.getElementById('view-mode-selector');
      if (selector && selector.value !== mode) selector.value = mode;

      const leftPane = document.getElementById('left-split-pane');
      const rightPane = document.getElementById('right-split-pane');
      const rPhone = document.getElementById('right-content-phone');

      if (mode === 'dual-crm-phone') {
        setSplitLeft('crm');
        setSplitRight('phone');
        if (typeof showToast === 'function') showToast("💻📱 Vista Dividida: CRM Escritorio + Celular al lado", "info");
      } else if (mode === 'dual-prd-phone') {
        setSplitLeft('prd');
        setSplitRight('phone');
        if (typeof showToast === 'function') showToast("📑📱 Vista Dividida: PRD Maestro + Celular al lado", "info");
      } else if (mode === 'dual-crm-prd') {
        setSplitLeft('crm');
        setSplitRight('prd');
        if (typeof showToast === 'function') showToast("💻📑 Vista Dividida: CRM Escritorio + PRD Maestro", "info");
      } else if (mode === 'desktop') {
        setSplitLeft('crm');
        setSplitRight('none');
        if (typeof showToast === 'function') showToast("💻 Modo Escritorio Completo (100%)", "info");
      } else if (mode === 'mobile') {
        if (leftPane) leftPane.classList.add('hidden');
        if (rightPane) {
          rightPane.classList.remove('hidden');
          rightPane.className = "w-full max-w-[420px] mx-auto flex flex-col items-center py-2";
        }
        if (rPhone) rPhone.classList.remove('hidden');
        currentRightView = 'phone';
        updateSplitToolbarButtons();
        if (typeof showToast === 'function') showToast("📱 Modo Celular Asesor en Terreno", "info");
      } else if (mode === 'prd') {
        setSplitLeft('prd');
        setSplitRight('none');
        if (typeof showToast === 'function') showToast("📑 Modo Especificación PRD Maestro (100%)", "info");
      }
    }

    // ==============================================================
    // DON FRAGUADO MASCOT INTERACTION (DESKTOP)
    // ==============================================================
    let desktopTipsIndex = 0;
    const desktopDonFraguadoTips = [
      "¡Pilas Carlos! Cada bulto de Cemento Estructural Max colocado hoy defiende la obra frente a Argos.",
      "¿Sabías que el Cemento Marino Ultracem resiste hasta un 40% más de sulfatos en cimentaciones costeras?",
      "La racha de 21 días te coloca a solo 140 Ton de entrar al podio con Milena Ospino e Hichel Espitia.",
      "Recuerda: si Cartera tiene bloqueado el cupo, escala el caso antes de las 11:59 PM y tu racha no sufrirá daño.",
      "¡Esa es la actitud de un Asesor Diamante! Planta Galapa tiene los silos listos para despachar mañana."
    ];

    function pokeDesktopMascot() {
      if (typeof playChime === 'function') playChime('poke');
      const container = document.getElementById('desktop-don-fraguado-container');
      const dialogue = document.getElementById('desktop-fraguado-dialogue');
      if (container) {
        container.classList.remove('mascot-wiggle');
        void container.offsetWidth;
        container.classList.add('mascot-wiggle');
      }
      desktopTipsIndex = (desktopTipsIndex + 1) % desktopDonFraguadoTips.length;
      if (dialogue) {
        dialogue.textContent = `"${desktopDonFraguadoTips[desktopTipsIndex]}"`;
      }
      if (typeof showToast === 'function') showToast("💬 Don Fraguado: Consejo de obra actualizado", "info");
    }

    // ==============================================================
    // DESKTOP CRM TAB SWITCHER
    // ==============================================================
    function switchDesktopCrmTab(tabName) {
      if (typeof playChime === 'function') playChime('click');
      const tabs = ['racha', 'copiloto', 'mapa', 'liga', 'perfil'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dcrm-tab-btn-${t}`);
        const sec = document.getElementById(`dcrm-content-${t}`);
        if (t === tabName) {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-all bg-[#FDCA02] text-[#003E78] shadow-xs";
          if (sec) sec.classList.remove('hidden');
        } else {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]";
          if (sec) sec.classList.add('hidden');
        }
      });

      if (tabName === 'mapa') {
        setTimeout(initDesktopColombiaMap, 150);
      }
    }

    // Desktop Client Selection
    let currentSelectedClientId = 1;
    function seleccionarClienteDesktop(id) {
      if (typeof playChime === 'function') playChime('click');
      currentSelectedClientId = id;
      const clients = {
        1: { name: "Constructora Bolívar", subtitle: "Torres del Mar • 120 Ton Cemento Estructural Max", transcript: "Minuta: El ingeniero de Constructora Bolívar confirma necesidad de 40 Ton de Cemento Estructural Max para el vaciado del miércoles..." },
        2: { name: "Ferretería El Constructor", subtitle: "Sede Centro Soledad • 45 Ton Cemento Uso General", transcript: "Minuta: Don Álvaro solicita reposición de 200 bultos de Uso General. Pide confirmar despacho para mañana jueves antes de las 10 AM..." },
        3: { name: "Marval — Altos de Riomar", subtitle: "Torre 3 • 210 Ton Cemento Marino Impermeable", transcript: "Minuta: Verificación de fraguado de losa en Cemento Marino completada sin fisuras. Ensayo de probeta a 7 días cumple norma NTC 121..." }
      };

      const c = clients[id] || clients[1];
      const title = document.getElementById('dconsole-client-name');
      const transcript = document.getElementById('daudio-transcript-text');
      if (title) title.textContent = c.name;
      if (transcript) transcript.textContent = c.transcript;

      [1, 2, 3].forEach(cid => {
        const card = document.getElementById(`dcard-client-${cid}`);
        if (card) {
          if (cid === id) card.classList.add('ring-2', 'ring-[#003E78]');
          else card.classList.remove('ring-2', 'ring-[#003E78]');
        }
      });
      if (typeof showToast === 'function') showToast(`Cliente seleccionado: ${c.name}`, "info");
    }

    // Desktop Filter
    function filtrarClientesDesktop(filter) {
      if (typeof playChime === 'function') playChime('click');
      const btns = {
        'todos': document.getElementById('dfilter-todos'),
        'obras': document.getElementById('dfilter-obras'),
        'ferreterias': document.getElementById('dfilter-ferreterias'),
        'rojos': document.getElementById('dfilter-rojos')
      };
      Object.entries(btns).forEach(([k, b]) => {
        if (!b) return;
        if (k === filter) b.className = "px-3 py-1 rounded-lg font-bold bg-[#003E78] text-white";
        else b.className = "px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200";
      });

      const c1 = document.getElementById('dcard-client-1');
      const c2 = document.getElementById('dcard-client-2');
      const c3 = document.getElementById('dcard-client-3');

      if (filter === 'todos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = '';
      } else if (filter === 'obras') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = '';
      } else if (filter === 'ferreterias') {
        if (c1) c1.style.display = 'none';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = 'none';
      } else if (filter === 'rojos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = 'none';
      }
    }

    // Desktop Audio Recording Simulation
    let isDesktopAudioRecording = false;
    function toggleDesktopAudioRecording() {
      const btn = document.getElementById('dbtn-record-audio');
      const btnText = document.getElementById('dbtn-record-text');
      const badge = document.getElementById('daudio-status-badge');
      const player = document.getElementById('daudio-player');

      if (!isDesktopAudioRecording) {
        isDesktopAudioRecording = true;
        if (typeof playChime === 'function') playChime('click');
        if (btnText) btnText.textContent = "Detener y Transcribir Audio...";
        if (badge) {
          badge.textContent = "Grabando 00:06...";
          badge.className = "text-[10px] bg-rose-600 text-white px-2 py-0.5 rounded-full font-mono-data animate-pulse";
        }
      } else {
        isDesktopAudioRecording = false;
        if (typeof playChime === 'function') playChime('success');
        if (btnText) btnText.textContent = "Grabar Nota de Audio";
        if (badge) {
          badge.textContent = "Audio Guardado & Transcrito";
          badge.className = "text-[10px] bg-emerald-600 text-white px-2 py-0.5 rounded-full font-mono-data";
        }
        if (player && typeof generateSyntheticAudioMemoWav === 'function') {
          const wavBlob = generateSyntheticAudioMemoWav(6);
          player.src = URL.createObjectURL(wavBlob);
          player.load();
        }
        if (typeof showToast === 'function') showToast("🎙️ Nota de voz procesada con Whisper Turbo", "success");
      }
    }

    // Desktop Escalation SLA
    function escalarCasoDesktop() {
      if (typeof playChime === 'function') playChime('success');
      const select = document.getElementById('descalation-dept-select');
      const deptName = select ? select.options[select.selectedIndex].text : "Cartera";
      if (typeof showToast === 'function') showToast(`⚡ Caso escalado a ${deptName}. ¡Racha diaria protegida (+150 XP)!`, "success");
    }

    // Desktop WhatsApp
    function contactarClienteWhatsApp(clienteName) {
      if (typeof playChime === 'function') playChime('click');
      if (typeof showToast === 'function') showToast(`📲 Abriendo WhatsApp para ${clienteName} (+50 XP)`, "success");
    }

    // Desktop Quick Prompts
    function probarPromptRapidoDesktop(promptText) {
      const input = document.getElementById('desktop-chat-input');
      if (input) {
        input.value = promptText;
        enviarConsultaAIDesktop();
      }
    }

    // Desktop AI Chat
    function enviarConsultaAIDesktop() {
      const input = document.getElementById('desktop-chat-input');
      const container = document.getElementById('desktop-chat-messages');
      if (!input || !container) return;
      const text = input.value.trim();
      if (!text) return;

      if (typeof playChime === 'function') playChime('click');
      input.value = '';

      // Append User message
      const uMsg = document.createElement('div');
      uMsg.className = "flex items-start justify-end space-x-2";
      uMsg.innerHTML = `
        <div class="bg-[#003E78] text-white rounded-2xl p-3 max-w-xl text-xs shadow-xs">
          <p>${text}</p>
        </div>
      `;
      container.appendChild(uMsg);
      container.scrollTop = container.scrollHeight;

      // Handle Guardrails: Reject non-business queries
      const lower = text.toLowerCase();
      let aiResponse = "";
      if (lower.includes('ribonucleico') || lower.includes('arn') || lower.includes('adn') || lower.includes('receta') || lower.includes('cocina')) {
        aiResponse = "Estimado asesor: Como Copiloto Comercial de Ultracem, mis parámetros de consulta están certificados exclusivamente para la comercialización de cemento y concreto, dosificaciones bajo norma NTC 121 y acompañamiento en obra civil. ¿Deseas consultar dosificaciones de Cemento Estructural Max o Cemento Marino?";
      } else if (lower.includes('3000') || lower.includes('losa') || lower.includes('dosificaci')) {
        aiResponse = "Para una losa maciza de 3000 PSI (21 MPa) a 28 días con Cemento Gris Estructural Max Ultracem (NTC 121), la dosificación recomendada por m³ es: 350 kg de Cemento (7 bultos de 50 kg), 0.55 m³ de arena lavada de río, 0.65 m³ de triturado de 1/2 pulgada y 180 litros de agua (relación a/c 0.51).";
      } else if (lower.includes('argos') || lower.includes('competencia') || lower.includes('descuento')) {
        aiResponse = "Argumento de defensa frente al descuento de Argos: 'En Ultracem garantizamos curva de resistencia temprana superior a los 3 días que le ahorra al constructor hasta 24 horas en el desencofre de placas, reduciendo costos de formaleta que superan ampliamente los $500 del bulto. Además, nuestro laboratorio de Planta Galapa expide los certificados de rotura sin costo adicional'.";
      } else {
        aiResponse = `Entendido. Con base en las especificaciones de Cemento Ultracem NTC 121 y los despachos programados desde Planta Galapa, te sugiero ofrecer Cemento Estructural Max con entrega directa en obra para asegurar el cumplimiento de la racha de recompra.`;
      }

      setTimeout(() => {
        if (typeof playChime === 'function') playChime('success');
        const aiMsg = document.createElement('div');
        aiMsg.className = "flex items-start space-x-3";
        aiMsg.innerHTML = `
          <div class="w-8 h-8 rounded-full bg-[#003E78] text-[#FDCA02] font-black flex items-center justify-center text-xs flex-shrink-0">U</div>
          <div class="bg-slate-100 rounded-2xl p-3.5 max-w-2xl text-slate-800 leading-relaxed space-y-1 shadow-xs">
            <div class="font-bold text-[#003E78]">Copiloto Comercial Ultracem</div>
            <p>${aiResponse}</p>
          </div>
        `;
        container.appendChild(aiMsg);
        container.scrollTop = container.scrollHeight;
      }, 400);
    }

    // Desktop Map Sub-views
    function switchDesktopMapSubView(sub) {
      if (typeof playChime === 'function') playChime('click');
      const bMap = document.getElementById('dmap-sub-btn-map');
      const bPros = document.getElementById('dmap-sub-btn-prospects');
      const vMap = document.getElementById('dmap-view-container');
      const vPros = document.getElementById('dprospects-view-container');

      if (sub === 'mapa') {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (vMap) vMap.classList.remove('hidden');
        if (vPros) vPros.classList.add('hidden');
        setTimeout(initDesktopColombiaMap, 100);
      } else {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (vMap) vMap.classList.add('hidden');
        if (vPros) vPros.classList.remove('hidden');
      }
    }

    // Leaflet Desktop Map Initializer with CartoDB Voyager
    let desktopLeafletMap = null;
    let desktopSatelliteActive = false;
    let desktopSatLayer = null;

    const clientSites = [
      { nombre: "Ultracem Planta Galapa (Central)", ciudad: "Galapa, Atlántico", tipo: "planta", lat: 10.9022, lng: -74.8911 },
      { nombre: "Constructora Bolívar - Torres del Mar", ciudad: "Barranquilla", tipo: "obra", lat: 11.0125, lng: -74.8214 },
      { nombre: "Ferretería El Constructor", ciudad: "Soledad", tipo: "ferreteria", lat: 10.9214, lng: -74.7712 },
      { nombre: "Marval — Altos de Riomar", ciudad: "Barranquilla", tipo: "obra", lat: 11.0089, lng: -74.8190 },
      { nombre: "Argos Vía 40 (Competencia)", ciudad: "Barranquilla", tipo: "competencia", lat: 10.9980, lng: -74.7810 },
      { nombre: "Cemex Caracolí (Competencia)", ciudad: "Malambo", tipo: "competencia", lat: 10.9100, lng: -74.8100 },
      { nombre: "Concretos del Norte", ciudad: "Barranquilla", tipo: "prospecto", lat: 10.9850, lng: -74.8020 },
      { nombre: "Prefabricados del Caribe", ciudad: "Malambo", tipo: "prospecto", lat: 10.8600, lng: -74.7700 },
      { nombre: "Ferretería Metrópolis", ciudad: "Barranquilla", tipo: "ferreteria", lat: 10.9500, lng: -74.7900 },
      { nombre: "Amarilo — Parque Heredia", ciudad: "Cartagena", tipo: "obra", lat: 10.3950, lng: -75.4750 },
      { nombre: "Obycon — Puerto Madero", ciudad: "Santa Marta", tipo: "obra", lat: 11.2350, lng: -74.2000 },
      { nombre: "Pavimentos del Atlántico", ciudad: "Baranoa", tipo: "prospecto", lat: 10.7950, lng: -74.9150 }
    ];

    function initDesktopColombiaMap() {
      const container = document.getElementById('desktop-colombia-map');
      if (!container) return;
      if (desktopLeafletMap) {
        desktopLeafletMap.invalidateSize();
        return;
      }
      if (typeof L === 'undefined') {
        console.warn('Leaflet is loading...');
        setTimeout(initDesktopColombiaMap, 300);
        return;
      }

      desktopLeafletMap = L.map('desktop-colombia-map', {
        center: [10.9639, -74.7964],
        zoom: 11
      });

      // ESRI World Street Map - High resolution, crystal clear, 0 API key required, 0 watermarks!
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Caribbean Logistics & Infrastructure',
        maxZoom: 18
      }).addTo(desktopLeafletMap);

      desktopSatLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri',
        maxZoom: 19
      });

      // Markers
      clientSites.forEach(s => {
        let color = '#003E78';
        if (s.tipo === 'planta') color = '#FDCA02';
        else if (s.tipo === 'competencia') color = '#DC2626';
        else if (s.tipo === 'prospecto') color = '#059669';

        const marker = L.circleMarker([s.lat, s.lng], {
          radius: s.tipo === 'planta' ? 12 : 8,
          fillColor: color,
          color: '#FFFFFF',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.9
        }).addTo(desktopLeafletMap);

        marker.bindPopup(`<strong>${s.nombre}</strong><br>${s.ciudad} • ${s.tipo}`);
      });

      setTimeout(() => {
        if (desktopLeafletMap) desktopLeafletMap.invalidateSize();
      }, 200);
    }

    function toggleDesktopMapSatellite() {
      if (!desktopLeafletMap || !desktopSatLayer) return;
      if (typeof playChime === 'function') playChime('click');
      if (desktopSatelliteActive) {
        desktopLeafletMap.removeLayer(desktopSatLayer);
        desktopSatelliteActive = false;
        if (typeof showToast === 'function') showToast("Capa Calles CartoDB activa", "info");
      } else {
        desktopSatLayer.addTo(desktopLeafletMap);
        desktopSatelliteActive = true;
        if (typeof showToast === 'function') showToast("Capa Satelital ESRI activa", "info");
      }
    }
    '''

    # Assemble HTML
    # 1. Header replacement
    h_start = base_html.find("<header class=")
    h_end = base_html.find("</header>") + 9
    part_before_header = base_html[:h_start]

    # Inject Leaflet into <head>
    leaflet_tags = """  <!-- Leaflet CSS & JS for Interactive Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
</head>"""
    part_before_header = part_before_header.replace('</head>', leaflet_tags)

    # 2. Main replacement
    m_start = base_html.find('<main id="main-content"')
    m_end = base_html.find('</main>', m_start) + 7
    part_after_main = base_html[m_end:]

    # Combine
    full_html = part_before_header + new_header_html + "\n\n" + new_main_html + "\n\n" + part_after_main

    # Inject new_js_logic before </body>
    body_close = full_html.rfind("</body>")
    full_html = full_html[:body_close] + f"<script>\n{new_js_logic}\n</script>\n" + full_html[body_close:]

    # Clean branding
    print("Sanitizing branding to 100% pure Ultracem...")
    full_html = sanitize_branding(full_html)

    # Remove all gradients
    print("Enforcing solid colors (0 gradients)...")
    full_html = remove_gradients(full_html)

    # Output paths
    index_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\index.html"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Written index.html successfully: {len(full_html)} chars")

    artifact_path = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
    with open(artifact_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Written brain artifact successfully: {artifact_path}")

if __name__ == "__main__":
    main()
