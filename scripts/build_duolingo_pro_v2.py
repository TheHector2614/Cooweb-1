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
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
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
      50% {{ transform: scale(1.15) rotate(3deg); filter: drop-shadow(0 0 14px rgba(234, 88, 12, 0.8)); }}
    }}
    .flame-active {{
      display: inline-flex;
      animation: pulse-flame 1.5s infinite ease-in-out;
      transform-origin: bottom center;
    }}
    
    @keyframes mascot-breath {{
      0%, 100% {{ transform: scale(1) translateY(0); }}
      50% {{ transform: scale(1.02) translateY(-3px); }}
    }}
    .mascot-breathing {{
      animation: mascot-breath 2.4s infinite ease-in-out;
      transform-origin: bottom center;
    }}

    @keyframes mascot-wiggle {{
      0%, 100% {{ transform: rotate(0deg); }}
      25% {{ transform: rotate(-5deg) scale(1.05); }}
      75% {{ transform: rotate(5deg) scale(1.05); }}
    }}
    .mascot-wiggle {{
      animation: mascot-wiggle 0.5s ease-in-out;
    }}

    @keyframes mascot-tremble {{
      0%, 100% {{ transform: translate(0, 0); }}
      20% {{ transform: translate(-2px, 1px); }}
      40% {{ transform: translate(2px, -1px); }}
      60% {{ transform: translate(-1px, -2px); }}
      80% {{ transform: translate(2px, 2px); }}
    }}
    .mascot-panic {{
      animation: mascot-tremble 0.25s infinite ease-in-out;
    }}

    @keyframes mascot-jump {{
      0%, 100% {{ transform: translateY(0) scale(1); }}
      50% {{ transform: translateY(-10px) scale(1.08); }}
    }}
    .mascot-jump {{
      animation: mascot-jump 0.6s infinite ease-in-out;
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
      background: linear-gradient(135deg, #0284c7, #38bdf8, #bae6fd, #38bdf8);
      background-size: 200% 200%;
      animation: freeze-shimmer 3s ease infinite;
    }}

    /* In-Phone Bottom Sheet Slide Up */
    @keyframes slide-up {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}
    .animate-sheet-up {{
      animation: slide-up 0.28s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    /* Tactile Press 4px bottom shadow style */
    .btn-tactile {{
      position: relative;
      transition: all 0.12s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-tactile:active {{
      transform: translateY(2px);
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
<body class="bg-slate-100/70 text-slate-900 antialiased min-h-screen flex flex-col selection:bg-blue-100 selection:text-blue-900">

  <!-- ACCESSIBILITY: SKIP LINK -->
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-[#004797] focus:text-white focus:rounded-xl text-xs font-bold">
    Saltar al contenido principal
  </a>

  <!-- ============================================================== -->
  <!-- TOP APP BAR                                                    -->
  <!-- ============================================================== -->
  <header class="bg-white border-b border-slate-200/90 sticky top-0 z-40 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Name -->
      <div class="flex items-center space-x-3.5">
        <img src="data:image/png;base64,{logo_base64}" alt="Logotipo Oficial Ultracem" class="h-7 w-auto object-contain" width="115" height="28">
        <div class="h-4 w-px bg-slate-200" aria-hidden="true"></div>
        <div class="flex items-center space-x-2">
          <span class="font-extrabold text-slate-900 tracking-tight text-lg">Ultra<span class="text-[#004797]">Racha</span></span>
          <span class="text-[10px] font-bold text-slate-500 bg-slate-100 border border-slate-200 px-2 py-0.5 rounded-full uppercase tracking-wider">CRM Comercial</span>
        </div>
      </div>

      <!-- Controls: View Switcher & Day/Night Mode -->
      <div class="flex items-center space-x-3">
        
        <!-- View Toggle (Asesor vs Supervisor) -->
        <nav aria-label="Selector de Vistas" class="bg-slate-100 p-1 rounded-xl flex items-center border border-slate-200/80">
          <button id="btn-view-mobile" onclick="switchView('mobile')" aria-label="Cambiar a Vista Asesor Móvil" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs">
            <span>📱</span>
            <span>Asesor Móvil</span>
          </button>
          <button id="btn-view-web" onclick="switchView('web')" aria-label="Cambiar a Dashboard Supervisor" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900">
            <span>💻</span>
            <span>Supervisor Web</span>
          </button>
        </nav>

        <!-- Time Mode Simulation Pill (10:00 AM vs 10:45 PM Drama) -->
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
    <!-- 1. VISTA ASESOR MÓVIL (FRAME NATIVO 100% CONTENIDO)            -->
    <!-- ============================================================== -->
    <div id="view-mobile" class="w-full flex justify-center items-start">
      
      <!-- Phone Canvas Frame: Everything happens INSIDE this container -->
      <div class="w-full max-w-[420px] bg-white rounded-[40px] shadow-2xl border-4 border-slate-800 overflow-hidden flex flex-col min-h-[850px] relative">
        
        <!-- Phone Status Notch -->
        <div class="bg-slate-900 pt-3.5 px-6 pb-2 flex justify-between items-center text-white text-[11px] font-mono-data select-none">
          <span id="phone-clock" class="font-bold text-slate-200">10:00 AM</span>
          <div class="w-20 h-4 bg-slate-800 rounded-full flex items-center justify-center">
            <span class="w-2.5 h-2.5 rounded-full bg-slate-950"></span>
          </div>
          <div class="flex items-center space-x-1.5 text-slate-300">
            <span>5G</span>
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          </div>
        </div>

        <!-- ========================================================== -->
        <!-- IN-PHONE BOTTOM SHEET (100% INTERNAL - NO EXTERNAL WINDOWS) -->
        <!-- ========================================================== -->
        <div id="inphone-sheet-overlay" class="hidden absolute inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex flex-col justify-end rounded-[36px] overflow-hidden transition-all duration-300">
          <!-- Backdrop click to dismiss -->
          <div class="flex-1 cursor-pointer" onclick="closeInPhoneSheet()" title="Cerrar panel"></div>
          
          <!-- Sheet Body Panel (Slides up from bottom inside the phone) -->
          <div id="inphone-sheet-panel" class="bg-white rounded-t-[28px] max-h-[88%] flex flex-col shadow-2xl border-t border-slate-200 overflow-hidden transform animate-sheet-up">
            
            <!-- Sheet Header -->
            <div class="px-5 pt-3 pb-2.5 border-b border-slate-100 flex items-center justify-between bg-slate-50/80 flex-shrink-0">
              <div class="flex items-center space-x-2.5">
                <span id="sheet-header-icon" class="text-xl">💬</span>
                <div>
                  <h3 id="sheet-header-title" class="font-bold text-sm text-slate-900 leading-tight">Título</h3>
                  <p id="sheet-header-subtitle" class="text-[10px] text-slate-500 font-medium">Subtítulo descriptivo</p>
                </div>
              </div>
              <button onclick="closeInPhoneSheet()" class="w-7 h-7 rounded-full bg-slate-200/80 hover:bg-slate-300 text-slate-600 flex items-center justify-center text-xs font-bold transition-all" aria-label="Cerrar ventana interna">✕</button>
            </div>
            
            <!-- Drag Handle Pill -->
            <div class="w-10 h-1 bg-slate-300 rounded-full mx-auto my-1.5 flex-shrink-0"></div>

            <!-- Dynamic Sheet Content Injected by JS -->
            <div id="inphone-sheet-body" class="flex-1 overflow-y-auto p-4 space-y-4">
              <!-- Content rendered dynamically -->
            </div>

          </div>
        </div>

        <!-- ========================================================== -->
        <!-- SCREENS WRAPPER                                            -->
        <!-- ========================================================== -->
        <div id="mobile-screen-content" class="flex-1 flex flex-col overflow-hidden">
          
          <!-- ======================================================== -->
          <!-- PANTALLA 1: RACHA & CLIENTES                             -->
          <!-- ======================================================== -->
          <div id="screen-racha" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Mobile Header Bar: Asesor, Streak & Casco -->
            <div class="bg-gradient-to-r from-[#0033A0] to-[#004797] text-white p-4.5 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-3">
                  <div class="relative cursor-pointer" onclick="navigateToTab('perfil')" title="Ver mi Perfil y Casco">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-11 h-11 rounded-full border-2 border-white object-cover shadow-sm">
                    <span class="absolute -bottom-0.5 -right-0.5 w-3 h-3 rounded-full bg-emerald-400 border-2 border-[#0033A0]"></span>
                  </div>
                  <div>
                    <div class="flex items-center space-x-1.5">
                      <h2 class="font-bold text-sm tracking-tight text-white">Carlos Mendoza</h2>
                      <span class="text-[9px] bg-white/20 text-white font-extrabold px-1.5 py-0.5 rounded-full uppercase">Niv 4</span>
                    </div>
                    <p class="text-[11px] text-blue-200">Regional Caribe • Obras</p>
                  </div>
                </div>

                <!-- Streak Counter Pill -->
                <div class="bg-white/10 backdrop-blur-xs border border-white/25 rounded-2xl px-3 py-1 flex items-center space-x-2">
                  <span class="flame-active text-xl">🔥</span>
                  <div class="text-right">
                    <span id="streak-days" class="text-lg font-black text-amber-300 leading-none font-mono-data">21</span>
                    <span class="text-[8px] text-white/90 block font-bold uppercase tracking-wider">Días</span>
                  </div>
                </div>
              </div>

              <!-- Cutoff Clock & Shield Status -->
              <div class="mt-3 pt-2 border-t border-white/15 flex items-center justify-between text-xs">
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

            <!-- Scrollable Content Area -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <!-- ==================================================== -->
              <!-- DON FRAGUADO: MASCOTA VECTORIAL DUOLINGO-STYLE       -->
              <!-- ==================================================== -->
              <div id="mascot-card" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all">
                
                <!-- SVG Vector Mascot (Chunky cement sack with hard hat & emotive eyes) -->
                <div id="don-fraguado-container" class="relative w-16 h-18 flex-shrink-0 cursor-pointer select-none mascot-breathing" onclick="pokeMascot()" title="¡Haz clic en Don Fraguado!">
                  <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm overflow-visible" xmlns="http://www.w3.org/2000/svg">
                    <!-- Drop Shadow under character -->
                    <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />

                    <!-- Mascota: Bulto de Cemento Ultracem -->
                    <g id="mascot-body-group" class="transition-transform duration-300 origin-bottom">
                      <!-- Sack Tactile Depth -->
                      <path d="M 18,36 L 82,36 Q 88,36 89,45 L 92,94 Q 93,101 84,101 L 16,101 Q 7,101 8,94 L 11,45 Q 12,36 18,36 Z" fill="#94A3B8" />
                      <!-- Sack Front Skin -->
                      <path id="mascot-body-skin" d="M 18,34 L 82,34 Q 88,34 89,43 L 92,90 Q 93,97 84,97 L 16,97 Q 7,97 8,90 L 11,43 Q 12,34 18,34 Z" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.8" />
                      
                      <!-- Fold lines on sack shoulders -->
                      <path d="M 18,34 Q 28,42 36,34" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round"/>
                      <path d="M 82,34 Q 72,42 64,34" fill="none" stroke="#CBD5E1" stroke-width="1.5" stroke-linecap="round"/>

                      <!-- Ultracem Diagonal Brand Ribbon -->
                      <path d="M 10,68 L 90,68 L 91,80 L 9,80 Z" fill="#004797" />
                      <text x="50" y="77" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-weight="900" font-size="7.5" text-anchor="middle" letter-spacing="1">ULTRACEM</text>
                      
                      <!-- Subtitle badge (50kg NTC 121) -->
                      <rect x="35" y="83" width="30" height="6.5" rx="3" fill="#EA580C" />
                      <text x="50" y="88" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-weight="700" font-size="4.5" text-anchor="middle">50 kg • NTC</text>

                      <!-- Eyes Container (Reacts to States) -->
                      <g id="mascot-eyes">
                        <!-- Normal Eyes -->
                        <g id="eyes-normal">
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

                        <!-- Panic Eyes (Shown at 10:45 PM) -->
                        <g id="eyes-panic" class="hidden">
                          <ellipse cx="37" cy="52" rx="8.5" ry="10" fill="#FFFFFF" stroke="#E11D48" stroke-width="2" />
                          <circle cx="37" cy="53" r="2.8" fill="#E11D48" />
                          <path d="M 30,40 L 44,43" stroke="#E11D48" stroke-width="2" stroke-linecap="round" />

                          <ellipse cx="63" cy="52" rx="8.5" ry="10" fill="#FFFFFF" stroke="#E11D48" stroke-width="2" />
                          <circle cx="63" cy="53" r="2.8" fill="#E11D48" />
                          <path d="M 70,40 L 56,43" stroke="#E11D48" stroke-width="2" stroke-linecap="round" />

                          <!-- Open shivering mouth -->
                          <ellipse cx="50" cy="62" rx="4.5" ry="4" fill="#991B1B" />
                          <!-- Sweat drop -->
                          <path d="M 77,43 C 77,39 80,36 80,36 C 80,36 83,39 83,43 C 83,45 81.6,47 80,47 C 78.4,47 77,45 77,43 Z" fill="#38BDF8" />
                        </g>

                        <!-- Celebrate Eyes (Shown on Streak Save) -->
                        <g id="eyes-celebrate" class="hidden">
                          <!-- Joyful crescent eyes -->
                          <path d="M 30,53 Q 37,45 44,53" fill="none" stroke="#004797" stroke-width="2.5" stroke-linecap="round" />
                          <path d="M 56,53 Q 63,45 70,53" fill="none" stroke="#004797" stroke-width="2.5" stroke-linecap="round" />
                          <!-- Big open happy mouth with tongue -->
                          <path d="M 43,60 Q 50,70 57,60 Z" fill="#BE123C" />
                          <path d="M 46,65 Q 50,62 54,65" fill="#FDA4AF" />
                          <!-- Cheeks glow -->
                          <circle cx="27" cy="56" r="4" fill="#FB7185" opacity="0.6" />
                          <circle cx="73" cy="56" r="4" fill="#FB7185" opacity="0.6" />
                        </g>

                        <!-- Frozen Eyes (Shown on Casco Protector 24h) -->
                        <g id="eyes-frozen" class="hidden">
                          <ellipse cx="37" cy="52" rx="7.5" ry="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="2" />
                          <circle cx="37" cy="52" r="3" fill="#0369A1" />
                          <circle cx="38" cy="50" r="1" fill="#FFFFFF" />
                          
                          <ellipse cx="63" cy="52" rx="7.5" ry="8" fill="#E0F2FE" stroke="#0284C7" stroke-width="2" />
                          <circle cx="63" cy="52" r="3" fill="#0369A1" />
                          <circle cx="64" cy="50" r="1" fill="#FFFFFF" />

                          <!-- Shiver mouth -->
                          <path d="M 44,61 L 46,63 L 48,61 L 50,63 L 52,61 L 54,63 L 56,61" fill="none" stroke="#0284C7" stroke-width="1.8" stroke-linecap="round" />
                          <!-- Icicles on helmet edge -->
                          <polygon points="35,32 37,40 39,32" fill="#BAE6FD" />
                          <polygon points="49,33 51,43 53,33" fill="#E0F2FE" />
                          <polygon points="62,32 64,39 66,32" fill="#BAE6FD" />
                        </g>
                      </g>

                      <!-- Casco Amarillo de Seguridad (Hard Hat) with 3D Depth -->
                      <g id="mascot-hardhat">
                        <!-- Helmet Shadow under brim -->
                        <path d="M 14,33 Q 50,38 86,33 Q 50,42 14,33 Z" fill="#92400E" opacity="0.7" />
                        <!-- Helmet Dome -->
                        <path id="hardhat-dome" d="M 20,31 C 20,14 32,8 50,8 C 68,8 80,14 80,31 Z" fill="#F59E0B" />
                        <!-- Helmet Ridge Top -->
                        <path d="M 46,8 L 54,8 L 54,30 L 46,30 Z" fill="#FBBF24" />
                        <!-- Helmet Highlight -->
                        <path d="M 28,24 C 28,16 35,12 45,11" fill="none" stroke="#FEF3C7" stroke-width="2.5" stroke-linecap="round" opacity="0.8" />
                        <!-- Helmet Brim -->
                        <path id="hardhat-brim" d="M 12,30 C 22,27 78,27 88,30 C 90,32 86,34 82,34 C 54,36 46,36 18,34 C 14,34 10,32 12,30 Z" fill="#D97706" />
                        <!-- Small Ultracem Shield on Helmet -->
                        <circle cx="50" cy="20" r="4.5" fill="#004797" stroke="#FFFFFF" stroke-width="1" />
                        <path d="M 48,19 L 52,19 L 50,23 Z" fill="#FFFFFF" />
                      </g>

                      <!-- Sparkles / Stars / Confetti (Layer for celebrations) -->
                      <g id="mascot-particles" class="hidden">
                        <polygon points="10,20 13,26 19,26 14,30 16,36 10,32 5,36 7,30 2,26 8,26" fill="#F59E0B" />
                        <circle cx="92" cy="24" r="3" fill="#EC4899" />
                        <polygon points="86,10 90,14 84,16" fill="#06B6D4" />
                      </g>
                    </g>
                  </svg>
                </div>

                <!-- Speech Bubble with clean 8pt typography -->
                <div class="flex-1 text-xs">
                  <div class="flex items-center justify-between">
                    <strong class="text-slate-900 font-bold text-xs">Don Fraguado</strong>
                    <span class="text-[10px] text-slate-400 font-mono-data bg-slate-100 px-1.5 py-0.5 rounded">Copiloto Activo</span>
                  </div>
                  <p id="mascot-speech" class="text-slate-600 text-xs mt-1 leading-snug">
                    “¡Buenos días Carlos! Tienes <strong>2 cuentas prioritarias</strong> hoy. Registra un Check-in GPS o envía mensaje para asegurar tu racha de 21 días 🔥.”
                  </p>
                </div>
              </div>

              <!-- Section Title & Filters -->
              <div class="flex items-center justify-between pt-1">
                <div class="flex items-center space-x-2">
                  <span class="font-extrabold text-xs uppercase tracking-wider text-slate-500">Cuentas en Riesgo</span>
                  <span class="bg-rose-100 text-rose-700 text-[10px] font-bold px-2 py-0.5 rounded-full">2 Críticas</span>
                </div>
                <div class="flex space-x-1">
                  <button class="text-[11px] font-bold px-2.5 py-1 rounded-lg bg-[#004797] text-white">Todas (4)</button>
                  <button class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-600">Obras</button>
                  <button class="text-[11px] font-semibold px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-600">Ferreterías</button>
                </div>
              </div>

              <!-- ==================================================== -->
              <!-- CLIENT CARD 1: CONSTRUCTORA BOLÍVAR (OBRA MAYOR)     -->
              <!-- ==================================================== -->
              <div id="card-client-1" class="bg-white rounded-2xl p-4 border border-rose-300 shadow-xs space-y-3 transition-all">
                
                <!-- Card Header -->
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Constructora Bolívar</h3>
                      <span class="text-[10px] font-extrabold bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Torres del Mar • Barranquilla</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 border border-rose-200 px-2 py-0.5 rounded-md">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                    <span>RIESGO CHURN (23d)</span>
                  </span>
                </div>

                <!-- Structured Metric Cells (Strict 8pt Symmetry) -->
                <div class="grid grid-cols-3 gap-2 text-center">
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Volumen</span>
                    <span class="font-mono-data font-bold text-slate-800 text-xs">120 Ton</span>
                  </div>
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Cupo Activo</span>
                    <span class="font-mono-data font-bold text-slate-800 text-xs">$42.5 M</span>
                  </div>
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Retraso</span>
                    <span class="font-mono-data font-bold text-rose-600 text-xs">+8 Días</span>
                  </div>
                </div>

                <!-- Alert Notice -->
                <div class="text-[11px] text-slate-600 bg-amber-50/70 border border-amber-200/80 rounded-xl p-2.5 flex items-start space-x-2">
                  <span class="text-amber-600 text-xs">⚠️</span>
                  <p class="leading-snug">Vaciado de losas programado en 48h. El contratista está evaluando cotización de Argos.</p>
                </div>

                <!-- Action Button Matrix (All open In-Phone Sheets) -->
                <div class="grid grid-cols-2 gap-2 pt-1">
                  <!-- WhatsApp Live In-App Chat -->
                  <button onclick="openInAppWhatsApp('Constructora Bolívar', '120 Ton Cemento Estructural Max')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                    <span>💬</span>
                    <span>Chat WhatsApp</span>
                  </button>

                  <!-- GPS Check-in en Obra -->
                  <button onclick="realizarCheckInObra(1, 'Constructora Bolívar')" class="btn-tactile bg-sky-50 hover:bg-sky-100 text-sky-800 border border-sky-300 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5">
                    <span id="gps-icon-1">📍</span>
                    <span id="gps-text-1">Check-in Obra</span>
                  </button>

                  <!-- Copiloto IA (In-Phone Bottom Sheet) -->
                  <button onclick="openInAppCopiloto(1, 'Constructora Bolívar', 'industrial')" class="btn-tactile bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5">
                    <span>⚡</span>
                    <span>Copiloto IA</span>
                  </button>

                  <!-- Escalamiento a Supervisor (In-Phone Bottom Sheet) -->
                  <button onclick="openInAppEscalamiento(1, 'Constructora Bolívar')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1">
                    <span>🚨</span>
                    <span>Escalar (SLA)</span>
                  </button>
                </div>

                <!-- Expandable 30-Day Interaction Timeline Button -->
                <div class="pt-1 border-t border-slate-100">
                  <button onclick="toggleTimeline(1)" class="w-full flex items-center justify-between text-[11px] font-bold text-slate-500 hover:text-slate-800 py-1 transition-all">
                    <span>📋 Historial de 30 Días (3 Registros)</span>
                    <span id="timeline-arrow-1" class="text-xs transition-transform">▼</span>
                  </button>
                  
                  <!-- Timeline Content -->
                  <div id="timeline-box-1" class="hidden mt-2 p-3 bg-slate-50 rounded-xl space-y-2 border border-slate-100 text-[11px]">
                    <div class="flex items-start space-x-2">
                      <span class="w-2 h-2 rounded-full bg-emerald-500 mt-1 flex-shrink-0"></span>
                      <div>
                        <strong class="text-slate-800 block">Cotización #4120 Enviada</strong>
                        <span class="text-slate-500 text-[10px]">Hace 4 días • 120 Ton Cemento Estructural ($31.800/saco)</span>
                      </div>
                    </div>
                    <div class="flex items-start space-x-2">
                      <span class="w-2 h-2 rounded-full bg-blue-500 mt-1 flex-shrink-0"></span>
                      <div>
                        <strong class="text-slate-800 block">Visita Técnica en Obra</strong>
                        <span class="text-slate-500 text-[10px]">Hace 12 días • Verificación de resistencia de probetas NTC 121</span>
                      </div>
                    </div>
                    <div class="flex items-start space-x-2">
                      <span class="w-2 h-2 rounded-full bg-amber-500 mt-1 flex-shrink-0"></span>
                      <div>
                        <strong class="text-slate-800 block">Llamada de Seguimiento</strong>
                        <span class="text-slate-500 text-[10px]">Hace 23 días • Cliente solicitó plazo a 45 días</span>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- ==================================================== -->
              <!-- CLIENT CARD 2: FERRETERÍA EL CONSTRUCTOR             -->
              <!-- ==================================================== -->
              <div id="card-client-2" class="bg-white rounded-2xl p-4 border border-rose-300 shadow-xs space-y-3 transition-all">
                
                <!-- Card Header -->
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Ferretería El Constructor</h3>
                      <span class="text-[10px] font-extrabold bg-amber-50 text-amber-700 border border-amber-200 px-1.5 py-0.5 rounded">Distribuidor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Sede Centro • Soledad</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 border border-rose-200 px-2 py-0.5 rounded-md">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                    <span>SIN PEDIDO (19d)</span>
                  </span>
                </div>

                <!-- Metrics Grid -->
                <div class="grid grid-cols-3 gap-2 text-center">
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Promedio</span>
                    <span class="font-mono-data font-bold text-slate-800 text-xs">45 Ton</span>
                  </div>
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Cupo Disp.</span>
                    <span class="font-mono-data font-bold text-emerald-600 text-xs">$18.2 M</span>
                  </div>
                  <div class="bg-slate-50 rounded-xl p-2 border border-slate-100">
                    <span class="text-[9px] uppercase font-bold text-slate-400 block">Margen</span>
                    <span class="font-mono-data font-bold text-slate-800 text-xs">14.2%</span>
                  </div>
                </div>

                <!-- Notice -->
                <div class="text-[11px] text-slate-600 bg-slate-50 border border-slate-200 rounded-xl p-2.5 flex items-start space-x-2">
                  <span class="text-blue-600 text-xs">💡</span>
                  <p class="leading-snug">Stock de Cemento Uso General agotado. Se puede activar despacho express con flete bonificado.</p>
                </div>

                <!-- Actions Matrix -->
                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Ferretería El Constructor', '45 Ton Cemento Uso General')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                    <span>💬</span>
                    <span>Chat WhatsApp</span>
                  </button>

                  <button onclick="realizarCheckInObra(2, 'Ferretería El Constructor')" class="btn-tactile bg-sky-50 hover:bg-sky-100 text-sky-800 border border-sky-300 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5">
                    <span id="gps-icon-2">📍</span>
                    <span id="gps-text-2">Check-in Local</span>
                  </button>

                  <button onclick="openInAppCopiloto(2, 'Ferretería El Constructor', 'ferreteria')" class="btn-tactile bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5">
                    <span>⚡</span>
                    <span>Copiloto IA</span>
                  </button>

                  <button onclick="openInAppEscalamiento(2, 'Ferretería El Constructor')" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1">
                    <span>🚨</span>
                    <span>Escalar Cupo</span>
                  </button>
                </div>

              </div>

              <!-- Footer Spacing -->
              <div class="h-10"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 2: COPILOTO IA INTEGRADO EN MÓVIL               -->
          <!-- ======================================================== -->
          <div id="screen-copiloto" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Copiloto Header Bar flush with notch -->
            <div class="bg-gradient-to-r from-slate-900 via-[#0033A0] to-[#004797] text-white px-4.5 pt-3.5 pb-3 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-3">
                  <div class="w-10 h-10 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-xl shadow-xs">
                    ⚡
                  </div>
                  <div>
                    <div class="flex items-center space-x-1.5">
                      <h2 class="font-bold text-sm tracking-tight text-white">Copiloto Comercial IA</h2>
                      <span class="text-[9px] bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 font-extrabold px-1.5 py-0.5 rounded-full uppercase">Activo</span>
                    </div>
                    <p class="text-[11px] text-blue-200">Fichas Técnicas NTC & Argumentos de Cierre</p>
                  </div>
                </div>
                
                <div class="text-right">
                  <span class="text-[9px] text-blue-200 block uppercase font-bold tracking-wider">Norma</span>
                  <span class="text-xs font-mono-data font-bold text-amber-300 bg-white/10 px-2 py-0.5 rounded-md border border-white/15">NTC 121</span>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">

            <!-- Client Quick Switcher -->
            <div class="bg-white p-4 rounded-2xl border border-slate-200/90 shadow-xs space-y-3">
              <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider">Cliente a asesorar:</label>
              <select id="cop-client-select" onchange="cambiarClienteCopiloto(this.value)" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-bold text-slate-800">
                <option value="1">Constructora Bolívar (120 Ton Cemento Estructural)</option>
                <option value="2">Ferretería El Constructor (45 Ton Cemento Uso General)</option>
              </select>

              <div class="pt-2 border-t border-slate-100">
                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">Ficha Técnica NTC:</label>
                <div class="bg-slate-50 rounded-xl p-3 border border-slate-200 text-xs space-y-2">
                  <div class="flex justify-between items-center">
                    <span class="font-bold text-slate-700">Producto:</span>
                    <span id="cop-prod-name" class="font-bold text-[#004797]">Cemento Estructural Max (NTC 121)</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-slate-500">Resistencia 28d:</span>
                    <span class="font-mono-data font-bold text-slate-800">≥ 35.0 MPa (5000 PSI)</span>
                  </div>
                  <div class="flex justify-between items-center">
                    <span class="text-slate-500">Fraguado Inicial:</span>
                    <span class="font-mono-data font-bold text-slate-800">120 minutos</span>
                  </div>
                </div>
              </div>

              <!-- Objections Handling -->
              <div class="pt-2 border-t border-slate-100">
                <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1.5">Manejo de Objeción Competencia:</label>
                <div class="bg-amber-50/80 border border-amber-200/80 rounded-xl p-3 text-xs space-y-1.5">
                  <strong class="text-amber-900 block font-bold">Objeción: "Argos me ofrece $500 pesos menos por saco"</strong>
                  <p class="text-slate-700 leading-snug">
                    <strong>Respuesta Ultracem:</strong> "Nuestro clinker de alta pureza alcanza la resistencia requerida 4 días antes, reduciendo en 15% el tiempo de formaleta y generando un ahorro neto superior a los $1.200 por metro cúbico vaciado."
                  </p>
                </div>
              </div>

              <!-- Button to open Live WhatsApp with generated argument -->
              <button onclick="openInAppWhatsApp('Constructora Bolívar', '120 Ton Cemento Estructural Max')" class="w-full btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-2">
                <span>💬</span>
                <span>Copiar y Enviar a WhatsApp del Cliente</span>
              </button>
            </div>

            <div class="h-8"></div>
            </div>
          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 3: LIGA DIAMANTE (RANKING ASESORES)             -->
          <!-- ======================================================== -->
          <div id="screen-liga" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Liga Header Bar flush with notch -->
            <div class="bg-gradient-to-r from-amber-600 via-orange-500 to-amber-500 text-white px-4.5 pt-3.5 pb-3 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div>
                  <span class="text-[9px] font-black uppercase tracking-widest text-amber-100 bg-black/20 px-2 py-0.5 rounded-md">División Regional Caribe</span>
                  <h2 class="font-black text-base tracking-tight text-white mt-1">Liga Diamante del Clinker</h2>
                  <p class="text-[11px] text-amber-100 mt-0.5">Cierre de temporada en 3 días • Top 3 asciende</p>
                </div>

                <div class="text-right flex flex-col items-end">
                  <div class="w-10 h-10 rounded-2xl bg-white/15 border border-white/30 flex items-center justify-center text-2xl shadow-sm">
                    💎
                  </div>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">

            <!-- Top 5 Leaderboard -->
            <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs divide-y divide-slate-100 overflow-hidden">
              
              <!-- Rank 1 -->
              <div class="p-3.5 flex items-center justify-between bg-amber-50/40">
                <div class="flex items-center space-x-3">
                  <span class="w-6 text-center font-black text-amber-600 text-sm">🥇</span>
                  <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80" alt="Andrés R." class="w-9 h-9 rounded-full object-cover border border-amber-300">
                  <div>
                    <h4 class="font-bold text-xs text-slate-900">Andrés Restrepo</h4>
                    <span class="text-[10px] text-slate-500">Bogotá Norte • 48d Racha</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="font-mono-data font-bold text-slate-900 text-xs">980 Ton</span>
                  <span class="text-[9px] text-amber-600 block font-semibold">+450 XP</span>
                </div>
              </div>

              <!-- Rank 2 -->
              <div class="p-3.5 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <span class="w-6 text-center font-bold text-slate-400 text-sm">🥈</span>
                  <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&auto=format&fit=crop&q=80" alt="Laura V." class="w-9 h-9 rounded-full object-cover">
                  <div>
                    <h4 class="font-bold text-xs text-slate-900">Laura Valencia</h4>
                    <span class="text-[10px] text-slate-500">Medellín • 34d Racha</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="font-mono-data font-bold text-slate-900 text-xs">840 Ton</span>
                  <span class="text-[9px] text-slate-500 block font-semibold">+320 XP</span>
                </div>
              </div>

              <!-- Rank 3: Carlos Mendoza (User Highlighted) -->
              <div class="p-3.5 flex items-center justify-between bg-blue-50/60 border-l-4 border-[#004797]">
                <div class="flex items-center space-x-3">
                  <span class="w-6 text-center font-black text-[#004797] text-sm">🥉</span>
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=80&auto=format&fit=crop&q=80" alt="Carlos M." class="w-9 h-9 rounded-full object-cover border-2 border-[#004797]">
                  <div>
                    <div class="flex items-center space-x-1">
                      <h4 class="font-bold text-xs text-slate-900">Carlos Mendoza (Tú)</h4>
                      <span class="text-[9px] bg-[#004797] text-white px-1.5 py-0.2 rounded font-bold">TOP 3</span>
                    </div>
                    <span class="text-[10px] text-[#004797] font-semibold">Caribe • 21d Racha 🔥</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="font-mono-data font-bold text-slate-900 text-xs">790 Ton</span>
                  <span class="text-[9px] text-[#004797] block font-bold">+280 XP</span>
                </div>
              </div>

              <!-- Rank 4 -->
              <div class="p-3.5 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                  <span class="w-6 text-center font-bold text-slate-400 text-xs">4</span>
                  <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Felipe M." class="w-9 h-9 rounded-full object-cover">
                  <div>
                    <h4 class="font-bold text-xs text-slate-900">Felipe Morales</h4>
                    <span class="text-[10px] text-slate-500">Cali Sur • 18d Racha</span>
                  </div>
                </div>
                <div class="text-right">
                  <span class="font-mono-data font-bold text-slate-900 text-xs">680 Ton</span>
                  <span class="text-[9px] text-slate-500 block font-semibold">+190 XP</span>
                </div>
              </div>

            </div>

            <div class="h-8"></div>
            </div>
          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 4: PERFIL, CASCO PROTECTOR & HEATMAP 90 DÍAS    -->
          <!-- ======================================================== -->
          <div id="screen-perfil" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Perfil Header Bar flush with notch -->
            <div class="bg-gradient-to-r from-[#002D80] via-[#003B99] to-[#004797] text-white px-4.5 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center space-x-3.5 relative z-10">
                <div class="relative">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-13 h-13 rounded-full border-2 border-white object-cover shadow-sm">
                  <span class="absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 rounded-full bg-emerald-400 border-2 border-[#002D80]"></span>
                </div>
                <div>
                  <div class="flex items-center space-x-2">
                    <h2 class="font-extrabold text-base tracking-tight text-white">Carlos Mendoza</h2>
                    <span class="bg-white/20 text-white font-extrabold text-[9px] px-1.5 py-0.5 rounded-full uppercase">Niv 4</span>
                  </div>
                  <p class="text-xs text-blue-100">Asesor Comercial Senior • Obras Atlántico</p>
                  <div class="flex items-center space-x-2 mt-1.5">
                    <span class="bg-white/15 border border-white/25 text-white font-bold text-[10px] px-2 py-0.5 rounded-full">Maestro Clinker</span>
                    <span class="text-[10px] text-amber-300 font-bold">★ 850 / 1000 XP</span>
                    <span class="text-[10px] text-orange-300 font-bold">🔥 21d</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">

            <!-- XP Progress Bar -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-slate-700">Progreso a Nivel 5 (Gran Maestro de Obra)</span>
                <span class="font-mono-data font-bold text-[#004797]">85%</span>
              </div>
              <div class="w-full bg-slate-100 h-3 rounded-full overflow-hidden p-0.5 border border-slate-200">
                <div class="bg-gradient-to-r from-blue-600 to-[#004797] h-full rounded-full transition-all duration-500" style="width: 85%"></div>
              </div>
              <p class="text-[10px] text-slate-500">Despacha 60 toneladas adicionales este mes para desbloquear el cupo autónomo de $80M.</p>
            </div>

            <!-- Casco Protector (Streak Freeze 24h) Inventory Card -->
            <div id="shield-inventory-card" class="bg-gradient-to-br from-amber-500 to-orange-600 text-white rounded-2xl p-4 shadow-md space-y-3">
              <div class="flex items-start justify-between">
                <div class="flex items-center space-x-2.5">
                  <span class="text-2xl">⛑️</span>
                  <div>
                    <h4 class="font-extrabold text-sm">Casco Protector (Streak Freeze)</h4>
                    <p class="text-[11px] text-amber-100">Congela tu racha por 24h en descansos o emergencias</p>
                  </div>
                </div>
                <span id="shield-status-badge" class="bg-white/20 font-extrabold text-[10px] px-2 py-0.5 rounded-full">1 DISPONIBLE</span>
              </div>

              <div class="bg-black/20 rounded-xl p-2.5 text-xs text-amber-100 leading-snug">
                Si no puedes registrar gestiones hoy por visita de planta o descanso de fin de semana, activa el Casco para no perder tus 21 días de racha.
              </div>

              <button id="btn-activate-shield" onclick="activarCascoProtector24h()" class="btn-tactile w-full bg-white text-orange-700 hover:bg-orange-50 font-black py-2.5 rounded-xl text-xs shadow-sm flex items-center justify-center space-x-1.5">
                <span>🛡️</span>
                <span>Equipar Casco (Congelar Racha 24h)</span>
              </button>
            </div>

            <!-- Heatmap de Actividad de 90 Días (Strict 8pt Symmetry) -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="font-extrabold text-xs text-slate-800 uppercase tracking-wider">Historial de Racha (90 Días)</h4>
                  <p class="text-[10px] text-slate-500">Constancia y gestiones diarias de Carlos</p>
                </div>
                <span class="font-mono-data font-bold text-xs text-[#004797]">21 Días Activo 🔥</span>
              </div>

              <!-- Clean 13-Week Grid (7 rows for Mon-Sun) -->
              <div class="flex space-x-2">
                <!-- Day Labels -->
                <div class="flex flex-col justify-between text-[9px] font-bold text-slate-400 py-0.5">
                  <span>L</span>
                  <span>M</span>
                  <span>V</span>
                  <span>D</span>
                </div>

                <!-- 13 Columns of Days (91 days total) -->
                <div class="flex-1 overflow-x-auto pb-1">
                  <div class="grid grid-flow-col grid-rows-7 gap-1">
                    <!-- Week 1 to 13 generated squares -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100" title="Día sin actividad"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-200" title="1 Gestión"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-300" title="2 Gestiones"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600" title="3 Gestiones"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-200"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>

                    <!-- Column 2 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-300"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-300"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 3 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 4 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-300"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 5 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 6 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 7 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 8 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 9 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-600"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>

                    <!-- Column 10 (Last 21 Days Streak Active) -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900 border border-amber-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-300"></div>

                    <!-- Column 11 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-700"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>

                    <!-- Column 12 -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-800"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-500"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-400"></div>

                    <!-- Column 13 (Today: Flame indicator) -->
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-blue-900"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-amber-500 ring-2 ring-amber-300 animate-pulse" title="Hoy: Racha activa de 21 días"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                    <div class="w-3.5 h-3.5 rounded-[3px] bg-slate-100"></div>
                  </div>
                </div>
              </div>

              <!-- Legend -->
              <div class="flex items-center justify-between text-[10px] text-slate-400 pt-1 border-t border-slate-100">
                <span>Hace 90 días</span>
                <div class="flex items-center space-x-1">
                  <span>Menos</span>
                  <span class="w-2.5 h-2.5 rounded-[2px] bg-slate-100 inline-block"></span>
                  <span class="w-2.5 h-2.5 rounded-[2px] bg-blue-200 inline-block"></span>
                  <span class="w-2.5 h-2.5 rounded-[2px] bg-blue-500 inline-block"></span>
                  <span class="w-2.5 h-2.5 rounded-[2px] bg-blue-900 inline-block"></span>
                  <span>Más</span>
                </div>
                <span>Hoy</span>
              </div>
            </div>

            <!-- Vitrina de 6 Trofeos (Balanced 2x3 Grid) -->
            <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="font-extrabold text-xs text-slate-800 uppercase tracking-wider">Vitrina de Trofeos</h4>
                <span class="text-[10px] text-slate-400">Toca para inspeccionar</span>
              </div>

              <div class="grid grid-cols-3 gap-2.5">
                
                <!-- Trophy 1 -->
                <button onclick="openInAppTrofeo('Centinela del Clinker', 'Mantén una racha ininterrumpida de 30 días gestionando cuentas críticas.', '🔥', '+150 XP')" class="btn-tactile bg-amber-50/70 border border-amber-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-amber-100/50">
                  <span class="text-2xl">🔥</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Centinela</span>
                  <span class="text-[8px] font-extrabold text-amber-700 bg-amber-200/80 px-1 rounded">21/30d</span>
                </button>

                <!-- Trophy 2 -->
                <button onclick="openInAppTrofeo('Titán de Obra', 'Despacha más de 500 toneladas de Cemento Estructural en un solo mes.', '🏗️', '+300 XP')" class="btn-tactile bg-blue-50/70 border border-blue-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-blue-100/50">
                  <span class="text-2xl">🏗️</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Titán Obra</span>
                  <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                </button>

                <!-- Trophy 3 -->
                <button onclick="openInAppTrofeo('Negociador Ágil', 'Responde y gestiona objeciones técnicas en menos de 1 hora mediante Copiloto.', '⚡', '+100 XP')" class="btn-tactile bg-purple-50/70 border border-purple-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-purple-100/50">
                  <span class="text-2xl">⚡</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Ágil SLA</span>
                  <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                </button>

                <!-- Trophy 4 -->
                <button onclick="openInAppTrofeo('Escudo Antichurn', 'Salva a 3 clientes en riesgo crítico antes de que cambien a la competencia.', '🛡️', '+200 XP')" class="btn-tactile bg-emerald-50/70 border border-emerald-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-emerald-100/50">
                  <span class="text-2xl">🛡️</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Antichurn</span>
                  <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                </button>

                <!-- Trophy 5 -->
                <button onclick="openInAppTrofeo('Maestro Técnico', 'Comparte 25 certificados NTC 121 y curvas de fraguado validadas por laboratorio.', '📐', '+120 XP')" class="btn-tactile bg-slate-50 border border-slate-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-slate-100">
                  <span class="text-2xl">📐</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Mtro Técnico</span>
                  <span class="text-[8px] font-extrabold text-slate-500 bg-slate-200 px-1 rounded">18/25</span>
                </button>

                <!-- Trophy 6 -->
                <button onclick="openInAppTrofeo('Líder Regional', 'Alcanza el Top 3 en la Liga Diamante durante 2 semanas consecutivas.', '👑', '+250 XP')" class="btn-tactile bg-amber-50/70 border border-amber-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-amber-100/50">
                  <span class="text-2xl">👑</span>
                  <span class="text-[10px] font-bold text-slate-800 leading-tight">Líder Caribe</span>
                  <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                </button>

              </div>
            </div>

            <div class="h-8"></div>
            </div>
          </div>

        </div>

        <!-- ========================================================== -->
        <!-- BOTTOM NAVIGATION BAR (FIXED INSIDE PHONE)                 -->
        <!-- ========================================================== -->
        <nav aria-label="Navegación Móvil" class="bg-white/95 backdrop-blur-md border-t border-slate-200/80 px-4 py-2.5 flex justify-around items-center select-none z-30">
          
          <button id="nav-btn-racha" onclick="navigateToTab('racha')" class="btn-tactile flex flex-col items-center text-[#004797] font-bold">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>
            </svg>
            <span class="text-[10px]">Racha</span>
          </button>

          <button id="nav-btn-copiloto" onclick="navigateToTab('copiloto')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
            <span class="text-[10px]">Copiloto</span>
          </button>

          <button id="nav-btn-liga" onclick="navigateToTab('liga')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
              <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/>
              <path d="M10 14.66V17c0 .55-.45 1-1 1H7v4h10v-4h-2c-.55 0-1-.45-1-1v-2.34"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/>
            </svg>
            <span class="text-[10px]">Liga</span>
          </button>

          <button id="nav-btn-perfil" onclick="navigateToTab('perfil')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            <span class="text-[10px]">Perfil</span>
          </button>

        </nav>

      </div>
    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA SUPERVISOR WEB (DASHBOARD ESCRITORIO COMPLETO)         -->
    <!-- ============================================================== -->
    <div id="view-web" class="hidden w-full max-w-6xl mx-auto space-y-6">
      
      <!-- Top Supervisor Summary Banner -->
      <div class="bg-gradient-to-r from-slate-900 to-[#004797] rounded-3xl p-6 text-white shadow-lg flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-blue-200">Panel de Control Regional • Caribe</span>
          <h2 class="text-2xl font-black tracking-tight mt-0.5">Control de Cartera, Rachas & Prevención Antichurn</h2>
          <p class="text-xs text-slate-300 mt-1">Supervisión en tiempo real de 18 asesores de campo y 240 obras activas.</p>
        </div>
        <div class="flex items-center space-x-3">
          <div class="bg-white/10 backdrop-blur-md rounded-2xl px-4 py-2 text-center border border-white/20">
            <span class="text-[10px] text-blue-200 block uppercase font-bold">Racha Promedio</span>
            <span class="text-xl font-black text-amber-300 font-mono-data">18.4 Días</span>
          </div>
          <div class="bg-white/10 backdrop-blur-md rounded-2xl px-4 py-2 text-center border border-white/20">
            <span class="text-[10px] text-blue-200 block uppercase font-bold">Cartera en Riesgo</span>
            <span class="text-xl font-black text-rose-300 font-mono-data">$184 M</span>
          </div>
        </div>
      </div>

      <!-- KPI Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
        <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs">
          <span class="text-xs font-bold text-slate-400 uppercase">Cuentas Críticas</span>
          <h3 class="text-2xl font-black text-rose-600 mt-1 font-mono-data">6 Obras</h3>
          <p class="text-[11px] text-slate-500 mt-0.5">SLA de contacto venciendo hoy</p>
        </div>
        <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs">
          <span class="text-xs font-bold text-slate-400 uppercase">Volumen en Riesgo</span>
          <h3 class="text-2xl font-black text-amber-600 mt-1 font-mono-data">480 Ton</h3>
          <p class="text-[11px] text-slate-500 mt-0.5">Equivalente a $152.6M COP</p>
        </div>
        <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs">
          <span class="text-xs font-bold text-slate-400 uppercase">Tasa de Salvamento</span>
          <h3 class="text-2xl font-black text-emerald-600 mt-1 font-mono-data">88.2%</h3>
          <p class="text-[11px] text-slate-500 mt-0.5">+4.2% con Don Fraguado IA</p>
        </div>
        <div class="bg-white rounded-2xl p-4 border border-slate-200 shadow-xs">
          <span class="text-xs font-bold text-slate-400 uppercase">Cascos Activos</span>
          <h3 class="text-2xl font-black text-[#004797] mt-1 font-mono-data">3 Asesores</h3>
          <p class="text-[11px] text-slate-500 mt-0.5">En congelación de racha 24h</p>
        </div>
      </div>

      <!-- Matrix of Accounts at Risk -->
      <div class="bg-white rounded-3xl border border-slate-200 shadow-xs overflow-hidden">
        <div class="p-5 border-b border-slate-100 flex items-center justify-between">
          <div>
            <h3 class="font-extrabold text-base text-slate-900">Radar Antichurn de Obras & Ferreterías</h3>
            <p class="text-xs text-slate-500">Cuentas que superaron su ventana habitual de reposición de cemento</p>
          </div>
          <button onclick="showToast('Informe exportado a Excel correctamente', 'success')" class="btn-tactile bg-[#004797] text-white text-xs font-bold px-3 py-1.5 rounded-xl">Descargar Reporte</button>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50 text-slate-400 uppercase font-bold text-[10px] tracking-wider border-b border-slate-100">
              <tr>
                <th class="py-3 px-5">Cliente / Obra</th>
                <th class="py-3 px-4">Asesor Asignado</th>
                <th class="py-3 px-4">Retraso / Riesgo</th>
                <th class="py-3 px-4">Volumen Mensual</th>
                <th class="py-3 px-4">Estado Racha</th>
                <th class="py-3 px-5 text-right">Acción Supervisor</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr class="hover:bg-slate-50/50">
                <td class="py-3.5 px-5 font-bold text-slate-900">
                  Constructora Bolívar
                  <span class="block text-[10px] font-normal text-slate-400">Torres del Mar • Barranquilla</span>
                </td>
                <td class="py-3.5 px-4 font-semibold text-slate-700">Carlos Mendoza (21d 🔥)</td>
                <td class="py-3.5 px-4">
                  <span class="bg-rose-100 text-rose-800 text-[10px] font-bold px-2 py-0.5 rounded-full">8 días atraso</span>
                </td>
                <td class="py-3.5 px-4 font-mono-data font-bold">120 Ton</td>
                <td class="py-3.5 px-4">
                  <span class="text-amber-600 font-bold">⚠️ Corte 11:59 PM</span>
                </td>
                <td class="py-3.5 px-5 text-right">
                  <button onclick="showToast('Notificación enviada a Carlos Mendoza por WhatsApp', 'info')" class="bg-emerald-50 text-emerald-700 border border-emerald-200 px-2.5 py-1 rounded-lg font-bold text-[11px] hover:bg-emerald-100">Contactar Asesor</button>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/50">
                <td class="py-3.5 px-5 font-bold text-slate-900">
                  Ferretería El Constructor
                  <span class="block text-[10px] font-normal text-slate-400">Sede Centro • Soledad</span>
                </td>
                <td class="py-3.5 px-4 font-semibold text-slate-700">Carlos Mendoza (21d 🔥)</td>
                <td class="py-3.5 px-4">
                  <span class="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full">4 días atraso</span>
                </td>
                <td class="py-3.5 px-4 font-mono-data font-bold">45 Ton</td>
                <td class="py-3.5 px-4">
                  <span class="text-amber-600 font-bold">⚠️ Corte 11:59 PM</span>
                </td>
                <td class="py-3.5 px-5 text-right">
                  <button onclick="showToast('Aprobación de cupo de $20M pre-autorizada', 'success')" class="bg-blue-50 text-blue-700 border border-blue-200 px-2.5 py-1 rounded-lg font-bold text-[11px] hover:bg-blue-100">Aprobar Cupo</button>
                </td>
              </tr>

              <tr class="hover:bg-slate-50/50">
                <td class="py-3.5 px-5 font-bold text-slate-900">
                  Concretos del Norte
                  <span class="block text-[10px] font-normal text-slate-400">Vía 40 • Barranquilla</span>
                </td>
                <td class="py-3.5 px-4 font-semibold text-slate-700">Andrés Restrepo (48d 🔥)</td>
                <td class="py-3.5 px-4">
                  <span class="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full">Gestionado Hoy</span>
                </td>
                <td class="py-3.5 px-4 font-mono-data font-bold">310 Ton</td>
                <td class="py-3.5 px-4">
                  <span class="text-emerald-600 font-bold">✓ Racha Protegida</span>
                </td>
                <td class="py-3.5 px-5 text-right">
                  <span class="text-slate-400 font-semibold text-[11px]">En Despacho</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

  </main>

  <!-- ============================================================== -->
  <!-- TOAST NOTIFICATION CONTAINER                                   -->
  <!-- ============================================================== -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>

  <!-- ============================================================== -->
  <!-- JAVASCRIPT: CONTROLLER, SIMULATION & AUDIO SYNTHESIS           -->
  <!-- ============================================================== -->
  <script>
    // Audio synthesis via Web Audio API (Zero external MP3 dependencies)
    let audioCtx = null;
    function getAudioContext() {{
      if (!audioCtx) {{
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }}
      return audioCtx;
    }}

    function playChime(type) {{
      try {{
        const ctx = getAudioContext();
        if (ctx.state === 'suspended') {{
          ctx.resume();
        }}
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        const now = ctx.currentTime;

        if (type === 'streak') {{
          // Duolingo victory chord: C5 -> E5 -> G5 -> C6
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.setValueAtTime(659.25, now + 0.1);
          osc.frequency.setValueAtTime(783.99, now + 0.2);
          osc.frequency.setValueAtTime(1046.50, now + 0.3);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
          osc.start(now);
          osc.stop(now + 0.7);
        }} else if (type === 'freeze') {{
          // Ice crystal chime
          osc.type = 'sine';
          osc.frequency.setValueAtTime(1200, now);
          osc.frequency.exponentialRampToValueAtTime(2400, now + 0.25);
          gain.gain.setValueAtTime(0.25, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
          osc.start(now);
          osc.stop(now + 0.5);
        }} else if (type === 'radar') {{
          // GPS radar ping
          osc.type = 'sine';
          osc.frequency.setValueAtTime(880, now);
          gain.gain.setValueAtTime(0.3, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.start(now);
          osc.stop(now + 0.3);
        }} else if (type === 'poke') {{
          // Cute squeak for Don Fraguado
          osc.type = 'sine';
          osc.frequency.setValueAtTime(450, now);
          osc.frequency.exponentialRampToValueAtTime(750, now + 0.15);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
          osc.start(now);
          osc.stop(now + 0.25);
        }} else {{
          // Tactile button click
          osc.type = 'sine';
          osc.frequency.setValueAtTime(400, now);
          gain.gain.setValueAtTime(0.08, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
          osc.start(now);
          osc.stop(now + 0.05);
        }}
      }} catch (e) {{
        console.warn("Audio Context error:", e);
      }}
    }}

    // State Variables
    let currentStreak = 21;
    let cascosDisponibles = 1;
    let isShieldActive = false;
    let currentActiveClientId = 1;
    let currentMascotState = 'normal'; // 'normal', 'panic', 'celebrate', 'frozen'

    // Mascot Poke Interaction
    function pokeMascot() {{
      playChime('poke');
      const container = document.getElementById('don-fraguado-container');
      container.classList.remove('mascot-breathing');
      container.classList.add('mascot-wiggle');
      
      const tips = [
        "“¡Recuerda! Los viernes el cemento debe programarse antes de las 3:00 PM.”",
        "“¡Ese es el espíritu! Un cliente visitado en obra tiene 3x más probabilidad de recompra.”",
        "“¡El Clinker Ultracem fragua con fuerza y resistencia garantizada!”",
        "“¿Sabías que el Cemento Estructural alcanza 35 MPa a los 28 días? ¡Un argumento ganador!”"
      ];
      const randomTip = tips[Math.floor(Math.random() * tips.length)];
      document.getElementById('mascot-speech').innerHTML = randomTip;

      setTimeout(() => {{
        container.classList.remove('mascot-wiggle');
        container.classList.add('mascot-breathing');
      }}, 500);
    }}

    // Update Mascot Visual State
    function setMascotExpression(state) {{
      currentMascotState = state;
      const eyesNormal = document.getElementById('eyes-normal');
      const eyesPanic = document.getElementById('eyes-panic');
      const eyesCelebrate = document.getElementById('eyes-celebrate');
      const eyesFrozen = document.getElementById('eyes-frozen');
      const particles = document.getElementById('mascot-particles');
      const container = document.getElementById('don-fraguado-container');

      [eyesNormal, eyesPanic, eyesCelebrate, eyesFrozen, particles].forEach(el => {{
        if (el) el.classList.add('hidden');
      }});
      container.classList.remove('mascot-panic', 'mascot-jump');

      if (state === 'panic') {{
        eyesPanic.classList.remove('hidden');
        container.classList.add('mascot-panic');
      }} else if (state === 'celebrate') {{
        eyesCelebrate.classList.remove('hidden');
        particles.classList.remove('hidden');
        container.classList.add('mascot-jump');
        setTimeout(() => {{
          setMascotExpression(isShieldActive ? 'frozen' : 'normal');
        }}, 4000);
      }} else if (state === 'frozen') {{
        eyesFrozen.classList.remove('hidden');
      }} else {{
        eyesNormal.classList.remove('hidden');
      }}
    }}

    // IN-PHONE BOTTOM SHEET HANDLER (Keeps everything 100% inside mobile frame)
    function openInPhoneSheet(icon, title, subtitle, htmlBody) {{
      playChime('click');
      document.getElementById('sheet-header-icon').textContent = icon;
      document.getElementById('sheet-header-title').textContent = title;
      document.getElementById('sheet-header-subtitle').textContent = subtitle;
      document.getElementById('inphone-sheet-body').innerHTML = htmlBody;
      
      const overlay = document.getElementById('inphone-sheet-overlay');
      overlay.classList.remove('hidden');
    }}

    function closeInPhoneSheet() {{
      playChime('click');
      document.getElementById('inphone-sheet-overlay').classList.add('hidden');
    }}

    // 1. In-Phone WhatsApp Chat Simulator
    function openInAppWhatsApp(clientName, pedido) {{
      const body = `
        <div class="bg-[#ECE5DD] -m-4 p-3 flex flex-col h-[400px]">
          <!-- WhatsApp Contact Bar -->
          <div class="bg-[#075E54] text-white p-2.5 -mx-3 -mt-3 flex items-center justify-between shadow-xs">
            <div class="flex items-center space-x-2">
              <div class="w-8 h-8 rounded-full bg-slate-200 text-[#075E54] font-black flex items-center justify-center text-xs">
                ${{clientName.charAt(0)}}
              </div>
              <div>
                <strong class="text-xs block leading-tight text-white">${{clientName}}</strong>
                <span class="text-[9px] text-emerald-200 block">En línea • Comprador Autorizado</span>
              </div>
            </div>
            <span class="text-xs text-white/80 font-bold">Ultracem Direct</span>
          </div>

          <!-- Chat Messages Container -->
          <div id="wa-messages-box" class="flex-1 overflow-y-auto p-2 space-y-2 text-xs">
            <div class="flex justify-center my-1">
              <span class="bg-white/80 text-slate-500 text-[9px] px-2 py-0.5 rounded shadow-xs">Hoy</span>
            </div>
            <div class="flex justify-end">
              <div class="bg-[#DCF8C6] p-2.5 rounded-xl rounded-tr-none shadow-xs max-w-[85%] text-slate-900">
                <p>Estimado cliente, un saludo cordial desde Ultracem. Le confirmamos la programación prioritaria de <strong>${{pedido}}</strong> con entrega programada y certificados NTC 121 incluidos.</p>
                <span class="text-[9px] text-emerald-800 block text-right mt-1">10:14 AM ✓✓</span>
              </div>
            </div>
          </div>

          <!-- Input Bar -->
          <div class="bg-white p-2 -mx-3 -mb-3 flex items-center space-x-1.5 border-t border-slate-200">
            <input type="text" id="wa-chat-input" placeholder="Escribe un mensaje de seguimiento..." class="flex-1 bg-slate-100 rounded-full px-3 py-1.5 text-xs text-slate-800 border-none focus:outline-none" value="Confirmar despacho para mañana a primera hora">
            <button onclick="sendInAppChatMessage('${{clientName}}')" class="w-8 h-8 rounded-full bg-[#128C7E] hover:bg-[#075E54] text-white flex items-center justify-center text-sm shadow-sm">
              ➤
            </button>
          </div>
        </div>
      `;
      openInPhoneSheet('💬', clientName, 'Simulador de Chat en Obra', body);
    }}

    function sendInAppChatMessage(clientName) {{
      playChime('click');
      const input = document.getElementById('wa-chat-input');
      const container = document.getElementById('wa-messages-box');
      if (!input || !input.value) return;

      const userBubble = document.createElement('div');
      userBubble.className = "flex justify-end";
      userBubble.innerHTML = `
        <div class="bg-[#DCF8C6] p-2.5 rounded-xl rounded-tr-none shadow-xs max-w-[85%] text-slate-900">
          <p>${{input.value}}</p>
          <span class="text-[9px] text-emerald-800 block text-right mt-1">10:16 AM ✓✓</span>
        </div>
      `;
      container.appendChild(userBubble);
      input.value = "";
      container.scrollTop = container.scrollHeight;

      // Simulated positive buyer response
      setTimeout(() => {{
        playChime('streak');
        const replyBubble = document.createElement('div');
        replyBubble.className = "flex justify-start";
        replyBubble.innerHTML = `
          <div class="bg-white p-2.5 rounded-xl rounded-tl-none shadow-xs max-w-[85%] text-slate-800">
            <p>¡Listo Carlos! Autorizado. Despáchame a primera hora. Muchas gracias por el seguimiento rápido.</p>
            <span class="text-[9px] text-slate-400 block text-right mt-1">10:16 AM</span>
          </div>
        `;
        container.appendChild(replyBubble);
        container.scrollTop = container.scrollHeight;

        // Save Streak Action
        salvarRachaCliente(currentActiveClientId, "Mensaje de WhatsApp verificado");
      }}, 1000);
    }}

    // 2. In-Phone Copiloto IA Sheet
    function openInAppCopiloto(clientId, clientName, type) {{
      currentActiveClientId = clientId;
      const isIndustrial = (type === 'industrial');
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-blue-50 border border-blue-200 rounded-xl p-3">
            <span class="font-bold text-[#004797] block text-xs">Argumento Técnico Personalizado</span>
            <p class="text-slate-700 mt-1 leading-snug">
              ${{isIndustrial 
                ? 'El Cemento Estructural Max cumple la norma NTC 121 tipo HE (Alta Resistencia Inicial). Permite desencofrar en 18h en lugar de 36h, ahorrando hasta $1.500/m³ en alquiler de formaleta.' 
                : 'El Cemento Uso General ofrece una trabajabilidad insuperable y retención de agua ideal para mampostería y pañetes sin fisuras.'
              }}
            </p>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 space-y-2">
            <div class="flex justify-between items-center">
              <span class="font-bold text-slate-700">Ficha de Resistencia:</span>
              <span class="font-mono-data font-bold text-[#004797]">≥ 35.0 MPa (28d)</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="font-bold text-slate-700">Tiempo de Fraguado:</span>
              <span class="font-mono-data font-bold text-slate-700">120 minutos</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="font-bold text-slate-700">Certificación NTC:</span>
              <span class="font-mono-data font-bold text-emerald-600">ICONTEC 121 Vigente</span>
            </div>
          </div>

          <!-- Calculadora de Volumen y Margen -->
          <div class="bg-amber-50/70 border border-amber-200/80 rounded-xl p-3 space-y-2">
            <div class="flex justify-between items-center">
              <strong class="text-amber-900 text-xs">Calculadora de Despacho:</strong>
              <span class="font-mono-data font-bold text-amber-700" id="calc-ton-val">120 Ton</span>
            </div>
            <input type="range" min="30" max="300" step="10" value="120" oninput="document.getElementById('calc-ton-val').textContent = this.value + ' Ton'" class="w-full accent-[#004797]">
            <p class="text-[10px] text-slate-500">Ajusta el pedido para recalcular la bonificación por flete directo desde planta Galapa.</p>
          </div>

          <div class="grid grid-cols-2 gap-2 pt-1">
            <button onclick="closeInPhoneSheet(); openInAppWhatsApp('${{clientName}}', '120 Ton Cemento')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>💬</span>
              <span>Enviar a WhatsApp</span>
            </button>
            <button onclick="salvarRachaCliente(${{clientId}}, 'Argumento técnico compartido'); closeInPhoneSheet();" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>✓</span>
              <span>Marcar Gestionado</span>
            </button>
          </div>
        </div>
      `;
      openInPhoneSheet('⚡', 'Copiloto IA: ' + clientName, 'Sugerencia de Cierre y Ficha NTC', body);
    }}

    // 3. In-Phone Escalamiento Sheet
    function openInAppEscalamiento(clientId, clientName) {{
      currentActiveClientId = clientId;
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-rose-50 border border-rose-200 rounded-xl p-3 flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <span class="text-lg">⏱️</span>
              <div>
                <strong class="text-rose-900 block font-bold">Compromiso SLA de Respuesta</strong>
                <span class="text-rose-700 text-[10px]">Supervisor Regional responde en &lt; 4 horas</span>
              </div>
            </div>
            <span class="font-mono-data font-bold text-rose-800 bg-rose-200/80 px-2 py-0.5 rounded text-[11px]">03:59:45</span>
          </div>

          <div class="space-y-1">
            <label class="block font-bold text-slate-700 text-xs">Motivo del Escalamiento:</label>
            <textarea id="esc-motivo-text" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 h-20 focus:outline-none" placeholder="Describe la solicitud del cliente...">Cliente solicita aprobación prioritaria de cupo a 45 días y envío de certificados NTC 121 para vaciado urgente.</textarea>
          </div>

          <div class="bg-slate-50 rounded-xl p-2.5 border border-slate-200 text-[11px] text-slate-600">
            Se notificará automáticamente al supervisor regional <strong>Martín Giraldo</strong> vía WhatsApp y correo institucional.
          </div>

          <button onclick="confirmarEscalamiento(${{clientId}})" class="btn-tactile w-full bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>🚨</span>
            <span>Confirmar y Enviar al Supervisor</span>
          </button>
        </div>
      `;
      openInPhoneSheet('🚨', 'Escalar: ' + clientName, 'Gestión con Supervisor Regional', body);
    }}

    // 4. In-Phone Trophy Detail Sheet
    function openInAppTrofeo(title, desc, icon, xp) {{
      const body = `
        <div class="text-center space-y-3 p-2">
          <div class="w-20 h-20 bg-amber-50 rounded-full border-2 border-amber-300 mx-auto flex items-center justify-center text-4xl shadow-inner">
            ${{icon}}
          </div>
          <div>
            <h4 class="font-black text-base text-slate-900">${{title}}</h4>
            <span class="inline-block bg-amber-100 text-amber-800 font-extrabold text-[10px] px-2.5 py-0.5 rounded-full mt-1">${{xp}} Comerciales</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed px-4">
            ${{desc}}
          </p>
          <div class="pt-2 border-t border-slate-100">
            <button onclick="closeInPhoneSheet()" class="btn-tactile w-full bg-slate-900 text-white font-bold text-xs py-2 rounded-xl">
              Cerrar Detalle
            </button>
          </div>
        </div>
      `;
      openInPhoneSheet(icon, title, 'Insignia Comercial Desbloqueable', body);
    }}

    // Check-in GPS en Obra
    function realizarCheckInObra(clientId, clientName) {{
      playChime('radar');
      const icon = document.getElementById('gps-icon-' + clientId);
      const text = document.getElementById('gps-text-' + clientId);
      
      icon.innerHTML = '<span class="inline-block w-3 h-3 rounded-full border-2 border-sky-600 border-t-transparent animate-spin"></span>';
      text.textContent = "Escaneando GPS...";

      setTimeout(() => {{
        playChime('streak');
        icon.textContent = "✓";
        text.textContent = "Obra Verificada";
        
        salvarRachaCliente(clientId, "Visita y Check-in GPS confirmados en obra");
        showToast("📍 Check-in en Obra verificado con éxito", "success");
      }}, 800);
    }}

    // Confirm Escalamiento
    function confirmarEscalamiento(clientId) {{
      playChime('streak');
      closeInPhoneSheet();
      
      const card = document.getElementById('card-client-' + clientId);
      if (card) {{
        card.classList.remove('border-rose-300');
        card.classList.add('border-amber-300', 'bg-amber-50/20');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-100 px-2 py-0.5 rounded-md border border-amber-300";
          badge.innerHTML = "<span>⏱️ EN REVISIÓN SUPERVISOR (SLA 4h)</span>";
        }}
      }}

      salvarRachaCliente(clientId, "Escalamiento a Supervisor enviado");
      showToast("🚨 Escalamiento enviado al supervisor regional", "info");
    }}

    // Save Streak Logic
    function salvarRachaCliente(clientId, motivo) {{
      currentStreak = 22;
      document.getElementById('streak-days').textContent = currentStreak;

      const card = document.getElementById('card-client-' + clientId);
      if (card) {{
        card.classList.remove('border-rose-300');
        card.classList.add('border-emerald-300', 'bg-emerald-50/20');
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {{
          badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded-md border border-emerald-300";
          badge.innerHTML = "<span>🟢 GESTIONADO HOY (Racha Protegida)</span>";
        }}
      }}

      // Mascot Celebrates
      setMascotExpression('celebrate');
      document.getElementById('mascot-speech').innerHTML = `“¡EXCELENTE TRABAJO! 🔥 ${{motivo}}. <strong>¡Tu racha subió a 22 días!</strong> El cemento fragua con disciplina.”`;
      
      showToast("🎉 ¡Racha protegida: 22 Días Activo! 🔥", "success");
    }}

    // Casco Protector 24h Freeze Shield
    function activarCascoProtector24h() {{
      if (cascosDisponibles <= 0) {{
        alert("Ya has consumido tus cascos protectores. Mantén una racha de 7 días continuos para desbloquear uno nuevo.");
        return;
      }}

      playChime('freeze');
      isShieldActive = true;
      cascosDisponibles--;

      document.getElementById('header-casco-count').textContent = "0 Cascos";
      document.getElementById('shield-status-badge').textContent = "❄️ ESCUDO ACTIVO 24H";
      document.getElementById('shield-status-badge').className = "bg-sky-400 text-white font-extrabold text-[10px] px-2 py-0.5 rounded-full animate-pulse";

      const card = document.getElementById('shield-inventory-card');
      card.className = "freeze-glow text-white rounded-2xl p-4 shadow-lg relative overflow-hidden transition-all duration-300 space-y-3";

      const btn = document.getElementById('btn-activate-shield');
      btn.innerHTML = "<span>🛡️ Racha Congelada por 24 Horas</span>";
      btn.disabled = true;
      btn.className = "w-full bg-white/20 backdrop-blur-md text-white font-black py-2.5 rounded-xl text-xs cursor-default";

      // Mascot enters Frost Mode
      setMascotExpression('frozen');
      document.getElementById('mascot-speech').innerHTML = '“¡MODO FRAGUADO PROTEGIDO! 🧊 Te has equipado el <strong>Casco Protector</strong>. Tu racha queda congelada por 24 horas ante cualquier emergencia. ¡Descansa seguro!”';
      
      showToast("❄️ ¡Casco Protector activado! Racha congelada 24h", "info");
    }}

    // Toggle 30-Day Timeline
    function toggleTimeline(id) {{
      playChime('click');
      const box = document.getElementById('timeline-box-' + id);
      const arrow = document.getElementById('timeline-arrow-' + id);
      if (box.classList.contains('hidden')) {{
        box.classList.remove('hidden');
        arrow.style.transform = 'rotate(180deg)';
      }} else {{
        box.classList.add('hidden');
        arrow.style.transform = 'rotate(0deg)';
      }}
    }}

    // Mobile Tabs Navigation (Racha, Copiloto, Liga, Perfil)
    function navigateToTab(tab) {{
      playChime('click');
      const screens = {{
        racha: document.getElementById('screen-racha'),
        copiloto: document.getElementById('screen-copiloto'),
        liga: document.getElementById('screen-liga'),
        perfil: document.getElementById('screen-perfil')
      }};

      const buttons = {{
        racha: document.getElementById('nav-btn-racha'),
        copiloto: document.getElementById('nav-btn-copiloto'),
        liga: document.getElementById('nav-btn-liga'),
        perfil: document.getElementById('nav-btn-perfil')
      }};

      // Hide all screens
      Object.values(screens).forEach(s => s && s.classList.add('hidden'));
      // Reset button styles
      Object.values(buttons).forEach(b => {{
        if (b) b.className = "btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold";
      }});

      if (screens[tab]) {{
        screens[tab].classList.remove('hidden');
      }}
      if (buttons[tab]) {{
        buttons[tab].className = "btn-tactile flex flex-col items-center text-[#004797] font-bold";
      }}
    }}

    // Time Mode Simulator (10:00 AM vs 10:45 PM Cierre)
    function setTimeMode(mode) {{
      playChime('click');
      const btnDay = document.getElementById('btn-time-day');
      const btnNight = document.getElementById('btn-time-night');
      const phoneClock = document.getElementById('phone-clock');
      const countdown = document.getElementById('countdown-timer');

      if (mode === 'night') {{
        btnDay.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        btnNight.className = "px-2.5 py-1 rounded-lg font-bold bg-rose-600 text-white text-[11px] transition-all";
        phoneClock.textContent = "10:45 PM";
        countdown.textContent = "01h : 14m : 02s";
        countdown.className = "font-mono-data font-black text-rose-300 bg-rose-950/80 px-2 py-0.5 rounded text-[11px] animate-pulse";

        // Trigger Mascot Panic
        setMascotExpression('panic');
        document.getElementById('mascot-speech').innerHTML = '“¡CARLOS! Faltan solo <strong>74 minutos para el corte</strong> de las 11:59 PM 😱. Tienes cuentas críticas sin gestionar. ¡Haz el Check-in o perderás tus 21 días de racha!”';
        
        showToast("🌙 Modo 10:45 PM: ¡Riesgo inminente de perder la racha!", "warning");
      }} else {{
        btnDay.className = "px-2.5 py-1 rounded-lg font-bold bg-slate-900 text-white text-[11px] transition-all";
        btnNight.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        phoneClock.textContent = "10:00 AM";
        countdown.textContent = "13h : 59m : 12s";
        countdown.className = "font-mono-data font-bold text-amber-300 bg-black/30 px-2 py-0.5 rounded text-[11px]";

        setMascotExpression(isShieldActive ? 'frozen' : 'normal');
        document.getElementById('mascot-speech').innerHTML = '“¡Buenos días Carlos! Tienes <strong>2 cuentas prioritarias</strong> hoy. Registra un Check-in GPS o envía mensaje para asegurar tu racha de 21 días 🔥.”';
      }}
    }}

    // Switch between Asesor Mobile and Supervisor Web
    function switchView(view) {{
      playChime('click');
      const viewMobile = document.getElementById('view-mobile');
      const viewWeb = document.getElementById('view-web');
      const btnMobile = document.getElementById('btn-view-mobile');
      const btnWeb = document.getElementById('btn-view-web');

      if (view === 'web') {{
        viewMobile.classList.add('hidden');
        viewWeb.classList.remove('hidden');
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs";
      }} else {{
        viewWeb.classList.add('hidden');
        viewMobile.classList.remove('hidden');
        btnWeb.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900";
        btnMobile.className = "btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs";
      }}
    }}

    // Toast Notifications
    function showToast(message, type) {{
      const container = document.getElementById('toast-container');
      const toast = document.createElement('div');
      
      let borderClass = "border-slate-800 bg-slate-900 text-white";
      if (type === 'success') borderClass = "border-emerald-600 bg-emerald-900 text-white";
      if (type === 'warning') borderClass = "border-amber-600 bg-amber-900 text-white";
      if (type === 'info') borderClass = "border-blue-600 bg-[#004797] text-white";

      toast.className = `p-3 rounded-2xl shadow-xl border text-xs font-bold flex items-center space-x-2 transition-all duration-300 transform translate-y-2 pointer-events-auto ${{borderClass}}`;
      toast.innerHTML = `<span>${{message}}</span>`;
      container.appendChild(toast);

      setTimeout(() => {{
        toast.classList.remove('translate-y-2');
      }}, 10);

      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-2');
        setTimeout(() => toast.remove(), 300);
      }}, 3200);
    }}
  </script>
</body>
</html>
'''

# Compile to index.html
output_index_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\COOWEB\index.html"
with open(output_index_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Compiled successfully: {output_index_path}")

# Compile to brain artifact
artifact_path = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
with open(artifact_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Compiled successfully: {artifact_path}")
