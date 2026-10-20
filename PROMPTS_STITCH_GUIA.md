# Guía de Prompts y Especificaciones de Diseño para Stitch

**Proyecto:** UltraRacha — CRM Gamificado & Copiloto Comercial Ultracem  
**Herramienta:** Stitch (Diseñador UI con IA) / Figma / v0  

---

## 1. Tokens de Identidad Visual Ultracem

Alimentar estos valores exactos en Stitch o en la configuración de estilos:

* **Paleta Primaria:**
  - `Azul Corporativo Ultracem:` `#0033A0` (Botones primarios, encabezados, branding)
  - `Azul Oscuro Estructura:` `#002D62` (Textos pesados, bordes principales)
  - `Verde Éxito Ultracem:` `#009639` (Barras de progreso de toneladas, estados saludables)
  - `Blanco & Gris Concreto:` `#F8FAFC`, `#F1F5F9`, `#E2E8F0` (Fondos limpios, tarjetas)
* **Acentos de Gamificación:**
  - `Naranja Racha Fuego:` `#FF6B00` (Insignia de racha activa, fuegos, alertas de cierre)
  - `Amarillo Fraguado:` `#F59E0B` (Clientes en advertencia 4-7 días)
  - `Rojo Crítico / Stop:` `#EF4444` (Clientes con +8 días o cotización a vencer hoy)
* **Tipografía Recomendada:**
  - `Headings:` Plus Jakarta Sans (Bold / ExtraBold 700/800)
  - `Body / Datos:` Inter (Regular / SemiBold 400/600)

---

## 2. Prompts Maestros Listos para Stitch

### Prompt Pantalla 1: Mobile App — Vista del Asesor Comercial (Carlos Mendoza)

```text
Diseña una pantalla móvil nativa de alta fidelidad (iOS/Android) para "UltraRacha", el CRM gamificado de la compañía cementera ULTRACEM. 
Estilo visual: Limpio, corporativo pero altamente gamificado (fusión entre Salesforce y Duolingo). Paleta de colores: Azul Corporativo (#0033A0), Verde Ultracem (#009639), Naranja Fuego (#FF6B00) y fondos Gris Concreto claro (#F8FAFC).

Componentes requeridos en la pantalla:
1. Header Gamificado:
   - Avatar del vendedor "Carlos Mendoza" (Asesor Caribe) con badge verde online.
   - Logo oficial de ULTRACEM en la esquina superior izquierda.
   - Contador de racha prominente: "21 Días 🔥" con micro-animación de llama naranja brillante.
   - Ícono de inventario: "⛑️ 1 Casco Protector" (comodín que congela racha).
   - Reloj de cuenta regresiva para el corte de medianoche: "Cierre de Racha: 01h 59m 12s (11:59 PM)" con estilo visual de urgencia.

2. Tarjeta de Mascota "Don Fraguado":
   - Mascota amigable: Un saco de cemento animado con casco blanco de ingeniero, gafas de protección y botas de obra.
   - Burbuja de diálogo: "¡Pilas Carlos! Tienes 2 clientes en Riesgo Crítico. Gestiona o escala antes de las 11:59 PM para no perder tu racha de 21 días. 🔥"

3. Progreso Comercial:
   - Barra de progreso mensual: "420 / 500 Toneladas (84% meta mensual)" con gradiente verde Ultracem.

4. Pestañas de Filtro:
   - Chips de selección rápida: [Todos (4)] [🏢 Obras / Industrial] [🏪 Ferreterías / Depósitos].

5. Bandeja de Clientes por Semáforo de Riesgo (Estilo Salesforce adaptado):
   - Tarjeta 1 (Riesgo Rojo): "Constructora Bolívar — Torre del Mar", Canal Industrial, etiqueta roja "🔴 8 DÍAS SIN CONTACTO", alerta: "Cotización de 120 Ton vence hoy a las 5:00 PM". Valor: $54,000,000 COP. 3 botones de acción rápida en la tarjeta: "📞 Registrar Seguimiento", "🚨 Escalar a Depto (SLA)" y "✨ Copiloto IA".
   - Tarjeta 2 (Riesgo Rojo): "Ferretería El Constructor", Canal Tradicional, etiqueta roja "🔴 5 DÍAS SIN CONTACTO", alerta: "Riesgo de compra a Argos". Valor: $19,000,000 COP. 3 botones de acción rápida.
   - Tarjeta 3 (Amarillo): "Consorcio Vías del Magdalena", etiqueta "🟡 6 Días sin contacto".

6. Barra de Navegación Inferior (Bottom Bar):
   - 4 íconos: 🔥 UltraRacha (activo con acento azul), ✨ Copiloto IA, 🏆 Ranking Liga, 👤 Perfil.
```

---

### Prompt Pantalla 2: Modal / Drawer — Copiloto Comercial IA de Ultracem

```text
Diseña un modal/drawer emergente moderno en la app móvil de UltraRacha titulado "Copiloto IA Ultracem".
Estilo: Inteligencia artificial moderna, interfaz limpia con detalles en azul Ultracem y destellos sutiles violeta/azul.

Componentes requeridos:
1. Encabezado con ícono de chispas brillantes "✨ Copiloto Comercial Ultracem — Constructora Bolívar".
2. Tres pestañas horizontales superiores:
   - [📝 Redactar Escrito] (Activa)
   - [📚 Fichas Ultracem (RAG)]
   - [🔍 Investigar Cliente]
3. Contenido de la pestaña "Redactar Escrito":
   - Campo de texto de dictado rápido con botón de micrófono "🎙️ Dictar notas en obra".
   - Botón de acción: "✨ Generar Minuta CRM y WhatsApp".
   - Tarjeta de resultado con el texto redactado por IA listo para enviar por WhatsApp: "Estimado Ing. Andrés, un cordial saludo de Ultracem... confirmamos 120 Toneladas Cemento Estructural NTC 121...".
   - Botón prominente "📋 Copiar para WhatsApp" con feedback visual.
4. Sección complementaria "Fichas Técnicas Oficiales":
   - Selector de producto: "Cemento Estructural Tipo ART (NTC 121)".
   - Métricas clave mostradas en tarjetas: Resistencia 28 días (≥ 28.0 MPa) y Fraguado Inicial (≥ 45 min).
   - "Argumento de Venta Ultracem": Acelera el desencofrado 36 horas antes que el cemento estándar.
```

---

### Prompt Pantalla 3: Web Dashboard — Vista del Supervisor Comercial (Ing. Roberto Vega)

```text
Diseña un Dashboard Web ejecutivo responsivo (resolución 1440x900) para el Líder Comercial de ULTRACEM en el sistema "UltraRacha".
Estilo visual: Dashboard corporativo de primer nivel (estilo Stripe / Linear / Salesforce Lightning). Colores: Azul marino (#0033A0), fondos en Slate-50 (#F8FAFC) y tarjetas blancas nítidas con sombras sutiles.

Componentes requeridos:
1. Header Superior:
   - Logo oficial de ULTRACEM.
   - Título: "UltraRacha — Centro de Mando Comercial (Regional Caribe)".
   - Perfil del supervisor: "Ing. Roberto Vega — Líder Comercial".
   - Filtros de fecha y zona comercial.

2. Fila de 4 KPIs Principales:
   - KPI 1: "Toneladas del Mes: 3,420 / 3,750 Ton" (91.2% meta, ícono de grúa/estructura).
   - KPI 2: "Seguimiento Oportuno: 94.8%" (+6.2% vs mes anterior).
   - KPI 3: "Clientes Críticos Salvados Hoy: 23 / 24" (Alerta: 1 pendiente antes de medianoche).
   - KPI 4: "Casos Escalados Activos: 6" (100% dentro de SLA, tiempo promedio 1h 42m).

3. Tabla de Gamificación Izquierda: "🏆 Liga Maestros Ultracem":
   - Tabla con ranking de los mejores asesores:
     - 1º Carlos Mendoza | 21 Días de Racha 🔥 | 420 Ton | Estado: Al día ✅
     - 2º Andrea Polo | 19 Días de Racha 🔥 | 395 Ton | Estado: Al día ✅
     - 3º Javier Restrepo | 15 Días de Racha 🔥 | 360 Ton | Estado: Al día ✅
     - 4º Felipe Castro | 7 Días de Racha ⚠️ | 280 Ton | Estado: 1 cuenta crítica pendiente.

4. Panel de Auditoría Derecho: "🚨 Bandeja de Casos Escalados a Departamentos con SLA":
   - Tabla con tickets activos escalados por asesores:
     - Ticket #TR-4091 | Cliente: Consorcio Vías | Depto: 🚚 Logística (SLA 2h) | Tiempo Restante: 01h 14m | Asesor: Carlos Mendoza | Botón: "Acelerar ⚡"
     - Ticket #TR-4088 | Cliente: Ferretería El Sol | Depto: 💳 Cartera (SLA 4h) | Tiempo Restante: 02h 45m | Asesor: Andrea Polo | Botón: "Revisar 🔍"
     - Ticket #TR-4082 | Cliente: Constructora Bolívar | Depto: 🔬 Calidad NTC 121 (SLA 6h) | Tiempo Restante: 00h 48m | Botón: "Liberar ✅"
   - Banner inferior informativo: "Impacto: 48 ventas desbloqueadas este mes gracias al escalamiento sin penalizar la racha del vendedor."
```
