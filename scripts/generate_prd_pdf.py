# -*- coding: utf-8 -*-
"""
Script to generate the Official Executive PRD PDF for UltraRacha CRM (Ultracem S.A.S.).
8 balanced, comprehensive, and concise pages with 100% solid colors, publication-grade styling,
and automated PyMuPDF running headers/footers.
"""

import os
import subprocess
import fitz # PyMuPDF

def load_logo_base64():
    logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo_base64.txt")
    if os.path.exists(logo_path):
        with open(logo_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""

def build_prd_html():
    logo_base64 = load_logo_base64()
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>PRD Maestro: UltraRacha CRM — Ultracem S.A.S.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Montserrat:wght@400;500;600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4 portrait;
      margin: 10mm 12mm 12mm 12mm;
    }}
    
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    
    body {{
      font-family: 'Outfit', 'Montserrat', sans-serif;
      color: #0A233F;
      background-color: #FFFFFF;
      font-size: 8.5pt;
      line-height: 1.38;
    }}

    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Exact Page Containers for Pixel-Perfect Multi-page Layout */
    .page {{
      page-break-after: always;
      break-after: page;
      min-height: 260mm;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
    }}

    .page:last-child {{
      page-break-after: auto;
      break-after: auto;
    }}

    .avoid-break {{
      page-break-inside: avoid;
      break-inside: avoid;
    }}

    /* Cover Page Styles */
    .cover-container {{
      min-height: 260mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 3px solid #003E78;
      border-top: 12px solid #FDCA02;
      border-radius: 12px;
      padding: 20mm 16mm 16mm 16mm;
      background: #FFFFFF;
      box-sizing: border-box;
    }}

    .cover-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #E5E7EB;
      padding-bottom: 14px;
    }}

    .cover-logo-box {{
      padding: 8px 16px;
      background: #FFFFFF;
      border: 2px solid #FDCA02;
      border-radius: 8px;
      display: inline-block;
    }}

    .cover-logo-box img {{
      height: 44px;
      width: auto;
      display: block;
    }}

    .badge-pill {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 7pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .badge-corp {{
      background: #003E78;
      color: #FFFFFF;
    }}

    .badge-yellow {{
      background: #FDCA02;
      color: #003E78;
    }}

    .badge-green {{
      background: #D1FAE5;
      color: #065F46;
      border: 1px solid #34D399;
    }}

    .badge-red {{
      background: #FEE2E2;
      color: #991B1B;
      border: 1px solid #F87171;
    }}

    .badge-amber {{
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #FCD34D;
    }}

    .badge-slate {{
      background: #F1F5F9;
      color: #334155;
      border: 1px solid #CBD5E1;
    }}

    .cover-title-group {{
      margin: 18px 0;
    }}

    .cover-title-pre {{
      font-size: 10pt;
      font-weight: 800;
      color: #FDCA02;
      background: #003E78;
      display: inline-block;
      padding: 4px 12px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      margin-bottom: 12px;
    }}

    .cover-title {{
      font-size: 26pt;
      font-weight: 900;
      color: #003E78;
      line-height: 1.12;
      letter-spacing: -0.5px;
      margin-bottom: 10px;
    }}

    .cover-subtitle {{
      font-size: 11.5pt;
      font-weight: 600;
      color: #4B5563;
      line-height: 1.35;
      margin-bottom: 16px;
    }}

    .cover-manifesto {{
      background: #F2F1EC;
      border-left: 6px solid #FDCA02;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 10.5pt;
      font-weight: 700;
      color: #003E78;
      font-style: italic;
    }}

    .cover-meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-top: 18px;
      border-top: 2px solid #E5E7EB;
      padding-top: 16px;
    }}

    .meta-box {{
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      padding: 8px 12px;
    }}

    .meta-label {{
      font-size: 7pt;
      text-transform: uppercase;
      font-weight: 700;
      color: #64748B;
      letter-spacing: 0.5px;
    }}

    .meta-val {{
      font-size: 8.8pt;
      font-weight: 800;
      color: #003E78;
      margin-top: 2px;
    }}

    /* Content Header Bar */
    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #003E78;
      padding-bottom: 6px;
      margin-bottom: 10px;
      flex-shrink: 0;
    }}

    .header-bar .doc-title {{
      font-size: 7.8pt;
      font-weight: 800;
      color: #003E78;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .header-bar .doc-version {{
      font-size: 7.2pt;
      font-weight: 700;
      color: #64748B;
      font-family: 'JetBrains Mono', monospace;
    }}

    .section-title {{
      display: flex;
      align-items: center;
      gap: 7px;
      font-size: 11pt;
      font-weight: 900;
      color: #003E78;
      margin: 7px 0 5px 0;
      padding-bottom: 3px;
      border-bottom: 1.5px solid #FDCA02;
      text-transform: uppercase;
      letter-spacing: -0.2px;
      flex-shrink: 0;
    }}

    .section-title-num {{
      background: #003E78;
      color: #FDCA02;
      font-size: 8pt;
      font-weight: 900;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .sub-title {{
      font-size: 8.8pt;
      font-weight: 800;
      color: #0A233F;
      margin: 6px 0 3px 0;
      flex-shrink: 0;
    }}

    p {{
      margin-bottom: 5px;
      text-align: justify;
      color: #1F2937;
    }}

    /* Tables */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 5px 0 7px 0;
      font-size: 7.2pt;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      overflow: hidden;
    }}

    table.data-table th {{
      background: #003E78;
      color: #FFFFFF;
      padding: 4px 6px;
      text-align: left;
      font-weight: 800;
      text-transform: uppercase;
      font-size: 6.8pt;
      letter-spacing: 0.3px;
      border-right: 1px solid #1E4E79;
    }}

    table.data-table th:last-child {{
      border-right: none;
    }}

    table.data-table td {{
      padding: 3.5px 6px;
      border-bottom: 1px solid #E2E8F0;
      border-right: 1px solid #E2E8F0;
      vertical-align: middle;
      color: #1E293B;
    }}

    table.data-table td:last-child {{
      border-right: none;
    }}

    table.data-table tr:nth-child(even) {{
      background-color: #F8FAFC;
    }}

    table.data-table tr:last-child td {{
      border-bottom: none;
    }}

    /* Grids & Cards */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 5px 0;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 7px;
      margin: 5px 0;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin: 5px 0;
    }}

    .card {{
      background: #FFFFFF;
      border: 1.5px solid #CBD5E1;
      border-radius: 7px;
      padding: 7px 9px;
    }}

    .card-accent-blue {{
      border-left: 4px solid #003E78;
    }}

    .card-accent-yellow {{
      border-left: 4px solid #FDCA02;
    }}

    .card-accent-green {{
      border-left: 4px solid #059669;
    }}

    .card-accent-red {{
      border-left: 4px solid #DC2626;
    }}

    .card-cement {{
      background: #F2F1EC;
      border: 1.5px solid #D5D3CA;
    }}

    .card-title {{
      font-size: 8pt;
      font-weight: 800;
      color: #003E78;
      margin-bottom: 3px;
      display: flex;
      align-items: center;
      gap: 4px;
    }}

    .metric-hero {{
      font-size: 12pt;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
      color: #003E78;
      line-height: 1;
    }}

    .metric-sub {{
      font-size: 6.8pt;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
      margin-top: 2px;
    }}

    .feature-list {{
      list-style: none;
      padding-left: 0;
      margin: 3px 0 4px 0;
    }}

    .feature-list li {{
      position: relative;
      padding-left: 11px;
      margin-bottom: 2.5px;
      font-size: 7.2pt;
      color: #1F2937;
    }}

    .feature-list li::before {{
      content: "■";
      position: absolute;
      left: 0;
      top: 0;
      color: #FDCA02;
      font-size: 6.5pt;
    }}

    .feature-list.blue li::before {{
      color: #003E78;
    }}

    /* Diagrams & Flows */
    .flow-step {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      padding: 4px 7px;
      margin-bottom: 3.5px;
    }}

    .flow-badge {{
      background: #003E78;
      color: #FDCA02;
      font-weight: 800;
      font-size: 6.8pt;
      padding: 2px 5px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }}
  </style>
</head>
<body>

  <!-- ============================================================== -->
  <!-- PÁGINA 1: PORTADA EJECUTIVA                                    -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="cover-container">
      <div class="cover-header">
        <div class="cover-logo-box">
          <img src="data:image/png;base64,{logo_base64}" alt="Ultracem Cemento y Concreto" />
        </div>
        <div>
          <span class="badge-pill badge-corp">Documento Oficial PRD</span>
          <span class="badge-pill badge-yellow">Versión 2.0</span>
        </div>
      </div>

      <div class="cover-title-group">
        <div class="cover-title-pre">Product Requirements Document (PRD)</div>
        <h1 class="cover-title">UltraRacha CRM</h1>
        <p class="cover-subtitle">
          Ecosistema Comercial Gamificado, Prevención Antichurn, Cartografía B2B & Copiloto IA de Terreno para la Industria de Materiales de Construcción.
        </p>

        <div class="cover-manifesto">
          “Que el cemento fragüe, pero que tu cliente nunca se enfríe.”
          <div style="font-size: 7.5pt; font-weight: 600; color: #4B5563; margin-top: 4px; font-style: normal;">
            Desarrollado para la fuerza de ventas técnica de <strong>Ultracem S.A.S.</strong> bajo el framework de aceleración <strong>Semillero by CooWeb</strong>.
          </div>
        </div>
      </div>

      <div>
        <div class="cover-meta-grid">
          <div class="meta-box">
            <div class="meta-label">Cliente / Aliado Estratégico</div>
            <div class="meta-val">Ultracem S.A.S. (Colombia & Guatemala)</div>
          </div>
          <div class="meta-box">
            <div class="meta-label">Epicentro Operativo</div>
            <div class="meta-val">Planta Galapa • Km 8 Vía Tubará, Atlántico</div>
          </div>
          <div class="meta-box">
            <div class="meta-label">Framework de Origen</div>
            <div class="meta-val">Semillero by CooWeb (Aceleración de Talento)</div>
          </div>
          <div class="meta-box">
            <div class="meta-label">Fecha de Liberación</div>
            <div class="meta-val">Octubre 2026 • Entorno Producción</div>
          </div>
          <div class="meta-box">
            <div class="meta-label">Estado de Ingeniería</div>
            <div class="meta-val">
              <span class="badge-pill badge-green">Aprobado para Producción</span>
            </div>
          </div>
          <div class="meta-box">
            <div class="meta-label">Normativas Clave</div>
            <div class="meta-val">NTC 121 / NTC 321 / NTC 3318 (ICONTEC)</div>
          </div>
        </div>

        <div style="margin-top: 14px; border-top: 1px solid #E5E7EB; padding-top: 10px; display: flex; justify-content: space-between; font-size: 7pt; color: #64748B;">
          <span><strong>Clasificación:</strong> Confidencial / Corporativo Ultracem</span>
          <span><strong>Distribución:</strong> Dirección Comercial, Logística, Operaciones & Tech</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 2: RESUMEN EJECUTIVO & CONTEXTO DE NEGOCIO              -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 1 & 2</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">01</span>
      <span>Resumen Ejecutivo & Problema de Negocio</span>
    </div>

    <p>
      En la comercialización de cemento y concreto premezclado, la velocidad y oportunidad del contacto comercial determinan la supervivencia de la cartera. En el Caribe colombiano, las decisiones de compra no ocurren en oficinas lejanas: se toman a pie de obra antes de fundir una placa o en el mostrador de una ferretería con camiones esperando bultos. Si un asesor tarda más de 24 horas en cotizar o resolver un cupo, el contratista compra de inmediato a Argos o Cemex.
    </p>

    <div class="grid-2">
      <div class="card card-accent-red avoid-break">
        <div class="card-title" style="color: #DC2626;">
          <span>⚠️</span> <span>El Dolor Operativo (Línea Base)</span>
        </div>
        <ul class="feature-list">
          <li><strong>Seguimiento Tardío:</strong> Tiempos de respuesta de hasta 48 horas en cotizaciones por sobrecarga en campo.</li>
          <li><strong>Fuga Inmediata a la Competencia:</strong> Pérdida del 35% de cotizaciones abiertas ante ofertas agresivas.</li>
          <li><strong>Bloqueos Interdepartamentales Invisibles:</strong> Despachos detenidos en Cartera o Logística sin aviso rápido al vendedor.</li>
          <li><strong>Resistencia al CRM Tradicional:</strong> 60% de rechazo a sistemas complejos por alta fricción de digitación en obra.</li>
        </ul>
      </div>

      <div class="card card-accent-green avoid-break">
        <div class="card-title" style="color: #059669;">
          <span>🎯</span> <span>La Solución UltraRacha CRM</span>
        </div>
        <ul class="feature-list">
          <li><strong>Gamificación Antichurn con Corte 11:59 PM:</strong> Hábito diario innegociable sincronizado con Planta Galapa.</li>
          <li><strong>Copiloto IA Técnico con Guardrails NTC 121:</strong> Consultas de resistencia (2500/3000/4000 PSI) y notas de voz Whisper.</li>
          <li><strong>Escalamiento con SLAs Vinculantes:</strong> Transferencia en 1 clic a Cartera (4h), Logística (2h) o Laboratorio (6h).</li>
          <li><strong>Cartografía B2B en Tiempo Real:</strong> 12 prospectos estratégicos geolocalizados y rutas directas de visita.</li>
        </ul>
      </div>
    </div>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">02</span>
      <span>Objetivos Estratégicos & Métricas de Impacto (KPIs)</span>
    </div>

    <p>
      El proyecto establece metas cuantitativas auditables sobre la operación de Planta Galapa y la fuerza comercial del Caribe:
    </p>

    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Indicador / Métrica Clave</th>
          <th>Situación Inicial (Línea Base)</th>
          <th>Meta UltraRacha (Año 1)</th>
          <th>Impacto Económico / Operativo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Tiempo Primer Contacto a Cotización</strong></td>
          <td>48 horas promedio</td>
          <td><strong>&lt; 4 horas laborales</strong></td>
          <td>Incremento de conversión de cierre en un 38%.</td>
        </tr>
        <tr>
          <td><strong>Pérdida de Cotizaciones por Abandono</strong></td>
          <td>35% de oportunidades perdidas</td>
          <td><strong>&lt; 5% de abandono</strong></td>
          <td>Recuperación estimada de 4,200 Toneladas/año.</td>
        </tr>
        <tr>
          <td><strong>Adopción Diaria de la Fuerza Comercial</strong></td>
          <td>40% (registro esporádico)</td>
          <td><strong>&gt; 92% adherencia activa</strong></td>
          <td>Información de campo en tiempo real para gerencia.</td>
        </tr>
        <tr>
          <td><strong>Resolución de Bloqueos Internos (SLAs)</strong></td>
          <td>3 a 4 días laborales</td>
          <td><strong>&lt; 4 horas hábiles</strong></td>
          <td>Despachos Just-in-Time sin retrasos de cuadrilla.</td>
        </tr>
        <tr>
          <td><strong>Tasa de Recompra (Retención Activa)</strong></td>
          <td>78.5% retención mensual</td>
          <td><strong>94.2% retención sostenida</strong></td>
          <td>Blindaje de clientes clave frente a Argos y Cemex.</td>
        </tr>
        <tr>
          <td><strong>Cumplimiento de Entrega (OTD) Galapa</strong></td>
          <td>74% a tiempo en obra</td>
          <td><strong>93.0% entregas puntuales</strong></td>
          <td>Tiempo promedio de entrega: 84 minutos.</td>
        </tr>
      </tbody>
    </table>

    <div class="grid-4 avoid-break" style="margin-top: 4px;">
      <div class="card card-cement">
        <div class="metric-hero">2,855 Ton</div>
        <div class="metric-sub">Pipeline Activo</div>
      </div>
      <div class="card card-cement">
        <div class="metric-hero">$910.8M</div>
        <div class="metric-sub">Valor Total COP</div>
      </div>
      <div class="card card-cement">
        <div class="metric-hero">94.2%</div>
        <div class="metric-sub">Tasa Recompra</div>
      </div>
      <div class="card card-cement">
        <div class="metric-hero">84 Min</div>
        <div class="metric-sub">OTD Promedio</div>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 3: ROLES, PERSONAS Y FLUJOS OPERATIVOS                  -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 3</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">03</span>
      <span>Roles, Arquetipos de Usuario & Flujos de Operación</span>
    </div>

    <div class="grid-2">
      <!-- Rol 1 -->
      <div class="card card-accent-blue avoid-break">
        <div class="card-title">
          <span>👷</span> <span>Rol 1: Asesor Comercial de Terreno (Mobile First)</span>
        </div>
        <p style="font-size: 7.4pt;"><strong>Arquetipo:</strong> Carlos Mendoza • Asesor Técnico Comercial Zona Norte (Atlántico / Bolívar).</p>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><strong>Contexto:</strong> 85% de su tiempo en frentes de obra y ferreterías con sol, polvo y ruido.</li>
          <li><strong>Objetivo:</strong> Cumplir cuota de 500 Ton/mes, mantener racha activa y retener clientes ferreteros.</li>
          <li><strong>Herramientas:</strong> Móvil, notas de voz Whisper, semáforos de riesgo y Copiloto IA de dosificación.</li>
          <li><strong>Frustración:</strong> Perder racha o ventas por demoras de Cartera o falta de fichas técnicas en sitio.</li>
        </ul>
      </div>

      <!-- Rol 2 -->
      <div class="card card-accent-yellow avoid-break">
        <div class="card-title">
          <span>👔</span> <span>Rol 2: Supervisor / Líder Comercial (Web Desktop)</span>
        </div>
        <p style="font-size: 7.4pt;"><strong>Arquetipo:</strong> Vanesa Peñaranda • Gerente Comercial Regional Caribe.</p>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><strong>Contexto:</strong> Sala de mando en Planta Galapa y oficinas corporativas en Barranquilla.</li>
          <li><strong>Objetivo:</strong> Monitorear embudo de 2,855 Ton, cumplimiento de SLAs y ranking de ligas comerciales.</li>
          <li><strong>Herramientas:</strong> Web Dashboard consolidado, tablero Kanban B2B, mapa de calor y auditoría de tickets.</li>
          <li><strong>Frustración:</strong> Enterarse tarde de una cuenta perdida o de pedidos represados en despacho.</li>
        </ul>
      </div>
    </div>

    <div class="sub-title">Matriz de Departamentos de Soporte y SLAs Operativos</div>
    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Departamento Ultracem</th>
          <th>SLA Comprometido</th>
          <th>Motivos de Escalamiento Válidos</th>
          <th>Criterio de Resolución</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cartera &amp; Crédito</strong></td>
          <td><span class="badge-pill badge-green">4 Horas Hábiles</span></td>
          <td>Cupo insuficiente, validación de consignación bancaria, ampliación de plazo a 30/60 días.</td>
          <td>Liberación de pedido en sistema comercial o reestructuración de cupo notificada al asesor.</td>
        </tr>
        <tr>
          <td><strong>Logística &amp; Despachos</strong></td>
          <td><span class="badge-pill badge-green">2 Horas Hábiles</span></td>
          <td>Rastreo satelital de tractomulas o mixers, reprogramación de turno en báscula Galapa.</td>
          <td>Confirmación de hora exacta de llegada a obra (ETA) o reasignación inmediata de vehículo.</td>
        </tr>
        <tr>
          <td><strong>Soporte Técnico &amp; Calidad</strong></td>
          <td><span class="badge-pill badge-green">6 Horas Hábiles</span></td>
          <td>Emisión de certificados de calidad NTC 121, diseño de mezcla especial, peritaje de fraguado.</td>
          <td>Envío de dossier técnico firmado por laboratorista oficial de Planta Galapa.</td>
        </tr>
        <tr>
          <td><strong>Gerencia / Pricing</strong></td>
          <td><span class="badge-pill badge-green">4 Horas Hábiles</span></td>
          <td>Descuento especial por volumen masivo (&gt;200 Ton), contraoferta ante ataque de precios Argos.</td>
          <td>Aprobación de tarifa especial con margen mínimo de contribución garantizado.</td>
        </tr>
      </tbody>
    </table>

    <div class="sub-title">Diagrama de Flujo del Ciclo Comercial Diario</div>
    <div class="card card-cement avoid-break">
      <div class="flow-step">
        <span class="flow-badge">07:00 AM</span>
        <strong style="color: #003E78; font-size: 7.4pt;">Apertura &amp; Priorización:</strong>
        <span style="font-size: 7.1pt; color: #4B5563;">Revisión de cuentas en Rojo Crítico y horas restantes para las 11:59 PM.</span>
      </div>
      <div class="flow-step">
        <span class="flow-badge">10:30 AM</span>
        <strong style="color: #003E78; font-size: 7.4pt;">Gestión en Obra / Ferretería:</strong>
        <span style="font-size: 7.1pt; color: #4B5563;">Check-in GPS, dictado de nota de voz con Whisper Turbo o cálculo de dosificación NTC 121.</span>
      </div>
      <div class="flow-step">
        <span class="flow-badge">03:45 PM</span>
        <strong style="color: #003E78; font-size: 7.4pt;">Detección de Traba &amp; Escalamiento:</strong>
        <span style="font-size: 7.1pt; color: #4B5563;">Cliente bloqueado por cartera; se escala a Cartera (SLA 4h). La racha queda protegida al instante.</span>
      </div>
      <div class="flow-step">
        <span class="flow-badge">11:59 PM</span>
        <strong style="color: #DC2626; font-size: 7.4pt;">Corte Estricto de Medianoche:</strong>
        <span style="font-size: 7.1pt; color: #4B5563;">100% de cuentas rojas gestionadas. Don Fraguado celebra racha (+100 PTS para recompensas).</span>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 4: MOTOR DE RACHA & PIPELINE B2B                        -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 4 (MÓDULOS 1 & 2)</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">04</span>
      <span>Módulo 1: Motor de Rachas & Regla de Oro (11:59 PM)</span>
    </div>

    <div class="card card-accent-yellow avoid-break">
      <div class="card-title">
        <span>⏰</span> <span>La Justificación Operativa del Corte 11:59 PM</span>
      </div>
      <p style="font-size: 7.4pt;">
        En la logística pesada de Planta Galapa, la planeación de molienda y asignación de tractomulas para despachos de las 6:30 AM se congela estrictamente a la medianoche. Todo pedido no gestionado antes de las 11:59 PM pierde su ventana matutina y corre riesgo de compra a la competencia. El asesor suma <strong>+1 día de racha</strong> si atiende el 100% de sus cuentas en semáforo rojo antes del corte.
      </p>
    </div>

    <div class="sub-title">Semáforo de Recompra Diferenciado por Canal (Estilo Salesforce Adaptado)</div>
    <div class="grid-2 avoid-break">
      <div class="card card-accent-blue">
        <div class="card-title">🏪 Canal Tradicional (Ferreterías)</div>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><span class="badge-pill badge-green">🟢 0-2 Días</span> <strong>Saludable:</strong> Rotación normal de sacos de 50 kg; stock estable.</li>
          <li><span class="badge-pill badge-amber">🟡 3-4 Días</span> <strong>Advertencia:</strong> Desaceleración; riesgo de quiebre de inventario.</li>
          <li><span class="badge-pill badge-red">🔴 +5 Días</span> <strong>Riesgo Crítico:</strong> Churn inminente. Contacto obligatorio hoy.</li>
        </ul>
      </div>

      <div class="card card-accent-yellow">
        <div class="card-title">🏗️ Canal Industrial (Constructoras / Obras)</div>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><span class="badge-pill badge-green">🟢 0-4 Días</span> <strong>Saludable:</strong> Consumo según cronograma de vaciado de losas.</li>
          <li><span class="badge-pill badge-amber">🟡 5-7 Días</span> <strong>Advertencia:</strong> Retraso en formaleta o cotización con Argos/Cemex.</li>
          <li><span class="badge-pill badge-red">🔴 +8 Días o 24h</span> <strong>Riesgo Crítico:</strong> Cotización por expirar o parada de obra.</li>
        </ul>
      </div>
    </div>

    <div class="sub-title">Las 4 Acciones Válidas de Salvaguarda de Racha (+100 a +150 XP)</div>
    <div class="grid-4 avoid-break">
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">1. Check-in GPS</strong>
        <span class="badge-pill badge-corp" style="margin: 2px 0;">+100 XP</span>
        <p style="font-size: 6.8pt; color: #4B5563;">Geocerca de 100m en frente de obra o mostrador.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">2. Nota Whisper</strong>
        <span class="badge-pill badge-corp" style="margin: 2px 0;">+120 XP</span>
        <p style="font-size: 6.8pt; color: #4B5563;">Nota de voz procesada con extracción de toneladas.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">3. WhatsApp NTC</strong>
        <span class="badge-pill badge-corp" style="margin: 2px 0;">+80 XP</span>
        <p style="font-size: 6.8pt; color: #4B5563;">Envío de cotización generada por Copiloto IA.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">4. Escalar SLA</strong>
        <span class="badge-pill badge-yellow" style="margin: 2px 0;">+150 XP</span>
        <p style="font-size: 6.8pt; color: #4B5563;">Traspaso de bloqueo a Cartera, Logística o Calidad.</p>
      </div>
    </div>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">05</span>
      <span>Módulo 2: Pipeline Comercial B2B (5 Etapas Industriales)</span>
    </div>

    <p>
      Estructura de embudo diseñada para contratos pesados de cemento a granel, concreto premezclado y sacos paletizados:
    </p>

    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Etapa del Pipeline</th>
          <th>Definición Operativa</th>
          <th>Criterio de Salida / Avance</th>
          <th>Cuentas / Volumen</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Obra Identificada</strong></td>
          <td>Prospección de licitación, licencia de curaduría o excavación inicial.</td>
          <td>Identificación de constructor, metros cúbicos y fecha de vaciado.</td>
          <td>4 Cuentas • 820 Ton</td>
        </tr>
        <tr>
          <td><strong>2. Cotización Técnica</strong></td>
          <td>Propuesta comercial con dosificación NTC 121 y tarifa por tonelada.</td>
          <td>Aceptación de precio base o solicitud de ensayos previos.</td>
          <td>3 Cuentas • 650 Ton</td>
        </tr>
        <tr>
          <td><strong>3. Muestra &amp; Ensayo NTC 121</strong></td>
          <td>Envío de cilindros de prueba y rotura a 3, 7 y 28 días en laboratorio.</td>
          <td>Certificado de resistencia &gt; 100% de la norma requerida.</td>
          <td>2 Cuentas • 485 Ton</td>
        </tr>
        <tr>
          <td><strong>4. Cierre &amp; Despacho</strong></td>
          <td>Orden de compra formal, cupo de crédito aprobado y programación.</td>
          <td>Generación de orden de cargue en báscula Galapa.</td>
          <td>2 Cuentas • 410 Ton</td>
        </tr>
        <tr>
          <td><strong>5. Suministro Continuo</strong></td>
          <td>Despacho periódico 'Just-in-Time' con monitoreo antichurn diario.</td>
          <td>Retención activa y recompra continua sin alertas rojas.</td>
          <td>3 Cuentas • 490 Ton</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 5: COPILOTO IA, WHISPER & RADAR CARTOGRÁFICO            -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 5 (MÓDULOS 3 & 4)</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">06</span>
      <span>Módulo 3: Copiloto IA Multimodelo & Consola Whisper Turbo</span>
    </div>

    <div class="grid-2">
      <div class="card card-accent-blue avoid-break">
        <div class="card-title">
          <span>🤖</span> <span>Arquitectura Multimodelo & Guardrails NTC 121</span>
        </div>
        <p style="font-size: 7.4pt;">
          Conectividad universal compatible con el estándar OpenAI Schema con conmutación dinámica:
        </p>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><strong>Groq Cloud LPU:</strong> `llama-3.3-70b-versatile`, `gpt-oss-120b` y `gpt-oss-20b` con inferencia ultrarrápida (500 a 1,000 tokens/s).</li>
          <li><strong>NVIDIA NIM:</strong> `llama-3-70b-instruct` y `mistral-nemo-12b` vía proxy Node.js sin bloqueos CORS.</li>
          <li><strong>DeepSeek API:</strong> `deepseek-chat` (V3) y `deepseek-reasoner` (R1) para cubicaciones complejas de concreto.</li>
          <li><strong>Guardrails Estrictos:</strong> La IA rechaza temas no constructivos y responde exclusivamente sobre especificaciones de Cemento Estructural Max, Uso General, Marino, dosificación 3000 PSI y manejo de objeciones.</li>
        </ul>
      </div>

      <div class="card card-accent-yellow avoid-break">
        <div class="card-title">
          <span>🎙️</span> <span>Consola de Voz Whisper Large V3 Turbo</span>
        </div>
        <p style="font-size: 7.4pt;">
          Diseñada para el entorno ruidoso de la construcción (mezcladoras, vibradores y camiones):
        </p>
        <ul class="feature-list" style="font-size: 7.1pt;">
          <li><strong>Dictado Rápido:</strong> Grabación audible de 15 a 45 segundos sin necesidad de escribir en teclado bajo el sol.</li>
          <li><strong>Transcripción Instantánea:</strong> Procesamiento con Groq Audio (`whisper-large-v3-turbo`) en español colombiano.</li>
          <li><strong>Extracción de Entidades:</strong> Identifica nombre de la constructora/ferretería, producto requerido (Estructural Max, Gris, Granel), volumen en toneladas y fecha de colado.</li>
          <li><strong>Almacenamiento Local:</strong> Respaldo en `localStorage` con reproductor táctil para auditoría de campo.</li>
        </ul>
      </div>
    </div>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">07</span>
      <span>Módulo 4: Radar Cartográfico Leaflet & Directorio B2B</span>
    </div>

    <p>
      Motor de mapeo espacial basado en <strong>Leaflet 1.9.4</strong> con capas satelitales y de calles de <strong>ESRI (World Street Map & World Imagery)</strong> sin dependencia de API keys privadas:
    </p>

    <div class="grid-3 avoid-break">
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">🟡 Planta Galapa (Central)</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 2px;">Km 8 Vía Tubará. Monitoreo de hornos clinker a 1,450 °C y flota de tractomulas.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">🔵 Cuentas Clave Activas</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 2px;">Constructoras Bolívar (Torres del Mar), Marval (Riomar), Ferretería El Constructor.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #DC2626; font-size: 7.4pt; display: block;">🔴 Plantas Competidoras</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 2px;">Monitoreo de Argos (Vía 40) y Cemex (Caracolí) para contramedidas de precio y entrega.</p>
      </div>
    </div>

    <div class="sub-title">Muestra del Directorio Estratégico B2B del Caribe (12 Cuentas Mapeadas)</div>
    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Cuenta / Proyecto</th>
          <th>Ciudad / Ubicación</th>
          <th>Canal</th>
          <th>Volumen Estimado</th>
          <th>Estado / Competidor Actual</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Torres del Mar (Const. Bolívar)</strong></td>
          <td>Barranquilla • Cra 58 #91</td>
          <td>Industrial (VIS)</td>
          <td><strong>450 Ton / Mes</strong></td>
          <td>Activo • Suministro Continuo Ultracem</td>
        </tr>
        <tr>
          <td><strong>Altos de Riomar (Marval)</strong></td>
          <td>Barranquilla • Cl 84 #51B</td>
          <td>Industrial (No VIS)</td>
          <td><strong>380 Ton / Mes</strong></td>
          <td>En cotización • Ensayos NTC 121 vigentes</td>
        </tr>
        <tr>
          <td><strong>Doble Calzada Ruta Caribe</strong></td>
          <td>Malambo • Vía Oriental</td>
          <td>Infraestructura 4G</td>
          <td><strong>800 Ton Granel</strong></td>
          <td>Bloqueado por cupo • Escalado a Cartera</td>
        </tr>
        <tr>
          <td><strong>Ferretería El Constructor</strong></td>
          <td>Soledad • Calle 30</td>
          <td>Tradicional</td>
          <td><strong>120 Ton (Sacos)</strong></td>
          <td>Riesgo Amarillo (3 días sin pedido)</td>
        </tr>
        <tr>
          <td><strong>Parque Heredia (Amarilo)</strong></td>
          <td>Cartagena • Cordialidad</td>
          <td>Industrial (VIS)</td>
          <td><strong>500 Ton / Mes</strong></td>
          <td>Prospecto • Competidor actual: Argos</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 6: SUPERVISOR, RECOMPENSAS & DON FRAGUADO               -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 6 (MÓDULOS 5, 6 & 7)</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">08</span>
      <span>Módulo 5: Centro de Mando del Supervisor & Telemetría Galapa</span>
    </div>

    <p>
      Consola unificada para la gerencia regional que conecta en tiempo real los datos comerciales de campo con los indicadores operativos de Planta Galapa:
    </p>

    <div class="grid-3 avoid-break">
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Telemetría de Molienda</strong>
        <div class="metric-hero" style="font-size: 11pt; margin-top: 2px;">180 T/h • 93%</div>
        <p style="font-size: 6.8pt; color: #4B5563;">Cumplimiento global de producción; hornos a 1,450 °C.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Tiempos de Entrega (OTD)</strong>
        <div class="metric-hero" style="font-size: 11pt; margin-top: 2px;">84 Min Promedio</div>
        <p style="font-size: 6.8pt; color: #4B5563;">94.2% de mixers y tractomulas a tiempo en obra.</p>
      </div>
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Auditoría de Escalamientos</strong>
        <div class="metric-hero" style="font-size: 11pt; margin-top: 2px;">4 Tickets Activos</div>
        <p style="font-size: 6.8pt; color: #4B5563;">Control de cuellos de botella en Cartera y Logística.</p>
      </div>
    </div>

    <div class="sub-title">Ranking Regional: Liga Maestros del Cemento & Auditoría de Despachos</div>
    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Asesor Comercial</th>
          <th>Zona / Territorio</th>
          <th>Racha Activa</th>
          <th>Volumen Despachado</th>
          <th>Puntos Acumulados</th>
          <th>Estado Operativo</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Carlos Mendoza</strong></td>
          <td>Barranquilla Norte</td>
          <td><strong>21 Días 🔥</strong></td>
          <td>480 Ton</td>
          <td><span class="font-mono">2,100 PTS</span></td>
          <td><span class="badge-pill badge-green">Casco Activo ⛑️</span></td>
        </tr>
        <tr>
          <td><strong>Jorge Salcedo</strong></td>
          <td>Cartagena / Bolívar</td>
          <td><strong>18 Días 🔥</strong></td>
          <td>420 Ton</td>
          <td><span class="font-mono">1,800 PTS</span></td>
          <td><span class="badge-pill badge-green">Saludable</span></td>
        </tr>
        <tr>
          <td><strong>Andrea Polo</strong></td>
          <td>Soledad / Malambo</td>
          <td><strong>14 Días 🔥</strong></td>
          <td>390 Ton</td>
          <td><span class="font-mono">1,400 PTS</span></td>
          <td><span class="badge-pill badge-amber">1 Ticket Escalado</span></td>
        </tr>
        <tr>
          <td><strong>Ricardo Meza</strong></td>
          <td>Santa Marta / Magd.</td>
          <td><strong>9 Días 🔥</strong></td>
          <td>310 Ton</td>
          <td><span class="font-mono">900 PTS</span></td>
          <td><span class="badge-pill badge-green">Saludable</span></td>
        </tr>
      </tbody>
    </table>

    <div class="section-title" style="margin-top: 6px;">
      <span class="section-title-num">09</span>
      <span>Módulo 6: Billetera de Puntos & Catálogo de Recompensas</span>
    </div>

    <p>
      Incentivos tangibles no salariales vinculados al sostenimiento de rachas (100 PTS por cada día de racha activa a las 11:59 PM):
    </p>

    <div class="grid-3 avoid-break">
      <div class="card card-accent-blue">
        <span class="badge-pill badge-corp">Nivel 7 Días</span>
        <div class="metric-hero" style="font-size: 10pt; margin-top: 2px;">700 Puntos</div>
        <strong style="font-size: 7.2pt; color: #003E78; display: block; margin-top: 2px;">Bono Gasolina + Kit EPPs</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 1px;">
          Bono combustible ($50.000 COP) para vehículo + Kit de protección oficial Ultracem.
        </p>
      </div>

      <div class="card card-accent-yellow">
        <span class="badge-pill badge-yellow">Nivel 14 Días</span>
        <div class="metric-hero" style="font-size: 10pt; margin-top: 2px;">1,400 Puntos</div>
        <strong style="font-size: 7.2pt; color: #003E78; display: block; margin-top: 2px;">Almuerzo Cuadrilla + Merch</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 1px;">
          Bono almuerzo para cuadrilla de obra + Gorra y Termo Don Fraguado VIP.
        </p>
      </div>

      <div class="card card-accent-green">
        <span class="badge-pill badge-green">Nivel 30 Días</span>
        <div class="metric-hero" style="font-size: 10pt; margin-top: 2px;">3,000 Puntos</div>
        <strong style="font-size: 7.2pt; color: #003E78; display: block; margin-top: 2px;">Acelerador + Día Libre</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 1px;">
          +3% comisión en Estructural Max del mes + 1 Día compensatorio remunerado.
        </p>
      </div>
    </div>

    <div class="section-title" style="margin-top: 6px;">
      <span class="section-title-num">10</span>
      <span>Módulo 7: Don Fraguado (Mascota Vectorial & Mentor)</span>
    </div>

    <div class="card card-cement avoid-break">
      <div style="display: flex; gap: 9px; align-items: center;">
        <div style="width: 50px; height: 60px; background: #FFFFFF; border: 2px solid #FDCA02; border-radius: 7px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <svg viewBox="0 0 100 110" style="width: 40px; height: 48px;" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" />
            <path d="M 18,34 L 82,34 Q 88,34 89,43 L 92,90 Q 93,97 84,97 L 16,97 Q 7,97 8,90 L 11,43 Q 12,34 18,34 Z" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="2" />
            <path d="M 10,68 L 90,68 L 91,80 L 9,80 Z" fill="#003E78" />
            <text x="50" y="77" fill="#FFFFFF" font-family="'Outfit', sans-serif" font-weight="900" font-size="7.5" text-anchor="middle">ULTRACEM</text>
            <rect x="35" y="83" width="30" height="6.5" rx="3" fill="#FDCA02" />
            <circle cx="38" cy="52" r="3.5" fill="#0F172A" />
            <circle cx="62" cy="52" r="3.5" fill="#0F172A" />
            <path d="M 44,61 Q 50,66 56,61" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round" />
            <path d="M 20,31 C 20,14 32,8 50,8 C 68,8 80,14 80,31 Z" fill="#FDCA02" />
            <path d="M 12,30 C 22,27 78,27 88,30 C 90,32 86,34 82,34 C 54,36 46,36 18,34 C 14,34 10,32 12,30 Z" fill="#CA8A04" />
          </svg>
        </div>
        <div>
          <h4 style="font-size: 8.2pt; font-weight: 800; color: #003E78;">Don Fraguado: El Bulto de 50 kg con Casco de Ingeniero</h4>
          <p style="font-size: 7pt; color: #334155; margin-top: 1px;">
            Personificación en vector SVG puro del Cemento Gris Estructural Max Ultracem. Actúa como el mentor emocional del asesor en 4 estados:
          </p>
        </div>
      </div>

      <div class="grid-4" style="margin-top: 5px;">
        <div style="background: #FFFFFF; padding: 3px 5px; border-radius: 4px; border: 1px solid #CBD5E1;">
          <strong style="color: #059669; font-size: 6.8pt; display: block;">1. Motivado (Día)</strong>
          <span style="font-size: 6.3pt; color: #4B5563;">Alienta las visitas de la mañana.</span>
        </div>
        <div style="background: #FFFFFF; padding: 3px 5px; border-radius: 4px; border: 1px solid #CBD5E1;">
          <strong style="color: #DC2626; font-size: 6.8pt; display: block;">2. Pánico (10:45 PM)</strong>
          <span style="font-size: 6.3pt; color: #4B5563;">Alerta de corte y pérdida de racha.</span>
        </div>
        <div style="background: #FFFFFF; padding: 3px 5px; border-radius: 4px; border: 1px solid #CBD5E1;">
          <strong style="color: #D97706; font-size: 6.8pt; display: block;">3. Victoria</strong>
          <span style="font-size: 6.3pt; color: #4B5563;">Celebración con confeti (+150 XP).</span>
        </div>
        <div style="background: #FFFFFF; padding: 3px 5px; border-radius: 4px; border: 1px solid #CBD5E1;">
          <strong style="color: #003E78; font-size: 6.8pt; display: block;">4. Criogénico</strong>
          <span style="font-size: 6.3pt; color: #4B5563;">Casco Protector activo por 24h.</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 7: BRANDING, MULTI-SPLIT & ARQUITECTURA TÉCNICA         -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 7 & 8 (BRANDING & ARQUITECTURA)</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">11</span>
      <span>Manual de Identidad Visual: Colores 100% Sólidos Oficiales</span>
    </div>

    <p>
      Estricto cumplimiento del principio neo-brutalista industrial: <strong>prohibición total de degradados CSS</strong> para garantizar máxima legibilidad en obra bajo luz solar directa:
    </p>

    <div class="grid-4 avoid-break">
      <div class="card" style="border-top: 5px solid #003E78;">
        <strong style="color: #003E78; font-size: 7.5pt; display: block;">Azul Ultracem</strong>
        <span class="font-mono" style="font-size: 7.2pt; font-weight: 800; color: #003E78;">#003E78</span>
        <p style="font-size: 6.5pt; color: #64748B; margin-top: 2px;">Primario • Cabeceras, autoridad institucional, botones secundarios.</p>
      </div>

      <div class="card" style="border-top: 5px solid #FDCA02;">
        <strong style="color: #854D0E; font-size: 7.5pt; display: block;">Amarillo Ultracem</strong>
        <span class="font-mono" style="font-size: 7.2pt; font-weight: 800; color: #854D0E;">#FDCA02</span>
        <p style="font-size: 6.5pt; color: #64748B; margin-top: 2px;">Acento • Rachas, cascos, botones de acción primaria y alertas.</p>
      </div>

      <div class="card" style="border-top: 5px solid #0A233F;">
        <strong style="color: #0A233F; font-size: 7.5pt; display: block;">Azul Marino</strong>
        <span class="font-mono" style="font-size: 7.2pt; font-weight: 800; color: #0A233F;">#0A233F</span>
        <p style="font-size: 6.5pt; color: #64748B; margin-top: 2px;">Superficie • Sidebar corporativo y consolas de alto contraste.</p>
      </div>

      <div class="card" style="border-top: 5px solid #F2F1EC; background: #F8FAFC;">
        <strong style="color: #475569; font-size: 7.5pt; display: block;">Gris Cemento</strong>
        <span class="font-mono" style="font-size: 7.2pt; font-weight: 800; color: #475569;">#F2F1EC</span>
        <p style="font-size: 6.5pt; color: #64748B; margin-top: 2px;">Fondo Neutro • Tarjetas de lectura, fichas técnicas y tablas.</p>
      </div>
    </div>

    <div class="sub-title">Tipografía &amp; Sistema de Iconos Vectoriales</div>
    <p style="font-size: 7.4pt;">
      Tipografía institucional: <strong>Outfit / Montserrat</strong> para jerarquía visual y botones; <strong>JetBrains Mono</strong> para valores de resistencia NTC 121, cubicaciones y horas. Iconografía: <strong>100% Lucide SVG</strong> vectoriales con trazo limpio de 2px; cero emojis unicode.
    </p>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">12</span>
      <span>Consola Multi-Split: Pantallas Divididas a Elección</span>
    </div>

    <div class="grid-2 avoid-break">
      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Panel Izquierdo (Módulos Mayores):</strong>
        <ul class="feature-list blue" style="font-size: 7pt;">
          <li><strong>CRM Escritorio:</strong> Pipeline, telemetría y escalamiento.</li>
          <li><strong>PRD Maestro:</strong> Especificaciones técnicas completas.</li>
          <li><strong>Radar &amp; B2B:</strong> Cartografía Leaflet con 12 prospectos.</li>
          <li><strong>Liga de Asesores:</strong> Ranking de toneladas y rachas.</li>
        </ul>
      </div>

      <div class="card card-cement">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Panel Derecho (Módulos Complementarios):</strong>
        <ul class="feature-list blue" style="font-size: 7pt;">
          <li><strong>Celular en Terreno:</strong> Vista táctil del asesor a pie de obra.</li>
          <li><strong>Copiloto IA Lateral:</strong> Asistente para consultas técnicas simultáneas.</li>
          <li><strong>Radar Lateral:</strong> Mapa flotante de apoyo a la negociación.</li>
          <li><strong>Pantalla Única:</strong> Expansión al 100% del módulo seleccionado.</li>
        </ul>
      </div>
    </div>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">13</span>
      <span>Arquitectura de Software & Stack Tecnológico</span>
    </div>

    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>Capa / Componente</th>
          <th>Tecnología Seleccionada</th>
          <th>Función y Justificación de Arquitectura</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Frontend Client SPA</strong></td>
          <td>Tailwind CSS CDN + Vanilla JS Modular</td>
          <td>Carga ultrarrápida (&lt; 150 KB gzip), sin dependencias pesadas de frameworks, óptimo para 4G/3G en obra.</td>
        </tr>
        <tr>
          <td><strong>Micro-Proxy Backend</strong></td>
          <td>Node.js HTTP Server (`server.js` :3000)</td>
          <td>Proxy nativo sin dependencias para canalizar peticiones a NVIDIA NIM y Groq evitando bloqueos CORS.</td>
        </tr>
        <tr>
          <td><strong>Motores Cartográficos</strong></td>
          <td>Leaflet 1.9.4 + ESRI World Street &amp; Imagery</td>
          <td>Zero API Key, disponibilidad garantizada, capas de satélite de alta fidelidad para frentes de obra.</td>
        </tr>
        <tr>
          <td><strong>Persistencia &amp; Estado</strong></td>
          <td>Client-Side Reactive Stores + `localStorage`</td>
          <td>Persistencia desacoplada para `UltraPipelineStore`, `UltraRewardStore`, notas de voz y API keys.</td>
        </tr>
        <tr>
          <td><strong>Despliegue &amp; CI/CD</strong></td>
          <td>GitHub Actions + GitHub Pages</td>
          <td>Despliegue estático automatizado en repo global con verificación continua de endpoints.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- ============================================================== -->
  <!-- PÁGINA 8: USER STORIES, FALLBACK & CERTIFICACIÓN               -->
  <!-- ============================================================== -->
  <div class="page">
    <div class="header-bar">
      <span class="doc-title">UltraRacha CRM • PRD Maestro de Producto</span>
      <span class="doc-version">ULTRACEM S.A.S. | SECCIÓN 9 & 10 (HISTORIAS & APROBACIÓN)</span>
    </div>

    <div class="section-title">
      <span class="section-title-num">14</span>
      <span>Historias de Usuario (User Stories) & Criterios de Aceptación</span>
    </div>

    <table class="data-table avoid-break">
      <thead>
        <tr>
          <th>ID</th>
          <th>Rol</th>
          <th>Historia de Usuario (User Story)</th>
          <th>Criterio de Aceptación (Gherkin Sintético)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>US-01</strong></td>
          <td>Asesor</td>
          <td>Visualizar semáforo de riesgo por canal y cuenta regresiva a medianoche.</td>
          <td><strong>Dado</strong> que es jornada laboral, <strong>cuando</strong> abre la app, <strong>ve</strong> racha activa, tiempo a 11:59 PM y cuentas rojas.</td>
        </tr>
        <tr>
          <td><strong>US-02</strong></td>
          <td>Asesor</td>
          <td>Escalar caso a Cartera/Logística cuando la venta esté bloqueada.</td>
          <td><strong>Dado</strong> un pedido trabado, <strong>cuando</strong> pulsa "Escalar a Cartera", <strong>se asigna</strong> SLA y racha sube +1 día.</td>
        </tr>
        <tr>
          <td><strong>US-03</strong></td>
          <td>Asesor</td>
          <td>Consultar dosificación NTC 121 y generar minutas técnicas con IA.</td>
          <td><strong>Dado</strong> un requerimiento de obra, <strong>cuando</strong> consulta 3000 PSI, <strong>la IA</strong> responde en &lt; 500 ms con datos oficiales.</td>
        </tr>
        <tr>
          <td><strong>US-04</strong></td>
          <td>Asesor</td>
          <td>Grabar nota de voz en obra con transcripción automática por Whisper.</td>
          <td><strong>Dado</strong> ambiente ruidoso, <strong>cuando</strong> graba 20s, <strong>Whisper</strong> extrae toneladas y tipo de cemento a texto.</td>
        </tr>
        <tr>
          <td><strong>US-05</strong></td>
          <td>Supervisor</td>
          <td>Auditar embudo de toneladas, ranking de rachas y SLAs represados.</td>
          <td><strong>Dado</strong> acceso al dashboard, <strong>cuando</strong> filtra por asesor, <strong>ve</strong> volumen, OTD Galapa y tickets abiertos.</td>
        </tr>
        <tr>
          <td><strong>US-06</strong></td>
          <td>Asesor</td>
          <td>Redimir recompensas comerciales con puntos de racha acumulados.</td>
          <td><strong>Dado</strong> saldo de 700 pts, <strong>cuando</strong> redime bono gasolina, <strong>el saldo</strong> se descuenta y se emite voucher.</td>
        </tr>
      </tbody>
    </table>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">15</span>
      <span>Matriz de Resiliencia & Plan de Fallback Operativo</span>
    </div>

    <div class="grid-2 avoid-break">
      <div class="card card-accent-blue">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Falla en Modelos de Lenguaje (LLM):</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 2px;">
          Despliegue inmediato de <strong>Chips de Registro Rápido en 1 Clic</strong> (*"Cliente en fundida"*, *"Pide cotización"*).
        </p>
      </div>

      <div class="card card-accent-yellow">
        <strong style="color: #003E78; font-size: 7.4pt; display: block;">Falla en RAG de Fichas Técnicas:</strong>
        <p style="font-size: 6.8pt; color: #4B5563; margin-top: 2px;">
          Activación de visor offline con las fichas técnicas en PDF embebido para consulta sin internet en obra.
        </p>
      </div>
    </div>

    <div class="section-title" style="margin-top: 8px;">
      <span class="section-title-num">16</span>
      <span>Certificación Formal & Firmas de Aprobación</span>
    </div>

    <div class="card card-cement avoid-break">
      <p style="font-size: 7.1pt; color: #1E293B;">
        El presente Documento de Requisitos de Producto (PRD v2.0) ha sido revisado y validado en todas sus dimensiones funcionales, operativas, de marca y de seguridad, autorizando su operación en la fuerza de ventas de <strong>Ultracem S.A.S.</strong>
      </p>

      <div class="grid-3" style="margin-top: 8px;">
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 6px; padding: 6px 8px; text-align: center;">
          <div style="font-size: 6.8pt; font-weight: 700; color: #64748B;">DIRECCIÓN COMERCIAL</div>
          <div style="font-size: 7.4pt; font-weight: 900; color: #003E78; margin-top: 12px; border-top: 1px solid #94A3B8; padding-top: 3px;">Vanesa Peñaranda</div>
          <div style="font-size: 6.2pt; color: #64748B;">Gerencia Regional Caribe</div>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 6px; padding: 6px 8px; text-align: center;">
          <div style="font-size: 6.8pt; font-weight: 700; color: #64748B;">OPERACIONES &amp; PLANTA</div>
          <div style="font-size: 7.4pt; font-weight: 900; color: #003E78; margin-top: 12px; border-top: 1px solid #94A3B8; padding-top: 3px;">Ing. Jefe de Despachos</div>
          <div style="font-size: 6.2pt; color: #64748B;">Planta Galapa (Atlántico)</div>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 6px; padding: 6px 8px; text-align: center;">
          <div style="font-size: 6.8pt; font-weight: 700; color: #64748B;">ARQUITECTURA &amp; SOFTWARE</div>
          <div style="font-size: 7.4pt; font-weight: 900; color: #003E78; margin-top: 12px; border-top: 1px solid #94A3B8; padding-top: 3px;">Equipo de Ingeniería</div>
          <div style="font-size: 6.2pt; color: #64748B;">Semillero by CooWeb</div>
        </div>
      </div>
    </div>
  </div>

</body>
</html>
"""
    return html

def main():
    print("Iniciando generación del PRD en PDF...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(script_dir, ".."))
    
    html_content = build_prd_html()
    temp_html_path = os.path.join(project_dir, "temp_prd_export.html")
    temp_pdf_path = os.path.join(project_dir, "temp_raw_prd.pdf")
    final_pdf_path = os.path.join(project_dir, "PRD_UltraRacha_Ultracem.pdf")
    
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML temporal guardado en: {temp_html_path}")
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    file_url = "file:///" + temp_html_path.replace("\\", "/")
    
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={temp_pdf_path}",
        file_url
    ]
    
    print("Compilando HTML a PDF con Microsoft Edge Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error ejecutando Edge: {res.stderr}")
        return False
        
    if not os.path.exists(temp_pdf_path):
        print("Error: No se encontró el PDF temporal generado.")
        return False
        
    print(f"PDF temporal generado exitosamente ({os.path.getsize(temp_pdf_path)} bytes).")
    
    # Post-procesamiento con PyMuPDF: agregar numeración y membrete de pie de página
    print("Aplicando membretes y paginación ejecutiva con PyMuPDF...")
    doc = fitz.open(temp_pdf_path)
    total_pages = len(doc)
    print(f"Total de páginas detectadas: {total_pages}")
    
    for page_num in range(total_pages):
        page = doc[page_num]
        rect = page.rect
        
        # En la portada (página 0) no se coloca pie de página
        if page_num > 0:
            footer_left = "Ultracem S.A.S. • Planta Galapa (Atlántico) | PRD Maestro: UltraRacha CRM v2.0"
            footer_right = f"Página {page_num + 1} de {total_pages}"
            
            # Línea sutil superior de pie de página
            page.draw_line(
                p1=(rect.x0 + 35, rect.height - 24),
                p2=(rect.width - 35, rect.height - 24),
                color=(0.82, 0.85, 0.88),
                width=0.75
            )
            
            # Texto izquierdo
            page.insert_text(
                point=(rect.x0 + 35, rect.height - 14),
                text=footer_left,
                fontsize=7,
                color=(0.3, 0.35, 0.45)
            )
            
            # Texto derecho
            page.insert_text(
                point=(rect.width - 95, rect.height - 14),
                text=footer_right,
                fontsize=7,
                color=(0.3, 0.35, 0.45)
            )
            
    doc.save(final_pdf_path)
    doc.close()
    
    # Limpieza de temporales
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
        
    print(f"\n¡ÉXITO! Documento PDF generado en:\n{final_pdf_path}")
    print(f"Tamaño final: {os.path.getsize(final_pdf_path):,} bytes | Páginas: {total_pages}")
    return True

if __name__ == "__main__":
    main()
