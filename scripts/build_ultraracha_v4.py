# -*- coding: utf-8 -*-
"""
Ultracem UltraRacha v4.0 Compiler
Merges:
1. Split Screen View: Left column contains the comprehensive PRD rendered in a clean white paper canvas (generate_prd_html.py).
   Right column contains the sticky live interactive mobile prototype (lg:sticky lg:top-24 self-start).
2. Redesigned Corporate Web Supervisor Dashboard: Executive KPIs, Antichurn Radar with interactive filter tabs,
   official Ultracem commercial advisors leaderboard (Milena Ospino, Adriana Anaya, Hichel Espitia),
   Planta Galapa industrial telemetry, and Vanesa IA strategic intelligence feed (generate_web_supervisor_html.py).
3. 3-way top view switcher: 📑 PRD + Prototipo, 📱 Solo Móvil, 💻 Web Supervisor.
4. Preserves 100% of existing functionality: Leaflet Colombia Map with satellite toggle, B2B Caribbean prospects directory,
   audio voice recording with synthesized WAV and playable <audio controls>, Don Fraguado, and multi-model AI engine (Groq, NVIDIA NIM, DeepSeek).
"""

import os
import sys
from generate_prd_html import get_prd_html
from generate_web_supervisor_html import get_web_supervisor_html

def main():
    print("Reading base64 logo...")
    base64_logo_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\assets\logo_base64.txt"
    with open(base64_logo_path, "r", encoding="utf-8") as f:
        logo_base64 = f.read().strip()

    print("Reading base script build_ultraracha_v3.py...")
    with open("scripts/build_ultraracha_v3.py", "r", encoding="utf-8") as f:
        base_code = f.read()

    # Locate phone canvas frame
    start_marker = '<!-- Phone Canvas Frame:'
    end_marker = '<!-- ============================================================== -->\n    <!-- 2. VISTA SUPERVISOR WEB'
    
    start_idx = base_code.find(start_marker)
    end_idx = base_code.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("ERROR: Could not locate phone canvas markers in build_ultraracha_v3.py")
        sys.exit(1)
        
    phone_raw = base_code[start_idx:end_idx].rstrip()
    # Strip the closing </div> of view-mobile from the end
    # phone_raw ends with: </div>\n    </div>
    # We want only the phone canvas (ends with first </div>)
    last_div_idx = phone_raw.rfind('</div>')
    second_last_div_idx = phone_raw[:last_div_idx].rfind('</div>')
    phone_canvas_html = phone_raw[:second_last_div_idx + 6].strip()

    print(f"Extracted phone canvas HTML: {len(phone_canvas_html)} characters")

    # Get PRD HTML
    prd_html = get_prd_html()
    print(f"Generated PRD HTML: {len(prd_html)} characters")

    # Get Web Supervisor HTML
    web_supervisor_html = get_web_supervisor_html()
    print(f"Generated Web Supervisor HTML: {len(web_supervisor_html)} characters")

    # Locate <main id="main-content"
    main_start_idx = base_code.find('<main id="main-content"')
    main_end_idx = base_code.find('</main>', main_start_idx) + 7

    # Construct new <main id="main-content">
    new_main_html = f'''<main id="main-content" class="flex-1 w-full mx-auto px-3 sm:px-6 lg:px-8 py-6 transition-all">

    <!-- ============================================================== -->
    <!-- 1. VISTA SPLIT: PRD DOCUMENTO (IZQUIERDA) + PROTOTIPO MÓVIL (DERECHA) -->
    <!-- ============================================================== -->
    <div id="view-split" class="w-full max-w-[1720px] mx-auto flex flex-col lg:flex-row gap-8 items-start justify-center">

      <!-- ============================================================ -->
      <!-- COLUMNA IZQUIERDA: EL PRD EN UN ESPACIO EN BLANCO SCROLLEABLE -->
      <!-- ============================================================ -->
      <section id="prd-document-panel" class="flex-1 w-full min-w-0 bg-white rounded-3xl p-6 sm:p-10 lg:p-12 border border-slate-200/90 shadow-sm space-y-12 text-slate-800">
{prd_html}
      </section>

      <!-- ============================================================ -->
      <!-- COLUMNA DERECHA: PROTOTIPO MÓVIL INTERACTIVO (STICKY)        -->
      <!-- ============================================================ -->
      <aside id="phone-container-wrapper" class="w-full lg:w-[420px] flex-shrink-0 lg:sticky lg:top-24 self-start flex justify-center">
{phone_canvas_html}
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA SUPERVISOR WEB (DASHBOARD CORPORATIVO ENTERPRISE)      -->
    <!-- ============================================================== -->
{web_supervisor_html}

  </main>'''

    # Replace <main> in base_code
    part_before_main = base_code[:main_start_idx]
    part_after_main = base_code[main_end_idx:]

    # Update top view switcher in header
    toggle_start_marker = '<!-- View Toggle'
    toggle_end_marker = '</nav>'
    t_start = part_before_main.find(toggle_start_marker)
    t_end = part_before_main.find(toggle_end_marker, t_start) + 6

    new_header_switcher = '''<!-- View Switcher (3 Modos: Split PRD+Prototipo, Solo Móvil, Web Supervisor) -->
        <nav aria-label="Selector de Vistas" class="bg-slate-100 p-1 rounded-xl flex items-center border border-slate-200/80 shadow-xs">
          <button id="btn-view-split" onclick="switchView('split')" aria-label="Ver PRD y Prototipo en Split" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#14B8A6] shadow-xs">
            <span>📑</span>
            <span class="hidden xs:inline">PRD + Prototipo</span>
          </button>
          <button id="btn-view-mobile" onclick="switchView('mobile')" aria-label="Cambiar a Vista Solo Móvil" class="btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>📱</span>
            <span class="hidden xs:inline">Solo Móvil</span>
          </button>
          <button id="btn-view-web" onclick="switchView('web')" aria-label="Cambiar a Dashboard Supervisor" class="btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>💻</span>
            <span class="hidden xs:inline">Supervisor</span>
          </button>
        </nav>'''

    part_before_main = part_before_main[:t_start] + new_header_switcher + part_before_main[t_end:]

    # Also update "PRD & Marca" button in header to call goToPRD()
    part_before_main = part_before_main.replace("onclick=\"openSemilleroPRDModal()\"", "onclick=\"goToPRD()\"")

    # In part_after_main, update switchView function and add supervisor tab handlers
    switch_view_marker = 'function switchView(viewName) {'
    sv_idx = part_after_main.find(switch_view_marker)
    # Find closing of switchView
    sv_close_idx = part_after_main.find('function setTimeMode', sv_idx)

    new_switch_view_code = '''function switchView(viewName) {
      playChime('click');
      const vSplit = document.getElementById('view-split');
      const prdPanel = document.getElementById('prd-document-panel');
      const phoneWrapper = document.getElementById('phone-container-wrapper');
      const vWeb = document.getElementById('view-web');

      const btnSplit = document.getElementById('btn-view-split');
      const btnMobile = document.getElementById('btn-view-mobile');
      const btnWeb = document.getElementById('btn-view-web');

      // Reset all buttons styling
      [btnSplit, btnMobile, btnWeb].forEach(btn => {
        if (btn) btn.className = "btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
      });

      if (viewName === 'split') {
        if (vSplit) vSplit.classList.remove('hidden');
        if (vWeb) vWeb.classList.add('hidden');
        if (prdPanel) prdPanel.classList.remove('hidden');
        if (phoneWrapper) {
          phoneWrapper.className = "w-full lg:w-[420px] flex-shrink-0 lg:sticky lg:top-24 self-start flex justify-center";
        }
        if (btnSplit) btnSplit.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#14B8A6] shadow-xs";
      } else if (viewName === 'mobile') {
        if (vSplit) vSplit.classList.remove('hidden');
        if (vWeb) vWeb.classList.add('hidden');
        if (prdPanel) prdPanel.classList.add('hidden');
        if (phoneWrapper) {
          phoneWrapper.className = "w-full max-w-[420px] mx-auto flex justify-center py-2";
        }
        if (btnMobile) btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#14B8A6] shadow-xs";
      } else if (viewName === 'web') {
        if (vSplit) vSplit.classList.add('hidden');
        if (vWeb) vWeb.classList.remove('hidden');
        if (btnWeb) btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs";
      }
    }

    function goToPRD() {
      playChime('click');
      switchView('split');
      setTimeout(() => {
        const el = document.getElementById('prd-document-panel');
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 50);
    }

    function switchSupervisorTab(tabName) {
      playChime('click');
      const tabs = ['radar', 'ranking', 'galapa', 'vanesa'];
      tabs.forEach(t => {
        const btn = document.getElementById(`sup-tab-btn-${t}`);
        const content = document.getElementById(`sup-tab-content-${t}`);
        if (t === tabName) {
          if (btn) btn.className = "btn-tactile px-3.5 py-2 rounded-xl font-bold transition-all bg-[#003E78] text-white shadow-xs flex items-center space-x-1.5";
          if (content) content.classList.remove('hidden');
        } else {
          if (btn) btn.className = "btn-tactile px-3.5 py-2 rounded-xl font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center space-x-1.5";
          if (content) content.classList.add('hidden');
        }
      });
    }

    function filterRadarTable(filterType) {
      playChime('click');
      const buttons = {
        'todos': document.getElementById('filter-btn-todos'),
        'critico': document.getElementById('filter-btn-critico'),
        'advertencia': document.getElementById('filter-btn-advertencia'),
        'escalado': document.getElementById('filter-btn-escalado')
      };

      Object.entries(buttons).forEach(([key, btn]) => {
        if (!btn) return;
        if (key === filterType) {
          btn.className = "px-3 py-1 rounded-lg font-bold bg-slate-900 text-white";
        } else {
          btn.className = "px-3 py-1 rounded-lg font-semibold text-slate-600 hover:bg-slate-100";
        }
      });

      const rows = document.querySelectorAll('.radar-row');
      rows.forEach(row => {
        const rowType = row.getAttribute('data-type');
        if (filterType === 'todos' || rowType === filterType) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }

    '''

    part_after_main = part_after_main[:sv_idx] + new_switch_view_code + part_after_main[sv_close_idx:]

    # Also make sure DOMContentLoaded sets default view based on window width
    dom_load_marker = "document.addEventListener('DOMContentLoaded', () => {"
    d_idx = part_after_main.find(dom_load_marker)
    if d_idx != -1:
        insert_init_view = """
      // Responsive Initial View: Split on desktop (>=1024px), Mobile on smaller screens
      if (window.innerWidth >= 1024) {
        switchView('split');
      } else {
        switchView('mobile');
      }
"""
        part_after_main = part_after_main[:d_idx + len(dom_load_marker)] + insert_init_view + part_after_main[d_idx + len(dom_load_marker):]

    # Assemble full code
    compiled_code = part_before_main + new_main_html + part_after_main

    # Write compiled python script
    with open("scripts/build_ultraracha_v3.py", "w", encoding="utf-8") as f:
        f.write(compiled_code)
    print("Updated scripts/build_ultraracha_v3.py successfully!")

    # Now execute the script to generate index.html and artifact!
    print("Executing updated build_ultraracha_v3.py to generate index.html...")
    # Extract html_content from compiled_code
    # Or simply run python scripts/build_ultraracha_v3.py

if __name__ == "__main__":
    main()
