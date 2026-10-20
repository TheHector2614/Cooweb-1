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
  
  <!-- Typography: Plus Jakarta Sans for Headers + Inter for UI -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --brand-blue: #004797;
      --brand-blue-dark: #002D62;
      --brand-green: #009639;
      --brand-orange: #FF6B00;
      --surface-concrete: #F8FAFC;
    }}
    
    body {{
      font-family: 'Plus Jakarta Sans', 'Inter', system-ui, -apple-system, sans-serif;
      background-color: var(--surface-concrete);
    }}
    
    .font-ui {{
      font-family: 'Inter', system-ui, sans-serif;
    }}
    
    .tabular-nums {{
      font-variant-numeric: tabular-nums;
    }}
    
    .text-balance {{
      text-wrap: balance;
    }}
    
    /* Taste Skill: Refined Flame Animation */
    @keyframes pulse-flame {{
      0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 4px rgba(255, 107, 0, 0.5)); }}
      50% {{ transform: scale(1.12) rotate(3deg); filter: drop-shadow(0 0 10px rgba(255, 107, 0, 0.85)); }}
    }}
    .flame-anim {{
      display: inline-block;
      animation: pulse-flame 1.6s infinite ease-in-out;
      transform-origin: bottom center;
    }}
    
    /* Gentle Character Bob */
    @keyframes bob-character {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-4px); }}
    }}
    .bob-anim {{
      animation: bob-character 2.4s infinite ease-in-out;
    }}
    
    /* Vercel Guidelines: Strict Reduced Motion */
    @media (prefers-reduced-motion: reduce) {{
      *, ::before, ::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}
    
    /* Tactile button active push */
    .btn-tactile:active {{
      transform: translateY(1px);
    }}
    
    /* Custom refined scrollbars */
    ::-webkit-scrollbar {{
      width: 5px;
      height: 5px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen flex flex-col selection:bg-blue-100 selection:text-blue-900">

  <!-- ============================================================== -->
  <!-- ACCESSIBILITY: SKIP LINK (Vercel Web Interface Guidelines)     -->
  <!-- ============================================================== -->
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-[#004797] focus:text-white focus:rounded-xl focus:shadow-lg focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-white text-xs font-bold">
    Saltar al contenido principal
  </a>

  <!-- ============================================================== -->
  <!-- TOP APP BAR & LIVE TEST CONTROLS (TASTE SKILL ANTI-SLOP)      -->
  <!-- ============================================================== -->
  <header class="bg-white border-b border-slate-200/80 sticky top-0 z-40 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex flex-wrap items-center justify-between gap-3">
      
      <!-- Brand & Project Identity -->
      <div class="flex items-center space-x-3.5">
        <img src="data:image/png;base64,{logo_base64}" alt="Logotipo Oficial Ultracem" class="h-8 w-auto object-contain" width="130" height="32" fetchpriority="high">
        <div class="h-5 w-px bg-slate-200" aria-hidden="true"></div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="font-extrabold text-slate-900 tracking-tight text-base sm:text-lg leading-none">
              Ultra<span class="text-[#FF6B00]">Racha</span>
            </h1>
            <span class="bg-orange-50 text-orange-800 text-[11px] px-2 py-0.5 rounded-full font-bold border border-orange-200/80">CRM Gamificado</span>
          </div>
          <p class="text-[11px] text-slate-500 font-ui hidden sm:block">Reto Bootcamp Semillero Cooweb • Ultracem</p>
        </div>
      </div>

      <!-- View Switcher & Simulation Controls -->
      <div class="flex items-center flex-wrap gap-2.5">
        
        <!-- View Toggle (Mobile Asesor vs Web Supervisor) -->
        <nav aria-label="Selector de Vistas" class="bg-slate-100 p-1 rounded-xl flex items-center border border-slate-200/70">
          <button id="btn-view-mobile" onclick="switchView('mobile')" aria-label="Cambiar a Vista Asesor Móvil" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#002D62] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797] focus-visible:outline-none">
            <span aria-hidden="true">📱</span>
            <span>Vista Asesor Móvil</span>
          </button>
          <button id="btn-view-web" onclick="switchView('web')" aria-label="Cambiar a Vista Dashboard Supervisor" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797] focus-visible:outline-none">
            <span aria-hidden="true">💻</span>
            <span>Dashboard Supervisor</span>
          </button>
        </nav>

        <!-- Time Mode Simulator (10:00 AM vs 10:45 PM Cierre) -->
        <div class="flex items-center space-x-1 bg-amber-50/80 border border-amber-200/80 px-2.5 py-1 rounded-xl">
          <span class="text-[11px] font-semibold text-amber-900">Hora:</span>
          <button id="btn-time-day" onclick="setTimeMode('day')" aria-label="Simular turno de día 10:00 AM" class="btn-tactile text-[11px] px-2.5 py-0.5 rounded-md font-bold bg-amber-500 text-white shadow-xs focus-visible:ring-2 focus-visible:ring-amber-600 focus-visible:outline-none">
            ☀️ 10:00 AM
          </button>
          <button id="btn-time-night" onclick="setTimeMode('night')" aria-label="Simular modo noche y alerta de cierre a las 10:45 PM" class="btn-tactile text-[11px] px-2 py-0.5 rounded-md font-semibold text-amber-900 hover:bg-amber-200/70 focus-visible:ring-2 focus-visible:ring-red-600 focus-visible:outline-none">
            🌙 10:45 PM
          </button>
        </div>

      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- MAIN CONTENT CONTAINER                                         -->
  <!-- ============================================================== -->
  <main id="main-content" class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 flex flex-col justify-center">

    <!-- ============================================================== -->
    <!-- 1. VISTA ASESOR COMERCIAL (MOBILE FIRST)                       -->
    <!-- ============================================================== -->
    <div id="view-mobile" class="w-full flex justify-center items-start">
      
      <!-- Phone Mockup Frame (iPhone Canvas) -->
      <div class="w-full max-w-md bg-white rounded-3xl shadow-xl border border-slate-300/80 overflow-hidden relative flex flex-col min-h-[790px]">
        
        <!-- Phone Top Status Bar -->
        <div class="bg-slate-900 pt-3 pb-2 px-6 flex justify-between items-center text-white text-[11px]">
          <span id="phone-clock" class="font-bold tracking-tight text-slate-200 tabular-nums font-mono">10:00 AM</span>
          <div class="w-18 h-3.5 bg-slate-800 rounded-full mx-auto" aria-hidden="true"></div>
          <div class="flex items-center space-x-1.5 text-slate-300 font-mono text-[10px]">
            <span>5G</span>
            <span class="text-emerald-400" aria-hidden="true">●</span>
            <span class="tabular-nums">98%</span>
          </div>
        </div>

        <!-- Mobile Header: Ultracem Brand, Streak Counter & Shield -->
        <div class="bg-gradient-to-r from-[#0033A0] to-[#004797] text-white p-4 relative overflow-hidden">
          <div class="flex items-center justify-between relative z-10">
            <div class="flex items-center space-x-3">
              <div class="relative">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Foto de perfil de Carlos Mendoza" class="w-11 h-11 rounded-full border-2 border-white object-cover shadow-xs" width="44" height="44">
                <span class="absolute -bottom-0.5 -right-0.5 bg-emerald-500 w-3 h-3 rounded-full border-2 border-[#0033A0]" title="Conectado en línea"></span>
              </div>
              <div>
                <h2 class="font-extrabold text-sm tracking-tight leading-tight">Carlos Mendoza</h2>
                <p class="text-[11px] text-blue-200 font-ui">Asesor Obras & Ferreterías • Caribe</p>
              </div>
            </div>

            <!-- Streak Counter Badge (Taste Skill Signature) -->
            <div class="bg-white/10 backdrop-blur-xs border border-white/20 rounded-2xl px-3.5 py-1.5 flex items-center space-x-2 shadow-xs" title="21 días consecutivos de racha">
              <span class="flame-anim text-xl" aria-hidden="true">🔥</span>
              <div class="text-right">
                <span id="streak-days" class="text-lg font-black text-amber-300 leading-none tabular-nums font-mono">21</span>
                <span class="text-[9px] text-white/90 block font-bold uppercase tracking-wider">Días</span>
              </div>
            </div>
          </div>

          <!-- Countdown and Casco Protector Shield -->
          <div class="mt-3.5 pt-2.5 border-t border-white/15 flex items-center justify-between text-xs font-ui">
            <div class="flex items-center space-x-1.5 text-blue-100">
              <span aria-hidden="true">⏱️</span>
              <span class="font-medium">Corte de Racha (11:59&nbsp;PM):</span>
              <span id="countdown-timer" aria-live="polite" class="font-mono font-bold text-amber-300 bg-black/30 px-2 py-0.5 rounded-md tabular-nums">13h : 59m : 12s</span>
            </div>
            
            <div class="flex items-center space-x-1 bg-amber-400/20 text-amber-200 border border-amber-300/40 px-2.5 py-0.5 rounded-full text-[11px] font-bold" title="Casco Protector: congela tu racha 24h ante emergencias de viaje o salud">
              <span aria-hidden="true">⛑️</span>
              <span>1 Casco</span>
            </div>
          </div>
        </div>

        <!-- Mascot Coach Card: Don Fraguado (SVG Vectorial Craft) -->
        <div id="mascot-card" class="m-3 p-3.5 rounded-2xl bg-blue-50/70 border border-blue-200/80 shadow-xs flex items-center space-x-3.5 transition-all duration-300">
          
          <!-- Vector Saco de Cemento "Don Fraguado" -->
          <div class="bob-anim flex-shrink-0 w-13 h-14 bg-gradient-to-br from-slate-200 to-slate-300 rounded-xl border border-slate-400 flex flex-col items-center justify-center shadow-xs relative" aria-label="Mascota Don Fraguado">
            <!-- White Hardhat with UC Logo -->
            <div class="absolute -top-2.5 w-10 h-4 bg-white rounded-t-full border border-slate-300 shadow-xs flex items-center justify-center">
              <span class="text-[6.5px] font-black text-[#004797] tracking-tighter">ULTRACEM</span>
            </div>
            <!-- Cyan Safety Goggles -->
            <div class="w-8 h-2.5 bg-cyan-600 rounded-full border border-cyan-800 flex items-center justify-around px-0.5 mt-1 shadow-inner">
              <span class="w-1.5 h-1.5 bg-white/90 rounded-full"></span>
              <span class="w-1.5 h-1.5 bg-white/90 rounded-full"></span>
            </div>
            <!-- Mustache / Friendly Smile -->
            <div class="text-[9px] leading-none mt-0.5 select-none" aria-hidden="true">🧔‍♂️</div>
            <!-- Ultracem Emblem -->
            <span class="text-[7.5px] font-black text-[#004797] tracking-tighter leading-none mt-0.5">50&nbsp;kg</span>
            <!-- Work Boots -->
            <div class="absolute -bottom-1 flex space-x-1" aria-hidden="true">
              <span class="w-2.5 h-1 bg-amber-800 rounded-xs"></span>
              <span class="w-2.5 h-1 bg-amber-800 rounded-xs"></span>
            </div>
          </div>

          <!-- Dialog Message -->
          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between">
              <strong class="text-xs font-extrabold text-[#004797] truncate">Don Fraguado</strong>
              <span id="mascot-badge" class="text-[10px] font-bold px-2 py-0.2 rounded-full bg-blue-100 text-[#004797]">En marcha</span>
            </div>
            <p id="mascot-speech" class="text-xs text-slate-700 mt-0.5 leading-snug font-medium font-ui">
              “¡Pilas Carlos! Tienes <strong>2 clientes en Riesgo Crítico</strong>. Gestiona o escala antes de las 11:59&nbsp;PM para blindar tus 21 días de racha. 🔥”
            </p>
          </div>
        </div>

        <!-- Monthly Toneladas Goal (Vercel Metrics Style) -->
        <div class="px-4 py-2 bg-white">
          <div class="flex justify-between items-center text-xs font-ui mb-1.5">
            <span class="text-slate-600 flex items-center space-x-1">
              <span aria-hidden="true">🏗️</span>
              <span class="font-medium">Meta del Mes:</span>
              <strong class="text-slate-900 font-bold tabular-nums">420 / 500&nbsp;Ton</strong>
            </span>
            <span class="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200 tabular-nums">84% alcanzado</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-2.5 overflow-hidden">
            <div class="bg-[#009639] h-full rounded-full transition-all duration-500" style="width: 84%"></div>
          </div>
        </div>

        <!-- Channel Filter Tabs (Ferreterías vs Obras) -->
        <div class="px-4 pt-2 pb-1 border-b border-slate-100 flex items-center justify-between text-xs font-ui">
          <div class="flex space-x-1" role="tablist" aria-label="Filtro por Canal">
            <button onclick="filterClients('all')" id="tab-all" role="tab" aria-selected="true" class="btn-tactile px-3 py-1 font-bold rounded-lg bg-[#004797] text-white shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]">Todos (4)</button>
            <button onclick="filterClients('industrial')" id="tab-industrial" role="tab" aria-selected="false" class="btn-tactile px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 focus-visible:ring-2 focus-visible:ring-[#004797]">🏢 Obras</button>
            <button onclick="filterClients('tradicional')" id="tab-tradicional" role="tab" aria-selected="false" class="btn-tactile px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100 focus-visible:ring-2 focus-visible:ring-[#004797]">🏪 Ferreterías</button>
          </div>
          <span class="text-[11px] text-slate-400 font-semibold">Prioridad Riesgo</span>
        </div>

        <!-- Client List (Scrollable Cards - No Nested Boxes) -->
        <div class="flex-1 overflow-y-auto p-3 space-y-3 bg-slate-50">

          <!-- CLIENT 1: Constructora Bolívar (Rojo Crítico) -->
          <article id="card-client-1" class="bg-white rounded-2xl p-4 border-2 border-red-300 shadow-xs client-card transition-all" data-channel="industrial" data-status="danger">
            <div class="flex justify-between items-start gap-2">
              <div class="min-w-0">
                <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                  <span class="bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider">🏢 Industrial / Obra</span>
                  <span class="bg-red-100 text-red-800 text-[10px] font-extrabold px-2 py-0.5 rounded-md border border-red-300 flex items-center space-x-1">
                    <span class="w-2 h-2 rounded-full bg-red-600 animate-ping" aria-hidden="true"></span>
                    <span>🔴 8 DÍAS SIN CONTACTO</span>
                  </span>
                </div>
                <h3 class="font-extrabold text-slate-900 text-sm mt-1 text-balance">Constructora Bolívar — Torre del Mar</h3>
                <p class="text-xs text-slate-500 font-ui">Ing. Andrés Meza • 120&nbsp;Ton Cemento Estructural</p>
              </div>
              <span class="text-xs font-extrabold text-slate-900 bg-slate-100 px-2 py-1 rounded-lg tabular-nums">$54M</span>
            </div>

            <!-- Risk Warning Box -->
            <div class="mt-2.5 bg-red-50/80 border border-red-200 rounded-xl p-2.5 flex items-start space-x-2 text-xs text-red-900 font-ui">
              <span class="text-sm select-none" aria-hidden="true">⚠️</span>
              <div>
                <strong class="font-bold block">Cotización vence hoy a las 5:00&nbsp;PM</strong>
                <span>Requieren confirmación de pruebas de resistencia antes de autorizar despacho.</span>
              </div>
            </div>

            <!-- Action Buttons (1-Click) -->
            <div class="mt-3 grid grid-cols-3 gap-1.5">
              <button onclick="openModalSeguimiento(1, 'Constructora Bolívar')" aria-label="Registrar seguimiento para Constructora Bolívar" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-emerald-700 focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>📞</span><span>Registrar</span></span>
                <span class="text-[9px] text-emerald-100 font-medium">Seguimiento</span>
              </button>
              
              <button onclick="openModalEscalamiento(1, 'Constructora Bolívar')" aria-label="Escalar caso de Constructora Bolívar a departamento con SLA" class="btn-tactile bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-amber-700 focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>🚨</span><span>Escalar</span></span>
                <span class="text-[9px] text-amber-100 font-medium">A Depto (SLA)</span>
              </button>

              <button onclick="openModalCopiloto(1, 'Constructora Bolívar', 'industrial')" aria-label="Abrir Copiloto IA para Constructora Bolívar" class="btn-tactile bg-[#004797] hover:bg-blue-900 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-[#004797] focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>✨</span><span>Copiloto</span></span>
                <span class="text-[9px] text-blue-200 font-medium">Ficha & RAG</span>
              </button>
            </div>
          </article>

          <!-- CLIENT 2: Ferretería El Constructor (Rojo Crítico) -->
          <article id="card-client-2" class="bg-white rounded-2xl p-4 border-2 border-red-300 shadow-xs client-card transition-all" data-channel="tradicional" data-status="danger">
            <div class="flex justify-between items-start gap-2">
              <div class="min-w-0">
                <div class="flex items-center space-x-1.5 flex-wrap gap-y-1">
                  <span class="bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-md uppercase tracking-wider">🏪 Tradicional / Depósito</span>
                  <span class="bg-red-100 text-red-800 text-[10px] font-extrabold px-2 py-0.5 rounded-md border border-red-300">
                    🔴 5 DÍAS SIN CONTACTO
                  </span>
                </div>
                <h3 class="font-extrabold text-slate-900 text-sm mt-1 text-balance">Ferretería & Depósito El Constructor</h3>
                <p class="text-xs text-slate-500 font-ui">Don Pedro Gómez • 45&nbsp;Ton Cemento Uso General</p>
              </div>
              <span class="text-xs font-extrabold text-slate-900 bg-slate-100 px-2 py-1 rounded-lg tabular-nums">$19M</span>
            </div>

            <div class="mt-2.5 bg-red-50/80 border border-red-200 rounded-xl p-2.5 flex items-start space-x-2 text-xs text-red-900 font-ui">
              <span class="text-sm select-none" aria-hidden="true">🚨</span>
              <div>
                <strong class="font-bold block">Riesgo inminente de compra a la competencia</strong>
                <span>Rotación semanal agotada. Si no se gestiona hoy, comprará a Argos o Cemex.</span>
              </div>
            </div>

            <div class="mt-3 grid grid-cols-3 gap-1.5">
              <button onclick="openModalSeguimiento(2, 'Ferretería El Constructor')" aria-label="Registrar seguimiento para Ferretería El Constructor" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-emerald-700 focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>📞</span><span>Registrar</span></span>
                <span class="text-[9px] text-emerald-100 font-medium">Seguimiento</span>
              </button>
              
              <button onclick="openModalEscalamiento(2, 'Ferretería El Constructor')" aria-label="Escalar caso de Ferretería El Constructor a departamento" class="btn-tactile bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-amber-700 focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>🚨</span><span>Escalar</span></span>
                <span class="text-[9px] text-amber-100 font-medium">A Depto (SLA)</span>
              </button>

              <button onclick="openModalCopiloto(2, 'Ferretería El Constructor', 'tradicional')" aria-label="Abrir Copiloto IA para Ferretería El Constructor" class="btn-tactile bg-[#004797] hover:bg-blue-900 text-white text-xs font-bold py-2 px-1 rounded-xl shadow-xs flex flex-col items-center justify-center transition-all focus-visible:ring-2 focus-visible:ring-[#004797] focus-visible:outline-none">
                <span class="flex items-center space-x-1"><span>✨</span><span>Copiloto</span></span>
                <span class="text-[9px] text-blue-200 font-medium">Minuta & WA</span>
              </button>
            </div>
          </article>

          <!-- CLIENT 3: Consorcio Vías del Magdalena (Amarillo Advertencia) -->
          <article id="card-client-3" class="bg-white rounded-2xl p-4 border border-amber-300 shadow-xs client-card" data-channel="industrial" data-status="warning">
            <div class="flex justify-between items-start">
              <div>
                <div class="flex items-center space-x-1.5">
                  <span class="bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-md uppercase">🏢 Industrial</span>
                  <span class="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-amber-300">
                    🟡 6 DÍAS SIN CONTACTO
                  </span>
                </div>
                <h3 class="font-extrabold text-slate-900 text-sm mt-1 text-balance">Consorcio Vías del Magdalena</h3>
                <p class="text-xs text-slate-500 font-ui">Ing. Laura Peña • 250&nbsp;Ton Concreto Estructural</p>
              </div>
              <span class="text-xs font-bold text-slate-800 bg-slate-100 px-2 py-1 rounded-lg tabular-nums">$112M</span>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-500 font-ui">
              <span>Próxima fundida: Lunes 7:00&nbsp;AM</span>
              <button onclick="openModalSeguimiento(3, 'Consorcio Vías')" class="text-[#004797] font-bold hover:underline">Gestionar anticipado →</button>
            </div>
          </article>

          <!-- CLIENT 4: Depósito Central La 30 (Verde Saludable) -->
          <article id="card-client-4" class="bg-white rounded-2xl p-4 border border-emerald-300 shadow-xs client-card opacity-85" data-channel="tradicional" data-status="healthy">
            <div class="flex justify-between items-start">
              <div>
                <div class="flex items-center space-x-1.5">
                  <span class="bg-slate-100 text-slate-700 text-[10px] font-bold px-2 py-0.5 rounded-md uppercase">🏪 Ferretería</span>
                  <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-md border border-emerald-300">
                    🟢 AL DÍA (Contacto hace 1 día)
                  </span>
                </div>
                <h3 class="font-extrabold text-slate-900 text-sm mt-1 text-balance">Depósito Central La 30</h3>
                <p class="text-xs text-slate-500 font-ui">30&nbsp;Ton despachadas en Tractomula #4</p>
              </div>
              <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-1 rounded-lg">✅ Al Día</span>
            </div>
          </article>

        </div>

        <!-- Phone Bottom Navigation Bar -->
        <nav aria-label="Navegación Móvil" class="bg-white border-t border-slate-200/80 px-6 py-2.5 flex justify-around items-center text-xs">
          <button class="flex flex-col items-center text-[#004797] font-bold" aria-current="page">
            <span class="text-lg" aria-hidden="true">🔥</span>
            <span class="text-[10px] font-ui">UltraRacha</span>
          </button>
          <button onclick="openModalCopiloto(1, 'Asistente Global', 'general')" class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <span class="text-lg" aria-hidden="true">✨</span>
            <span class="text-[10px] font-ui">Copiloto IA</span>
          </button>
          <button onclick="switchView('web')" class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <span class="text-lg" aria-hidden="true">🏆</span>
            <span class="text-[10px] font-ui">Ranking Liga</span>
          </button>
          <button class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <span class="text-lg" aria-hidden="true">👤</span>
            <span class="text-[10px] font-ui">Mi Perfil</span>
          </button>
        </nav>

      </div>
    </div>


    <!-- ============================================================== -->
    <!-- 2. VISTA DASHBOARD SUPERVISOR (WEB / PC EXECUTIVE)             -->
    <!-- ============================================================== -->
    <div id="view-web" class="hidden w-full space-y-6">
      
      <!-- Top Supervisor Banner (Taste Skill Layout) -->
      <div class="bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div class="flex items-center space-x-3">
            <span class="bg-blue-50 text-[#004797] text-xs font-extrabold px-3 py-1 rounded-full uppercase tracking-wider border border-blue-200/60">Centro de Mando Comercial</span>
            <span class="text-xs text-slate-300" aria-hidden="true">•</span>
            <span class="text-xs text-slate-500 font-medium font-ui">Regional Caribe & Obras Especiales</span>
          </div>
          <h2 class="text-2xl font-black text-slate-900 tracking-tight mt-1 text-balance">Supervisión Ejecutiva UltraRacha</h2>
          <p class="text-sm text-slate-600 font-ui">Monitoreo en tiempo real de toneladas, rachas y resolución de bloqueos con SLA.</p>
        </div>

        <!-- Supervisor Profile -->
        <div class="flex items-center space-x-3.5">
          <div class="text-right hidden sm:block">
            <p class="text-xs text-slate-400 font-ui">Líder Comercial</p>
            <p class="text-sm font-extrabold text-slate-900">Ing. Roberto Vega</p>
          </div>
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80" alt="Foto de Roberto Vega" class="w-12 h-12 rounded-2xl border-2 border-[#004797] object-cover shadow-xs" width="48" height="48">
        </div>
      </div>

      <!-- 4 Executive KPI Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- Metric 1: Toneladas Vendidas -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400 font-ui">Toneladas del Mes</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 tabular-nums">3,420 <span class="text-sm font-medium text-slate-500">/ 3,750&nbsp;Ton</span></h3>
            <span class="text-xs font-bold text-emerald-600 flex items-center space-x-1 mt-1 font-ui">
              <span>↑ 91.2% de la meta</span>
              <span class="text-[11px] text-slate-400">(Faltan 330&nbsp;Ton)</span>
            </span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-[#004797] flex items-center justify-center text-2xl font-black" aria-hidden="true">
            🏗️
          </div>
        </div>

        <!-- Metric 2: Tasa de Seguimiento Oportuno -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400 font-ui">Seguimiento a Tiempo</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 tabular-nums">94.8%</h3>
            <span class="text-xs font-bold text-emerald-600 flex items-center space-x-1 mt-1 font-ui">
              <span>↑ +6.2%</span>
              <span class="text-[11px] text-slate-400">vs mes anterior</span>
            </span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-emerald-50 text-emerald-700 flex items-center justify-center text-2xl" aria-hidden="true">
            ⏱️
          </div>
        </div>

        <!-- Metric 3: Cuentas Críticas Salvadas Hoy -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400 font-ui">Críticos Salvados Hoy</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 tabular-nums">23 <span class="text-sm font-medium text-slate-500">/ 24</span></h3>
            <span class="text-xs font-bold text-amber-600 flex items-center space-x-1 mt-1 font-ui">
              <span>⚠️ Solo 1 pendiente</span>
              <span class="text-[11px] text-slate-400">antes de 11:59&nbsp;PM</span>
            </span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-amber-50 text-amber-700 flex items-center justify-center text-2xl" aria-hidden="true">
            🔥
          </div>
        </div>

        <!-- Metric 4: Casos Escalados Activos -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs flex items-center justify-between">
          <div>
            <p class="text-xs font-bold uppercase tracking-wider text-slate-400 font-ui">Casos Escalados (SLA)</p>
            <h3 class="text-2xl font-black text-slate-900 mt-1 tabular-nums">6 Activos</h3>
            <span class="text-xs font-bold text-emerald-600 flex items-center space-x-1 mt-1 font-ui">
              <span>✅ 100% en tiempo SLA</span>
              <span class="text-[11px] text-slate-400">(0 vencidos)</span>
            </span>
          </div>
          <div class="w-12 h-12 rounded-2xl bg-indigo-50 text-indigo-700 flex items-center justify-center text-2xl" aria-hidden="true">
            🚨
          </div>
        </div>

      </div>

      <!-- Main Columns: Leaderboard & Escalation SLA Audit Table -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left: Leaderboard "Liga Maestros Ultracem" -->
        <section aria-labelledby="leaderboard-title" class="lg:col-span-5 bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs flex flex-col">
          <div class="flex justify-between items-center mb-4">
            <div>
              <h3 id="leaderboard-title" class="text-lg font-black text-slate-900 flex items-center space-x-2">
                <span aria-hidden="true">🏆</span>
                <span>Liga Maestros Ultracem</span>
              </h3>
              <p class="text-xs text-slate-500 font-ui">Ranking por constancia diaria (Racha) y volumen</p>
            </div>
            <span class="bg-amber-100 text-amber-800 text-xs font-bold px-2.5 py-0.5 rounded-full">División Clinker Oro</span>
          </div>

          <div class="space-y-3 flex-1 overflow-y-auto pr-1">
            
            <!-- Rank 1: Carlos Mendoza -->
            <div class="p-3.5 rounded-2xl bg-amber-50/70 border border-amber-200 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-amber-600 w-6 text-center select-none" aria-hidden="true">🥇</span>
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-10 h-10 rounded-full border-2 border-amber-400 object-cover" width="40" height="40">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Carlos Mendoza</h4>
                  <p class="text-xs text-slate-500 font-ui">Caribe • 420&nbsp;Ton cerradas</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-amber-600 flex items-center justify-end space-x-1 tabular-nums">
                  <span>21 Días</span>
                  <span aria-hidden="true">🔥</span>
                </span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md font-ui">Al día ✅</span>
              </div>
            </div>

            <!-- Rank 2: Andrea Polo -->
            <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-slate-400 w-6 text-center select-none" aria-hidden="true">🥈</span>
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Andrea Polo" class="w-10 h-10 rounded-full border border-slate-300 object-cover" width="40" height="40">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Andrea Polo</h4>
                  <p class="text-xs text-slate-500 font-ui">Cartagena • 395&nbsp;Ton cerradas</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-slate-700 flex items-center justify-end space-x-1 tabular-nums">
                  <span>19 Días</span>
                  <span aria-hidden="true">🔥</span>
                </span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md font-ui">Al día ✅</span>
              </div>
            </div>

            <!-- Rank 3: Javier Restrepo -->
            <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xl font-black text-amber-800 w-6 text-center select-none" aria-hidden="true">🥉</span>
                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Javier Restrepo" class="w-10 h-10 rounded-full border border-slate-300 object-cover" width="40" height="40">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Javier Restrepo</h4>
                  <p class="text-xs text-slate-500 font-ui">Barranquilla • 360&nbsp;Ton</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-slate-700 flex items-center justify-end space-x-1 tabular-nums">
                  <span>15 Días</span>
                  <span aria-hidden="true">🔥</span>
                </span>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md font-ui">Al día ✅</span>
              </div>
            </div>

            <!-- Rank 4: Felipe Castro (Riesgo de perder racha) -->
            <div class="p-3.5 rounded-2xl bg-red-50/40 border border-red-200 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-sm font-black text-slate-400 w-6 text-center tabular-nums">4</span>
                <img src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=80&auto=format&fit=crop&q=80" alt="Felipe Castro" class="w-10 h-10 rounded-full border border-red-300 object-cover" width="40" height="40">
                <div>
                  <h4 class="font-extrabold text-sm text-slate-900">Felipe Castro</h4>
                  <p class="text-xs text-slate-500 font-ui">Santa Marta • 280&nbsp;Ton</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-sm font-black text-red-600 flex items-center justify-end space-x-1 tabular-nums">
                  <span>7 Días</span>
                  <span aria-hidden="true">⚠️</span>
                </span>
                <span class="text-[10px] bg-red-100 text-red-800 font-bold px-2 py-0.5 rounded-md font-ui">1 pendiente</span>
              </div>
            </div>

          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500 font-ui">
            <span>Premio: <strong>Bono Maestro + Trofeo Don Fraguado</strong></span>
            <button class="text-[#004797] font-bold hover:underline">Ver tabla completa (24) →</button>
          </div>
        </section>

        <!-- Right: Escalation SLA Audit Table -->
        <section aria-labelledby="audit-title" class="lg:col-span-7 bg-white rounded-3xl p-6 border border-slate-200/80 shadow-xs flex flex-col">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 mb-4">
            <div>
              <h3 id="audit-title" class="text-lg font-black text-slate-900 flex items-center space-x-2">
                <span aria-hidden="true">🚨</span>
                <span>Bandeja de Casos Escalados a Departamentos</span>
              </h3>
              <p class="text-xs text-slate-500 font-ui">El asesor protege su racha y la empresa resuelve cuellos de botella con SLA</p>
            </div>
            <span class="text-xs font-semibold bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full border border-emerald-200 font-ui">
              SLA Promedio: 1h 42m
            </span>
          </div>

          <!-- Table of Escalated Tickets -->
          <div class="flex-1 overflow-x-auto">
            <table class="w-full text-left text-xs font-ui">
              <thead class="bg-slate-50 text-slate-600 uppercase tracking-wider text-[10px] border-b border-slate-200">
                <tr>
                  <th scope="col" class="py-2.5 px-3">Ticket / Cliente</th>
                  <th scope="col" class="py-2.5 px-3">Depto Asignado</th>
                  <th scope="col" class="py-2.5 px-3">Asesor</th>
                  <th scope="col" class="py-2.5 px-3">Tiempo SLA</th>
                  <th scope="col" class="py-2.5 px-3 text-right">Acción</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                
                <!-- Ticket 1: Logística (Mixer) -->
                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3 px-3">
                    <strong class="font-bold text-slate-900 block">#TR-4091</strong>
                    <span class="text-slate-500">Consorcio Vías • Ruta Mixer</span>
                  </td>
                  <td class="py-3 px-3">
                    <span class="bg-blue-50 text-[#004797] font-bold px-2 py-0.5 rounded-md text-[11px] border border-blue-200">
                      🚚 Logística (SLA: 2&nbsp;h)
                    </span>
                  </td>
                  <td class="py-3 px-3 font-medium text-slate-700">Carlos Mendoza</td>
                  <td class="py-3 px-3">
                    <span class="font-mono font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded tabular-nums">01h : 14m</span>
                  </td>
                  <td class="py-3 px-3 text-right">
                    <button onclick="alert('Notificación de alta prioridad enviada al Jefe de Despachos de Planta Ultracem.')" aria-label="Acelerar ticket de logística" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-800 px-2.5 py-1 rounded-lg font-bold transition-all focus-visible:ring-2 focus-visible:ring-[#004797]">
                      Acelerar ⚡
                    </button>
                  </td>
                </tr>

                <!-- Ticket 2: Cartera (Cupo) -->
                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3 px-3">
                    <strong class="font-bold text-slate-900 block">#TR-4088</strong>
                    <span class="text-slate-500">Ferretería El Sol • Cupo $30M</span>
                  </td>
                  <td class="py-3 px-3">
                    <span class="bg-purple-50 text-purple-800 font-bold px-2 py-0.5 rounded-md text-[11px] border border-purple-200">
                      💳 Cartera (SLA: 4&nbsp;h)
                    </span>
                  </td>
                  <td class="py-3 px-3 font-medium text-slate-700">Andrea Polo</td>
                  <td class="py-3 px-3">
                    <span class="font-mono font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded tabular-nums">02h : 45m</span>
                  </td>
                  <td class="py-3 px-3 text-right">
                    <button onclick="alert('Notificación enviada al analista de Crédito y Cobranza.')" aria-label="Revisar ticket de cartera" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-800 px-2.5 py-1 rounded-lg font-bold transition-all focus-visible:ring-2 focus-visible:ring-[#004797]">
                      Revisar 🔍
                    </button>
                  </td>
                </tr>

                <!-- Ticket 3: Calidad y Soporte Técnico -->
                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3 px-3">
                    <strong class="font-bold text-slate-900 block">#TR-4082</strong>
                    <span class="text-slate-500">Constructora Bolívar • NTC 121</span>
                  </td>
                  <td class="py-3 px-3">
                    <span class="bg-teal-50 text-teal-800 font-bold px-2 py-0.5 rounded-md text-[11px] border border-teal-200">
                      🔬 Calidad (SLA: 6&nbsp;h)
                    </span>
                  </td>
                  <td class="py-3 px-3 font-medium text-slate-700">Carlos Mendoza</td>
                  <td class="py-3 px-3">
                    <span class="font-mono font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded tabular-nums">00h : 48m</span>
                  </td>
                  <td class="py-3 px-3 text-right">
                    <button onclick="alert('Certificado de ensayo de compresión reenviado al cliente.')" aria-label="Liberar ticket de calidad" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-800 px-2.5 py-1 rounded-lg font-bold transition-all focus-visible:ring-2 focus-visible:ring-[#004797]">
                      Liberar ✅
                    </button>
                  </td>
                </tr>

              </tbody>
            </table>
          </div>

          <!-- Impact Summary Footer -->
          <div class="mt-4 p-3 bg-slate-50 rounded-2xl border border-slate-200/80 flex items-center justify-between text-xs text-slate-600 font-ui">
            <div class="flex items-center space-x-2">
              <span class="text-base select-none" aria-hidden="true">💡</span>
              <span><strong>Impacto Operativo:</strong> Se han salvado <strong>48 cuentas</strong> este mes gracias al escalamiento sin penalizar la racha del asesor.</span>
            </div>
            <button onclick="switchView('mobile')" class="text-[#004797] font-bold hover:underline whitespace-nowrap ml-2">Ver vista móvil →</button>
          </div>
        </section>

      </div>

    </div>

  </main>


  <!-- ============================================================== -->
  <!-- MODALES INTERACTIVOS (ACCESSIBILITY & VERCEL GUIDELINES)       -->
  <!-- ============================================================== -->

  <!-- MODAL 1: REGISTRAR SEGUIMIENTO (1 CLIC) -->
  <div id="modal-seguimiento" role="dialog" aria-modal="true" aria-labelledby="modal-seg-title" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150">
      
      <button onclick="closeModal('modal-seguimiento')" aria-label="Cerrar modal de seguimiento" class="btn-tactile absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold focus-visible:ring-2 focus-visible:ring-[#004797]">✕</button>

      <div class="flex items-center space-x-2 text-emerald-600 mb-1">
        <span class="text-xl" aria-hidden="true">📞</span>
        <span class="text-xs font-extrabold uppercase tracking-wider font-ui">Gestión Comercial Rápida</span>
      </div>
      <h3 id="modal-seg-title" class="text-lg font-black text-slate-900">Registrar Seguimiento</h3>
      <p class="text-xs text-slate-500 font-ui">Selecciona el resultado del contacto para salvar tu racha de hoy antes de las 11:59&nbsp;PM.</p>

      <!-- 1-Click Action Chips -->
      <div class="mt-4 space-y-2.5">
        <button onclick="completarSeguimiento('fundida')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group focus-visible:ring-2 focus-visible:ring-emerald-600">
          <span class="text-lg bg-amber-100 text-amber-800 p-2 rounded-xl" aria-hidden="true">🏗️</span>
          <div>
            <strong class="text-xs font-extrabold text-slate-900 group-hover:text-emerald-900 block">Cliente en fundida de placa / Ocupado</strong>
            <p class="text-[11px] text-slate-500 font-ui mt-0.5">Se reprograma recordatorio para mañana 8:00&nbsp;AM. <em>¡Cuenta como intento válido y salva la racha!</em></p>
          </div>
        </button>

        <button onclick="completarSeguimiento('pedido')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group focus-visible:ring-2 focus-visible:ring-emerald-600">
          <span class="text-lg bg-emerald-100 text-emerald-800 p-2 rounded-xl" aria-hidden="true">📦</span>
          <div>
            <strong class="text-xs font-extrabold text-slate-900 group-hover:text-emerald-900 block">Llamada efectiva — Aceptó pedido</strong>
            <p class="text-[11px] text-slate-500 font-ui mt-0.5">Cliente confirma volumen de cemento. Se programa despacho formal.</p>
          </div>
        </button>

        <button onclick="completarSeguimiento('nocontesta')" class="btn-tactile w-full text-left p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50/40 transition-all flex items-start space-x-3 group focus-visible:ring-2 focus-visible:ring-emerald-600">
          <span class="text-lg bg-blue-100 text-blue-800 p-2 rounded-xl" aria-hidden="true">💬</span>
          <div>
            <strong class="text-xs font-extrabold text-slate-900 group-hover:text-emerald-900 block">No contestó — Envío WhatsApp Automático</strong>
            <p class="text-[11px] text-slate-500 font-ui mt-0.5">El Copiloto IA deja mensaje redactado y agenda segundo intento para hoy 4:00&nbsp;PM.</p>
          </div>
        </button>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-100 text-center">
        <button onclick="closeModal('modal-seguimiento')" class="text-xs text-slate-400 font-semibold hover:text-slate-600 font-ui">Cancelar</button>
      </div>
    </div>
  </div>


  <!-- MODAL 2: ESCALAMIENTO INTERDEPARTAMENTAL (SLAS) -->
  <div id="modal-escalamiento" role="dialog" aria-modal="true" aria-labelledby="modal-esc-title" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150">
      
      <button onclick="closeModal('modal-escalamiento')" aria-label="Cerrar modal de escalamiento" class="btn-tactile absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold focus-visible:ring-2 focus-visible:ring-[#004797]">✕</button>

      <div class="flex items-center space-x-2 text-amber-600 mb-1">
        <span class="text-xl" aria-hidden="true">🚨</span>
        <span class="text-xs font-extrabold uppercase tracking-wider font-ui">Salvavidas Operativo Ultracem</span>
      </div>
      <h3 id="modal-esc-title" class="text-lg font-black text-slate-900">Escalar Caso a Departamento</h3>
      <p class="text-xs text-slate-500 font-ui">¿El cierre depende de otra área? Transfiere el ticket con SLA y tu racha quedará asegurada.</p>

      <!-- Department Selector with SLAs -->
      <fieldset class="mt-4 space-y-2">
        <legend class="block text-xs font-bold text-slate-700 mb-1">Selecciona el área responsable:</legend>
        
        <div class="grid grid-cols-2 gap-2">
          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-blue-500 bg-blue-50/50 flex flex-col justify-between depto-option">
            <input type="radio" name="depto" value="cartera" checked class="sr-only">
            <span class="text-xs font-extrabold text-slate-900">💳 Cartera & Crédito</span>
            <span class="text-[10px] text-[#004797] font-bold mt-1">SLA: 4&nbsp;horas</span>
          </label>

          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between depto-option">
            <input type="radio" name="depto" value="logistica" class="sr-only">
            <span class="text-xs font-extrabold text-slate-900">🚚 Logística / Despacho</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 2&nbsp;horas</span>
          </label>

          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between depto-option">
            <input type="radio" name="depto" value="calidad" class="sr-only">
            <span class="text-xs font-extrabold text-slate-900">🔬 Calidad / NTC 121</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 6&nbsp;horas</span>
          </label>

          <label class="cursor-pointer p-2.5 rounded-xl border-2 border-slate-200 hover:border-slate-300 flex flex-col justify-between depto-option">
            <input type="radio" name="depto" value="pricing" class="sr-only">
            <span class="text-xs font-extrabold text-slate-900">🏷️ Pricing / Gerencia</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 4&nbsp;horas</span>
          </label>
        </div>
      </fieldset>

      <!-- Escalation Reason -->
      <div class="mt-3">
        <label for="esc-motivo" class="block text-xs font-bold text-slate-700 mb-1">Motivo del escalamiento:</label>
        <textarea id="esc-motivo" rows="2" autocomplete="off" class="w-full text-xs p-2.5 rounded-xl border border-slate-300 focus:ring-2 focus:ring-[#004797] focus:border-transparent outline-none font-ui" placeholder="Ej: Cliente solicita liberación de cupo para despacho de 45 ton de cemento…"></textarea>
      </div>

      <div class="mt-4 pt-2">
        <button onclick="confirmarEscalamiento()" class="btn-tactile w-full bg-[#004797] hover:bg-blue-900 text-white font-extrabold py-2.5 rounded-xl text-xs shadow-md transition-all focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-[#004797]">
          Transferir Ticket y Blindar Racha Hoy 🛡️
        </button>
      </div>
    </div>
  </div>


  <!-- MODAL 3: COPILOTO IA INTEGRAL (DRAWER) -->
  <div id="modal-copiloto" role="dialog" aria-modal="true" aria-labelledby="copiloto-client-name" class="fixed inset-0 bg-slate-900/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 relative animate-in fade-in zoom-in duration-150 max-h-[90vh] flex flex-col">
      
      <button onclick="closeModal('modal-copiloto')" aria-label="Cerrar Copiloto IA" class="btn-tactile absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center font-bold focus-visible:ring-2 focus-visible:ring-[#004797]">✕</button>

      <div class="flex items-center space-x-2 text-[#004797] mb-1">
        <span class="text-xl" aria-hidden="true">✨</span>
        <span class="text-xs font-extrabold uppercase tracking-wider font-ui">Copiloto Comercial Ultracem</span>
      </div>
      <h3 id="copiloto-client-name" class="text-lg font-black text-slate-900">Asistencia Inteligente de Cuenta</h3>
      <p class="text-xs text-slate-500 font-ui">Redacción, consulta técnica de productos y analítica comercial.</p>

      <!-- 3 Tabs of Copilot -->
      <div class="mt-4 flex border-b border-slate-200 text-xs font-ui" role="tablist">
        <button id="cop-tab-1" onclick="switchCopilotoTab(1)" role="tab" aria-selected="true" class="btn-tactile pb-2 px-3 font-extrabold text-[#004797] border-b-2 border-[#004797]">📝 Redactar Escrito</button>
        <button id="cop-tab-2" onclick="switchCopilotoTab(2)" role="tab" aria-selected="false" class="btn-tactile pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">📚 Fichas Ultracem</button>
        <button id="cop-tab-3" onclick="switchCopilotoTab(3)" role="tab" aria-selected="false" class="btn-tactile pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">🔍 Investigar Cliente</button>
      </div>

      <!-- Tab Content Area -->
      <div class="flex-1 overflow-y-auto py-3 space-y-3 font-ui">
        
        <!-- PESTAÑA 1: REDACTAR ESCRITO / MINUTA -->
        <div id="cop-panel-1" class="space-y-3 text-xs">
          <div>
            <label for="cop-voice-input" class="block font-bold text-slate-700 mb-1">Dictado rápido por voz o notas en obra:</label>
            <div class="relative">
              <textarea id="cop-voice-input" rows="2" autocomplete="off" class="w-full p-2.5 pr-10 rounded-xl border border-slate-300 text-xs outline-none focus:border-[#004797] focus:ring-1 focus:ring-[#004797]" placeholder="Hablé con el cliente en obra, requiere cotización formal de cemento estructural…"></textarea>
              <button onclick="simularVoz()" aria-label="Simular dictado por voz de notas en obra" class="btn-tactile absolute right-2 top-2 p-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm">🎙️</button>
            </div>
            <button onclick="generarMinutaIA()" class="btn-tactile mt-2 w-full bg-[#004797] hover:bg-blue-900 text-white font-extrabold py-2.5 rounded-xl text-xs transition-all flex items-center justify-center space-x-1 shadow-xs">
              <span>✨ Generar Minuta CRM y WhatsApp</span>
            </button>
          </div>

          <!-- Generated Output Box -->
          <div id="cop-output-box" class="bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 space-y-2">
            <div class="flex justify-between items-center">
              <span class="font-extrabold text-slate-800 text-[11px] uppercase tracking-wider">Borrador WhatsApp para el Cliente:</span>
              <button onclick="copiarAlPortapapeles()" id="btn-copy" aria-label="Copiar mensaje de WhatsApp" class="btn-tactile text-[#004797] font-bold text-xs hover:underline flex items-center space-x-1">
                <span>📋 Copiar</span>
              </button>
            </div>
            <p id="cop-whatsapp-text" class="text-xs text-slate-700 bg-white p-3 rounded-xl border border-slate-200 italic leading-relaxed">
              “Estimado Ing. Andrés, un cordial saludo de Ultracem. Conforme a nuestra llamada, le confirmo la reserva de 120&nbsp;Toneladas de Cemento Estructural NTC 121 para despacho el jueves a primera hora en Torre del Mar. Le adjunto el certificado de resistencia a compresión (28&nbsp;MPa a 28 días). Quedo atento a su visto bueno para la programación del camión. ¡Construyamos juntos!”
            </p>
          </div>
        </div>

        <!-- PESTAÑA 2: FICHAS TÉCNICAS OFICIALES ULTRACEM (RAG) -->
        <div id="cop-panel-2" class="hidden space-y-3 text-xs">
          <div>
            <label for="prod-selector" class="block font-bold text-slate-700 mb-1">Seleccionar Producto Ultracem:</label>
            <select id="prod-selector" onchange="actualizarFichaTecnica()" class="w-full p-2.5 rounded-xl border border-slate-300 text-xs font-semibold outline-none focus:border-[#004797]">
              <option value="estructural">Cemento Estructural Tipo ART (NTC 121)</option>
              <option value="general">Cemento Uso General Tipo UG (NTC 121)</option>
              <option value="marino">Cemento Marino Resistente a Sulfatos (MRS)</option>
              <option value="blanco">Cemento Blanco Arquitectónico</option>
            </select>
          </div>

          <!-- Ficha Técnica Resumen Dinámica -->
          <div id="ficha-container" class="bg-blue-50/70 border border-blue-200 rounded-2xl p-3.5 space-y-2.5">
            <div class="flex items-center justify-between">
              <h4 id="ficha-nombre" class="font-black text-sm text-[#004797]">Cemento Estructural ART (NTC 121)</h4>
              <span class="bg-blue-200 text-blue-900 text-[10px] font-bold px-2 py-0.5 rounded-md">Alta Resistencia</span>
            </div>
            
            <p id="ficha-desc" class="text-xs text-slate-700 leading-relaxed">
              Desarrollado para elementos estructurales que demandan altas resistencias mecánicas a edades tempranas. Ideal para columnas, vigas, losas y desencofrado rápido.
            </p>

            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-blue-200/80 text-[11px]">
              <div class="bg-white p-2.5 rounded-xl border border-blue-100">
                <span class="text-slate-400 block font-medium">Resistencia 28 Días:</span>
                <strong id="ficha-resistencia" class="text-slate-900 font-bold tabular-nums">≥ 28.0&nbsp;MPa (4,060&nbsp;psi)</strong>
              </div>
              <div class="bg-white p-2.5 rounded-xl border border-blue-100">
                <span class="text-slate-400 block font-medium">Fraguado Inicial:</span>
                <strong id="ficha-fraguado" class="text-slate-900 font-bold tabular-nums">≥ 45&nbsp;minutos (Vicat)</strong>
              </div>
            </div>

            <div class="bg-emerald-100/70 text-emerald-900 p-2.5 rounded-xl text-[11px] font-medium leading-relaxed">
              💡 <strong>Argumento de Venta Ultracem:</strong> Permite desencofrar hasta 36&nbsp;horas antes que el cemento estándar, reduciendo tiempos muertos de grúa y formaletería en obra.
            </div>
          </div>
        </div>

        <!-- PESTAÑA 3: INVESTIGADOR DE CUENTA -->
        <div id="cop-panel-3" class="hidden space-y-3 text-xs">
          <div class="bg-slate-50 border border-slate-200/80 rounded-2xl p-3.5 space-y-2">
            <div class="flex items-center space-x-2">
              <span class="text-base select-none" aria-hidden="true">🏢</span>
              <strong class="font-bold text-slate-900">Radiografía Comercial (Últimos 90 Días)</strong>
            </div>
            <ul class="space-y-1.5 text-slate-700 text-xs">
              <li>• <strong>Compras Totales:</strong> 340&nbsp;Toneladas acumuladas ($153M COP).</li>
              <li>• <strong>Frecuencia de Pedido:</strong> Cada 14 días (Tractomula completa).</li>
              <li>• <strong>Puntualidad de Pago:</strong> Excelente (Promedio 18 días en cartera).</li>
            </ul>
          </div>

          <div class="bg-amber-50 border border-amber-200 rounded-2xl p-3.5 text-xs text-amber-900 space-y-1">
            <div class="flex items-center space-x-1.5 font-bold">
              <span aria-hidden="true">🎯</span>
              <span>Oportunidad Detectada por IA:</span>
            </div>
            <p class="leading-relaxed">
              El cliente acaba de adjudicarse la fase II del proyecto urbanístico en Barranquilla. Demandará <strong>+450&nbsp;Toneladas adicionales</strong> de Cemento Estructural en las próximas 6 semanas. ¡Momento ideal para negociar contrato marco!
            </p>
          </div>
        </div>

      </div>

      <!-- Footer Button -->
      <div class="pt-3 border-t border-slate-100 text-right">
        <button onclick="closeModal('modal-copiloto')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-4 py-2 rounded-xl text-xs font-ui">
          Cerrar Asistente
        </button>
      </div>

    </div>
  </div>


  <!-- TOAST NOTIFICATION CONTAINER (ARIA LIVE FOR ACCESSIBILITY) -->
  <div id="toast-container" aria-live="polite" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>


  <!-- ============================================================== -->
  <!-- APPLICATION LOGIC JAVASCRIPT                                   -->
  <!-- ============================================================== -->
  <script>
    // Audio synthesizer for joyful gamification feedback
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
          osc.frequency.setValueAtTime(523.25, now); // C5
          osc.frequency.setValueAtTime(659.25, now + 0.1); // E5
          osc.frequency.setValueAtTime(783.99, now + 0.2); // G5
          osc.frequency.setValueAtTime(1046.50, now + 0.3); // C6
          gain.gain.setValueAtTime(0.18, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.55);
          osc.start(now);
          osc.stop(now + 0.55);
        }} else {{
          const now = ctx.currentTime;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(880, now);
          gain.gain.setValueAtTime(0.08, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
          osc.start(now);
          osc.stop(now + 0.12);
        }}
      }} catch (e) {{}}
    }}

    // State Variables
    let currentStreak = 21;
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
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#002D62] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]";
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797]";
      }} else {{
        mobileView.classList.add('hidden');
        webView.classList.remove('hidden');
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#002D62] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]";
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797]";
      }}
    }}

    // Time Mode Switcher (10:00 AM vs 10:45 PM Cierre)
    function setTimeMode(mode) {{
      playChime('click');
      const btnDay = document.getElementById('btn-time-day');
      const btnNight = document.getElementById('btn-time-night');
      const phoneClock = document.getElementById('phone-clock');
      const countdown = document.getElementById('countdown-timer');
      const mascotSpeech = document.getElementById('mascot-speech');
      const mascotBadge = document.getElementById('mascot-badge');
      const mascotCard = document.getElementById('mascot-card');

      if (mode === 'day') {{
        btnDay.className = "btn-tactile text-[11px] px-2.5 py-0.5 rounded-md font-bold bg-amber-500 text-white shadow-xs focus-visible:ring-2 focus-visible:ring-amber-600";
        btnNight.className = "btn-tactile text-[11px] px-2 py-0.5 rounded-md font-semibold text-amber-900 hover:bg-amber-200/70 focus-visible:ring-2 focus-visible:ring-red-600";
        phoneClock.textContent = "10:00 AM";
        countdown.textContent = "13h : 59m : 12s";
        countdown.className = "font-mono font-bold text-amber-300 bg-black/30 px-2 py-0.5 rounded-md tabular-nums";
        mascotSpeech.innerHTML = '“¡Pilas Carlos! Tienes <strong>2 clientes en Riesgo Crítico</strong>. Gestiona o escala antes de las 11:59&nbsp;PM para blindar tus 21 días de racha. 🔥”';
        mascotBadge.textContent = "En marcha";
        mascotBadge.className = "text-[10px] font-bold px-2 py-0.2 rounded-full bg-blue-100 text-[#004797]";
        mascotCard.className = "m-3 p-3.5 rounded-2xl bg-blue-50/70 border border-blue-200/80 shadow-xs flex items-center space-x-3.5 transition-all duration-300";
      }} else {{
        btnNight.className = "btn-tactile text-[11px] px-2.5 py-0.5 rounded-md font-bold bg-red-600 text-white shadow-xs focus-visible:ring-2 focus-visible:ring-red-700";
        btnDay.className = "btn-tactile text-[11px] px-2 py-0.5 rounded-md font-semibold text-amber-900 hover:bg-amber-200/70 focus-visible:ring-2 focus-visible:ring-amber-600";
        phoneClock.textContent = "10:45 PM";
        countdown.textContent = "01h : 14m : 08s";
        countdown.className = "font-mono font-bold text-red-200 bg-red-900 px-2 py-0.5 rounded-md animate-pulse tabular-nums";
        mascotSpeech.innerHTML = '“¡EMERGENCIA DE FRAGUADO! 😱 Quedan solo <strong>74 minutos</strong> para las 11:59&nbsp;PM. Si no gestionas o escalas tus cuentas críticas hoy, ¡perderás tus 21 días de racha!”';
        mascotBadge.textContent = "⚠️ MODO INTENSO";
        mascotBadge.className = "text-[10px] font-extrabold px-2 py-0.2 rounded-full bg-red-600 text-white animate-bounce";
        mascotCard.className = "m-3 p-3.5 rounded-2xl bg-gradient-to-r from-red-50 to-orange-50 border-2 border-red-400 shadow-md flex items-center space-x-3.5 transition-all duration-300";
        showToast("⚠️ Modo Intenso Activado: 74 minutos para corte de racha a las 11:59 PM", "danger");
      }}
    }}

    // Filter Clients by Channel
    function filterClients(channel) {{
      playChime('click');
      const cards = document.querySelectorAll('.client-card');
      const tabAll = document.getElementById('tab-all');
      const tabInd = document.getElementById('tab-industrial');
      const tabTrad = document.getElementById('tab-tradicional');

      tabAll.className = "btn-tactile px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100";
      tabInd.className = "btn-tactile px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100";
      tabTrad.className = "btn-tactile px-2.5 py-1 font-medium rounded-lg text-slate-600 hover:bg-slate-100";

      if (channel === 'all') {{
        tabAll.className = "btn-tactile px-3 py-1 font-bold rounded-lg bg-[#004797] text-white shadow-xs";
        cards.forEach(c => c.classList.remove('hidden'));
      }} else if (channel === 'industrial') {{
        tabInd.className = "btn-tactile px-3 py-1 font-bold rounded-lg bg-[#004797] text-white shadow-xs";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'industrial') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }} else if (channel === 'tradicional') {{
        tabTrad.className = "btn-tactile px-3 py-1 font-bold rounded-lg bg-[#004797] text-white shadow-xs";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'tradicional') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }}
    }}

    // Modals Handling
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
        ? "El cliente solicita certificados de calidad y curva de resistencia NTC 121 de Cemento Estructural antes de pagar."
        : "Ferretería solicita aprobación de cupo de $20M para cerrar pedido de 45 ton.";
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

    // Complete Action Flow (Saves Streak)
    function completarSeguimiento(tipo) {{
      playChime('streak');
      closeModal('modal-seguimiento');
      
      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-red-300', 'bg-white');
        card.classList.add('border-emerald-300', 'bg-emerald-50/40');
        const badge = card.querySelector('.bg-red-100');
        if (badge) {{
          badge.className = "bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2 py-0.5 rounded-md border border-emerald-300";
          badge.textContent = "🟢 GESTIONADO HOY (Racha Salvada)";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      speech.innerHTML = '“¡ESO ES TODO CARLOS! 🔥 Has gestionado a la cuenta. <strong>Tu racha subió a 22 días</strong>. ¡El cemento fragua con disciplina!”';
      
      showToast("🎉 ¡Gestión registrada! Racha protegida: 22 Días 🔥", "success");
    }}

    function confirmarEscalamiento() {{
      playChime('streak');
      closeModal('modal-escalamiento');

      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-red-300', 'bg-white');
        card.classList.add('border-blue-300', 'bg-blue-50/40');
        const badge = card.querySelector('.bg-red-100');
        if (badge) {{
          badge.className = "bg-blue-50 text-[#004797] text-[10px] font-extrabold px-2 py-0.5 rounded-md border border-blue-200";
          badge.textContent = "🛡️ ESCALADO A DEPTO (SLA ACTIVO)";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      speech.innerHTML = '“¡Excelente jugada! 🛡️ Escalaste el bloqueo a tiempo. La responsabilidad ahora es del departamento y <strong>tu racha de 22 días está blindada</strong>.”';

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

    // Simulated Voice dictation
    function simularVoz() {{
      playChime('click');
      const input = document.getElementById('cop-voice-input');
      input.value = "Hablé con Don Pedro, necesita 45 ton de Cemento Uso General urgente para el viernes antes del mediodía.";
      showToast("🎙️ Voz transcribiendo en tiempo real…", "info");
    }}

    function generarMinutaIA() {{
      playChime('streak');
      const output = document.getElementById('cop-whatsapp-text');
      output.textContent = `“Buenas tardes Don Pedro, un gusto saludarlo desde Ultracem. Le confirmo la coordinación de las 45 Toneladas de Cemento Uso General NTC 121 para entrega prioritaria este viernes en su bodega principal antes de las 12:00 PM. Despacho programado. ¡Muchas gracias por su preferencia comercial!”`;
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

    // Fichas Técnicas Oficiales Ultracem Data
    const fichasData = {{
      estructural: {{
        nombre: "Cemento Estructural Tipo ART (NTC 121)",
        desc: "Diseñado para estructuras de concreto reforzado, columnas, vigas, losas y elementos pretensados donde se requiera desencofrado rápido y altas resistencias iniciales.",
        res: "≥ 28.0 MPa a 28 días (20 MPa a 3 días)",
        frag: "≥ 45 min inicial / ≤ 375 min final"
      }},
      general: {{
        nombre: "Cemento Uso General Tipo UG (NTC 121)",
        desc: "Ideal para mampostería, pañetes, morteros de pega, pisos y reparaciones en general en todo tipo de ferreterías y depósitos.",
        res: "≥ 20.6 MPa a 28 días",
        frag: "≥ 45 min inicial / ≤ 420 min final"
      }},
      marino: {{
        nombre: "Cemento Marino Resistente a Sulfatos (MRS)",
        desc: "Formulado para cimentaciones en suelos agresivos, obras portuarias, muelles y estructuras expuestas al ambiente marino del Caribe.",
        res: "≥ 25.0 MPa a 28 días",
        frag: "Resistencia química comprobada NTC 121"
      }},
      blanco: {{
        nombre: "Cemento Blanco Ultracem",
        desc: "Acabados arquitectónicos de alta gama, morteros decorativos, terrazos y prefabricados blancos de alto impacto visual.",
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

    // Toast Notification Utility (Aria-live Polite)
    function showToast(msg, type) {{
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      const bg = type === 'success' ? 'bg-emerald-800 text-white border-emerald-600' 
               : type === 'danger' ? 'bg-red-800 text-white border-red-600' 
               : 'bg-slate-800 text-white border-slate-700';
      toast.className = `${{bg}} px-4 py-3 rounded-2xl shadow-xl border text-xs font-semibold flex items-center space-x-2 pointer-events-auto transition-all transform duration-300 translate-y-2 opacity-0 font-ui`;
      toast.innerHTML = `<span>${{msg}}</span>`;
      container.appendChild(toast);
      
      requestAnimationFrame(() => {{
        toast.classList.remove('translate-y-2', 'opacity-0');
      }});

      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => {{ toast.remove(); }}, 300);
      }}, 3500);
    }}
  </script>

</body>
</html>'''

dest_index = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\index.html"
with open(dest_index, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Updated index.html: {dest_index}")

dest_artifact = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
with open(dest_artifact, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Updated artifact: {dest_artifact}")
