# Project: UltraRacha CRM Redesign (Ultracem S.A.S.)

## Architecture
- **Application Model**: High-performance Single-Page Application (SPA) delivered via `index.html`, served locally by `server.js` (Node.js HTTP proxy on port 3000) and deployed globally via GitHub Actions (`.github/workflows/static.yml`) to GitHub Pages (`https://thehector2614.github.io/Cooweb-1/`).
- **Visual Styling & Desaturation (R1)**: Tailwind CSS CDN (`https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js`), Google Fonts `Outfit` (Headings & UI) and `JetBrains Mono` (Tabular metrics & engineering data).
- **Corporate Color Palette**: 100% solid colors without CSS gradients (`bg-gradient-*`, `linear-gradient`, `radial-gradient`):
  - Azul Corporativo: `#003E78`
  - Amarillo Ultracem: `#FDCA02`
  - Azul Marino: `#0A233F`
  - Blanco: `#FFFFFF`
  - Fondo Cemento: `#F2F1EC`
- **Iconography System (R5)**: 100% Lucide SVG vector icons (1.75px/2px stroke, `currentColor`, clean viewBox `0 0 24 24`). Zero emoji unicode characters in HTML, CSS, or JS.
- **Mapping Engine (R3)**: Leaflet 1.9.4 with ESRI World Street Map & ESRI World Imagery (Satellite) tiles (zero API key requirement, open endpoints). Concurrent independent instances for desktop (`desktopColombiaMap`) and mobile (`mobileLeafletMap`).
- **Data & State Management**: Reactive client-side stores (`window.UltraPipelineStore`, `window.UltraRewardStore`, `window.UltraMapStore`) with `localStorage` persistence and rich seed datasets for Caribbean infrastructure.

---

## Feature Inventory
Every feature from `ORIGINAL_REQUEST.md` is cataloged below with its assigned milestone:

| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Desaturación Visual & Paleta Sólida | Eliminación de saturación, fondos cemento `#F2F1EC`, azules corporativos `#003E78` y `#0A233F`, amarillo `#FDCA02`, cero degradados. | M1 | R1 |
| 2 | Navegación Modular Limpia (5 Secciones) | Barra superior/lateral con 5 secciones: Pipeline B2B, Radar/Mapa, Dashboard KPIs, Recompensas por Racha, Copiloto Técnico NTC 121. | M1 | R1 |
| 3 | Eliminación Total de Emojis | Erradicación del 100% de emojis en todo el código HTML/JS/CSS (183 instancias detectadas). | M1 | R5 |
| 4 | Adopción de Lucide Icons (SVG) | Reemplazo sistemático por SVG vectoriales limpios (Lucide) con colores corporativos y neutros. | M1 | R5 |
| 5 | Pipeline B2B: 5 Etapas Industriales | Obra Identificada, Cotización Técnica, Muestra & Ensayo NTC 121, Cierre & Despacho Programado, Suministro Continuo & Antichurn. | M2 | R2 |
| 6 | Vistas Kanban & Lista B2B | Tablero Kanban de 5 columnas y vista de tabla interactiva con filtros, búsqueda y cambio de etapa. | M2 | R2 |
| 7 | Tarjetas Industriales Detalladas | Obra/constructora, volumen en toneladas, valor en COP, responsable comercial, último contacto y semáforo de recompra. | M2 | R2 |
| 8 | Métricas Consolidadas del Pipeline | Total Toneladas en Pipeline (2,855 Ton), Valor Total en COP ($910.8M), Cuentas Activas (14), Alertas 11:59 PM. | M2 | R2 |
| 9 | Dashboard de KPIs Industriales | Telemetría de Planta Galapa (cumplimiento 93%), toneladas despachadas, tiempos de entrega (OTD 84 min), y tasa de recompra (94.2%). | M2 | R1, R2 |
| 10 | Copiloto Técnico NTC 121 Modular | Consultas técnicas, calculadora de dosificación 2500/3000/4000 PSI sin interferir con la operación diaria. | M2 | R1 |
| 11 | Navegación Móvil de 5 Pestañas | Barra inferior smartphone con pestañas: Racha, Radar, Pipeline, Copiloto, Perfil/Recompensas. | M3 | R3 |
| 12 | Mapa Nativo Celular Leaflet + ESRI | Contenedor móvil dedicado con azulejos ESRI (Calles y Satelital), fluido y sin grisáceos de renderizado. | M3 | R3 |
| 13 | Georreferenciación Caribeña (6 Ciudades) | Marcadores interactivos en Barranquilla, Galapa (Planta), Soledad, Malambo, Cartagena y Santa Marta. | M3 | R3 |
| 14 | Tarjetas Emergentes de Acción Móvil | Popups con diseño Tailwind con botones directos para "Llamar" (`tel:`) e "Iniciar Ruta" (Google Maps). | M3 | R3 |
| 15 | Billetera de Puntos de Racha | Saldo de puntos (2,100 PTS para Carlos Mendoza a 100 pts/día de racha activa a las 11:59 PM). | M4 | R4 |
| 16 | Catálogo de Recompensas: Nivel 7 Días | Bono combustible ($50.000 COP) + Kit EPPs Ultracem (Costo: 700 PTS). | M4 | R4 |
| 17 | Catálogo de Recompensas: Nivel 14 Días | Bono almuerzo de cuadrilla + Merchandising Don Fraguado VIP (Costo: 1,400 PTS). | M4 | R4 |
| 18 | Catálogo de Recompensas: Nivel 30 Días | Acelerador comisión (+3% Cemento Estructural Max) + Día libre compensatorio (Costo: 3,000 PTS). | M4 | R4 |
| 19 | Flujo Interactivo de Redención | Botón "Redimir Recompensa" con confirmación modal, deducción inmediata de saldo, sonido y registro en historial. | M4 | R4 |
| 20 | E2E Testing Suite (Tiers 1-4) | Opaque-box test suite con verificación exhaustiva de todas las características y criterios de aceptación. | M5 | Acceptance |
| 21 | Sincronización Git & GitHub Pages | Despliegue verificado en el repositorio remoto y en GitHub Pages (`https://thehector2614.github.io/Cooweb-1/`). | M5 | Acceptance |

---

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Desaturación Visual & Navegación Modular (R1) + Lucide Icons (R5) | Header limpio, tabs de 5 módulos en desktop, cero degradados, colores corporativos, reemplazo de 183 emojis por Lucide SVGs. | None | DONE |
| M2 | Pipeline Comercial B2B 5 Etapas & Dashboard KPIs (R2) | Kanban de 5 columnas + Vista de Lista, tarjetas con toneladas/COP/semáforo, métricas consolidadas, dashboard de KPIs de Galapa, y Copiloto NTC 121. | M1 (Interfaces) | IN_PROGRESS |
| M3 | Mapa Georreferenciado Nativo Celular (R3) | Barra inferior móvil de 5 tabs (Racha, Radar, Pipeline, Copiloto, Recompensas), mapa Leaflet + ESRI en móvil, marcadores en 6 ciudades caribeñas, popups con Llamar y Ruta. | M1 | PLANNED |
| M4 | Catálogo de Recompensas por Racha Comercial (R4) | Billetera de puntos de racha, catálogo de 3 niveles (7, 14, 30 días), modal de redención con descuento de saldo y registro histórico de canjes. | M1 | PLANNED |
| M5 | E2E Verification & Git/GitHub Pages Sync | Ejecución del 100% de la suite de pruebas E2E, auditoría forense de integridad, commit y push a `main`, y verificación en GitHub Pages. | M1, M2, M3, M4 | PLANNED |

---

## Code Layout & Write Boundaries
To prevent conflicts across parallel work:
- **`index.html` Head & Global Styles**: Lines 1-149. (M1)
- **`index.html` Desktop Navigation & Header**: Lines 150-330. (M1)
- **`index.html` Desktop Pipeline & KPIs Containers**: `#dcrm-content-pipeline`, `#dcrm-content-kpis`, `#dcrm-content-copiloto`. (M2)
- **`index.html` Mobile Phone Bottom Nav & Screens**: `#right-content-phone`, `#screen-radar`, `#screen-pipeline`, `#screen-perfil`. (M3 & M4)
- **`index.html` JavaScript Stores & Logic**:
  - Global navigation & Lucide render helpers (M1)
  - `UltraPipelineStore` & KPI telemetry logic (M2)
  - `mobileLeafletMap` & site popups logic (M3)
  - `UltraRewardStore` & redemption logic (M4)
- **`server.js`**: Server proxy and health endpoints.
- **`tests/e2e/`**: Dedicated directory for E2E opaque-box test suites. (E2E Testing Track)

---

## Interface Contracts

### 1. Global Navigation Contract
```javascript
// Desktop tab switching
window.navigateToDesktopTab = function(tabName) {
  // tabName: 'pipeline' | 'mapa' | 'kpis' | 'recompensas' | 'copiloto'
};

// Mobile tab switching
window.navigateToTab = function(tabName) {
  // tabName: 'racha' | 'radar' | 'pipeline' | 'copiloto' | 'perfil'
};
```

### 2. Pipeline Account Data Model
```typescript
interface PipelineAccount {
  id: number;
  nombreObra: string;
  constructora: string;
  canal: 'obra' | 'ferreteria' | 'infraestructura' | 'prefabricados';
  etapa: 1 | 2 | 3 | 4 | 5; // 1: Identificada, 2: Cotizada, 3: Muestra NTC 121, 4: Cierre/Despacho, 5: Suministro
  volumenTon: number;
  valorCOP: number;
  asesor: string;
  ultimoContacto: string;
  diasSinContacto: number;
  semaforo: 'verde' | 'amarillo' | 'rojo'; // rojo = corte 11:59 PM
  especificacion: string;
}
```

### 3. Reward Tier Data Model
```typescript
interface RewardTier {
  id: string; // 'tier-7d' | 'tier-14d' | 'tier-30d'
  nivelDias: number; // 7, 14, 30
  costoPuntos: number; // 700, 1400, 3000
  titulo: string;
  beneficioPrincipal: string;
  beneficioSecundario: string;
}
```

### 4. Client Map Site Data Model
```typescript
interface ClientSite {
  id: number;
  nombre: string;
  ciudad: 'Barranquilla' | 'Galapa' | 'Soledad' | 'Malambo' | 'Cartagena' | 'Santa Marta';
  tipo: 'planta' | 'obra' | 'ferreteria' | 'competencia';
  direccion: string;
  volumen: string;
  telefono: string;
  lat: number;
  lng: number;
  color: string;
}
```
