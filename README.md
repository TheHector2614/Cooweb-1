# Cooweb #1: UltraRacha CRM — Ultracem S.A.S.

> **Ecosistema Comercial Gamificado B2B, Prevención Antichurn & Copiloto Técnico NTC 121**  
> *Desarrollado para la fuerza de ventas técnica y gerencia comercial de **Ultracem S.A.S.** (Planta Galapa, Atlántico).*

---

## Despliegue en Vivo

El sistema se encuentra desplegado y accesible públicamente a través de GitHub Pages:

**URL Oficial:** [https://thehector2614.github.io/Cooweb-1/](https://thehector2614.github.io/Cooweb-1/)

---

## Novedades & Arquitectura Desaturada (Versión 2.0)

A solicitud de la dirección comercial y mediante la intervención de un equipo multi-agente de UX/UI, la plataforma fue refactorizada íntegramente bajo principios de **desaturación visual**, **cero emojis**, **iconografía vectorial SVG (Lucide Icons)** y **paleta de colores 100% sólidos de Ultracem** (sin degradados CSS):

### 1. Navegación Modular en 5 Pestañas Industriales
La interfaz de escritorio fue desaturada eliminando barras flotantes innecesarias y organizando el trabajo comercial en 5 módulos especializados:
- **Pipeline B2B**: Tablero Kanban industrial y vista de lista para gestión de cuentas de obras y ferreterías a lo largo de 5 etapas comerciales.
- **Radar / Mapa**: Cartografía georreferenciada con Leaflet y azulejos de alta fidelidad **ESRI World Street Map** y satelital **ESRI World Imagery**.
- **Dashboard de KPIs**: Métricas operativas de Planta Galapa (cumplimiento mensual del 93%, despacho del día de 1.420 Ton, tiempos de entrega OTD de 84 min y retención de cuentas del 94.2%).
- **Recompensas por Racha**: Catálogo de beneficios canjeables por puntos acumulados al mantener activa la racha comercial con corte diario a las 11:59 PM.
- **Copiloto Técnico NTC 121**: Calculadora y consultor técnico de dosificación de concreto estructural (2500, 3000, 4000 y 5000 PSI) bajo la norma colombiana NTC 121.

### 2. Pipeline Comercial B2B de 5 Etapas para Construcción
Gestión comercial de 14 cuentas clave en Barranquilla, Galapa, Soledad, Malambo, Cartagena y Santa Marta, totalizando 2.855 Toneladas y $910.8M COP:
1. **Obra Identificada**: Detección temprana de licencias de construcción y volumen estimado.
2. **Cotización Técnica**: Propuesta comercial según resistencia requerida y tipo de cemento (Max vs Marino).
3. **Muestra & Ensayo NTC 121**: Validación en laboratorio/obra de cilindros de prueba a 28 días.
4. **Cierre & Despacho Programado**: Asignación de cupo de crédito y programación de despacho en Planta Galapa.
5. **Suministro Continuo & Antichurn**: Seguimiento de vaciado periódico con semáforo de recompra antes de las 11:59 PM.

### 3. Mapa Georreferenciado Nativo en el Celular (Radar Móvil)
- Pestaña fija **Radar** en la barra de navegación inferior del smartphone.
- Carga reactiva de Leaflet con azulejos ESRI que previene teselados grises mediante `invalidateSize()`.
- Marcadores de obras, ferreterías y plantas de la competencia en el Atlántico y Bolívar.
- Tarjetas emergentes con botones directos para llamar al contacto y abrir la ruta GPS en Google Maps.

### 4. Catálogo de Recompensas por Racha Comercial
Billetera comercial con persistencia local (`UltraRewardStore`) y saldo inicial de 2.100 puntos, con beneficios estructurados en 3 niveles de racha:
- **Nivel 7 Días (700 PTS)**: Bono de combustible ($50.000 COP) para visitas de obra + Kit de EPPs Ultracem.
- **Nivel 14 Días (1.400 PTS)**: Bono de almuerzo de obra para cuadrillas de maestros de obra + Merchandising exclusivo Don Fraguado.
- **Nivel 30 Días (3.000 PTS)**: Acelerador de comisión (+3% sobre toneladas de Cemento Estructural Max) + Día libre compensatorio de terreno.
- Módulo de canje con validación de saldo, modal de confirmación y generación de código único de redención.

### 5. Cero Emojis & Lucide Icons Vectoriales
- Erradicación del 100% de caracteres emoji en código HTML, scripts y servidor.
- Sustitución integral por más de 140 componentes vectoriales SVG nítidos de la librería **Lucide Icons** con atributos estándar (`viewBox="0 0 24 24"`, `currentColor`).

### 6. Paleta Corporativa 100% Sólida
- **Azul Corporativo Ultracem**: `#003E78`
- **Amarillo Ultracem**: `#FDCA02`
- **Azul Marino Sidebar**: `#0A233F`
- **Blanco Puro**: `#FFFFFF`
- **Fondo Neutro Cemento**: `#F2F1EC`
- Estricto 0% de gradientes CSS (`linear-gradient`, `radial-gradient`, etc.).

---

## Verificación & Suite de Pruebas Automatizadas E2E

El proyecto cuenta con una suite de **225 pruebas automatizadas Playwright** estructurada en 4 niveles de aseguramiento de calidad (Category-Partition, BVA, Pairwise y Workloads):

```bash
cd "#1"
node tests/e2e/runner.js
```

### Resultados de la Auditoría:
- **Tier 1 (Cobertura Funcional - 20 features x 5 tests)**: 100 / 100 aprobados (100%)
- **Tier 2 (Límites, BVA y Casos de Borde)**: 100 / 100 aprobados (100%)
- **Tier 3 (Integración Cruzada y Pairwise)**: 20 / 20 aprobados (100%)
- **Tier 4 (Escenarios Operativos Reales Caribe)**: 5 / 5 aprobados (100%)
- **Tasa de Aprobación Global**: **225 / 225 (100% Pass Rate)**

---

## Puesta en Marcha Local

### Prerrequisitos
- Node.js (v18+)

### Instrucciones
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TheHector2614/Cooweb-1.git
   cd Cooweb-1
   ```

2. Iniciar el servidor local:
   ```bash
   node server.js
   ```

3. Abrir en el navegador:
   ```
   http://localhost:3000
   ```
   *(También puede abrirse `index.html` directamente en cualquier navegador web).*

---

## Estructura del Repositorio

```
├── .github/workflows/static.yml # Despliegue automatizado a GitHub Pages
├── .gitignore                   # Exclusiones de dependencias y logs
├── .nojekyll                    # Instrucción para bypass de motor Jekyll
├── assets/                      # Logos e identidad gráfica oficial
├── screenshots/                 # Capturas de la interfaz y módulos
├── scripts/                     # Automatizaciones y utilidades
├── tests/e2e/                   # Suite de 225 pruebas automatizadas
│   ├── runner.js                # Ejecutor maestro Playwright
│   ├── test_helpers.js          # Harness y utilidades de prueba
│   ├── tier1_feature_coverage.test.js
│   ├── tier2_boundary_corner.test.js
│   ├── tier3_pairwise_cross.test.js
│   └── tier4_workload_scenarios.test.js
├── index.html                   # Aplicación web completa autocontenida
├── server.js                    # Servidor local Node.js con CORS proxy
├── PROJECT.md                   # Catálogo de funcionalidades y arquitectura
├── TEST_INFRA.md                # Especificación de infraestructura de pruebas
├── TEST_READY.md                # Matriz de trazabilidad y cobertura
├── PRD_UltraRacha.md            # Documento de Requerimientos de Producto
└── README.md                    # Documentación oficial del proyecto
```

---

## Ultracem S.A.S.
*Planta Galapa • Km 8 Vía Tubará, Atlántico, Colombia.*  
*“Calidad, Resistencia y Rendimiento”.*
