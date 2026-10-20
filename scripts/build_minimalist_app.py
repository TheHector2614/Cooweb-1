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
  
  <!-- Modern Minimalist Typography: Outfit (Neo-geometric) + JetBrains Mono (Technical/Data) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --brand-blue: #004797;
      --brand-blue-hover: #003672;
      --brand-blue-subtle: #F0F5FA;
      --brand-slate-dark: #0F172A;
      --brand-slate-muted: #64748B;
      --brand-amber: #EA580C;
      --brand-green: #059669;
    }}
    
    body {{
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
    }}
    
    .font-mono-data {{
      font-family: 'JetBrains Mono', monospace;
      font-variant-numeric: tabular-nums;
    }}
    
    .text-balance {{
      text-wrap: balance;
    }}
    
    /* Minimalist Flame Pulse */
    @keyframes pulse-amber {{
      0%, 100% {{ transform: scale(1); opacity: 0.95; }}
      50% {{ transform: scale(1.08); opacity: 1; }}
    }}
    .flame-minimal {{
      display: inline-flex;
      align-items: center;
      animation: pulse-amber 2s infinite ease-in-out;
    }}
    
    /* Tactile button interaction */
    .btn-press {{
      transition: all 0.15s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-press:active {{
      transform: scale(0.985);
    }}
    
    /* Accessibility: Reduced Motion */
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
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-[#004797] focus:text-white focus:rounded-lg text-xs font-semibold">
    Saltar al contenido principal
  </a>

  <!-- ============================================================== -->
  <!-- 1. TOP NAV: MINIMALIST & ELEVATED ARCHITECTURE                 -->
  <!-- ============================================================== -->
  <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/80 sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand Minimalist Lockup -->
      <div class="flex items-center space-x-3.5">
        <img src="data:image/png;base64,{logo_base64}" alt="Ultracem" class="h-7 w-auto object-contain" width="115" height="28">
        <div class="h-4 w-px bg-slate-200" aria-hidden="true"></div>
        <div class="flex items-center space-x-2">
          <span class="font-extrabold text-slate-900 tracking-tight text-lg">Ultra<span class="text-[#004797]">Racha</span></span>
          <span class="text-[11px] font-semibold text-slate-500 uppercase tracking-widest bg-slate-100 px-2 py-0.5 rounded-md">PRO</span>
        </div>
      </div>

      <!-- Center & Right Controls -->
      <div class="flex items-center space-x-3">
        
        <!-- View Segmented Switcher (Minimalist Tab Bar) -->
        <nav aria-label="Selector de Vista" class="bg-slate-100/80 p-1 rounded-xl flex items-center border border-slate-200/60">
          <button id="btn-view-mobile" onclick="switchView('mobile')" aria-label="Ver Vista Asesor Móvil" class="btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all bg-white text-[#004797] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
            <span>Asesor Móvil</span>
          </button>
          <button id="btn-view-web" onclick="switchView('web')" aria-label="Ver Dashboard Supervisor" class="btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797]">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
            <span>Supervisor Web</span>
          </button>
        </nav>

        <!-- Time Simulator Pill -->
        <div class="hidden sm:flex items-center space-x-1 text-xs border border-slate-200 rounded-xl p-1 bg-white">
          <button id="btn-time-day" onclick="setTimeMode('day')" aria-label="Modo Día 10:00 AM" class="px-2.5 py-1 rounded-lg font-semibold bg-slate-900 text-white text-[11px] transition-all">
            10:00 AM
          </button>
          <button id="btn-time-night" onclick="setTimeMode('night')" aria-label="Modo Noche 10:45 PM" class="px-2.5 py-1 rounded-lg font-medium text-slate-600 hover:text-slate-900 text-[11px] transition-all">
            10:45 PM
          </button>
        </div>

      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- MAIN CONTAINER                                                 -->
  <!-- ============================================================== -->
  <main id="main-content" class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 flex flex-col justify-center">

    <!-- ============================================================== -->
    <!-- 1. VISTA ASESOR MÓVIL (MINIMALIST NATIVE CANVAS)               -->
    <!-- ============================================================== -->
    <div id="view-mobile" class="w-full flex justify-center items-start">
      
      <!-- Minimalist Device Frame -->
      <div class="w-full max-w-[410px] bg-white rounded-[32px] shadow-2xl shadow-slate-200/80 border border-slate-200/80 overflow-hidden flex flex-col min-h-[820px]">
        
        <!-- Status Bar -->
        <div class="pt-3.5 px-6 pb-2 flex justify-between items-center text-xs text-slate-400 font-mono-data text-[11px]">
          <span id="phone-clock" class="font-bold text-slate-800">10:00 AM</span>
          <div class="w-16 h-3 bg-slate-100 rounded-full"></div>
          <div class="flex items-center space-x-1.5 text-slate-600">
            <span>5G</span>
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          </div>
        </div>

        <!-- Asesor Header & Streak Bar (Minimalist Luxury) -->
        <div class="px-5 pt-3 pb-4 border-b border-slate-100">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <div class="relative">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-11 h-11 rounded-full object-cover ring-2 ring-slate-100">
                <span class="absolute bottom-0 right-0 w-2.5 h-2.5 rounded-full bg-emerald-500 ring-2 ring-white"></span>
              </div>
              <div>
                <h2 class="font-bold text-slate-900 text-sm tracking-tight">Carlos Mendoza</h2>
                <p class="text-xs text-slate-500">Zona Norte • Obras & Ferreterías</p>
              </div>
            </div>

            <!-- Streak Pill (Refined Amber Flame) -->
            <div class="flex items-center space-x-2 bg-amber-500/10 border border-amber-500/20 px-3 py-1.5 rounded-xl">
              <span class="flame-minimal text-amber-600">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c.5 3 2 4.5 3.5 6 1.8 1.8 2.5 3.5 2.5 5.5 0 4.4-3.6 8-8 8s-8-3.6-8-8c0-3.5 2.2-6.5 5.5-7.5.5 2 .5 3.5 1.5 5 1-2.5 2-6 3-9z"/></svg>
              </span>
              <span class="text-sm font-extrabold text-amber-700 font-mono-data tracking-tight">
                <span id="streak-days">21</span>d
              </span>
            </div>
          </div>

          <!-- Cutoff Time & Casco Protector Strip -->
          <div class="mt-3.5 flex items-center justify-between text-xs bg-slate-50 rounded-xl p-2.5 border border-slate-100">
            <div class="flex items-center space-x-1.5 text-slate-600">
              <svg class="w-3.5 h-3.5 text-slate-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              <span class="text-[11px] font-medium">Corte 11:59&nbsp;PM:</span>
              <span id="countdown-timer" class="font-mono-data font-bold text-slate-900 text-[11px]">13h : 59m : 12s</span>
            </div>
            
            <div class="flex items-center space-x-1 text-[11px] font-semibold text-slate-700 bg-white px-2 py-0.5 rounded-md border border-slate-200/70" title="Casco Protector activo: congela tu racha 24h">
              <span>⛑️</span>
              <span>1 Casco</span>
            </div>
          </div>
        </div>

        <!-- Mascot Coach: "Don Fraguado" (Minimalist Architectural Avatar) -->
        <div id="mascot-card" class="mx-4 my-3 p-3.5 rounded-2xl bg-white border border-slate-200/80 shadow-xs flex items-center space-x-3.5 transition-all">
          
          <!-- Geometric Saco Mascot -->
          <div class="relative w-11 h-12 flex-shrink-0 bg-slate-100 rounded-xl border border-slate-300 flex flex-col items-center justify-center">
            <div class="absolute -top-2 w-8 h-3 bg-white rounded-t-full border border-slate-300 flex items-center justify-center">
              <span class="text-[6px] font-extrabold text-[#004797]">UC</span>
            </div>
            <div class="w-6 h-1.5 bg-[#004797] rounded-full mt-1"></div>
            <span class="text-[7px] font-bold text-slate-600 tracking-tight mt-1">50kg</span>
          </div>

          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-900">Don Fraguado</span>
              <span id="mascot-badge" class="text-[10px] font-semibold text-[#004797] bg-blue-50 px-2 py-0.2 rounded-full">Alerta de Hoy</span>
            </div>
            <p id="mascot-speech" class="text-xs text-slate-600 mt-0.5 leading-snug">
              “Tienes <strong>2 cuentas en Riesgo Crítico</strong>. Gestiona o escala antes de medianoche para no perder tu racha.”
            </p>
          </div>
        </div>

        <!-- Toneladas Progress Strip -->
        <div class="px-5 py-2">
          <div class="flex justify-between items-center text-xs mb-1.5">
            <span class="text-slate-500 font-medium">Meta Mensual</span>
            <span class="font-mono-data font-bold text-slate-900 text-xs">420 <span class="text-slate-400 font-normal">/ 500 Ton</span></span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-1.5 overflow-hidden">
            <div class="bg-[#004797] h-full rounded-full transition-all duration-500" style="width: 84%"></div>
          </div>
        </div>

        <!-- Channel Filter (Minimalist Chips) -->
        <div class="px-5 pt-2 pb-1 flex items-center justify-between text-xs">
          <div class="flex space-x-1" role="tablist">
            <button onclick="filterClients('all')" id="tab-all" class="px-3 py-1 font-bold rounded-lg bg-slate-900 text-white text-[11px] transition-all">Todos (4)</button>
            <button onclick="filterClients('industrial')" id="tab-industrial" class="px-2.5 py-1 font-medium rounded-lg text-slate-500 hover:text-slate-900 text-[11px] transition-all">Obras</button>
            <button onclick="filterClients('tradicional')" id="tab-tradicional" class="px-2.5 py-1 font-medium rounded-lg text-slate-500 hover:text-slate-900 text-[11px] transition-all">Ferreterías</button>
          </div>
          <span class="text-[11px] text-slate-400 font-mono-data">Prioridad Riesgo</span>
        </div>

        <!-- Client Cards Container -->
        <div class="flex-1 overflow-y-auto p-4 space-y-3 bg-slate-50/60">

          <!-- CLIENT 1: Constructora Bolívar -->
          <article id="card-client-1" class="bg-white rounded-2xl p-4 border border-rose-200 shadow-xs client-card transition-all" data-channel="industrial" data-status="danger">
            <div class="flex justify-between items-start gap-2">
              <div class="min-w-0">
                <div class="flex items-center space-x-2">
                  <span class="text-[10px] font-semibold text-slate-500 uppercase tracking-wider">Obra</span>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-600 animate-pulse"></span>
                    <span>8 DÍAS INACTIVO</span>
                  </span>
                </div>
                <h3 class="font-bold text-slate-900 text-sm mt-1.5 truncate">Constructora Bolívar — Torre del Mar</h3>
                <p class="text-xs text-slate-500 mt-0.5">Ing. Andrés Meza • 120&nbsp;Ton Cemento Estructural</p>
              </div>
              <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200/60">$54M</span>
            </div>

            <div class="mt-3 p-2.5 bg-rose-50/50 rounded-xl border border-rose-100 flex items-start space-x-2 text-xs text-rose-900">
              <svg class="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              <span class="leading-tight">Cotización vence hoy 5:00&nbsp;PM. Requiere certificación NTC 121 antes de pago.</span>
            </div>

            <!-- Action Buttons: Clean & Ergonomic -->
            <div class="mt-3.5 grid grid-cols-3 gap-2">
              <button onclick="openModalSeguimiento(1, 'Constructora Bolívar')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white shadow-xs">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                <span>Seguimiento</span>
              </button>

              <button onclick="openModalEscalamiento(1, 'Constructora Bolívar')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200/80">
                <svg class="w-3.5 h-3.5 text-amber-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                <span>Escalar</span>
              </button>

              <button onclick="openModalCopiloto(1, 'Constructora Bolívar', 'industrial')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-[#004797] hover:bg-[#003672] text-white shadow-xs">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
                <span>Copiloto</span>
              </button>
            </div>
          </article>

          <!-- CLIENT 2: Ferretería El Constructor -->
          <article id="card-client-2" class="bg-white rounded-2xl p-4 border border-rose-200 shadow-xs client-card transition-all" data-channel="tradicional" data-status="danger">
            <div class="flex justify-between items-start gap-2">
              <div class="min-w-0">
                <div class="flex items-center space-x-2">
                  <span class="text-[10px] font-semibold text-slate-500 uppercase tracking-wider">Ferretería</span>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">
                    <span>5 DÍAS INACTIVO</span>
                  </span>
                </div>
                <h3 class="font-bold text-slate-900 text-sm mt-1.5 truncate">Ferretería El Constructor</h3>
                <p class="text-xs text-slate-500 mt-0.5">Don Pedro Gómez • 45&nbsp;Ton Cemento Uso General</p>
              </div>
              <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200/60">$19M</span>
            </div>

            <div class="mt-3 p-2.5 bg-rose-50/50 rounded-xl border border-rose-100 flex items-start space-x-2 text-xs text-rose-900">
              <svg class="w-4 h-4 text-rose-600 flex-shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
              <span class="leading-tight">Riesgo inminente de compra a la competencia por rotación semanal agotada.</span>
            </div>

            <div class="mt-3.5 grid grid-cols-3 gap-2">
              <button onclick="openModalSeguimiento(2, 'Ferretería El Constructor')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white shadow-xs">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                <span>Seguimiento</span>
              </button>

              <button onclick="openModalEscalamiento(2, 'Ferretería El Constructor')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-200/80">
                <svg class="w-3.5 h-3.5 text-amber-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                <span>Escalar</span>
              </button>

              <button onclick="openModalCopiloto(2, 'Ferretería El Constructor', 'tradicional')" class="btn-press flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold bg-[#004797] hover:bg-[#003672] text-white shadow-xs">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
                <span>Copiloto</span>
              </button>
            </div>
          </article>

          <!-- CLIENT 3: Consorcio Vías del Magdalena -->
          <article id="card-client-3" class="bg-white rounded-2xl p-4 border border-amber-200/80 shadow-xs client-card" data-channel="industrial" data-status="warning">
            <div class="flex justify-between items-start">
              <div>
                <div class="flex items-center space-x-2">
                  <span class="text-[10px] font-semibold text-slate-500 uppercase">Obra</span>
                  <span class="text-[10px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                    6 DÍAS INACTIVO
                  </span>
                </div>
                <h3 class="font-bold text-slate-900 text-sm mt-1.5">Consorcio Vías del Magdalena</h3>
                <p class="text-xs text-slate-500">Ing. Laura Peña • 250&nbsp;Ton Concreto</p>
              </div>
              <span class="text-xs font-bold text-slate-900 font-mono-data bg-slate-50 px-2 py-1 rounded-md border border-slate-200/60">$112M</span>
            </div>
            <div class="mt-2.5 flex items-center justify-between text-xs text-slate-500 pt-2 border-t border-slate-100">
              <span>Próxima fundida: Lunes</span>
              <button onclick="openModalSeguimiento(3, 'Consorcio Vías')" class="text-[#004797] font-semibold hover:underline">Gestionar →</button>
            </div>
          </article>

          <!-- CLIENT 4: Depósito Central La 30 -->
          <article id="card-client-4" class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs client-card opacity-80" data-channel="tradicional" data-status="healthy">
            <div class="flex justify-between items-start">
              <div>
                <div class="flex items-center space-x-2">
                  <span class="text-[10px] font-semibold text-slate-500 uppercase">Ferretería</span>
                  <span class="text-[10px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                    AL DÍA
                  </span>
                </div>
                <h3 class="font-bold text-slate-900 text-sm mt-1.5">Depósito Central La 30</h3>
                <p class="text-xs text-slate-500">30&nbsp;Ton despachadas ayer en orden #402</p>
              </div>
              <span class="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2 py-1 rounded-md">Al día</span>
            </div>
          </article>

        </div>

        <!-- Phone Bottom Bar -->
        <nav aria-label="Navegación Móvil" class="bg-white border-t border-slate-100 px-6 py-3 flex justify-around items-center text-xs">
          <button class="flex flex-col items-center text-[#004797] font-bold">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2c.5 3 2 4.5 3.5 6 1.8 1.8 2.5 3.5 2.5 5.5 0 4.4-3.6 8-8 8s-8-3.6-8-8c0-3.5 2.2-6.5 5.5-7.5.5 2 .5 3.5 1.5 5 1-2.5 2-6 3-9z"/></svg>
            <span class="text-[10px] mt-0.5">Racha</span>
          </button>
          <button onclick="openModalCopiloto(1, 'Asistente Global', 'general')" class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            <span class="text-[10px] mt-0.5">Copiloto</span>
          </button>
          <button onclick="switchView('web')" class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg>
            <span class="text-[10px] mt-0.5">Liga</span>
          </button>
          <button class="flex flex-col items-center text-slate-400 hover:text-slate-700">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span class="text-[10px] mt-0.5">Perfil</span>
          </button>
        </nav>

      </div>
    </div>


    <!-- ============================================================== -->
    <!-- 2. VISTA SUPERVISOR WEB (MINIMALIST STRIPE/LINEAR DATA GRID)    -->
    <!-- ============================================================== -->
    <div id="view-web" class="hidden w-full space-y-6">
      
      <!-- Top Executive Banner -->
      <div class="bg-white rounded-2xl p-6 border border-slate-200/80 shadow-xs flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <div class="flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Centro de Operaciones</span>
            <span class="text-slate-300">•</span>
            <span class="text-xs text-slate-500">Regional Caribe</span>
          </div>
          <h2 class="text-2xl font-extrabold text-slate-900 tracking-tight mt-1">Supervisión Comercial UltraRacha</h2>
          <p class="text-sm text-slate-500">Trazabilidad en tiempo real de toneladas, rachas y cumplimiento de SLAs.</p>
        </div>

        <div class="flex items-center space-x-3">
          <div class="text-right hidden sm:block">
            <p class="text-xs text-slate-400">Líder Regional</p>
            <p class="text-sm font-bold text-slate-900">Ing. Roberto Vega</p>
          </div>
          <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80" alt="Roberto Vega" class="w-11 h-11 rounded-full border border-slate-200 object-cover">
        </div>
      </div>

      <!-- 4 Minimalist Data Tiles -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs">
          <span class="text-xs font-medium text-slate-500 block">Toneladas del Mes</span>
          <div class="mt-2 flex items-baseline space-x-2">
            <span class="text-3xl font-extrabold text-slate-900 font-mono-data tracking-tight">3,420</span>
            <span class="text-xs text-slate-400 font-mono-data">/ 3,750&nbsp;Ton</span>
          </div>
          <span class="text-xs font-semibold text-emerald-600 block mt-1.5">↑ 91.2% completado</span>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs">
          <span class="text-xs font-medium text-slate-500 block">Seguimiento a Tiempo</span>
          <div class="mt-2 flex items-baseline space-x-2">
            <span class="text-3xl font-extrabold text-slate-900 font-mono-data tracking-tight">94.8%</span>
          </div>
          <span class="text-xs font-semibold text-emerald-600 block mt-1.5">↑ +6.2% vs mes anterior</span>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs">
          <span class="text-xs font-medium text-slate-500 block">Cuentas Críticas Salvadas</span>
          <div class="mt-2 flex items-baseline space-x-2">
            <span class="text-3xl font-extrabold text-slate-900 font-mono-data tracking-tight">23</span>
            <span class="text-xs text-slate-400 font-mono-data">/ 24</span>
          </div>
          <span class="text-xs font-semibold text-amber-600 block mt-1.5">⚠️ 1 pendiente antes de 11:59&nbsp;PM</span>
        </div>

        <div class="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs">
          <span class="text-xs font-medium text-slate-500 block">Casos Escalados (SLA)</span>
          <div class="mt-2 flex items-baseline space-x-2">
            <span class="text-3xl font-extrabold text-slate-900 font-mono-data tracking-tight">6</span>
            <span class="text-xs text-slate-400 font-mono-data">activos</span>
          </div>
          <span class="text-xs font-semibold text-emerald-600 block mt-1.5">100% dentro del plazo</span>
        </div>

      </div>

      <!-- Main Columns: Leaderboard & Escalation SLA Audit Table -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- Left: Leaderboard "Liga Maestros Ultracem" -->
        <section class="lg:col-span-5 bg-white rounded-2xl p-6 border border-slate-200/80 shadow-xs">
          <div class="flex justify-between items-center mb-5">
            <div>
              <h3 class="text-base font-bold text-slate-900 tracking-tight">Liga Maestros Ultracem</h3>
              <p class="text-xs text-slate-400">Ranking por constancia diaria (Racha)</p>
            </div>
            <span class="text-[11px] font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">Oro</span>
          </div>

          <div class="space-y-2.5">
            
            <div class="p-3 rounded-xl bg-slate-50 border border-slate-200/60 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xs font-bold text-amber-600 font-mono-data w-4 text-center">01</span>
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-9 h-9 rounded-full object-cover">
                <div>
                  <h4 class="font-bold text-xs text-slate-900">Carlos Mendoza</h4>
                  <p class="text-[11px] text-slate-400 font-mono-data">420 Ton • Caribe</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-xs font-bold text-amber-700 font-mono-data">21 días 🔥</span>
                <span class="block text-[10px] text-emerald-600 font-medium">Al día</span>
              </div>
            </div>

            <div class="p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200/60 transition-colors flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xs font-bold text-slate-400 font-mono-data w-4 text-center">02</span>
                <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Andrea Polo" class="w-9 h-9 rounded-full object-cover">
                <div>
                  <h4 class="font-bold text-xs text-slate-900">Andrea Polo</h4>
                  <p class="text-[11px] text-slate-400 font-mono-data">395 Ton • Cartagena</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-xs font-bold text-slate-700 font-mono-data">19 días 🔥</span>
                <span class="block text-[10px] text-emerald-600 font-medium">Al día</span>
              </div>
            </div>

            <div class="p-3 rounded-xl hover:bg-slate-50 border border-transparent hover:border-slate-200/60 transition-colors flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xs font-bold text-slate-400 font-mono-data w-4 text-center">03</span>
                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Javier Restrepo" class="w-9 h-9 rounded-full object-cover">
                <div>
                  <h4 class="font-bold text-xs text-slate-900">Javier Restrepo</h4>
                  <p class="text-[11px] text-slate-400 font-mono-data">360 Ton • Barranquilla</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-xs font-bold text-slate-700 font-mono-data">15 días 🔥</span>
                <span class="block text-[10px] text-emerald-600 font-medium">Al día</span>
              </div>
            </div>

            <div class="p-3 rounded-xl bg-rose-50/40 border border-rose-200/60 flex items-center justify-between">
              <div class="flex items-center space-x-3">
                <span class="text-xs font-bold text-rose-500 font-mono-data w-4 text-center">04</span>
                <img src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=80&auto=format&fit=crop&q=80" alt="Felipe Castro" class="w-9 h-9 rounded-full object-cover">
                <div>
                  <h4 class="font-bold text-xs text-slate-900">Felipe Castro</h4>
                  <p class="text-[11px] text-slate-400 font-mono-data">280 Ton • Santa Marta</p>
                </div>
              </div>
              <div class="text-right">
                <span class="text-xs font-bold text-rose-600 font-mono-data">7 días ⚠️</span>
                <span class="block text-[10px] text-rose-600 font-medium">1 pendiente</span>
              </div>
            </div>

          </div>
        </section>

        <!-- Right: Escalation SLA Audit Table -->
        <section class="lg:col-span-7 bg-white rounded-2xl p-6 border border-slate-200/80 shadow-xs">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 mb-5">
            <div>
              <h3 class="text-base font-bold text-slate-900 tracking-tight">Casos Escalados a Departamentos</h3>
              <p class="text-xs text-slate-400">Tickets transferidos con compromiso de respuesta SLA</p>
            </div>
            <span class="text-[11px] font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200/60">
              SLA Promedio: 1h 42m
            </span>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <thead class="text-slate-400 font-semibold border-b border-slate-100 text-[11px]">
                <tr>
                  <th class="pb-3 font-medium">Ticket / Cliente</th>
                  <th class="pb-3 font-medium">Departamento</th>
                  <th class="pb-3 font-medium">Asesor</th>
                  <th class="pb-3 font-medium">SLA Restante</th>
                  <th class="pb-3 text-right font-medium">Acción</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-slate-100">
                
                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3.5">
                    <span class="font-bold text-slate-900 font-mono-data block">#TR-4091</span>
                    <span class="text-slate-500 text-[11px]">Consorcio Vías • Mixer</span>
                  </td>
                  <td class="py-3.5">
                    <span class="text-[11px] font-semibold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-md">Logística (2h)</span>
                  </td>
                  <td class="py-3.5 text-slate-600">Carlos Mendoza</td>
                  <td class="py-3.5">
                    <span class="font-mono-data font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded text-[11px]">01h : 14m</span>
                  </td>
                  <td class="py-3.5 text-right">
                    <button onclick="alert('Notificación enviada a Despachos Planta Ultracem.')" class="btn-press px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-700 hover:bg-slate-100 border border-slate-200">
                      Acelerar
                    </button>
                  </td>
                </tr>

                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3.5">
                    <span class="font-bold text-slate-900 font-mono-data block">#TR-4088</span>
                    <span class="text-slate-500 text-[11px]">Ferretería El Sol • Cupo</span>
                  </td>
                  <td class="py-3.5">
                    <span class="text-[11px] font-semibold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-md">Cartera (4h)</span>
                  </td>
                  <td class="py-3.5 text-slate-600">Andrea Polo</td>
                  <td class="py-3.5">
                    <span class="font-mono-data font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded text-[11px]">02h : 45m</span>
                  </td>
                  <td class="py-3.5 text-right">
                    <button onclick="alert('Notificación enviada al analista de Crédito.')" class="btn-press px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-700 hover:bg-slate-100 border border-slate-200">
                      Revisar
                    </button>
                  </td>
                </tr>

                <tr class="hover:bg-slate-50 transition-colors">
                  <td class="py-3.5">
                    <span class="font-bold text-slate-900 font-mono-data block">#TR-4082</span>
                    <span class="text-slate-500 text-[11px]">Constructora Bolívar • NTC</span>
                  </td>
                  <td class="py-3.5">
                    <span class="text-[11px] font-semibold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-md">Calidad (6h)</span>
                  </td>
                  <td class="py-3.5 text-slate-600">Carlos Mendoza</td>
                  <td class="py-3.5">
                    <span class="font-mono-data font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded text-[11px]">00h : 48m</span>
                  </td>
                  <td class="py-3.5 text-right">
                    <button onclick="alert('Certificado de compresión reenviado al cliente.')" class="btn-press px-2.5 py-1 rounded-lg text-xs font-semibold text-slate-700 hover:bg-slate-100 border border-slate-200">
                      Liberar
                    </button>
                  </td>
                </tr>

              </tbody>
            </table>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>Se han salvado <strong>48 cuentas</strong> este mes por escalamiento oportuno.</span>
            <button onclick="switchView('mobile')" class="text-[#004797] font-semibold hover:underline">Ver vista móvil →</button>
          </div>
        </section>

      </div>

    </div>

  </main>


  <!-- ============================================================== -->
  <!-- MODALES MINIMALISTAS                                           -->
  <!-- ============================================================== -->

  <!-- MODAL 1: REGISTRAR SEGUIMIENTO -->
  <div id="modal-seguimiento" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-xl border border-slate-200 relative animate-in fade-in duration-150">
      
      <button onclick="closeModal('modal-seguimiento')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full flex items-center justify-center text-sm">✕</button>

      <div class="flex items-center space-x-2 text-emerald-600 mb-1">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        <span class="text-xs font-semibold uppercase tracking-wider">Gestión Comercial</span>
      </div>
      <h3 id="modal-seg-title" class="text-base font-bold text-slate-900">Registrar Seguimiento</h3>
      <p class="text-xs text-slate-500">Selecciona el resultado para asegurar tu racha de hoy antes de las 11:59&nbsp;PM.</p>

      <div class="mt-4 space-y-2">
        <button onclick="completarSeguimiento('fundida')" class="btn-press w-full text-left p-3.5 rounded-xl border border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all flex items-start space-x-3">
          <div class="p-2 rounded-lg bg-amber-50 text-amber-700 mt-0.5">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
          </div>
          <div>
            <strong class="text-xs font-bold text-slate-900 block">Cliente en fundida de placa / Ocupado</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">Reprograma recordatorio automático para mañana 8:00 AM. <em>Salva la racha</em>.</p>
          </div>
        </button>

        <button onclick="completarSeguimiento('pedido')" class="btn-press w-full text-left p-3.5 rounded-xl border border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all flex items-start space-x-3">
          <div class="p-2 rounded-lg bg-emerald-50 text-emerald-700 mt-0.5">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
          </div>
          <div>
            <strong class="text-xs font-bold text-slate-900 block">Llamada efectiva — Aceptó pedido</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">Cliente confirma volumen de cemento. Se programa despacho.</p>
          </div>
        </button>

        <button onclick="completarSeguimiento('nocontesta')" class="btn-press w-full text-left p-3.5 rounded-xl border border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all flex items-start space-x-3">
          <div class="p-2 rounded-lg bg-blue-50 text-[#004797] mt-0.5">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <div>
            <strong class="text-xs font-bold text-slate-900 block">No contestó — Envío WhatsApp Automático</strong>
            <p class="text-[11px] text-slate-500 mt-0.5">El Copiloto IA redacta mensaje y agenda segundo intento para hoy 4:00 PM.</p>
          </div>
        </button>
      </div>

      <div class="mt-4 pt-3 border-t border-slate-100 text-center">
        <button onclick="closeModal('modal-seguimiento')" class="text-xs text-slate-400 font-medium hover:text-slate-600">Cancelar</button>
      </div>
    </div>
  </div>


  <!-- MODAL 2: ESCALAMIENTO CON SLA -->
  <div id="modal-escalamiento" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-xl border border-slate-200 relative animate-in fade-in duration-150">
      
      <button onclick="closeModal('modal-escalamiento')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full flex items-center justify-center text-sm">✕</button>

      <div class="flex items-center space-x-2 text-amber-600 mb-1">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
        <span class="text-xs font-semibold uppercase tracking-wider">Salvavidas Operativo</span>
      </div>
      <h3 id="modal-esc-title" class="text-base font-bold text-slate-900">Escalar Caso a Departamento</h3>
      <p class="text-xs text-slate-500">Transfiere el ticket con SLA y tu racha quedará asegurada.</p>

      <div class="mt-4 space-y-2">
        <label class="block text-xs font-bold text-slate-700">Selecciona el área responsable:</label>
        
        <div class="grid grid-cols-2 gap-2">
          <label class="cursor-pointer p-3 rounded-xl border border-blue-500 bg-blue-50/50 flex flex-col justify-between">
            <input type="radio" name="depto" value="cartera" checked class="sr-only">
            <span class="text-xs font-bold text-slate-900">Cartera & Crédito</span>
            <span class="text-[10px] text-[#004797] font-semibold mt-1">SLA: 4 horas</span>
          </label>

          <label class="cursor-pointer p-3 rounded-xl border border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="logistica" class="sr-only">
            <span class="text-xs font-bold text-slate-900">Logística / Despacho</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 2 horas</span>
          </label>

          <label class="cursor-pointer p-3 rounded-xl border border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="calidad" class="sr-only">
            <span class="text-xs font-bold text-slate-900">Calidad / NTC 121</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 6 horas</span>
          </label>

          <label class="cursor-pointer p-3 rounded-xl border border-slate-200 hover:border-slate-300 flex flex-col justify-between">
            <input type="radio" name="depto" value="pricing" class="sr-only">
            <span class="text-xs font-bold text-slate-900">Pricing / Gerencia</span>
            <span class="text-[10px] text-slate-500 font-semibold mt-1">SLA: 4 horas</span>
          </label>
        </div>
      </div>

      <div class="mt-3">
        <label for="esc-motivo" class="block text-xs font-bold text-slate-700 mb-1">Motivo:</label>
        <textarea id="esc-motivo" rows="2" class="w-full text-xs p-2.5 rounded-xl border border-slate-200 focus:border-[#004797] focus:ring-1 focus:ring-[#004797] outline-none" placeholder="Detalle del bloqueo…"></textarea>
      </div>

      <div class="mt-4 pt-1">
        <button onclick="confirmarEscalamiento()" class="btn-press w-full bg-[#004797] hover:bg-[#003672] text-white font-bold py-2.5 rounded-xl text-xs shadow-xs transition-all">
          Transferir Ticket y Blindar Racha Hoy 🛡️
        </button>
      </div>
    </div>
  </div>


  <!-- MODAL 3: COPILOTO IA -->
  <div id="modal-copiloto" role="dialog" aria-modal="true" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full p-6 shadow-xl border border-slate-200 relative animate-in fade-in duration-150 max-h-[85vh] flex flex-col">
      
      <button onclick="closeModal('modal-copiloto')" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 w-8 h-8 rounded-full flex items-center justify-center text-sm">✕</button>

      <div class="flex items-center space-x-2 text-[#004797] mb-1">
        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
        <span class="text-xs font-semibold uppercase tracking-wider">Copiloto Comercial</span>
      </div>
      <h3 id="copiloto-client-name" class="text-base font-bold text-slate-900">Copiloto IA</h3>
      <p class="text-xs text-slate-500">Redacción, consulta técnica de productos y análisis de cuenta.</p>

      <div class="mt-4 flex border-b border-slate-100 text-xs">
        <button id="cop-tab-1" onclick="switchCopilotoTab(1)" class="pb-2 px-3 font-bold text-[#004797] border-b-2 border-[#004797]">Redactar</button>
        <button id="cop-tab-2" onclick="switchCopilotoTab(2)" class="pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">Fichas Técnicas</button>
        <button id="cop-tab-3" onclick="switchCopilotoTab(3)" class="pb-2 px-3 font-medium text-slate-500 hover:text-slate-800">Investigar</button>
      </div>

      <div class="flex-1 overflow-y-auto py-3 space-y-3">
        
        <!-- PESTAÑA 1 -->
        <div id="cop-panel-1" class="space-y-3 text-xs">
          <div>
            <label for="cop-voice-input" class="block font-medium text-slate-700 mb-1">Notas en obra o dictado:</label>
            <div class="relative">
              <textarea id="cop-voice-input" rows="2" class="w-full p-2.5 pr-9 rounded-xl border border-slate-200 text-xs outline-none focus:border-[#004797] focus:ring-1 focus:ring-[#004797]" placeholder="Hablé con el cliente, requiere cotización formal de cemento estructural…"></textarea>
              <button onclick="simularVoz()" class="absolute right-2 top-2 p-1.5 rounded-md hover:bg-slate-100 text-slate-500">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="22"></line></svg>
              </button>
            </div>
            <button onclick="generarMinutaIA()" class="btn-press mt-2 w-full bg-[#004797] hover:bg-[#003672] text-white font-bold py-2 rounded-xl text-xs transition-all flex items-center justify-center space-x-1 shadow-xs">
              <span>Generar Minuta y WhatsApp</span>
            </button>
          </div>

          <div id="cop-output-box" class="bg-slate-50 border border-slate-200/60 rounded-xl p-3 space-y-2">
            <div class="flex justify-between items-center">
              <span class="font-bold text-slate-700 text-[11px] uppercase tracking-wider">Borrador para WhatsApp</span>
              <button onclick="copiarAlPortapapeles()" id="btn-copy" class="text-[#004797] font-semibold text-xs hover:underline flex items-center space-x-1">
                <span>Copiar</span>
              </button>
            </div>
            <p id="cop-whatsapp-text" class="text-xs text-slate-600 bg-white p-2.5 rounded-lg border border-slate-200/60 italic leading-relaxed">
              “Estimado Ing. Andrés, un cordial saludo de Ultracem. Conforme a nuestra llamada, le confirmo la reserva de 120&nbsp;Toneladas de Cemento Estructural NTC 121 para despacho el jueves a primera hora en Torre del Mar. Le adjunto el certificado de resistencia a compresión (28&nbsp;MPa a 28 días). Quedo atento a su visto bueno para la programación del camión. ¡Construyamos juntos!”
            </p>
          </div>
        </div>

        <!-- PESTAÑA 2 -->
        <div id="cop-panel-2" class="hidden space-y-3 text-xs">
          <div>
            <label for="prod-selector" class="block font-medium text-slate-700 mb-1">Producto Ultracem:</label>
            <select id="prod-selector" onchange="actualizarFichaTecnica()" class="w-full p-2.5 rounded-xl border border-slate-200 text-xs font-semibold outline-none focus:border-[#004797]">
              <option value="estructural">Cemento Estructural Tipo ART (NTC 121)</option>
              <option value="general">Cemento Uso General Tipo UG (NTC 121)</option>
              <option value="marino">Cemento Marino Resistente a Sulfatos (MRS)</option>
              <option value="blanco">Cemento Blanco Arquitectónico</option>
            </select>
          </div>

          <div class="bg-blue-50/50 border border-blue-100 rounded-xl p-3.5 space-y-2">
            <div class="flex items-center justify-between">
              <h4 id="ficha-nombre" class="font-bold text-sm text-[#004797]">Cemento Estructural ART (NTC 121)</h4>
              <span class="bg-blue-100 text-[#004797] text-[10px] font-bold px-2 py-0.5 rounded">Alta Resistencia</span>
            </div>
            
            <p id="ficha-desc" class="text-xs text-slate-600 leading-relaxed">
              Desarrollado para elementos estructurales que demandan altas resistencias mecánicas a edades tempranas. Ideal para columnas, vigas y desencofrado rápido.
            </p>

            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-blue-100 text-[11px]">
              <div class="bg-white p-2 rounded-lg border border-blue-100">
                <span class="text-slate-400 block font-medium">Resistencia 28 Días:</span>
                <strong id="ficha-resistencia" class="text-slate-900 font-bold font-mono-data">≥ 28.0&nbsp;MPa</strong>
              </div>
              <div class="bg-white p-2 rounded-lg border border-blue-100">
                <span class="text-slate-400 block font-medium">Fraguado Inicial:</span>
                <strong id="ficha-fraguado" class="text-slate-900 font-bold font-mono-data">≥ 45&nbsp;minutos</strong>
              </div>
            </div>
          </div>
        </div>

        <!-- PESTAÑA 3 -->
        <div id="cop-panel-3" class="hidden space-y-3 text-xs">
          <div class="bg-slate-50 border border-slate-200/60 rounded-xl p-3 space-y-1.5">
            <strong class="font-bold text-slate-900 block">Historial de Compras (90 Días)</strong>
            <p class="text-slate-600">• Compras Totales: 340&nbsp;Ton ($153M COP).</p>
            <p class="text-slate-600">• Frecuencia de Pedido: Cada 14 días.</p>
            <p class="text-slate-600">• Puntualidad de Pago: 18 días promedio.</p>
          </div>

          <div class="bg-amber-50/60 border border-amber-200/60 rounded-xl p-3 text-xs text-amber-900 space-y-1">
            <strong class="font-bold block">Oportunidad Detectada:</strong>
            <p class="leading-relaxed">
              El cliente acaba de iniciar la fase de cimentación de la Torre 2. Se estima demanda de <strong>+450&nbsp;Ton</strong> en las próximas semanas.
            </p>
          </div>
        </div>

      </div>

      <div class="pt-3 border-t border-slate-100 text-right">
        <button onclick="closeModal('modal-copiloto')" class="px-4 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-slate-100">
          Cerrar
        </button>
      </div>

    </div>
  </div>


  <!-- TOAST NOTIFICATIONS -->
  <div id="toast-container" aria-live="polite" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>


  <!-- ============================================================== -->
  <!-- JAVASCRIPT STATE ENGINE                                        -->
  <!-- ============================================================== -->
  <script>
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
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
          osc.start(now);
          osc.stop(now + 0.5);
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
    let currentActiveClientId = 1;

    function switchView(view) {{
      playChime('click');
      const mobileView = document.getElementById('view-mobile');
      const webView = document.getElementById('view-web');
      const btnMobile = document.getElementById('btn-view-mobile');
      const btnWeb = document.getElementById('btn-view-web');

      if (view === 'mobile') {{
        mobileView.classList.remove('hidden');
        webView.classList.add('hidden');
        btnMobile.className = "btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all bg-white text-[#004797] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]";
        btnWeb.className = "btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797]";
      }} else {{
        mobileView.classList.add('hidden');
        webView.classList.remove('hidden');
        btnWeb.className = "btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all bg-white text-[#004797] shadow-xs focus-visible:ring-2 focus-visible:ring-[#004797]";
        btnMobile.className = "btn-press flex items-center space-x-1.5 px-3.5 py-1.5 rounded-lg text-xs font-medium transition-all text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-[#004797]";
      }}
    }}

    function setTimeMode(mode) {{
      playChime('click');
      const btnDay = document.getElementById('btn-time-day');
      const btnNight = document.getElementById('btn-time-night');
      const phoneClock = document.getElementById('phone-clock');
      const countdown = document.getElementById('countdown-timer');
      const mascotSpeech = document.getElementById('mascot-speech');
      const mascotBadge = document.getElementById('mascot-badge');

      if (mode === 'day') {{
        btnDay.className = "px-2.5 py-1 rounded-lg font-semibold bg-slate-900 text-white text-[11px] transition-all";
        btnNight.className = "px-2.5 py-1 rounded-lg font-medium text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        phoneClock.textContent = "10:00 AM";
        countdown.textContent = "13h : 59m : 12s";
        countdown.className = "font-mono-data font-bold text-slate-900 text-[11px]";
        mascotSpeech.innerHTML = '“Tienes <strong>2 cuentas en Riesgo Crítico</strong>. Gestiona o escala antes de medianoche para no perder tu racha.”';
        mascotBadge.textContent = "Alerta de Hoy";
        mascotBadge.className = "text-[10px] font-semibold text-[#004797] bg-blue-50 px-2 py-0.2 rounded-full";
      }} else {{
        btnNight.className = "px-2.5 py-1 rounded-lg font-semibold bg-rose-600 text-white text-[11px] transition-all";
        btnDay.className = "px-2.5 py-1 rounded-lg font-medium text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        phoneClock.textContent = "10:45 PM";
        countdown.textContent = "01h : 14m : 08s";
        countdown.className = "font-mono-data font-bold text-rose-600 text-[11px] animate-pulse";
        mascotSpeech.innerHTML = '“¡Quedan <strong>74 minutos</strong>! Gestiona tus cuentas rojas o tu racha de 21 días se perderá a medianoche.”';
        mascotBadge.textContent = "Cierre Inminente";
        mascotBadge.className = "text-[10px] font-bold text-white bg-rose-600 px-2 py-0.2 rounded-full";
        showToast("Quedan 74 minutos para corte de medianoche", "danger");
      }}
    }}

    function filterClients(channel) {{
      playChime('click');
      const cards = document.querySelectorAll('.client-card');
      const tabAll = document.getElementById('tab-all');
      const tabInd = document.getElementById('tab-industrial');
      const tabTrad = document.getElementById('tab-tradicional');

      tabAll.className = "px-2.5 py-1 font-medium rounded-lg text-slate-500 hover:text-slate-900 text-[11px] transition-all";
      tabInd.className = "px-2.5 py-1 font-medium rounded-lg text-slate-500 hover:text-slate-900 text-[11px] transition-all";
      tabTrad.className = "px-2.5 py-1 font-medium rounded-lg text-slate-500 hover:text-slate-900 text-[11px] transition-all";

      if (channel === 'all') {{
        tabAll.className = "px-3 py-1 font-bold rounded-lg bg-slate-900 text-white text-[11px] transition-all";
        cards.forEach(c => c.classList.remove('hidden'));
      }} else if (channel === 'industrial') {{
        tabInd.className = "px-3 py-1 font-bold rounded-lg bg-slate-900 text-white text-[11px] transition-all";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'industrial') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }} else if (channel === 'tradicional') {{
        tabTrad.className = "px-3 py-1 font-bold rounded-lg bg-slate-900 text-white text-[11px] transition-all";
        cards.forEach(c => {{
          if (c.getAttribute('data-channel') === 'tradicional') c.classList.remove('hidden');
          else c.classList.add('hidden');
        }});
      }}
    }}

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
        ? "El cliente solicita certificados de calidad NTC 121 antes de autorizar despacho."
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

    function completarSeguimiento(tipo) {{
      playChime('streak');
      closeModal('modal-seguimiento');
      
      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-rose-200');
        card.classList.add('border-emerald-200');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "text-[10px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200";
          badge.textContent = "GESTIONADO HOY";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      speech.innerHTML = '“¡Excelente gestión! <strong>Tu racha subió a 22 días</strong>. ¡La disciplina construye resultados!”';
      
      showToast("Racha asegurada: 22 Días 🔥", "success");
    }}

    function confirmarEscalamiento() {{
      playChime('streak');
      closeModal('modal-escalamiento');

      const card = document.getElementById('card-client-' + currentActiveClientId);
      if (card) {{
        card.classList.remove('border-rose-200');
        card.classList.add('border-blue-200');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "text-[10px] font-bold text-[#004797] bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200";
          badge.textContent = "ESCALADO (SLA ACTIVO)";
        }}
      }}

      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;
      
      const speech = document.getElementById('mascot-speech');
      speech.innerHTML = '“Ticket escalado con éxito. <strong>Tu racha de 22 días queda protegida</strong>.”';

      showToast("Ticket transferido. Racha protegida hoy 🛡️", "success");
    }}

    function switchCopilotoTab(tabIndex) {{
      playChime('click');
      for (let i = 1; i <= 3; i++) {{
        document.getElementById('cop-tab-' + i).className = i === tabIndex 
          ? "pb-2 px-3 font-bold text-[#004797] border-b-2 border-[#004797]" 
          : "pb-2 px-3 font-medium text-slate-500 hover:text-slate-800";
        document.getElementById('cop-panel-' + i).className = i === tabIndex ? "space-y-3 text-xs" : "hidden space-y-3 text-xs";
      }}
    }}

    function simularVoz() {{
      playChime('click');
      const input = document.getElementById('cop-voice-input');
      input.value = "Hablé con Don Pedro, necesita 45 ton de Cemento Uso General urgente para el viernes en la mañana.";
      showToast("Voz transcrita con éxito", "info");
    }}

    function generarMinutaIA() {{
      playChime('streak');
      const output = document.getElementById('cop-whatsapp-text');
      output.textContent = `“Buenas tardes Don Pedro, un saludo de Ultracem. Le confirmo la reserva de las 45 Toneladas de Cemento Uso General NTC 121 para entrega prioritaria este viernes en su bodega principal antes de las 12:00 PM. Despacho programado. ¡Muchas gracias!”`;
      showToast("Borrador generado por IA", "success");
    }}

    function copiarAlPortapapeles() {{
      const text = document.getElementById('cop-whatsapp-text').textContent;
      navigator.clipboard.writeText(text).then(() => {{
        const btn = document.getElementById('btn-copy');
        btn.innerHTML = "<span>¡Copiado!</span>";
        setTimeout(() => {{ btn.innerHTML = "<span>Copiar</span>"; }}, 2000);
        showToast("Texto copiado al portapapeles", "info");
      }}).catch(() => {{
        showToast("Texto disponible", "info");
      }});
    }}

    const fichasData = {{
      estructural: {{
        nombre: "Cemento Estructural Tipo ART (NTC 121)",
        desc: "Diseñado para estructuras de concreto reforzado, columnas, vigas y losas que demandan altas resistencias a edades tempranas.",
        res: "≥ 28.0 MPa",
        frag: "≥ 45 minutos"
      }},
      general: {{
        nombre: "Cemento Uso General Tipo UG (NTC 121)",
        desc: "Ideal para mampostería, pañetes, morteros de pega y pisos en ferreterías y depósitos.",
        res: "≥ 20.6 MPa",
        frag: "≥ 45 minutos"
      }},
      marino: {{
        nombre: "Cemento Marino Resistente a Sulfatos (MRS)",
        desc: "Formulado para cimentaciones en suelos agresivos y obras portuarias en ambiente marino.",
        res: "≥ 25.0 MPa",
        frag: "Resistente a sulfatos"
      }},
      blanco: {{
        nombre: "Cemento Blanco Ultracem",
        desc: "Acabados arquitectónicos de alta gama, morteros decorativos y terrazos.",
        res: "≥ 22.0 MPa",
        frag: "Blancura > 85%"
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
      const bg = type === 'success' ? 'bg-slate-900 text-white' 
               : type === 'danger' ? 'bg-rose-600 text-white' 
               : 'bg-slate-800 text-white';
      toast.className = `${{bg}} px-4 py-2.5 rounded-xl shadow-lg text-xs font-semibold flex items-center space-x-2 pointer-events-auto transition-all transform duration-200 translate-y-2 opacity-0`;
      toast.innerHTML = `<span>${{msg}}</span>`;
      container.appendChild(toast);
      
      requestAnimationFrame(() => {{
        toast.classList.remove('translate-y-2', 'opacity-0');
      }});

      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => {{ toast.remove(); }}, 2500);
      }}, 3000);
    }}
  </script>

</body>
</html>'''

dest_index = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\index.html"
with open(dest_index, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Minimalist index.html compiled: {dest_index}")

dest_artifact = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
with open(dest_artifact, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Minimalist artifact compiled: {dest_artifact}")
