# -*- coding: utf-8 -*-
"""
Generates the comprehensive HTML for the redesigned Web Supervisor Corporate Dashboard
(#view-web). Incorporates executive KPIs, live Antichurn Radar with interactive filter tabs,
official Ultracem advisors leaderboard (Milena Ospino, Adriana Anaya, Hichel Espitia),
Planta Galapa industrial telemetry, and Vanesa IA strategic intelligence feed.
"""

def get_web_supervisor_html():
    return r'''
    <!-- ============================================================== -->
    <!-- VISTA SUPERVISOR WEB: PORTAL CORPORATIVO EJECUTIVO             -->
    <!-- ============================================================== -->
    <div id="view-web" class="hidden w-full max-w-7xl mx-auto space-y-6 animate-fadeIn">
      
      <!-- Top Corporate Executive Banner -->
      <div class="bg-gradient-to-r from-[#0F172A] via-[#003E78] to-[#0F172A] rounded-3xl p-6 sm:p-8 text-white shadow-xl border-t-4 border-[#FDCA02] relative overflow-hidden">
        <!-- Background subtle glow -->
        <div class="absolute -right-16 -bottom-16 w-64 h-64 bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6 relative z-10">
          <div class="space-y-2">
            <div class="flex flex-wrap items-center gap-2">
              <span class="text-[10px] font-black uppercase tracking-widest text-teal-300 bg-teal-950/80 px-2.5 py-0.5 rounded-full border border-teal-500/40">Portal de Mando Ejecutivo</span>
              <span class="text-xs text-slate-400">•</span>
              <span class="text-[10px] font-bold text-amber-300 bg-amber-950/60 px-2.5 py-0.5 rounded-full border border-amber-500/40">Planta Galapa, Atlántico</span>
              <span class="text-xs text-slate-400">•</span>
              <span class="text-[10px] font-bold text-emerald-300 bg-emerald-950/60 px-2.5 py-0.5 rounded-full border border-emerald-500/40 flex items-center">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse mr-1"></span>
                Operaciones 100% en Vivo
              </span>
            </div>

            <h2 class="text-2xl sm:text-3xl font-black tracking-tight text-white">
              Supervisión Comercial, Ligas de Campo & Prevención Antichurn
            </h2>
            <p class="text-xs text-slate-300 max-w-2xl leading-relaxed">
              Monitoreo centralizado de 18 asesores comerciales de campo, 240 obras activas en la Región Caribe y estado de despachos de tractomulas y mixers de cemento Ultracem.
            </p>
          </div>

          <!-- Quick Action Buttons -->
          <div class="flex flex-wrap items-center gap-2.5 flex-shrink-0">
            <button onclick="showToast('Sincronización con ERP SAP iniciada: 240 cuentas actualizadas', 'info')" class="btn-tactile text-xs font-bold px-3.5 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white border border-white/20 transition-all flex items-center space-x-1.5 backdrop-blur-md">
              <span>🔄</span>
              <span>Sincronizar SAP</span>
            </button>
            <button onclick="showToast('Informe Ejecutivo descargado en formato Excel/PDF', 'success')" class="btn-tactile text-xs font-bold px-4 py-2 rounded-xl bg-[#FDCA02] hover:bg-amber-400 text-slate-900 shadow-md transition-all flex items-center space-x-1.5">
              <span>📊</span>
              <span>Exportar Reporte</span>
            </button>
          </div>
        </div>

        <!-- Telemetry Status Bar -->
        <div class="mt-6 pt-4 border-t border-white/10 flex flex-wrap items-center justify-between gap-3 text-xs text-slate-300">
          <div class="flex items-center space-x-4 text-[11px]">
            <span>🏭 <strong>Molienda Galapa:</strong> 180 Ton/h</span>
            <span>🔥 <strong>Hornos Clínker:</strong> 1,450 °C</span>
            <span>🚚 <strong>Flota en Ruta:</strong> 22 Tractomulas + 14 Mixers</span>
          </div>
          <div class="text-[11px] font-mono-data text-amber-300">
            ⏰ Próximo Corte Antichurn: <strong>11:59 PM Hoy</strong>
          </div>
        </div>
      </div>

      <!-- KPI Grid (5 Enterprise Cards) -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3.5">
        <!-- KPI 1 -->
        <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
          <div class="flex items-center justify-between text-slate-400 text-xs">
            <span class="font-bold uppercase tracking-wider text-[10px]">Toneladas Mes</span>
            <span>📦</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-black text-slate-900 font-mono-data">14,850 T</h3>
          <div class="w-full bg-slate-100 rounded-full h-1.5 mt-2 overflow-hidden">
            <div class="bg-teal-500 h-1.5 rounded-full" style="width: 92.8%"></div>
          </div>
          <p class="text-[10px] text-teal-700 font-bold mt-1">92.8% de la meta (16k T)</p>
        </div>

        <!-- KPI 2 -->
        <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
          <div class="flex items-center justify-between text-slate-400 text-xs">
            <span class="font-bold uppercase tracking-wider text-[10px]">Facturación Activa</span>
            <span>💰</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-black text-[#003E78] font-mono-data">$4,722 M</h3>
          <p class="text-[10px] text-emerald-600 font-bold mt-2 flex items-center">
            <span>▲ +8.4%</span>
            <span class="text-slate-400 font-normal ml-1">vs mes anterior</span>
          </p>
        </div>

        <!-- KPI 3 -->
        <div class="bg-white rounded-2xl p-4 border border-rose-200 bg-rose-50/20 shadow-xs space-y-1">
          <div class="flex items-center justify-between text-rose-500 text-xs">
            <span class="font-bold uppercase tracking-wider text-[10px]">Cartera en Riesgo</span>
            <span>🚨</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-black text-rose-600 font-mono-data">$184.2 M</h3>
          <p class="text-[10px] text-rose-700 font-bold mt-2">6 cuentas con SLA crítico</p>
        </div>

        <!-- KPI 4 -->
        <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1">
          <div class="flex items-center justify-between text-slate-400 text-xs">
            <span class="font-bold uppercase tracking-wider text-[10px]">SLA Desbloqueo</span>
            <span>⏱️</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-black text-emerald-600 font-mono-data">1.8 Horas</h3>
          <p class="text-[10px] text-slate-500 mt-2">Meta: &lt; 4.0h • 98.4% a tiempo</p>
        </div>

        <!-- KPI 5 -->
        <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-1 col-span-2 sm:col-span-1">
          <div class="flex items-center justify-between text-slate-400 text-xs">
            <span class="font-bold uppercase tracking-wider text-[10px]">Racha Promedio</span>
            <span>🔥</span>
          </div>
          <h3 class="text-xl sm:text-2xl font-black text-amber-600 font-mono-data">18.4 Días</h3>
          <p class="text-[10px] text-slate-500 mt-2">3 Cascos protectores activos</p>
        </div>
      </div>

      <!-- Supervisor Internal Tabs Bar -->
      <div class="bg-white rounded-2xl border border-slate-200 p-1.5 flex flex-wrap items-center justify-between gap-2 shadow-xs">
        <div class="flex items-center space-x-1 overflow-x-auto text-xs">
          <button id="sup-tab-btn-radar" onclick="switchSupervisorTab('radar')" class="btn-tactile px-3.5 py-2 rounded-xl font-bold transition-all bg-[#003E78] text-white shadow-xs flex items-center space-x-1.5">
            <span>🎯</span>
            <span>Radar Antichurn (6)</span>
          </button>
          <button id="sup-tab-btn-ranking" onclick="switchSupervisorTab('ranking')" class="btn-tactile px-3.5 py-2 rounded-xl font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center space-x-1.5">
            <span>🏆</span>
            <span>Ranking Asesores & Ligas</span>
          </button>
          <button id="sup-tab-btn-galapa" onclick="switchSupervisorTab('galapa')" class="btn-tactile px-3.5 py-2 rounded-xl font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center space-x-1.5">
            <span>🏭</span>
            <span>Planta Galapa & Silos</span>
          </button>
          <button id="sup-tab-btn-vanesa" onclick="switchSupervisorTab('vanesa')" class="btn-tactile px-3.5 py-2 rounded-xl font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center space-x-1.5">
            <span>🤖</span>
            <span>Inteligencia Vanesa IA</span>
          </button>
        </div>

        <div class="text-xs text-slate-500 px-3 hidden md:flex items-center space-x-2">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          <span>Actualización en tiempo real</span>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- SUPERVISOR TAB 1: RADAR ANTICHURN & CUENTAS CRÍTICAS           -->
      <!-- ============================================================== -->
      <div id="sup-tab-content-radar" class="space-y-4">
        
        <!-- Filter Bar -->
        <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex flex-wrap items-center justify-between gap-3 text-xs">
          <div class="flex flex-wrap items-center gap-1.5">
            <span class="text-slate-400 font-bold uppercase text-[10px] mr-1">Filtrar por:</span>
            <button onclick="filterRadarTable('todos')" id="filter-btn-todos" class="px-3 py-1 rounded-lg font-bold bg-slate-900 text-white">Todas (6)</button>
            <button onclick="filterRadarTable('critico')" id="filter-btn-critico" class="px-3 py-1 rounded-lg font-semibold text-rose-700 bg-rose-50 hover:bg-rose-100 border border-rose-200">🔴 Críticas (3)</button>
            <button onclick="filterRadarTable('advertencia')" id="filter-btn-advertencia" class="px-3 py-1 rounded-lg font-semibold text-amber-700 bg-amber-50 hover:bg-amber-100 border border-amber-200">🟡 Advertencia (2)</button>
            <button onclick="filterRadarTable('escalado')" id="filter-btn-escalado" class="px-3 py-1 rounded-lg font-semibold text-blue-700 bg-blue-50 hover:bg-blue-100 border border-blue-200">⏳ Escaladas (1)</button>
          </div>
          <div class="text-slate-500 text-[11px]">
            Mostrando 6 cuentas en ventana de reposición
          </div>
        </div>

        <!-- Radar Table Container -->
        <div class="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                <tr>
                  <th class="py-3.5 px-5">Cliente / Obra</th>
                  <th class="py-3.5 px-4">Canal & Ubicación</th>
                  <th class="py-3.5 px-4">Asesor Asignado</th>
                  <th class="py-3.5 px-4">Semáforo & Inactividad</th>
                  <th class="py-3.5 px-4">Volumen Mensual</th>
                  <th class="py-3.5 px-4">Bloqueo / SLA</th>
                  <th class="py-3.5 px-5 text-right">Acción Supervisor</th>
                </tr>
              </thead>
              <tbody id="sup-radar-table-body" class="divide-y divide-slate-100">
                
                <!-- Row 1: Crítico 1 -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="critico">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Consorcio Vial del Norte</div>
                    <span class="text-[11px] text-slate-500">Autopista al Mar 3 • Puente Magdalena</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-blue-50 text-blue-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-blue-200">Industrial 4G</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Barranquilla, ATL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-blue-100 text-[#003E78] font-bold text-[9px] flex items-center justify-center">MO</span>
                      <span>Milena Ospino</span>
                    </div>
                    <span class="text-[10px] text-emerald-600 font-bold">28 días racha 🔥</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-100 text-rose-800 border border-rose-200">
                      <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse mr-1"></span>
                      9 días sin contacto
                    </span>
                    <span class="block text-[10px] text-rose-600 font-bold mt-0.5">Riesgo fuga a Argos</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">320 Ton</span>
                    <span class="block text-[10px] text-slate-500">$98.5 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-rose-700 font-bold text-[11px] block">Exceso de Cupo Cartera</span>
                    <span class="text-[10px] text-slate-500">SLA Cartera: 1h 20m restantes</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Aprobación excepcional de cupo concedida para Consorcio Vial', 'success')" class="btn-tactile bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 font-bold px-2.5 py-1 rounded-lg text-[11px]">
                      Aprobar Cupo
                    </button>
                    <button onclick="showToast('Alerta enviada a Milena Ospino por WhatsApp', 'info')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold px-2.5 py-1 rounded-lg text-[11px]">
                      Avisar
                    </button>
                  </td>
                </tr>

                <!-- Row 2: Crítico 2 -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="critico">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Ferretería El Martillo del Caribe</div>
                    <span class="text-[11px] text-slate-500">Sede Principal • Av. Pedro de Heredia</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-teal-50 text-teal-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-teal-200">Ferretería</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Cartagena, BOL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-amber-100 text-amber-800 font-bold text-[9px] flex items-center justify-center">AA</span>
                      <span>Adriana Anaya</span>
                    </div>
                    <span class="text-[10px] text-emerald-600 font-bold">24 días racha 🔥</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-100 text-rose-800 border border-rose-200">
                      <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse mr-1"></span>
                      6 días sin pedido
                    </span>
                    <span class="block text-[10px] text-amber-600 font-bold mt-0.5">Stock bultos al 15%</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">85 Ton</span>
                    <span class="block text-[10px] text-slate-500">$26.8 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-amber-700 font-bold text-[11px] block">Precio Competencia</span>
                    <span class="text-[10px] text-slate-500">Argos ofreció -$600/bulto</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Descuento especial por volumen autorizado para Cartagena', 'success')" class="btn-tactile bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 font-bold px-2.5 py-1 rounded-lg text-[11px]">
                      Ajustar Margen
                    </button>
                    <button onclick="showToast('Notificación enviada a Adriana Anaya', 'info')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold px-2.5 py-1 rounded-lg text-[11px]">
                      Avisar
                    </button>
                  </td>
                </tr>

                <!-- Row 3: Crítico 3 (Asesor Actual Demo) -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="critico">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Constructora Bolívar — Torres del Mar</div>
                    <span class="text-[11px] text-slate-500">Torre 4 en fundición de placa</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-blue-50 text-blue-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-blue-200">Industrial</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Barranquilla, ATL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-teal-100 text-teal-800 font-bold text-[9px] flex items-center justify-center">CM</span>
                      <span>Carlos Mendoza (Demo)</span>
                    </div>
                    <span class="text-[10px] text-amber-600 font-bold">18 días racha ⚠️</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-rose-100 text-rose-800 border border-rose-200">
                      <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse mr-1"></span>
                      8 días atraso
                    </span>
                    <span class="block text-[10px] text-rose-600 font-bold mt-0.5">Corte racha 11:59 PM</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">120 Ton</span>
                    <span class="block text-[10px] text-slate-500">$38.2 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-purple-700 font-bold text-[11px] block">Retraso Despacho Mixer</span>
                    <span class="text-[10px] text-slate-500">SLA Logística: Vencido</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Mixer #14 priorizado desde Planta Galapa', 'success')" class="btn-tactile bg-teal-50 hover:bg-teal-100 text-teal-800 border border-teal-200 font-bold px-2.5 py-1 rounded-lg text-[11px]">
                      Priorizar Mixer
                    </button>
                    <button onclick="openTransferClientModal('Constructora Bolívar')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold px-2.5 py-1 rounded-lg text-[11px]">
                      Reasignar
                    </button>
                  </td>
                </tr>

                <!-- Row 4: Advertencia 1 -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="advertencia">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Bloquera del Caribe S.A.S.</div>
                    <span class="text-[11px] text-slate-500">Parque Industrial Malambo (PIMSA)</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-indigo-50 text-indigo-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-indigo-200">Prefabricados</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Malambo, ATL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-purple-100 text-purple-800 font-bold text-[9px] flex items-center justify-center">HE</span>
                      <span>Hichel Espitia</span>
                    </div>
                    <span class="text-[10px] text-emerald-600 font-bold">21 días racha 🔥</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-amber-100 text-amber-800 border border-amber-200">
                      4 días sin contacto
                    </span>
                    <span class="block text-[10px] text-slate-500 mt-0.5">Requiere Cemento Estructural</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">190 Ton</span>
                    <span class="block text-[10px] text-slate-500">$59.4 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-emerald-700 font-bold text-[11px] block">Cotización en Revisión</span>
                    <span class="text-[10px] text-slate-500">Vence en 48 horas</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Recordatorio automático enviado a Hichel Espitia', 'info')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold px-2.5 py-1 rounded-lg text-[11px]">
                      Recordar
                    </button>
                  </td>
                </tr>

                <!-- Row 5: Advertencia 2 -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="advertencia">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Ferretería El Constructor de Soledad</div>
                    <span class="text-[11px] text-slate-500">Sede Calle 30 • Soledad 2000</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-teal-50 text-teal-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-teal-200">Ferretería</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Soledad, ATL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-teal-100 text-teal-800 font-bold text-[9px] flex items-center justify-center">CM</span>
                      <span>Carlos Mendoza (Demo)</span>
                    </div>
                    <span class="text-[10px] text-amber-600 font-bold">18 días racha ⚠️</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-amber-100 text-amber-800 border border-amber-200">
                      4 días atraso
                    </span>
                    <span class="block text-[10px] text-amber-600 font-bold mt-0.5">Alerta Fraguado</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">45 Ton</span>
                    <span class="block text-[10px] text-slate-500">$14.2 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-blue-700 font-bold text-[11px] block">Cupo de $20M en trámite</span>
                    <span class="text-[10px] text-slate-500">SLA Cartera: 2h restantes</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Cupo de $20M pre-aprobado por supervisor', 'success')" class="btn-tactile bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 font-bold px-2.5 py-1 rounded-lg text-[11px]">
                      Aprobar Cupo
                    </button>
                  </td>
                </tr>

                <!-- Row 6: Escalada -->
                <tr class="hover:bg-slate-50/80 transition-colors radar-row" data-type="escalado">
                  <td class="py-3.5 px-5">
                    <div class="font-extrabold text-slate-900 text-sm">Marval — Altos de Riomar Torre 3</div>
                    <span class="text-[11px] text-slate-500">Diseño Especial Cemento Marino NTC 121</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="bg-blue-50 text-blue-800 font-bold px-2 py-0.5 rounded-full text-[10px] border border-blue-200">Industrial</span>
                    <span class="block text-[10px] text-slate-400 mt-0.5">Barranquilla, ATL</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <div class="font-semibold text-slate-800 flex items-center space-x-1.5">
                      <span class="w-5 h-5 rounded-full bg-emerald-100 text-emerald-800 font-bold text-[9px] flex items-center justify-center">LV</span>
                      <span>Laura Valencia</span>
                    </div>
                    <span class="text-[10px] text-emerald-600 font-bold">34 días racha 🔥</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-blue-100 text-blue-800 border border-blue-200">
                      Escalado Activo
                    </span>
                    <span class="block text-[10px] text-emerald-600 font-bold mt-0.5">Racha Salvada</span>
                  </td>
                  <td class="py-3.5 px-4 font-mono-data">
                    <span class="font-bold text-slate-900">210 Ton</span>
                    <span class="block text-[10px] text-slate-500">$65.8 M COP</span>
                  </td>
                  <td class="py-3.5 px-4">
                    <span class="text-teal-700 font-bold text-[11px] block">Laboratorio Calidad Galapa</span>
                    <span class="text-[10px] text-slate-500">SLA Calidad: 3h restantes</span>
                  </td>
                  <td class="py-3.5 px-5 text-right space-x-1 whitespace-nowrap">
                    <button onclick="showToast('Certificado de rotura y resistencia NTC 121 emitido en línea', 'success')" class="btn-tactile bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 font-bold px-2.5 py-1 rounded-lg text-[11px]">
                      Emitir Certificado
                    </button>
                  </td>
                </tr>

              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- SUPERVISOR TAB 2: RANKING ASESORES OFICIALES & LIGAS           -->
      <!-- ============================================================== -->
      <div id="sup-tab-content-ranking" class="hidden space-y-6">
        
        <!-- Podium Top 3 Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          
          <!-- 1st Place: Milena Ospino -->
          <div class="bg-gradient-to-b from-amber-50 to-white rounded-3xl p-5 border-2 border-amber-300 shadow-sm relative space-y-3">
            <div class="absolute -top-3 -right-2 bg-amber-400 text-slate-900 font-black text-xs px-3 py-1 rounded-full shadow-xs flex items-center space-x-1">
              <span>🥇</span>
              <span>Líder Regional</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-12 h-12 rounded-2xl bg-[#003E78] text-white font-black text-sm flex items-center justify-center shadow-xs">MO</div>
              <div>
                <h3 class="font-extrabold text-base text-slate-900">Milena Ospino</h3>
                <span class="text-xs text-slate-500 block">Asesora Senior Concretos • Costa Norte</span>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div class="bg-white p-2.5 rounded-xl border border-amber-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Racha Activa</span>
                <span class="font-black text-amber-600 text-base font-mono-data">28 Días 🔥</span>
              </div>
              <div class="bg-white p-2.5 rounded-xl border border-amber-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Volumen Mes</span>
                <span class="font-black text-slate-900 text-base font-mono-data">940 Ton</span>
              </div>
            </div>
            <div class="text-[11px] text-slate-600 space-y-1">
              <p>📧 <strong>Email:</strong> mospino@ultracem.co</p>
              <p>🌱 <strong>Nivel Semillero:</strong> Brote Nivel 4 (Planta Fértil)</p>
              <p>🛡️ <strong>Cascos de Seguridad:</strong> 2 activos</p>
            </div>
          </div>

          <!-- 2nd Place: Adriana Anaya -->
          <div class="bg-gradient-to-b from-slate-50 to-white rounded-3xl p-5 border border-slate-300 shadow-sm relative space-y-3">
            <div class="absolute -top-3 -right-2 bg-slate-300 text-slate-800 font-black text-xs px-3 py-1 rounded-full shadow-xs flex items-center space-x-1">
              <span>🥈</span>
              <span>2° Puesto</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-12 h-12 rounded-2xl bg-amber-500 text-white font-black text-sm flex items-center justify-center shadow-xs">AA</div>
              <div>
                <h3 class="font-extrabold text-base text-slate-900">Adriana Anaya</h3>
                <span class="text-xs text-slate-500 block">Ferreterías & Depósitos • Bolívar / Atlántico</span>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Racha Activa</span>
                <span class="font-black text-amber-600 text-base font-mono-data">24 Días 🔥</span>
              </div>
              <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Volumen Mes</span>
                <span class="font-black text-slate-900 text-base font-mono-data">820 Ton</span>
              </div>
            </div>
            <div class="text-[11px] text-slate-600 space-y-1">
              <p>📧 <strong>Email:</strong> aanaya@ultracem.co</p>
              <p>🌱 <strong>Nivel Semillero:</strong> Brote Nivel 4 (Planta Fértil)</p>
              <p>🛡️ <strong>Cascos de Seguridad:</strong> 1 activo</p>
            </div>
          </div>

          <!-- 3rd Place: Hichel Espitia -->
          <div class="bg-gradient-to-b from-amber-50/40 to-white rounded-3xl p-5 border border-amber-200 shadow-sm relative space-y-3">
            <div class="absolute -top-3 -right-2 bg-amber-700 text-white font-black text-xs px-3 py-1 rounded-full shadow-xs flex items-center space-x-1">
              <span>🥉</span>
              <span>3° Puesto</span>
            </div>
            <div class="flex items-center space-x-3">
              <div class="w-12 h-12 rounded-2xl bg-[#14B8A6] text-white font-black text-sm flex items-center justify-center shadow-xs">HE</div>
              <div>
                <h3 class="font-extrabold text-base text-slate-900">Hichel Espitia</h3>
                <span class="text-xs text-slate-500 block">Proyectos Industriales & Obra 4G</span>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Racha Activa</span>
                <span class="font-black text-amber-600 text-base font-mono-data">21 Días 🔥</span>
              </div>
              <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-center">
                <span class="text-[10px] text-slate-400 block font-bold">Volumen Mes</span>
                <span class="font-black text-slate-900 text-base font-mono-data">1,150 Ton</span>
              </div>
            </div>
            <div class="text-[11px] text-slate-600 space-y-1">
              <p>📱 <strong>Teléfono:</strong> 310 250 3454</p>
              <p>🌱 <strong>Nivel Semillero:</strong> Brote Nivel 3 (Tallo Fuerte)</p>
              <p>🛡️ <strong>Cascos de Seguridad:</strong> 2 activos</p>
            </div>
          </div>

        </div>

        <!-- Team Table -->
        <div class="bg-white rounded-3xl border border-slate-200 shadow-xs overflow-hidden">
          <div class="p-5 border-b border-slate-100 flex items-center justify-between">
            <h3 class="font-extrabold text-sm text-slate-900">Plantilla Completa de Asesores de Campo (18 Asesores)</h3>
            <span class="text-xs text-slate-500">Ordenados por racha continua acumulada</span>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-50 text-slate-400 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                <tr>
                  <th class="py-3 px-5">Pos</th>
                  <th class="py-3 px-4">Asesor Comercial</th>
                  <th class="py-3 px-4">Zona / Especialidad</th>
                  <th class="py-3 px-4">Racha Activa</th>
                  <th class="py-3 px-4">Toneladas Despachadas</th>
                  <th class="py-3 px-4">Cumplimiento SLA</th>
                  <th class="py-3 px-5 text-right">Acción</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                <tr class="hover:bg-slate-50">
                  <td class="py-3 px-5 font-bold text-amber-600">1°</td>
                  <td class="py-3 px-4 font-bold text-slate-900">Milena Ospino</td>
                  <td class="py-3 px-4 text-slate-600">Costa Norte (Concretos)</td>
                  <td class="py-3 px-4 font-bold text-amber-600 font-mono-data">28 Días 🔥</td>
                  <td class="py-3 px-4 font-mono-data">940 Ton</td>
                  <td class="py-3 px-4 text-emerald-600 font-bold">100%</td>
                  <td class="py-3 px-5 text-right"><button onclick="showToast('Ver perfil de Milena Ospino', 'info')" class="text-teal-700 hover:underline font-bold">Ver Perfil</button></td>
                </tr>
                <tr class="hover:bg-slate-50">
                  <td class="py-3 px-5 font-bold text-slate-500">2°</td>
                  <td class="py-3 px-4 font-bold text-slate-900">Adriana Anaya</td>
                  <td class="py-3 px-4 text-slate-600">Ferreterías Bolívar/Atlántico</td>
                  <td class="py-3 px-4 font-bold text-amber-600 font-mono-data">24 Días 🔥</td>
                  <td class="py-3 px-4 font-mono-data">820 Ton</td>
                  <td class="py-3 px-4 text-emerald-600 font-bold">98%</td>
                  <td class="py-3 px-5 text-right"><button onclick="showToast('Ver perfil de Adriana Anaya', 'info')" class="text-teal-700 hover:underline font-bold">Ver Perfil</button></td>
                </tr>
                <tr class="hover:bg-slate-50">
                  <td class="py-3 px-5 font-bold text-amber-800">3°</td>
                  <td class="py-3 px-4 font-bold text-slate-900">Hichel Espitia</td>
                  <td class="py-3 px-4 text-slate-600">Infraestructura 4G</td>
                  <td class="py-3 px-4 font-bold text-amber-600 font-mono-data">21 Días 🔥</td>
                  <td class="py-3 px-4 font-mono-data">1,150 Ton</td>
                  <td class="py-3 px-4 text-emerald-600 font-bold">96%</td>
                  <td class="py-3 px-5 text-right"><button onclick="showToast('Ver perfil de Hichel Espitia', 'info')" class="text-teal-700 hover:underline font-bold">Ver Perfil</button></td>
                </tr>
                <tr class="hover:bg-slate-50 bg-teal-50/20">
                  <td class="py-3 px-5 font-bold text-slate-700">4°</td>
                  <td class="py-3 px-4 font-bold text-slate-900">Carlos Mendoza (Demo Activa)</td>
                  <td class="py-3 px-4 text-slate-600">Soledad & Corredor Industrial</td>
                  <td class="py-3 px-4 font-bold text-amber-600 font-mono-data">18 Días 🔥</td>
                  <td class="py-3 px-4 font-mono-data">680 Ton</td>
                  <td class="py-3 px-4 text-emerald-600 font-bold">94%</td>
                  <td class="py-3 px-5 text-right"><button onclick="switchView('mobile')" class="text-[#003E78] hover:underline font-bold">Ver en Móvil</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>

      <!-- ============================================================== -->
      <!-- SUPERVISOR TAB 3: PLANTA GALAPA & SILOS                        -->
      <!-- ============================================================== -->
      <div id="sup-tab-content-galapa" class="hidden space-y-6">
        
        <div class="bg-white rounded-3xl p-6 border border-slate-200 shadow-xs space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
            <div>
              <span class="text-[10px] font-bold uppercase tracking-wider text-teal-700 bg-teal-50 px-2.5 py-0.5 rounded-full border border-teal-200">Hub Industrial Central</span>
              <h3 class="text-xl font-black text-slate-900 mt-1">Planta de Cemento Galapa (Atlántico)</h3>
              <p class="text-xs text-slate-500">Km 8 Vía Galapa - Tubará • Capacidad instalada: 180 Ton/hora</p>
            </div>
            <div class="flex items-center space-x-2">
              <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse mr-1.5"></span>
                Operación Normal Continua
              </span>
            </div>
          </div>

          <!-- Silos Grid -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Silo 1 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-slate-900">Silo 1: Estructural Max</span>
                <span class="font-bold text-teal-700 font-mono-data">94% Capacidad</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-3 overflow-hidden">
                <div class="bg-[#003E78] h-3 rounded-full" style="width: 94%"></div>
              </div>
              <div class="flex justify-between text-[11px] text-slate-500">
                <span>Disponible: <strong>4,700 Ton</strong></span>
                <span>Capacidad: 5,000 Ton</span>
              </div>
              <span class="block text-[10px] text-slate-400">Norma NTC 121 • Alta resistencia temprana a 3 y 28 días</span>
            </div>

            <!-- Silo 2 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-slate-900">Silo 2: Uso General</span>
                <span class="font-bold text-teal-700 font-mono-data">88% Capacidad</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-3 overflow-hidden">
                <div class="bg-teal-600 h-3 rounded-full" style="width: 88%"></div>
              </div>
              <div class="flex justify-between text-[11px] text-slate-500">
                <span>Disponible: <strong>3,960 Ton</strong></span>
                <span>Capacidad: 4,500 Ton</span>
              </div>
              <span class="block text-[10px] text-slate-400">Para ferreterías, pañetes y fundiciones residenciales estándar</span>
            </div>

            <!-- Silo 3 -->
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-slate-900">Silo 3: Cemento Marino</span>
                <span class="font-bold text-teal-700 font-mono-data">76% Capacidad</span>
              </div>
              <div class="w-full bg-slate-200 rounded-full h-3 overflow-hidden">
                <div class="bg-amber-500 h-3 rounded-full" style="width: 76%"></div>
              </div>
              <div class="flex justify-between text-[11px] text-slate-500">
                <span>Disponible: <strong>2,280 Ton</strong></span>
                <span>Capacidad: 3,000 Ton</span>
              </div>
              <span class="block text-[10px] text-slate-400">Resistente a sulfatos marinos y obras portuarias en el Caribe</span>
            </div>
          </div>

          <!-- Logistics Fleet Status -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs pt-2">
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <div class="flex items-center space-x-2">
                <span class="text-base">🚚</span>
                <h4 class="font-bold text-slate-900">Despacho de Tractomulas a Granel</h4>
              </div>
              <p class="text-slate-600">22 tractomulas graneleras despachadas hoy hacia plantas de concreto de Barranquilla, Malambo y Cartagena.</p>
              <span class="inline-block text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">Tiempo promedio báscula: 14 min</span>
            </div>

            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <div class="flex items-center space-x-2">
                <span class="text-base">🔄</span>
                <h4 class="font-bold text-slate-900">Flota de Mixers (Concreto Premezclado)</h4>
              </div>
              <p class="text-slate-600">14 camiones mezcladores en ruta activa con monitoreo GPS de temperatura de fraguado y tiempo de descarga.</p>
              <span class="inline-block text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded-full">SLA de entrega en obra: 99.1%</span>
            </div>
          </div>
        </div>

      </div>

      <!-- ============================================================== -->
      <!-- SUPERVISOR TAB 4: INTELIGENCIA COMERCIAL VANESA IA             -->
      <!-- ============================================================== -->
      <div id="sup-tab-content-vanesa" class="hidden space-y-4">
        
        <div class="bg-gradient-to-r from-[#0F172A] via-[#132A3E] to-[#0F172A] rounded-3xl p-6 text-white space-y-4 border border-teal-500/30">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 rounded-xl bg-teal-500/20 border border-teal-400 flex items-center justify-center text-lg">🤖</div>
            <div>
              <h3 class="font-black text-lg text-white">Copiloto Estratégico Vanesa IA • Alertas de Mercado</h3>
              <p class="text-xs text-teal-200/80">Motor de análisis predictivo alimentado con Groq LPU y telemetría de obras</p>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
          <!-- Card 1 -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs space-y-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">Oportunidad de Demanda</span>
            <h4 class="font-extrabold text-slate-900 text-sm">Incremento de Obras Portuarias en Bolívar</h4>
            <p class="text-slate-600 leading-relaxed">
              Se proyecta un incremento del 14% en la demanda de Cemento Marino para el mes de noviembre por adecuaciones portuarias en Mamonal.
            </p>
            <button onclick="showToast('Alerta de oportunidad enviada a Adriana Anaya', 'info')" class="text-teal-700 font-bold hover:underline">Asignar campaña preventiva ➔</button>
          </div>

          <!-- Card 2 -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs space-y-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">Radar de Competencia</span>
            <h4 class="font-extrabold text-slate-900 text-sm">Ajuste de Precios de Argos en Soledad</h4>
            <p class="text-slate-600 leading-relaxed">
              Argos redujo el precio de bulto en $500 COP en 4 ferreterías de la Calle 30. Se recomienda contraofertar con asistencia técnica gratuita en obra.
            </p>
            <button onclick="showToast('Protocolo de defensa comercial activado para Soledad', 'success')" class="text-teal-700 font-bold hover:underline">Activar protocolo de defensa ➔</button>
          </div>

          <!-- Card 3 -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs space-y-2">
            <span class="text-[10px] font-bold uppercase tracking-wider text-teal-700 bg-teal-50 px-2 py-0.5 rounded-md border border-teal-200">Predicción Antichurn</span>
            <h4 class="font-extrabold text-slate-900 text-sm">Recompra Prevista: Bloqueras Vía 40</h4>
            <p class="text-slate-600 leading-relaxed">
              Consorcio Bloqueras de la Vía 40 agotará su inventario de clínker en 72 horas. Si Hichel Espitia contacta hoy, la probabilidad de cierre es del 96%.
            </p>
            <button onclick="showToast('Recomendación enviada a Hichel Espitia', 'info')" class="text-teal-700 font-bold hover:underline">Notificar a asesor ➔</button>
          </div>
        </div>

      </div>

    </div>
'''
