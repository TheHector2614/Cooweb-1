# -*- coding: utf-8 -*-
"""
Ultracem UltraRacha v6.0 Compiler
Fulfills all user requirements:
1. 100% PURE ULTRACEM S.A.S. BRANDING (Zero Semillero / CooWeb).
2. Uses the mobile CRM features & interactions in full Desktop Computer format
   ("Usa tipo el que esta en el celular pero para computador y que tenga las mismas funcionalidades y interacciones").
3. Dropdown selector for view modes:
   - Desktop Application (Complete)
   - Dual Split View (Desktop + Phone beside it)
   - Mobile Only (Field Rep Phone)
   - PRD (Ultracem Specification)
4. Primary Ultracem Palette: Amarillo (#FDCA02), Azul Oscuro (#003E78 / #0A233F), and Blanco (#FFFFFF).
5. 100% SOLID COLORS ONLY (zero gradients).
"""

import os
import re
import sys
from generate_ultracem_desktop_crm import get_ultracem_desktop_crm_html
from generate_prd_html import get_prd_html

def remove_gradients(html_str):
    """Replaces all gradient utility classes with solid colors"""
    replacements = [
        (r'bg-gradient-to-r from-\[#0F172A\] via-\[#132A3E\] to-\[#0F172A\]', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-\[#0F172A\] via-\[#003E78\] to-\[#0F172A\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-\[#0033A0\] to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-900 to-\[#003E78\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-900 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-slate-900 via-slate-800 to-\[#004797\]', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-sky-900 via-\[#004797\] to-blue-950', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-amber-500 via-amber-600 to-orange-600', 'bg-[#D9531E]'),
        (r'bg-gradient-to-r from-\[#002D80\] via-\[#003B99\] to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-blue-600 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-teal-900 via-\[#0F172A\] to-slate-900', 'bg-[#0A233F]'),
        (r'bg-gradient-to-r from-slate-900 to-\[#004797\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-r from-\[#003E78\] to-\[#005AB5\]', 'bg-[#003E78]'),
        (r'bg-gradient-to-b from-amber-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-slate-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-amber-50/40 to-white', 'bg-white'),
        (r'bg-gradient-to-[a-z]+', 'bg-[#003E78]'),
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

    print("Reading base script build_ultraracha_v3.py...")
    with open("scripts/build_ultraracha_v3.py", "r", encoding="utf-8") as f:
        base_code = f.read()

    # Extract phone canvas
    phone_start_marker = '<!-- Phone Canvas Frame:'
    p_start = base_code.find(phone_start_marker)
    if p_start == -1:
        print("ERROR: Could not find phone canvas start marker.")
        sys.exit(1)

    p_end = base_code.find('</aside>', p_start)
    phone_canvas_raw = base_code[p_start:p_end].strip()

    # Remove any activation card from phone canvas
    phone_canvas_raw = re.sub(
        r'<div id="activation-stage-card".*?</div>\s*</div>',
        '',
        phone_canvas_raw,
        flags=re.DOTALL
    )

    print(f"Extracted phone canvas HTML: {len(phone_canvas_raw)} characters")

    # Get Desktop CRM HTML
    desktop_crm_html = get_ultracem_desktop_crm_html()
    print(f"Generated Desktop CRM HTML: {len(desktop_crm_html)} characters")

    # Get PRD HTML
    prd_html = get_prd_html()
    print(f"Generated PRD HTML: {len(prd_html)} characters")

    # Build Header: Solid Navy with Amarillo border and clean View Mode Dropdown
    new_header_html = f'''  <!-- ============================================================== -->
  <!-- TOP APP HEADER: SOLID AZUL OSCURO (#003E78) & AMARILLO (#FDCA02) -->
  <!-- ============================================================== -->
  <header class="bg-[#003E78] text-white border-b-4 border-[#FDCA02] shadow-md sticky top-0 z-50">
    <div class="max-w-[1780px] mx-auto px-4 sm:px-6 py-2.5 flex items-center justify-between gap-4">
      
      <!-- Brand Logo Ultracem -->
      <div class="flex items-center space-x-3 select-none">
        <div class="bg-white px-2.5 py-1 rounded-xl shadow-xs border border-white/40">
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
            <option value="desktop" selected>💻 Aplicación de Escritorio (Completa)</option>
            <option value="dual">💻📱 Vista Dividida (Escritorio + Celular al lado)</option>
            <option value="mobile">📱 Versión Celular (Móvil en Terreno)</option>
            <option value="prd">📑 Especificación PRD Ultracem</option>
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

    # Build Main Container
    new_main_html = f'''  <!-- ============================================================== -->
  <!-- MAIN WORKSPACE CONTAINER (FONDO SÓLIDO #F2F1EC)                -->
  <!-- ============================================================== -->
  <main id="main-content" class="flex-1 w-full mx-auto px-3 sm:px-5 lg:px-6 py-5 transition-all bg-[#F2F1EC]">

    <!-- ============================================================== -->
    <!-- 1. VISTA WORKSTATION: COMPUTADOR (IZQUIERDA) + CELULAR (DERECHA)-->
    <!-- Permite operar el CRM de escritorio y ver el celular al lado   -->
    <!-- ============================================================== -->
    <div id="view-workstation" class="w-full max-w-[1780px] mx-auto flex flex-col xl:flex-row gap-6 items-start justify-center">

      <!-- PANEL PRINCIPAL COMPUTADOR: CRM DE ESCRITORIO ULTRACEM -->
      <div id="desktop-app-wrapper" class="flex-1 w-full min-w-0">
{desktop_crm_html}
      </div>

      <!-- PANEL CELULAR: APLICACIÓN MÓVIL EN VIVO (STICKY DERECHA) -->
      <aside id="phone-container-wrapper" class="hidden xl:flex w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex-col items-center">
        <div class="mb-2 text-center">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white border-2 border-[#FDCA02] shadow-xs">
            📱 Asesor Móvil en Terreno
          </span>
        </div>
{phone_canvas_raw}
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA PRD MAESTRO COMPLETO (CANVAS BLANCO)                  -->
    <!-- ============================================================== -->
    <div id="view-prd" class="hidden w-full max-w-5xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border-2 border-slate-300 shadow-sm space-y-10 text-slate-800">
{prd_html}
    </div>

  </main>'''

    # JavaScript Functions to manage Desktop CRM tabs and View Mode dropdown
    new_js_logic = '''
    // ==============================================================
    // ULTRACEM VIEW MODE CONTROLLER (DROPDOWN SELECTOR)
    // ==============================================================
    function changeViewMode(mode) {
      playChime('click');
      const ws = document.getElementById('view-workstation');
      const dWrapper = document.getElementById('desktop-app-wrapper');
      const pWrapper = document.getElementById('phone-container-wrapper');
      const vPrd = document.getElementById('view-prd');
      const selector = document.getElementById('view-mode-selector');

      if (selector && selector.value !== mode) {
        selector.value = mode;
      }

      if (mode === 'desktop') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) pWrapper.classList.add('hidden');
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻 Modo Escritorio Completo", "info");
      } else if (mode === 'dual') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻📱 Vista Dividida: Computador + Celular al lado", "info");
      } else if (mode === 'mobile') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.add('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full max-w-[420px] mx-auto flex flex-col items-center py-2";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("📱 Modo Celular Asesor de Terreno", "info");
      } else if (mode === 'prd') {
        if (ws) ws.classList.add('hidden');
        if (vPrd) vPrd.classList.remove('hidden');
        showToast("📑 Especificación PRD Ultracem", "info");
        setTimeout(() => {
          if (vPrd) vPrd.scrollIntoView({ behavior: 'smooth' });
        }, 50);
      }
    }

    // ==============================================================
    // DESKTOP CRM TAB SWITCHER
    // ==============================================================
    function switchDesktopCrmTab(tabName) {
      playChime('click');
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
        setTimeout(initDesktopColombiaMap, 100);
      }
    }

    // Desktop Client Selection
    let currentSelectedClientId = 1;
    function seleccionarClienteDesktop(id) {
      playChime('click');
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
      showToast(`Cliente seleccionado: ${c.name}`, "info");
    }

    // Desktop Filter
    function filtrarClientesDesktop(filter) {
      playChime('click');
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
        playChime('click');
        if (btnText) btnText.textContent = "Detener y Transcribir Audio...";
        if (badge) {
          badge.textContent = "Grabando 00:06...";
          badge.className = "text-[10px] bg-rose-600 text-white px-2 py-0.5 rounded-full font-mono-data animate-pulse";
        }
      } else {
        isDesktopAudioRecording = false;
        playChime('success');
        if (btnText) btnText.textContent = "Grabar Nota de Audio";
        if (badge) {
          badge.textContent = "Audio Guardado & Transcrito";
          badge.className = "text-[10px] bg-emerald-600 text-white px-2 py-0.5 rounded-full font-mono-data";
        }
        if (player) {
          const wavBlob = generateSyntheticAudioMemoWav(6);
          player.src = URL.createObjectURL(wavBlob);
          player.load();
        }
        showToast("🎙️ Nota de voz procesada con Whisper Turbo", "success");
      }
    }

    // Desktop Escalation SLA
    function escalarCasoDesktop() {
      playChime('success');
      const select = document.getElementById('descalation-dept-select');
      const deptName = select ? select.options[select.selectedIndex].text : "Cartera";
      showToast(`⚡ Caso escalado a ${deptName}. ¡Racha diaria protegida (+150 XP)!`, "success");
    }

    // Desktop WhatsApp
    function contactarClienteWhatsApp(clienteName) {
      playChime('click');
      showToast(`📲 Abriendo WhatsApp para ${clienteName} (+50 XP)`, "success");
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

      playChime('click');
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
        playChime('success');
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
      playChime('click');
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

    // Leaflet Desktop Map Initializer
    let desktopLeafletMap = null;
    let desktopSatelliteActive = false;
    let desktopSatLayer = null;

    function initDesktopColombiaMap() {
      const container = document.getElementById('desktop-colombia-map');
      if (!container || desktopLeafletMap) {
        if (desktopLeafletMap) desktopLeafletMap.invalidateSize();
        return;
      }

      desktopLeafletMap = L.map('desktop-colombia-map', {
        center: [10.9639, -74.7964],
        zoom: 11
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(desktopLeafletMap);

      desktopSatLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri'
      });

      // Markers
      if (typeof clientSites !== 'undefined') {
        clientSites.forEach(s => {
          let color = '#003E78';
          if (s.tipo === 'planta') color = '#FDCA02';
          else if (s.tipo === 'competencia') color = '#DC2626';

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
      }
    }

    function toggleDesktopMapSatellite() {
      if (!desktopLeafletMap || !desktopSatLayer) return;
      playChime('click');
      if (desktopSatelliteActive) {
        desktopLeafletMap.removeLayer(desktopSatLayer);
        desktopSatelliteActive = false;
        showToast("Capa Calles activa", "info");
      } else {
        desktopSatLayer.addTo(desktopLeafletMap);
        desktopSatelliteActive = true;
        showToast("Capa Satelital ESRI activa", "info");
      }
    }
    '''

    # Assemble everything into base_code:
    # 1. Replace header
    h_start = base_code.find('<header class=')
    h_end = base_code.find('</header>') + 9
    part_before = base_code[:h_start] + new_header_html

    # 2. Replace main
    m_start = base_code.find('<main id="main-content"')
    m_end = base_code.find('</main>', m_start) + 7
    part_middle = new_main_html

    # 3. Update JavaScript logic
    part_after = base_code[m_end:]
    # Replace switchMainView / switchView logic
    sv_start = part_after.find('function switchMainView(mode) {')
    if sv_start == -1:
        sv_start = part_after.find('function switchView(viewName) {')
    sv_end = part_after.find('function setTimeMode', sv_start)

    part_after = part_after[:sv_start] + new_js_logic + part_after[sv_end:]

    # Combine
    full_code = part_before + part_middle + part_after

    # 4. Sanitize branding: Eliminate ALL Semillero / CooWeb mentions
    print("Sanitizing branding to 100% Ultracem...")
    full_code = sanitize_branding(full_code)

    # 5. Remove all gradients to enforce 100% solid colors
    print("Enforcing solid colors (zero gradients)...")
    full_code = remove_gradients(full_code)

    # Write to scripts/build_ultraracha_v3.py
    with open("scripts/build_ultraracha_v3.py", "w", encoding="utf-8") as f:
        f.write(full_code)
    print("Updated scripts/build_ultraracha_v3.py successfully!")

    # Execute generator
    print("Generating index.html and prototype...")
    import subprocess
    res = subprocess.run([sys.executable, "scripts/build_ultraracha_v3.py"], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)

if __name__ == "__main__":
    main()
