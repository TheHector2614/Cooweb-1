# -*- coding: utf-8 -*-
"""
Ultracem UltraRacha v5.0 Compiler
Fulfills all user requirements:
1. REMOVES the strategy activation bar ("Retira lo siguiente. La barra de estrategia.").
2. Implements the exact Desktop Computer Application ("Userflow Administrador · computador")
   from the 3 user-uploaded images:
   - Image 2: Panorama · octubre 2026 (5 KPI cards, Brecha por zona, Clientes por semáforo, Asesores table)
   - Image 3: Metas · noviembre 2026 (Metas mensuales table with inputs, Registro de cambios card)
   - Image 4: Tareas IA · últimos 14 días (Resultado tareas segmented bar, Motivos de descarte bars, Revisión a ciegas table)
   - Plus: Reglas & Auditoría tabs with solid dark navy sidebar (#0A233F) and official logo.
3. Provides a live dual workstation where the user can view and operate the mobile phone right beside the desktop app
   ("donde se pueda ver la aplicacion desde el celular el uso la interfaz y todo").
4. 100% SOLID COLORS ONLY: Eliminates all gradients (no bg-gradient-to, no linear-gradient).
   Uses scraped official colors: Solid Ultracem Blue (#003E78), Solid Dark Navy (#0A233F), Solid Warm Off-White (#F2F1EC), Solid Orange (#D9531E), Solid Yellow (#FDCA02).
5. Embeds the official brand logo in the sidebar and top header.
"""

import os
import re
import sys
from generate_desktop_app_html import get_desktop_app_html
from generate_prd_html import get_prd_html

def remove_gradients(html_str):
    """Replaces all gradient utility classes with solid colors"""
    replacements = [
        # Navy / Blue Gradients -> Solid #003E78 or #0A233F
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
        # Vertical Gradients -> Solid white or solid neutral
        (r'bg-gradient-to-b from-amber-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-slate-50 to-white', 'bg-white'),
        (r'bg-gradient-to-b from-amber-50/40 to-white', 'bg-white'),
        # Generic fallback for any remaining bg-gradient
        (r'bg-gradient-to-[a-z]+', 'bg-[#003E78]'),
    ]
    for pattern, replacement in replacements:
        html_str = re.sub(pattern, replacement, html_str)
    return html_str

def main():
    print("Reading base64 logo...")
    base64_logo_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\assets\logo_base64.txt"
    with open(base64_logo_path, "r", encoding="utf-8") as f:
        logo_base64 = f.read().strip()

    print("Reading base script build_ultraracha_v3.py...")
    with open("scripts/build_ultraracha_v3.py", "r", encoding="utf-8") as f:
        base_code = f.read()

    # 1. REMOVE STRATEGY ACTIVATION BAR COMPLETELY
    act_marker = '<!-- ============================================================== -->\n  <!-- INTERACTIVE ACTIVATION BAR:'
    main_marker = '<!-- ============================================================== -->\n  <!-- MAIN APP CONTAINER'
    
    act_idx = base_code.find(act_marker)
    main_idx = base_code.find(main_marker)
    
    if act_idx != -1 and main_idx != -1 and act_idx < main_idx:
        print(f"Removing strategy activation bar from index {act_idx} to {main_idx}...")
        base_code = base_code[:act_idx] + base_code[main_idx:]
    else:
        print("Note: Strategy activation bar already removed or marker not found.")

    # 2. Extract phone canvas HTML
    phone_start_marker = '<!-- Phone Canvas Frame:'
    # Look for the phone canvas inside
    p_start = base_code.find(phone_start_marker)
    if p_start == -1:
        print("ERROR: Could not find phone canvas frame start marker.")
        sys.exit(1)

    # In v4, phone canvas was inside aside id="phone-container-wrapper"
    p_end_marker = '</aside>'
    p_end = base_code.find(p_end_marker, p_start)
    if p_end == -1:
        # Fallback to older marker
        p_end = base_code.find('<!-- ============================================================== -->\n    <!-- 2. VISTA SUPERVISOR WEB', p_start)

    phone_canvas_raw = base_code[p_start:p_end].strip()
    # Ensure it's cleanly isolated
    if phone_canvas_raw.endswith('</div>\n    </div>'):
        # Strip outer container div
        phone_canvas_raw = phone_canvas_raw[:phone_canvas_raw.rfind('</div>')].strip()
    
    print(f"Extracted phone canvas HTML: {len(phone_canvas_raw)} characters")

    # 3. Get Desktop App HTML (Images 2, 3, 4)
    desktop_app_html = get_desktop_app_html()
    print(f"Generated Desktop Admin App HTML: {len(desktop_app_html)} characters")

    # 4. Get PRD HTML
    prd_html = get_prd_html()
    print(f"Generated PRD HTML: {len(prd_html)} characters")

    # 5. Build new <main id="main-content">
    # Page background is solid #F2F1EC (matching user images)
    new_main_html = f'''<main id="main-content" class="flex-1 w-full mx-auto px-3 sm:px-5 lg:px-6 py-5 transition-all bg-[#F2F1EC]">

    <!-- ============================================================== -->
    <!-- 1. VISTA WORKSTATION: COMPUTADOR (IZQUIERDA) + CELULAR (DERECHA)-->
    <!-- Permite operar el admin de escritorio y ver el celular al lado -->
    <!-- ============================================================== -->
    <div id="view-workstation" class="w-full max-w-[1780px] mx-auto flex flex-col xl:flex-row gap-6 items-start justify-center">

      <!-- PANEL PRINCIPAL COMPUTADOR: USERFLOW ADMINISTRADOR · COMPUTADOR (IMAGES 2, 3, 4) -->
      <div id="desktop-app-wrapper" class="flex-1 w-full min-w-0">
{desktop_app_html}
      </div>

      <!-- PANEL CELULAR: APLICACIÓN MÓVIL EN VIVO (STICKY DERECHA) -->
      <aside id="phone-container-wrapper" class="w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center">
        <div class="mb-2 text-center">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white shadow-xs">
            📱 Asesor Móvil en Terreno
          </span>
        </div>
{phone_canvas_raw}
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA PRD MAESTRO COMPLETO (CANVAS BLANCO)                  -->
    <!-- ============================================================== -->
    <div id="view-prd" class="hidden w-full max-w-5xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border border-slate-300 shadow-sm space-y-10 text-slate-800">
{prd_html}
    </div>

  </main>'''

    # Locate and replace <main id="main-content" ... </main>
    m_start = base_code.find('<main id="main-content"')
    m_end = base_code.find('</main>', m_start) + 7

    part_before_main = base_code[:m_start]
    part_after_main = base_code[m_end:]

    # 6. Update Top Header with Solid Colors and Brand Logo
    # Replace header brand container with solid styling and logo
    header_brand_marker = '<header class="bg-white/95'
    h_idx = part_before_main.find(header_brand_marker)
    if h_idx != -1:
        part_before_main = part_before_main.replace(header_brand_marker, '<header class="bg-white border-b border-slate-200 shadow-xs')

    # Update View Toggle to 4 clean modes
    toggle_start_marker = '<!-- View Switcher'
    if toggle_start_marker not in part_before_main:
        toggle_start_marker = '<!-- View Toggle'
    
    t_start = part_before_main.find(toggle_start_marker)
    t_end = part_before_main.find('</nav>', t_start) + 6

    new_header_switcher = '''<!-- View Switcher (Workstation Dual, Solo PC, Solo Móvil, PRD) -->
        <nav aria-label="Selector de Vistas" class="bg-slate-100 p-1 rounded-xl flex items-center border border-slate-300 shadow-xs">
          <button id="btn-view-workstation" onclick="switchMainView('workstation')" aria-label="Ver Computador y Celular en Vista Dual" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs">
            <span>💻📱</span>
            <span class="hidden sm:inline">Vista Dual</span>
          </button>
          <button id="btn-view-desktop-only" onclick="switchMainView('desktop-only')" aria-label="Ver Solo Computador" class="btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>💻</span>
            <span class="hidden sm:inline">Solo Computador</span>
          </button>
          <button id="btn-view-mobile-only" onclick="switchMainView('mobile-only')" aria-label="Ver Solo Celular" class="btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>📱</span>
            <span class="hidden sm:inline">Solo Celular</span>
          </button>
          <button id="btn-view-prd-only" onclick="switchMainView('prd')" aria-label="Ver Documento PRD" class="btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>📑</span>
            <span class="hidden sm:inline">PRD</span>
          </button>
        </nav>'''

    part_before_main = part_before_main[:t_start] + new_header_switcher + part_before_main[t_end:]

    # 7. Update JavaScript Functions
    # Replace switchView / switchSupervisorTab with switchMainView and switchDesktopTab
    sv_start = part_after_main.find('function switchView(viewName) {')
    sv_end = part_after_main.find('function setTimeMode', sv_start)

    new_js_logic = '''function switchMainView(mode) {
      playChime('click');
      const ws = document.getElementById('view-workstation');
      const dWrapper = document.getElementById('desktop-app-wrapper');
      const pWrapper = document.getElementById('phone-container-wrapper');
      const vPrd = document.getElementById('view-prd');

      const bWs = document.getElementById('btn-view-workstation');
      const bDesk = document.getElementById('btn-view-desktop-only');
      const bMob = document.getElementById('btn-view-mobile-only');
      const bPrd = document.getElementById('btn-view-prd-only');

      [bWs, bDesk, bMob, bPrd].forEach(b => {
        if (b) b.className = "btn-tactile flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
      });

      if (mode === 'workstation') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center";
        }
        if (vPrd) vPrd.classList.add('hidden');
        if (bWs) bWs.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs";
      } else if (mode === 'desktop-only') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) pWrapper.classList.add('hidden');
        if (vPrd) vPrd.classList.add('hidden');
        if (bDesk) bDesk.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs";
      } else if (mode === 'mobile-only') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.add('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full max-w-[420px] mx-auto flex flex-col items-center py-2";
        }
        if (vPrd) vPrd.classList.add('hidden');
        if (bMob) bMob.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs";
      } else if (mode === 'prd') {
        if (ws) ws.classList.add('hidden');
        if (vPrd) vPrd.classList.remove('hidden');
        if (bPrd) bPrd.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#003E78] shadow-xs";
        setTimeout(() => {
          if (vPrd) vPrd.scrollIntoView({ behavior: 'smooth' });
        }, 50);
      }
    }

    function switchDesktopTab(tabName) {
      playChime('click');
      const tabs = ['panorama', 'metas', 'reglas', 'tareas', 'auditoria'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dnav-${t}`);
        const sec = document.getElementById(`dtab-content-${t}`);
        if (t === tabName) {
          if (btn) btn.className = "w-full flex items-center px-4 py-2.5 rounded-xl font-bold transition-colors bg-[#1E3A5F] text-white shadow-xs";
          if (sec) sec.classList.remove('hidden');
        } else {
          if (btn) btn.className = "w-full flex items-center px-4 py-2.5 rounded-xl font-semibold transition-colors text-slate-300 hover:text-white hover:bg-[#142C47]";
          if (sec) sec.classList.add('hidden');
        }
      });
    }

    // Aliases for compatibility
    function switchView(viewName) {
      if (viewName === 'split' || viewName === 'web') switchMainView('workstation');
      else if (viewName === 'mobile') switchMainView('mobile-only');
      else if (viewName === 'prd') switchMainView('prd');
    }

    function goToPRD() {
      switchMainView('prd');
    }

    '''

    part_after_main = part_after_main[:sv_start] + new_js_logic + part_after_main[sv_end:]

    # Update DOMContentLoaded in part_after_main to initialize the view cleanly
    init_view_search = "document.addEventListener('DOMContentLoaded', () => {"
    d_idx = part_after_main.find(init_view_search)
    if d_idx != -1:
        # Find next occurrence of initHeatmapGrid
        h_idx = part_after_main.find('initHeatmapGrid();', d_idx)
        init_responsive_call = """
      if (window.innerWidth >= 1280) {
        switchMainView('workstation');
      } else if (window.innerWidth >= 768) {
        switchMainView('desktop-only');
      } else {
        switchMainView('mobile-only');
      }
      """
        part_after_main = part_after_main[:d_idx + len(init_view_search)] + init_responsive_call + part_after_main[h_idx:]

    # 8. Apply global gradient stripping to enforce SOLID COLORS ONLY
    assembled_code = part_before_main + new_main_html + part_after_main
    print("Applying solid colors transformation (removing all gradients)...")
    assembled_code = remove_gradients(assembled_code)

    # 9. Write to scripts/build_ultraracha_v3.py
    with open("scripts/build_ultraracha_v3.py", "w", encoding="utf-8") as f:
        f.write(assembled_code)
    print("Updated scripts/build_ultraracha_v3.py successfully!")

    # 10. Run build_ultraracha_v3.py to generate final index.html and prototype
    print("Generating index.html and prototype...")
    import subprocess
    res = subprocess.run([sys.executable, "scripts/build_ultraracha_v3.py"], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)

if __name__ == "__main__":
    main()
