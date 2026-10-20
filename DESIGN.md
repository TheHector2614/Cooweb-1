# Design System: UltraRacha Minimal (Ultracem Edition)

> **Philosophy:** Modern Minimalist B2B Architecture (Stripe / Linear precision + Swiss Typography)  
> **Brand Owner:** Ultracem (Industria Cementera & Materiales de Construcción)  
> **Font Stack:** Outfit + JetBrains Mono  
> **Icon Family:** Lucide / Feather Linear Minimalist (1.75px stroke)  

---

## 1. Visual Theme & Atmosphere
- **Atmosphere:** Elevado, arquitectónico y minimalista. Elimina cualquier aspecto de "juguete" o "app colorinche". Utiliza amplios espacios en blanco, bordes finos de 1px (`#E2E8F0`), superficies en blanco puro sobre fondo de caliza suave (`#F8FAFC`), y tipografía geométrica con carácter industrial.
- **Spectrum Dials:**
  - `VISUAL_DENSITY:` **3.5** (Muy aireado, limpio, libre de cajas anidadas).
  - `DESIGN_VARIANCE:` **6** (Estructura de cuadrícula asimétrica y balanceada).
  - `MOTION_INTENSITY:` **4** (Micro-interacciones táctiles sutiles de pulsación y resorte).

---

## 2. Nueva Paleta de Colores Corporativa (Fiel a Ultracem)

| Rol Semántico | Nombre | Hex Code | Aplicación |
| :--- | :--- | :--- | :--- |
| **Primary Brand** | Azul Cobalto Ultracem | `#004797` | Botones primarios, acentos de marca, estados activos y foco. |
| **Brand Hover** | Cobalto Profundo | `#003672` | Estado de interacción al pasar el cursor sobre elementos primarios. |
| **Surface Base** | Caliza Arquitectónica | `#F8FAFC` (Slate-50) | Fondo limpio general de la aplicación. |
| **Surface Card** | Blanco Nieve | `#FFFFFF` | Tarjetas de clientes, modales y barras de navegación. |
| **Ink Dominant** | Basalto Obsidiana | `#0F172A` (Slate-900) | Títulos principales, cifras numéricas y nombres de clientes. |
| **Ink Muted** | Grafito Neutro | `#64748B` (Slate-500) | Subtítulos, metadatos y descripciones. |
| **Border Line** | Línea Árida Sutil | `#E2E8F0` (Slate-200) | Bordes finos de 1px con precisión geométrica. |
| **Streak Fire** | Ámbar Fraguado | `#EA580C` / `#D97706` | Píldora de racha minimalista con brillo sutil (21d 🔥). |
| **Status Critical** | Carmesí Nórdico | `#E11D48` (`bg-rose-50`) | Clientes con +5d/+8d sin contacto (badge sutil, sin saturación excesiva). |
| **Status Warning** | Ocre Industrial | `#D97706` (`bg-amber-50`) | Clientes en advertencia preventiva. |
| **Status Success** | Verde Esmeralda | `#059669` (`bg-emerald-50`) | Gestión completada, racha salvada y pedidos al día. |

---

## 3. Tipografía & Jerarquía (Nueva Elección)

- **Headings & Display:** `Outfit` (Google Fonts: 500, 600, 700, 800).
  - Aporta una personalidad moderna, geométrica y sumamente legible, alineada con identidades contemporáneas de ingeniería y construcción.
- **Data, Tiempos & Moneda:** `JetBrains Mono` (Google Fonts: 500, 700 con `tabular-nums`).
  - Formato monoespaciado técnico para métricas de toneladas (`3,420 / 3,750 Ton`), valores monetarios (`$54M`, `$19M`), y temporizadores de SLA (`01h : 14m`).

---

## 4. Nuevo Paquete de Iconos (Linear Vectorial 1.75px)

Se reemplazaron todos los emojis informales en la interfaz por iconos lineales vectoriales de alta precisión:
* 📞 **Seguimiento:** `phone` lineal con trazo de 2px.
* 🚨 **Escalar a Depto:** `send` / vector de flecha angulada.
* ✨ **Copiloto IA:** `sparkles` minimalista de cuatro puntas.
* ⏱️ **Corte y Tiempo:** `clock` con manecillas técnicas.
* 🔥 **Racha:** `flame` minimalista estilizado en píldora ámbar.
* 🏢 **Canal Industrial:** `building-2` geométrico.
* 🏪 **Canal Tradicional:** `store` lineal.
* 🏆 **Liga / Ranking:** `trophy` moderno.
