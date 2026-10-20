# Cooweb #1: UltraRacha CRM — Ultracem S.A.S.

> **Ecosistema Comercial Gamificado, Prevención Antichurn & Copiloto IA de Terreno para la Industria del Cemento y Concreto**  
> *Desarrollado para la fuerza de ventas técnica de **Ultracem S.A.S.** (Planta Galapa, Atlántico).*

---

## 🏗️ Descripción del Proyecto

**UltraRacha CRM** transforma la fricción operativa del seguimiento de obras y ferreterías en un hábito comercial diario a través de gamificación de rachas con corte estricto a las **11:59 PM**, acompañamiento de **Don Fraguado** (mentor de marca en vector SVG), un copiloto IA multimodelo con guardrails certificados bajo la norma técnica **NTC 121**, cartografía interactiva con **Leaflet & ESRI**, y una **consola flexible de pantallas divididas** que permite operar el CRM de escritorio y la aplicación móvil simultáneamente.

---

## ✨ Características Principales

### 1. 🔥 Racha Comercial & Prevención Antichurn (Corte 11:59 PM)
- **Temporizador en Vivo**: Cuenta regresiva hacia el corte diario de las 11:59 PM (hora en que se congelan los despachos matutinos de Planta Galapa).
- **Semáforos de Recompra**:
  - 🟢 **Verde (0 a 3 días)**: Cuenta al día y consumiendo según curva de vaciado.
  - 🟡 **Amarillo (4 a 6 días)**: Alerta de desaceleración y riesgo de fuga de pedidos a la competencia.
  - 🔴 **Rojo (7+ días sin pedido)**: Riesgo crítico de churn. Requiere intervención inmediata antes de medianoche para salvar la racha (+150 XP).
- **Consola de Voz Whisper Turbo**: Grabación y reproducción de notas de voz en obra con transcripción automatizada y extracción de entidades (volumen en toneladas, tipo de cemento, fecha de vaciado).
- **Escalamiento con SLAs**: Traspaso ágil de bloqueos a Cartera & Crédito (4h), Logística & Despachos (2h) o Laboratorio de Calidad (8h) que salvaguarda la racha inmediatamente.

### 2. 👷 Don Fraguado (Mascota Vectorial SVG)
- Personificación del bulto de 50 kg de Cemento Gris Estructural Max con casco amarillo de seguridad.
- 4 estados emocionales adaptativos: **Motivado** (mañana), **Pánico de Fraguado** (10:45 PM a 11:59 PM con sudor y alerta), **Victoria** (celebración con estrellas y confeti) y **Criogénico** (casco protector activo).
- Interactivo al clic: reproduce audio táctil y cicla consejos comerciales de obra.

### 3. 🤖 Copiloto IA Multimodelo & Guardrails NTC 121
- Soporte para **Groq LPU** (Llama 3.3 70B, Llama 3.1 8B Instant), **NVIDIA NIM** (Llama 3 70B Instruct, Mistral NeMo) y **DeepSeek V3/R1**.
- **Guardrails Técnicos**:
  - Dosificación de losas de 3000 PSI según norma NTC 121.
  - Especificaciones de Cemento Estructural Max vs Uso General.
  - Resistencia a sulfatos en ambientes marinos con Cemento Marino Ultracem.
  - Manejo de objeciones frente a descuentos de la competencia (Argos, Cemex).
  - Rechazo de consultas ajenas a la construcción y reorientación comercial.

### 4. 🗺️ Radar Cartográfico Leaflet & Directorio B2B
- Cartografía georreferenciada utilizando capas de alta fidelidad **ESRI World Street Map** y **ESRI World Imagery** (satelital).
- Marcadores estratégicos:
  - 🟡 **Planta Galapa (Central)**: Km 8 Vía Tubará.
  - 🔵 **Obras & Ferreterías Activas**: Constructora Bolívar, Marval, Ferretería El Constructor.
  - 🔴 **Competencia**: Plantas de Argos Vía 40 y Cemex Caracolí.
  - 🟢 **12 Prospectos B2B Calificados** en Barranquilla, Soledad, Malambo, Baranoa, Cartagena y Santa Marta.

### 5. 🎛️ Consola de Pantallas Divididas a Elección (Multi-Split)
- Selector interactivo superior que permite combinar **cualquier pantalla** en el panel izquierdo y derecho:
  - `💻 CRM Escritorio + 📱 Celular al lado`
  - `📑 PRD Maestro + 📱 Celular al lado`
  - `💻 CRM Escritorio + 📑 PRD Maestro`
  - `💻 Solo CRM Escritorio (Completo)`
  - `📱 Solo Celular en Terreno (Centrado)`
  - `📑 Solo PRD Maestro (Canvas Blanco Completo)`

### 6. 🎨 Identidad Visual 100% Sólida (Cero Degradados)
- **Azul Ultracem**: `#003E78` (Identidad y liderazgo industrial)
- **Amarillo Ultracem**: `#FDCA02` (Sol del Caribe, energía y alertas de racha)
- **Azul Marino Profundo**: `#0A233F` (Sidebar y control de alto contraste)
- **Blanco Puro**: `#FFFFFF` (Tarjetas y pulcritud de datos)
- **Gris Cemento Cálido**: `#F2F1EC` (Fondo neutro de obra civil)

---

## 🚀 Puesta en Marcha Local

### Prerrequisitos
- Node.js (versión 18 o superior)
- Python 3.10+ (opcional, para regenerar el compilador si se desea)

### Ejecución Inmediata
1. Clona el repositorio:
   ```bash
   git clone https://github.com/TheHector2614/Cooweb-1.git
   cd Cooweb-1
   ```

2. Inicia el servidor local:
   ```bash
   node server.js
   ```

3. Abre en tu navegador:
   ```
   http://localhost:3000
   ```
   *(También puedes abrir `index.html` directamente con doble clic en cualquier navegador).*

---

## 📁 Estructura del Repositorio

```
├── assets/                     # Recursos visuales y logo en Base64
├── screenshots/                # Capturas de pantalla de la aplicación
├── scripts/
│   ├── build_direct_ultracem.py     # Compilador principal del prototipo interactivo
│   ├── generate_ultracem_desktop_crm.py # Componente CRM de escritorio y Don Fraguado
│   ├── generate_prd_html.py        # Generador del PRD y Manual de Marca
│   └── capture_screenshots.js      # Automatización de capturas con Playwright
├── server.js                   # Servidor HTTP local con proxy CORS para NVIDIA NIM
├── index.html                  # Aplicación web completa autocontenida
├── PRD_UltraRacha.md           # Documento de requerimientos de producto
└── README.md                   # Documentación oficial del proyecto
```

---

## 🏢 Créditos & Marca

**Ultracem S.A.S.**  
*Planta Galapa • Km 8 Vía Tubará, Atlántico, Colombia.*  
*Lema: “Calidad, Resistencia y Rendimiento”.*
