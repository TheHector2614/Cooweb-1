# -*- coding: utf-8 -*-
"""
Generates the Comprehensive Master PRD & Brand Book for Ultracem CRM.
100% PURE ULTRACEM S.A.S. BRANDING (Zero Semillero / CooWeb).
Colors: Amarillo (#FDCA02), Azul Oscuro (#003E78 / #0A233F), and Blanco (#FFFFFF).
100% SOLID COLORS (zero gradients).
"""

def get_prd_html():
    return r'''
      <!-- ============================================================== -->
      <!-- PRD MASTER DOCUMENT & BRAND SCRIPT: ULTRACEM S.A.S.             -->
      <!-- ============================================================== -->
      
      <!-- Document Header & Meta Bar -->
      <header class="border-b-4 border-[#FDCA02] pb-8 space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center space-x-3.5">
            <!-- Ultracem Official Logo Icon with Crisp White Background & Solid Yellow Border -->
            <div class="h-14 px-4 rounded-2xl bg-white border-2 border-[#FDCA02] flex items-center justify-center shadow-xs">
              <img src="data:image/png;base64,{logo_base64}" alt="Ultracem Cemento & Concreto" class="h-9 w-auto object-contain" />
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xs font-black uppercase tracking-wider text-[#003E78] bg-blue-100/70 px-2.5 py-0.5 rounded-full border border-blue-300">ULTRACEM S.A.S.</span>
                <span class="text-xs font-bold text-slate-400">•</span>
                <span class="text-xs font-black uppercase tracking-wider text-amber-900 bg-amber-100/80 px-2.5 py-0.5 rounded-full border border-amber-300">PLANTA GALAPA, ATLÁNTICO</span>
              </div>
              <p class="text-xs text-slate-600 font-semibold mt-0.5">Documento de Especificación de Producto (PRD) & Manual de Marca • Versión 2.0 Oficial</p>
            </div>
          </div>
          
          <div class="flex items-center space-x-2.5">
            <span class="inline-flex items-center px-3.5 py-1.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-900 border border-emerald-300">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 mr-2"></span>
              Plataforma Operativa en Producción
            </span>
            <button onclick="window.print()" class="btn-tactile text-xs font-bold text-[#003E78] hover:text-white bg-amber-100 hover:bg-[#003E78] px-3.5 py-1.5 rounded-xl border-2 border-[#FDCA02] transition-all flex items-center space-x-1.5 shadow-xs" title="Imprimir / Exportar a PDF">
              <span>📄</span>
              <span class="hidden sm:inline">Exportar PRD</span>
            </button>
          </div>
        </div>

        <div>
          <h1 class="text-3xl sm:text-4xl font-black text-[#003E78] tracking-tight leading-tight">
            UltraRacha CRM: Ecosistema Comercial Gamificado, Prevención Antichurn & Copiloto IA de Terreno
          </h1>
          <p class="text-base text-slate-700 mt-3 leading-relaxed">
            Plataforma de alta productividad e inteligencia comercial diseñada a la medida de la fuerza de ventas técnica de <strong>Ultracem S.A.S.</strong> en el Caribe colombiano. Transforma la fricción operativa de la gestión de pedidos de cemento y concreto en un hábito diario innegociable a través de rachas comerciales con corte a las 11:59 PM, acompañamiento del copiloto IA certificado bajo norma técnica <strong>NTC 121</strong>, y cartografía georreferenciada de obras e infraestructura.
          </p>
        </div>

        <!-- Metadata Ribbon -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
          <div class="bg-white p-3.5 rounded-xl border-2 border-slate-200">
            <span class="text-slate-500 block font-bold text-[10px] uppercase">Lema Institucional</span>
            <span class="font-extrabold text-[#003E78]">“Calidad, Resistencia y Rendimiento”</span>
          </div>
          <div class="bg-white p-3.5 rounded-xl border-2 border-slate-200">
            <span class="text-slate-500 block font-bold text-[10px] uppercase">Epicentro Operativo</span>
            <span class="font-extrabold text-[#003E78]">Planta Galapa • Km 8 Vía Tubará</span>
          </div>
          <div class="bg-white p-3.5 rounded-xl border-2 border-slate-200">
            <span class="text-slate-500 block font-bold text-[10px] uppercase">Infraestructura IA</span>
            <span class="font-extrabold text-[#003E78]">Groq LPU, NVIDIA NIM & DeepSeek</span>
          </div>
          <div class="bg-white p-3.5 rounded-xl border-2 border-slate-200">
            <span class="text-slate-500 block font-bold text-[10px] uppercase">Regla de Oro Antichurn</span>
            <span class="font-extrabold text-[#D9531E]">Corte Diario Estricto 11:59 PM</span>
          </div>
        </div>
      </header>

      <!-- SECCIÓN 1: GUION DE BRANDING Y FILOSOFÍA CORPORATIVA -->
      <section class="space-y-5 pt-4">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#FDCA02] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">1. Guion de Branding & Filosofía Operativa Ultracem</h2>
        </div>
        
        <div class="bg-[#003E78] rounded-3xl p-6 sm:p-8 text-white space-y-4 border-l-8 border-[#FDCA02] shadow-sm">
          <div class="flex items-center justify-between flex-wrap gap-2">
            <span class="text-[11px] font-black uppercase tracking-widest text-[#FDCA02] bg-[#0A233F] px-3 py-1 rounded-full border border-amber-400/40">Manifiesto Comercial Ultracem</span>
            <span class="text-xs text-blue-200 font-mono-data">Planta Galapa • 1.2M Ton/Año</span>
          </div>
          <p class="text-xl sm:text-2xl font-black leading-snug italic text-white">
            “Que el cemento fragüe, pero que tu cliente nunca se enfríe.”
          </p>
          <p class="text-sm text-blue-100 leading-relaxed">
            En la industria del cemento y el concreto premezclado, las decisiones de compra no se toman en salas de juntas alfombradas con semanas de anticipación; se toman a pie de obra, frente al vaciado de una losa o en el mostrador de una ferretería con clientes esperando bultos. Si un asesor de Ultracem tarda más de 24 horas en responder una cotización técnica o en desbloquear un cupo de cartera, el contratista compra de inmediato a Argos o Cemex. <strong>UltraRacha CRM</strong> nace para erradicar la procrastinación comercial y garantizar presencia activa en cada obra del Caribe colombiano.
          </p>
        </div>

        <!-- Los 3 Pilares de Marca -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
          <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-2.5">
            <div class="w-9 h-9 rounded-xl bg-amber-100 text-[#003E78] flex items-center justify-center font-black text-base border border-[#FDCA02]">1</div>
            <h3 class="font-black text-sm text-[#003E78]">Calidad Certificada (NTC 121 & 321)</h3>
            <p class="text-slate-600 leading-relaxed">
              Cada bulto de Cemento Estructural Max y Concreto Ultracem cumple con los más rigurosos ensayos de resistencia a la compresión a los 3, 7 y 28 días, respaldados por el laboratorio central de Planta Galapa.
            </p>
          </div>
          <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-2.5">
            <div class="w-9 h-9 rounded-xl bg-blue-100 text-[#003E78] flex items-center justify-center font-black text-base border border-blue-300">2</div>
            <h3 class="font-black text-sm text-[#003E78]">Resistencia Temprana Superior</h3>
            <p class="text-slate-600 leading-relaxed">
              La curva de fraguado de Ultracem permite desencofrar placas y columnas hasta 24 horas antes que la competencia, generando ahorros directos millonarios en alquiler de formaleta y mano de obra para las constructoras.
            </p>
          </div>
          <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-2.5">
            <div class="w-9 h-9 rounded-xl bg-emerald-100 text-emerald-900 flex items-center justify-center font-black text-base border border-emerald-300">3</div>
            <h3 class="font-black text-sm text-[#003E78]">Rendimiento Logístico Caribeño</h3>
            <p class="text-slate-600 leading-relaxed">
              Despacho ininterrumpido desde Galapa con flota propia de tractomulas y camiones mixer hacia Barranquilla, Soledad, Cartagena, Santa Marta, Valledupar y Montería, garantizando entregas 'Just in Time'.
            </p>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 2: MANUAL DE IDENTIDAD VISUAL Y PALETA SÓLIDA -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#003E78] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">2. Manual de Identidad Visual: Colores Sólidos Oficiales</h2>
        </div>

        <p class="text-sm text-slate-700 leading-relaxed">
          La identidad visual de Ultracem en UltraRacha CRM se rige bajo una regla estricta: <strong>100% colores sólidos, sin degradados ni efectos difusos</strong>. Esta decisión de diseño evoca la solidez del concreto endurecido, la claridad del sol caribeño y la estética neo-brutalista de la infraestructura pesada, garantizando máxima legibilidad tanto bajo el sol directo en obra como en monitores de oficina.
        </p>

        <!-- Grilla de Colores Sólidos Primarios -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-xs">
          <!-- Azul Ultracem -->
          <div class="bg-white border-2 border-[#003E78] rounded-2xl p-4 space-y-2 shadow-xs">
            <div class="h-14 rounded-xl bg-[#003E78] mb-2 flex items-center justify-center text-white font-black text-xs">PRIMARIO</div>
            <span class="font-black text-slate-900 block text-sm">Azul Ultracem</span>
            <div class="space-y-0.5 text-[11px] font-mono-data text-slate-600">
              <p>HEX: <strong class="text-[#003E78]">#003E78</strong></p>
              <p>RGB: 0, 62, 120</p>
              <p>Rol: Cabeceras, identidad institucional, botones secundarios.</p>
            </div>
          </div>

          <!-- Amarillo Ultracem -->
          <div class="bg-white border-2 border-[#FDCA02] rounded-2xl p-4 space-y-2 shadow-xs">
            <div class="h-14 rounded-xl bg-[#FDCA02] mb-2 flex items-center justify-center text-[#003E78] font-black text-xs">ACENTO</div>
            <span class="font-black text-slate-900 block text-sm">Amarillo Ultracem</span>
            <div class="space-y-0.5 text-[11px] font-mono-data text-slate-600">
              <p>HEX: <strong class="text-amber-800">#FDCA02</strong></p>
              <p>RGB: 253, 202, 2</p>
              <p>Rol: Fuego de racha, cascos, botones de acción primaria, bordes clave.</p>
            </div>
          </div>

          <!-- Azul Marino Profundo -->
          <div class="bg-white border-2 border-[#0A233F] rounded-2xl p-4 space-y-2 shadow-xs">
            <div class="h-14 rounded-xl bg-[#0A233F] mb-2 flex items-center justify-center text-white font-black text-xs">SUPERFICIE</div>
            <span class="font-black text-slate-900 block text-sm">Azul Marino Fondo</span>
            <div class="space-y-0.5 text-[11px] font-mono-data text-slate-600">
              <p>HEX: <strong class="text-[#0A233F]">#0A233F</strong></p>
              <p>RGB: 10, 35, 63</p>
              <p>Rol: Sidebar corporativo, barras de herramientas de control.</p>
            </div>
          </div>

          <!-- Blanco Puro -->
          <div class="bg-white border-2 border-slate-300 rounded-2xl p-4 space-y-2 shadow-xs">
            <div class="h-14 rounded-xl bg-white border-2 border-slate-300 mb-2 flex items-center justify-center text-slate-800 font-black text-xs">CONTENIDO</div>
            <span class="font-black text-slate-900 block text-sm">Blanco Puro</span>
            <div class="space-y-0.5 text-[11px] font-mono-data text-slate-600">
              <p>HEX: <strong class="text-slate-900">#FFFFFF</strong></p>
              <p>RGB: 255, 255, 255</p>
              <p>Rol: Tarjetas de clientes, consolas, contenedores de datos.</p>
            </div>
          </div>
        </div>

        <div class="bg-amber-50 rounded-2xl p-4 border-2 border-amber-300 text-xs text-amber-950 flex items-start space-x-3">
          <span class="text-xl">⚠️</span>
          <div>
            <strong>Regla de Diseño Inviolable:</strong> Queda estrictamente vetado el uso de degradados de color en la interfaz. Todos los fondos, barras y botones deben presentarse con tintas sólidas y bordes de contraste definido, garantizando la identidad de marca industrial establecida.
          </div>
        </div>
      </section>

      <!-- SECCIÓN 3: EL PERSONAJE DON FRAGUADO Y SU PSICOLOGÍA -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#FDCA02] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">3. El Personaje Don Fraguado: Storytelling, Psicología y Guion de Voz</h2>
        </div>

        <div class="bg-white rounded-3xl p-6 sm:p-8 border-2 border-slate-200 space-y-5">
          <div class="flex flex-col sm:flex-row items-center sm:items-start gap-5">
            <!-- Don Fraguado Badge / Mascot Display -->
            <div class="w-24 h-28 bg-[#F2F1EC] rounded-2xl p-2 border-2 border-[#FDCA02] flex items-center justify-center flex-shrink-0 shadow-xs">
              <div class="relative w-20 h-24">
                <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm" xmlns="http://www.w3.org/2000/svg">
                  <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />
                  <g class="origin-bottom">
                    <path d="M 18,36 L 82,36 Q 88,36 89,45 L 92,94 Q 93,101 84,101 L 16,101 Q 7,101 8,94 L 11,45 Q 12,36 18,36 Z" fill="#94A3B8" />
                    <path d="M 18,34 L 82,34 Q 88,34 89,43 L 92,90 Q 93,97 84,97 L 16,97 Q 7,97 8,90 L 11,43 Q 12,34 18,34 Z" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.8" />
                    <path d="M 10,68 L 90,68 L 91,80 L 9,80 Z" fill="#003E78" />
                    <text x="50" y="77" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-weight="900" font-size="7.5" text-anchor="middle" letter-spacing="1">ULTRACEM</text>
                    <rect x="35" y="83" width="30" height="6.5" rx="3" fill="#FDCA02" />
                    <text x="50" y="88" fill="#003E78" font-family="'JetBrains Mono', monospace" font-weight="700" font-size="4.5" text-anchor="middle">50 kg • NTC</text>
                    <g>
                      <ellipse cx="37" cy="52" rx="7.5" ry="9" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.8" />
                      <circle cx="38" cy="52" r="3.8" fill="#0F172A" />
                      <circle cx="40" cy="50" r="1.5" fill="#FFFFFF" />
                      <ellipse cx="63" cy="52" rx="7.5" ry="9" fill="#FFFFFF" stroke="#1E293B" stroke-width="1.8" />
                      <circle cx="62" cy="52" r="3.8" fill="#0F172A" />
                      <circle cx="64" cy="50" r="1.5" fill="#FFFFFF" />
                      <circle cx="28" cy="58" r="3" fill="#F43F5E" opacity="0.35" />
                      <circle cx="72" cy="58" r="3" fill="#F43F5E" opacity="0.35" />
                      <path d="M 44,61 Q 50,66 56,61" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" />
                    </g>
                    <!-- Hard Hat -->
                    <g>
                      <path d="M 14,33 Q 50,38 86,33 Q 50,42 14,33 Z" fill="#92400E" opacity="0.7" />
                      <path d="M 20,31 C 20,14 32,8 50,8 C 68,8 80,14 80,31 Z" fill="#FDCA02" />
                      <path d="M 46,8 L 54,8 L 54,30 L 46,30 Z" fill="#EAB308" />
                      <path d="M 12,30 C 22,27 78,27 88,30 C 90,32 86,34 82,34 C 54,36 46,36 18,34 C 14,34 10,32 12,30 Z" fill="#CA8A04" />
                      <circle cx="50" cy="20" r="4.5" fill="#003E78" stroke="#FFFFFF" stroke-width="1" />
                    </g>
                  </svg>
                </svg>
              </div>
            </div>

            <div class="space-y-2 text-xs">
              <h3 class="text-base font-black text-[#003E78]">Don Fraguado: El Mentor Concretero de Ultracem</h3>
              <p class="text-slate-700 leading-relaxed">
                <strong>Don Fraguado</strong> es la personificación viva del bulto de 50 kg de Cemento Gris Estructural Max Ultracem. Lleva su casco amarillo reglamentario con el escudo corporativo de Ultracem y encarna la voz de la experiencia en la obra civil. No es un simple bot; es el compañero leal del asesor que celebra sus victorias comerciales, advierte los riesgos de pérdida de clientes y activa alarmas enérgicas cuando el corte de las 11:59 PM se aproxima.
              </p>
            </div>
          </div>

          <!-- Los 4 Estados Emocionales -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs pt-3">
            <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200 space-y-1.5">
              <div class="flex items-center space-x-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <strong class="text-slate-900">1. Motivado (Día)</strong>
              </div>
              <p class="text-[11px] text-slate-600">
                Ojos amigables y sonrisa. Alienta al asesor en la mañana: <em>"¡Carlos! Tienes 3 obras por visitar hoy. Cada bulto colocado defiende el territorio Ultracem."</em>
              </p>
            </div>

            <div class="bg-rose-50 p-3.5 rounded-xl border border-rose-200 space-y-1.5">
              <div class="flex items-center space-x-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-rose-600 animate-pulse"></span>
                <strong class="text-rose-900">2. Pánico Fraguado (Noche)</strong>
              </div>
              <p class="text-[11px] text-rose-800">
                Pupilas contraídas y gota de sudor. A partir de las 10:45 PM: <em>"¡Pilas! Faltan 74 minutos para las 11:59 PM. Escala a Cartera o perderás tu racha de 21 días."</em>
              </p>
            </div>

            <div class="bg-amber-50 p-3.5 rounded-xl border border-amber-300 space-y-1.5">
              <div class="flex items-center space-x-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
                <strong class="text-amber-900">3. Victoria (Celebración)</strong>
              </div>
              <p class="text-[11px] text-amber-800">
                Ojos en media luna, confeti y salto. Al salvar la racha: <em>"¡Golazo comercial! Racha protegida, +150 XP y despacho garantizado desde Planta Galapa."</em>
              </p>
            </div>

            <div class="bg-blue-50 p-3.5 rounded-xl border border-blue-200 space-y-1.5">
              <div class="flex items-center space-x-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
                <strong class="text-blue-900">4. Criogénico (Casco)</strong>
              </div>
              <p class="text-[11px] text-blue-800">
                Casco escarchado e íconos de hielo. Cuando se activa el Casco Protector: <em>"Modo freeze activo por 24h. Descansa tranquilo; tu racha no sufrirá daños."</em>
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 4: LA ARQUITECTURA DE RACHAS Y EL CORTE 11:59 PM -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#003E78] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">4. Mecánica de Gamificación & Prevención Antichurn</h2>
        </div>

        <div class="space-y-4 text-xs">
          <!-- Regla del Corte 11:59 PM -->
          <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-3">
            <h3 class="text-base font-black text-[#003E78] flex items-center space-x-2">
              <span>⏰</span>
              <span>La Justificación Operativa del Corte 11:59 PM</span>
            </h3>
            <p class="text-slate-700 leading-relaxed">
              En la logística pesada de Ultracem, la programación de los despachos de Planta Galapa para el día siguiente se congela a la medianoche. Los trenes de molienda y la asignación de tractomulas inician a las 4:30 AM para que el cemento llegue a las obras a primera hora de la mañana (6:30 AM). Por ello, el asesor comercial tiene hasta las <strong>11:59 PM</strong> para registrar una de las 4 acciones de salvaguarda de racha. Si el reloj marca las 12:00 AM sin gestión, la cuenta entra en riesgo crítico de churn y la racha se congela o se rompe.
            </p>
          </div>

          <!-- Semáforos de Recompra -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <div class="bg-emerald-50 border-2 border-emerald-300 rounded-2xl p-4 space-y-1.5">
              <span class="text-xs font-black text-emerald-900 uppercase">🟢 Semáforo Verde (Al Día)</span>
              <p class="text-[11px] text-emerald-800">
                0 a 3 días desde el último pedido. La obra está consumiendo cemento según su cronograma de vaciado o la ferretería mantiene stock adecuado.
              </p>
            </div>
            <div class="bg-amber-50 border-2 border-amber-300 rounded-2xl p-4 space-y-1.5">
              <span class="text-xs font-black text-amber-900 uppercase">🟡 Semáforo Amarillo (Atención)</span>
              <p class="text-[11px] text-amber-800">
                4 a 6 días sin pedido. Alerta de desaceleración. Es probable que la obra esté cotizando con distribuidores de Argos o Cemex. Requiere contacto comercial inmediato.
              </p>
            </div>
            <div class="bg-rose-50 border-2 border-rose-300 rounded-2xl p-4 space-y-1.5">
              <span class="text-xs font-black text-rose-900 uppercase">🔴 Semáforo Rojo (Peligro Churn)</span>
              <p class="text-[11px] text-rose-800">
                7+ días sin pedido. Pérdida inminente del cliente. Si no se escala o atiende antes de las 11:59 PM, la cuenta pasa a auditoría de supervisión y se pierde la racha.
              </p>
            </div>
          </div>

          <!-- Las 4 Acciones de Salvamento -->
          <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-3">
            <h3 class="text-base font-black text-[#003E78]">Las 4 Acciones Válidas de Salvaguarda de Racha (+100 a +150 XP)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-[#003E78] block">1. Check-in GPS Georreferenciado (+100 XP)</strong>
                <span class="text-[11px] text-slate-600">Registro con geocerca de 100m en el frente de obra o en la ferretería aliada.</span>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-[#003E78] block">2. Nota de Voz Procesada por Whisper (+120 XP)</strong>
                <span class="text-[11px] text-slate-600">Grabación de 15-45 segundos resumiendo los requerimientos de la visita, transcrita por IA.</span>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-[#003E78] block">3. Mensaje Técnico vía WhatsApp (+80 XP)</strong>
                <span class="text-[11px] text-slate-600">Envío de cotización formal o argumento de dosificación generado por el Copiloto IA.</span>
              </div>
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <strong class="text-[#003E78] block">4. Escalamiento Departamental con SLA (+150 XP)</strong>
                <span class="text-[11px] text-slate-600">Transferencia de bloqueo a Cartera (4h), Logística (2h) o Calidad (8h). Salva la racha al instante.</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 5: COPILOTO IA, GUARDRAILS NTC 121 Y CONSOLA DE VOZ -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#FDCA02] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">5. Copiloto IA Multimodelo & Consola de Voz Whisper</h2>
        </div>

        <div class="space-y-4 text-xs">
          <p class="text-sm text-slate-700 leading-relaxed">
            El Copiloto IA de Ultracem está integrado de manera nativa con motores de inferencia de última generación: <strong>Groq LPU (Llama 3.3 70B y 8B Instant)</strong>, <strong>NVIDIA NIM (Llama 3 70B Instruct, Mistral NeMo)</strong>, <strong>DeepSeek V3</strong> y <strong>OpenAI</strong>.
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Guardrails Técnicos NTC 121 -->
            <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-2.5">
              <h3 class="font-black text-sm text-[#003E78] flex items-center space-x-2">
                <span>🛡️</span>
                <span>Guardrails Certificados NTC 121</span>
              </h3>
              <p class="text-slate-600 leading-relaxed">
                El sistema cuenta con un filtro estricto de contexto: rechaza inmediatamente consultas ajenas a la construcción y el cemento (como preguntas de cocina, genética o entretenimiento) y enfoca al asesor en dosificaciones técnicas:
              </p>
              <ul class="list-disc list-inside space-y-1 text-[11px] text-slate-700 font-medium">
                <li>Dosificación de losas y columnas de 3000 PSI (21 MPa).</li>
                <li>Ventajas del Cemento Estructural Max vs Cemento de Uso General.</li>
                <li>Uso de Cemento Marino Ultracem resistente a sulfatos y cloruros.</li>
                <li>Argumentación frente a descuentos de $500 por bulto de Argos/Cemex.</li>
              </ul>
            </div>

            <!-- Consola Whisper Speech-to-Text -->
            <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-2.5">
              <h3 class="font-black text-sm text-[#003E78] flex items-center space-x-2">
                <span>🎙️</span>
                <span>Consola de Voz Whisper Turbo</span>
              </h3>
              <p class="text-slate-600 leading-relaxed">
                El asesor graba su audio mientras recorre la obra con casco y chaleco. El modelo de reconocimiento de voz sintetiza y extrae automáticamente las entidades clave:
              </p>
              <ul class="list-disc list-inside space-y-1 text-[11px] text-slate-700 font-medium">
                <li>Nombre de la constructora o ferretería.</li>
                <li>Tipo de cemento solicitado (Estructural Max, Marino o Gris).</li>
                <li>Volumen proyectado en toneladas o bultos de 50 kg.</li>
                <li>Objeciones de pago o requerimientos de crédito a 30 días.</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 6: RADAR CARTOGRÁFICO Y ESTRATEGIA B2B -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#003E78] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">6. Radar Cartográfico Leaflet & Directorio B2B Caribe</h2>
        </div>

        <div class="bg-white rounded-2xl p-5 border-2 border-slate-200 space-y-4 text-xs">
          <p class="text-sm text-slate-700 leading-relaxed">
            El mapa interactivo cartográfico utiliza la infraestructura de <strong>CartoDB Voyager</strong> y <strong>ESRI World Imagery</strong> para garantizar visualización ininterrumpida y libre de bloqueos de servidores voluntarios.
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="p-3 bg-amber-50 rounded-xl border border-amber-300">
              <span class="font-bold text-amber-900 block text-xs">🟡 Planta Galapa (Central)</span>
              <p class="text-[11px] text-amber-800 mt-1">Epicentro productivo en Km 8 Vía Tubará. Monitoreo de hornos a 1,450 °C y molienda de 180 T/h.</p>
            </div>
            <div class="p-3 bg-blue-50 rounded-xl border border-blue-300">
              <span class="font-bold text-blue-900 block text-xs">🔵 Obras & Ferreterías Activas</span>
              <p class="text-[11px] text-blue-800 mt-1">Constructora Bolívar (Torres del Mar), Marval (Altos de Riomar), Ferretería El Constructor (Soledad).</p>
            </div>
            <div class="p-3 bg-rose-50 rounded-xl border border-rose-300">
              <span class="font-bold text-rose-900 block text-xs">🔴 Puntos de Competencia</span>
              <p class="text-[11px] text-rose-800 mt-1">Plantas de Argos Vía 40 y Cemex Caracolí para monitoreo de precios y logística agresiva.</p>
            </div>
          </div>

          <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
            <h4 class="font-black text-[#003E78] text-xs uppercase mb-2">Directorio Calificado de 12 Prospectos Estratégicos del Caribe:</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed">
              Incluye constructoras de infraestructura vial (Pavimentos del Atlántico), prefabricadoras de Malambo, grandes desarrollos de VIS en Cartagena (Amarilo - Parque Heredia), proyectos turísticos en Santa Marta (Obycon - Puerto Madero) y distribuidores mayoristas de cemento en Barranquilla.
            </p>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 7: ESPECIFICACIÓN DE PANTALLAS DIVIDIDAS (SPLIT WORKSPACE) -->
      <section class="space-y-5 border-t-2 border-slate-200 pt-8 pb-12">
        <div class="flex items-center space-x-2.5">
          <span class="w-3 h-8 bg-[#FDCA02] rounded-full"></span>
          <h2 class="text-2xl font-black text-[#003E78] tracking-tight">7. Sistema Flexible de Pantallas Divididas a Elección del Asesor</h2>
        </div>

        <div class="bg-white rounded-3xl p-6 sm:p-8 border-2 border-slate-200 space-y-4 text-xs">
          <p class="text-sm text-slate-700 leading-relaxed">
            Para satisfacer la necesidad de supervisión y operación simultánea, UltraRacha CRM incorpora una <strong>consola de división de pantalla multivariable</strong>. El usuario puede seleccionar independientemente qué pantalla desea proyectar en el panel izquierdo y qué pantalla en el panel derecho:
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-slate-50 rounded-2xl border-2 border-slate-200 space-y-2">
              <span class="font-black text-sm text-[#003E78]">Panel Izquierdo (Módulos Mayores):</span>
              <ul class="list-disc list-inside space-y-1 text-slate-700 text-[11px]">
                <li><strong>💻 CRM Escritorio Completo:</strong> Racha, Obras, Consola de Notas de Voz y Escalamiento.</li>
                <li><strong>📑 PRD Maestro & Brand Book:</strong> Especificación técnica, manual de marca y guiones.</li>
                <li><strong>🗺️ Radar & B2B:</strong> Cartografía interactiva Leaflet con 12 prospectos.</li>
                <li><strong>🤖 Copiloto IA:</strong> Chat conversacional técnico con guardrails NTC 121.</li>
                <li><strong>🏆 Liga de Asesores:</strong> Podio regional y clasificación por volumen despachado.</li>
              </ul>
            </div>

            <div class="p-4 bg-slate-50 rounded-2xl border-2 border-slate-200 space-y-2">
              <span class="font-black text-sm text-[#003E78]">Panel Derecho (Módulos Complementarios):</span>
              <ul class="list-disc list-inside space-y-1 text-slate-700 text-[11px]">
                <li><strong>📱 Celular Móvil en Terreno:</strong> Simulación interactiva táctil del asesor a pie de obra.</li>
                <li><strong>📑 PRD Maestro Ultracem:</strong> Consulta de especificaciones al lado de la app.</li>
                <li><strong>🤖 Copiloto IA Asistente:</strong> Chat lateral para consultar mientras se gestionan obras.</li>
                <li><strong>🗺️ Radar & Directorio:</strong> Mapa lateral para georreferenciación inmediata.</li>
                <li><strong>❌ Pantalla Única:</strong> Expansión al 100% del panel izquierdo seleccionado.</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
'''
