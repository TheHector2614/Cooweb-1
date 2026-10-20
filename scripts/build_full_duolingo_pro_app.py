import os

base64_logo_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\assets\logo_base64.txt"
with open(base64_logo_path, "r", encoding="utf-8") as f:
    logo_base64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="es" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UltraRacha — CRM Gamificado & Copiloto Comercial Ultracem</title>
  
  <!-- Tailwind CSS via allowlisted CDN -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  
  <!-- Typography: Outfit (Neo-geometric) + JetBrains Mono (Data & Precision) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --brand-blue: #004797;
      --brand-blue-hover: #003672;
      --brand-blue-light: #EFF6FF;
      --brand-amber: #EA580C;
      --brand-amber-light: #FFF7ED;
      --brand-emerald: #059669;
      --brand-emerald-light: #ECFDF5;
      --brand-rose: #E11D48;
      --brand-rose-light: #FFF1F2;
      --surface-slate: #F8FAFC;
    }}
    
    body {{
      font-family: 'Outfit', system-ui, -apple-system, sans-serif;
      background-color: var(--surface-slate);
      color: #0F172A;
    }}
    
    .font-mono-data {{
      font-family: 'JetBrains Mono', monospace;
      font-variant-numeric: tabular-nums;
    }}
    
    .text-balance {{
      text-wrap: balance;
    }}
    
    /* Duolingo Pro Animations */
    @keyframes pulse-flame {{
      0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 4px rgba(234, 88, 12, 0.4)); }}
      50% {{ transform: scale(1.14) rotate(4deg); filter: drop-shadow(0 0 12px rgba(234, 88, 12, 0.8)); }}
    }}
    .flame-active {{
      display: inline-flex;
      animation: pulse-flame 1.5s infinite ease-in-out;
      transform-origin: bottom center;
    }}
    
    @keyframes bob-mascot {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-5px); }}
    }}
    .mascot-bob {{
      animation: bob-mascot 2.5s infinite ease-in-out;
    }}

    @keyframes radar-ping {{
      0% {{ transform: scale(0.9); opacity: 1; }}
      100% {{ transform: scale(2.2); opacity: 0; }}
    }}
    .radar-pulse {{
      animation: radar-ping 1.8s infinite cubic-bezier(0, 0, 0.2, 1);
    }}

    @keyframes freeze-shimmer {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}
    .freeze-glow {{
      background: linear-gradient(135deg, #0ea5e9, #38bdf8, #bae6fd, #38bdf8);
      background-size: 200% 200%;
      animation: freeze-shimmer 3s ease infinite;
    }}

    .btn-tactile {{
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-tactile:active {{
      transform: scale(0.97) translateY(1px);
    }}

    @media (prefers-reduced-motion: reduce) {{
      *, ::before, ::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-900 antialiased min-h-screen flex flex-col selection:bg-blue-100 selection:text-blue-900">

  <!-- ACCESSIBILITY: SKIP LINK -->
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-[#004797] focus:text-white focus:rounded-xl text-xs font-bold">
    Saltar al contenido principal
  </a>

  <!-- ============================================================== -->
  <!-- TOP APP BAR                                                    -->
  <!-- ============================================================== -->
  <header class="bg-white border-b border-slate-200/80 sticky top-0 z-40 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Name -->
      <div class="flex items-center space-x-3.5">
        <img src="data:image/png;base64,{logo_base64}" alt="Logotipo Oficial Ultracem" class="h-7 w-auto object-contain" width="115" height="28">
        <div class="h-4 w-px bg-slate-200" aria-hidden="true"></div>
        <div class="flex items-center space-x-2">
          <span class="font-extrabold text-slate-900 tracking-tight text-lg">Ultra<span class="text-[#004797]">Racha</span></span>
          <span class="text-[10px] font-bold text-orange-700 bg-orange-50 border border-orange-200 px-2 py-0.5 rounded-full uppercase tracking-wider">Duolingo B2B</span>
        </div>
      </div>

      <!-- Controls: View Switcher & Day/Night Mode -->
      <div class="flex items-center space-x-3">
        
        <!-- View Toggle (Asesor vs Supervisor) -->
        <nav aria-label="Selector de Vistas" class="bg-slate-100 p-1 rounded-xl flex items-center border border-slate-200/70">
          <button id="btn-view-mobile" onclick="switchView('mobile')" aria-label="Cambiar a Vista Asesor Móvil" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs">
            <span>📱</span>
            <span>Asesor Móvil</span>
          </button>
          <button id="btn-view-web" onclick="switchView('web')" aria-label="Cambiar a Dashboard Supervisor" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>💻</span>
            <span>Supervisor Web</span>
          </button>
        </nav>

        <!-- Time Mode Simulation Pill -->
        <div class="hidden sm:flex items-center space-x-1 text-xs border border-slate-200 rounded-xl p-1 bg-white">
          <button id="btn-time-day" onclick="setTimeMode('day')" aria-label="Simular 10:00 AM" class="px-2.5 py-1 rounded-lg font-bold bg-slate-900 text-white text-[11px] transition-all">
            ☀️ 10:00 AM
          </button>
          <button id="btn-time-night" onclick="setTimeMode('night')" aria-label="Simular 10:45 PM" class="px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all">
            🌙 10:45 PM
          </button>
        </div>

      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- MAIN APP CONTAINER                                             -->
  <!-- ============================================================== -->
  <main id="main-content" class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 flex flex-col justify-center">

    <!-- ============================================================== -->
    <!-- 1. VISTA ASESOR MÓVIL (FRAME NATIVO COMPLETO)                  -->
    <!-- ============================================================== -->
    <div id="view-mobile" class="w-full flex justify-center items-start">
      
      <!-- Phone Canvas Frame -->
      <div class="w-full max-w-[420px] bg-white rounded-[36px] shadow-2xl border border-slate-300/80 overflow-hidden flex flex-col min-h-[850px] relative">
        
        <!-- Phone Status Notch -->
        <div class="bg-slate-900 pt-3.5 px-6 pb-2 flex justify-between items-center text-white text-[11px] font-mono-data">
          <span id="phone-clock" class="font-bold text-slate-200">10:00 AM</span>
          <div class="w-18 h-3.5 bg-slate-800 rounded-full"></div>
          <div class="flex items-center space-x-1.5 text-slate-300">
            <span>5G</span>
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          </div>
        </div>

        <!-- Dynamic Screen Content Container -->
        <div id="mobile-screen-content" class="flex-1 flex flex-col overflow-hidden">
          
          <!-- ========================================== -->
          <!-- PANTALLA 1: BANDEJA DE RACHA (CLIENTES)    -->
          <!-- ========================================== -->
          <div id="screen-racha" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Mobile Header Bar: Streak, Casco & Countdowns -->
            <div class="bg-gradient-to-r from-[#0033A0] to-[#004797] text-white p-4.5 relative overflow-hidden">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-3">
                  <div class="relative cursor-pointer" onclick="navigateToTab('perfil')" title="Ir a mi perfil">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-12 h-12 rounded-full border-2 border-white object-cover shadow-sm">
                    <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-[#0033A0]"></span>
                  </div>
                  <div>
                    <div class="flex items-center space-x-1.5">
                      <h2 class="font-bold text-sm tracking-tight">Carlos Mendoza</h2>
                      <span class="text-[9px] bg-white/20 px-1.5 py-0.5 rounded-full font-bold uppercase">Nivel 4</span>
                    </div>
                    <p class="text-[11px] text-blue-200">Regional Caribe • Obras</p>
                  </div>
                </div>

                <!-- Streak Counter Pill -->
                <div class="bg-white/10 backdrop-blur-xs border border-white/25 rounded-2xl px-3.5 py-1.5 flex items-center space-x-2">
                  <span class="flame-active text-xl">🔥</span>
                  <div class="text-right">
                    <span id="streak-days" class="text-xl font-black text-amber-300 leading-none font-mono-data">21</span>
                    <span class="text-[9px] text-white/90 block font-bold uppercase tracking-wider">Días</span>
                  </div>
                </div>
              </div>

              <!-- Cutoff Clock & Shield Status -->
              <div class="mt-3.5 pt-2.5 border-t border-white/15 flex items-center justify-between text-xs">
                <div class="flex items-center space-x-1.5 text-blue-100">
                  <span>⏱️</span>
                  <span class="font-medium text-[11px]">Corte 11:59&nbsp;PM:</span>
                  <span id="countdown-timer" class="font-mono-data font-bold text-amber-300 bg-black/30 px-2 py-0.5 rounded text-[11px]">13h : 59m : 12s</span>
                </div>
                
                <button onclick="navigateToTab('perfil')" class="flex items-center space-x-1 bg-amber-400/20 text-amber-200 border border-amber-300/40 px-2.5 py-0.5 rounded-full text-[11px] font-bold hover:bg-amber-400/30 transition-all" title="Ver inventario de cascos">
                  <span>⛑️</span>
                  <span id="header-casco-count">1 Casco</span>
                </button>
              </div>
            </div>

            <!-- Mascota "Don Fraguado" (4 Estados Reactivos) -->
            <div id="mascot-card" class="m-3 p-3.5 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all">
              
              <!-- Character Avatar with Expression States -->
              <div id="mascot-avatar" class="mascot-bob relative flex-shrink-0 w-13 h-14 bg-gradient-to-br from-slate-100 to-slate-200 rounded-xl border border-slate-300 flex flex-col items-center justify-center shadow-xs">
                <!-- Helmet with Ultracem Monogram -->
                <div id="mascot-helmet" class="absolute -top-2.5 w-10 h-4 bg-white rounded-t-full border border-slate-300 shadow-xs flex items-center justify-center">
                  <span class="text-[6.5px] font-extrabold text-[#004797]">ULTRACEM</span>
                </div>
                <!-- Goggles -->
                <div id="mascot-goggles" class="w-8 h-2.5 bg-cyan-600 rounded-full border border-cyan-800 flex items-center justify-around px-0.5 mt-1">
                  <span class="w-1.5 h-1.5 bg-white rounded-full"></span>
                  <span class="w-1.5 h-1.5 bg-white rounded-full"></span>
                </div>
                <!-- Expression / Mustache -->
                <div id="mascot-face" class="text-[10px] leading-none mt-0.5">🧔‍♂️</div>
                <!-- Sack Badge -->
                <span class="text-[7.5px] font-extrabold text-[#004797] tracking-tight mt-0.5">50kg</span>
              </div>

              <!-- Speech Bubble -->
              <div class="flex-1 min-w-0">
                <div class="flex justify-between items-center">
                  <strong class="text-xs font-bold text-slate-900">Don Fraguado</strong>
                  <span id="mascot-badge" class="text-[10px] font-bold px-2 py-0.2 rounded-full bg-blue-100 text-[#004797]">En marcha</span>
                </div>
                <p id="mascot-speech" class="text-xs text-slate-700 mt-0.5 leading-snug font-medium">
                  “Tienes <strong>2 cuentas en Riesgo Crítico</strong> hoy. ¡Gestiona en 1 toque o escala antes de las 11:59&nbsp;PM para no perder tu racha!”
                </p>
              </div>
            </div>

            <!-- Toneladas Progress Strip -->
            <div class="px-4 py-1.5 bg-white">
              <div class="flex justify-between items-center text-xs mb-1">
                <span class="text-slate-500 font-medium">Meta del Mes (Toneladas)</span>
                <span class="font-mono-data font-bold text-slate-900">420 <span class="text-slate-400 font-normal">/ 500 Ton (84%)</span></span>
              </div>
              <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                <div class="bg-[#004797] h-full rounded-full transition-all duration-500" style="width: 84%"></div>
              </div>
            </div>

            <!-- Channel Filter Tabs -->
            <div class="px-4 pt-2 pb-1 flex items-center justify-between text-xs">
              <div class="flex space-x-1" role="tablist">
                <button onclick="filterClients('all')" id="tab-all" class="px-3 py-1 font-bold rounded-lg bg-[#004797] text-white text-[11px] transition-all">Todos (4)</button>
                <button onclick="filterClients('industrial')" id="tab-industrial" class="px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 text-[11px] transition-all">🏢 Obras</button>
                <button onclick="filterClients('tradicional')" id="tab-tradicional" class="px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 text-[11px] transition-all">🏪 Ferreterías</button>
              </div>
              <span class="text-[11px] text-slate-400 font-mono-data">Prioridad Riesgo</span>
            </div>

            <!-- Client Cards List -->
            <div class="flex-1 overflow-y-auto p-3.5 space-y-3 bg-slate-50/70">

              <!-- CLIENT 1: Constructora Bolívar -->
              <article id="card-client-1" class="bg-white rounded-2xl p-4 border-2 border-rose-300 shadow-xs client-card transition-all" data-channel="industrial" data-status="danger">
                <div class="flex justify-between items-start gap-2">
                  <div class="min-w-0">
                    <div class="flex items-center space-x-2">
                      <span class="text-[10px] font-bold text-slate-500 uppercase tracking-wider bg-slate-100 px-2 py-0.5 rounded">🏢 Industrial</span>
                      <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-600 animate-pulse"></span>
                        <span>🔴 8 DÍAS SIN CONTACTO</span>
                      </span>
                    </div>
                    <h3 class="font-extrabold text-slate-900 text-sm mt-1.5 truncate">Constructora Bolívar — Torre del Mar</h3>
                    <p class="text-xs text-slate-500">Ing. Andrés Meza • 120&nbsp;Ton Cemento Estructural</p>
                  </div>
                  <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200">$54M</span>
                </div>

                <!-- Warning Box -->
                <div class="mt-2.5 p-2.5 bg-rose-50 rounded-xl border border-rose-200/80 flex items-start space-x-2 text-xs text-rose-900">
                  <span class="text-sm">⚠️</span>
                  <div class="leading-tight">
                    <strong class="font-bold block">Cotización vence hoy a las 5:00&nbsp;PM</strong>
                    <span>Requieren confirmación de pruebas NTC 121 antes de autorizar despacho.</span>
                  </div>
                </div>

                <!-- Interactive Features: Timeline Toggle, GPS Check-in & WhatsApp -->
                <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                  <button onclick="toggleTimeline(1)" class="text-[#004797] font-bold hover:underline flex items-center space-x-1">
                    <span id="timeline-chevron-1">▼</span>
                    <span>Ver Historial de Gestiones</span>
                  </button>

                  <div class="flex items-center space-x-1.5">
                    <!-- GPS Check-in button -->
                    <button onclick="realizarCheckinGPS(1, 'Constructora Bolívar')" class="btn-tactile bg-blue-50 hover:bg-blue-100 text-[#004797] border border-blue-200 px-2 py-1 rounded-lg text-[11px] font-bold flex items-center space-x-1" title="Registrar presencia física en obra">
                      <span>📍</span>
                      <span>Check-in Obra</span>
                    </button>
                    <!-- WhatsApp Simulator button -->
                    <button onclick="abrirWhatsAppSimulado('Constructora Bolívar', '120 Ton Cemento Estructural')" class="btn-tactile bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 px-2 py-1 rounded-lg text-[11px] font-bold flex items-center space-x-1" title="Abrir chat de WhatsApp">
                      <span>💬</span>
                      <span>Chat WA</span>
                    </button>
                  </div>
                </div>

                <!-- Expandable Timeline Panel -->
                <div id="timeline-panel-1" class="hidden mt-2.5 p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2 text-xs">
                  <div class="flex items-start space-x-2">
                    <span class="w-2 h-2 rounded-full bg-slate-400 mt-1"></span>
                    <div>
                      <p class="font-bold text-slate-800">Hace 8 días: Envío de Cotización #COT-902</p>
                      <p class="text-[11px] text-slate-500">120 Ton Cemento Estructural a $450,000/Ton.</p>
                    </div>
                  </div>
                  <div class="flex items-start space-x-2">
                    <span class="w-2 h-2 rounded-full bg-slate-400 mt-1"></span>
                    <div>
                      <p class="font-bold text-slate-800">Hace 15 días: Visita Técnica en Obra</p>
                      <p class="text-[11px] text-slate-500">Revisión de formaletas y diseño de mezcla con Ing. Meza.</p>
                    </div>
                  </div>
                </div>

                <!-- Primary 1-Click Action Buttons -->
                <div class="mt-3.5 grid grid-cols-3 gap-2">
                  <button onclick="openModalSeguimiento(1, 'Constructora Bolívar')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>📞 Registrar</span>
                    <span class="text-[9px] text-emerald-100">Seguimiento</span>
                  </button>

                  <button onclick="openModalEscalamiento(1, 'Constructora Bolívar')" class="btn-tactile bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>🚨 Escalar</span>
                    <span class="text-[9px] text-amber-100">A Depto (SLA)</span>
                  </button>

                  <button onclick="openModalCopiloto(1, 'Constructora Bolívar', 'industrial')" class="btn-tactile bg-[#004797] hover:bg-blue-900 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>✨ Copiloto</span>
                    <span class="text-[9px] text-blue-200">Fichas & RAG</span>
                  </button>
                </div>
              </article>

              <!-- CLIENT 2: Ferretería El Constructor -->
              <article id="card-client-2" class="bg-white rounded-2xl p-4 border-2 border-rose-300 shadow-xs client-card transition-all" data-channel="tradicional" data-status="danger">
                <div class="flex justify-between items-start gap-2">
                  <div class="min-w-0">
                    <div class="flex items-center space-x-2">
                      <span class="text-[10px] font-bold text-slate-500 uppercase tracking-wider bg-slate-100 px-2 py-0.5 rounded">🏪 Ferretería</span>
                      <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-300">
                        <span>🔴 5 DÍAS SIN CONTACTO</span>
                      </span>
                    </div>
                    <h3 class="font-extrabold text-slate-900 text-sm mt-1.5 truncate">Ferretería El Constructor</h3>
                    <p class="text-xs text-slate-500">Don Pedro Gómez • 45&nbsp;Ton Cemento Uso General</p>
                  </div>
                  <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200">$19M</span>
                </div>

                <div class="mt-2.5 p-2.5 bg-rose-50 rounded-xl border border-rose-200/80 flex items-start space-x-2 text-xs text-rose-900">
                  <span class="text-sm">🚨</span>
                  <div class="leading-tight">
                    <strong class="font-bold block">Riesgo inminente de compra a la competencia</strong>
                    <span>Rotación semanal agotada. Si no se contacta hoy, pedirá a Argos.</span>
                  </div>
                </div>

                <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                  <button onclick="toggleTimeline(2)" class="text-[#004797] font-bold hover:underline flex items-center space-x-1">
                    <span id="timeline-chevron-2">▼</span>
                    <span>Ver Historial</span>
                  </button>
                  <div class="flex items-center space-x-1.5">
                    <button onclick="realizarCheckinGPS(2, 'Ferretería El Constructor')" class="btn-tactile bg-blue-50 hover:bg-blue-100 text-[#004797] border border-blue-200 px-2 py-1 rounded-lg text-[11px] font-bold">
                      <span>📍 Check-in</span>
                    </button>
                    <button onclick="abrirWhatsAppSimulado('Ferretería El Constructor', '45 Ton Cemento Uso General')" class="btn-tactile bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 px-2 py-1 rounded-lg text-[11px] font-bold">
                      <span>💬 Chat WA</span>
                    </button>
                  </div>
                </div>

                <div id="timeline-panel-2" class="hidden mt-2.5 p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2 text-xs">
                  <div class="flex items-start space-x-2">
                    <span class="w-2 h-2 rounded-full bg-slate-400 mt-1"></span>
                    <div>
                      <p class="font-bold text-slate-800">Hace 5 días: Consulta de precio Cemento UG</p>
                      <p class="text-[11px] text-slate-500">Don Pedro pide mantener descuento de distribuidor mayorista.</p>
                    </div>
                  </div>
                </div>

                <div class="mt-3.5 grid grid-cols-3 gap-2">
                  <button onclick="openModalSeguimiento(2, 'Ferretería El Constructor')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>📞 Registrar</span>
                    <span class="text-[9px] text-emerald-100">Seguimiento</span>
                  </button>

                  <button onclick="openModalEscalamiento(2, 'Ferretería El Constructor')" class="btn-tactile bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>🚨 Escalar</span>
                    <span class="text-[9px] text-amber-100">A Depto (SLA)</span>
                  </button>

                  <button onclick="openModalCopiloto(2, 'Ferretería El Constructor', 'tradicional')" class="btn-tactile bg-[#004797] hover:bg-blue-900 text-white text-xs font-bold py-2.5 px-2 rounded-xl shadow-xs flex flex-col items-center justify-center">
                    <span>✨ Copiloto</span>
                    <span class="text-[9px] text-blue-200">Minuta & WA</span>
                  </button>
                </div>
              </article>

              <!-- CLIENT 3: Consorcio Vías del Magdalena -->
              <article id="card-client-3" class="bg-white rounded-2xl p-4 border border-amber-300 shadow-xs client-card" data-channel="industrial" data-status="warning">
                <div class="flex justify-between items-start">
                  <div>
                    <div class="flex items-center space-x-2">
                      <span class="text-[10px] font-bold text-slate-500 uppercase bg-slate-100 px-2 py-0.5 rounded">🏢 Obra</span>
                      <span class="text-[10px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-300">
                        🟡 6 DÍAS SIN CONTACTO
                      </span>
                    </div>
                    <h3 class="font-extrabold text-slate-900 text-sm mt-1.5">Consorcio Vías del Magdalena</h3>
                    <p class="text-xs text-slate-500">Ing. Laura Peña • 250&nbsp;Ton Concreto</p>
                  </div>
                  <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200">$112M</span>
                </div>
                <div class="mt-2.5 flex items-center justify-between text-xs text-slate-500 pt-2 border-t border-slate-100">
                  <span>Próxima fundida: Lunes 7:00&nbsp;AM</span>
                  <button onclick="openModalSeguimiento(3, 'Consorcio Vías')" class="text-[#004797] font-bold hover:underline">Gestionar anticipado →</button>
                </div>
              </article>

              <!-- CLIENT 4: Depósito Central La 30 -->
              <article id="card-client-4" class="bg-white rounded-2xl p-4 border border-emerald-300 shadow-xs client-card opacity-85" data-channel="tradicional" data-status="healthy">
                <div class="flex justify-between items-start">
                  <div>
                    <div class="flex items-center space-x-2">
                      <span class="text-[10px] font-bold text-slate-500 uppercase bg-slate-100 px-2 py-0.5 rounded">🏪 Ferretería</span>
                      <span class="text-[10px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-300">
                        🟢 AL DÍA
                      </span>
                    </div>
                    <h3 class="font-extrabold text-slate-900 text-sm mt-1.5">Depósito Central La 30</h3>
                    <p class="text-xs text-slate-500">30&nbsp;Ton despachadas ayer en Tractomula #4</p>
                  </div>
                  <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-1 rounded-md">✅ Satisfecho</span>
                </div>
              </article>

            </div>

          </div>

          <!-- ========================================== -->
          <!-- PANTALLA 2: LIGA MÓVIL (CLASIFICACIÓN)     -->
          <!-- ========================================== -->
          <div id="screen-liga" class="hidden flex-1 flex flex-col overflow-y-auto p-4 bg-slate-50">
            <div class="bg-gradient-to-r from-amber-500 to-orange-500 text-white p-4 rounded-2xl shadow-sm mb-4">
              <div class="flex justify-between items-center">
                <div>
                  <span class="text-[10px] uppercase font-bold tracking-wider text-amber-100">Competición Semanal</span>
                  <h3 class="text-lg font-black tracking-tight">División Clinker Oro</h3>
                </div>
                <span class="text-2xl">🏆</span>
              </div>
              <p class="text-xs text-amber-100 mt-1">Los 3 primeros clasifican a la <strong>División Diamante</strong> con bono adicional.</p>
            </div>

            <div class="space-y-2.5">
              <!-- Rank 1 (Current User) -->
              <div class="p-3.5 rounded-2xl bg-white border-2 border-amber-400 shadow-xs flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <span class="text-lg font-black text-amber-600 font-mono-data w-6 text-center">🥇</span>
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-10 h-10 rounded-full object-cover ring-2 ring-amber-400">
                  <div>
                    <div class="flex items-center space-x-1">
                      <strong class="text-xs font-bold text-slate-900">Carlos Mendoza</strong>
                      <span class="text-[9px] bg-blue-100 text-[#004797] font-bold px-1.5 py-0.2 rounded">Tú</span>
                    </div>
                    <span class="text-[11px] text-slate-500 font-mono-data">420 Ton • Caribe</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-xs font-black text-amber-600 font-mono-data">21 días 🔥</span>
                  <span class="block text-[10px] text-emerald-600 font-bold">Zona Ascenso</span>
                </div>
              </div>

              <!-- Rank 2 -->
              <div class="p-3.5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <span class="text-lg font-black text-slate-400 font-mono-data w-6 text-center">🥈</span>
                  <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Andrea Polo" class="w-10 h-10 rounded-full object-cover">
                  <div>
                    <strong class="text-xs font-bold text-slate-900">Andrea Polo</strong>
                    <span class="block text-[11px] text-slate-500 font-mono-data">395 Ton • Cartagena</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-xs font-bold text-slate-700 font-mono-data">19 días 🔥</span>
                  <span class="block text-[10px] text-emerald-600 font-bold">Zona Ascenso</span>
                </div>
              </div>

              <!-- Rank 3 -->
              <div class="p-3.5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <span class="text-lg font-black text-amber-800 font-mono-data w-6 text-center">🥉</span>
                  <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Javier Restrepo" class="w-10 h-10 rounded-full object-cover">
                  <div>
                    <strong class="text-xs font-bold text-slate-900">Javier Restrepo</strong>
                    <span class="block text-[11px] text-slate-500 font-mono-data">360 Ton • Barranquilla</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-xs font-bold text-slate-700 font-mono-data">15 días 🔥</span>
                  <span class="block text-[10px] text-emerald-600 font-bold">Zona Ascenso</span>
                </div>
              </div>

              <!-- Rank 4 -->
              <div class="p-3.5 rounded-2xl bg-white border border-slate-200 flex items-center justify-between opacity-80">
                <div class="flex items-center space-x-3">
                  <span class="text-sm font-bold text-slate-400 font-mono-data w-6 text-center">4</span>
                  <img src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=80&auto=format&fit=crop&q=80" alt="Felipe Castro" class="w-10 h-10 rounded-full object-cover">
                  <div>
                    <strong class="text-xs font-bold text-slate-900">Felipe Castro</strong>
                    <span class="block text-[11px] text-slate-500 font-mono-data">280 Ton • Santa Marta</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="text-xs font-bold text-rose-600 font-mono-data">7 días ⚠️</span>
                  <span class="block text-[10px] text-slate-400">Permanencia</span>
                </div>
              </div>
            </div>
          </div>

          <!-- ========================================== -->
          <!-- PANTALLA 3: MI PERFIL (COMPLETA Y VIBRANTE)-->
          <!-- ========================================== -->
          <div id="screen-perfil" class="hidden flex-1 flex flex-col overflow-y-auto p-4 bg-slate-50 space-y-4">
            
            <!-- User Profile Card -->
            <div class="bg-white rounded-3xl p-5 border border-slate-200/90 shadow-xs relative overflow-hidden">
              <div class="flex items-center space-x-4">
                <div class="relative">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-16 h-16 rounded-full object-cover ring-4 ring-[#004797]/15">
                  <span class="absolute bottom-0 right-0 bg-[#004797] text-white p-1 rounded-full text-[10px]">⭐</span>
                </div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900 leading-tight">Carlos Mendoza</h3>
                  <p class="text-xs text-slate-500 font-medium">Asesor Senior • Regional Caribe</p>
                  <div class="mt-1 flex items-center space-x-2">
                    <span class="bg-blue-50 text-[#004797] border border-blue-200 text-[10px] font-extrabold px-2 py-0.5 rounded-full">Nivel 4: Maestro del Clinker</span>
                  </div>
                </div>
              </div>

              <!-- XP Progress Bar -->
              <div class="mt-4 pt-3 border-t border-slate-100">
                <div class="flex justify-between items-center text-xs mb-1">
                  <span class="text-slate-500 font-semibold text-[11px]">Experiencia Comercial (XP)</span>
                  <span class="font-mono-data font-bold text-slate-900 text-[11px]">850 / 1,000 XP</span>
                </div>
                <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                  <div class="bg-gradient-to-r from-blue-600 to-[#004797] h-full rounded-full" style="width: 85%"></div>
                </div>
                <span class="text-[10px] text-slate-400 mt-1 block">Faltan 150 XP para desbloquear <em>División Diamante</em></span>
              </div>
            </div>

            <!-- Casco Protector / Escudo de Fraguado Module -->
            <div id="shield-inventory-card" class="bg-gradient-to-br from-amber-50 to-orange-50 border-2 border-amber-300 rounded-3xl p-4 shadow-xs relative overflow-hidden transition-all duration-300">
              <div class="flex items-center justify-between mb-2">
                <div class="flex items-center space-x-2">
                  <span class="text-2xl">⛑️</span>
                  <div>
                    <h4 class="font-bold text-xs text-slate-900 leading-tight">Inventario de Cascos Protectores</h4>
                    <p class="text-[11px] text-amber-800">1 Casco disponible (Ganas 1 cada 7 días)</p>
                  </div>
                </div>
                <span id="shield-status-badge" class="bg-amber-500 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-full">Listo</span>
              </div>
              <p class="text-xs text-slate-700 leading-snug">
                ¿Tienes una emergencia de salud o viaje en carretera sin señal? Activa el casco para congelar tu racha por 24 horas sin penalización.
              </p>
              
              <button id="btn-activate-shield" onclick="activarCascoProtector24h()" class="btn-tactile mt-3 w-full bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-700 hover:to-orange-700 text-white font-extrabold py-2.5 rounded-2xl text-xs shadow-sm flex items-center justify-center space-x-2">
                <span>🧊</span>
                <span>Activar Escudo 24h (Congelar Racha)</span>
              </button>
            </div>

            <!-- Vitrina de Trofeos Interactiva -->
            <div class="bg-white rounded-3xl p-4 border border-slate-200/90 shadow-xs">
              <div class="flex justify-between items-center mb-3">
                <h4 class="font-extrabold text-sm text-slate-900 flex items-center space-x-1.5">
                  <span>🏅</span>
                  <span>Vitrina de Trofeos Ultracem</span>
                </h4>
                <span class="text-[11px] font-bold text-slate-400">5 / 6 Desbloqueados</span>
              </div>

              <div class="grid grid-cols-3 gap-2.5">
                <!-- Trophy 1 -->
                <button onclick="verDetalleTrofeo('Furia de Medianoche', 'Salvaste una cuenta en semáforo rojo a las 11:58 PM justo antes del cierre.', '🏆', '+100 XP')" class="btn-tactile p-2.5 rounded-2xl bg-amber-50 border border-amber-200 flex flex-col items-center text-center">
                  <span class="text-2xl">🏆</span>
                  <span class="text-[10px] font-bold text-slate-900 mt-1 leading-tight">Furia 11:58</span>
                  <span class="text-[9px] text-amber-700 font-bold">+100 XP</span>
                </button>
                <!-- Trophy 2 -->
                <button onclick="verDetalleTrofeo('Llama de Hierro', 'Mantuviste una racha ininterrumpida de 21 días consecutivos.', '🔥', '+250 XP')" class="btn-tactile p-2.5 rounded-2xl bg-orange-50 border border-orange-200 flex flex-col items-center text-center">
                  <span class="text-2xl">🔥</span>
                  <span class="text-[10px] font-bold text-slate-900 mt-1 leading-tight">Llama Hierro</span>
                  <span class="text-[9px] text-orange-700 font-bold">+250 XP</span>
                </button>
                <!-- Trophy 3 -->
                <button onclick="verDetalleTrofeo('Titán del Clinker', 'Superaste las 400 Toneladas despachadas en un solo mes.', '🏗️', '+300 XP')" class="btn-tactile p-2.5 rounded-2xl bg-blue-50 border border-blue-200 flex flex-col items-center text-center">
                  <span class="text-2xl">🏗️</span>
                  <span class="text-[10px] font-bold text-slate-900 mt-1 leading-tight">Titán Clinker</span>
                  <span class="text-[9px] text-blue-700 font-bold">+300 XP</span>
                </button>
                <!-- Trophy 4 -->
                <button onclick="verDetalleTrofeo('Desbloqueador de Cartera', 'Escalaste 5 casos a tiempo logrando liberar $150M en cupos.', '🛡️', '+150 XP')" class="btn-tactile p-2.5 rounded-2xl bg-purple-50 border border-purple-200 flex flex-col items-center text-center">
                  <span class="text-2xl">🛡️</span>
                  <span class="text-[10px] font-bold text-slate-900 mt-1 leading-tight">Desbloqueador</span>
                  <span class="text-[9px] text-purple-700 font-bold">+150 XP</span>
                </button>
                <!-- Trophy 5 -->
                <button onclick="verDetalleTrofeo('Conquistador de Obra', 'Realizaste 20 check-ins GPS exitosos directamente en terreno.', '📍', '+200 XP')" class="btn-tactile p-2.5 rounded-2xl bg-emerald-50 border border-emerald-200 flex flex-col items-center text-center">
                  <span class="text-2xl">📍</span>
                  <span class="text-[10px] font-bold text-slate-900 mt-1 leading-tight">Check-in Pro</span>
                  <span class="text-[9px] text-emerald-700 font-bold">+200 XP</span>
                </button>
                <!-- Trophy 6 (Locked) -->
                <button onclick="verDetalleTrofeo('Leyenda Diamante', 'BLOQUEADO: Alcanza 30 días seguidos de racha y 500 Ton en el mes.', '🔒', '+500 XP')" class="btn-tactile p-2.5 rounded-2xl bg-slate-100 border border-slate-200 flex flex-col items-center text-center opacity-60">
                  <span class="text-2xl">🔒</span>
                  <span class="text-[10px] font-bold text-slate-600 mt-1 leading-tight">Leyenda Dia</span>
                  <span class="text-[9px] text-slate-400 font-bold">Bloqueado</span>
                </button>
              </div>
            </div>

            <!-- Mapa de Calor de Rachas (Estilo GitHub / Duolingo) -->
            <div class="bg-white rounded-3xl p-4 border border-slate-200/90 shadow-xs">
              <div class="flex justify-between items-center mb-2">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Mapa de Calor de Rachas (90 Días)</h4>
                  <p class="text-[11px] text-slate-500">Cada celda representa un día de seguimiento activo</p>
                </div>
                <span class="text-xs font-black text-amber-600 font-mono-data">98% Éxito</span>
              </div>

              <!-- Interactive Heatmap Grid -->
              <div class="mt-3 overflow-x-auto pb-1">
                <div class="grid grid-flow-col grid-rows-7 gap-1.5 w-max">
                  <!-- Generating 7x12 calendar grid with CSS classes -->
                  <!-- Week 1 to 12 simulated -->
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500" title="1 Sep: 100% Gestionado"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600" title="2 Sep: Pedido cerrado"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500" title="3 Sep: 100% Gestionado"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500" title="4 Sep: Racha salvada 11:45 PM"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500" title="5 Sep: Gestionado"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600" title="6 Sep: Despacho 40 Ton"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200" title="7 Sep: Domingo (Fraguado Seguro)"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-sky-400" title="10 Sep: Casco Protector activado"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-sky-400" title="Casco Protector"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-slate-200"></div>

                  <!-- Current Week active -->
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-500"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-emerald-600"></div>
                  <div class="w-3.5 h-3.5 rounded-xs bg-orange-500 ring-2 ring-orange-300 animate-pulse" title="Hoy: En Racha Activa"></div>
                </div>
              </div>

              <div class="mt-2.5 flex items-center justify-between text-[10px] text-slate-400">
                <div class="flex items-center space-x-2">
                  <span class="flex items-center space-x-1"><span class="w-2 h-2 rounded-xs bg-emerald-500 inline-block"></span><span>Al día</span></span>
                  <span class="flex items-center space-x-1"><span class="w-2 h-2 rounded-xs bg-orange-500 inline-block"></span><span>Racha</span></span>
                  <span class="flex items-center space-x-1"><span class="w-2 h-2 rounded-xs bg-sky-400 inline-block"></span><span>Casco</span></span>
                </div>
                <span>Hace 90 días ➔ Hoy</span>
              </div>
            </div>

          </div>

        </div>

        <!-- Phone 4-Tab Bottom Navigation Bar -->
        <nav aria-label="Navegación Móvil" class="bg-white border-t border-slate-200/80 px-4 py-2.5 flex justify-around items-center text-xs">
          <button id="nav-btn-racha" onclick="navigateToTab('racha')" class="btn-tactile flex flex-col items-center text-[#004797] font-bold">
            <span class="text-lg">🔥</span>
            <span class="text-[10px] mt-0.5">Racha</span>
          </button>
          <button id="nav-btn-copiloto" onclick="openModalCopiloto(1, 'Asistente Global', 'general')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <span class="text-lg">✨</span>
            <span class="text-[10px] mt-0.5">Copiloto</span>
          </button>
          <button id="nav-btn-liga" onclick="navigateToTab('liga')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <span class="text-lg">🏆</span>
            <span class="text-[10px] mt-0.5">Liga</span>
          </button>
          <button id="nav-btn-perfil" onclick="navigateToTab('perfil')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <span class="text-lg">👤</span>
            <span class="text-[10px] mt-0.5">Perfil</span>
          </button>
        </nav>

      </div>
    </div>


    <!-- ============================================================== -->
    <!-- 2. VISTA DASHBOARD SUPERVISOR (WEB / PC EXECUTIVE)             -->
    <!-- ============================================================== -->
    <div id="view-web" class="hidden w-full space-y-6">
      
      <!-- Top Executive Banner -->
      <div class="bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div class="flex items-center space-x-3">
            <span class="bg-blue-50 text-[#004797] text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider border border-blue-200/60">Centro de Operaciones</span>
            <span class="text-xs text-slate-300">•</span>
            <span class="text-xs text-slate-500 font-medium">Regional Caribe & Obras</span>
          </div>
          <h2 class="text-2xl font-black text-slate-900 tracking-tight mt-1">Supervisión Ejecutiva UltraRacha</h2>
          <p class="text-sm text-slate-600">Monitoreo en tiempo real de toneladas, rachas y resolución de bloqueos con SLA.</p>
        </div>

        <div class="flex items-center space-x-3.5">
          <div class="text-right hidden sm:block">
            <p class="text-xs text-slate-400">Líder Regional</p>
            <p class="text-sm font-extrabold text-slate-900">Ing. Roberto Vega</p>
          </div>
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80" alt="Roberto Vega" class="w-12 h-12 rounded-2xl border-2 border-[#004797] object-cover shadow-xs">
        </div>
      </div>

      <!-- 4 Data Tiles -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400">Toneladas del Mes</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 font-mono-data">3,420 <span class="text-sm font-medium text-slate-500">/ 3,750 Ton</span></h3>
            <span class="text-xs font-bold text-emerald-600 mt-1 block">↑ 91.2% de la meta</span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#004797] flex items-center justify-center text-2xl font-black">🏗️</div>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400">Seguimiento a Tiempo</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 font-mono-data">94.8%</h3>
            <span class="text-xs font-bold text-emerald-600 mt-1 block">↑ +6.2% vs mes anterior</span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-700 flex items-center justify-center text-2xl">⏱️</div>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400">Críticos Salvados Hoy</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 font-mono-data">23 <span class="text-sm font-medium text-slate-500">/ 24</span></h3>
            <span class="text-xs font-bold text-amber-600 mt-1 block">⚠️ 1 pendiente antes 11:59 PM</span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-amber-50 text-amber-700 flex items-center justify-center text-2xl">🔥</div>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400">Casos Escalados (SLA)</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 font-mono-data">6 Activos</h3>
            <span class="text-xs font-bold text-emerald-600 mt-1 block">✅ 100% en tiempo SLA</span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-700 flex items-center justify-center text-2xl">🚨</div>
        </div>
      </div>

      <!-- Main Columns: Leaderboard & Escalation Table -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <section class="lg:col-span-5 bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs">
          <div class="flex justify-between items-center mb-4">
            <div>
              <h3 class="text-lg font-black text-slate-900">Liga Maestros Ultracem</h3>
              <p class="text-xs text-slate-500">Ranking por constancia diaria (Racha) y volumen</p>
            </div>
            <span class="bg-amber-100 text-amber-800 text-xs font-bold px-2.5 py-0.5 rounded-full">División Oro</span>
          </div>

          <div class="space-y-3">
            <div class="p-3.5 rounded-2xl bg-amber-50/70 border border-amber-200 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-amber-600 w-6 text-center">🥇</span>
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-10 h-10 rounded-full border-2 border-amber-400 object-cover">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Carlos Mendoza</h4>
                  <p class="text-xs text-slate-500 font-mono-data">420 Ton • Caribe</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-amber-600 font-mono-data">21 Días 🔥</span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md block">Al día</span>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-slate-400 w-6 text-center">🥈</span>
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Andrea Polo" class="w-10 h-10 rounded-full border border-slate-300 object-cover">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Andrea Polo</h4>
                  <p class="text-xs text-slate-500 font-mono-data">395 Ton • Cartagena</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-slate-700 font-mono-data">19 Días 🔥</span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md block">Al día</span>
              </div>
            </div>

            <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-amber-800 w-6 text-center">🥉</span>
                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Javier Restrepo" class="w-10 h-10 rounded-full border border-slate-300 object-cover">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Javier Restrepo</h4>
                  <p class="text-xs text-slate-500 font-mono-data">360 Ton • Barranquilla</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-slate-700 font-mono-data">15 Días 🔥</span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md block">Al día</span>
              </div>
            </div>
          </div>
        </section>

        <!-- Right: Escalation SLA Audit Table -->
        <section class="lg:col-span-7 bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 mb-4">
            <div>
              <h3 class="text-lg font-black text-slate-900">Bandeja de Casos Escalados con SLA</h3>
              <p class="text-xs text-slate-500">Tickets transferidos a Cartera, Logística y Calidad</p>
            </div>
            <span class="text-xs font-semibold bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full border border-emerald-200">
              SLA Promedio: 1h 42m
            </span>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <thead class="bg-slate-50 text-slate-600 uppercase tracking-wider text-[10px] border-b border-slate-200">
                <tr>
                  <th class="py-2.5 px-3">Ticket / Cliente</th>
                  <th class="py-2.5 px-3">Depto Asignado</th>
                  <th class="py-2.5 px-3">Asesor</th>
                  <th class="py-2.5 px-3">Tiempo SLA</th>
                  <th class="py-2.5 px-3 text-right">Acción</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100 font-mono-data">
                <tr class="hover:bg-slate-50">
                  <td class="py-3 px-3">
                    <strong class="font-bold text-slate-900 block font-sans">#TR-4091</strong>
                    <span class="text-slate-500 font-sans">Consorcio Vías • Ruta Mixer</span>
                  </td>
                  <td class="py-3 px-3 font-sans">
                    <span class="bg-blue-50 text-[#004797] font-bold px-2 py-0.5 rounded-md text-[11px] border border-blue-200">
                      🚚 Logística (2h)
                    </span>
                  </td>
                  <td class="py-3 px-3 font-sans text-slate-700">Carlos Mendoza</td>
                  <td class="py-3 px-3">
                    <span class="font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">01h : 14m</span>
                  </td>
                  <td class="py-3 px-3 text-right font-sans">
                    <button onclick="alert('Notificación enviada a Planta Ultracem.')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-800 px-2.5 py-1 rounded-lg font-bold">
                      Acelerar ⚡
                    </button>
                  </td>
                </tr>

                <tr class="hover:bg-slate-50">
                  <td class="py-3 px-3">
                    <strong class="font-bold text-slate-900 block font-sans">#TR-4088</strong>
                    <span class="text-slate-500 font-sans">Ferretería El Sol • Cupo $30M</span>
                  </td>
                  <td class="py-3 px-3 font-sans">
                    <span class="bg-purple-50 text-purple-800 font-bold px-2 py-0.5 rounded-md text-[11px] border border-purple-200">
                      💳 Cartera (4h)
                    </span>
                  </td>
                  <td class="py-3 px-3 font-sans text-slate-700">Andrea Polo</td>
                  <td class="py-3 px-3">
                    <span class="font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">02h : 45m</span>
                  </td>
                  <td class="py-3 px-3 text-right font-sans">
                    <button onclick="alert('Notificación enviada al analista de Crédito.')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-800 px-2.5 py-1 rounded-lg font-bold">
                      Revisar 🔍
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

      </div>
    </div>

  </main>


  <!-- ============================================================== -->
  <!-- MODALES INTERACTIVOS Y EXPANDIBLES                             -->
  <!-- ============================================================== -->

  <!-- MODAL: DETALLE DE TROFEO -->
  <div id="modal-trofeo" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-sm w-full p-6 shadow-2xl border border-slate-200 text-center relative animate-in fade-in zoom-in duration-150">
      <button onclick="closeModal('modal-trofeo')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold">✕</button>
      <div id="trofeo-modal-icon" class="text-5xl mx-auto my-2">🏆</div>
      <h3 id="trofeo-modal-title" class="text-lg font-black text-slate-900 mt-2">Título Trofeo</h3>
      <span id="trofeo-modal-xp" class="inline-block my-1.5 bg-amber-100 text-amber-800 font-extrabold text-xs px-3 py-1 rounded-full">+100 XP Comercial</span>
      <p id="trofeo-modal-desc" class="text-xs text-slate-600 mt-2 leading-relaxed">Descripción del logro y cómo se obtuvo.</p>
      <button onclick="closeModal('modal-trofeo')" class="btn-tactile mt-5 w-full bg-[#004797] hover:bg-blue-900 text-white font-bold py-2.5 rounded-xl text-xs">
        ¡Excelente!
      </button>
    </div>
  </div>

  <!-- MODAL: SIMULADOR DE WHATSAPP EN VIVO -->
  <div id="modal-whatsapp" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-[#ECE5DD] rounded-3xl max-w-sm w-full shadow-2xl border border-slate-300 overflow-hidden flex flex-col relative animate-in fade-in zoom-in duration-150 h-[550px]">
      
      <!-- WhatsApp Green Header -->
      <div class="bg-[#075E54] text-white p-3 flex items-center justify-between">
        <div class="flex items-center space-x-2.5">
          <button onclick="closeModal('modal-whatsapp')" class="text-white text-lg font-bold">←</button>
          <div class="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center text-slate-800 font-bold text-xs">🏢</div>
          <div>
            <h4 id="wa-contact-name" class="font-bold text-xs leading-tight">Constructora Bolívar</h4>
            <span class="text-[10px] text-emerald-200">En línea</span>
          </div>
        </div>
        <button onclick="closeModal('modal-whatsapp')" class="text-white text-xs font-bold bg-white/20 px-2 py-1 rounded-lg">Cerrar</button>
      </div>

      <!-- Chat Messages Area -->
      <div id="wa-messages-container" class="flex-1 p-3 overflow-y-auto space-y-2 text-xs">
        <!-- Received -->
        <div class="flex justify-start">
          <div class="bg-white p-2.5 rounded-xl rounded-tl-none shadow-xs max-w-[85%] text-slate-800">
            <p>Hola Carlos, ¿cómo va la programación de las 120 Ton de cemento estructural? ¿Me confirmas el ensayo de compresión?</p>
            <span class="text-[9px] text-slate-400 block text-right mt-1">10:14 AM</span>
          </div>
        </div>
        <!-- Sent Draft -->
        <div class="flex justify-end">
          <div id="wa-sent-bubble" class="bg-[#DCF8C6] p-2.5 rounded-xl rounded-tr-none shadow-xs max-w-[85%] text-slate-900">
            <p id="wa-sent-text">“Estimado Ing. Andrés, un cordial saludo de Ultracem. Confirmamos 120 Toneladas Cemento Estructural NTC 121 (28 MPa a 28 días) para despacho prioritario el jueves en Torre del Mar.”</p>
            <span class="text-[9px] text-emerald-800 block text-right mt-1">10:15 AM ✓✓</span>
          </div>
        </div>
      </div>

      <!-- Input Footer -->
      <div class="bg-white p-2 flex items-center space-x-2 border-t border-slate-200">
        <input type="text" id="wa-input" class="flex-1 bg-slate-100 text-xs px-3 py-2 rounded-full outline-none" value="¿Autorizamos el despacho para el jueves a las 7 AM?">
        <button onclick="enviarMensajeWASimulado()" class="btn-tactile w-9 h-9 rounded-full bg-[#075E54] text-white flex items-center justify-center text-sm font-bold shadow-xs">
          ➤
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL: REGISTRAR SEGUIMIENTO -->
  <div id="modal-seguimiento" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150">
      <button onclick="closeModal('modal-seguimiento')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold">✕</button>

      <div class="flex items-center space-x-2 text-emerald-600 mb-1">
        <span class="text-xl">📞</span>
        <span class="text-xs font-bold uppercase tracking-wider">Gestión Comercial Rápida</span>
      </div>
      <h3 id="modal-seg-title" class="text-lg font-black text-slate-900">Registrar Seguimiento</h3>
      <p class="text-xs text-slate-500">Selecciona el resultado del contacto para salvar tu racha de hoy antes de medianoche.</p>

      <div class="mt-4 space-y-2.5">
        <button onclick="completarSeguimiento('fundida')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group">
          <span class="text-lg bg-amber-100 text-amber-800 p-2 rounded-xl">🏗️</span>
          <div>
            <strong class="text-xs font-bold text-slate-900 group-hover:text-emerald-900 block">Cliente en fundida de placa / Ocupado</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">Se reprograma recordatorio para mañana 8:00 AM. <em>¡Cuenta como intento válido y salva la racha!</em></p>
          </div>
        </button>

        <button onclick="completarSeguimiento('pedido')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group">
          <span class="text-lg bg-emerald-100 text-emerald-800 p-2 rounded-xl">📦</span>
          <div>
            <strong class="text-xs font-bold text-slate-900 group-hover:text-emerald-900 block">Llamada efectiva — Aceptó pedido</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">Cliente confirma volumen de cemento. Se programa despacho formal.</p>
          </div>
        </button>

        <button onclick="completarSeguimiento('nocontesta')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group">
          <span class="text-lg bg-blue-100 text-blue-800 p-2 rounded-xl">💬</span>
          <div>
            <strong class="text-xs font-bold text-slate-900 group-hover:text-emerald-900 block">No contestó — Envío WhatsApp Automático</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">El Copiloto IA deja mensaje redactado y agenda segundo intento para hoy 4:00 PM.</p>
          </div>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL: ESCALAMIENTO A DEPARTAMENTO CON SLA -->
  <div id="modal-escalamiento" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150">
      <button onclick="closeModal('modal-escalamiento')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold">✕</button>

      <div class="flex items-center space-x-2 text-amber-600 mb-1">
        <span class="text-xl">🚨</span>
        <span class="text-xs font-bold uppercase tracking-wider">Salvavidas Operativo Ultracem</span>
      </div>
      <h3 id="modal-esc-title" class="text-lg font-black text-slate-900">Escalar Caso a Departamento</h3>
      <p class="text-xs text-slate-500">¿El cierre depende de otra área? Transfiere el ticket con SLA y tu racha quedará asegurada.</p>

      <fieldset class="mt-4 space-y-2">
        <legend class="block text-xs font-bold text-slate-700 mb-1">Selecciona el área responsable:</legend>
        <div class="grid grid-cols-2 gap-2">
          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-blue-500 bg-blue-50/50 flex flex-col justify-between">
            <input type="radio" name="depto" value="cartera" checked class="sr-only">
            <span class="text-xs font-bold text-slate-900">💳 Cartera & Crédito</span>
            <span class="text-[10px] text-[#004797] font-bold mt-1">SLA: 4 horas</span>
          </label>
          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="logistica" class="sr-only">
            <span class="text-xs font-bold text-slate-900">🚚 Logística / Despacho</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 2 horas</span>
          </label>
          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="calidad" class="sr-only">
            <span class="text-xs font-bold text-slate-900">🔬 Calidad / NTC 121</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 6 horas</span>
          </label>
          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="pricing" class="sr-only">
            <span class="text-xs font-bold text-slate-900">🏷️ Pricing / Gerencia</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 4 horas</span>
          </label>
        </div>
      </fieldset>

      <div class="mt-3">
        <label for="esc-motivo" class="block text-xs font-bold text-slate-700 mb-1">Motivo del escalamiento:</label>
        <textarea id="esc-motivo" rows="2" class="w-full text-xs p-2.5 rounded-xl border border-slate-300 outline-none focus:ring-2 focus:ring-[#004797]"></textarea>
      </div>

      <div class="mt-4 pt-1">
        <button onclick="confirmarEscalamiento()" class="btn-tactile w-full bg-[#004797] hover:bg-blue-900 text-white font-extrabold py-2.5 rounded-xl text-xs shadow-md transition-all">
          Transferir Ticket y Blindar Racha Hoy 🛡️
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL: COPILOTO IA INTEGRAL -->
  <div id="modal-copiloto" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150 max-h-[90vh] flex flex-col">
      <button onclick="closeModal('modal-copiloto')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold">✕</button>

      <div class="flex items-center space-x-2 text-[#004797] mb-1">
        <span class="text-xl">✨</span>
        <span class="text-xs font-extrabold uppercase tracking-wider">Copiloto Comercial Ultracem</span>
      </div>
      <h3 id="copiloto-client-name" class="text-lg font-black text-slate-900">Asistencia Inteligente de Cuenta</h3>
      <p class="text-xs text-slate-500">Redacción, consulta técnica de productos y analítica comercial.</p>

      <div class="mt-4 flex border-b border-slate-200 text-xs" role="tablist">
        <button id="cop-tab-1" onclick="switchCopilotoTab(1)" class="btn-tactile pb-2 px-3 font-extrabold text-[#004797] border-b-2 border-[#004797]">📝 Redactar Escrito</button>
        <button id="cop-tab-2" onclick="switchCopilotoTab(2)" class="btn-tactile pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">📚 Fichas Ultracem</button>
        <button id="cop-tab-3" onclick="switchCopilotoTab(3)" class="btn-tactile pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">🔍 Investigar Cliente</button>
      </div>

      <div class="flex-1 overflow-y-auto py-3 space-y-3">
        <!-- PESTAÑA 1 -->
        <div id="cop-panel-1" class="space-y-3 text-xs">
          <div>
            <label class="block font-bold text-slate-700 mb-1">Dictado rápido por voz o notas en obra:</label>
            <div class="relative">
              <textarea id="cop-voice-input" rows="2" class="w-full p-2.5 pr-10 rounded-xl border border-slate-300 text-xs outline-none focus:border-[#004797]" placeholder="Hablé con el cliente en obra, requiere cotización formal de cemento estructural…"></textarea>
              <button onclick="simularVoz()" class="btn-tactile absolute right-2 top-2 p-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm">🎙️</button>
            </div>
            <button onclick="generarMinutaIA()" class="btn-tactile mt-2 w-full bg-[#004797] hover:bg-blue-900 text-white font-extrabold py-2.5 rounded-xl text-xs transition-all flex items-center justify-center space-x-1 shadow-xs">
              <span>✨ Generar Minuta CRM y WhatsApp</span>
            </button>
          </div>

          <div id="cop-output-box" class="bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 space-y-2">
            <div class="flex justify-between items-center">
              <span class="font-extrabold text-slate-800 text-[11px] uppercase tracking-wider">Borrador WhatsApp para el Cliente:</span>
              <button onclick="copiarAlPortapapeles()" id="btn-copy" class="btn-tactile text-[#004797] font-bold text-xs hover:underline flex items-center space-x-1">
                <span>📋 Copiar</span>
              </button>
            </div>
            <p id="cop-whatsapp-text" class="text-xs text-slate-700 bg-white p-3 rounded-xl border border-slate-200 italic leading-relaxed">
              “Estimado Ing. Andrés, un cordial saludo de Ultracem. Conforme a nuestra llamada, le confirmo la reserva de 120 Toneladas de Cemento Estructural NTC 121 para despacho el jueves a primera hora en Torre del Mar. Le adjunto el certificado de resistencia a compresión (28 MPa a 28 días). Quedo atento a su visto bueno para la programación del camión. ¡Construyamos juntos!”
            </p>
          </div>
        </div>

        <!-- PESTAÑA 2 -->
        <div id="cop-panel-2" class="hidden space-y-3 text-xs">
          <div>
            <label class="block font-bold text-slate-700 mb-1">Seleccionar Producto Ultracem:</label>
            <select id="prod-selector" onchange="actualizarFichaTecnica()" class="w-full p-2.5 rounded-xl border border-slate-300 text-xs font-semibold outline-none focus:border-[#004797]">
              <option value="estructural">Cemento Estructural Tipo ART (NTC 121)</option>
              <option value="general">Cemento Uso General Tipo UG (NTC 121)</option>
              <option value="marino">Cemento Marino Resistente a Sulfatos (MRS)</option>
              <option value="blanco">Cemento Blanco Arquitectónico</option>
            </select>
          </div>

          <div class="bg-blue-50/70 border border-blue-200 rounded-2xl p-3.5 space-y-2.5">
            <div class="flex items-center justify-between">
              <h4 id="ficha-nombre" class="font-black text-sm text-[#004797]">Cemento Estructural ART (NTC 121)</h4>
              <span class="bg-blue-200 text-blue-900 text-[10px] font-bold px-2 py-0.5 rounded-md">Alta Resistencia</span>
            </div>
            <p id="ficha-desc" class="text-xs text-slate-700 leading-relaxed">
              Desarrollado para estructuras de concreto reforzado que demandan altas resistencias tempranas. Ideal para desencofrado rápido.
            </p>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-blue-200/80 text-[11px]">
              <div class="bg-white p-2.5 rounded-xl border border-blue-100">
                <span class="text-slate-400 block font-medium">Resistencia 28 Días:</span>
                <strong id="ficha-resistencia" class="text-slate-900 font-bold font-mono-data">≥ 28.0 MPa</strong>
              </div>
              <div class="bg-white p-2.5 rounded-xl border border-blue-100">
                <span class="text-slate-400 block font-medium">Fraguado Inicial:</span>
                <strong id="ficha-fraguado" class="text-slate-900 font-bold font-mono-data">≥ 45 minutos</strong>
              </div>
            </div>
          </div>
        </div>

        <!-- PESTAÑA 3 -->
        <div id="cop-panel-3" class="hidden space-y-3 text-xs">
          <div class="bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 space-y-2">
            <strong class="font-bold text-slate-900 block">Radiografía Comercial (Últimos 90 Días)</strong>
            <p class="text-slate-700">• Compras Totales: 340 Toneladas acumuladas ($153M COP).</p>
            <p class="text-slate-700">• Frecuencia de Pedido: Cada 14 días.</p>
            <p class="text-slate-700">• Puntualidad de Pago: 18 días promedio.</p>
          </div>
          <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3.5 text-xs text-amber-900 space-y-1">
            <strong class="font-bold block">🎯 Oportunidad Detectada por IA:</strong>
            <p>Se adjudicó la fase II del proyecto en Barranquilla. Demandará <strong>+450 Toneladas</strong> adicionales de Cemento Estructural en las próximas semanas.</p>
          </div>
        </div>
      </div>

      <div class="pt-3 border-t border-slate-100 text-right">
        <button onclick="closeModal('modal-copiloto')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-4 py-2 rounded-xl text-xs">
          Cerrar Asistente
        </button>
      </div>
    </div>
  </div>


  <!-- TOAST NOTIFICATIONS (ARIA LIVE) -->
  <div id="toast-container" aria-live="polite" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>


  <!-- ============================================================== -->
  <!-- JAVASCRIPT STATE ENGINE                                        -->
  <!-- ============================================================== -->
  <script>
    // Audio synthesizer for audio feedback
    function playChime(type) {{
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        if (type === 'streak') {{
          const now = ctx.currentTime;
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.setValueAtTime(659.25, now + 0.1);
          osc.frequency.setValueAtTime(783.99, now + 0.2);
          osc.frequency.setValueAtTime(1046.50, now + 0.3);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
          osc.start(now);
          osc.stop(now + 0.6);
        }} else if (type === 'freeze') {{
          // Icy crystal chime
          const now = ctx.currentTime;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(1200, now);
          osc.frequency.exponentialRampToValueAtTime(400, now + 0.5);
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
          osc.start(now);
          osc.stop(now + 0.5);
        }} else if (type === 'gps') {{
          // Radar ping
          const now = ctx.currentTime;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(950, now);
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
          osc.start(now);
          osc.stop(now + 0.25);
        }} else {{
          const now = ctx.currentTime;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(880, now);
          gain.gain.setValueAtTime(0.06, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.1);
          osc.start(now);
          osc.stop(now + 0.1);
        }}
      }} catch (e) {{}}
    }}

    let currentStreak = 21;
    let cascosDisponibles = 1;
    let isShieldActive = false;
    let currentActiveClientId = 1;

    // View Switcher (Mobile vs Web Dashboard)
    function switchView(view) {{
      playChime('click');
      const mobileView = document.getElementById('view-mobile');
      const webView = document.getElementById('view-web');
      const btnMobile = document.getElementById('btn-view-mobile');
      const btnWeb = document.getElementById('btn-view-web');

      if (view === 'mobile') {{
        mobileView.classList.remove('hidden');
        webView.classList.add('hidden');
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs";
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
      }} else {{
        mobileView.classList.add('hidden');
        webView.classList.remove('hidden');
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs";
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
      }}
    }}

    // Mobile Tabs Navigation (Racha, Copiloto, Liga, Perfil)
    function navigateToTab(tab) {{
      playChime('click');
      const screenRacha = document.getElementById('screen-racha');
      const screenLiga = document.getElementById('screen-liga');
      const screenPerfil = document.getElementById('screen-perfil');

      const btnRacha = document.getElementById('nav-btn-racha');
      const btnLiga = document.getElementById('nav-btn-liga');
      const btnPerfil = document.getElementById('nav-btn-perfil');

      // Reset tabs style
      [btnRacha, btnLiga, btnPerfil].forEach(b => {{
        b.className = "btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold";
      }});

      screenRacha.classList.add('hidden');
      screenLiga.classList.add('hidden');
      screenPerfil.classList.add('hidden');

      if (tab === 'racha') {{
        screenRacha.classList.remove('hidden');
        btnRacha.className = "btn-tactile flex flex-col items-center text-[#004797] font-bold";
      }} else if (tab === 'liga') {{
        screenLiga.classList.remove('hidden');
        btnLiga.className = "btn-tactile flex flex-col items-center text-[#004797] font-bold";
      }} else if (tab === 'perfil') {{
        screenPerfil.classList.remove('hidden');
        btnPerfil.className = "btn-tactile flex flex-col items-center text-[#004797] font-bold";
      }}
    }}

    // Time Simulator (10:00 AM vs 10:45 PM Cierre)
    function setTimeMode(mode) {{
      playChime('click');
      const btnDay = document.getElementById('btn-time-day');
      const btnNight = document.getElementById('btn-time-night');
      const phoneClock = document.getElementById('phone-clock');
      const countdown = document.getElementById('countdown-timer');
      const mascotSpeech = document.getElementById('mascot-speech');
      const mascotBadge = document.getElementById('mascot-badge');
      const mascotCard = document.getElementById('mascot-card');
      const mascotFace = document.getElementById('mascot-face');

      if (mode === 'day') {{
        btnDay.className = "px-2.5 py-1 rounded-lg font-bold bg-slate-900 text-white text-[11px] transition-all";
        btnNight.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        phoneClock.textContent = "10:00 AM";
        countdown.textContent = "13h : 59m : 12s";
        countdown.className = "font-mono-data font-bold text-amber-300 bg-black/30 px-2 py-0.5 rounded text-[11px]";
        mascotSpeech.innerHTML = '“Tienes <strong>2 cuentas en Riesgo Crítico</strong> hoy. ¡Gestiona en 1 toque o escala antes de las 11:59&nbsp;PM para no perder tu racha!”';
        mascotBadge.textContent = "En marcha";
        mascotBadge.className = "text-[10px] font-bold px-2 py-0.2 rounded-full bg-blue-100 text-[#004797]";
        mascotCard.className = "m-3 p-3.5 rounded-2xl bg-white border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all";
        mascotFace.textContent = "🧔‍♂️";
      }} else {{
        btnNight.className = "px-2.5 py-1 rounded-lg font-bold bg-rose-600 text-white text-[11px] transition-all";
        btnDay.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        phoneClock.textContent = "10:45 PM";
        countdown.textContent = "01h : 14m : 08s";
        countdown.className = "font-mono-data font-bold text-rose-200 bg-rose-900 px-2 py-0.5 rounded text-[11px] animate-pulse";
        mascotSpeech.innerHTML = '“¡EMERGENCIA DE FRAGUADO! 😱 Quedan solo <strong>74 minutos</strong>. Si no gestionas a Constructora Bolívar y Ferretería El Constructor, ¡perderás tus 21 días de racha!”';
        mascotBadge.textContent = "⚠️ MODO INTENSO";
        mascotBadge.className = "text-[10px] font-extrabold px-2 py-0.2 rounded-full bg-rose-600 text-white animate-bounce";
        mascotCard.className = "m-3 p-3.5 rounded-2xl bg-gradient-to-r from-red-50 to-orange-50 border-2 border-rose-400 shadow-md flex items-center space-x-3.5 transition-all";
        mascotFace.textContent = "😱";
        showToast("⚠️ Modo Intenso: 74 minutos para corte de medianoche", "danger");
      }}
    }}

    // Filter Clients by Channel
    function filterClients(channel) {{
      playChime('click');
      const cards = document.querySelectorAll('.client-card');
      const tabAll = document.getElementById('tab-all');
      const tabInd = document.getElementById('tab-industrial');
      const tabTrad = document.getElementById('tab-tradicional');

      tabAll.className = "px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 text-[11px] transition-all";
      tabInd.className = "px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 text-[11px] transition-all";
      tabTrad.className = "px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 text-[11px] transition-all";

      if (channel === 'all') {{
        tabAll.className = "px-3 py-1 font-bold rounded-lg bg-[#004797] text-white text-[11px] transition-all";
        cards.forEach(c => c.classList.remove('hidden'));
      }} else if (channel === 'industrial') {{
        tabInd.className = "px-3 py-1 font-bold rounded-lg bg-[#004797] text-white text-[11px] transition-all";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'industrial') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }} else if (channel === 'tradicional') {{
        tabTrad.className = "px-3 py-1 font-bold rounded-lg bg-[#004797] text-white text-[11px] transition-all";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'tradicional') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }}
    }}

    // Expandable Client Timeline
    function toggleTimeline(id) {{
      playChime('click');
      const panel = document.getElementById('timeline-panel-' + id);
      const chevron = document.getElementById('timeline-chevron-' + id);
      if (panel.classList.contains('hidden')) {{
        panel.classList.remove('hidden');
        chevron.textContent = "▲";
      }} else {{
        panel.classList.add('hidden');
        chevron.textContent = "▼";
      }}
    }}

    // GPS Check-in Simulation
    function realizarCheckinGPS(id, name) {{
      playChime('gps');
      const card = document.getElementById('card-client-' + id);
      showToast("📡 Localizando coordenadas GPS en obra...", "info");

      setTimeout(() => {{
        playChime('streak');
        if (card) {{
          card.classList.remove('border-rose-300');
          card.classList.add('border-emerald-300', 'bg-emerald-50/20');
          const badge = card.querySelector('.bg-rose-50');
          if (badge) {{
            badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded-md border border-emerald-300";
            badge.innerHTML = "<span>📍 CHECK-IN VALIDADO (En Obra)</span>";
          }}
        }}

        currentStreak = 22;
        document.getElementById('streak-days').textContent = currentStreak;

        const speech = document.getElementById('mascot-speech');
        const face = document.getElementById('mascot-face');
        face.textContent = "🤠";
        speech.innerHTML = '“¡Check-in en obra confirmado por GPS! 📍 Visita física registrada y <strong>racha subió a 22 días 🔥</strong>.”';

        showToast("📍 Check-in verificado. ¡Racha salvada hoy!", "success");
      }}, 800);
    }}

    // WhatsApp Live Simulator
    function abrirWhatsAppSimulado(client, pedido) {{
      playChime('click');
      document.getElementById('wa-contact-name').textContent = client;
      document.getElementById('wa-sent-text').textContent = `“Estimado cliente, un saludo cordial desde Ultracem. Le confirmamos la programación prioritaria de ${{pedido}} con entrega programada y certificados NTC 121 incluidos.”`;
      document.getElementById('modal-whatsapp').classList.remove('hidden');
    }}

    function enviarMensajeWASimulado() {{
      playChime('click');
      const input = document.getElementById('wa-input');
      const container = document.getElementById('wa-messages-container');
      if (!input.value) return;

      const newMsg = document.createElement('div');
      newMsg.className = "flex justify-end";
      newMsg.innerHTML = `
        <div class="bg-[#DCF8C6] p-2.5 rounded-xl rounded-tr-none shadow-xs max-w-[85%] text-slate-900">
          <p>${{input.value}}</p>
          <span class="text-[9px] text-emerald-800 block text-right mt-1">10:16 AM ✓✓</span>
        </div>
      `;
      container.appendChild(newMsg);
      input.value = "";
      container.scrollTop = container.scrollHeight;

      setTimeout(() => {{
        playChime('streak');
        const reply = document.createElement('div');
        reply.className = "flex justify-start";
        reply.innerHTML = `
          <div class="bg-white p-2.5 rounded-xl rounded-tl-none shadow-xs max-w-[85%] text-slate-800">
            <p>¡Listo Carlos! Autorizado. Despáchame a primera hora. Muchas gracias por el seguimiento rápido.</p>
            <span class="text-[9px] text-slate-400 block text-right mt-1">10:16 AM</span>
          </div>
        `;
        container.appendChild(reply);
        container.scrollTop = container.scrollHeight;
        showToast("💬 ¡Cliente respondió positivamente por WhatsApp!", "success");
      }}, 1200);
    }}

    // Casco Protector 24h Freeze Shield
    function activarCascoProtector24h() {{
      if (cascosDisponibles <= 0) {{
        alert("Ya has consumido tus cascos protectores. Mantén una racha de 7 días para desbloquear uno nuevo.");
        return;
      }}

      playChime('freeze');
      isShieldActive = true;
      cascosDisponibles--;

      document.getElementById('header-casco-count').textContent = "0 Cascos";
      document.getElementById('shield-status-badge').textContent = "❄️ ESCUDO ACTIVO 24H";
      document.getElementById('shield-status-badge').className = "bg-sky-500 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-full animate-pulse";

      const card = document.getElementById('shield-inventory-card');
      card.className = "freeze-glow text-white rounded-3xl p-4 shadow-lg relative overflow-hidden transition-all duration-300";

      const btn = document.getElementById('btn-activate-shield');
      btn.innerHTML = "<span>🛡️ Racha Congelada por 24 Horas</span>";
      btn.disabled = true;
      btn.className = "mt-3 w-full bg-white/20 backdrop-blur-md text-white font-black py-2.5 rounded-2xl text-xs cursor-default";

      // Mascot puts on Golden Helmet & freezes
      const mascotFace = document.getElementById('mascot-face');
      const mascotSpeech = document.getElementById('mascot-speech');
      const mascotCard = document.getElementById('mascot-card');
      mascotFace.textContent = "🥶";
      mascotSpeech.innerHTML = '“¡MODO FRAGUADO PROTEGIDO! 🧊 Te has equipado el <strong>Casco Protector</strong>. Tu racha de 21 días queda congelada por 24 horas ante emergencias. ¡Descansa seguro!”';
      mascotCard.className = "m-3 p-3.5 rounded-2xl bg-sky-50 border-2 border-sky-400 shadow-sm flex items-center space-x-3.5 transition-all";

      showToast("❄️ ¡Casco Protector activado! Racha congelada 24h", "info");
    }}

    // Trophy Detail Modal
    function verDetalleTrofeo(title, desc, icon, xp) {{
      playChime('click');
      document.getElementById('trofeo-modal-title').textContent = title;
      document.getElementById('trofeo-modal-desc').textContent = desc;
      document.getElementById('trofeo-modal-icon').textContent = icon;
      document.getElementById('trofeo-modal-xp').textContent = xp + " Comercial";
      document.getElementById('modal-trofeo').classList.remove('hidden');
    }}

    // Modal Handlers
    function openModalSeguimiento(id, name) {{
      playChime('click');
      currentActiveClientId = id;
      document.getElementById('modal-seg-title').textContent = "Seguimiento: " + name;
      document.getElementById('modal-seguimiento').classList.remove('hidden');
    }}

    function openModalEscalamiento(id, name) {{
      playChime('click');
      currentActiveClientId = id;
      document.getElementById('modal-esc-title').textContent = "Escalar: " + name;
      document.getElementById('esc-motivo').value = id === 1 
        ? "El cliente solicita certificados de calidad y curva de resistencia NTC 121 de Cemento Estructural antes de autorizar despacho."
        : "Ferretería solicita aprobación de cupo de $20M para pedido de 45 ton.";
      document.getElementById('modal-escalamiento').classList.remove('hidden');
    }}

    function openModalCopiloto(id, name, type) {{
      playChime('click');
      currentActiveClientId = id;
      document.getElementById('copiloto-client-name').textContent = "Copiloto IA: " + name;
      document.getElementById('modal-copiloto').classList.remove('hidden');
      if (type === 'industrial') {{
        document.getElementById('prod-selector').value = 'estructural';
        actualizarFichaTecnica();
      }} else {{
        document.getElementById('prod-selector').value = 'general';
        actualizarFichaTecnica();
      }}
    }}

    function closeModal(id) {{
      playChime('click');
      document.getElementById(id).classList.add('hidden');
    }}

    // Actions that save streak
    function completarSeguimiento(tipo) {{
      playChime('streak');
      closeModal('modal-seguimiento');
      
      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-rose-300');
        card.classList.add('border-emerald-300', 'bg-emerald-50/20');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded-md border border-emerald-300";
          badge.innerHTML = "<span>🟢 GESTIONADO HOY (Racha Salvada)</span>";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      const face = document.getElementById('mascot-face');
      face.textContent = "🥳";
      speech.innerHTML = '“¡EXCELENTE GESTIÓN! 🔥 Has contactado al cliente a tiempo. <strong>Tu racha subió a 22 días</strong>. ¡El cemento fragua con disciplina!”';
      
      showToast("🎉 ¡Gestión registrada! Racha protegida: 22 Días 🔥", "success");
    }}

    function confirmarEscalamiento() {{
      playChime('streak');
      closeModal('modal-escalamiento');

      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-rose-300');
        card.classList.add('border-blue-300', 'bg-blue-50/20');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-[#004797] bg-blue-100 px-2 py-0.5 rounded-md border border-blue-300";
          badge.innerHTML = "<span>🛡️ ESCALADO A DEPTO (SLA ACTIVO)</span>";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      const face = document.getElementById('mascot-face');
      face.textContent = "😎";
      speech.innerHTML = '“¡Gran jugada! 🛡️ Escalaste el ticket con SLA. La responsabilidad ahora es del departamento y <strong>tu racha de 22 días está blindada</strong>.”';

      showToast("🛡️ Ticket transferido con éxito. ¡Racha blindada hoy!", "success");
    }}

    // Copilot Tabs
    function switchCopilotoTab(tabIndex) {{
      playChime('click');
      for (let i = 1; i <= 3; i++) {{
        document.getElementById('cop-tab-' + i).className = i === tabIndex 
          ? "btn-tactile pb-2 px-3 font-extrabold text-[#004797] border-b-2 border-[#004797]" 
          : "btn-tactile pb-2 px-3 font-medium text-slate-500 hover:text-slate-800";
        document.getElementById('cop-panel-' + i).className = i === tabIndex ? "space-y-3 text-xs" : "hidden space-y-3 text-xs";
      }}
    }}

    function simularVoz() {{
      playChime('click');
      const input = document.getElementById('cop-voice-input');
      input.value = "Hablé con Don Pedro, necesita 45 ton de Cemento Uso General urgente para el viernes en la mañana.";
      showToast("🎙️ Voz transcribiendo en tiempo real…", "info");
    }}

    function generarMinutaIA() {{
      playChime('streak');
      const output = document.getElementById('cop-whatsapp-text');
      output.textContent = `“Buenas tardes Don Pedro, un gusto saludarlo desde Ultracem. Le confirmo la coordinación de las 45 Toneladas de Cemento Uso General NTC 121 para entrega prioritaria este viernes en su bodega principal antes de las 12:00 PM. Despacho programado. ¡Muchas gracias!”`;
      showToast("✨ Minuta y mensaje WhatsApp redactados por IA", "success");
    }}

    function copiarAlPortapapeles() {{
      const text = document.getElementById('cop-whatsapp-text').textContent;
      navigator.clipboard.writeText(text).then(() => {{
        const btn = document.getElementById('btn-copy');
        btn.innerHTML = "<span>✅ ¡Copiado!</span>";
        setTimeout(() => {{ btn.innerHTML = "<span>📋 Copiar</span>"; }}, 2000);
        showToast("📋 Texto copiado para enviar por WhatsApp", "info");
      }}).catch(() => {{
        showToast("Texto listo para compartir", "info");
      }});
    }}

    const fichasData = {{
      estructural: {{
        nombre: "Cemento Estructural Tipo ART (NTC 121)",
        desc: "Diseñado para estructuras de concreto reforzado que demandan altas resistencias tempranas. Ideal para desencofrado rápido.",
        res: "≥ 28.0 MPa a 28 días (20 MPa a 3 días)",
        frag: "≥ 45 min inicial / ≤ 375 min final"
      }},
      general: {{
        nombre: "Cemento Uso General Tipo UG (NTC 121)",
        desc: "Ideal para mampostería, pañetes, morteros de pega, pisos y reparaciones en general en todo tipo de ferreterías.",
        res: "≥ 20.6 MPa a 28 días",
        frag: "≥ 45 min inicial / ≤ 420 min final"
      }},
      marino: {{
        nombre: "Cemento Marino Resistente a Sulfatos (MRS)",
        desc: "Formulado para cimentaciones en suelos agresivos, obras portuarias y muelles en ambiente marino del Caribe.",
        res: "≥ 25.0 MPa a 28 días",
        frag: "Resistencia química comprobada NTC 121"
      }},
      blanco: {{
        nombre: "Cemento Blanco Ultracem",
        desc: "Acabados arquitectónicos de alta gama, morteros decorativos y terrazos.",
        res: "≥ 22.0 MPa a 28 días",
        frag: "Blancura superior al 85%"
      }}
    }};

    function actualizarFichaTecnica() {{
      const sel = document.getElementById('prod-selector').value;
      const data = fichasData[sel];
      if (data) {{
        document.getElementById('ficha-nombre').textContent = data.nombre;
        document.getElementById('ficha-desc').textContent = data.desc;
        document.getElementById('ficha-resistencia').textContent = data.res;
        document.getElementById('ficha-fraguado').textContent = data.frag;
      }}
    }}

    function showToast(msg, type) {{
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      const bg = type === 'success' ? 'bg-emerald-800 text-white' 
               : type === 'danger' ? 'bg-rose-800 text-white' 
               : 'bg-slate-900 text-white';
      toast.className = `${{bg}} px-4 py-3 rounded-2xl shadow-xl border border-white/10 text-xs font-semibold flex items-center space-x-2 pointer-events-auto transition-all transform duration-200 translate-y-2 opacity-0`;
      toast.innerHTML = `<span>${{msg}}</span>`;
      container.appendChild(toast);
      
      requestAnimationFrame(() => {{
        toast.classList.remove('translate-y-2', 'opacity-0');
      }});

      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => {{ toast.remove(); }}, 3000);
      }}, 3500);
    }}
  </script>

</body>
</html>'''

dest_index = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\index.html"
with open(dest_index, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Compiled: {dest_index}")

dest_artifact = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
with open(dest_artifact, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Compiled: {dest_artifact}")
