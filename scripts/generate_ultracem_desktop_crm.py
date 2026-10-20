# -*- coding: utf-8 -*-
"""
Generates the Full Desktop Computer Application of the Ultracem CRM
("Usa tipo el que esta en el celular pero para computador y que tenga las mismas funcionalidades y interacciones.")

STRICT SPECIFICATIONS:
1. ONLY ULTRACEM BRANDING (Semillero / CooWeb 100% removed).
2. Primary brand colors: Amarillo (#FDCA02), Azul Oscuro (#003E78 / #0A233F), and Blanco (#FFFFFF).
3. 100% SOLID COLORS ONLY (zero gradients).
4. Full features:
   - Tab 1: Racha & Obras (Carlos Mendoza, racha 21d, corte 11:59 PM timer, Don Fraguado widget, client portfolio with semaphores, audio recording console, WhatsApp action, internal escalation SLA).
   - Tab 2: Copiloto IA (Multimodel Groq/NVIDIA/DeepSeek chat with starters and cement NTC 121 guardrails).
   - Tab 3: Radar & Directorio B2B (Interactive Leaflet Colombia Map + 12 Caribbean qualified prospects).
   - Tab 4: Liga de Asesores (Leaderboard with Milena Ospino, Adriana Anaya, Hichel Espitia, Carlos Mendoza).
   - Tab 5: Perfil & Cartera (Safety helmets, 30-day activity heatmap, client transfer module).
"""

def get_ultracem_desktop_crm_html():
    return r'''
    <!-- ============================================================== -->
    <!-- APLICACIÓN DE ESCRITORIO ULTRACEM CRM (FULL COMPUTADOR)        -->
    <!-- Misma funcionalidad e interacciones que el celular en desktop  -->
    <!-- Colores Primarios: Amarillo #FDCA02, Azul Oscuro #003E78, Blanco #FFFFFF -->
    <!-- ============================================================== -->
    <div id="ultracem-desktop-crm" class="w-full bg-[#F2F1EC] rounded-3xl border-2 border-slate-300 shadow-md overflow-hidden flex flex-col md:flex-row min-h-[820px]">
      
      <!-- ============================================================ -->
      <!-- SIDEBAR CORPORATIVO: AZUL OSCURO SÓLIDO (#003E78 / #0A233F)  -->
      <!-- ============================================================ -->
      <aside class="w-full md:w-64 bg-[#0A233F] text-white flex flex-col flex-shrink-0 p-4 border-r-2 border-slate-800 select-none justify-between">
        
        <div>
          <!-- Logo Ultracem Container with Amarillo Accent -->
          <div class="bg-white rounded-2xl p-2.5 border-2 border-[#FDCA02] mb-5 flex items-center justify-center shadow-xs">
            <img src="data:image/png;base64,{logo_base64}" alt="Ultracem Cemento & Concreto" class="h-8 w-auto object-contain" />
          </div>

          <!-- Active Advisor Profile Chip in Sidebar -->
          <div class="bg-[#0B1E33] rounded-2xl p-3 border border-slate-700/80 mb-5 flex items-center space-x-3">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-10 h-10 rounded-full border-2 border-[#FDCA02] object-cover" />
              <span class="absolute bottom-0 right-0 w-2.5 h-2.5 rounded-full bg-emerald-400 border border-[#0A233F]"></span>
            </div>
            <div class="overflow-hidden">
              <div class="flex items-center space-x-1.5">
                <span class="font-extrabold text-xs text-white truncate">Carlos Mendoza</span>
                <span class="text-[9px] bg-[#FDCA02] text-[#003E78] font-black px-1.5 py-0.2 rounded-full uppercase">Niv 4</span>
              </div>
              <span class="text-[10px] text-slate-400 block truncate">Asesor Obras • Atlántico</span>
              <span class="text-[10px] text-amber-300 font-bold block mt-0.5">🔥 21 Días de Racha</span>
            </div>
          </div>

          <!-- Navigation Tabs Menu -->
          <nav class="space-y-1.5 text-xs font-semibold">
            <button id="dcrm-tab-btn-racha" onclick="switchDesktopCrmTab('racha')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-all bg-[#FDCA02] text-[#003E78] shadow-xs">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🔥</span>
                <span>Racha & Obras</span>
              </div>
              <span class="bg-[#003E78] text-[#FDCA02] font-black text-[10px] px-2 py-0.5 rounded-full">3</span>
            </button>

            <button id="dcrm-tab-btn-copiloto" onclick="switchDesktopCrmTab('copiloto')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🤖</span>
                <span>Copiloto IA</span>
              </div>
              <span class="text-[9px] bg-blue-900/60 text-blue-200 border border-blue-500/30 px-1.5 py-0.5 rounded-md font-mono-data">Groq/NIM</span>
            </button>

            <button id="dcrm-tab-btn-mapa" onclick="switchDesktopCrmTab('mapa')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🗺️</span>
                <span>Radar & B2B</span>
              </div>
              <span class="text-[9px] bg-amber-900/60 text-amber-300 border border-amber-500/30 px-1.5 py-0.5 rounded-full font-bold">12 B2B</span>
            </button>

            <button id="dcrm-tab-btn-liga" onclick="switchDesktopCrmTab('liga')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🏆</span>
                <span>Liga de Asesores</span>
              </div>
              <span class="text-[10px] text-amber-300 font-bold">#4</span>
            </button>

            <button id="dcrm-tab-btn-perfil" onclick="switchDesktopCrmTab('perfil')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">👤</span>
                <span>Perfil & Cartera</span>
              </div>
              <span class="text-[9px] text-emerald-400 font-bold">1 Casco</span>
            </button>
          </nav>
        </div>

        <!-- Sidebar Footer Status -->
        <div class="pt-4 border-t border-slate-700/80 text-[11px] text-slate-400 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-slate-300 font-bold flex items-center">
              <span class="w-2 h-2 rounded-full bg-[#FDCA02] mr-1.5"></span>
              Planta Galapa
            </span>
            <span class="text-[10px] bg-emerald-950 text-emerald-300 px-1.5 py-0.2 rounded font-bold border border-emerald-500/40">100% OK</span>
          </div>
          <p class="text-[10px] text-slate-400">Molienda: 180 T/h • Hornos: 1,450 °C</p>
        </div>

      </aside>

      <!-- ============================================================ -->
      <!-- WORKSPACE PRINCIPAL (FONDO SÓLIDO #F2F1EC / TARJETAS BLANCAS)-->
      <!-- ============================================================ -->
      <main class="flex-1 p-5 sm:p-7 overflow-y-auto space-y-6">

        <!-- ========================================================== -->
        <!-- TAB 1: RACHA & SEGUIMIENTO COMERCIAL DE OBRAS              -->
        <!-- ========================================================== -->
        <div id="dcrm-content-racha" class="space-y-6">
          
          <!-- Top Executive Banner: Racha + Don Fraguado Mascot -->
          <div class="bg-[#003E78] rounded-2xl p-5 text-white border-2 border-[#FDCA02] shadow-sm flex flex-col lg:flex-row lg:items-center justify-between gap-5">
            <div class="space-y-2">
              <div class="flex flex-wrap items-center gap-2">
                <span class="bg-[#FDCA02] text-[#003E78] font-black text-xs px-2.5 py-0.5 rounded-full uppercase">Racha Activa: 21 Días 🔥</span>
                <span class="text-xs text-blue-200">•</span>
                <span class="text-xs text-amber-200 font-bold flex items-center">
                  ⏰ Corte Antichurn: <span id="desktop-countdown-timer" class="font-mono-data ml-1.5 bg-[#0A233F] text-amber-300 px-2 py-0.5 rounded-lg border border-amber-400/40">13h : 59m : 55s</span>
                </span>
                <span class="text-xs text-blue-200">•</span>
                <span class="text-xs bg-[#0A233F] text-white px-2.5 py-0.5 rounded-full font-bold border border-white/20">🛡️ 1 Casco Disponible</span>
              </div>
              <h2 class="text-2xl font-black tracking-tight text-white">Gestión de Cuentas, Pedidos & Prevención Antichurn</h2>
              <p class="text-xs text-blue-100 max-w-2xl leading-relaxed">
                Atiende o escala tus clientes en semáforo rojo antes de las 11:59 PM para proteger tu racha y sumar +150 XP.
              </p>
            </div>

            <!-- Don Fraguado Interactive Card (Desktop) with Rich Vector SVG Mascot -->
            <div onclick="pokeDesktopMascot()" class="btn-tactile bg-white text-slate-800 rounded-2xl p-3 border-2 border-[#FDCA02] shadow-sm flex items-center space-x-3.5 flex-shrink-0 cursor-pointer max-w-sm hover:border-[#003E78] transition-all" title="¡Haz clic en Don Fraguado para consejos comerciales!">
              <div id="desktop-don-fraguado-container" class="relative w-14 h-16 flex-shrink-0 cursor-pointer select-none mascot-breathing">
                <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm overflow-visible" xmlns="http://www.w3.org/2000/svg">
                  <!-- Drop Shadow under character -->
                  <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />

                  <!-- Mascota: Bulto de Cemento Ultracem -->
                  <g id="desktop-mascot-body-group" class="transition-transform duration-300 origin-bottom">
                    <!-- Sack Tactile Depth -->
                    <path d="M 18,36 L 82,36 Q 88,36 89,45 L 92,94 Q 93,101 84,101 L 16,101 Q 7,101 8,94 L 11,45 Q 12,36 18,36 Z" fill="#94A3B8" />
                    <!-- Sack Front Skin -->
                    <path id="desktop-mascot-body-skin" d="M 18,34 L 82,34 Q 88,34 89,43 L 92,90 Q 93,97 84,97 L 16,97 Q 7,97 8,90 L 11,43 Q 12,34 18,34 Z" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.8" />
                    
                    <!-- Fold lines on sack shoulders -->
                    <path d="M 18,34 Q 28,42 36,34" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round"/>
                    <path d="M 82,34 Q 72,42 64,34" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round"/>

                    <!-- Ultracem Diagonal Brand Ribbon -->
                    <path d="M 10,68 L 90,68 L 91,80 L 9,80 Z" fill="#003E78" />
                    <text x="50" y="77" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-weight="900" font-size="7.5" text-anchor="middle" letter-spacing="1">ULTRACEM</text>
                    
                    <!-- Subtitle badge (50kg NTC 121) -->
                    <rect x="35" y="83" width="30" height="6.5" rx="3" fill="#FDCA02" />
                    <text x="50" y="88" fill="#003E78" font-family="'JetBrains Mono', monospace" font-weight="700" font-size="4.5" text-anchor="middle">50 kg • NTC</text>

                    <!-- Eyes Container -->
                    <g id="desktop-mascot-eyes">
                      <!-- Left Eye -->
                      <ellipse cx="37" cy="52" rx="7.5" ry="9" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.8" />
                      <circle cx="38" cy="52" r="3.8" fill="#0F172A" />
                      <circle cx="40" cy="50" r="1.5" fill="#FFFFFF" />
                      <path d="M 31,41 Q 38,39 44,42" fill="none" stroke="#334155" stroke-width="1.8" stroke-linecap="round" />

                      <!-- Right Eye -->
                      <ellipse cx="63" cy="52" rx="7.5" ry="9" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.8" />
                      <circle cx="62" cy="52" r="3.8" fill="#0F172A" />
                      <circle cx="64" cy="50" r="1.5" fill="#FFFFFF" />
                      <path d="M 69,41 Q 62,39 56,42" fill="none" stroke="#334155" stroke-width="1.8" stroke-linecap="round" />

                      <!-- Cheeks Blush -->
                      <circle cx="28" cy="58" r="3" fill="#F43F5E" opacity="0.35" />
                      <circle cx="72" cy="58" r="3" fill="#F43F5E" opacity="0.35" />

                      <!-- Smile -->
                      <path d="M 44,61 Q 50,66 56,61" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" />
                    </g>

                    <!-- Casco Amarillo de Seguridad (Hard Hat) with 3D Depth -->
                    <g id="desktop-mascot-hardhat">
                      <path d="M 14,33 Q 50,38 86,33 Q 50,42 14,33 Z" fill="#92400E" opacity="0.7" />
                      <path d="M 20,31 C 20,14 32,8 50,8 C 68,8 80,14 80,31 Z" fill="#FDCA02" />
                      <path d="M 46,8 L 54,8 L 54,30 L 46,30 Z" fill="#FBBF24" />
                      <path d="M 28,24 C 28,16 35,12 45,11" fill="none" stroke="#FEF3C7" stroke-width="2.5" stroke-linecap="round" opacity="0.8" />
                      <path d="M 12,30 C 22,27 78,27 88,30 C 90,32 86,34 82,34 C 54,36 46,36 18,34 C 14,34 10,32 12,30 Z" fill="#D97706" />
                      <circle cx="50" cy="20" r="4.5" fill="#003E78" stroke="#FFFFFF" stroke-width="1" />
                      <path d="M 48,19 L 52,19 L 50,23 Z" fill="#FFFFFF" />
                    </g>
                  </g>
                </svg>
              </div>
              <div class="text-xs">
                <div class="flex items-center space-x-1.5">
                  <span class="font-black text-[#003E78]">Don Fraguado</span>
                  <span id="desktop-fraguado-badge" class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full">Motivado</span>
                </div>
                <p id="desktop-fraguado-dialogue" class="text-[11px] text-slate-600 mt-0.5 leading-snug">
                  "¡Buenos días Carlos! Tu racha está protegida. Toca aquí para consejos de venta."
                </p>
              </div>
            </div>
          </div>

          <!-- Split 2-Column Desktop CRM Layout -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
            
            <!-- Columna Izquierda (7 cols): Cartera de Clientes -->
            <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-4">
              
              <!-- Filter chips -->
              <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                <div class="flex flex-wrap items-center gap-1.5 text-xs">
                  <button onclick="filtrarClientesDesktop('todos')" id="dfilter-todos" class="px-3 py-1 rounded-lg font-bold bg-[#003E78] text-white">Todos (3)</button>
                  <button onclick="filtrarClientesDesktop('obras')" id="dfilter-obras" class="px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200">🏗️ Obras (2)</button>
                  <button onclick="filtrarClientesDesktop('ferreterias')" id="dfilter-ferreterias" class="px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200">🏪 Ferreterías (1)</button>
                  <button onclick="filtrarClientesDesktop('rojos')" id="dfilter-rojos" class="px-3 py-1 rounded-lg font-semibold text-rose-700 bg-rose-50 border border-rose-200">🔴 En Riesgo (1)</button>
                </div>
                <span class="text-xs text-slate-400 font-medium">3 Casos Asignados</span>
              </div>

              <!-- List of Client Cards -->
              <div class="space-y-3.5">
                
                <!-- Client 1: Constructora Bolívar -->
                <div id="dcard-client-1" onclick="seleccionarClienteDesktop(1)" class="p-4 rounded-xl border-2 border-rose-300 bg-rose-50/20 hover:bg-rose-50/40 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Constructora Bolívar</h3>
                        <span class="text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full">Obra Mayor 4G</span>
                      </div>
                      <span class="text-xs text-slate-500">Torres del Mar • 120 Ton Cemento Estructural Max</span>
                    </div>
                    <span class="bg-[#DC2626] text-white font-black text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">🔴 8D Sin Pedido</span>
                  </div>

                  <div class="bg-white p-2.5 rounded-lg border border-rose-200 text-xs text-rose-800 space-y-1">
                    <p class="font-bold">⚠️ Riesgo Crítico de Pérdida:</p>
                    <p class="text-[11px] text-slate-600">Superó su ciclo habitual de reposición por 3 días. Contacta hoy para salvar tu racha comercial (+100 XP).</p>
                  </div>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $38.2 M COP</span>
                    <div class="space-x-1.5 text-xs">
                      <button onclick="event.stopPropagation(); contactarClienteWhatsApp('Constructora Bolívar')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg">WhatsApp (+50 XP)</button>
                      <button onclick="event.stopPropagation(); seleccionarClienteDesktop(1)" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-3 py-1 rounded-lg">Gestionar Caso ➔</button>
                    </div>
                  </div>
                </div>

                <!-- Client 2: Ferretería El Constructor -->
                <div id="dcard-client-2" onclick="seleccionarClienteDesktop(2)" class="p-4 rounded-xl border border-amber-300 bg-amber-50/20 hover:bg-amber-50/40 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Ferretería El Constructor</h3>
                        <span class="text-[10px] bg-teal-100 text-teal-800 font-bold px-2 py-0.5 rounded-full">Ferretería</span>
                      </div>
                      <span class="text-xs text-slate-500">Sede Centro Soledad • 45 Ton Cemento Uso General</span>
                    </div>
                    <span class="bg-[#FDCA02] text-[#003E78] font-black text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">🟡 4D Sin Pedido</span>
                  </div>

                  <p class="text-xs text-slate-600">Alerta de fraguado: Requiere reposición de bultos antes del fin de semana.</p>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $14.2 M COP</span>
                    <div class="space-x-1.5 text-xs">
                      <button onclick="event.stopPropagation(); contactarClienteWhatsApp('Ferretería El Constructor')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg">WhatsApp</button>
                      <button onclick="event.stopPropagation(); seleccionarClienteDesktop(2)" class="btn-tactile bg-slate-800 hover:bg-slate-900 text-white font-bold px-3 py-1 rounded-lg">Gestionar Caso ➔</button>
                    </div>
                  </div>
                </div>

                <!-- Client 3: Marval Altos de Riomar -->
                <div id="dcard-client-3" onclick="seleccionarClienteDesktop(3)" class="p-4 rounded-xl border border-slate-200 bg-slate-50/40 hover:bg-slate-50 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Marval — Altos de Riomar</h3>
                        <span class="text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full">Industrial</span>
                      </div>
                      <span class="text-xs text-slate-500">Torre 3 • 210 Ton Cemento Marino Impermeable</span>
                    </div>
                    <span class="bg-emerald-100 text-emerald-800 font-bold text-[10px] px-2.5 py-0.5 rounded-full uppercase">🟢 Al Día (Placa Fundida)</span>
                  </div>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $65.8 M COP</span>
                    <button onclick="event.stopPropagation(); seleccionarClienteDesktop(3)" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-3 py-1 rounded-lg text-xs">Ver Bitácora ➔</button>
                  </div>
                </div>

              </div>

            </div>

            <!-- Columna Derecha (5 cols): Consola de Acción en Vivo -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-5">
              
              <div class="border-b border-slate-100 pb-3 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Consola de Acción</span>
                  <h3 id="dconsole-client-name" class="font-black text-base text-slate-900">Constructora Bolívar</h3>
                </div>
                <span class="text-[10px] font-bold bg-rose-100 text-rose-800 px-2 py-0.5 rounded-full">🔴 Prioridad Alta</span>
              </div>

              <!-- Audio Recording Console (Same as Mobile) -->
              <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3">
                <div class="flex items-center justify-between text-xs">
                  <span class="font-bold text-slate-800 flex items-center">
                    <span class="text-base mr-1.5">🎙️</span>
                    Nota de Voz de la Visita
                  </span>
                  <span id="daudio-status-badge" class="text-[10px] bg-slate-200 text-slate-600 px-2 py-0.5 rounded-full font-mono-data">Listo</span>
                </div>

                <div class="flex items-center space-x-2">
                  <button id="dbtn-record-audio" onclick="toggleDesktopAudioRecording()" class="btn-tactile flex-1 bg-[#D9531E] hover:bg-[#c24615] text-white font-bold py-2 px-3 rounded-xl text-xs flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>🔴</span>
                    <span id="dbtn-record-text">Grabar Nota de Audio</span>
                  </button>
                </div>

                <!-- Audio Playback Container -->
                <div id="daudio-player-container" class="space-y-2 pt-1">
                  <audio id="daudio-player" controls class="w-full h-8"></audio>
                  <p id="daudio-transcript-text" class="text-[11px] text-slate-600 italic bg-white p-2 rounded-lg border border-slate-200">
                    "Minuta: El ingeniero de Constructora Bolívar confirma necesidad de 40 Ton de Cemento Estructural Max para el vaciado del miércoles..."
                  </p>
                </div>
              </div>

              <!-- Internal Department Escalation Module (Saves Streak in 1 Click) -->
              <div class="bg-[#0A233F] text-white p-4 rounded-xl space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold uppercase tracking-wider text-[#FDCA02]">Escalamiento a Departamento</span>
                  <span class="text-[10px] bg-emerald-500 text-white font-bold px-2 py-0.5 rounded-full">Salva Racha</span>
                </div>
                <h4 class="font-bold text-xs text-white">¿Bloqueo administrativo? Transfiere el caso:</h4>
                
                <select id="descalation-dept-select" class="w-full bg-[#0B1E33] text-white border border-slate-600 rounded-lg p-2 text-xs font-semibold focus:outline-none">
                  <option value="cartera">💰 Cartera & Crédito (SLA: 4 horas) — Cupo excedido</option>
                  <option value="logistica">🚚 Logística & Mixers (SLA: 2 horas) — Tractomula en ruta</option>
                  <option value="calidad">🔬 Calidad NTC 121 (SLA: 6 horas) — Certificado de rotura</option>
                  <option value="pricing">🏷️ Dirección Comercial (SLA: 4 horas) — Descuento por volumen</option>
                </select>

                <button onclick="escalarCasoDesktop()" class="w-full btn-tactile bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] font-black py-2.5 px-3 rounded-xl text-xs flex items-center justify-center space-x-1.5 shadow-md">
                  <span>⚡</span>
                  <span>Escalar Caso y Proteger Mi Racha</span>
                </button>
              </div>

              <!-- Client Transfer to Colleague -->
              <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                <span class="text-slate-500">¿Reasignar zona?</span>
                <button onclick="openTransferClientModal(1, 'Constructora Bolívar')" class="text-[#003E78] font-bold hover:underline">
                  Transferir cliente a un compañero ➔
                </button>
              </div>

            </div>

          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 2: COPILOTO IA MULTIMODELO (GROQ / NVIDIA / DEEPSEEK)  -->
        <!-- ========================================================== -->
        <div id="dcrm-content-copiloto" class="hidden space-y-5">
          
          <!-- Copilot Header Bar -->
          <div class="bg-[#003E78] text-white rounded-2xl p-5 border-2 border-[#FDCA02] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xl">🤖</span>
                <h2 class="text-xl font-black">Copiloto IA Multimodelo Ultracem</h2>
              </div>
              <p class="text-xs text-blue-100 mt-0.5">Asistente técnico comercial con guardrails certificados de la norma NTC 121</p>
            </div>

            <!-- Provider & Setup Action -->
            <div class="flex items-center space-x-2">
              <select id="dcopilot-provider-select" onchange="cambiarProveedorSeleccionado(this.value)" class="bg-[#0A233F] text-white border border-slate-600 rounded-xl px-3 py-1.5 text-xs font-bold cursor-pointer">
                <option value="groq">Groq Cloud (LPU 500-1000 t/s)</option>
                <option value="nvidia">NVIDIA NIM (Llama 3.1 70B)</option>
                <option value="deepseek">DeepSeek (V3 / R1)</option>
                <option value="openai">OpenAI (GPT-4o)</option>
              </select>
              <button onclick="openInPhoneAISettings()" class="btn-tactile bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] font-black px-3.5 py-1.5 rounded-xl text-xs flex items-center space-x-1 shadow-xs">
                <span>⚙️</span>
                <span>Configurar API Key</span>
              </button>
            </div>
          </div>

          <!-- Quick Prompts Chips -->
          <div class="flex flex-wrap items-center gap-2 text-xs">
            <span class="text-slate-400 font-bold uppercase text-[10px] mr-1">Preguntas Frecuentes:</span>
            <button onclick="probarPromptRapidoDesktop('¿Cuál es la dosificación exacta para una losa de 3000 PSI con Cemento Estructural Max NTC 121?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              📐 Dosificación 3000 PSI NTC 121
            </button>
            <button onclick="probarPromptRapidoDesktop('Argos ofreció $500 menos por bulto en Soledad. ¿Qué argumentos técnicos doy para defender nuestro Cemento Uso General?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              ⚔️ Defensa Comercial vs Argos
            </button>
            <button onclick="probarPromptRapidoDesktop('¿Por qué el Cemento Marino Ultracem es superior para obras portuarias en el Caribe?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              🌊 Cemento Marino vs Sulfatos
            </button>
            <button onclick="probarPromptRapidoDesktop('¿Qué es el ácido ribonucleico?')" class="bg-white hover:bg-rose-50 text-rose-700 border border-rose-200 px-3 py-1 rounded-lg font-semibold shadow-xs" title="Prueba los guardrails estrictos de Ultracem">
              🛡️ Probar Guardrails (Pregunta No Comercial)
            </button>
          </div>

          <!-- Desktop Chat Window -->
          <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col h-[520px] overflow-hidden">
            
            <!-- Chat Messages Feed -->
            <div id="desktop-chat-messages" class="flex-1 overflow-y-auto p-5 space-y-4 text-xs">
              
              <!-- AI Welcome -->
              <div class="flex items-start space-x-3">
                <div class="w-8 h-8 rounded-full bg-[#003E78] text-[#FDCA02] font-black flex items-center justify-center text-xs flex-shrink-0">
                  U
                </div>
                <div class="bg-slate-100 rounded-2xl p-3.5 max-w-2xl text-slate-800 leading-relaxed space-y-1">
                  <div class="font-bold text-[#003E78]">Copiloto Comercial Ultracem</div>
                  <p>¡Hola Carlos! Estoy listo para apoyarte en campo. Puedo calcular dosificaciones de concreto, redactar cotizaciones técnicas según la norma <strong>NTC 121</strong> o preparar argumentos de venta frente a la competencia.</p>
                  <span class="text-[10px] text-slate-400 block pt-1">Motor: Groq Cloud LPU (openai/gpt-oss-120b)</span>
                </div>
              </div>

            </div>

            <!-- Chat Input Bar -->
            <div class="p-3.5 bg-slate-50 border-t border-slate-200 flex items-center space-x-2">
              <input id="desktop-chat-input" type="text" placeholder="Escribe tu consulta sobre cemento, dosificaciones o clientes..." onkeydown="if(event.key==='Enter') enviarConsultaAIDesktop()" class="flex-1 bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs text-slate-800 focus:outline-none focus:border-[#003E78]" />
              <button onclick="enviarConsultaAIDesktop()" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-5 py-2.5 rounded-xl text-xs shadow-xs flex items-center space-x-1">
                <span>Enviar</span>
                <span>➔</span>
              </button>
            </div>

          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 3: RADAR GEORREFERENCIADO & DIRECTORIO B2B            -->
        <!-- ========================================================== -->
        <div id="dcrm-content-mapa" class="hidden space-y-5">
          
          <!-- Top Sub-view Selector -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-3.5 rounded-2xl border border-slate-200/90 shadow-xs">
            <div class="flex items-center space-x-2 text-xs">
              <button onclick="switchDesktopMapSubView('mapa')" id="dmap-sub-btn-map" class="px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs">
                🗺️ Mapa Interactivo de Colombia
              </button>
              <button onclick="switchDesktopMapSubView('prospectos')" id="dmap-sub-btn-prospects" class="px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100">
                🏢 Directorio B2B (12 Empresas Caribe)
              </button>
            </div>

            <div class="flex items-center space-x-2 text-xs">
              <button onclick="toggleDesktopMapSatellite()" class="bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold px-3 py-1.5 rounded-lg shadow-xs">
                🛰️ Capa Satelital ESRI
              </button>
              <span class="text-xs text-slate-400">Planta Galapa • Km 8 Vía Tubará</span>
            </div>
          </div>

          <!-- Subview 1: Full Desktop Map -->
          <div id="dmap-view-container" class="bg-white rounded-2xl border border-slate-200/90 shadow-xs p-3 space-y-3">
            <div id="desktop-colombia-map" class="w-full h-[540px] rounded-xl overflow-hidden border border-slate-200 z-10"></div>
          </div>

          <!-- Subview 2: B2B Caribbean Directory -->
          <div id="dprospects-view-container" class="hidden bg-white rounded-2xl border border-slate-200/90 shadow-xs p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
              <div>
                <h3 class="font-black text-base text-slate-900">Directorio de Empresas & Obras para Conquistar</h3>
                <p class="text-xs text-slate-500">12 prospectos estratégicos del Caribe actualmente atendidos por la competencia</p>
              </div>
              <span class="text-xs bg-[#FDCA02] text-[#003E78] font-black px-3 py-1 rounded-full">+50 XP por Primer Contacto</span>
            </div>

            <!-- Prospects Table -->
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                  <tr>
                    <th class="py-3 px-4">Empresa / Proyecto</th>
                    <th class="py-3 px-3">Ubicación</th>
                    <th class="py-3 px-3">Volumen Estimado</th>
                    <th class="py-3 px-3">Proveedor Actual</th>
                    <th class="py-3 px-3">Gancho Ultracem</th>
                    <th class="py-3 px-4 text-right">Acción Comercial</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 font-mono-data text-[11px]">
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Constructora Amarilo — Parque Heredia</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Cartagena, BOL</td>
                    <td class="py-3 px-3 font-bold text-slate-800">450 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded">Argos</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Despacho garantizado en mixer antes de 2h</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(301)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Bloquera del Sinú S.A.S.</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Montería, COR</td>
                    <td class="py-3 px-3 font-bold text-slate-800">280 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-orange-100 text-orange-800 font-bold px-2 py-0.5 rounded">Cemex</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Resistencia temprana a 3 días con Estructural Max</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(302)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Consorcio Vial Puerta de Oro</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Barranquilla, ATL</td>
                    <td class="py-3 px-3 font-bold text-slate-800">620 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded">Argos</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Flete bonificado desde Planta Galapa</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(303)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 4: LIGA DE ASESORES COMERCIAL                         -->
        <!-- ========================================================== -->
        <div id="dcrm-content-liga" class="hidden space-y-6">
          
          <!-- Top Podium: Amarillo, Azul Oscuro y Blanco -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
            
            <!-- 1st Place: Milena Ospino -->
            <div class="bg-white rounded-3xl p-5 border-4 border-[#FDCA02] shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-[#FDCA02] text-[#003E78] font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥇 1° Líder Regional
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#003E78] text-[#FDCA02] font-black text-base flex items-center justify-center">MO</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Milena Ospino</h3>
                  <span class="text-xs text-slate-500 block">Costa Norte • Concretos Especiales</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-[#003E78] text-base font-mono-data">28 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-[#003E78] text-base font-mono-data">940 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📧 mospino@ultracem.co • 100% SLA cumplido</p>
              </div>
            </div>

            <!-- 2nd Place: Adriana Anaya -->
            <div class="bg-white rounded-3xl p-5 border-2 border-slate-300 shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-slate-200 text-slate-800 font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥈 2° Puesto
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#0A233F] text-white font-black text-base flex items-center justify-center">AA</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Adriana Anaya</h3>
                  <span class="text-xs text-slate-500 block">Ferreterías • Bolívar / Atlántico</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">24 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">820 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📧 aanaya@ultracem.co • 98% SLA cumplido</p>
              </div>
            </div>

            <!-- 3rd Place: Hichel Espitia -->
            <div class="bg-white rounded-3xl p-5 border-2 border-amber-300 shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-amber-100 text-amber-900 font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥉 3° Puesto
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#003E78] text-white font-black text-base flex items-center justify-center">HE</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Hichel Espitia</h3>
                  <span class="text-xs text-slate-500 block">Infraestructura & Obra 4G</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">21 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">1,150 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📱 310 250 3454 • 96% SLA cumplido</p>
              </div>
            </div>

          </div>

          <!-- Asesor Actual (Carlos Mendoza) Status Card -->
          <div class="bg-[#003E78] text-white rounded-2xl p-5 border-2 border-[#FDCA02] shadow-xs flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-[#FDCA02] text-[#003E78] font-black text-sm flex items-center justify-center">
                4°
              </div>
              <div>
                <h4 class="font-black text-sm">Tu Posición: Carlos Mendoza (4° Puesto)</h4>
                <p class="text-xs text-blue-200">21 Días de Racha acumulada • 680 Ton despachadas • Estás a solo 140 Ton del podio</p>
              </div>
            </div>
            <span class="bg-[#FDCA02] text-[#003E78] font-black text-xs px-3 py-1 rounded-xl">Zona Caribe</span>
          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 5: PERFIL & GESTIÓN DE CARTERA                        -->
        <!-- ========================================================== -->
        <div id="dcrm-content-perfil" class="hidden space-y-6">
          
          <div class="bg-white rounded-3xl p-6 border border-slate-200/90 shadow-xs space-y-6">
            
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-5">
              <div class="flex items-center space-x-4">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=140&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-16 h-16 rounded-full border-4 border-[#FDCA02] object-cover" />
                <div>
                  <h3 class="text-xl font-black text-slate-900">Carlos Mendoza</h3>
                  <p class="text-xs text-slate-500 font-medium">Asesor Comercial Senior • Ultracem S.A.S. (Costa Norte)</p>
                  <span class="inline-block text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full mt-1">Caribe: Obras & Constructoras</span>
                </div>
              </div>

              <!-- Casco inventory -->
              <div class="bg-[#0A233F] text-white p-3.5 rounded-2xl border border-slate-700 text-center">
                <span class="text-[10px] text-[#FDCA02] uppercase font-bold block">Inventario de Seguridad</span>
                <span class="text-xl font-black font-mono-data">1 Casco Activo 🛡️</span>
                <span class="text-[10px] text-slate-300 block">Congelación 24h ante emergencias</span>
              </div>
            </div>

            <!-- Heatmap 30 days grid -->
            <div class="space-y-2">
              <h4 class="font-bold text-xs text-slate-800">Registro de Cumplimiento de Visitas (Últimos 30 Días)</h4>
              <div class="grid grid-cols-10 gap-1.5 p-3 bg-slate-50 rounded-xl border border-slate-200">
                <div class="h-6 rounded bg-[#003E78]" title="Día 1: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 2: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 3: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 4: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 5: 100%"></div>
                <div class="h-6 rounded bg-slate-200" title="Día 6: Domingo"></div>
                <div class="h-6 rounded bg-slate-200" title="Día 7: Domingo"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 8: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 9: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 10: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 11: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 12: 100%"></div>
                <div class="h-6 rounded bg-[#FDCA02]" title="Día 13: Casco utilizado"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 14: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 15: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 16: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 17: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 18: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 19: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 20: 100%"></div>
                <div class="h-6 rounded bg-[#FDCA02] border border-[#003E78]" title="Día 21: Hoy en progreso"></div>
              </div>
            </div>

            <!-- Transfer module -->
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <h4 class="font-bold text-xs text-slate-900">Transferencia Voluntaria de Clientes</h4>
                <p class="text-xs text-slate-500">¿Saldrás a vacaciones o requieres apoyo en una zona? Transfiere una cuenta a Milena, Adriana o Hichel.</p>
              </div>
              <button onclick="openTransferClientModal(1, 'Constructora Bolívar')" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-4 py-2 rounded-xl text-xs whitespace-nowrap shadow-xs">
                Transferir un Cliente
              </button>
            </div>

          </div>

        </div>

      </main>

    </div>
'''
