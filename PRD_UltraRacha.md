# PRD Maestro: UltraRacha — CRM Gamificado & Copiloto Comercial Ultracem

**Proyecto:** Reto Bootcamp Semillero By Cooweb — Día 1  
**Cliente:** Ultracem  
**Enfoque:** CRM + Gamificación (Rachas) + Copiloto IA + Activación de Marca  
**Herramienta de Prototipado UI:** Stitch  

---

## 1. Problema y Contexto de Negocio
En la industria cementera y de materiales de construcción (Ultracem), la velocidad de respuesta comercial define quién se queda con el suministro de una obra o el inventario de una ferretería. Actualmente, los asesores comerciales sufren de **seguimiento tardío a sus clientes**, ocasionado por la alta carga operativa en terreno, la fricción al documentar gestiones en sistemas tradicionales y la falta de visibilidad sobre qué cuentas se están enfriando.

* **Impacto:** Pérdida de toneladas vendidas, cotizaciones vencidas sin respuesta y cuellos de botella cuando un requerimiento depende de otro departamento interno (Cartera, Logística, Calidad o Pricing).
* **Oportunidad:** Transformar la disciplina del seguimiento diario en un hábito gamificado asistido por IA, donde el asesor no es castigado si el cliente está ocupado, sino premiado por mantener su cartera activamente gestionada o escalada a tiempo antes del cierre del día (11:59 PM).

---

## 2. Usuarios, Roles y Flujos (User Flows)

### Rol 1: Asesor Comercial (Terreno / Obra / Ferreterías)
* **Dolor:** Poco tiempo para escribir reportes largos; olvida dar seguimiento a clientes que pidieron ser contactados días después o pierde tiempo buscando fichas técnicas.
* **Motivador:** Mantener su **racha diaria** activa, subir en la liga comercial y cerrar su meta de toneladas sin fricción administrativa.
* **User Flow en Stitch (Mobile First):**  
  `Login` -> `Alerta de racha activa y cuenta regresiva (11:59 PM)` -> `Bandeja de clientes segmentada por Canal y priorizada por Días de Riesgo (estilo Salesforce)` -> `Acción en 1 clic (Registrar seguimiento con Copiloto IA o Escalar a departamento con SLA)` -> `Celebración de mascota y suma de racha`.

### Rol 2: Líder Comercial / Supervisor (Back-Office)
* **Dolor:** Descubre que un cliente importante se perdió cuando ya le compró a la competencia; no tiene visibilidad rápida de si un pedido está frenado por falta de gestión del vendedor o por demora de un área interna.
* **Motivador:** Visibilidad preventiva de cuentas en riesgo crítico, desbloqueo rápido de casos escalados y un equipo motivado compitiendo sanamente.
* **User Flow en Stitch (Web Dashboard):**  
  `Vista ejecutiva del embudo y toneladas del equipo` -> `Ranking gamificado de rachas de asesores` -> `Mapa de calor de clientes en Riesgo Crítico` -> `Bandeja de auditoría de tickets escalados por departamento y cumplimiento de SLA`.

---

## 3. Historias de Usuario Detalladas

| ID | Rol | Historia de Usuario | Valor de Negocio |
| :--- | :--- | :--- | :--- |
| **US-01** | Asesor | Quiero visualizar un indicador de **Días de Riesgo** (semáforo estilo Salesforce adaptado a Ferretería o Constructora) y mi **Racha Actual**, para saber exactamente a quién debo gestionar antes de las 11:59 PM. | Evita el abandono involuntario de cuentas activas o cotizaciones abiertas próximas a vencer. |
| **US-02** | Asesor | Quiero registrar un intento de contacto válido o **escalar el caso a otro departamento** (Cartera, Logística, Soporte Técnico, Pricing) cuando el cliente no conteste o tenga un bloqueo, para proteger mi racha diaria sin depender de terceros. | Elimina la frustración del vendedor y transparenta los cuellos de botella operativos de la empresa. |
| **US-03** | Asesor | Quiero contar con un **Copiloto de IA** que redacte mis notas de seguimiento, consulte fichas técnicas oficiales de Ultracem e investigue datos del cliente, para resolver dudas técnicas y comerciales en segundos. | Reduce el tiempo administrativo en campo y eleva la precisión consultiva frente al ingeniero o ferretero. |
| **US-04** | Supervisor | Quiero ver un tablero con el ranking de rachas de mi equipo, las toneladas proyectadas y el estado de los casos escalados, para intervenir a tiempo en cuentas críticas y premiar la constancia. | Gestión preventiva basada en datos reales de actividad diaria y resolución de bloqueos internos. |

---

## 4. Mecánica de Gamificación y Reglas de Negocio (Criterio Ultracem)

### A. La Regla de Oro (Corte 11:59 PM)
El asesor suma **+1 día de racha** si, antes de las 11:59 PM, el 100% de sus clientes ubicados en **Riesgo Crítico (Rojo)** tuvieron al menos una acción válida registrada durante la jornada.

### B. Acciones Válidas que Salvan la Racha
1. **Seguimiento Efectivo:** Llamada, visita en obra/ferretería o mensaje contestado con minuta registrada en el CRM.
2. **Intento Documentado:** El cliente estaba en fundida de placa o no contestó, pero el asesor dejó evidencia del intento y el sistema reprogramó recordatorio automático.
3. **Escalamiento Departamental:** El asesor gestionó al cliente, detectó un bloqueo interno y transfirió el ticket al área responsable.

### C. Segmentación Inteligente de "Días de Riesgo" (Estilo Salesforce)
Dado que Ultracem atiende dos canales con velocidades de compra distintas, el semáforo ajusta sus umbrales automáticamente según el perfil del cliente:

| Canal / Tipo de Cliente | 🟢 Saludable | 🟡 En Advertencia | 🔴 Riesgo Crítico (Obligatorio hoy) | Criterio Comercial Ultracem |
| :--- | :--- | :--- | :--- | :--- |
| **Canal Tradicional (Ferreterías y Depósitos)** | 0 a 2 días | 3 a 4 días | **+5 días sin contacto** | Alta rotación semanal de sacos de 50 kg; al 5to día sin atención existe alto riesgo de compra a la competencia. |
| **Canal Industrial (Constructoras y Obras)** | 0 a 4 días | 5 a 7 días | **+8 días o cotización a 24h de vencer** | Ciclos ligados al cronograma de obra; el riesgo se dispara por inactividad prolongada o cotizaciones de granel/concreto por expirar. |

### D. Matriz de Escalamiento y SLAs Internos
Para que el escalamiento sea auditable en el panel del supervisor, cada área tiene un tiempo máximo de respuesta (SLA):
* **Cartera y Crédito (SLA: 4 horas laborales):** Liberación de cupos bloqueados o validación de pagos pendientes.
* **Logística y Despachos (SLA: 2 horas laborales):** Rastreo en tiempo real de tractomulas de cemento o camiones mixer en ruta hacia la obra.
* **Soporte Técnico y Calidad (SLA: 6 horas laborales):** Solicitud de certificados de calidad, diseños de mezcla o asesoría en norma NTC 121.
* **Gerencia Comercial / Pricing (SLA: 4 horas laborales):** Aprobación de descuentos especiales por volumen en toneladas.

### E. Regla de "Fraguado Seguro" (Protección y Congelamiento de Racha)
* **Domingos y Festivos:** El reloj de las 11:59 PM entra en modo *"Fraguado"* (pausa automática para proteger el descanso). Si el asesor registra actividad voluntaria, recibe un **Multiplicador x1.5 de puntos**.
* **Escudo "Casco de Seguridad":** Por cada **7 días consecutivos de racha**, el asesor desbloquea 1 *"Casco Protector"* en su inventario, el cual congela su racha por 24 horas en caso de incapacidad médica o imprevistos en carretera.

---

## 5. Arquitectura del Copiloto IA (Asistencia Integral)

1. **Redacción Inteligente de Minutas y Escritos:** El asesor dicta por voz o escribe ideas rápidas (*"Hablé con Ferretería El Sol, pide 30 toneladas de Cemento Uso General para el viernes, pero requiere revisión de cupo"*) y la IA redacta la nota formal en el CRM, programa el seguimiento y genera el borrador de WhatsApp/correo para el cliente.
2. **Consultor Técnico Oficial Ultracem (RAG Documental):** Respuestas instantáneas basadas en las fichas técnicas oficiales del portafolio Ultracem (*Cemento Uso General, Cemento Estructural, Cemento Marino, Cemento Blanco, Morteros Secos y Concretos*), incluyendo resistencias, tiempos de fraguado y normativa NTC.
3. **Investigador Contextual de Cuenta:** Analiza el historial de compras de los últimos 90 días del cliente y cruza información externa (nuevas licitaciones, obras adjudicadas o crecimiento de la constructora) para darle argumentos de venta al asesor antes de llamar.
4. **Priorizador Dinámico de Agenda:** Ordena la lista diaria del asesor combinando: `Nivel de Riesgo` + `Potencial de Toneladas` + `Probabilidad de Cierre`.

---

## 6. Alcance Sí / No (MVP Día 1)

### Alcance SÍ (Incluido en la entrega de hoy)
* Diseño de flujos completos de alta fidelidad en **Stitch** (Vista Móvil del Asesor + Dashboard Web del Supervisor) aplicando la identidad visual de Ultracem.
* Visualización clara del contador de rachas, reloj de corte (11:59 PM), inventario de "Casco Protector" y semáforo de Días de Riesgo por canal.
* Flujo interactivo de **Escalamiento interdepartamental** con visualización de SLAs.
* Interfaz del **Copiloto IA** integrada en la vista del cliente (pestañas de: Redactar Escrito, Consultar Ficha Técnica Ultracem e Investigar Cliente).
* Guion de marca, creación de mascota corporativa y estrategia de activación en redes sociales.

### Alcance NO (Excluido de este MVP)
* Integración bidireccional en vivo con el ERP/SAP de Ultracem para facturación electrónica o inventario físico de planta `[SUPUESTO]`.
* Central telefónica VoIP embebida dentro de la aplicación `[SUPUESTO]`.
* Liquidación y dispersión automática de bonos monetarios en el sistema de nómina `[SUPUESTO]`.

---

## 7. Fases Verificables de Ejecución

| Fase | Entregable / Hito | Criterio de Verificación |
| :--- | :--- | :--- |
| **Fase 1: Diseño UI/UX en Stitch** | Prototipo visual Mobile (Asesor) y Web (Supervisor). | Navegación clara entre roles usando los colores corporativos de Ultracem (Azul, Verde y Blanco) más acentos de gamificación. |
| **Fase 2: Motor de Racha y Riesgo** | Flujo de resolución de cuentas en rojo antes de las 11:59 PM. | Demostración visual de cómo gestionar o escalar un cliente en Riesgo Crítico actualiza su estado y asegura la racha del día. |
| **Fase 3: Copiloto IA Contextual** | Interfaz del asistente con casos reales del portafolio Ultracem. | Visualización de una consulta técnica real (ej. Cemento Estructural vs. Uso General) y generación automática de minuta. |
| **Fase 4: Activación de Marca y Pitch** | Guion de campaña para redes y narrativa de venta ejecutiva. | Pitch estructurado desde el minuto uno como solución de negocio lista para presentar a la directiva de Ultracem. |

---

## 8. Criterios de Aceptación
* **CA-01 (Branding):** La interfaz en Stitch respeta el logo y la paleta oficial de Ultracem, integrando elementos visuales de gamificación sin perder sobriedad corporativa.
* **CA-02 (Foco en Racha y Riesgo):** El asesor identifica en menos de 3 segundos cuántos días lleva de racha, cuánto tiempo falta para las 11:59 PM y cuáles son sus clientes en semáforo rojo.
* **CA-03 (Salvavidas por Escalamiento):** Existe el botón **"Escalar Caso"** con selección de los 4 departamentos de Ultracem, liberando al asesor de bloqueos ajenos a su gestión.
* **CA-04 (Copiloto Integral):** La pantalla del Copiloto IA muestra explícitamente las funciones de redacción de mensajes, consulta de fichas técnicas oficiales e investigación de cliente.
* **CA-05 (Visibilidad de Líder):** El dashboard del supervisor muestra métricas de toneladas, ranking de rachas del equipo y tabla de casos escalados con sus respectivos SLAs.

---

## 9. Qué se Corta Primero y Plan de Respaldo (Fallback de IA)

### Qué se corta primero si hay restricción de tiempo:
1. **Scraping web externo en vivo sobre constructoras:** Se prioriza el resumen inteligente basado en el historial interno de compras del cliente en Ultracem.
2. **Animaciones 3D complejas de la mascota:** Se utilizan avatares 2D expresivos de alto impacto en tres estados (En Racha 🔥, Alerta Nocturna ⚠️, Meta Cumplida 🏆).
3. **Vistas de configuración avanzada del supervisor:** Se concentra el dashboard web en una sola vista maestra de alto impacto ejecutivo.

### Respaldo si la IA falla (Plan de Contingencia Operativa):
* **Falla en generación de texto/minutas:** El sistema despliega automáticamente **Chips de Registro Rápido en 1 Clic** (*"Cliente en fundida, llamar mañana"*, *"Solicita cotización Cemento UG"*, *"Escalado a Cartera por cupo"*).
* **Falla en consulta RAG de fichas técnicas:** Se activa un visor offline con las fichas técnicas en PDF de los productos principales de Ultracem.
* **Falla en el algoritmo priorizador:** La bandeja de clientes se ordena por regla determinista tradicional: de mayor a menor según `días_sin_contacto` y `toneladas_promedio`.

---

## 10. Guion de Marca y Estrategia de Activación en Redes

### Identidad del Producto y Mascota
* **Nombre del Producto:** **UltraRacha** *(El motor comercial de Ultracem)*.
* **La Mascota:** **"Don Fraguado" (o "CemenTito")** — Un carismático personaje inspirado en un saco de cemento Ultracem con casco blanco de ingeniero, gafas de seguridad y botas de obra. Posee la personalidad dual de Duo (Duolingo): celebra con euforia cada tonelada cerrada, pero a las 10:00 PM cambia a modo intenso y dramático recordándole al asesor que no deje enfriar a sus clientes antes de las 11:59 PM.
* **Eslogan Oficial:** *"Que el cemento fragüe, pero que tu cliente nunca se enfríe"*.

### Sistema de Diseño (Guía Visual)
* **Paleta Corporativa Ultracem:** Azul Corporativo (`#0033A0` / `#004797` - confianza y estructura), Verde Ultracem (`#009639` - sostenibilidad y metas cumplidas) y Blanco/Gris Concreto para fondos limpios.
* **Acentos de Gamificación:** Naranja Fuego (`#FF6B00`) para rachas activas, Amarillo Advertencia (`#FFC107`) y Rojo Crítico (`#DC3545`) para clientes en riesgo de pérdida.

### Estrategia y Guion de Contenidos para Redes (TikTok / Instagram Reels / LinkedIn)

#### 1. Fase de Expectativa (Teaser Interno y Redes - 15s)
* **Visual:** Toma cinematográfica de un casco de obra sobre un escritorio a las 11:45 PM. El celular vibra y aparece "Don Fraguado" asomándose por la pantalla con una linterna.
* **Texto en pantalla / Audio:** *"En la construcción, un minuto tarde detiene una obra. En las ventas, un día tarde pierde un cliente. Llega UltraRacha. ¿Tienes lo necesario para mantener el fuego encendido?"*

#### 2. Video de Lanzamiento — Guion de Reel / TikTok (30s)
* **00s - 08s (El Problema):** Un asesor comercial en una obra bajo el sol del Caribe, lleno de llamadas perdidas, buscando en papeles arrugados qué precio dio la semana pasada mientras un ferretero le dice: *"Como no me llamaste, pedí el cemento en otro lado"*.
* **08s - 22s (La Transformación con Stitch + IA):** Aparece "Don Fraguado" chocando el casco y le activa **UltraRacha** en el móvil. Se muestra la interfaz diseñada en **Stitch**: el asesor ve al cliente en semáforo rojo, abre el **Copiloto IA** para enviar la ficha técnica del Cemento Estructural en 2 segundos, escala una liberación de cupo a Cartera con un toque y ¡BUM!, su racha sube a **21 días seguidos 🔥** ganando el escudo "Casco de Seguridad".
* **22s - 30s (El Resultado):** El supervisor en oficina ve subir la barra de toneladas del equipo en el Dashboard Web. Cierre con logo de Ultracem: *"UltraRacha: Construyendo relaciones sólidas, todos los días"*.

#### 3. Activación Corporativa B2B (LinkedIn)
* **Formato:** Carrusel interactivo titulado *"Cómo en Ultracem convertimos el seguimiento comercial en un deporte de alto rendimiento con IA y Gamificación"*, destacando la reducción en tiempos de respuesta al cliente y la sinergia entre ventas, cartera y logística.

---

## 11. Prompt Maestro Optimizado para Stitch

> **Instrucciones:** Copia y pega este prompt en Stitch adjuntando el logo y la paleta de colores de Ultracem para generar las pantallas del proyecto:
>
> Diseña una prueba de concepto UI/UX de alta fidelidad para "UltraRacha", el CRM gamificado de Ultracem (empresa líder de cemento y concreto). Aplica la identidad visual de Ultracem (Azul corporativo, Verde progreso y Blanco/Gris concreto) combinada con una estética moderna estilo Duolingo + Salesforce.
> 
> Genera dos vistas principales conectadas:
> 
> 1. **Mobile App (User Flow Asesor Comercial):**
>    - **Header Gamificado:** Perfil del asesor, contador destacado de "Racha Activa: 21 días 🔥", ícono de comodín "Casco Protector activado ⛑️", reloj de cuenta regresiva "Cierre de hoy: 11:59 PM" y avatar de la mascota "Don Fraguado" (saco de cemento animado con casco de ingeniero).
>    - **Progreso Comercial:** Barra de meta mensual en Toneladas (ej. 420 / 500 Toneladas vendidas).
>    - **Bandeja de Clientes por Días de Riesgo (Estilo Salesforce):** Tarjetas de clientes diferenciadas por canal ("Constructora Bolívar - Obra Norte" y "Ferretería El Constructor") con etiquetas de semáforo: Rojo Crítico ("+8 días sin contacto - Cotización vence hoy") y Amarillo ("4 días sin contacto").
>    - **Acciones en 1 Clic por Cliente:** Tres botones claros: "Registrar Seguimiento", "Escalar Caso (Cartera / Logística / Técnico)" y "Copiloto IA ✨".
>    - **Drawer/Modal del Copiloto IA:** Mostrando tres funciones activas: 1) Redacción automática de minuta y mensaje por voz/texto, 2) Consulta rápida de Ficha Técnica Oficial Ultracem (Cemento Uso General vs. Estructural NTC 121), y 3) Resumen de investigación e historial del cliente.
> 
> 2. **Web Dashboard (User Flow Supervisor / Líder Comercial):**
>    - **KPIs Superiores:** Total Toneladas del Equipo, % de Seguimiento Oportuno, Clientes en Riesgo Crítico salvados hoy y Tickets Escalados activos.
>    - **Leaderboard Gamificado:** Tabla "Liga Maestros Ultracem" con el ranking de asesores según su racha de días consecutivos, medallas y toneladas cerradas.
>    - **Panel de Auditoría de Escalamientos y SLAs:** Lista en tiempo real de casos escalados a Cartera (SLA 4h), Logística (SLA 2h) y Soporte Técnico (SLA 6h) para desbloquear ventas rápidamente.
