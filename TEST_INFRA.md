# E2E Test Infra: UltraRacha CRM (Ultracem S.A.S.)

## Test Philosophy
- **Opaque-box, requirement-driven**: Tests derive strictly from user requirements in `ORIGINAL_REQUEST.md`, independent of implementation internal design.
- **Methodology**: 4-Tier Category-Partition + Boundary Value Analysis (BVA) + Pairwise Combinatorial Testing + Real-World Workload Testing.
- **Verification Channels**: Programmatic DOM and HTTP analysis via automated Node.js / Python test runner, ensuring deterministic evaluation of emojis, colors, navigation, pipeline logic, mobile ESRI map, and reward redemptions.

---

## Feature Inventory Coverage Map

| # | Feature | Requirement | Tier 1 (Min 5) | Tier 2 (Min 5) | Tier 3 (Pairwise) |
|---|---------|-------------|:--------------:|:--------------:|:-----------------:|
| 1 | Desaturación Visual & Paleta Sólida | R1 | 5 | 5 | ✓ |
| 2 | Navegación Modular Limpia (5 Secciones) | R1 | 5 | 5 | ✓ |
| 3 | Eliminación Total de Emojis | R5 | 5 | 5 | ✓ |
| 4 | Adopción de Lucide Icons (SVG) | R5 | 5 | 5 | ✓ |
| 5 | Pipeline B2B: 5 Etapas Industriales | R2 | 5 | 5 | ✓ |
| 6 | Vistas Kanban & Lista B2B | R2 | 5 | 5 | ✓ |
| 7 | Tarjetas Industriales Detalladas | R2 | 5 | 5 | ✓ |
| 8 | Métricas Consolidadas del Pipeline | R2 | 5 | 5 | ✓ |
| 9 | Dashboard de KPIs Industriales | R1, R2 | 5 | 5 | ✓ |
| 10 | Copiloto Técnico NTC 121 Modular | R1 | 5 | 5 | ✓ |
| 11 | Navegación Móvil de 5 Pestañas | R3 | 5 | 5 | ✓ |
| 12 | Mapa Nativo Celular Leaflet + ESRI | R3 | 5 | 5 | ✓ |
| 13 | Georreferenciación Caribeña (6 Ciudades) | R3 | 5 | 5 | ✓ |
| 14 | Tarjetas Emergentes de Acción Móvil | R3 | 5 | 5 | ✓ |
| 15 | Billetera de Puntos de Racha | R4 | 5 | 5 | ✓ |
| 16 | Catálogo de Recompensas: Nivel 7 Días | R4 | 5 | 5 | ✓ |
| 17 | Catálogo de Recompensas: Nivel 14 Días | R4 | 5 | 5 | ✓ |
| 18 | Catálogo de Recompensas: Nivel 30 Días | R4 | 5 | 5 | ✓ |
| 19 | Flujo Interactivo de Redención | R4 | 5 | 5 | ✓ |
| 20 | Despliegue Sincronizado GitHub Pages | Acceptance | 5 | 5 | ✓ |

---

## Test Architecture
- **Test Runner Location**: `tests/e2e/runner.js` and `tests/e2e/test_suite.py`
- **Invocation Command**: `node tests/e2e/runner.js` or `python tests/e2e/test_suite.py`
- **Pass/Fail Semantics**: Exit code `0` on 100% pass; non-zero exit code with detailed diagnostic assertions on any failure.
- **Directory Layout**:
  ```
  tests/e2e/
  ├── runner.js                      # Main automated test executor
  ├── tier1_feature_coverage.test.js # Tier 1 test cases
  ├── tier2_boundary_corner.test.js  # Tier 2 boundary cases
  ├── tier3_cross_feature.test.js    # Tier 3 interaction cases
  └── tier4_application.test.js      # Tier 4 real-world workloads
  ```

---

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | **Asesor en Terreno (Barranquilla & Galapa)**: Carlos Mendoza consulta el Pipeline Kanban, filtra por "Constructora Bolívar", revisa el semáforo crítico y cambia a vista de Lista para verificar las 120 Ton de Estructural Max. | F1, F2, F5, F6, F7, F8 | High |
| 2 | **Ruta Móvil de Inspección en Celular**: En la vista smartphone, el asesor abre la pestaña "Radar", visualiza los marcadores en Soledad y Galapa con azulejos ESRI, abre el popup de Ferretería El Constructor e inicia ruta por GPS. | F11, F12, F13, F14 | High |
| 3 | **Validación Técnica NTC 121 en Obra**: Desde el Pipeline, el asesor abre el Copiloto Técnico NTC 121, calcula la dosificación para 3000 PSI en vaciado de losa maciza (a/c 0.51), sin recargar la pantalla ni perder el contexto comercial. | F5, F7, F10 | Medium |
| 4 | **Recompensa por Racha Comercial (11:59 PM)**: Carlos Mendoza verifica su billetera con 2,100 PTS de racha acumulada (21 días), redime el Bono de Combustible ($50.000 COP) Nivel 7 Días, verifica el descuento a 1,400 PTS y el registro en el historial de canjes. | F15, F16, F19 | High |
| 5 | **Auditoría Ejecutiva de KPIs de Planta Galapa**: El Director Comercial abre el Dashboard de KPIs, verifica el cumplimiento del 93% mensual de Planta Galapa, revisa los tiempos OTD por corredor vial (Circunvalar vs Vía al Mar) y el semáforo antichurn general sin aberraciones visuales ni emojis. | F1, F2, F3, F4, F9 | High |

---

## Coverage Thresholds
- **Tier 1 (Feature Coverage)**: ≥100 test cases (≥5 per feature across 20 features)
- **Tier 2 (Boundary & Corner Cases)**: ≥100 test cases (zero emojis regex check, zero gradients check, extreme points redemption, missing contact data, phone viewport bounds)
- **Tier 3 (Cross-Feature Combinations)**: ≥20 test cases covering pairwise feature interactions
- **Tier 4 (Real-World Scenarios)**: 5 end-to-end multi-step industrial workloads
- **Total Minimum Test Cases**: ≥225 test cases
