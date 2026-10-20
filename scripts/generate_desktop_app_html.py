# -*- coding: utf-8 -*-
"""
Generates the exact Desktop Computer Application ("Userflow Administrador · computador")
as requested by the user and shown in the 3 uploaded screenshots:
- Image 2: Panorama · octubre 2026 (5 KPI cards, Brecha por zona, Clientes por semáforo, Asesores table)
- Image 3: Metas · noviembre 2026 (Metas mensuales table with inputs, Registro de cambios card)
- Image 4: Tareas IA · últimos 14 días (Resultado tareas segmented bar, Motivos de descarte bars, Revisión a ciegas table)
- Plus: Reglas & Auditoría tabs

STRICT RULES APPLIED:
1. SOLID COLORS ONLY: Zero gradients (no bg-gradient, no linear-gradient).
2. Scraping colors: Solid Ultracem Blue (#003E78), Solid Dark Navy (#0A233F), Solid Off-White (#F2F1EC), Solid Orange (#D9531E), Solid Yellow (#FDCA02).
3. Official brand logo included in the sidebar top.
"""

def get_desktop_app_html():
    return r'''
    <!-- ============================================================== -->
    <!-- DESKTOP WEB APPLICATION: USERFLOW ADMINISTRADOR · COMPUTADOR    -->
    <!-- Exact replication of Images 2, 3, and 4 with 100% Solid Colors -->
    <!-- ============================================================== -->
    <div id="desktop-admin-app" class="w-full bg-[#F2F1EC] rounded-3xl border border-slate-300 shadow-sm overflow-hidden flex flex-col md:flex-row">
      
      <!-- ============================================================ -->
      <!-- SIDEBAR: SOLID DARK NAVY (#0A233F)                           -->
      <!-- ============================================================ -->
      <aside class="w-full md:w-60 bg-[#0A233F] text-white flex flex-col flex-shrink-0 p-4 border-r border-slate-800 select-none">
        
        <!-- Logo Container -->
        <div class="bg-[#07182C] rounded-2xl p-3 border border-slate-700/60 mb-6 flex items-center justify-center">
          <img src="data:image/png;base64,{logo_base64}" alt="Logo Ultracem" class="h-9 w-auto object-contain" />
        </div>

        <!-- Sidebar Navigation Menu -->
        <nav class="space-y-1.5 flex-1 text-sm font-medium">
          <button id="dnav-panorama" onclick="switchDesktopTab('panorama')" class="w-full flex items-center px-4 py-2.5 rounded-xl font-bold transition-colors bg-[#1E3A5F] text-white shadow-xs">
            <span>Panorama</span>
          </button>

          <button id="dnav-metas" onclick="switchDesktopTab('metas')" class="w-full flex items-center px-4 py-2.5 rounded-xl font-semibold transition-colors text-slate-300 hover:text-white hover:bg-[#142C47]">
            <span>Metas</span>
          </button>

          <button id="dnav-reglas" onclick="switchDesktopTab('reglas')" class="w-full flex items-center px-4 py-2.5 rounded-xl font-semibold transition-colors text-slate-300 hover:text-white hover:bg-[#142C47]">
            <span>Reglas</span>
          </button>

          <button id="dnav-tareas" onclick="switchDesktopTab('tareas')" class="w-full flex items-center px-4 py-2.5 rounded-xl font-semibold transition-colors text-slate-300 hover:text-white hover:bg-[#142C47]">
            <span>Tareas IA</span>
          </button>

          <button id="dnav-auditoria" onclick="switchDesktopTab('auditoria')" class="w-full flex items-center px-4 py-2.5 rounded-xl font-semibold transition-colors text-slate-300 hover:text-white hover:bg-[#142C47]">
            <span>Auditoría</span>
          </button>
        </nav>

        <!-- Sidebar Footer Status -->
        <div class="pt-4 border-t border-slate-700/60 text-xs text-slate-400 space-y-1">
          <div class="flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span class="text-slate-300 font-semibold">Planta Galapa: 100%</span>
          </div>
          <p class="text-[11px] text-slate-400">Datos al 19 oct, 5:40 a. m.</p>
        </div>
      </aside>

      <!-- ============================================================ -->
      <!-- MAIN WORKSPACE CONTENT AREA (SOLID OFF-WHITE #F2F1EC)        -->
      <!-- ============================================================ -->
      <main class="flex-1 p-5 sm:p-7 overflow-y-auto space-y-6">

        <!-- ========================================================== -->
        <!-- SCREEN 2a: PANORAMA (IMAGE 2)                              -->
        <!-- ========================================================== -->
        <section id="dtab-content-panorama" class="space-y-6">
          
          <!-- Header Row -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Panorama · octubre 2026</h2>
              <p class="text-xs text-slate-500 font-medium mt-0.5">Barranquilla, Santa Marta · Datos al 19 oct, 5:40 a. m.</p>
            </div>

            <!-- Top Right Dropdown Filters -->
            <div class="flex items-center space-x-2 text-xs">
              <div class="relative">
                <select class="appearance-none bg-white border border-slate-300 rounded-xl px-3 py-1.5 pr-7 font-semibold text-slate-800 shadow-xs cursor-pointer focus:outline-none focus:ring-1 focus:ring-slate-400">
                  <option>Canal: Todos</option>
                  <option>Canal: Masivo (Ferreterías)</option>
                  <option>Canal: Industrial (Obras)</option>
                </select>
                <span class="absolute right-2.5 top-2 pointer-events-none text-slate-500 text-[10px]">▼</span>
              </div>

              <div class="relative">
                <select class="appearance-none bg-white border border-slate-300 rounded-xl px-3 py-1.5 pr-7 font-semibold text-slate-800 shadow-xs cursor-pointer focus:outline-none focus:ring-1 focus:ring-slate-400">
                  <option>Zonas: 2</option>
                  <option>Barranquilla</option>
                  <option>Santa Marta</option>
                </select>
                <span class="absolute right-2.5 top-2 pointer-events-none text-slate-500 text-[10px]">▼</span>
              </div>
            </div>
          </div>

          <!-- Top Metric Cards Grid (5 Solid White Cards) -->
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3.5">
            <!-- Card 1 -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500 block">Meta de las zonas</span>
              <div class="text-2xl sm:text-3xl font-black text-slate-900 font-mono-data">3.420 t</div>
              <span class="text-xs text-slate-400 block">13 asesores</span>
            </div>

            <!-- Card 2 -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500 block">Avance</span>
              <div class="text-2xl sm:text-3xl font-black text-slate-900 font-mono-data">71 %</div>
              <span class="text-xs text-slate-400 block">2.428 t facturadas</span>
            </div>

            <!-- Card 3 -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500 block">Oportunidad</span>
              <div class="text-2xl sm:text-3xl font-black text-[#D9531E] font-mono-data">612 t</div>
              <span class="text-xs text-slate-400 block">Suma de clientes</span>
            </div>

            <!-- Card 4 -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500 block">Clientes en rojo</span>
              <div class="text-2xl sm:text-3xl font-black text-[#DC2626] font-mono-data">46</div>
              <span class="text-xs text-slate-400 block">+5 vs semana anterior</span>
            </div>

            <!-- Card 5 -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1 col-span-2 sm:col-span-1">
              <span class="text-xs font-semibold text-slate-500 block">Adopción</span>
              <div class="text-2xl sm:text-3xl font-black text-[#0D9488] font-mono-data">78 %</div>
              <span class="text-xs text-slate-400 block">≥ 3 días/semana</span>
            </div>
          </div>

          <!-- Bottom Section: 2 Columns (Brecha por zona + Tabla de Asesores) -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
            
            <!-- Left Card: Brecha frente a meta por zona & Semáforo (5 cols) -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-6">
              
              <!-- Zone Progress Bars -->
              <div class="space-y-4">
                <h3 class="font-bold text-sm text-slate-900">Brecha frente a meta por zona</h3>

                <!-- Barranquilla -->
                <div class="space-y-1.5">
                  <div class="flex justify-between text-xs font-bold text-slate-800">
                    <span>Barranquilla</span>
                    <span class="font-mono-data">74%</span>
                  </div>
                  <div class="w-full bg-[#E2E8F0] rounded-full h-3 overflow-hidden">
                    <div class="bg-[#003E78] h-3 rounded-full" style="width: 74%"></div>
                  </div>
                  <div class="flex justify-between text-[11px] text-slate-500 font-mono-data">
                    <span>1.554 / 2.100 t</span>
                    <span>Oport. 371 t</span>
                  </div>
                </div>

                <!-- Santa Marta -->
                <div class="space-y-1.5 pt-2">
                  <div class="flex justify-between text-xs font-bold text-slate-800">
                    <span>Santa Marta</span>
                    <span class="font-mono-data">66%</span>
                  </div>
                  <div class="w-full bg-[#E2E8F0] rounded-full h-3 overflow-hidden">
                    <div class="bg-[#003E78] h-3 rounded-full" style="width: 66%"></div>
                  </div>
                  <div class="flex justify-between text-[11px] text-slate-500 font-mono-data">
                    <span>874 / 1.320 t</span>
                    <span>Oport. 241 t</span>
                  </div>
                </div>
              </div>

              <!-- Segmented Semaphore Bar -->
              <div class="space-y-2 pt-4 border-t border-slate-100">
                <h3 class="font-bold text-sm text-slate-900">Clientes por semáforo</h3>
                
                <div class="w-full flex h-3.5 rounded-full overflow-hidden">
                  <div class="bg-[#059669] h-full" style="width: 52%" title="Verde: 158 clientes"></div>
                  <div class="bg-[#FDCA02] h-full" style="width: 28%" title="Amarillo: 85 clientes"></div>
                  <div class="bg-[#DC2626] h-full" style="width: 15%" title="Rojo: 46 clientes"></div>
                  <div class="bg-[#94A3B8] h-full" style="width: 5%" title="Nuevo: 14 clientes"></div>
                </div>

                <div class="flex flex-wrap items-center justify-between text-xs text-slate-600 pt-1 font-medium">
                  <span class="flex items-center space-x-1.5"><span class="w-2.5 h-2.5 rounded-full bg-[#059669]"></span><span>Verde 158</span></span>
                  <span class="flex items-center space-x-1.5"><span class="w-2.5 h-2.5 rounded-full bg-[#FDCA02]"></span><span>Amarillo 85</span></span>
                  <span class="flex items-center space-x-1.5"><span class="w-2.5 h-2.5 rounded-full bg-[#DC2626]"></span><span>Rojo 46</span></span>
                  <span class="flex items-center space-x-1.5"><span class="w-2.5 h-2.5 rounded-full bg-[#94A3B8]"></span><span>Nuevo 14</span></span>
                </div>
              </div>

            </div>

            <!-- Right Card: Tabla de Asesores (7 cols) -->
            <div class="lg:col-span-7 bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
              <div class="overflow-x-auto">
                <table class="w-full text-left text-xs">
                  <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                    <tr>
                      <th class="py-3 px-3 sm:px-4">Asesor</th>
                      <th class="py-3 px-2 sm:px-3">Zona</th>
                      <th class="py-3 px-2 sm:px-3">Avance</th>
                      <th class="py-3 px-2 sm:px-3">Oportunidad ↓</th>
                      <th class="py-3 px-2 text-center text-[#DC2626]">Rojos</th>
                      <th class="py-3 px-2 sm:px-3">Tareas Hechas</th>
                      <th class="py-3 px-3 text-right">Uso</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 font-mono-data text-[11px]">
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Yesid Padilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Barranquilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">47 %</td>
                      <td class="py-2.5 px-2 sm:px-3">78,2 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">11</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">48 %</td>
                      <td class="py-2.5 px-3 text-right text-slate-500 font-sans">2 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Rafael Barrios</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Santa Marta</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">52 %</td>
                      <td class="py-2.5 px-2 sm:px-3">71,8 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">8</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">55 %</td>
                      <td class="py-2.5 px-3 text-right text-slate-500 font-sans">3 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Diana Charris</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Santa Marta</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">59 %</td>
                      <td class="py-2.5 px-2 sm:px-3">58,6 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">6</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">61 %</td>
                      <td class="py-2.5 px-3 text-right text-slate-500 font-sans">4 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Jorge Mejia</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Barranquilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">64 %</td>
                      <td class="py-2.5 px-2 sm:px-3">52,1 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">5</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">66 %</td>
                      <td class="py-2.5 px-3 text-right text-slate-500 font-sans">5 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50 bg-amber-50/40">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900 flex items-center space-x-1.5">
                        <span>Milena Ospino</span>
                        <span class="text-amber-600 text-[10px]">🔥</span>
                      </td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Barranquilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">68 %</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-[#D9531E]">96,3 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">7</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">72 %</td>
                      <td class="py-2.5 px-3 text-right text-emerald-700 font-sans font-bold">5 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Kelly Rangel</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Santa Marta</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">77 %</td>
                      <td class="py-2.5 px-2 sm:px-3">41,8 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">3</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">70 %</td>
                      <td class="py-2.5 px-3 text-right text-emerald-700 font-sans font-bold">5 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Luz Marina Vega</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Barranquilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">84 %</td>
                      <td class="py-2.5 px-2 sm:px-3">33,0 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">2</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">81 %</td>
                      <td class="py-2.5 px-3 text-right text-emerald-700 font-sans font-bold">5 d/sem</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-3 sm:px-4 font-sans font-bold text-slate-900">Andrés Polo</td>
                      <td class="py-2.5 px-2 sm:px-3 font-sans text-slate-600">Barranquilla</td>
                      <td class="py-2.5 px-2 sm:px-3 font-bold text-slate-800">91 %</td>
                      <td class="py-2.5 px-2 sm:px-3">28,4 t</td>
                      <td class="py-2.5 px-2 text-center text-[#DC2626] font-bold">1</td>
                      <td class="py-2.5 px-2 sm:px-3 text-slate-700">86 %</td>
                      <td class="py-2.5 px-3 text-right text-emerald-700 font-sans font-bold">5 d/sem</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

          </div>

        </section>

        <!-- ========================================================== -->
        <!-- SCREEN 2b: METAS (IMAGE 3)                                 -->
        <!-- ========================================================== -->
        <section id="dtab-content-metas" class="hidden space-y-6">
          
          <!-- Header Row -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Metas · noviembre 2026</h2>
              <p class="text-xs text-slate-500 font-medium mt-0.5">Toneladas de cemento por asesor. Los cambios se aplican mañana.</p>
            </div>

            <div class="flex items-center space-x-2 text-xs">
              <button onclick="showToast('Archivo CSV de metas procesado correctamente', 'info')" class="bg-white hover:bg-slate-50 text-slate-800 border border-slate-300 font-semibold px-3.5 py-2 rounded-xl transition-all shadow-xs">
                Cargar archivo
              </button>
              <button onclick="showToast('2 cambios de metas guardados correctamente', 'success')" class="bg-[#D9531E] hover:bg-[#c24615] text-white font-bold px-4 py-2 rounded-xl transition-all shadow-xs">
                Guardar 2 cambios
              </button>
            </div>
          </div>

          <!-- Metas Layout: Table + Registro de Cambios -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
            
            <!-- Left Table (8 cols) -->
            <div class="lg:col-span-8 bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
              <div class="overflow-x-auto">
                <table class="w-full text-left text-xs">
                  <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                    <tr>
                      <th class="py-3 px-4">Asesor</th>
                      <th class="py-3 px-3">Canal</th>
                      <th class="py-3 px-3">Real Oct</th>
                      <th class="py-3 px-3">Meta Oct</th>
                      <th class="py-3 px-3">Promedio 3 M</th>
                      <th class="py-3 px-4 text-right">Meta Nov (T)</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-slate-100 font-mono-data text-[11px]">
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Milena Ospino</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">383 t</td>
                      <td class="py-2.5 px-3">446 t</td>
                      <td class="py-2.5 px-3">421 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="460" class="w-20 text-right font-bold text-slate-900 border-2 border-[#D9531E] rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Andrés Polo</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">282 t</td>
                      <td class="py-2.5 px-3">310 t</td>
                      <td class="py-2.5 px-3">298 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="320" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Luz Marina Vega</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">269 t</td>
                      <td class="py-2.5 px-3">320 t</td>
                      <td class="py-2.5 px-3">305 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="320" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Jorge Mejia</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Consumidor</td>
                      <td class="py-2.5 px-3">186 t</td>
                      <td class="py-2.5 px-3">290 t</td>
                      <td class="py-2.5 px-3">262 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="280" class="w-20 text-right font-bold text-slate-900 border-2 border-[#D9531E] rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Kelly Rangel</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">208 t</td>
                      <td class="py-2.5 px-3">270 t</td>
                      <td class="py-2.5 px-3">251 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="270" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Diana Charris</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Preventista</td>
                      <td class="py-2.5 px-3">153 t</td>
                      <td class="py-2.5 px-3">260 t</td>
                      <td class="py-2.5 px-3">240 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="260" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Rafael Barrios</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">146 t</td>
                      <td class="py-2.5 px-3">280 t</td>
                      <td class="py-2.5 px-3">255 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="280" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                      <td class="py-2.5 px-4 font-sans font-bold text-slate-900">Yesid Padilla</td>
                      <td class="py-2.5 px-3 font-sans text-slate-600">Masivo</td>
                      <td class="py-2.5 px-3">146 t</td>
                      <td class="py-2.5 px-3">310 t</td>
                      <td class="py-2.5 px-3">270 t</td>
                      <td class="py-2.5 px-4 text-right">
                        <input type="text" value="310" class="w-20 text-right text-slate-800 border border-slate-300 rounded-lg px-2 py-1 bg-white focus:outline-none" />
                      </td>
                    </tr>
                  </tbody>
                  <tfoot class="bg-slate-50 border-t border-slate-200 text-xs font-bold text-slate-900">
                    <tr>
                      <td colspan="4" class="py-3 px-4 font-sans">Total zona</td>
                      <td colspan="2" class="py-3 px-4 text-right font-mono-data text-slate-900">
                        3.560 t &nbsp; <span class="text-[#059669] font-sans font-bold">+4,1 % vs octubre</span>
                      </td>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </div>

            <!-- Right Card: Registro de Cambios (4 cols) -->
            <div class="lg:col-span-4 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-4">
              <h3 class="font-bold text-sm text-slate-900">Registro de cambios</h3>

              <div class="space-y-3.5 text-xs">
                <!-- Item 1 -->
                <div class="space-y-0.5 border-b border-slate-100 pb-2.5">
                  <div class="font-bold text-slate-800">Meta nov · Milena Ospino</div>
                  <div class="font-mono-data text-slate-600">446 ➔ 460 t <span class="text-[#D9531E] font-sans font-bold">(sin guardar)</span></div>
                  <div class="text-[10px] text-slate-400">Carlos Díaz · ahora</div>
                </div>

                <!-- Item 2 -->
                <div class="space-y-0.5 border-b border-slate-100 pb-2.5">
                  <div class="font-bold text-slate-800">Umbral rojo: días sin comprar</div>
                  <div class="font-mono-data text-slate-600">40 ➔ 45 días</div>
                  <div class="text-[10px] text-slate-400">Carlos Díaz · 14 oct, 4:02 p. m.</div>
                </div>

                <!-- Item 3 -->
                <div class="space-y-0.5 border-b border-slate-100 pb-2.5">
                  <div class="font-bold text-slate-800">Puntos: rojo a verde</div>
                  <div class="font-mono-data text-slate-600">120 ➔ 150 pts</div>
                  <div class="text-[10px] text-slate-400">Ana Ruiz · 10 oct, 9:15 a. m.</div>
                </div>

                <!-- Item 4 -->
                <div class="space-y-0.5">
                  <div class="font-bold text-slate-800">Carga de metas oct</div>
                  <div class="font-mono-data text-slate-600">archivo metas_oct.csv · 13 filas</div>
                  <div class="text-[10px] text-slate-400">Carlos Díaz · 30 sep, 6:20 p. m.</div>
                </div>
              </div>
            </div>

          </div>

        </section>

        <!-- ========================================================== -->
        <!-- SCREEN 2c: TAREAS IA (IMAGE 4)                             -->
        <!-- ========================================================== -->
        <section id="dtab-content-tareas" class="hidden space-y-6">
          
          <!-- Header Row -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Tareas IA · últimos 14 días</h2>
              <p class="text-xs text-slate-500 font-medium mt-0.5">Barranquilla, Santa Marta · 312 tareas sugeridas</p>
            </div>

            <div class="flex items-center text-xs">
              <span class="bg-[#FEF9C3] text-[#854D0E] border border-[#FDE047] font-semibold px-3 py-1.5 rounded-xl shadow-xs flex items-center space-x-1.5">
                <span>🟡</span>
                <span>Hoy: 2 de 13 listas en «Prioridad automática»</span>
              </span>
            </div>
          </div>

          <!-- Top 2 Cards: Resultado de Tareas + Motivos de Descarte -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            
            <!-- Card 1: Resultado de las tareas -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-4">
              <h3 class="font-bold text-sm text-slate-900">Resultado de las tareas</h3>

              <!-- Segmented Bar -->
              <div class="w-full flex h-3.5 rounded-full overflow-hidden">
                <div class="bg-[#003E78] h-full" style="width: 64%" title="64% Hechas"></div>
                <div class="bg-[#D9531E] h-full" style="width: 21%" title="21% Descartadas"></div>
                <div class="bg-[#CBD5E1] h-full" style="width: 15%" title="15% Ignoradas"></div>
              </div>

              <div class="grid grid-cols-3 gap-2 text-center pt-2">
                <div>
                  <div class="text-xl sm:text-2xl font-black text-slate-900 font-mono-data">64 %</div>
                  <div class="text-xs text-slate-500 font-medium">Hechas</div>
                </div>
                <div>
                  <div class="text-xl sm:text-2xl font-black text-[#D9531E] font-mono-data">21 %</div>
                  <div class="text-xs text-slate-500 font-medium">Descartadas</div>
                </div>
                <div>
                  <div class="text-xl sm:text-2xl font-black text-slate-400 font-mono-data">15 %</div>
                  <div class="text-xs text-slate-500 font-medium">Ignoradas</div>
                </div>
              </div>
            </div>

            <!-- Card 2: Motivos de descarte -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-3">
              <h3 class="font-bold text-sm text-slate-900">Motivos de descarte</h3>

              <div class="space-y-2 text-xs">
                <!-- Bar 1 -->
                <div class="flex items-center space-x-3">
                  <span class="w-40 text-slate-700 truncate">Cliente cerrado o ausente</span>
                  <div class="flex-1 bg-slate-100 rounded-full h-2.5 overflow-hidden">
                    <div class="bg-[#003E78] h-2.5 rounded-full" style="width: 70%"></div>
                  </div>
                  <span class="font-mono-data font-bold text-slate-900 w-6 text-right">25</span>
                </div>

                <!-- Bar 2 -->
                <div class="flex items-center space-x-3">
                  <span class="w-40 text-slate-700 truncate">Ya lo gestioné ayer</span>
                  <div class="flex-1 bg-slate-100 rounded-full h-2.5 overflow-hidden">
                    <div class="bg-[#003E78] h-2.5 rounded-full" style="width: 50%"></div>
                  </div>
                  <span class="font-mono-data font-bold text-slate-900 w-6 text-right">18</span>
                </div>

                <!-- Bar 3 -->
                <div class="flex items-center space-x-3">
                  <span class="w-40 text-slate-700 truncate">No tiene sentido</span>
                  <div class="flex-1 bg-slate-100 rounded-full h-2.5 overflow-hidden">
                    <div class="bg-[#D9531E] h-2.5 rounded-full" style="width: 35%"></div>
                  </div>
                  <span class="font-mono-data font-bold text-[#D9531E] w-6 text-right">13</span>
                </div>

                <!-- Bar 4 -->
                <div class="flex items-center space-x-3">
                  <span class="w-40 text-slate-700 truncate">Fuera de ruta hoy</span>
                  <div class="flex-1 bg-slate-100 rounded-full h-2.5 overflow-hidden">
                    <div class="bg-[#003E78] h-2.5 rounded-full" style="width: 25%"></div>
                  </div>
                  <span class="font-mono-data font-bold text-slate-900 w-6 text-right">10</span>
                </div>
              </div>
            </div>

          </div>

          <!-- Bottom Card: Revisión a ciegas · muestra de hoy -->
          <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 class="font-bold text-sm text-slate-900">Revisión a ciegas · muestra de hoy</h3>
              <span class="text-xs text-slate-500 font-mono-data">Aprobadas <strong>8 de 10</strong> · meta ≥ 8</span>
            </div>

            <div class="divide-y divide-slate-100 text-xs">
              <!-- Item 1 -->
              <div class="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="space-y-0.5 sm:w-2/3">
                  <div class="flex items-center space-x-2">
                    <span class="font-bold text-slate-900">Milena Ospino</span>
                    <span class="text-slate-400">•</span>
                    <span class="font-bold text-slate-700">Ferretería El Progreso</span>
                  </div>
                  <p class="text-slate-500">47 días sin comprar; antes compraba cada 12 días.</p>
                </div>
                <div class="flex items-center space-x-3 sm:w-1/3 justify-end font-mono-data">
                  <span class="font-bold text-slate-800">18,4 t</span>
                  <div class="flex items-center space-x-1.5 font-sans">
                    <button onclick="showToast('Sugerencia validada como útil', 'success')" class="bg-[#003E78] hover:bg-[#002D58] text-white font-bold px-3 py-1.5 rounded-lg transition-all text-xs">
                      Tiene sentido
                    </button>
                    <button onclick="showToast('Sugerencia rechazada', 'info')" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 font-semibold px-3 py-1.5 rounded-lg transition-all text-xs">
                      No
                    </button>
                  </div>
                </div>
              </div>

              <!-- Item 2 -->
              <div class="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="space-y-0.5 sm:w-2/3">
                  <div class="flex items-center space-x-2">
                    <span class="font-bold text-slate-900">Yesid Padilla</span>
                    <span class="text-slate-400">•</span>
                    <span class="font-bold text-slate-700">Ferremax Soledad</span>
                  </div>
                  <p class="text-slate-500">Volumen cayó 41 % y tiene obra activa cerca.</p>
                </div>
                <div class="flex items-center space-x-3 sm:w-1/3 justify-end font-mono-data">
                  <span class="font-bold text-slate-800">11,2 t</span>
                  <div class="flex items-center space-x-1.5 font-sans">
                    <button onclick="showToast('Sugerencia validada como útil', 'success')" class="bg-[#003E78] hover:bg-[#002D58] text-white font-bold px-3 py-1.5 rounded-lg transition-all text-xs">
                      Tiene sentido
                    </button>
                    <button onclick="showToast('Sugerencia rechazada', 'info')" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 font-semibold px-3 py-1.5 rounded-lg transition-all text-xs">
                      No
                    </button>
                  </div>
                </div>
              </div>

              <!-- Item 3 -->
              <div class="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="space-y-0.5 sm:w-2/3">
                  <div class="flex items-center space-x-2">
                    <span class="font-bold text-slate-900">Rafael Barrios</span>
                    <span class="text-slate-400">•</span>
                    <span class="font-bold text-slate-700">Depósito Gaira</span>
                  </div>
                  <p class="text-slate-500">Ofrecer Pañete y Estuco 2 en 1; compra solo cemento.</p>
                </div>
                <div class="flex items-center space-x-3 sm:w-1/3 justify-end font-mono-data">
                  <span class="font-bold text-slate-800">3,0 t</span>
                  <div class="flex items-center space-x-1.5 font-sans">
                    <button onclick="showToast('Sugerencia validada como útil', 'success')" class="bg-[#003E78] hover:bg-[#002D58] text-white font-bold px-3 py-1.5 rounded-lg transition-all text-xs">
                      Tiene sentido
                    </button>
                    <button onclick="showToast('Sugerencia rechazada', 'info')" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 font-semibold px-3 py-1.5 rounded-lg transition-all text-xs">
                      No
                    </button>
                  </div>
                </div>
              </div>

              <!-- Item 4 -->
              <div class="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="space-y-0.5 sm:w-2/3">
                  <div class="flex items-center space-x-2">
                    <span class="font-bold text-slate-900">Diana Charris</span>
                    <span class="text-slate-400">•</span>
                    <span class="font-bold text-slate-700">Materiales Taganga</span>
                  </div>
                  <p class="text-slate-500">Factura vencida hace 36 días.</p>
                </div>
                <div class="flex items-center space-x-3 sm:w-1/3 justify-end font-mono-data">
                  <span class="font-bold text-slate-800">6,1 t</span>
                  <div class="flex items-center space-x-1.5 font-sans">
                    <button onclick="showToast('Sugerencia validada como útil', 'success')" class="bg-[#003E78] hover:bg-[#002D58] text-white font-bold px-3 py-1.5 rounded-lg transition-all text-xs">
                      Tiene sentido
                    </button>
                    <button onclick="showToast('Sugerencia rechazada', 'info')" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 font-semibold px-3 py-1.5 rounded-lg transition-all text-xs">
                      No
                    </button>
                  </div>
                </div>
              </div>

            </div>
          </div>

        </section>

        <!-- ========================================================== -->
        <!-- SCREEN 2d: REGLAS                                          -->
        <!-- ========================================================== -->
        <section id="dtab-content-reglas" class="hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Reglas del Juego & Semáforo</h2>
              <p class="text-xs text-slate-500 font-medium mt-0.5">Definición de umbrales de compra, puntos de gamificación y condiciones de racha.</p>
            </div>
            <button onclick="showToast('Reglas guardadas en el sistema', 'success')" class="bg-[#003E78] hover:bg-[#002D58] text-white font-bold px-4 py-2 rounded-xl text-xs transition-all shadow-xs">
              Guardar Reglas
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-5 text-xs">
            <!-- Regla 1 -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-3">
              <span class="text-[10px] font-bold uppercase tracking-wider text-[#059669] bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">Umbrales Semáforo</span>
              <h3 class="font-bold text-sm text-slate-900">Días sin Compra de Cemento</h3>
              <div class="space-y-2 text-slate-600">
                <p>🟢 <strong>Verde:</strong> 0 a 14 días sin comprar.</p>
                <p>🟡 <strong>Amarillo:</strong> 15 a 39 días sin comprar.</p>
                <p>🔴 <strong>Rojo:</strong> 40+ días sin comprar (Alerta Crítica Antichurn).</p>
              </div>
            </div>

            <!-- Regla 2 -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-3">
              <span class="text-[10px] font-bold uppercase tracking-wider text-[#D9531E] bg-orange-50 px-2 py-0.5 rounded-md border border-orange-200">Gamificación</span>
              <h3 class="font-bold text-sm text-slate-900">Sistema de Puntos y Rachas</h3>
              <div class="space-y-2 text-slate-600">
                <p>⭐ <strong>Rescate Rojo ➔ Verde:</strong> +150 XP al asesor.</p>
                <p>🔥 <strong>Racha Diaria (11:59 PM):</strong> +100 XP por atender casos rojos.</p>
                <p>🛡️ <strong>Casco Protector:</strong> 1 comodín cada 7 días continuos.</p>
              </div>
            </div>

            <!-- Regla 3 -->
            <div class="bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-3">
              <span class="text-[10px] font-bold uppercase tracking-wider text-[#003E78] bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">Copiloto IA</span>
              <h3 class="font-bold text-sm text-slate-900">Políticas de Prioridad Automática</h3>
              <div class="space-y-2 text-slate-600">
                <p>🤖 <strong>Límite diario:</strong> Máximo 5 tareas sugeridas por asesor.</p>
                <p>🎯 <strong>Umbral de Aprobación:</strong> Mínimo 80% de utilidad.</p>
                <p>🔒 <strong>Protección Anticolisión:</strong> Casos asignados quedan bloqueados.</p>
              </div>
            </div>
          </div>
        </section>

        <!-- ========================================================== -->
        <!-- SCREEN 2e: AUDITORÍA                                       -->
        <!-- ========================================================== -->
        <section id="dtab-content-auditoria" class="hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">Auditoría & Bitácora Operativa</h2>
              <p class="text-xs text-slate-500 font-medium mt-0.5">Trazabilidad de modificaciones de metas, transferencias de cartera y auditoría IA.</p>
            </div>
            <button onclick="showToast('Log de auditoría exportado a CSV', 'info')" class="bg-white border border-slate-300 hover:bg-slate-50 text-slate-800 font-semibold px-4 py-2 rounded-xl text-xs transition-all shadow-xs">
              Descargar Bitácora
            </button>
          </div>

          <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs overflow-hidden">
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                  <tr>
                    <th class="py-3 px-4">Fecha & Hora</th>
                    <th class="py-3 px-4">Usuario</th>
                    <th class="py-3 px-4">Tipo de Acción</th>
                    <th class="py-3 px-4">Detalle / Valor Anterior ➔ Nuevo</th>
                    <th class="py-3 px-4 text-right">Estado</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 text-[11px]">
                  <tr class="hover:bg-slate-50">
                    <td class="py-2.5 px-4 font-mono-data text-slate-500">19 oct 2026, 05:40:12</td>
                    <td class="py-2.5 px-4 font-bold text-slate-900">Carlos Díaz</td>
                    <td class="py-2.5 px-4"><span class="bg-blue-50 text-blue-800 font-bold px-2 py-0.5 rounded-full text-[10px]">Ajuste de Meta</span></td>
                    <td class="py-2.5 px-4 font-mono-data">Milena Ospino · Noviembre: 446 t ➔ 460 t</td>
                    <td class="py-2.5 px-4 text-right text-emerald-700 font-bold">Completado</td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-2.5 px-4 font-mono-data text-slate-500">19 oct 2026, 04:15:33</td>
                    <td class="py-2.5 px-4 font-bold text-slate-900">Sistema Copiloto</td>
                    <td class="py-2.5 px-4"><span class="bg-purple-50 text-purple-800 font-bold px-2 py-0.5 rounded-full text-[10px]">Inferencia Groq LPU</span></td>
                    <td class="py-2.5 px-4 font-mono-data">openai/gpt-oss-120b · 312 sugerencias generadas</td>
                    <td class="py-2.5 px-4 text-right text-emerald-700 font-bold">Completado</td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-2.5 px-4 font-mono-data text-slate-500">18 oct 2026, 17:30:00</td>
                    <td class="py-2.5 px-4 font-bold text-slate-900">Carlos Mendoza</td>
                    <td class="py-2.5 px-4"><span class="bg-amber-50 text-amber-800 font-bold px-2 py-0.5 rounded-full text-[10px]">Transferencia Cartera</span></td>
                    <td class="py-2.5 px-4">Constructora Bolívar ➔ Milena Ospino</td>
                    <td class="py-2.5 px-4 text-right text-emerald-700 font-bold">Aprobado</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>

      </main>

    </div>
'''
