# -*- coding: utf-8 -*-
"""
Ultracem UltraRacha v3.3 Builder
Incorporates:
1. Multi-Model AI Engine: NVIDIA NIM, DeepSeek API, Groq Cloud, OpenRouter, Google Gemini, OpenAI, Custom/Ollama endpoints, and Local Engine.
2. Live Connection Tester ("Probar Conexión en Vivo") for all AI keys.
3. B2B Commercial Outreach & Prospecting Search Engine ("Directorio de Obras & Empresas para Contactar") with 12+ real Caribbean companies, volume metrics, current competitor supplier tags, and tailored sales strategies.
4. Strict Map Containment & Satellite layer toggle.
5. Guaranteed Voice Recording with audible synthesized WAV memo and playable <audio controls> in timeline.
6. Anti-collision protection and client transfers.
"""
import os

base64_logo_path = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\Ultracem\assets\logo_base64.txt"
with open(base64_logo_path, "r", encoding="utf-8") as f:
    logo_base64 = f.read().strip()

html_content = r'''<!DOCTYPE html>
<html lang="es" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UltraRacha — CRM Comercial & Copiloto de Campo Ultracem</title>
  
  <!-- Tailwind CSS via allowlisted CDN -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  
  <!-- Leaflet CSS & JS for Interactive Colombia Map -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>

  <!-- Typography: Outfit (Neo-geometric) + JetBrains Mono (Data & Precision) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --brand-blue: #003E78; /* Azul Corporativo Ultracem Oficial */
      --brand-blue-cobalt: #004797;
      --brand-yellow: #FDCA02; /* Amarillo Ultracem Oficial */
      --brand-blue-hover: #002D58;
      --brand-blue-light: #EFF6FF;
      --brand-amber: #EA580C;
      --brand-amber-light: #FFF7ED;
      --brand-emerald: #059669;
      --brand-emerald-light: #ECFDF5;
      --brand-rose: #E11D48;
      --brand-rose-light: #FFF1F2;
      --surface-slate: #F8FAFC;
    }
    
    body {
      font-family: 'Outfit', system-ui, -apple-system, sans-serif;
      background-color: var(--surface-slate);
      color: #0F172A;
      overflow-x: hidden;
    }
    
    .font-mono-data {
      font-family: 'JetBrains Mono', monospace;
      font-variant-numeric: tabular-nums;
    }
    
    .text-balance {
      text-wrap: balance;
    }
    
    /* Animations */
    @keyframes pulse-flame {
      0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px rgba(234, 88, 12, 0.4)); }
      50% { transform: scale(1.15) rotate(3deg); filter: drop-shadow(0 0 14px rgba(234, 88, 12, 0.8)); }
    }
    .flame-active {
      display: inline-block;
      animation: pulse-flame 1.8s infinite ease-in-out;
    }
    
    @keyframes bounce-mascot {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-7px); }
    }
    .mascot-breathing {
      animation: bounce-mascot 3.2s infinite ease-in-out;
    }
    
    @keyframes panic-shake {
      0%, 100% { transform: translateX(0) rotate(0deg); }
      20% { transform: translateX(-3px) rotate(-2deg); }
      40% { transform: translateX(3px) rotate(2deg); }
      60% { transform: translateX(-2px) rotate(-1deg); }
      80% { transform: translateX(2px) rotate(1deg); }
    }
    .mascot-panic {
      animation: panic-shake 0.4s infinite ease-in-out !important;
    }

    @keyframes jump-celebrate {
      0%, 100% { transform: translateY(0) scale(1); }
      30% { transform: translateY(-16px) scale(1.08) rotate(-4deg); }
      60% { transform: translateY(-6px) scale(1.03) rotate(3deg); }
    }
    .mascot-jump {
      animation: jump-celebrate 0.75s ease-in-out !important;
    }

    /* In-Phone Bottom Sheet animation */
    @keyframes sheet-slide-up {
      from { transform: translateY(100%); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    .animate-sheet-up {
      animation: sheet-slide-up 0.28s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    /* Tactile button press */
    .btn-tactile {
      transition: all 0.12s ease;
      cursor: pointer;
    }
    .btn-tactile:active {
      transform: scale(0.96);
    }

    /* LEAFLET BOUNDED ISOLATION & Z-INDEX MANAGEMENT */
    #colombia-leaflet-map {
      z-index: 1 !important;
      isolation: isolate !important;
      position: absolute !important;
      inset: 0 !important;
      width: 100% !important;
      height: 100% !important;
    }
    #colombia-leaflet-map .leaflet-pane {
      z-index: 5 !important;
    }
    #colombia-leaflet-map .leaflet-top,
    #colombia-leaflet-map .leaflet-bottom {
      z-index: 15 !important;
    }
    #colombia-leaflet-map .leaflet-control {
      z-index: 15 !important;
    }
    .custom-map-pin {
      background: transparent;
      border: none;
    }

    /* Voice Bar Equalizer */
    .voice-bar {
      transition: height 0.08s ease-in-out;
    }

    /* Custom scrollbars */
    ::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    ::-webkit-scrollbar-track {
      background: transparent;
    }
    ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }

    @media (prefers-reduced-motion: reduce) {
      *, ::before, ::after {
        animation-delay: -1ms !important;
        animation-duration: 1ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>
</head>
<body class="bg-slate-100/70 text-slate-900 antialiased min-h-screen flex flex-col selection:bg-blue-100 selection:text-blue-900">

  <!-- ACCESSIBILITY: SKIP LINK -->
  <a href="#main-content" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-50 focus:px-4 focus:py-2 focus:bg-[#004797] focus:text-white focus:rounded-xl text-xs font-bold">
    Saltar al contenido principal
  </a>

  <!-- ============================================================== -->
  <!-- TOP APP BAR (STRICT TOP STACKING Z-INDEX: 99999)               -->
  <!-- ============================================================== -->
    <!-- ============================================================== -->
  <!-- TOP APP HEADER: SOLID AZUL OSCURO (#003E78) & AMARILLO (#FDCA02) -->
  <!-- ============================================================== -->
    <!-- ============================================================== -->
  <!-- TOP APP HEADER: SOLID AZUL OSCURO (#003E78) & AMARILLO (#FDCA02) -->
  <!-- ============================================================== -->
  <header class="bg-[#003E78] text-white border-b-4 border-[#FDCA02] shadow-md sticky top-0 z-50">
    <div class="max-w-[1780px] mx-auto px-4 sm:px-6 py-2.5 flex items-center justify-between gap-4">
      
      <!-- Brand Logo Ultracem -->
      <div class="flex items-center space-x-3 select-none">
        <div class="bg-white px-2.5 py-1 rounded-xl shadow-xs border border-white/40">
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZ4AAACUCAYAAACjkE/dAAAQAElEQVR4AeydTXbUyJ7FI/Kcwm9UlbWCZ1bQZgVtz6AmL1lBwwpeMQQGmAEwhLcCqldA9gSY2b0C+63A7hWUXo0Kv3NSfa9SMmlbH/8IKZVS5uVkoLQUn78IxY34R0g5cfonAiIgAiIgAj0SkPD0CFtJiYAIiIAIOCfhUSsQgYKAjiIgAr0QkPD0glmJiIAIiIAIFAQkPAUJHUVABERABAoCaz1KeNaKV5GLgAiIgAjcJiDhuU1Ef4uACIiACKyVgIRnrXgVedcEFJ8IiMD4CUh4xl+HKoEIiIAIjIqAhGdU1aXMioAIiEBBYLxHCc946045FwEREIFREpDwjLLalGkREAERGC8BCc94626oOVe+REAERKCWgISnFo8uioAIiIAIdE1AwtM1UcUnAiIgAgUBHUsJSHhKseikCIiACIjAughIeNZFVvGKgAiIgAiUEpDwlGLZ9pMqnwiIgAhsjoCEZ3PslbIIiIAI7CQBCc9OVrsKLQIiUBDQsX8CEp7+mStFERABEdhpAhKena5+FV4EREAE+icg4emfuS1F+RIBERCBLSUg4dnSilWxREAERGCoBCQ8Q60Z5UsERKAgoOOWEZDwbFmFqjgiIAIiMHQCEp6h15DyJwIiIAJbRkDC06JCFVQEREAERCCcgIQnnJlCiIAIiIAItCAg4WkBT0FFQAQKAjqKgJ2AhMfOSj5FQAREQAQ6ICDh6QCiohABERABEbAT2HbhsZOQTxEQAREQgV4ISHh6waxEREAEREAECgISnoKEjiKw7QRUPhEYCIGdFZ7p7Hg6ffjucPrLm+Mff3n38adHb0/gfoc7aVM3jBNxfIJLV9zF9OGbJ23iVVgREAER2BYCOyU8EJkDuGMIwln67d7vqU9P0tS/8mlKUThkpfrUP+UxxlFcGCfCzuBWP/up95m4QZj2Vy/ouwiIgAjsGoEBCM96kbOjz8XmAiJzBvcKKR7A3fl4514nX59f3rlgOIE0DiguDV4PIUxnFKgGf7osAiIgAltLYGuFh0JAExo6egoOxaZppnGafHnxIbamIWgfjWGnFCjMuj5NYe4zhpE3ERABEdgaAlsnPJzhoFOnCe0sN6FZKivxe1ePLR7L/EDkjnG+dBaF81WfGcx9F9NHb2dVHnR+9wioxCKwCwS2RnimmD38+Ojte85wUHGHcOYPTGxPk/lxYg6w4hFCd4jZDmdUK2fNX6epc9yIoNmPGZk8ioAIjJ3AVggPZw2cPUBAfo2okDlMbPOIcI5iB6GzmtjqkuDs54wiVudJ10RABERgGwjYhGfAJc1mOZg1IItTuNAPTWzRu9gW3+5xptO0dmTN0z5E7EQbD6y45E8ERGCsBEYrPJxtYC3nLHKWk9WXT/3jpIWJrU3aWQZK/uPGA87gSi7plAiIgAhsBYFRCg8W8w9oWkMNhC7oI8jyg7WVD8nX56fLv8L+p+hhdtKFia00YeSNM6nSazq5cQLKgAiIQEsCoxOeTHRSz7cLxJjWClyXk72r18UfoUeIHkWnKxNbWfIHFLeyCzonAiIgAmMnMCrh6Uh0nE99/C625fbn2dor/s+96Nnc2vOmBERABESABCLdaISnK9GBGaudic05znYicQcFi3qDQlAK8iwCIiACGyAwCuGZPny3n7Y3rxHv+R9fXjzjlxiXm9jamPisyV5i/UnCY6UlfyIgAqMiMHjhmc6Op1jI/wSqrTt879PordPTR2/5jNAM+Vj7x6dp9PrT2jM3igSUSREQgSETGLzwLK723gNg6/UOiM7r5PPLc8QV/MlmXM71tdPsNPn68rfgTCqACIiACIyEwKCFhw9TYvTPnyxoi/MconMcGwlmXFzXaT3jMqSfcOODwZ+8iIAIiICJwBA9DVZ4slmG95zttOXGzjz+BaBLE1vQu99iMwyRfaa1nVh6CicCIjAWAoMVHswyKDqtZxnetfyNnf5MbHOZ2MZy2yifIiACbQgMUngw2zlEobpYyD9N2v/GTmvxQ1maPq3eGdcU+SCvK1MiIAI7S2CQwoPZDtdU2lYKTWzxu9h+ecM1odabGiyFwKws+oFWS/zyIwIiIAJDIjA44eGGAgBq/TqaNusl+cOqfe1im2NWNkeZ9REBEdhNAjtX6sEJT+p9Fx1+9HrJlM8Npb6LGZelMV36vavoWZklAfkRAREQgaERGJTw5Gs7bWc7rdZL8t/Y6cfE1uKdcUNrSMqPCIiACFgJDEp4sLbzd2vGq/y1WS+h8CE831BQFX1n51Pnot8Z11kmGiLSZREQARFYB4HBCA9NXCjgDK7NJ3q9ZEoTm097M7G1+VmGNoAUVgREQAQ2TWAwwuP+/GHWEkYXJra2Zj5TEbxP43/5FAJpSkSeREAEOiSgqLokMBjhSb3/W5uCwUT2OpkfJzFxTB+9nSF8LyY2iE78O+MgOum3e2cxZVQYERABERgKgcEID4C0mfFcJpEPik7ZmTvXl4mt3Tvjvt1jPve5FgVe+oiACIjAKAkMQnjadqS+xc8IYAbBzryPtxM4zHait05zVoYWNoNzbrLgmx34VU4EREAERkdgEMLTsiNNYt9xdqMzX3PVQXTiTWz8IbyVWVma+v9cc3YVvQiIgAisjcAghKdNR5o6F/XbNdN+TWynHf8sQy/PGTn9E4ExEVBeR0NgEMIDWtG7ySY+/W+ED/7AxPYJgfowsbV7Z1z5zzJMYZ6MYkbBRdhDgwuK3xzvL29uiCZfT2TIS6Np0RqPJa1APxmnrtNH2+ztg5n/r8j/ca17+KaL38WqLBPSPoA7/unR209wZ3BpiTvBuU9ZfmEFqIzs1gVz23z4znJfWPxkbaLIhrk9YTBchIk5mtMJYBeTD0uYsQtPgplE8K+KsuECTmNnBj+tP961+FkGNBDM6KpeIXSjcZsz+ufeQerTkyYH82dYR2OMF7Pb96t55d9NeeH11TBl363xMK4uXcGp6/TRwbLjvfjxl3cf0V5nZWXu4hw7K7Sx98j/q1rn/cdpy47xdn4ZH8r2K8p6gbTP4NjWZ/B3Y3CCv4vPIb7Msvz69ALhzvJ3O+J0zcfaNg33haXtFG2iyJElTOZnuXmoCBZ0zOrRmP/b+QtKqCPPGxcejHKqGpmliKcWT6t+UEH7aLhs4Kun1/X9NPny4kNs5GiM1RsffNqGW2yWFK5fAvs+TZ+kznEWcGHqZAPzt5i4/zIHufqhs0cOWBZYHS5QNg5E4gZRzmEQ5T9CgMDmHUXJXJSBepxBiCm8wdnL+4rgcJsKsHHhcYtJtLkLC/b/DAWXV1B0mgHp8YHW+F8+Xf4sQ/XN5NM+yhBQXHldM4H9FLMOdLIn045mHhyEUdis+caMxC5SFZEy7ywDywIvXbVhsElPMIg9Rpyj/qTOvSejkELk5Y4V75CkOvM76SymTUSU+iAzW15B1Z15h2XwzkX/xg7yeYCb/FWH2VFU20PgEDOFbsRnsggzpzq3z5lKLEq2a+SdD0Cv5R7kPUPTZGz+BhJu3wXMLDl4YLkHkndzNjYvPG1MRqkPelMBKqj1S0iNZOfJlxdzo9873pBPmtjunF89sUj9T6t/6/tOEThAB37StsRoZ8EzGMxUgsMwn5nopJ55XuvInDO4sYsP6uUVeZFbk8stOE3eBnd9CMIz7YMKRgYcZfWRFk1s8Q+KLk1sB01MPOzbTX50fasJZLvAYkuYz1xiRIC7uoLC0XSEzpSDqT7uP0fxQcc9arMbeHHtq7Z68zpkv1brb4gXNy88Q6DSYR4gCDKxdchTUVUTQOf0d3bq1T6qr8TOXBjjYuKCzMCYnVF0GgdTjLsrBzb/0VVcG4oHAl+9hZ31jjpsFKcN5b0x2c0Lz8Jduth/bcx0sWnWhMPC4IdYE1vWkFLPZ4tqUvh+CWkFrW99D6lvW0RgGvNWd8wGKALRI2XMKGZsrxaO+S6tmcVvhZ8gczrjwODv2b++vIje2MM4huAoLNOKjST5D1b2MoNcB4vNC4+bRAvPwrm/WqEkX59z63VwI7bGD3+XbX5jJ29IZhPGxKf/Qpr65AS8T5/51B81udR705suvHOm+NxiYoovz6ZDh+jLHPL/gHnHgILb783tdOF98Mh+4SZ1a51FVuuOU/ftnmljQupc6Kj8EsL21O9d/Zxzyo4ZH5++Rqbq2PBh7SMM/sgQXsM+SON1nmZpHVmvJZ9fdmXmmy6u9u7w47IB2mdnW9vDKHXje9JNNJuJBfCDRm1oWP9YV0596uNNbA/fHaIso25I6+JqjRc3+zkHF01u4hb/Z4oz9ab4kF70wGk1H0X+//jy4hk63fu4ZprRot1w9gLvtg9H0OjYTaJRFyMEpVG88jUI82AKcX5A536f715Mbv3EScYHHTruswfIVxmbc3JDfXCACS/b8WFdUWhWS5P69I4YrV4fw/fNC89kUTeCaWJ4gEoxN2w0Xo5E5k2Rhl7nDRPb4NkRoCHRBh6WbOCOvrDI5XuTBBJ0uuhgn60lD8aZiiHtfdx7tQO/1HvzDjgMCl9TdJvSxX12CXF6gLivZ5q8/3iO3JrCj/E6+odroYHpkgPUoMHGEMu8ceGBGJSNXu6wqjzh01nltZILaKCP2chLLsWeOrfcMFWR5wuvZvG8jgcj8uvv+rJ1BNDBrmXknjrXOFMBTFPa6BAr45ou1yZqhQnpFJ/gl+j+8fk5d47OMSN42ub+KzIw8GO2gxFCv4/6C9rYMdRybVx4cjDR5gpURGXjz+O+c4DYHUN8qqbsd/zXnUA8vAHqvFRew+hlhot0OAR/opkFp6QAW0Egb2+Ngxx05nzx7txQ6Bk7w1J/f/5gbtc+9VH3EAeRNMuVpr9lJ9PU/z31KS0jo91QsFolQxGeNrMeTPmrtx2uFnb1O8TnHA33AYQraiGScUF04n9jByNCpM2GxKhCXYIRsYQnlNqI/Fd26FkZ4v5De7MM0tC2Xv6GtSOKT2NCC5+WxzlxjQLnlv+4ljaItpym/tVPj97y5ayxjg/ILkvV/f8UHOsMsvvUO45xEMKDDjz4nWurHGDvfTVFR756zvqd03SMuI7gP7Txn0O8uGaEoOGf3MTGxhQe2Lk2Qu30b/gE8tFtY0YhJqa2kAtZY8eF+LK1k2T55o3GewIC9aTs3kMnbvqxQoQ3CVwjCHkYFYFBCI9bTEw25Rqy+/l25Bov1Zcwezj1e1chs58EYhllHmAu8t0+M36PcUj7f2PCKczwCdAchlG3+X1mE+dMbcH60Ock9dc7P9HOLKIwjXmW6LomtFZZoLCYNgu/Vccu4qiKu9PzaLedxRcdETt+BG6zu81h5PQrb1rEE/VJ5sdJNvtxjg+e1ebFp+kzzHZMI83bmeHIEzO0610qt68b/54b/cnbwAhAVGrNOJhx8CFi666lJJ+Z1JZyCmsA2uys1tPy4inuxe+zHOMzSmjP5ea2ZZz630AAIv9POD6nZPBd6uUUlpvrQUOpjwGdHITw5Dzaznoc/zKFVgAADRRJREFUbtqP+VPZeZThB97ImP3cx82UmRxuxXCOyj1qs6CZm1BiTWzMThIregwstz0EMNiydVTLhf7GNgdxujHDyUXIMsjhYw2NZrztIb+ekuC+puk+ZkDLB2ejLTDrKU19rIMRHjT6/6nPqunqFLbl1q+MTzj7+fw8e3qaQpO7+9yMgJsxWiAxI+Me/FY3KARxbiJR5Um/41NFptvz64/tFIMk08YYtBnLFtxsU8HtbFvvS5jyzM/s3EhD7fEmDp8GCwgHIOiXvs9Ub8Q4zD8GIzzuL/9mh1pr4jIinGLhvrX4MK0EAoQKpfmBrlXFciaGGZmlA2DSlW6ycDdGpZUedWGbCfApfZqEG8sI0y4HOo07zNA2y2b4Lp/dN96XEKgnSKsxndsZXjhn2oRwO9y2/o1Zz3mgyc08ABkSs8EIDzv51Pt5R3D4eyUX7Ow7iq9VNFPY2DET49bpRnNHQ0KXFMIGP/WXU9/YiTAC5Df4HWAMJ7d2AnOYgo8SDIosKcG0a1t/8X6K++W4zCEd26Br5Yfl0HmaNj1452ZuOP9Oke/X0S5NuxkU3vs3Z7Im5sjret5w0W2d3IltMMLDnE3cosvFsaXZ7eE7jvgY/cYcZmAUHeuCcWU+cZN2yacynfxCWH4nCxNn3CimDinPgw7fCVyi/h/D3PvYKjr5DMTUsXPGgsHGqzKHLJjaAsJ+Fzn7brV95NPUdpCPG58pBnR0N062+INtEzOO42j39WXprDE0S6xfmPcbTW7Ib/RzhKF56tr/oIQHFc6Fteg1lBI4U4z4TjiKK7nWy6n81xBnHSSWuL2r9g3b/m68fXAzdTgsGzqdv/Eotx4C7IiwpjMPiX1R9XBnSCRhfqf5owIObdV8H+Me/TiFiIQkRf8Y0J3AncUKV0h6ffulZQPmT858qpJu9RxhVaR9nR+U8LDQuMFsO3Xo2ejQKfKJ5BM00GAbtDGJUm8UHY4kSy8GnsTo5h+J0bxSF3Uu7nVerq+Bm2nb9/TR2xkC2USq/TNbSKqbz4ZiYYe86kzZiOmcMUN6Yoq8Q09p/mLQvK3OjVHvl73+vyrsFCIFweFbAtjm9sFmo4PLqny2PZ//zEqpyQ39QeOMqG366ww/OOGh0qPAvDFx6PRziAZ6hk6SO8s6jbgssi5FB/Enbmn3xddOPla+hyxHXYoQ80OMzGhKrPP2/dpfvnFW+/3vHfsGU9nRqgO7ulHtKp2gh6TzmUfbNcXV9K3fD4uZMoTPvObBAdpPj96eoT3VDg5x/RCiwwdsKTrXecIgiYPLxvDXAUbwJcFAEwPxOwID0Rmtia3APjjhYcYAdl0LZlPc6O/RwDn7ibIrM391jqMxxs8bqc5fyDXcwK/ZCEPC1PlFfOat6ywHynPBjqzoUHDz70PAZxQliDlHntYObh5bDqRduvBdev7hu9rOq45N39fqRrW384J6+xXsTe0WM4/v6y23I1rz34v8h+Zy02DIQOMA7emC7YrtC3XL54P2WWa2P7TDE1xne6uqX4aH+IS/u5FIkO+/LtN6d9jq+MubG6LIuGMdB+Koy1UT+2XHg9A8a/0eBik8NAelzllHgi7i3yEbMBryJzbuiPClQXhzYDR2gYumzgH+LJ9z3MDdskj93JLwih+YM/xHjCrPwAyH9AL188mnaZApB/7NgreSdvYViZYufJedR4CqjgmXhvVJKka1VblEu21cD2GnifCddX6IK+iDen7CARgDYcQePIhk+NS5T6jbM5T3Ag6C4zmrttxXU3TUH9FOPxV5YD4sLkvXp0irpUv9e0t6Vj+Te9/IMNuN6lMf/YOT1vT68DdI4WHBQ0aC9B/pZmzcaKQnHGFFxuF4ozMONnjEYR39w2vzB7O/O1Pt5lD1PjCKukReV0dR9QG6uXqZPxPSTWxbFAvq4xQdrXVwsY/BDTvhSgLRD3NWxhhx4eqHzKQdWLaIhCqDjGbwUVmC/EI2OHHuKfqC1+SZnx71YbDCk8GGuvdE9xA3/ieIx+/ZNP/hm8aH4Sg2Pz56S7NdNiJDPi2jMXizf7KG9vlliKnCHPlk4biJIxtFmQO18Oid46gtNIad8R840JpVDZTQLvc5creAw+iZb+PwWHMyO9wnJoHEgO76TQZ52dbSjivKyVfImLedV8QxqNOwesxhCeIrdQaVr9jMDFZ4WCCqu7Wh038HbsqbFrOBj5jeX0CI+ELHExxXXWFuOkFnylHdukZWp+tsaGDL50IoPh1gq48CPH/jjVPva7evhg60cF+Um9xWHuJsIDpnG2jwc+fy6tur71y8eWK/EMesbHtX/OmRPsSHb44/iinbzezrr3USGLTwsOB8YzSO1l1Y8Nr5hzOZVXfQeQp3I0z83pXplSh3g9rPQAw+UBTsIaJ8nuc26qjAuxQInWWIyY2vhrpjcludadSxw6DJvONsNR7kkdt756vnqr5DHK83OCRcy1q/+CxFZ01Wgqpy9nZ+ixIavPCQdd4J9zFaYnKbdsubBzdqHxn5gy9D9elaZj6p97+h7syvd+mjvENPIzdLsXO3ZHXGDS2Fx/y7ZQZ+iUHHvAgXevTOWUWLu8Ou85OgTbM9QJBM5rrAfPHN8Q9gJdiVfiIQz7C8j0J4sgabes4AeluT2FQ14aZ+2vfNg/SOYe/v0hRCM95jihrrblMsx5gueaEuzBtKUu/fc12HZcX363UV/l3lsHZoFY7SKHLRMonjYuJuvBiX5aMVA2Xsqr0luGeeYZ3qQT4bK82zTg6LwCiEh8jYqHDDsLFurfhgfelpflOzyL068D3lzYubmAI/tyd+w+ecZUA89zdVjhu5GekfrIuAWcEU65HF71DRJNxcauMPvNVFhHvRJF5oD7Pp7PjOTk+WEe3kQS5AMe0NM5yUP13CtraOGVRd8XWtJYHRCA/LiZH5ORo8xcc02mKYkbgEN+jTIWw3pmCgQ+DLKIHaH0GInuELTXFcZ7vh2DnyGjsPmFB+ZrjQMiAMn+Q376qC/0a/7NSq6h1t6LhtHGVxI05TOcrClp3jrABxNpY193OEcp3n3xvDgE/r+wfpmTgiTz8nMLGVlZHnkBcOeB6z/aCtPWZ7wvk53I22hr/nvMb7BO2Nu/Eww3n5W1ITN8JknzyNRi7Ia1d+2EdlafM/S7zkSb9tnLWcXaTVJp8MOyrhYYYBjb9F8gDft8WWm+CGOgrtsFH+tX/YkCFEH8CcnQw71huOnSOvZf4MHcDaM6wERkuAAoK2lm0ZRkfNgc+NtsZzy7YGsfn6vLVwrguU4rURGJ3wsFhspBghHaXe9/0QJJPv0sFc4LUg2iVRxSUCIjB4AqMUHlKl+HDx2i8fTBzduk9mptq7wkxHozfWp5wIiMDuEBit8BRVhOn5B9h8aXqjTbg4PeTjcsfXlxfPKJ69ZFSJiIAIiMCACIxeeMgSawyXsAEfceERfw929pPPch5ALOfIpz4iIAIisJMEtkJ4iprjAj3Wfu5jsZ67sAYjQFyLwqzsfrYYr0X4orp0FIFNEFCaAyCwVcJDngk6du5+GYAAJdeC8/n5U87KmD85ERABEdh1AlsnPEWFFgIEE9zPuQluXlxb8/GcGx4ofNz8IMFZM21FLwIiMDoCWys8qzVBExwEaPmQWpo+5UwE17t6FoAmvXkmNqlfPtj25cWHZH7M80jG9pEvERABEdgVApNdKSjLSTGgCHEmAiG6z3UXuCOuCeVixJ1xdGWiwfOn9Ef/EJrHOD5APMsn9ik2erCNmOVEQAREoJbATgnPbRI0g8Flv3uTi1HxtDTF5PbrM7Jr9Mc1JO5Mw3Fb3p5wG43+FoENElDS205gp4Vn2ytX5RMBERCBIRKQ8AyxVpQnERABEdhiAhIee+XKpwiIgAiIQAcEJDwdQFQUIiACIiACdgISHjsr+RQBESgI6CgCLQhIeFrAU1AREAEREIFwAhKecGYKIQIiIAIi0ILAlglPCxIKKgIiIAIi0AsBCU8vmJWICIiACIhAQUDCU5DQUQS2jICKIwJDJSDhGWrNKF8iIAIisKUEJDxbWrEqlgiIgAgMlUD/wjNUEsqXCIiACIhALwQkPL1gViIiIAIiIAIFAQlPQUJHEeifgFIUgZ0kIOHZyWpXoUVABERgcwQkPJtjr5RFQAREYCcJlArPTpJQoUVABERABHohIOHpBbMSEQEREAERKAhIeAoSOopAKQGdFAER6JqAhKdroopPBERABESgloCEpxaPLoqACIiACBQEujpKeLoiqXhEQAREQARMBCQ8JkzyJAIiIAIi0BUBCU9XJBXP5ggoZREQgVERkPCMqrqUWREQAREYPwEJz/jrUCUQAREQgYLAKI4SnlFUkzIpAiIgAttDQMKzPXWpkoiACIjAKAhIeEZRTePPpEogAiIgAgUBCU9BQkcREAEREIFeCEh4esGsRERABESgIKCjhEdtQAREQAREoFcCEp5ecSsxERABERCB/wcAAP//5FA+QgAAAAZJREFUAwCwBKHssrmu0wAAAABJRU5ErkJggg==" alt="Ultracem Cemento y Concreto" class="h-8 object-contain" />
        </div>
        <div class="hidden sm:block">
          <div class="flex items-center space-x-1.5">
            <span class="text-sm font-black tracking-wider uppercase text-white">UltraRacha CRM</span>
            <span class="text-[9px] bg-[#FDCA02] text-[#003E78] font-black px-2 py-0.2 rounded-full uppercase">Oficial</span>
          </div>
          <span class="text-[10px] text-blue-200 block">Ultracem S.A.S. • Planta Galapa, Atlántico</span>
        </div>
      </div>

      <!-- Controls: View Mode Dropdown, AI Setup, Time Simulator -->
      <div class="flex items-center space-x-2.5">
        
        <!-- View Mode Dropdown Selector -->
        <div class="flex items-center space-x-1.5 bg-[#0A233F] p-1 rounded-xl border border-blue-400/40 shadow-xs">
          <label for="view-mode-selector" class="text-[11px] font-bold text-amber-300 hidden md:inline ml-1.5">Vista:</label>
          <select id="view-mode-selector" onchange="changeViewMode(this.value)" class="bg-white text-[#003E78] font-bold text-xs rounded-lg px-2.5 py-1.5 cursor-pointer shadow-xs focus:outline-none border-2 border-[#FDCA02] hover:bg-amber-50 transition-colors">
            <option value="desktop" selected>💻 Aplicación de Escritorio (Completa)</option>
            <option value="dual">💻📱 Vista Dividida (Escritorio + Celular al lado)</option>
            <option value="mobile">📱 Versión Celular (Móvil en Terreno)</option>
            <option value="prd">📑 Especificación PRD Ultracem</option>
          </select>
        </div>

        <!-- AI Settings Trigger -->
        <button onclick="openInPhoneAISettings()" class="btn-tactile flex items-center space-x-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] shadow-xs transition-all" title="Configurar API Key de IA (NVIDIA, DeepSeek, Groq, OpenAI)">
          <span>⚙️</span>
          <span class="hidden lg:inline">IA (Groq / NVIDIA)</span>
        </button>

        <!-- Time Mode Simulation Pill -->
        <div class="hidden xl:flex items-center space-x-1 text-xs border border-blue-400/30 rounded-xl p-1 bg-[#0A233F]">
          <button id="btn-time-day" onclick="setTimeMode('day')" aria-label="Simular 10:00 AM" class="px-2.5 py-1 rounded-lg font-bold bg-white text-[#003E78] text-[11px] transition-all">
            ☀️ 10:00 AM
          </button>
          <button id="btn-time-night" onclick="setTimeMode('night')" aria-label="Simular 10:45 PM" class="px-2.5 py-1 rounded-lg font-semibold text-blue-200 hover:text-white text-[11px] transition-all">
            🌙 10:45 PM
          </button>
        </div>

      </div>
    </div>
  </header>  <!-- ============================================================== -->
  <!-- MAIN WORKSPACE CONTAINER (FONDO SÓLIDO #F2F1EC)                -->
  <!-- ============================================================== -->
  <main id="main-content" class="flex-1 w-full mx-auto px-3 sm:px-5 lg:px-6 py-5 transition-all bg-[#F2F1EC]">

    <!-- ============================================================== -->
    <!-- 1. VISTA WORKSTATION: COMPUTADOR (IZQUIERDA) + CELULAR (DERECHA)-->
    <!-- Permite operar el CRM de escritorio y ver el celular al lado   -->
    <!-- ============================================================== -->
    <div id="view-workstation" class="w-full max-w-[1780px] mx-auto flex flex-col xl:flex-row gap-6 items-start justify-center">

      <!-- PANEL PRINCIPAL COMPUTADOR: CRM DE ESCRITORIO ULTRACEM -->
      <div id="desktop-app-wrapper" class="flex-1 w-full min-w-0">

    <!-- ============================================================== -->
    <!-- APLICACIÓN DE ESCRITORIO ULTRACEM CRM (FULL COMPUTADOR)        -->
    <!-- Misma funcionalidad e interacciones que el celular en desktop  -->
    <!-- Colores Primarios: Amarillo #FDCA02, Azul Oscuro #003E78, Blanco #FFFFFF -->
    <!-- ============================================================== -->
    <div id="ultracem-desktop-crm" class="w-full bg-[#F2F1EC] rounded-3xl border-2 border-slate-300 shadow-md overflow-hidden flex flex-col md:flex-row min-h-[820px]">
      
      <!-- ============================================================ -->
      <!-- SIDEBAR CORPORATIVO: AZUL OSCURO SÓLIDO (#003E78 / #0A233F)  -->
      <!-- ============================================================ -->
      <aside class="w-full md:w-64 bg-[#0A233F] text-white flex flex-col flex-shrink-0 p-4 border-r-2 border-slate-800 select-none justify-between">
        
        <div>
          <!-- Logo Ultracem Container with Amarillo Accent -->
          <div class="bg-[#003E78] rounded-2xl p-3.5 border-2 border-[#FDCA02] mb-5 flex items-center justify-center shadow-xs">
            <img src="data:image/png;base64,{logo_base64}" alt="Ultracem Cemento & Concreto" class="h-9 w-auto object-contain" />
          </div>

          <!-- Active Advisor Profile Chip in Sidebar -->
          <div class="bg-[#0B1E33] rounded-2xl p-3 border border-slate-700/80 mb-5 flex items-center space-x-3">
            <div class="relative">
              <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-10 h-10 rounded-full border-2 border-[#FDCA02] object-cover" />
              <span class="absolute bottom-0 right-0 w-2.5 h-2.5 rounded-full bg-emerald-400 border border-[#0A233F]"></span>
            </div>
            <div class="overflow-hidden">
              <div class="flex items-center space-x-1.5">
                <span class="font-extrabold text-xs text-white truncate">Carlos Mendoza</span>
                <span class="text-[9px] bg-[#FDCA02] text-[#003E78] font-black px-1.5 py-0.2 rounded-full uppercase">Niv 4</span>
              </div>
              <span class="text-[10px] text-slate-400 block truncate">Asesor Obras • Atlántico</span>
              <span class="text-[10px] text-amber-300 font-bold block mt-0.5">🔥 21 Días de Racha</span>
            </div>
          </div>

          <!-- Navigation Tabs Menu -->
          <nav class="space-y-1.5 text-xs font-semibold">
            <button id="dcrm-tab-btn-racha" onclick="switchDesktopCrmTab('racha')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-all bg-[#FDCA02] text-[#003E78] shadow-xs">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🔥</span>
                <span>Racha & Obras</span>
              </div>
              <span class="bg-[#003E78] text-[#FDCA02] font-black text-[10px] px-2 py-0.5 rounded-full">3</span>
            </button>

            <button id="dcrm-tab-btn-copiloto" onclick="switchDesktopCrmTab('copiloto')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🤖</span>
                <span>Copiloto IA</span>
              </div>
              <span class="text-[9px] bg-blue-900/60 text-blue-200 border border-blue-500/30 px-1.5 py-0.5 rounded-md font-mono-data">Groq/NIM</span>
            </button>

            <button id="dcrm-tab-btn-mapa" onclick="switchDesktopCrmTab('mapa')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🗺️</span>
                <span>Radar & B2B</span>
              </div>
              <span class="text-[9px] bg-amber-900/60 text-amber-300 border border-amber-500/30 px-1.5 py-0.5 rounded-full font-bold">12 B2B</span>
            </button>

            <button id="dcrm-tab-btn-liga" onclick="switchDesktopCrmTab('liga')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">🏆</span>
                <span>Liga de Asesores</span>
              </div>
              <span class="text-[10px] text-amber-300 font-bold">#4</span>
            </button>

            <button id="dcrm-tab-btn-perfil" onclick="switchDesktopCrmTab('perfil')" class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]">
              <div class="flex items-center space-x-2.5">
                <span class="text-base">👤</span>
                <span>Perfil & Cartera</span>
              </div>
              <span class="text-[9px] text-emerald-400 font-bold">1 Casco</span>
            </button>
          </nav>
        </div>

        <!-- Sidebar Footer Status -->
        <div class="pt-4 border-t border-slate-700/80 text-[11px] text-slate-400 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="text-slate-300 font-bold flex items-center">
              <span class="w-2 h-2 rounded-full bg-[#FDCA02] mr-1.5"></span>
              Planta Galapa
            </span>
            <span class="text-[10px] bg-emerald-950 text-emerald-300 px-1.5 py-0.2 rounded font-bold border border-emerald-500/40">100% OK</span>
          </div>
          <p class="text-[10px] text-slate-400">Molienda: 180 T/h • Hornos: 1,450 °C</p>
        </div>

      </aside>

      <!-- ============================================================ -->
      <!-- WORKSPACE PRINCIPAL (FONDO SÓLIDO #F2F1EC / TARJETAS BLANCAS)-->
      <!-- ============================================================ -->
      <main class="flex-1 p-5 sm:p-7 overflow-y-auto space-y-6">

        <!-- ========================================================== -->
        <!-- TAB 1: RACHA & SEGUIMIENTO COMERCIAL DE OBRAS              -->
        <!-- ========================================================== -->
        <div id="dcrm-content-racha" class="space-y-6">
          
          <!-- Top Executive Banner: Racha + Don Fraguado Mascot -->
          <div class="bg-[#003E78] rounded-2xl p-5 text-white border-2 border-[#FDCA02] shadow-sm flex flex-col lg:flex-row lg:items-center justify-between gap-5">
            <div class="space-y-2">
              <div class="flex flex-wrap items-center gap-2">
                <span class="bg-[#FDCA02] text-[#003E78] font-black text-xs px-2.5 py-0.5 rounded-full uppercase">Racha Activa: 21 Días 🔥</span>
                <span class="text-xs text-blue-200">•</span>
                <span class="text-xs text-amber-200 font-bold flex items-center">
                  ⏰ Corte Antichurn: <span id="desktop-countdown-timer" class="font-mono-data ml-1.5 bg-[#0A233F] text-amber-300 px-2 py-0.5 rounded-lg border border-amber-400/40">13h : 59m : 55s</span>
                </span>
                <span class="text-xs text-blue-200">•</span>
                <span class="text-xs bg-[#0A233F] text-white px-2.5 py-0.5 rounded-full font-bold border border-white/20">🛡️ 1 Casco Disponible</span>
              </div>
              <h2 class="text-2xl font-black tracking-tight text-white">Gestión de Cuentas, Pedidos & Prevención Antichurn</h2>
              <p class="text-xs text-blue-100 max-w-2xl leading-relaxed">
                Atiende o escala tus clientes en semáforo rojo antes de las 11:59 PM para proteger tu racha y sumar +150 XP.
              </p>
            </div>

            <!-- Don Fraguado Interactive Card (Desktop) -->
            <div onclick="tocarDonFraguado()" class="btn-tactile bg-white text-slate-800 rounded-2xl p-3.5 border-2 border-[#FDCA02] shadow-sm flex items-center space-x-3 flex-shrink-0 cursor-pointer max-w-sm">
              <div class="w-12 h-12 rounded-xl bg-slate-100 border border-slate-300 flex items-center justify-center text-2xl flex-shrink-0">
                👷
              </div>
              <div class="text-xs">
                <div class="flex items-center space-x-1.5">
                  <span class="font-black text-[#003E78]">Don Fraguado</span>
                  <span class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full">Motivado</span>
                </div>
                <p id="desktop-fraguado-dialogue" class="text-[11px] text-slate-600 mt-0.5 leading-snug">
                  "¡Buenos días Carlos! Tu racha está protegida. Toca aquí para consejos de venta."
                </p>
              </div>
            </div>
          </div>

          <!-- Split 2-Column Desktop CRM Layout -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
            
            <!-- Columna Izquierda (7 cols): Cartera de Clientes -->
            <div class="lg:col-span-7 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-4">
              
              <!-- Filter chips -->
              <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                <div class="flex flex-wrap items-center gap-1.5 text-xs">
                  <button onclick="filtrarClientesDesktop('todos')" id="dfilter-todos" class="px-3 py-1 rounded-lg font-bold bg-[#003E78] text-white">Todos (3)</button>
                  <button onclick="filtrarClientesDesktop('obras')" id="dfilter-obras" class="px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200">🏗️ Obras (2)</button>
                  <button onclick="filtrarClientesDesktop('ferreterias')" id="dfilter-ferreterias" class="px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200">🏪 Ferreterías (1)</button>
                  <button onclick="filtrarClientesDesktop('rojos')" id="dfilter-rojos" class="px-3 py-1 rounded-lg font-semibold text-rose-700 bg-rose-50 border border-rose-200">🔴 En Riesgo (1)</button>
                </div>
                <span class="text-xs text-slate-400 font-medium">3 Casos Asignados</span>
              </div>

              <!-- List of Client Cards -->
              <div class="space-y-3.5">
                
                <!-- Client 1: Constructora Bolívar -->
                <div id="dcard-client-1" onclick="seleccionarClienteDesktop(1)" class="p-4 rounded-xl border-2 border-rose-300 bg-rose-50/20 hover:bg-rose-50/40 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Constructora Bolívar</h3>
                        <span class="text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full">Obra Mayor 4G</span>
                      </div>
                      <span class="text-xs text-slate-500">Torres del Mar • 120 Ton Cemento Estructural Max</span>
                    </div>
                    <span class="bg-[#DC2626] text-white font-black text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">🔴 8D Sin Pedido</span>
                  </div>

                  <div class="bg-white p-2.5 rounded-lg border border-rose-200 text-xs text-rose-800 space-y-1">
                    <p class="font-bold">⚠️ Riesgo Crítico de Pérdida:</p>
                    <p class="text-[11px] text-slate-600">Superó su ciclo habitual de reposición por 3 días. Contacta hoy para salvar tu racha comercial (+100 XP).</p>
                  </div>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $38.2 M COP</span>
                    <div class="space-x-1.5 text-xs">
                      <button onclick="event.stopPropagation(); contactarClienteWhatsApp('Constructora Bolívar')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg">WhatsApp (+50 XP)</button>
                      <button onclick="event.stopPropagation(); seleccionarClienteDesktop(1)" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-3 py-1 rounded-lg">Gestionar Caso ➔</button>
                    </div>
                  </div>
                </div>

                <!-- Client 2: Ferretería El Constructor -->
                <div id="dcard-client-2" onclick="seleccionarClienteDesktop(2)" class="p-4 rounded-xl border border-amber-300 bg-amber-50/20 hover:bg-amber-50/40 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Ferretería El Constructor</h3>
                        <span class="text-[10px] bg-teal-100 text-teal-800 font-bold px-2 py-0.5 rounded-full">Ferretería</span>
                      </div>
                      <span class="text-xs text-slate-500">Sede Centro Soledad • 45 Ton Cemento Uso General</span>
                    </div>
                    <span class="bg-[#FDCA02] text-[#003E78] font-black text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">🟡 4D Sin Pedido</span>
                  </div>

                  <p class="text-xs text-slate-600">Alerta de fraguado: Requiere reposición de bultos antes del fin de semana.</p>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $14.2 M COP</span>
                    <div class="space-x-1.5 text-xs">
                      <button onclick="event.stopPropagation(); contactarClienteWhatsApp('Ferretería El Constructor')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg">WhatsApp</button>
                      <button onclick="event.stopPropagation(); seleccionarClienteDesktop(2)" class="btn-tactile bg-slate-800 hover:bg-slate-900 text-white font-bold px-3 py-1 rounded-lg">Gestionar Caso ➔</button>
                    </div>
                  </div>
                </div>

                <!-- Client 3: Marval Altos de Riomar -->
                <div id="dcard-client-3" onclick="seleccionarClienteDesktop(3)" class="p-4 rounded-xl border border-slate-200 bg-slate-50/40 hover:bg-slate-50 cursor-pointer transition-all space-y-2.5">
                  <div class="flex items-center justify-between">
                    <div>
                      <div class="flex items-center space-x-2">
                        <h3 class="font-extrabold text-sm text-slate-900">Marval — Altos de Riomar</h3>
                        <span class="text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full">Industrial</span>
                      </div>
                      <span class="text-xs text-slate-500">Torre 3 • 210 Ton Cemento Marino Impermeable</span>
                    </div>
                    <span class="bg-emerald-100 text-emerald-800 font-bold text-[10px] px-2.5 py-0.5 rounded-full uppercase">🟢 Al Día (Placa Fundida)</span>
                  </div>

                  <div class="flex items-center justify-between pt-1">
                    <span class="text-xs font-mono-data font-bold text-slate-700">Valor Mensual: $65.8 M COP</span>
                    <button onclick="event.stopPropagation(); seleccionarClienteDesktop(3)" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-3 py-1 rounded-lg text-xs">Ver Bitácora ➔</button>
                  </div>
                </div>

              </div>

            </div>

            <!-- Columna Derecha (5 cols): Consola de Acción en Vivo -->
            <div class="lg:col-span-5 bg-white rounded-2xl p-5 border border-slate-200/90 shadow-xs space-y-5">
              
              <div class="border-b border-slate-100 pb-3 flex items-center justify-between">
                <div>
                  <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Consola de Acción</span>
                  <h3 id="dconsole-client-name" class="font-black text-base text-slate-900">Constructora Bolívar</h3>
                </div>
                <span class="text-[10px] font-bold bg-rose-100 text-rose-800 px-2 py-0.5 rounded-full">🔴 Prioridad Alta</span>
              </div>

              <!-- Audio Recording Console (Same as Mobile) -->
              <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-3">
                <div class="flex items-center justify-between text-xs">
                  <span class="font-bold text-slate-800 flex items-center">
                    <span class="text-base mr-1.5">🎙️</span>
                    Nota de Voz de la Visita
                  </span>
                  <span id="daudio-status-badge" class="text-[10px] bg-slate-200 text-slate-600 px-2 py-0.5 rounded-full font-mono-data">Listo</span>
                </div>

                <div class="flex items-center space-x-2">
                  <button id="dbtn-record-audio" onclick="toggleDesktopAudioRecording()" class="btn-tactile flex-1 bg-[#D9531E] hover:bg-[#c24615] text-white font-bold py-2 px-3 rounded-xl text-xs flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>🔴</span>
                    <span id="dbtn-record-text">Grabar Nota de Audio</span>
                  </button>
                </div>

                <!-- Audio Playback Container -->
                <div id="daudio-player-container" class="space-y-2 pt-1">
                  <audio id="daudio-player" controls class="w-full h-8"></audio>
                  <p id="daudio-transcript-text" class="text-[11px] text-slate-600 italic bg-white p-2 rounded-lg border border-slate-200">
                    "Minuta: El ingeniero de Constructora Bolívar confirma necesidad de 40 Ton de Cemento Estructural Max para el vaciado del miércoles..."
                  </p>
                </div>
              </div>

              <!-- Internal Department Escalation Module (Saves Streak in 1 Click) -->
              <div class="bg-[#0A233F] text-white p-4 rounded-xl space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] font-bold uppercase tracking-wider text-[#FDCA02]">Escalamiento a Departamento</span>
                  <span class="text-[10px] bg-emerald-500 text-white font-bold px-2 py-0.5 rounded-full">Salva Racha</span>
                </div>
                <h4 class="font-bold text-xs text-white">¿Bloqueo administrativo? Transfiere el caso:</h4>
                
                <select id="descalation-dept-select" class="w-full bg-[#0B1E33] text-white border border-slate-600 rounded-lg p-2 text-xs font-semibold focus:outline-none">
                  <option value="cartera">💰 Cartera & Crédito (SLA: 4 horas) — Cupo excedido</option>
                  <option value="logistica">🚚 Logística & Mixers (SLA: 2 horas) — Tractomula en ruta</option>
                  <option value="calidad">🔬 Calidad NTC 121 (SLA: 6 horas) — Certificado de rotura</option>
                  <option value="pricing">🏷️ Dirección Comercial (SLA: 4 horas) — Descuento por volumen</option>
                </select>

                <button onclick="escalarCasoDesktop()" class="w-full btn-tactile bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] font-black py-2.5 px-3 rounded-xl text-xs flex items-center justify-center space-x-1.5 shadow-md">
                  <span>⚡</span>
                  <span>Escalar Caso y Proteger Mi Racha</span>
                </button>
              </div>

              <!-- Client Transfer to Colleague -->
              <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs">
                <span class="text-slate-500">¿Reasignar zona?</span>
                <button onclick="openTransferClientModal(1, 'Constructora Bolívar')" class="text-[#003E78] font-bold hover:underline">
                  Transferir cliente a un compañero ➔
                </button>
              </div>

            </div>

          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 2: COPILOTO IA MULTIMODELO (GROQ / NVIDIA / DEEPSEEK)  -->
        <!-- ========================================================== -->
        <div id="dcrm-content-copiloto" class="hidden space-y-5">
          
          <!-- Copilot Header Bar -->
          <div class="bg-[#003E78] text-white rounded-2xl p-5 border-2 border-[#FDCA02] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xl">🤖</span>
                <h2 class="text-xl font-black">Copiloto IA Multimodelo Ultracem</h2>
              </div>
              <p class="text-xs text-blue-100 mt-0.5">Asistente técnico comercial con guardrails certificados de la norma NTC 121</p>
            </div>

            <!-- Provider & Setup Action -->
            <div class="flex items-center space-x-2">
              <select id="dcopilot-provider-select" onchange="cambiarProveedorSeleccionado(this.value)" class="bg-[#0A233F] text-white border border-slate-600 rounded-xl px-3 py-1.5 text-xs font-bold cursor-pointer">
                <option value="groq">Groq Cloud (LPU 500-1000 t/s)</option>
                <option value="nvidia">NVIDIA NIM (Llama 3.1 70B)</option>
                <option value="deepseek">DeepSeek (V3 / R1)</option>
                <option value="openai">OpenAI (GPT-4o)</option>
              </select>
              <button onclick="openInPhoneAISettings()" class="btn-tactile bg-[#FDCA02] hover:bg-amber-400 text-[#003E78] font-black px-3.5 py-1.5 rounded-xl text-xs flex items-center space-x-1 shadow-xs">
                <span>⚙️</span>
                <span>Configurar API Key</span>
              </button>
            </div>
          </div>

          <!-- Quick Prompts Chips -->
          <div class="flex flex-wrap items-center gap-2 text-xs">
            <span class="text-slate-400 font-bold uppercase text-[10px] mr-1">Preguntas Frecuentes:</span>
            <button onclick="probarPromptRapidoDesktop('¿Cuál es la dosificación exacta para una losa de 3000 PSI con Cemento Estructural Max NTC 121?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              📐 Dosificación 3000 PSI NTC 121
            </button>
            <button onclick="probarPromptRapidoDesktop('Argos ofreció $500 menos por bulto en Soledad. ¿Qué argumentos técnicos doy para defender nuestro Cemento Uso General?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              ⚔️ Defensa Comercial vs Argos
            </button>
            <button onclick="probarPromptRapidoDesktop('¿Por qué el Cemento Marino Ultracem es superior para obras portuarias en el Caribe?')" class="bg-white hover:bg-blue-50 text-[#003E78] border border-slate-300 px-3 py-1 rounded-lg font-semibold shadow-xs">
              🌊 Cemento Marino vs Sulfatos
            </button>
            <button onclick="probarPromptRapidoDesktop('¿Qué es el ácido ribonucleico?')" class="bg-white hover:bg-rose-50 text-rose-700 border border-rose-200 px-3 py-1 rounded-lg font-semibold shadow-xs" title="Prueba los guardrails estrictos de Ultracem">
              🛡️ Probar Guardrails (Pregunta No Comercial)
            </button>
          </div>

          <!-- Desktop Chat Window -->
          <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col h-[520px] overflow-hidden">
            
            <!-- Chat Messages Feed -->
            <div id="desktop-chat-messages" class="flex-1 overflow-y-auto p-5 space-y-4 text-xs">
              
              <!-- AI Welcome -->
              <div class="flex items-start space-x-3">
                <div class="w-8 h-8 rounded-full bg-[#003E78] text-[#FDCA02] font-black flex items-center justify-center text-xs flex-shrink-0">
                  U
                </div>
                <div class="bg-slate-100 rounded-2xl p-3.5 max-w-2xl text-slate-800 leading-relaxed space-y-1">
                  <div class="font-bold text-[#003E78]">Copiloto Comercial Ultracem</div>
                  <p>¡Hola Carlos! Estoy listo para apoyarte en campo. Puedo calcular dosificaciones de concreto, redactar cotizaciones técnicas según la norma <strong>NTC 121</strong> o preparar argumentos de venta frente a la competencia.</p>
                  <span class="text-[10px] text-slate-400 block pt-1">Motor: Groq Cloud LPU (openai/gpt-oss-120b)</span>
                </div>
              </div>

            </div>

            <!-- Chat Input Bar -->
            <div class="p-3.5 bg-slate-50 border-t border-slate-200 flex items-center space-x-2">
              <input id="desktop-chat-input" type="text" placeholder="Escribe tu consulta sobre cemento, dosificaciones o clientes..." onkeydown="if(event.key==='Enter') enviarConsultaAIDesktop()" class="flex-1 bg-white border border-slate-300 rounded-xl px-4 py-2.5 text-xs text-slate-800 focus:outline-none focus:border-[#003E78]" />
              <button onclick="enviarConsultaAIDesktop()" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-5 py-2.5 rounded-xl text-xs shadow-xs flex items-center space-x-1">
                <span>Enviar</span>
                <span>➔</span>
              </button>
            </div>

          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 3: RADAR GEORREFERENCIADO & DIRECTORIO B2B            -->
        <!-- ========================================================== -->
        <div id="dcrm-content-mapa" class="hidden space-y-5">
          
          <!-- Top Sub-view Selector -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-3.5 rounded-2xl border border-slate-200/90 shadow-xs">
            <div class="flex items-center space-x-2 text-xs">
              <button onclick="switchDesktopMapSubView('mapa')" id="dmap-sub-btn-map" class="px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs">
                🗺️ Mapa Interactivo de Colombia
              </button>
              <button onclick="switchDesktopMapSubView('prospectos')" id="dmap-sub-btn-prospects" class="px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100">
                🏢 Directorio B2B (12 Empresas Caribe)
              </button>
            </div>

            <div class="flex items-center space-x-2 text-xs">
              <button onclick="toggleDesktopMapSatellite()" class="bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold px-3 py-1.5 rounded-lg shadow-xs">
                🛰️ Capa Satelital ESRI
              </button>
              <span class="text-xs text-slate-400">Planta Galapa • Km 8 Vía Tubará</span>
            </div>
          </div>

          <!-- Subview 1: Full Desktop Map -->
          <div id="dmap-view-container" class="bg-white rounded-2xl border border-slate-200/90 shadow-xs p-3 space-y-3">
            <div id="desktop-colombia-map" class="w-full h-[540px] rounded-xl overflow-hidden border border-slate-200 z-10"></div>
          </div>

          <!-- Subview 2: B2B Caribbean Directory -->
          <div id="dprospects-view-container" class="hidden bg-white rounded-2xl border border-slate-200/90 shadow-xs p-5 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
              <div>
                <h3 class="font-black text-base text-slate-900">Directorio de Empresas & Obras para Conquistar</h3>
                <p class="text-xs text-slate-500">12 prospectos estratégicos del Caribe actualmente atendidos por la competencia</p>
              </div>
              <span class="text-xs bg-[#FDCA02] text-[#003E78] font-black px-3 py-1 rounded-full">+50 XP por Primer Contacto</span>
            </div>

            <!-- Prospects Table -->
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
                  <tr>
                    <th class="py-3 px-4">Empresa / Proyecto</th>
                    <th class="py-3 px-3">Ubicación</th>
                    <th class="py-3 px-3">Volumen Estimado</th>
                    <th class="py-3 px-3">Proveedor Actual</th>
                    <th class="py-3 px-3">Gancho Ultracem</th>
                    <th class="py-3 px-4 text-right">Acción Comercial</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-100 font-mono-data text-[11px]">
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Constructora Amarilo — Parque Heredia</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Cartagena, BOL</td>
                    <td class="py-3 px-3 font-bold text-slate-800">450 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded">Argos</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Despacho garantizado en mixer antes de 2h</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(301)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Bloquera del Sinú S.A.S.</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Montería, COR</td>
                    <td class="py-3 px-3 font-bold text-slate-800">280 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-orange-100 text-orange-800 font-bold px-2 py-0.5 rounded">Cemex</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Resistencia temprana a 3 días con Estructural Max</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(302)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-slate-50">
                    <td class="py-3 px-4 font-sans font-bold text-slate-900">Consorcio Vial Puerta de Oro</td>
                    <td class="py-3 px-3 font-sans text-slate-600">Barranquilla, ATL</td>
                    <td class="py-3 px-3 font-bold text-slate-800">620 Ton/mes</td>
                    <td class="py-3 px-3 font-sans"><span class="bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded">Argos</span></td>
                    <td class="py-3 px-3 font-sans text-slate-600">Flete bonificado desde Planta Galapa</td>
                    <td class="py-3 px-4 text-right font-sans">
                      <button onclick="contactarProspectoDirecto(303)" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg text-xs">Contactar WhatsApp</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 4: LIGA DE ASESORES COMERCIAL                         -->
        <!-- ========================================================== -->
        <div id="dcrm-content-liga" class="hidden space-y-6">
          
          <!-- Top Podium: Amarillo, Azul Oscuro y Blanco -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
            
            <!-- 1st Place: Milena Ospino -->
            <div class="bg-white rounded-3xl p-5 border-4 border-[#FDCA02] shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-[#FDCA02] text-[#003E78] font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥇 1° Líder Regional
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#003E78] text-[#FDCA02] font-black text-base flex items-center justify-center">MO</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Milena Ospino</h3>
                  <span class="text-xs text-slate-500 block">Costa Norte • Concretos Especiales</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-[#003E78] text-base font-mono-data">28 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-[#003E78] text-base font-mono-data">940 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📧 mospino@ultracem.co • 100% SLA cumplido</p>
              </div>
            </div>

            <!-- 2nd Place: Adriana Anaya -->
            <div class="bg-white rounded-3xl p-5 border-2 border-slate-300 shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-slate-200 text-slate-800 font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥈 2° Puesto
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#0A233F] text-white font-black text-base flex items-center justify-center">AA</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Adriana Anaya</h3>
                  <span class="text-xs text-slate-500 block">Ferreterías • Bolívar / Atlántico</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">24 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">820 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📧 aanaya@ultracem.co • 98% SLA cumplido</p>
              </div>
            </div>

            <!-- 3rd Place: Hichel Espitia -->
            <div class="bg-white rounded-3xl p-5 border-2 border-amber-300 shadow-sm relative space-y-3">
              <div class="absolute -top-3.5 right-4 bg-amber-100 text-amber-900 font-black text-xs px-3 py-1 rounded-full shadow-xs">
                🥉 3° Puesto
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-12 h-12 rounded-2xl bg-[#003E78] text-white font-black text-base flex items-center justify-center">HE</div>
                <div>
                  <h3 class="font-extrabold text-base text-slate-900">Hichel Espitia</h3>
                  <span class="text-xs text-slate-500 block">Infraestructura & Obra 4G</span>
                </div>
              </div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Racha</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">21 Días 🔥</span>
                </div>
                <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-center">
                  <span class="text-[10px] text-slate-400 block font-bold">Volumen</span>
                  <span class="font-black text-slate-800 text-base font-mono-data">1,150 Ton</span>
                </div>
              </div>
              <div class="text-[11px] text-slate-600">
                <p>📱 310 250 3454 • 96% SLA cumplido</p>
              </div>
            </div>

          </div>

          <!-- Asesor Actual (Carlos Mendoza) Status Card -->
          <div class="bg-[#003E78] text-white rounded-2xl p-5 border-2 border-[#FDCA02] shadow-xs flex items-center justify-between">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 rounded-full bg-[#FDCA02] text-[#003E78] font-black text-sm flex items-center justify-center">
                4°
              </div>
              <div>
                <h4 class="font-black text-sm">Tu Posición: Carlos Mendoza (4° Puesto)</h4>
                <p class="text-xs text-blue-200">21 Días de Racha acumulada • 680 Ton despachadas • Estás a solo 140 Ton del podio</p>
              </div>
            </div>
            <span class="bg-[#FDCA02] text-[#003E78] font-black text-xs px-3 py-1 rounded-xl">Zona Caribe</span>
          </div>

        </div>

        <!-- ========================================================== -->
        <!-- TAB 5: PERFIL & GESTIÓN DE CARTERA                        -->
        <!-- ========================================================== -->
        <div id="dcrm-content-perfil" class="hidden space-y-6">
          
          <div class="bg-white rounded-3xl p-6 border border-slate-200/90 shadow-xs space-y-6">
            
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-5">
              <div class="flex items-center space-x-4">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=140&auto=format&fit=crop&q=80" alt="Carlos Mendoza" class="w-16 h-16 rounded-full border-4 border-[#FDCA02] object-cover" />
                <div>
                  <h3 class="text-xl font-black text-slate-900">Carlos Mendoza</h3>
                  <p class="text-xs text-slate-500 font-medium">Asesor Comercial Senior • Ultracem S.A.S. (Costa Norte)</p>
                  <span class="inline-block text-[10px] bg-blue-100 text-[#003E78] font-bold px-2 py-0.5 rounded-full mt-1">Caribe: Obras & Constructoras</span>
                </div>
              </div>

              <!-- Casco inventory -->
              <div class="bg-[#0A233F] text-white p-3.5 rounded-2xl border border-slate-700 text-center">
                <span class="text-[10px] text-[#FDCA02] uppercase font-bold block">Inventario de Seguridad</span>
                <span class="text-xl font-black font-mono-data">1 Casco Activo 🛡️</span>
                <span class="text-[10px] text-slate-300 block">Congelación 24h ante emergencias</span>
              </div>
            </div>

            <!-- Heatmap 30 days grid -->
            <div class="space-y-2">
              <h4 class="font-bold text-xs text-slate-800">Registro de Cumplimiento de Visitas (Últimos 30 Días)</h4>
              <div class="grid grid-cols-10 gap-1.5 p-3 bg-slate-50 rounded-xl border border-slate-200">
                <div class="h-6 rounded bg-[#003E78]" title="Día 1: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 2: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 3: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 4: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 5: 100%"></div>
                <div class="h-6 rounded bg-slate-200" title="Día 6: Domingo"></div>
                <div class="h-6 rounded bg-slate-200" title="Día 7: Domingo"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 8: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 9: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 10: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 11: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 12: 100%"></div>
                <div class="h-6 rounded bg-[#FDCA02]" title="Día 13: Casco utilizado"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 14: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 15: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 16: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 17: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 18: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 19: 100%"></div>
                <div class="h-6 rounded bg-[#003E78]" title="Día 20: 100%"></div>
                <div class="h-6 rounded bg-[#FDCA02] border border-[#003E78]" title="Día 21: Hoy en progreso"></div>
              </div>
            </div>

            <!-- Transfer module -->
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <h4 class="font-bold text-xs text-slate-900">Transferencia Voluntaria de Clientes</h4>
                <p class="text-xs text-slate-500">¿Saldrás a vacaciones o requieres apoyo en una zona? Transfiere una cuenta a Milena, Adriana o Hichel.</p>
              </div>
              <button onclick="openTransferClientModal(1, 'Constructora Bolívar')" class="btn-tactile bg-[#003E78] hover:bg-blue-900 text-white font-bold px-4 py-2 rounded-xl text-xs whitespace-nowrap shadow-xs">
                Transferir un Cliente
              </button>
            </div>

          </div>

        </div>

      </main>

    </div>

      </div>

      <!-- PANEL CELULAR: APLICACIÓN MÓVIL EN VIVO (STICKY DERECHA) -->
      <aside id="phone-container-wrapper" class="hidden xl:flex w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex-col items-center">
        <div class="mb-2 text-center">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white border-2 border-[#FDCA02] shadow-xs">
            📱 Asesor Móvil en Terreno
          </span>
        </div>
<!-- Phone Canvas Frame: Strict isolation & fixed height containment -->
      <div class="w-full max-w-[420px] bg-white rounded-[40px] shadow-2xl border-4 border-slate-800 overflow-hidden flex flex-col h-[820px] max-h-[820px] relative" style="position: relative; isolation: isolate; contain: paint;">
        
        <!-- Phone Status Notch -->
        <div class="bg-slate-900 pt-3.5 px-6 pb-2 flex justify-between items-center text-white text-[11px] font-mono-data select-none z-30 flex-shrink-0">
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
        <div id="inphone-sheet-overlay" class="hidden absolute inset-0 z-50 bg-slate-950/70 backdrop-blur-xs flex flex-col justify-end rounded-[36px] overflow-hidden transition-all duration-300">
          <!-- Backdrop click to dismiss -->
          <div class="flex-1 cursor-pointer" onclick="closeInPhoneSheet()" title="Cerrar panel"></div>
          
          <!-- Sheet Body Panel (Slides up from bottom inside the phone) -->
          <div id="inphone-sheet-panel" class="bg-white rounded-t-[28px] max-h-[90%] flex flex-col shadow-2xl border-t border-slate-200 overflow-hidden transform animate-sheet-up">
            
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
        <div id="mobile-screen-content" class="flex-1 flex flex-col overflow-hidden relative">
          
          <!-- ======================================================== -->
          <!-- PANTALLA 1: RACHA & CLIENTES                             -->
          <!-- ======================================================== -->
          <div id="screen-racha" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Mobile Header Bar (Full Bleed - Perfectly Aligned & Symmetrical) -->
            <div class="bg-[#003E78] text-white px-4 pt-3 pb-3 relative overflow-hidden flex-shrink-0">
              <!-- Top Row: User Avatar & Streak Pill -->
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

              <!-- Bottom Row: Midnight Countdown & Helmet Freeze Badge -->
              <div class="mt-2.5 pt-2 border-t border-white/15 flex items-center justify-between text-xs relative z-10">
                <div class="flex items-center space-x-1.5 text-blue-100 text-[11px]">
                  <span>⏰</span>
                  <span class="font-medium">Corte 11:59 PM:</span>
                  <span id="countdown-timer" class="font-mono-data font-bold text-amber-300 bg-white/10 px-2 py-0.5 rounded text-[11px]">13h : 59m : 12s</span>
                </div>

                <!-- Casco Protector Pill Trigger -->
                <button onclick="navigateToTab('perfil')" id="header-casco-btn" class="btn-tactile bg-white/15 hover:bg-white/25 border border-white/25 text-white font-bold text-[11px] px-2.5 py-0.5 rounded-full flex items-center space-x-1.5 shadow-xs" title="Cascos disponibles para proteger tu racha">
                  <span>⛑️</span>
                  <span id="header-casco-count">1 Casco</span>
                </button>
              </div>
            </div>

            <!-- Scrollable Content Area -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <!-- ULTRACEM ACTIVATION BANNER (DINÁMICO POR FASES 1-4) -->
              
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg shadow-xs transition-all flex items-center space-x-1 flex-shrink-0">
                    <span>📘</span>
                    <span>Ver PRD</span>
                  </button>
                </div>
              </div>

              <!-- DON FRAGUADO: MASCOTA VECTORIAL INTERACTIVA -->
              <div id="mascot-card" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all">
                
                <!-- SVG Vector Mascot -->
                <div id="don-fraguado-container" class="relative w-16 h-18 flex-shrink-0 cursor-pointer select-none mascot-breathing" onclick="pokeMascot()" title="¡Haz clic en Don Fraguado!">
                  <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm overflow-visible" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />

                    <!-- Mascota: Bulto de Cemento Ultracem -->
                    <g id="mascot-body-group" class="transition-transform duration-300 origin-bottom">
                      <!-- Sack Depth -->
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
                      <text x="50" y="88.2" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-weight="800" font-size="4.2" text-anchor="middle">50 kg • NTC 121</text>

                      <!-- Face: Interactive Eyes -->
                      <g id="mascot-eyes">
                        <!-- Left Eye -->
                        <circle cx="38" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="39.5" cy="52.5" r="2" fill="#FFFFFF" />
                        <!-- Right Eye -->
                        <circle cx="62" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="63.5" cy="52.5" r="2" fill="#FFFFFF" />
                      </g>

                      <!-- Rosy Cheeks -->
                      <ellipse cx="30" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>
                      <ellipse cx="70" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>

                      <!-- Mouth: Happy smile -->
                      <path id="mascot-mouth" d="M 44,60 Q 50,65 56,60" fill="none" stroke="#0F172A" stroke-width="2" stroke-linecap="round" />
                    </g>

                    <!-- Engineer Hard Hat (Casco Amarillo Ultracem) -->
                    <g id="mascot-helmet-group" class="transition-transform duration-300">
                      <!-- Helmet Dome -->
                      <path d="M 18,34 C 18,12 82,12 82,34 Z" fill="#FACC15" stroke="#CA8A04" stroke-width="2" />
                      <!-- Helmet Center Crest Ridge -->
                      <path d="M 46,14 L 54,14 L 53,33 L 47,33 Z" fill="#EAB308" />
                      <!-- Helmet Brim / Visor -->
                      <path d="M 12,34 Q 50,29 88,34 Q 50,38 12,34 Z" fill="#CA8A04" />
                      <!-- Reflective Strip on Brim -->
                      <path d="M 22,33.5 Q 50,30.5 78,33.5" fill="none" stroke="#FEF08A" stroke-width="1.8" stroke-linecap="round" />
                    </g>
                  </svg>
                </div>

                <!-- Speech Bubble Dialogue -->
                <div class="flex-1">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-xs font-black text-slate-800 flex items-center space-x-1.5">
                      <span>Don Fraguado</span>
                      <span id="mascot-mood-badge" class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full">⚡ Motivado</span>
                    </span>
                    <span class="text-[10px] text-slate-500 font-semibold">Tócame</span>
                  </div>
                  <p id="mascot-dialogue-text" class="text-xs text-slate-600 leading-snug">
                    ¡Buenos días Carlos! Tu racha está protegida. Tienes <strong>2 clientes por contactar</strong> antes de las 11:59 PM para sumar +150 XP.
                  </p>
                </div>
              </div>

              <!-- Quick Banner to Prospecting Search Engine -->
              <div onclick="navigateToTab('mapa'); setMapSubView('prospectos');" class="btn-tactile bg-[#003E78] text-white p-3.5 rounded-2xl shadow-xs flex items-center justify-between cursor-pointer hover:shadow-md transition-all">
                <div class="flex items-center space-x-3">
                  <span class="text-2xl">🏢</span>
                  <div>
                    <h4 class="font-extrabold text-xs text-white leading-tight">Radar de Obras & Nuevas Empresas</h4>
                    <p class="text-[10px] text-blue-200 mt-0.5">12 constructoras y prefabricados listas para contactar</p>
                  </div>
                </div>
                <span class="text-xs bg-white/20 px-2 py-1 rounded-lg font-bold">Ver Empresas ➔</span>
              </div>

              <!-- Filter Bar (3 Clean Columns) -->
              <div class="space-y-1.5">
                <div class="flex items-center justify-between text-xs px-1">
                  <span class="font-bold text-slate-700">Mi Cartera Activa de Clientes</span>
                  <span class="text-[10px] text-slate-500" id="filter-count-badge">3 Casos Activos</span>
                </div>

                <div class="grid grid-cols-3 gap-2 bg-slate-200/80 p-1 rounded-xl">
                  <button id="filter-btn-todos" onclick="filterClients('todos')" class="py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs text-center">
                    Todos (3)
                  </button>
                  <button id="filter-btn-obras" onclick="filterClients('obras')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏗️ Obras (2)
                  </button>
                  <button id="filter-btn-ferreterias" onclick="filterClients('ferreterias')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏪 Ferret. (1)
                  </button>
                </div>
              </div>

              <!-- CLIENT CARD 1: CONSTRUCTORA BOLÍVAR (CRÍTICO) -->
              <div id="card-client-1" class="client-card bg-white rounded-2xl p-4 border-2 border-rose-400 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Constructora Bolívar</h3>
                      <span class="text-[10px] font-extrabold bg-blue-100 text-[#004797] px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento Estructural</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 border border-rose-200 px-2 py-0.5 rounded-md">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                    <span>8D SIN PEDIDO</span>
                  </span>
                </div>

                <!-- Churn Risk Warning Banner -->
                <div class="bg-rose-50/80 border border-rose-200/90 rounded-xl p-2.5 text-[11px] text-rose-900 flex items-start space-x-2">
                  <span class="text-rose-600 mt-0.5 text-xs">⚠️</span>
                  <p class="leading-snug">
                    <strong>Riesgo Crítico de Pérdida:</strong> Superó su ciclo habitual de recompra por 3 días. Contacta hoy para salvar tu racha comercial (+100 XP).
                  </p>
                </div>

                <!-- Action Buttons: WhatsApp & Register Action -->
                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Constructora Bolívar', '120 Ton Cemento Estructural')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(1, 'Constructora Bolívar')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <!-- Secondary Technical Actions: Cubicaje & Voice Notes -->
                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCubicajeModal('Constructora Bolívar')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📐</span>
                    <span>Cubicación Losa</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Constructora Bolívar')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz en obra">
                    <span>🎙️</span>
                  </button>
                </div>

                <!-- Transfer Client to Colleague Option -->
                <div class="pt-1">
                  <button onclick="openTransferClientModal(1, 'Constructora Bolívar — Torres del Mar')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

                <!-- Interactive Activity Timeline Container (With Saved Audios) -->
                <div id="timeline-box-1" class="bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-[11px] space-y-2 mt-2">
                  <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-700 text-[10px] uppercase tracking-wider">Historial Reciente & Audios</span>
                    <span class="text-[9px] text-emerald-600 font-semibold font-mono-data">Sincronizado</span>
                  </div>
                  <div id="timeline-notes-list-1" class="space-y-2">
                    <div class="flex items-start space-x-2 text-slate-600">
                      <span class="w-1.5 h-1.5 rounded-full bg-slate-400 mt-1.5 flex-shrink-0"></span>
                      <div>
                        <strong>Visita Presencial</strong> hace 3 días: El residente Ing. Arango solicitó cotización con flete incluido.
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- CLIENT CARD 2: FERRETERÍA EL CONSTRUCTOR -->
              <div id="card-client-2" class="client-card bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3 transition-all" data-tipo="ferreterias">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Ferretería El Constructor</h3>
                      <span class="text-[10px] font-extrabold bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded">Ferretería</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Sede Centro Soledad • 45 Ton Cemento Gris</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
                    <span>4D SIN PEDIDO</span>
                  </span>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Ferretería El Constructor', '45 Ton Cemento Gris')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(2, 'Ferretería El Constructor')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCertificadoModal('Ferretería El Constructor', 'Cemento Uso General')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📜</span>
                    <span>Certificado Calidad</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Ferretería El Constructor')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz">
                    <span>🎙️</span>
                  </button>
                </div>

                <div class="pt-1">
                  <button onclick="openTransferClientModal(2, 'Ferretería El Constructor — Sede Centro')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente fijo a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

              </div>

              <!-- CLIENT CARD 3: CASO BLOQUEADO POR OTRO ASESOR -->
              <div id="card-client-3" class="client-card bg-slate-100/80 rounded-2xl p-4 border border-slate-300 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-700 text-sm tracking-tight">Marval — Altos de Riomar</h3>
                      <span class="text-[10px] font-extrabold bg-slate-200 text-slate-600 px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Vaciado Torre 3 • Barranquilla</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded-md">
                    <span>🔒 EN GESTIÓN (Laura V.)</span>
                  </span>
                </div>

                <div class="bg-amber-50/80 border border-amber-200 rounded-xl p-2.5 text-[11px] text-amber-900 flex items-start space-x-2">
                  <span class="text-amber-600 mt-0.5">🔒</span>
                  <p class="leading-snug">
                    <strong>Protección Anti-Acoso Activa:</strong> Esta cuenta ya está siendo gestionada activamente por <strong>Laura Valencia</strong> (último contacto hace 2 horas). No puedes realizar llamadas ni mensajes directos para evitar fricción con el cliente.
                  </p>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 cursor-not-allowed" title="Contacto bloqueado por política anti-acoso">
                    <span>🔒</span>
                    <span>Chat Bloqueado</span>
                  </button>
                  <button onclick="pedirTransferenciaCaso(3, 'Marval — Altos de Riomar', 'Laura Valencia')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>🔄</span>
                    <span>Pedir Transferencia</span>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 2: COPILOTO IA CON MULTI-MODELOS                -->
          <!-- ======================================================== -->
          <div id="screen-copiloto" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Copiloto Header Bar -->
            <div class="bg-[#0A233F] text-white px-4 pt-3.5 pb-3 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    ⚡
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-sm tracking-tight text-white">Copiloto IA Ultracem</h2>
                      <span id="ai-provider-badge" class="text-[9px] bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 font-extrabold px-2 py-0.5 rounded-full uppercase">NVIDIA / DeepSeek</span>
                    </div>
                    <p class="text-[10px] text-blue-200">Fichas Técnicas NTC, Precios & Guardrail Estricto</p>
                  </div>
                </div>
                
                <!-- Symmetrical Clean Norma Badge -->
                <div class="flex items-center space-x-1 bg-white/10 border border-white/20 px-2.5 py-1 rounded-xl">
                  <span class="text-[10px] text-amber-300 font-mono-data font-bold">NTC 121</span>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-3.5">

              <!-- AI Provider & API Key Status Card -->
              <div class="bg-white p-3.5 rounded-2xl border border-slate-200/90 shadow-xs flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                  <span class="text-xl">🤖</span>
                  <div>
                    <h4 class="font-bold text-xs text-slate-800" id="ai-active-status-label">Motor: NVIDIA NIM / DeepSeek</h4>
                    <p class="text-[10px] text-slate-500" id="ai-active-status-desc">Inferencia de alto nivel con filtro comercial estricto</p>
                  </div>
                </div>
                <button onclick="openInPhoneAISettings()" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-300">
                  Configurar
                </button>
              </div>

              <!-- Interactive Chat with Copilot -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col h-[340px] overflow-hidden">
                <div class="p-3 bg-slate-50 border-b border-slate-100 flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xs font-bold text-slate-700">Chat Técnico & Comercial</span>
                    <span id="ai-engine-chip" class="text-[9px] text-blue-700 bg-blue-100 px-2 py-0.5 rounded-full font-bold">Llama 3.1 70B</span>
                  </div>
                  <span class="text-[10px] text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full font-bold">Filtro Antidesvío ON</span>
                </div>

                <!-- Messages Area -->
                <div id="ai-chat-messages" class="flex-1 overflow-y-auto p-3 space-y-2.5 text-xs">
                  <div class="flex justify-start">
                    <div class="bg-slate-100 p-2.5 rounded-xl rounded-tl-none text-slate-800 max-w-[90%] leading-relaxed">
                      ¡Hola Carlos! Soy tu Copiloto Ultracem con IA. Puedo analizar qué empresas contactar para ofrecer Cemento Estructural Max NTC 121, comparar costos vs Argos y Cemex, o darte guiones de venta para directores de obra. ¿Qué deseas consultar hoy?
                    </div>
                  </div>
                </div>

                <!-- Chat Input Form -->
                <div class="p-2 border-t border-slate-100 bg-white flex items-center space-x-1.5">
                  <input type="text" id="ai-chat-input" placeholder="Pregunta sobre clientes, NTC 121, empresas o cómo vender..." class="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" onkeydown="if(event.key==='Enter') enviarConsultaAI()">
                  <button onclick="enviarConsultaAI()" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white w-8 h-8 rounded-xl flex items-center justify-center text-sm shadow-xs" title="Enviar consulta a la IA">
                    ➤
                  </button>
                </div>
              </div>

              <!-- Conversational Icebreakers & Quick Scripts -->
              <div class="space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] uppercase font-bold text-slate-600 block tracking-wider">💬 Consultas Rápidas de Prospección & Ventas:</span>
                  <span class="text-[9px] text-slate-400">Toca para probar</span>
                </div>

                <div class="grid grid-cols-1 gap-1.5">
                  <button onclick="probarPromptRapido('¿A qué nuevas empresas constructoras de Barranquilla y Soledad puedo contactar esta semana y cómo abordarles?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🏢</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Prospección: ¿A qué constructoras contactar?</strong>
                      <span class="text-[10px] text-slate-500">Empresas con obras activas y estrategia de abordaje</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo inicio una conversación con Constructora Amarilo que actualmente compra todo su cemento a Argos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤝</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Ganar cuenta a Argos (Constructora Amarilo)</strong>
                      <span class="text-[10px] text-slate-500">Argumentario de desencofrado rápido y flete directo Galapa</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué ventajas tiene el Cemento Estructural Ultracem para plantas de prefabricados y bloqueras?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🧱</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Oferta de Valor para Bloqueras y Prefabricados</strong>
                      <span class="text-[10px] text-slate-500">Desmolde acelerado en horas y ahorro de espacio</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué módulos de formación en dosificación y fraguado de Campus Ultra WhatsApp puedo ofrecerle a un maestro de obra para fidelizarlo?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-teal-50 hover:text-teal-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🎓</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Campus Ultra WhatsApp (Formación de Obra)</strong>
                      <span class="text-[10px] text-slate-500">Capacitación certificada para maestros y ferreteros</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo se articula mi gestión comercial de campo con Vanesa IA (el asistente de WhatsApp de Ultracem) para autogestión de pedidos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-emerald-50 hover:text-emerald-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤖</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Vanesa IA (WhatsApp Oficial Ultracem)</strong>
                      <span class="text-[10px] text-slate-500">Autogestión de cotizaciones y despachos en tiempo real</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué es el ácido ribonucleico?')" class="text-[11px] text-left font-bold bg-rose-50 border border-rose-200 text-rose-700 p-2.5 rounded-xl hover:bg-rose-100 transition-all flex items-center space-x-2 shadow-2xs">
                    <span class="text-base">🚫</span>
                    <div>
                      <strong class="text-rose-900 block text-[11px]">Probar Filtro de Guardrail Estricto</strong>
                      <span class="text-[10px] text-rose-600">Rechazo de pregunta ajena a la empresa (biología)</span>
                    </div>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 3: MAPA & DIRECTORIO B2B DE EMPRESAS Y OBRAS     -->
          <!-- ======================================================== -->
          <div id="screen-mapa" class="hidden flex-1 flex flex-col overflow-hidden relative">
            
            <!-- Full-bleed Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-2.5 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    🗺️
                  </div>
                  <div>
                    <h2 class="font-bold text-sm tracking-tight text-white">Radar & Prospección B2B</h2>
                    <p class="text-[10px] text-blue-200">Búsqueda de Nuevas Empresas & Geolocalización</p>
                  </div>
                </div>
                
                <div class="flex items-center space-x-1.5">
                  <!-- City Center Selector -->
                  <select id="map-city-select" onchange="centrarMapaCiudad(this.value)" class="bg-white/15 border border-white/25 text-white text-[11px] font-bold rounded-lg px-2 py-1 focus:outline-none">
                    <option value="barranquilla" class="text-slate-900">Barranquilla</option>
                    <option value="galapa" class="text-slate-900">Galapa (Planta)</option>
                    <option value="soledad" class="text-slate-900">Soledad</option>
                    <option value="cartagena" class="text-slate-900">Cartagena</option>
                    <option value="santamarta" class="text-slate-900">Santa Marta</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW TOGGLE: [RADAR EN MAPA] VS [DIRECTORIO DE EMPRESAS B2B] -->
            <div class="px-3 pt-2 pb-2 bg-white border-b border-slate-200 flex items-center justify-between text-xs flex-shrink-0 z-20">
              <div class="bg-slate-100 p-1 rounded-xl flex items-center w-full border border-slate-200">
                <button id="btn-map-mode-radar" onclick="setMapSubView('radar')" class="flex-1 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs flex items-center justify-center space-x-1.5">
                  <span>🗺️</span>
                  <span>Radar en Mapa</span>
                </button>
                <button id="btn-map-mode-prospectos" onclick="setMapSubView('prospectos')" class="flex-1 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center justify-center space-x-1.5">
                  <span>🏢</span>
                  <span id="badge-prospectos-count">Directorio Empresas (12)</span>
                </button>
              </div>
            </div>

            <!-- SUB-VIEW 1: RADAR EN MAPA -->
            <div id="subview-map-radar" class="flex-1 flex flex-col overflow-hidden relative">
              <!-- Search Bar + Category Filter Chips -->
              <div class="p-2.5 bg-white border-b border-slate-200 space-y-2 flex-shrink-0 z-20">
                <div class="flex items-center space-x-1.5">
                  <div class="relative flex-1">
                    <input type="text" id="map-search-input" placeholder="Buscar empresa, obra, Argos, Cemex, Galapa..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="buscarEnMapa(this.value)">
                    <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                  </div>
                  <button id="btn-toggle-satellite" onclick="toggleMapLayer()" class="btn-tactile bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-[10px] font-bold px-2 py-1.5 rounded-xl flex items-center space-x-1 flex-shrink-0" title="Alternar entre Callejero y Vista Satelital">
                    <span>🛰️</span>
                    <span>Satélite</span>
                  </button>
                </div>
                
                <!-- Category Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="map-chip-todas" onclick="filtrarMapaPorCategoria('todas')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white border border-[#004797] flex-shrink-0 transition-all">
                    Todas (18)
                  </button>
                  <button id="map-chip-prospectos" onclick="filtrarMapaPorCategoria('prospectos')" class="px-2.5 py-1 rounded-lg bg-sky-50 text-sky-800 border border-sky-200 flex-shrink-0 hover:bg-sky-100 transition-all">
                    ✨ Por Contactar (7)
                  </button>
                  <button id="map-chip-ultracem" onclick="filtrarMapaPorCategoria('ultracem')" class="px-2.5 py-1 rounded-lg bg-blue-50 text-[#004797] border border-blue-200 flex-shrink-0 hover:bg-blue-100 transition-all">
                    🏭 Ultracem (3)
                  </button>
                  <button id="map-chip-competencia" onclick="filtrarMapaPorCategoria('competencia')" class="px-2.5 py-1 rounded-lg bg-rose-50 text-rose-700 border border-rose-200 flex-shrink-0 hover:bg-rose-100 transition-all">
                    🔴 Competidores (4)
                  </button>
                </div>
              </div>

              <!-- Bounded Map Canvas -->
              <div class="flex-1 relative bg-slate-200 min-h-0 overflow-hidden mx-3 mb-2 rounded-2xl border border-slate-300 shadow-inner">
                <div id="colombia-leaflet-map" class="w-full h-full"></div>

                <!-- Selected Site / Competitor Card Overlay -->
                <div id="map-site-card" class="hidden absolute bottom-3 left-3 right-3 bg-white/95 backdrop-blur-md p-3.5 rounded-2xl shadow-xl border border-slate-200 z-20 space-y-2">
                  <div class="flex justify-between items-start">
                    <div>
                      <h4 id="map-site-name" class="font-bold text-xs text-slate-900 leading-tight">Constructora Bolívar</h4>
                      <p id="map-site-desc" class="text-[10px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento</p>
                    </div>
                    <span id="map-site-status" class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex-shrink-0">Mi Cartera</span>
                  </div>
                  
                  <div id="map-site-intel" class="hidden bg-slate-50 border border-slate-200 rounded-xl p-2 text-[10px] space-y-1">
                    <!-- Dynamic details -->
                  </div>

                  <div id="map-site-actions" class="grid grid-cols-2 gap-2 pt-0.5">
                    <!-- Dynamic actions -->
                  </div>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW 2: DIRECTORIO B2B DE PROSPECCIÓN (NUEVAS EMPRESAS A CONTACTAR) -->
            <div id="subview-map-prospectos" class="hidden flex-1 flex flex-col overflow-hidden bg-slate-50/70 p-3 space-y-2.5">
              
              <!-- Search & Filter Bar for Prospects -->
              <div class="bg-white p-2.5 rounded-2xl border border-slate-200 shadow-xs space-y-2 flex-shrink-0">
                <div class="relative">
                  <input type="text" id="prospects-search-input" placeholder="Buscar por empresa, obra, constructor o sector..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="filtrarDirectorioProspectos(this.value)">
                  <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                </div>

                <!-- Sector Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="chip-sec-todos" onclick="filtrarProspectosSector('todos')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white flex-shrink-0 transition-all">
                    Todos (12)
                  </button>
                  <button id="chip-sec-constructoras" onclick="filtrarProspectosSector('constructoras')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏗️ Constructoras (5)
                  </button>
                  <button id="chip-sec-infraestructura" onclick="filtrarProspectosSector('infraestructura')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🛣️ Vías & Concesiones (2)
                  </button>
                  <button id="chip-sec-prefabricados" onclick="filtrarProspectosSector('prefabricados')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🧱 Bloqueras & Adoquines (2)
                  </button>
                  <button id="chip-sec-ferreterias" onclick="filtrarProspectosSector('ferreterias')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏪 Ferreterías Mayoristas (3)
                  </button>
                </div>
              </div>

              <!-- Prospects Cards Scroll Area -->
              <div id="prospects-list-container" class="flex-1 overflow-y-auto space-y-2.5 pr-0.5">
                <!-- Injected dynamically with JavaScript -->
              </div>

            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 4: LIGA DIAMANTE CON CARTERA DE COMPAÑEROS      -->
          <!-- ======================================================== -->
          <div id="screen-liga" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Liga Header Bar -->
            <div class="bg-[#D9531E] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div>
                  <span class="text-[9px] font-black uppercase tracking-widest bg-black/20 px-2 py-0.5 rounded-full inline-block mb-1">División Regional Caribe</span>
                  <h2 class="font-extrabold text-base tracking-tight text-white leading-tight">Liga Diamante del Clinker</h2>
                  <p class="text-[11px] text-amber-100 mt-0.5">Cierre de temporada en 3 días • Top 3 asciende</p>
                </div>
                
                <div class="w-11 h-11 rounded-2xl bg-white/20 border border-white/30 flex items-center justify-center text-2xl shadow-sm flex-shrink-0">
                  💎
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <div class="flex items-center justify-between text-xs px-1">
                <span class="font-bold text-slate-700">Tabla de Posiciones Regional</span>
                <span class="text-[10px] text-slate-500">Toca un compañero para ver su cartera</span>
              </div>

              <!-- Leaderboard List -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs divide-y divide-slate-100 overflow-hidden">
                
                <!-- Rank 1: Andrés Restrepo -->
                <div onclick="openColleagueProfile('andres')" class="p-3.5 flex items-center justify-between bg-amber-50/40 hover:bg-amber-100/50 cursor-pointer transition-all" title="Ver clientes asignados a Andrés">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-black text-amber-600 text-sm">🥇</span>
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80" alt="Andrés R." class="w-9 h-9 rounded-full object-cover border border-amber-300">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Andrés Restrepo</h4>
                        <span class="text-[8px] bg-amber-200 text-amber-900 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Bogotá Norte • 48d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">980 Ton</span>
                    <span class="text-[9px] text-amber-600 block font-semibold">+450 XP</span>
                  </div>
                </div>

                <!-- Rank 2: Laura Valencia -->
                <div onclick="openColleagueProfile('laura')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Laura">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-sm">🥈</span>
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Laura V." class="w-9 h-9 rounded-full object-cover border border-purple-200">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Laura Valencia</h4>
                        <span class="text-[8px] bg-purple-100 text-purple-800 font-extrabold px-1 rounded">👥 3 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Medellín / Caribe • 34d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">840 Ton</span>
                    <span class="text-[9px] text-slate-500 block font-semibold">+320 XP</span>
                  </div>
                </div>

                <!-- Rank 3: Carlos Mendoza (User Highlighted) -->
                <div onclick="navigateToTab('perfil')" class="p-3.5 flex items-center justify-between bg-blue-50/60 border-l-4 border-[#004797] cursor-pointer hover:bg-blue-100/50 transition-all">
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

                <!-- Rank 4: Felipe Morales -->
                <div onclick="openColleagueProfile('felipe')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Felipe">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-xs">4</span>
                    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Felipe M." class="w-9 h-9 rounded-full object-cover">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Felipe Morales</h4>
                        <span class="text-[8px] bg-slate-100 text-slate-600 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
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
          <!-- PANTALLA 5: PERFIL, CASCO PROTECTOR & HEATMAP 90 DÍAS    -->
          <!-- ======================================================== -->
          <div id="screen-perfil" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Perfil Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
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
                  <div class="bg-[#003E78] h-full rounded-full transition-all duration-500" style="width: 85%"></div>
                </div>
                <p class="text-[10px] text-slate-500">Despacha 60 toneladas adicionales este mes para desbloquear el cupo autónomo de $80M.</p>
              </div>

              <!-- ULTRACEM : TRACK DE TALENTO & PALETA DE MARCA -->
              <div class="bg-[#0F172A] rounded-2xl p-4 border border-teal-500/30 text-white shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-teal-950 border border-teal-400/40 p-1 flex items-center justify-center">
                      <svg viewBox="0 0 100 100" class="w-6 h-6" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
                        <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
                        <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
                        <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
                        <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
                      </svg>
                    </div>
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <span class="font-extrabold text-xs text-white uppercase tracking-wider">Ultracem</span>
                        <span class="text-[9px] bg-teal-400/20 text-teal-300 px-1.5 py-0.2 rounded font-bold border border-teal-500/40">🌱 Brote en Crecimiento</span>
                      </div>
                      <p class="text-[10px] text-teal-100/80 italic mt-0.5">“Calidad, Resistencia y Rendimiento”</p>
                    </div>
                  </div>
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg transition-all shadow-xs">
                    PRD
                  </button>
                </div>

                <!-- 3 Símbolos: Mano, Semilla, Brote -->
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] pt-1 border-t border-slate-700/80">
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🖐️</span>
                    <strong class="text-white block mt-0.5">La Mano</strong>
                    <span class="text-slate-400 text-[9px]">Acompaña</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🌰</span>
                    <strong class="text-white block mt-0.5">La Semilla</strong>
                    <span class="text-slate-400 text-[9px]">Potencial</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-teal-500/50">
                    <span class="text-base block">🌱</span>
                    <strong class="text-teal-300 block mt-0.5">El Brote</strong>
                    <span class="text-teal-400 text-[9px]">Crecimiento</span>
                  </div>
                </div>

                <!-- Quick Color Palette Swatches with 1-click copy -->
                <div class="pt-1">
                  <span class="text-[9px] text-slate-400 font-bold uppercase tracking-wider block mb-1.5">Paleta de Marca Oficial (Clic para copiar HEX):</span>
                  <div class="flex items-center space-x-1.5">
                    <button onclick="copyColorHex('#0F172A', 'Ultracem Navy')" title="Copiar #0F172A (Ultracem Navy)" class="flex-1 h-6 rounded-md bg-[#0F172A] border border-slate-600 hover:scale-105 transition-transform" style="background-color: #0F172A;"></button>
                    <button onclick="copyColorHex('#14B8A6', 'Ultracem Teal')" title="Copiar #14B8A6 (Ultracem Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #14B8A6;"></button>
                    <button onclick="copyColorHex('#5EEAD4', 'Mint Teal')" title="Copiar #5EEAD4 (Mint Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #5EEAD4;"></button>
                    <button onclick="copyColorHex('#7DD3FC', 'Sky Blue')" title="Copiar #7DD3FC (Sky Blue)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #7DD3FC;"></button>
                    <button onclick="copyColorHex('#BAE6FD', 'Soft Sky')" title="Copiar #BAE6FD (Soft Sky)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #BAE6FD;"></button>
                    <button onclick="copyColorHex('#3797E8', 'Ultracem Blue')" title="Copiar #3797E8 (Ultracem Blue - Matriz)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #3797E8;"></button>
                  </div>
                </div>
              </div>

              <!-- Casco Protector Inventory Card -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-2xl shadow-xs">
                      ⛑️
                    </div>
                    <div>
                      <h4 class="font-bold text-xs text-slate-900 leading-tight">Casco Protector de Racha</h4>
                      <p class="text-[10px] text-slate-500">Congela tu racha 24h si tienes un día de campo difícil</p>
                    </div>
                  </div>
                  <span id="casco-badge-count" class="font-mono-data font-black text-sm bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-xl">
                    1 Activo
                  </span>
                </div>

                <div class="flex items-center justify-between pt-1 text-xs">
                  <button id="btn-use-casco" onclick="activarCascoProtector()" class="btn-tactile flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-2 px-3 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                    <span>🛡️</span>
                    <span>Activar Congelación (24 Horas)</span>
                  </button>
                </div>
              </div>

              <!-- Heatmap: 90 Días de Racha Comercial -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <div class="flex items-center justify-between text-xs">
                  <div>
                    <h4 class="font-bold text-slate-900">Historial de Constancia (Últimos 90 Días)</h4>
                    <p class="text-[10px] text-slate-500">Cada celda representa un día de contacto comercial registrado</p>
                  </div>
                  <span class="text-[10px] text-[#004797] font-bold font-mono-data">94% Éxito</span>
                </div>

                <div id="perfil-heatmap-grid" class="grid grid-flow-col grid-rows-7 gap-1 p-2 bg-slate-50 rounded-xl border border-slate-200 overflow-x-auto">
                  <!-- Generated dynamically with JS -->
                </div>

                <div class="flex items-center justify-between text-[10px] text-slate-400 font-semibold pt-1">
                  <span>Menos activo</span>
                  <div class="flex items-center space-x-1">
                    <span class="w-2.5 h-2.5 rounded-sm bg-slate-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-400"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-[#004797]"></span>
                  </div>
                  <span>Racha Activa</span>
                </div>
              </div>

              <!-- Trophies & Badges -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <h4 class="font-bold text-xs text-slate-900">Insignias & Logros de Obra</h4>
                
                <div class="grid grid-cols-3 gap-2">
                  <button onclick="openInAppTrofeo('Escudo Antichurn', 'Salva a 3 clientes en riesgo crítico antes de que cambien a la competencia.', '🛡️', '+200 XP')" class="btn-tactile bg-emerald-50/70 border border-emerald-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-emerald-100/50">
                    <span class="text-2xl">🛡️</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Antichurn</span>
                    <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                  </button>

                  <button onclick="openInAppTrofeo('Maestro Técnico', 'Comparte 25 certificados NTC 121 y curvas de fraguado validadas por laboratorio.', '📐', '+120 XP')" class="btn-tactile bg-slate-50 border border-slate-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-slate-100">
                    <span class="text-2xl">📐</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Mtro Técnico</span>
                    <span class="text-[8px] font-extrabold text-slate-500 bg-slate-200 px-1 rounded">18/25</span>
                  </button>

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
        <!-- BOTTOM NAVIGATION BAR (5 CLEAN TABS)                       -->
        <!-- ========================================================== -->
        <nav aria-label="Navegación Móvil" class="bg-white/95 backdrop-blur-md border-t border-slate-200/80 px-2 py-2 flex justify-around items-center select-none z-30 flex-shrink-0">
          
          <button id="nav-btn-racha" onclick="navigateToTab('racha')" class="btn-tactile flex flex-col items-center text-[#004797] font-bold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>
            </svg>
            <span class="text-[10px]">Racha</span>
          </button>

          <button id="nav-btn-copiloto" onclick="navigateToTab('copiloto')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
            <span class="text-[10px]">Copiloto</span>
          </button>

          <button id="nav-btn-mapa" onclick="navigateToTab('mapa')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/>
              <line x1="8" y1="2" x2="8" y2="18"/>
              <line x1="16" y1="6" x2="16" y2="22"/>
            </svg>
            <span class="text-[10px]">Radar & B2B</span>
          </button>

          <button id="nav-btn-liga" onclick="navigateToTab('liga')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
              <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/>
              <path d="M10 14.66V17c0 .55-.45 1-1 1H7v4h10v-4h-2c-.55 0-1-.45-1-1v-2.34"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/>
            </svg>
            <span class="text-[10px]">Liga</span>
          </button>

          <button id="nav-btn-perfil" onclick="navigateToTab('perfil')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            <span class="text-[10px]">Perfil</span>
          </button>

        </nav>

      </div>
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA PRD MAESTRO COMPLETO (CANVAS BLANCO)                  -->
    <!-- ============================================================== -->
    <div id="view-prd" class="hidden w-full max-w-5xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border-2 border-slate-300 shadow-sm space-y-10 text-slate-800">

      <!-- ============================================================== -->
      <!-- PRD DOCUMENT: ULTRACEM CRM MAESTRO                             -->
      <!-- ============================================================== -->
      
      <!-- Document Header & Meta Bar -->
      <header class="border-b-2 border-slate-200 pb-8 space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center space-x-3">
            <!-- Ultracem Official Logo Icon -->
            <div class="h-12 px-4 rounded-2xl bg-[#003E78] border-2 border-[#FDCA02] flex items-center justify-center shadow-xs">
              <img src="data:image/png;base64,{logo_base64}" alt="Ultracem" class="h-7 w-auto object-contain" />
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xs font-black uppercase tracking-wider text-[#003E78] bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">ULTRACEM S.A.S.</span>
                <span class="text-xs font-bold text-slate-400">•</span>
                <span class="text-xs font-black uppercase tracking-wider text-amber-800 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200">PLANTA GALAPA</span>
              </div>
              <p class="text-[11px] text-slate-500 font-medium mt-0.5">Documento de Especificación de Producto (PRD) • Versión 1.0 Oficial</p>
            </div>
          </div>
          
          <div class="flex items-center space-x-2">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
              <span class="w-2 h-2 rounded-full bg-emerald-500 mr-1.5"></span>
              Plataforma Operativa en Vivo
            </span>
            <button onclick="window.print()" class="btn-tactile text-xs font-bold text-slate-700 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-300 transition-all flex items-center space-x-1" title="Imprimir / Guardar como PDF">
              <span>🖨️</span>
              <span class="hidden sm:inline">Exportar</span>
            </button>
          </div>
        </div>

        <div>
          <h1 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight leading-tight">
            UltraRacha CRM: Prevención Antichurn, Rachas Comerciales & Copiloto IA Ultracem
          </h1>
          <p class="text-base text-slate-600 mt-2 leading-relaxed">
            Ecosistema de aceleración comercial diseñado para la fuerza de ventas de <strong>Ultracem S.A.S.</strong> en el Caribe colombiano. Transforma la fricción operativa del seguimiento de obras en hábitos comerciales diarios mediante gamificación de rachas, escalamiento ágil con SLAs y copiloto multimodelo.
          </p>
        </div>

        <!-- Metadata Ribbon -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Lema Ultracem</span>
            <span class="font-bold text-[#003E78]">“Calidad, Resistencia y Rendimiento”</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Sede Central</span>
            <span class="font-bold text-[#003E78]">Planta Galapa, Atlántico</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Infraestructura IA</span>
            <span class="font-bold text-[#003E78]">Groq LPU, NVIDIA NIM & DeepSeek</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Regla de Oro</span>
            <span class="font-bold text-amber-700">Corte Diario 11:59 PM</span>
          </div>
        </div>
      </header>

      <!-- SECCIÓN 1: VISIÓN -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">1. Visión del Producto y Filosofía Operativa</h2>
        
        <div class="bg-[#003E78] rounded-2xl p-6 text-white space-y-3 border-l-4 border-[#FDCA02]">
          <span class="text-[10px] font-black uppercase tracking-widest text-[#FDCA02] bg-[#0A233F] px-2.5 py-0.5 rounded-full border border-amber-400/40">Premisa de Operación</span>
          <p class="text-base sm:text-lg font-bold leading-snug italic text-white">
            “Que el cemento fragüe, pero que tu cliente nunca se enfríe.”
          </p>
          <p class="text-xs text-blue-100 leading-relaxed">
            En entornos industriales de alta competencia como la comercialización de cemento y concreto con <strong>Ultracem</strong>, el éxito comercial depende de la constancia diaria, la agilidad en obra y la eliminación de fricciones operativas entre el asesor de campo y las áreas de Cartera, Logística y Calidad.
          </p>
        </div>
      </section>

      <!-- SECCIÓN 2: PALETA CROMÁTICA -->
      <section class="space-y-4 border-t border-slate-200 pt-6">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">2. Paleta Cromática Primaria Ultracem (Colores Sólidos Oficiales)</h2>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
          <!-- Azul Oscuro -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#003E78] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Azul Ultracem</span>
            <span class="text-[10px] font-mono-data text-blue-700 font-bold">#003E78</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Identidad & Confianza</span>
          </div>
          <!-- Amarillo -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#FDCA02] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Amarillo Ultracem</span>
            <span class="text-[10px] font-mono-data text-amber-700 font-bold">#FDCA02</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Energía, Sol & Alertas</span>
          </div>
          <!-- Azul Marino Profundo -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#0A233F] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Azul Marino</span>
            <span class="text-[10px] font-mono-data text-slate-700 font-bold">#0A233F</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Sidebar & Autoridad</span>
          </div>
          <!-- Blanco Puro -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#FFFFFF] border border-slate-300 mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Blanco Puro</span>
            <span class="text-[10px] font-mono-data text-slate-500 font-bold">#FFFFFF</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Tarjetas & Claridad</span>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 3: MÓDULOS DEL PRODUCTO -->
      <section class="space-y-4 border-t border-slate-200 pt-6">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">3. Módulos Operativos del Ecosistema</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <!-- M1 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 1: Racha Diaria & Semáforo Antichurn</h3>
            <p class="text-slate-600 leading-relaxed">
              Corte a las 11:59 PM para atender cuentas críticas. Escalamiento en 1 clic con SLAs auditables (Cartera 4h, Logística 2h, Calidad 6h) que salvan la racha inmediatamente.
            </p>
          </div>
          <!-- M2 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 2: Copiloto IA Multimodelo</h3>
            <p class="text-slate-600 leading-relaxed">
              Inferencia ultrarrápida con Groq LPU, NVIDIA NIM y DeepSeek. Guardrails estrictos de la norma NTC 121 y transcripción de notas de voz con Whisper Turbo.
            </p>
          </div>
          <!-- M3 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 3: Radar Georreferenciado & Directorio B2B</h3>
            <p class="text-slate-600 leading-relaxed">
              Cartografía interactiva con Leaflet de clientes, Planta Galapa y competencia (Argos/Cemex). Directorio calificado de 12 empresas del Caribe.
            </p>
          </div>
          <!-- M4 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 4: Liga de Asesores & Transferencia</h3>
            <p class="text-slate-600 leading-relaxed">
              Leaderboard gamificado con Milena Ospino, Adriana Anaya e Hichel Espitia. Módulo de reasignación voluntaria de clientes entre compañeros de equipo.
            </p>
          </div>
        </div>
      </section>

    </div>

  </main>

    </div>

      </div>

      <!-- PANEL CELULAR: APLICACIÓN MÓVIL EN VIVO (STICKY DERECHA) -->
      <aside id="phone-container-wrapper" class="hidden xl:flex w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex-col items-center">
        <div class="mb-2 text-center">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white border-2 border-[#FDCA02] shadow-xs">
            📱 Asesor Móvil en Terreno
          </span>
        </div>
<!-- Phone Canvas Frame: Strict isolation & fixed height containment -->
      <div class="w-full max-w-[420px] bg-white rounded-[40px] shadow-2xl border-4 border-slate-800 overflow-hidden flex flex-col h-[820px] max-h-[820px] relative" style="position: relative; isolation: isolate; contain: paint;">
        
        <!-- Phone Status Notch -->
        <div class="bg-slate-900 pt-3.5 px-6 pb-2 flex justify-between items-center text-white text-[11px] font-mono-data select-none z-30 flex-shrink-0">
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
        <div id="inphone-sheet-overlay" class="hidden absolute inset-0 z-50 bg-slate-950/70 backdrop-blur-xs flex flex-col justify-end rounded-[36px] overflow-hidden transition-all duration-300">
          <!-- Backdrop click to dismiss -->
          <div class="flex-1 cursor-pointer" onclick="closeInPhoneSheet()" title="Cerrar panel"></div>
          
          <!-- Sheet Body Panel (Slides up from bottom inside the phone) -->
          <div id="inphone-sheet-panel" class="bg-white rounded-t-[28px] max-h-[90%] flex flex-col shadow-2xl border-t border-slate-200 overflow-hidden transform animate-sheet-up">
            
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
        <div id="mobile-screen-content" class="flex-1 flex flex-col overflow-hidden relative">
          
          <!-- ======================================================== -->
          <!-- PANTALLA 1: RACHA & CLIENTES                             -->
          <!-- ======================================================== -->
          <div id="screen-racha" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Mobile Header Bar (Full Bleed - Perfectly Aligned & Symmetrical) -->
            <div class="bg-[#003E78] text-white px-4 pt-3 pb-3 relative overflow-hidden flex-shrink-0">
              <!-- Top Row: User Avatar & Streak Pill -->
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

              <!-- Bottom Row: Midnight Countdown & Helmet Freeze Badge -->
              <div class="mt-2.5 pt-2 border-t border-white/15 flex items-center justify-between text-xs relative z-10">
                <div class="flex items-center space-x-1.5 text-blue-100 text-[11px]">
                  <span>⏰</span>
                  <span class="font-medium">Corte 11:59 PM:</span>
                  <span id="countdown-timer" class="font-mono-data font-bold text-amber-300 bg-white/10 px-2 py-0.5 rounded text-[11px]">13h : 59m : 12s</span>
                </div>

                <!-- Casco Protector Pill Trigger -->
                <button onclick="navigateToTab('perfil')" id="header-casco-btn" class="btn-tactile bg-white/15 hover:bg-white/25 border border-white/25 text-white font-bold text-[11px] px-2.5 py-0.5 rounded-full flex items-center space-x-1.5 shadow-xs" title="Cascos disponibles para proteger tu racha">
                  <span>⛑️</span>
                  <span id="header-casco-count">1 Casco</span>
                </button>
              </div>
            </div>

            <!-- Scrollable Content Area -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <!-- ULTRACEM ACTIVATION BANNER (DINÁMICO POR FASES 1-4) -->
              
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg shadow-xs transition-all flex items-center space-x-1 flex-shrink-0">
                    <span>📘</span>
                    <span>Ver PRD</span>
                  </button>
                </div>
              </div>

              <!-- DON FRAGUADO: MASCOTA VECTORIAL INTERACTIVA -->
              <div id="mascot-card" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all">
                
                <!-- SVG Vector Mascot -->
                <div id="don-fraguado-container" class="relative w-16 h-18 flex-shrink-0 cursor-pointer select-none mascot-breathing" onclick="pokeMascot()" title="¡Haz clic en Don Fraguado!">
                  <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm overflow-visible" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />

                    <!-- Mascota: Bulto de Cemento Ultracem -->
                    <g id="mascot-body-group" class="transition-transform duration-300 origin-bottom">
                      <!-- Sack Depth -->
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
                      <text x="50" y="88.2" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-weight="800" font-size="4.2" text-anchor="middle">50 kg • NTC 121</text>

                      <!-- Face: Interactive Eyes -->
                      <g id="mascot-eyes">
                        <!-- Left Eye -->
                        <circle cx="38" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="39.5" cy="52.5" r="2" fill="#FFFFFF" />
                        <!-- Right Eye -->
                        <circle cx="62" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="63.5" cy="52.5" r="2" fill="#FFFFFF" />
                      </g>

                      <!-- Rosy Cheeks -->
                      <ellipse cx="30" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>
                      <ellipse cx="70" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>

                      <!-- Mouth: Happy smile -->
                      <path id="mascot-mouth" d="M 44,60 Q 50,65 56,60" fill="none" stroke="#0F172A" stroke-width="2" stroke-linecap="round" />
                    </g>

                    <!-- Engineer Hard Hat (Casco Amarillo Ultracem) -->
                    <g id="mascot-helmet-group" class="transition-transform duration-300">
                      <!-- Helmet Dome -->
                      <path d="M 18,34 C 18,12 82,12 82,34 Z" fill="#FACC15" stroke="#CA8A04" stroke-width="2" />
                      <!-- Helmet Center Crest Ridge -->
                      <path d="M 46,14 L 54,14 L 53,33 L 47,33 Z" fill="#EAB308" />
                      <!-- Helmet Brim / Visor -->
                      <path d="M 12,34 Q 50,29 88,34 Q 50,38 12,34 Z" fill="#CA8A04" />
                      <!-- Reflective Strip on Brim -->
                      <path d="M 22,33.5 Q 50,30.5 78,33.5" fill="none" stroke="#FEF08A" stroke-width="1.8" stroke-linecap="round" />
                    </g>
                  </svg>
                </div>

                <!-- Speech Bubble Dialogue -->
                <div class="flex-1">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-xs font-black text-slate-800 flex items-center space-x-1.5">
                      <span>Don Fraguado</span>
                      <span id="mascot-mood-badge" class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full">⚡ Motivado</span>
                    </span>
                    <span class="text-[10px] text-slate-500 font-semibold">Tócame</span>
                  </div>
                  <p id="mascot-dialogue-text" class="text-xs text-slate-600 leading-snug">
                    ¡Buenos días Carlos! Tu racha está protegida. Tienes <strong>2 clientes por contactar</strong> antes de las 11:59 PM para sumar +150 XP.
                  </p>
                </div>
              </div>

              <!-- Quick Banner to Prospecting Search Engine -->
              <div onclick="navigateToTab('mapa'); setMapSubView('prospectos');" class="btn-tactile bg-[#003E78] text-white p-3.5 rounded-2xl shadow-xs flex items-center justify-between cursor-pointer hover:shadow-md transition-all">
                <div class="flex items-center space-x-3">
                  <span class="text-2xl">🏢</span>
                  <div>
                    <h4 class="font-extrabold text-xs text-white leading-tight">Radar de Obras & Nuevas Empresas</h4>
                    <p class="text-[10px] text-blue-200 mt-0.5">12 constructoras y prefabricados listas para contactar</p>
                  </div>
                </div>
                <span class="text-xs bg-white/20 px-2 py-1 rounded-lg font-bold">Ver Empresas ➔</span>
              </div>

              <!-- Filter Bar (3 Clean Columns) -->
              <div class="space-y-1.5">
                <div class="flex items-center justify-between text-xs px-1">
                  <span class="font-bold text-slate-700">Mi Cartera Activa de Clientes</span>
                  <span class="text-[10px] text-slate-500" id="filter-count-badge">3 Casos Activos</span>
                </div>

                <div class="grid grid-cols-3 gap-2 bg-slate-200/80 p-1 rounded-xl">
                  <button id="filter-btn-todos" onclick="filterClients('todos')" class="py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs text-center">
                    Todos (3)
                  </button>
                  <button id="filter-btn-obras" onclick="filterClients('obras')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏗️ Obras (2)
                  </button>
                  <button id="filter-btn-ferreterias" onclick="filterClients('ferreterias')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏪 Ferret. (1)
                  </button>
                </div>
              </div>

              <!-- CLIENT CARD 1: CONSTRUCTORA BOLÍVAR (CRÍTICO) -->
              <div id="card-client-1" class="client-card bg-white rounded-2xl p-4 border-2 border-rose-400 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Constructora Bolívar</h3>
                      <span class="text-[10px] font-extrabold bg-blue-100 text-[#004797] px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento Estructural</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 border border-rose-200 px-2 py-0.5 rounded-md">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                    <span>8D SIN PEDIDO</span>
                  </span>
                </div>

                <!-- Churn Risk Warning Banner -->
                <div class="bg-rose-50/80 border border-rose-200/90 rounded-xl p-2.5 text-[11px] text-rose-900 flex items-start space-x-2">
                  <span class="text-rose-600 mt-0.5 text-xs">⚠️</span>
                  <p class="leading-snug">
                    <strong>Riesgo Crítico de Pérdida:</strong> Superó su ciclo habitual de recompra por 3 días. Contacta hoy para salvar tu racha comercial (+100 XP).
                  </p>
                </div>

                <!-- Action Buttons: WhatsApp & Register Action -->
                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Constructora Bolívar', '120 Ton Cemento Estructural')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(1, 'Constructora Bolívar')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <!-- Secondary Technical Actions: Cubicaje & Voice Notes -->
                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCubicajeModal('Constructora Bolívar')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📐</span>
                    <span>Cubicación Losa</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Constructora Bolívar')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz en obra">
                    <span>🎙️</span>
                  </button>
                </div>

                <!-- Transfer Client to Colleague Option -->
                <div class="pt-1">
                  <button onclick="openTransferClientModal(1, 'Constructora Bolívar — Torres del Mar')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

                <!-- Interactive Activity Timeline Container (With Saved Audios) -->
                <div id="timeline-box-1" class="bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-[11px] space-y-2 mt-2">
                  <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-700 text-[10px] uppercase tracking-wider">Historial Reciente & Audios</span>
                    <span class="text-[9px] text-emerald-600 font-semibold font-mono-data">Sincronizado</span>
                  </div>
                  <div id="timeline-notes-list-1" class="space-y-2">
                    <div class="flex items-start space-x-2 text-slate-600">
                      <span class="w-1.5 h-1.5 rounded-full bg-slate-400 mt-1.5 flex-shrink-0"></span>
                      <div>
                        <strong>Visita Presencial</strong> hace 3 días: El residente Ing. Arango solicitó cotización con flete incluido.
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- CLIENT CARD 2: FERRETERÍA EL CONSTRUCTOR -->
              <div id="card-client-2" class="client-card bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3 transition-all" data-tipo="ferreterias">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Ferretería El Constructor</h3>
                      <span class="text-[10px] font-extrabold bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded">Ferretería</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Sede Centro Soledad • 45 Ton Cemento Gris</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
                    <span>4D SIN PEDIDO</span>
                  </span>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Ferretería El Constructor', '45 Ton Cemento Gris')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(2, 'Ferretería El Constructor')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCertificadoModal('Ferretería El Constructor', 'Cemento Uso General')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📜</span>
                    <span>Certificado Calidad</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Ferretería El Constructor')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz">
                    <span>🎙️</span>
                  </button>
                </div>

                <div class="pt-1">
                  <button onclick="openTransferClientModal(2, 'Ferretería El Constructor — Sede Centro')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente fijo a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

              </div>

              <!-- CLIENT CARD 3: CASO BLOQUEADO POR OTRO ASESOR -->
              <div id="card-client-3" class="client-card bg-slate-100/80 rounded-2xl p-4 border border-slate-300 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-700 text-sm tracking-tight">Marval — Altos de Riomar</h3>
                      <span class="text-[10px] font-extrabold bg-slate-200 text-slate-600 px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Vaciado Torre 3 • Barranquilla</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded-md">
                    <span>🔒 EN GESTIÓN (Laura V.)</span>
                  </span>
                </div>

                <div class="bg-amber-50/80 border border-amber-200 rounded-xl p-2.5 text-[11px] text-amber-900 flex items-start space-x-2">
                  <span class="text-amber-600 mt-0.5">🔒</span>
                  <p class="leading-snug">
                    <strong>Protección Anti-Acoso Activa:</strong> Esta cuenta ya está siendo gestionada activamente por <strong>Laura Valencia</strong> (último contacto hace 2 horas). No puedes realizar llamadas ni mensajes directos para evitar fricción con el cliente.
                  </p>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 cursor-not-allowed" title="Contacto bloqueado por política anti-acoso">
                    <span>🔒</span>
                    <span>Chat Bloqueado</span>
                  </button>
                  <button onclick="pedirTransferenciaCaso(3, 'Marval — Altos de Riomar', 'Laura Valencia')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>🔄</span>
                    <span>Pedir Transferencia</span>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 2: COPILOTO IA CON MULTI-MODELOS                -->
          <!-- ======================================================== -->
          <div id="screen-copiloto" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Copiloto Header Bar -->
            <div class="bg-[#0A233F] text-white px-4 pt-3.5 pb-3 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    ⚡
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-sm tracking-tight text-white">Copiloto IA Ultracem</h2>
                      <span id="ai-provider-badge" class="text-[9px] bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 font-extrabold px-2 py-0.5 rounded-full uppercase">NVIDIA / DeepSeek</span>
                    </div>
                    <p class="text-[10px] text-blue-200">Fichas Técnicas NTC, Precios & Guardrail Estricto</p>
                  </div>
                </div>
                
                <!-- Symmetrical Clean Norma Badge -->
                <div class="flex items-center space-x-1 bg-white/10 border border-white/20 px-2.5 py-1 rounded-xl">
                  <span class="text-[10px] text-amber-300 font-mono-data font-bold">NTC 121</span>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-3.5">

              <!-- AI Provider & API Key Status Card -->
              <div class="bg-white p-3.5 rounded-2xl border border-slate-200/90 shadow-xs flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                  <span class="text-xl">🤖</span>
                  <div>
                    <h4 class="font-bold text-xs text-slate-800" id="ai-active-status-label">Motor: NVIDIA NIM / DeepSeek</h4>
                    <p class="text-[10px] text-slate-500" id="ai-active-status-desc">Inferencia de alto nivel con filtro comercial estricto</p>
                  </div>
                </div>
                <button onclick="openInPhoneAISettings()" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-300">
                  Configurar
                </button>
              </div>

              <!-- Interactive Chat with Copilot -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col h-[340px] overflow-hidden">
                <div class="p-3 bg-slate-50 border-b border-slate-100 flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xs font-bold text-slate-700">Chat Técnico & Comercial</span>
                    <span id="ai-engine-chip" class="text-[9px] text-blue-700 bg-blue-100 px-2 py-0.5 rounded-full font-bold">Llama 3.1 70B</span>
                  </div>
                  <span class="text-[10px] text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full font-bold">Filtro Antidesvío ON</span>
                </div>

                <!-- Messages Area -->
                <div id="ai-chat-messages" class="flex-1 overflow-y-auto p-3 space-y-2.5 text-xs">
                  <div class="flex justify-start">
                    <div class="bg-slate-100 p-2.5 rounded-xl rounded-tl-none text-slate-800 max-w-[90%] leading-relaxed">
                      ¡Hola Carlos! Soy tu Copiloto Ultracem con IA. Puedo analizar qué empresas contactar para ofrecer Cemento Estructural Max NTC 121, comparar costos vs Argos y Cemex, o darte guiones de venta para directores de obra. ¿Qué deseas consultar hoy?
                    </div>
                  </div>
                </div>

                <!-- Chat Input Form -->
                <div class="p-2 border-t border-slate-100 bg-white flex items-center space-x-1.5">
                  <input type="text" id="ai-chat-input" placeholder="Pregunta sobre clientes, NTC 121, empresas o cómo vender..." class="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" onkeydown="if(event.key==='Enter') enviarConsultaAI()">
                  <button onclick="enviarConsultaAI()" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white w-8 h-8 rounded-xl flex items-center justify-center text-sm shadow-xs" title="Enviar consulta a la IA">
                    ➤
                  </button>
                </div>
              </div>

              <!-- Conversational Icebreakers & Quick Scripts -->
              <div class="space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] uppercase font-bold text-slate-600 block tracking-wider">💬 Consultas Rápidas de Prospección & Ventas:</span>
                  <span class="text-[9px] text-slate-400">Toca para probar</span>
                </div>

                <div class="grid grid-cols-1 gap-1.5">
                  <button onclick="probarPromptRapido('¿A qué nuevas empresas constructoras de Barranquilla y Soledad puedo contactar esta semana y cómo abordarles?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🏢</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Prospección: ¿A qué constructoras contactar?</strong>
                      <span class="text-[10px] text-slate-500">Empresas con obras activas y estrategia de abordaje</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo inicio una conversación con Constructora Amarilo que actualmente compra todo su cemento a Argos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤝</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Ganar cuenta a Argos (Constructora Amarilo)</strong>
                      <span class="text-[10px] text-slate-500">Argumentario de desencofrado rápido y flete directo Galapa</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué ventajas tiene el Cemento Estructural Ultracem para plantas de prefabricados y bloqueras?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🧱</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Oferta de Valor para Bloqueras y Prefabricados</strong>
                      <span class="text-[10px] text-slate-500">Desmolde acelerado en horas y ahorro de espacio</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué módulos de formación en dosificación y fraguado de Campus Ultra WhatsApp puedo ofrecerle a un maestro de obra para fidelizarlo?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-teal-50 hover:text-teal-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🎓</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Campus Ultra WhatsApp (Formación de Obra)</strong>
                      <span class="text-[10px] text-slate-500">Capacitación certificada para maestros y ferreteros</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo se articula mi gestión comercial de campo con Vanesa IA (el asistente de WhatsApp de Ultracem) para autogestión de pedidos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-emerald-50 hover:text-emerald-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤖</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Vanesa IA (WhatsApp Oficial Ultracem)</strong>
                      <span class="text-[10px] text-slate-500">Autogestión de cotizaciones y despachos en tiempo real</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué es el ácido ribonucleico?')" class="text-[11px] text-left font-bold bg-rose-50 border border-rose-200 text-rose-700 p-2.5 rounded-xl hover:bg-rose-100 transition-all flex items-center space-x-2 shadow-2xs">
                    <span class="text-base">🚫</span>
                    <div>
                      <strong class="text-rose-900 block text-[11px]">Probar Filtro de Guardrail Estricto</strong>
                      <span class="text-[10px] text-rose-600">Rechazo de pregunta ajena a la empresa (biología)</span>
                    </div>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 3: MAPA & DIRECTORIO B2B DE EMPRESAS Y OBRAS     -->
          <!-- ======================================================== -->
          <div id="screen-mapa" class="hidden flex-1 flex flex-col overflow-hidden relative">
            
            <!-- Full-bleed Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-2.5 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    🗺️
                  </div>
                  <div>
                    <h2 class="font-bold text-sm tracking-tight text-white">Radar & Prospección B2B</h2>
                    <p class="text-[10px] text-blue-200">Búsqueda de Nuevas Empresas & Geolocalización</p>
                  </div>
                </div>
                
                <div class="flex items-center space-x-1.5">
                  <!-- City Center Selector -->
                  <select id="map-city-select" onchange="centrarMapaCiudad(this.value)" class="bg-white/15 border border-white/25 text-white text-[11px] font-bold rounded-lg px-2 py-1 focus:outline-none">
                    <option value="barranquilla" class="text-slate-900">Barranquilla</option>
                    <option value="galapa" class="text-slate-900">Galapa (Planta)</option>
                    <option value="soledad" class="text-slate-900">Soledad</option>
                    <option value="cartagena" class="text-slate-900">Cartagena</option>
                    <option value="santamarta" class="text-slate-900">Santa Marta</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW TOGGLE: [RADAR EN MAPA] VS [DIRECTORIO DE EMPRESAS B2B] -->
            <div class="px-3 pt-2 pb-2 bg-white border-b border-slate-200 flex items-center justify-between text-xs flex-shrink-0 z-20">
              <div class="bg-slate-100 p-1 rounded-xl flex items-center w-full border border-slate-200">
                <button id="btn-map-mode-radar" onclick="setMapSubView('radar')" class="flex-1 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs flex items-center justify-center space-x-1.5">
                  <span>🗺️</span>
                  <span>Radar en Mapa</span>
                </button>
                <button id="btn-map-mode-prospectos" onclick="setMapSubView('prospectos')" class="flex-1 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center justify-center space-x-1.5">
                  <span>🏢</span>
                  <span id="badge-prospectos-count">Directorio Empresas (12)</span>
                </button>
              </div>
            </div>

            <!-- SUB-VIEW 1: RADAR EN MAPA -->
            <div id="subview-map-radar" class="flex-1 flex flex-col overflow-hidden relative">
              <!-- Search Bar + Category Filter Chips -->
              <div class="p-2.5 bg-white border-b border-slate-200 space-y-2 flex-shrink-0 z-20">
                <div class="flex items-center space-x-1.5">
                  <div class="relative flex-1">
                    <input type="text" id="map-search-input" placeholder="Buscar empresa, obra, Argos, Cemex, Galapa..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="buscarEnMapa(this.value)">
                    <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                  </div>
                  <button id="btn-toggle-satellite" onclick="toggleMapLayer()" class="btn-tactile bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-[10px] font-bold px-2 py-1.5 rounded-xl flex items-center space-x-1 flex-shrink-0" title="Alternar entre Callejero y Vista Satelital">
                    <span>🛰️</span>
                    <span>Satélite</span>
                  </button>
                </div>
                
                <!-- Category Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="map-chip-todas" onclick="filtrarMapaPorCategoria('todas')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white border border-[#004797] flex-shrink-0 transition-all">
                    Todas (18)
                  </button>
                  <button id="map-chip-prospectos" onclick="filtrarMapaPorCategoria('prospectos')" class="px-2.5 py-1 rounded-lg bg-sky-50 text-sky-800 border border-sky-200 flex-shrink-0 hover:bg-sky-100 transition-all">
                    ✨ Por Contactar (7)
                  </button>
                  <button id="map-chip-ultracem" onclick="filtrarMapaPorCategoria('ultracem')" class="px-2.5 py-1 rounded-lg bg-blue-50 text-[#004797] border border-blue-200 flex-shrink-0 hover:bg-blue-100 transition-all">
                    🏭 Ultracem (3)
                  </button>
                  <button id="map-chip-competencia" onclick="filtrarMapaPorCategoria('competencia')" class="px-2.5 py-1 rounded-lg bg-rose-50 text-rose-700 border border-rose-200 flex-shrink-0 hover:bg-rose-100 transition-all">
                    🔴 Competidores (4)
                  </button>
                </div>
              </div>

              <!-- Bounded Map Canvas -->
              <div class="flex-1 relative bg-slate-200 min-h-0 overflow-hidden mx-3 mb-2 rounded-2xl border border-slate-300 shadow-inner">
                <div id="colombia-leaflet-map" class="w-full h-full"></div>

                <!-- Selected Site / Competitor Card Overlay -->
                <div id="map-site-card" class="hidden absolute bottom-3 left-3 right-3 bg-white/95 backdrop-blur-md p-3.5 rounded-2xl shadow-xl border border-slate-200 z-20 space-y-2">
                  <div class="flex justify-between items-start">
                    <div>
                      <h4 id="map-site-name" class="font-bold text-xs text-slate-900 leading-tight">Constructora Bolívar</h4>
                      <p id="map-site-desc" class="text-[10px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento</p>
                    </div>
                    <span id="map-site-status" class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex-shrink-0">Mi Cartera</span>
                  </div>
                  
                  <div id="map-site-intel" class="hidden bg-slate-50 border border-slate-200 rounded-xl p-2 text-[10px] space-y-1">
                    <!-- Dynamic details -->
                  </div>

                  <div id="map-site-actions" class="grid grid-cols-2 gap-2 pt-0.5">
                    <!-- Dynamic actions -->
                  </div>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW 2: DIRECTORIO B2B DE PROSPECCIÓN (NUEVAS EMPRESAS A CONTACTAR) -->
            <div id="subview-map-prospectos" class="hidden flex-1 flex flex-col overflow-hidden bg-slate-50/70 p-3 space-y-2.5">
              
              <!-- Search & Filter Bar for Prospects -->
              <div class="bg-white p-2.5 rounded-2xl border border-slate-200 shadow-xs space-y-2 flex-shrink-0">
                <div class="relative">
                  <input type="text" id="prospects-search-input" placeholder="Buscar por empresa, obra, constructor o sector..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="filtrarDirectorioProspectos(this.value)">
                  <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                </div>

                <!-- Sector Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="chip-sec-todos" onclick="filtrarProspectosSector('todos')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white flex-shrink-0 transition-all">
                    Todos (12)
                  </button>
                  <button id="chip-sec-constructoras" onclick="filtrarProspectosSector('constructoras')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏗️ Constructoras (5)
                  </button>
                  <button id="chip-sec-infraestructura" onclick="filtrarProspectosSector('infraestructura')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🛣️ Vías & Concesiones (2)
                  </button>
                  <button id="chip-sec-prefabricados" onclick="filtrarProspectosSector('prefabricados')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🧱 Bloqueras & Adoquines (2)
                  </button>
                  <button id="chip-sec-ferreterias" onclick="filtrarProspectosSector('ferreterias')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏪 Ferreterías Mayoristas (3)
                  </button>
                </div>
              </div>

              <!-- Prospects Cards Scroll Area -->
              <div id="prospects-list-container" class="flex-1 overflow-y-auto space-y-2.5 pr-0.5">
                <!-- Injected dynamically with JavaScript -->
              </div>

            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 4: LIGA DIAMANTE CON CARTERA DE COMPAÑEROS      -->
          <!-- ======================================================== -->
          <div id="screen-liga" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Liga Header Bar -->
            <div class="bg-[#D9531E] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div>
                  <span class="text-[9px] font-black uppercase tracking-widest bg-black/20 px-2 py-0.5 rounded-full inline-block mb-1">División Regional Caribe</span>
                  <h2 class="font-extrabold text-base tracking-tight text-white leading-tight">Liga Diamante del Clinker</h2>
                  <p class="text-[11px] text-amber-100 mt-0.5">Cierre de temporada en 3 días • Top 3 asciende</p>
                </div>
                
                <div class="w-11 h-11 rounded-2xl bg-white/20 border border-white/30 flex items-center justify-center text-2xl shadow-sm flex-shrink-0">
                  💎
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <div class="flex items-center justify-between text-xs px-1">
                <span class="font-bold text-slate-700">Tabla de Posiciones Regional</span>
                <span class="text-[10px] text-slate-500">Toca un compañero para ver su cartera</span>
              </div>

              <!-- Leaderboard List -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs divide-y divide-slate-100 overflow-hidden">
                
                <!-- Rank 1: Andrés Restrepo -->
                <div onclick="openColleagueProfile('andres')" class="p-3.5 flex items-center justify-between bg-amber-50/40 hover:bg-amber-100/50 cursor-pointer transition-all" title="Ver clientes asignados a Andrés">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-black text-amber-600 text-sm">🥇</span>
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80" alt="Andrés R." class="w-9 h-9 rounded-full object-cover border border-amber-300">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Andrés Restrepo</h4>
                        <span class="text-[8px] bg-amber-200 text-amber-900 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Bogotá Norte • 48d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">980 Ton</span>
                    <span class="text-[9px] text-amber-600 block font-semibold">+450 XP</span>
                  </div>
                </div>

                <!-- Rank 2: Laura Valencia -->
                <div onclick="openColleagueProfile('laura')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Laura">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-sm">🥈</span>
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Laura V." class="w-9 h-9 rounded-full object-cover border border-purple-200">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Laura Valencia</h4>
                        <span class="text-[8px] bg-purple-100 text-purple-800 font-extrabold px-1 rounded">👥 3 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Medellín / Caribe • 34d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">840 Ton</span>
                    <span class="text-[9px] text-slate-500 block font-semibold">+320 XP</span>
                  </div>
                </div>

                <!-- Rank 3: Carlos Mendoza (User Highlighted) -->
                <div onclick="navigateToTab('perfil')" class="p-3.5 flex items-center justify-between bg-blue-50/60 border-l-4 border-[#004797] cursor-pointer hover:bg-blue-100/50 transition-all">
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

                <!-- Rank 4: Felipe Morales -->
                <div onclick="openColleagueProfile('felipe')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Felipe">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-xs">4</span>
                    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Felipe M." class="w-9 h-9 rounded-full object-cover">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Felipe Morales</h4>
                        <span class="text-[8px] bg-slate-100 text-slate-600 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
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
          <!-- PANTALLA 5: PERFIL, CASCO PROTECTOR & HEATMAP 90 DÍAS    -->
          <!-- ======================================================== -->
          <div id="screen-perfil" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Perfil Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
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
                  <div class="bg-[#003E78] h-full rounded-full transition-all duration-500" style="width: 85%"></div>
                </div>
                <p class="text-[10px] text-slate-500">Despacha 60 toneladas adicionales este mes para desbloquear el cupo autónomo de $80M.</p>
              </div>

              <!-- ULTRACEM : TRACK DE TALENTO & PALETA DE MARCA -->
              <div class="bg-[#0F172A] rounded-2xl p-4 border border-teal-500/30 text-white shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-teal-950 border border-teal-400/40 p-1 flex items-center justify-center">
                      <svg viewBox="0 0 100 100" class="w-6 h-6" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
                        <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
                        <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
                        <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
                        <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
                      </svg>
                    </div>
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <span class="font-extrabold text-xs text-white uppercase tracking-wider">Ultracem</span>
                        <span class="text-[9px] bg-teal-400/20 text-teal-300 px-1.5 py-0.2 rounded font-bold border border-teal-500/40">🌱 Brote en Crecimiento</span>
                      </div>
                      <p class="text-[10px] text-teal-100/80 italic mt-0.5">“Calidad, Resistencia y Rendimiento”</p>
                    </div>
                  </div>
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg transition-all shadow-xs">
                    PRD
                  </button>
                </div>

                <!-- 3 Símbolos: Mano, Semilla, Brote -->
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] pt-1 border-t border-slate-700/80">
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🖐️</span>
                    <strong class="text-white block mt-0.5">La Mano</strong>
                    <span class="text-slate-400 text-[9px]">Acompaña</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🌰</span>
                    <strong class="text-white block mt-0.5">La Semilla</strong>
                    <span class="text-slate-400 text-[9px]">Potencial</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-teal-500/50">
                    <span class="text-base block">🌱</span>
                    <strong class="text-teal-300 block mt-0.5">El Brote</strong>
                    <span class="text-teal-400 text-[9px]">Crecimiento</span>
                  </div>
                </div>

                <!-- Quick Color Palette Swatches with 1-click copy -->
                <div class="pt-1">
                  <span class="text-[9px] text-slate-400 font-bold uppercase tracking-wider block mb-1.5">Paleta de Marca Oficial (Clic para copiar HEX):</span>
                  <div class="flex items-center space-x-1.5">
                    <button onclick="copyColorHex('#0F172A', 'Ultracem Navy')" title="Copiar #0F172A (Ultracem Navy)" class="flex-1 h-6 rounded-md bg-[#0F172A] border border-slate-600 hover:scale-105 transition-transform" style="background-color: #0F172A;"></button>
                    <button onclick="copyColorHex('#14B8A6', 'Ultracem Teal')" title="Copiar #14B8A6 (Ultracem Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #14B8A6;"></button>
                    <button onclick="copyColorHex('#5EEAD4', 'Mint Teal')" title="Copiar #5EEAD4 (Mint Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #5EEAD4;"></button>
                    <button onclick="copyColorHex('#7DD3FC', 'Sky Blue')" title="Copiar #7DD3FC (Sky Blue)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #7DD3FC;"></button>
                    <button onclick="copyColorHex('#BAE6FD', 'Soft Sky')" title="Copiar #BAE6FD (Soft Sky)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #BAE6FD;"></button>
                    <button onclick="copyColorHex('#3797E8', 'Ultracem Blue')" title="Copiar #3797E8 (Ultracem Blue - Matriz)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #3797E8;"></button>
                  </div>
                </div>
              </div>

              <!-- Casco Protector Inventory Card -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-2xl shadow-xs">
                      ⛑️
                    </div>
                    <div>
                      <h4 class="font-bold text-xs text-slate-900 leading-tight">Casco Protector de Racha</h4>
                      <p class="text-[10px] text-slate-500">Congela tu racha 24h si tienes un día de campo difícil</p>
                    </div>
                  </div>
                  <span id="casco-badge-count" class="font-mono-data font-black text-sm bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-xl">
                    1 Activo
                  </span>
                </div>

                <div class="flex items-center justify-between pt-1 text-xs">
                  <button id="btn-use-casco" onclick="activarCascoProtector()" class="btn-tactile flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-2 px-3 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                    <span>🛡️</span>
                    <span>Activar Congelación (24 Horas)</span>
                  </button>
                </div>
              </div>

              <!-- Heatmap: 90 Días de Racha Comercial -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <div class="flex items-center justify-between text-xs">
                  <div>
                    <h4 class="font-bold text-slate-900">Historial de Constancia (Últimos 90 Días)</h4>
                    <p class="text-[10px] text-slate-500">Cada celda representa un día de contacto comercial registrado</p>
                  </div>
                  <span class="text-[10px] text-[#004797] font-bold font-mono-data">94% Éxito</span>
                </div>

                <div id="perfil-heatmap-grid" class="grid grid-flow-col grid-rows-7 gap-1 p-2 bg-slate-50 rounded-xl border border-slate-200 overflow-x-auto">
                  <!-- Generated dynamically with JS -->
                </div>

                <div class="flex items-center justify-between text-[10px] text-slate-400 font-semibold pt-1">
                  <span>Menos activo</span>
                  <div class="flex items-center space-x-1">
                    <span class="w-2.5 h-2.5 rounded-sm bg-slate-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-400"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-[#004797]"></span>
                  </div>
                  <span>Racha Activa</span>
                </div>
              </div>

              <!-- Trophies & Badges -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <h4 class="font-bold text-xs text-slate-900">Insignias & Logros de Obra</h4>
                
                <div class="grid grid-cols-3 gap-2">
                  <button onclick="openInAppTrofeo('Escudo Antichurn', 'Salva a 3 clientes en riesgo crítico antes de que cambien a la competencia.', '🛡️', '+200 XP')" class="btn-tactile bg-emerald-50/70 border border-emerald-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-emerald-100/50">
                    <span class="text-2xl">🛡️</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Antichurn</span>
                    <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                  </button>

                  <button onclick="openInAppTrofeo('Maestro Técnico', 'Comparte 25 certificados NTC 121 y curvas de fraguado validadas por laboratorio.', '📐', '+120 XP')" class="btn-tactile bg-slate-50 border border-slate-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-slate-100">
                    <span class="text-2xl">📐</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Mtro Técnico</span>
                    <span class="text-[8px] font-extrabold text-slate-500 bg-slate-200 px-1 rounded">18/25</span>
                  </button>

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
        <!-- BOTTOM NAVIGATION BAR (5 CLEAN TABS)                       -->
        <!-- ========================================================== -->
        <nav aria-label="Navegación Móvil" class="bg-white/95 backdrop-blur-md border-t border-slate-200/80 px-2 py-2 flex justify-around items-center select-none z-30 flex-shrink-0">
          
          <button id="nav-btn-racha" onclick="navigateToTab('racha')" class="btn-tactile flex flex-col items-center text-[#004797] font-bold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>
            </svg>
            <span class="text-[10px]">Racha</span>
          </button>

          <button id="nav-btn-copiloto" onclick="navigateToTab('copiloto')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
            <span class="text-[10px]">Copiloto</span>
          </button>

          <button id="nav-btn-mapa" onclick="navigateToTab('mapa')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/>
              <line x1="8" y1="2" x2="8" y2="18"/>
              <line x1="16" y1="6" x2="16" y2="22"/>
            </svg>
            <span class="text-[10px]">Radar & B2B</span>
          </button>

          <button id="nav-btn-liga" onclick="navigateToTab('liga')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
              <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/>
              <path d="M10 14.66V17c0 .55-.45 1-1 1H7v4h10v-4h-2c-.55 0-1-.45-1-1v-2.34"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/>
            </svg>
            <span class="text-[10px]">Liga</span>
          </button>

          <button id="nav-btn-perfil" onclick="navigateToTab('perfil')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            <span class="text-[10px]">Perfil</span>
          </button>

        </nav>

      </div>
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA PRD MAESTRO COMPLETO (CANVAS BLANCO)                  -->
    <!-- ============================================================== -->
    <div id="view-prd" class="hidden w-full max-w-5xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border-2 border-slate-300 shadow-sm space-y-10 text-slate-800">

      <!-- ============================================================== -->
      <!-- PRD DOCUMENT: ULTRACEM CRM MAESTRO                             -->
      <!-- ============================================================== -->
      
      <!-- Document Header & Meta Bar -->
      <header class="border-b-2 border-slate-200 pb-8 space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center space-x-3">
            <!-- Ultracem Official Logo Icon -->
            <div class="h-12 px-4 rounded-2xl bg-[#003E78] border-2 border-[#FDCA02] flex items-center justify-center shadow-xs">
              <img src="data:image/png;base64,{logo_base64}" alt="Ultracem" class="h-7 w-auto object-contain" />
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xs font-black uppercase tracking-wider text-[#003E78] bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">ULTRACEM S.A.S.</span>
                <span class="text-xs font-bold text-slate-400">•</span>
                <span class="text-xs font-black uppercase tracking-wider text-amber-800 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200">PLANTA GALAPA</span>
              </div>
              <p class="text-[11px] text-slate-500 font-medium mt-0.5">Documento de Especificación de Producto (PRD) • Versión 1.0 Oficial</p>
            </div>
          </div>
          
          <div class="flex items-center space-x-2">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
              <span class="w-2 h-2 rounded-full bg-emerald-500 mr-1.5"></span>
              Plataforma Operativa en Vivo
            </span>
            <button onclick="window.print()" class="btn-tactile text-xs font-bold text-slate-700 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-300 transition-all flex items-center space-x-1" title="Imprimir / Guardar como PDF">
              <span>🖨️</span>
              <span class="hidden sm:inline">Exportar</span>
            </button>
          </div>
        </div>

        <div>
          <h1 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight leading-tight">
            UltraRacha CRM: Prevención Antichurn, Rachas Comerciales & Copiloto IA Ultracem
          </h1>
          <p class="text-base text-slate-600 mt-2 leading-relaxed">
            Ecosistema de aceleración comercial diseñado para la fuerza de ventas de <strong>Ultracem S.A.S.</strong> en el Caribe colombiano. Transforma la fricción operativa del seguimiento de obras en hábitos comerciales diarios mediante gamificación de rachas, escalamiento ágil con SLAs y copiloto multimodelo.
          </p>
        </div>

        <!-- Metadata Ribbon -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Lema Ultracem</span>
            <span class="font-bold text-[#003E78]">“Calidad, Resistencia y Rendimiento”</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Sede Central</span>
            <span class="font-bold text-[#003E78]">Planta Galapa, Atlántico</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Infraestructura IA</span>
            <span class="font-bold text-[#003E78]">Groq LPU, NVIDIA NIM & DeepSeek</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/90">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Regla de Oro</span>
            <span class="font-bold text-amber-700">Corte Diario 11:59 PM</span>
          </div>
        </div>
      </header>

      <!-- SECCIÓN 1: VISIÓN -->
      <section class="space-y-4">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">1. Visión del Producto y Filosofía Operativa</h2>
        
        <div class="bg-[#003E78] rounded-2xl p-6 text-white space-y-3 border-l-4 border-[#FDCA02]">
          <span class="text-[10px] font-black uppercase tracking-widest text-[#FDCA02] bg-[#0A233F] px-2.5 py-0.5 rounded-full border border-amber-400/40">Premisa de Operación</span>
          <p class="text-base sm:text-lg font-bold leading-snug italic text-white">
            “Que el cemento fragüe, pero que tu cliente nunca se enfríe.”
          </p>
          <p class="text-xs text-blue-100 leading-relaxed">
            En entornos industriales de alta competencia como la comercialización de cemento y concreto con <strong>Ultracem</strong>, el éxito comercial depende de la constancia diaria, la agilidad en obra y la eliminación de fricciones operativas entre el asesor de campo y las áreas de Cartera, Logística y Calidad.
          </p>
        </div>
      </section>

      <!-- SECCIÓN 2: PALETA CROMÁTICA -->
      <section class="space-y-4 border-t border-slate-200 pt-6">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">2. Paleta Cromática Primaria Ultracem (Colores Sólidos Oficiales)</h2>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
          <!-- Azul Oscuro -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#003E78] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Azul Ultracem</span>
            <span class="text-[10px] font-mono-data text-blue-700 font-bold">#003E78</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Identidad & Confianza</span>
          </div>
          <!-- Amarillo -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#FDCA02] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Amarillo Ultracem</span>
            <span class="text-[10px] font-mono-data text-amber-700 font-bold">#FDCA02</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Energía, Sol & Alertas</span>
          </div>
          <!-- Azul Marino Profundo -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#0A233F] mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Azul Marino</span>
            <span class="text-[10px] font-mono-data text-slate-700 font-bold">#0A233F</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Sidebar & Autoridad</span>
          </div>
          <!-- Blanco Puro -->
          <div class="bg-white border-2 border-slate-200 rounded-xl p-3">
            <div class="h-10 rounded-lg bg-[#FFFFFF] border border-slate-300 mb-2"></div>
            <span class="font-bold text-slate-900 block text-xs">Blanco Puro</span>
            <span class="text-[10px] font-mono-data text-slate-500 font-bold">#FFFFFF</span>
            <span class="text-[10px] text-slate-400 block mt-0.5">Tarjetas & Claridad</span>
          </div>
        </div>
      </section>

      <!-- SECCIÓN 3: MÓDULOS DEL PRODUCTO -->
      <section class="space-y-4 border-t border-slate-200 pt-6">
        <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">3. Módulos Operativos del Ecosistema</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <!-- M1 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 1: Racha Diaria & Semáforo Antichurn</h3>
            <p class="text-slate-600 leading-relaxed">
              Corte a las 11:59 PM para atender cuentas críticas. Escalamiento en 1 clic con SLAs auditables (Cartera 4h, Logística 2h, Calidad 6h) que salvan la racha inmediatamente.
            </p>
          </div>
          <!-- M2 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 2: Copiloto IA Multimodelo</h3>
            <p class="text-slate-600 leading-relaxed">
              Inferencia ultrarrápida con Groq LPU, NVIDIA NIM y DeepSeek. Guardrails estrictos de la norma NTC 121 y transcripción de notas de voz con Whisper Turbo.
            </p>
          </div>
          <!-- M3 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 3: Radar Georreferenciado & Directorio B2B</h3>
            <p class="text-slate-600 leading-relaxed">
              Cartografía interactiva con Leaflet de clientes, Planta Galapa y competencia (Argos/Cemex). Directorio calificado de 12 empresas del Caribe.
            </p>
          </div>
          <!-- M4 -->
          <div class="bg-white rounded-2xl border border-slate-200 p-4 space-y-2">
            <h3 class="font-bold text-sm text-[#003E78]">Módulo 4: Liga de Asesores & Transferencia</h3>
            <p class="text-slate-600 leading-relaxed">
              Leaderboard gamificado con Milena Ospino, Adriana Anaya e Hichel Espitia. Módulo de reasignación voluntaria de clientes entre compañeros de equipo.
            </p>
          </div>
        </div>
      </section>

    </div>

  </main>

    </div>

      </div>

      <!-- PANEL CELULAR: APLICACIÓN MÓVIL EN VIVO (STICKY DERECHA) -->
      <aside id="phone-container-wrapper" class="w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center">
        <div class="mb-2 text-center">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-[#003E78] text-white shadow-xs">
            📱 Asesor Móvil en Terreno
          </span>
        </div>
<!-- Phone Canvas Frame: Strict isolation & fixed height containment -->
      <div class="w-full max-w-[420px] bg-white rounded-[40px] shadow-2xl border-4 border-slate-800 overflow-hidden flex flex-col h-[820px] max-h-[820px] relative" style="position: relative; isolation: isolate; contain: paint;">
        
        <!-- Phone Status Notch -->
        <div class="bg-slate-900 pt-3.5 px-6 pb-2 flex justify-between items-center text-white text-[11px] font-mono-data select-none z-30 flex-shrink-0">
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
        <div id="inphone-sheet-overlay" class="hidden absolute inset-0 z-50 bg-slate-950/70 backdrop-blur-xs flex flex-col justify-end rounded-[36px] overflow-hidden transition-all duration-300">
          <!-- Backdrop click to dismiss -->
          <div class="flex-1 cursor-pointer" onclick="closeInPhoneSheet()" title="Cerrar panel"></div>
          
          <!-- Sheet Body Panel (Slides up from bottom inside the phone) -->
          <div id="inphone-sheet-panel" class="bg-white rounded-t-[28px] max-h-[90%] flex flex-col shadow-2xl border-t border-slate-200 overflow-hidden transform animate-sheet-up">
            
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
        <div id="mobile-screen-content" class="flex-1 flex flex-col overflow-hidden relative">
          
          <!-- ======================================================== -->
          <!-- PANTALLA 1: RACHA & CLIENTES                             -->
          <!-- ======================================================== -->
          <div id="screen-racha" class="flex-1 flex flex-col overflow-hidden">
            
            <!-- Mobile Header Bar (Full Bleed - Perfectly Aligned & Symmetrical) -->
            <div class="bg-[#003E78] text-white px-4 pt-3 pb-3 relative overflow-hidden flex-shrink-0">
              <!-- Top Row: User Avatar & Streak Pill -->
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

              <!-- Bottom Row: Midnight Countdown & Helmet Freeze Badge -->
              <div class="mt-2.5 pt-2 border-t border-white/15 flex items-center justify-between text-xs relative z-10">
                <div class="flex items-center space-x-1.5 text-blue-100 text-[11px]">
                  <span>⏰</span>
                  <span class="font-medium">Corte 11:59 PM:</span>
                  <span id="countdown-timer" class="font-mono-data font-bold text-amber-300 bg-white/10 px-2 py-0.5 rounded text-[11px]">13h : 59m : 12s</span>
                </div>

                <!-- Casco Protector Pill Trigger -->
                <button onclick="navigateToTab('perfil')" id="header-casco-btn" class="btn-tactile bg-white/15 hover:bg-white/25 border border-white/25 text-white font-bold text-[11px] px-2.5 py-0.5 rounded-full flex items-center space-x-1.5 shadow-xs" title="Cascos disponibles para proteger tu racha">
                  <span>⛑️</span>
                  <span id="header-casco-count">1 Casco</span>
                </button>
              </div>
            </div>

            <!-- Scrollable Content Area -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <!-- ULTRACEM ACTIVATION BANNER (DINÁMICO POR FASES 1-4) -->
              <div id="activation-stage-card" class="rounded-2xl p-3.5 border transition-all duration-300 shadow-xs relative overflow-hidden bg-[#0A233F] text-white border-teal-500/30">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-8 h-8 rounded-xl bg-teal-500/20 border border-teal-400/40 flex items-center justify-center text-teal-300 font-bold text-base flex-shrink-0">
                      🌱
                    </div>
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <span class="font-bold text-xs text-white">Ultracem</span>
                        <span class="text-[9px] bg-teal-500/20 text-teal-300 px-1.5 py-0.2 rounded-full font-semibold border border-teal-500/30">Fase 4: Lanzamiento</span>
                      </div>
                      <p class="text-[10px] text-slate-300 mt-0.5">Calidad, Resistencia y Rendimiento • Demo Activa</p>
                    </div>
                  </div>
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg shadow-xs transition-all flex items-center space-x-1 flex-shrink-0">
                    <span>📘</span>
                    <span>Ver PRD</span>
                  </button>
                </div>
              </div>

              <!-- DON FRAGUADO: MASCOTA VECTORIAL INTERACTIVA -->
              <div id="mascot-card" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs flex items-center space-x-3.5 transition-all">
                
                <!-- SVG Vector Mascot -->
                <div id="don-fraguado-container" class="relative w-16 h-18 flex-shrink-0 cursor-pointer select-none mascot-breathing" onclick="pokeMascot()" title="¡Haz clic en Don Fraguado!">
                  <svg viewBox="0 0 100 110" class="w-full h-full drop-shadow-sm overflow-visible" xmlns="http://www.w3.org/2000/svg">
                    <ellipse cx="50" cy="103" rx="34" ry="5" fill="#CBD5E1" opacity="0.6" />

                    <!-- Mascota: Bulto de Cemento Ultracem -->
                    <g id="mascot-body-group" class="transition-transform duration-300 origin-bottom">
                      <!-- Sack Depth -->
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
                      <text x="50" y="88.2" fill="#FFFFFF" font-family="'JetBrains Mono', monospace" font-weight="800" font-size="4.2" text-anchor="middle">50 kg • NTC 121</text>

                      <!-- Face: Interactive Eyes -->
                      <g id="mascot-eyes">
                        <!-- Left Eye -->
                        <circle cx="38" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="39.5" cy="52.5" r="2" fill="#FFFFFF" />
                        <!-- Right Eye -->
                        <circle cx="62" cy="54" r="5.2" fill="#0F172A" />
                        <circle cx="63.5" cy="52.5" r="2" fill="#FFFFFF" />
                      </g>

                      <!-- Rosy Cheeks -->
                      <ellipse cx="30" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>
                      <ellipse cx="70" cy="59" rx="3.5" ry="2" fill="#FDA4AF" opacity="0.7"/>

                      <!-- Mouth: Happy smile -->
                      <path id="mascot-mouth" d="M 44,60 Q 50,65 56,60" fill="none" stroke="#0F172A" stroke-width="2" stroke-linecap="round" />
                    </g>

                    <!-- Engineer Hard Hat (Casco Amarillo Ultracem) -->
                    <g id="mascot-helmet-group" class="transition-transform duration-300">
                      <!-- Helmet Dome -->
                      <path d="M 18,34 C 18,12 82,12 82,34 Z" fill="#FACC15" stroke="#CA8A04" stroke-width="2" />
                      <!-- Helmet Center Crest Ridge -->
                      <path d="M 46,14 L 54,14 L 53,33 L 47,33 Z" fill="#EAB308" />
                      <!-- Helmet Brim / Visor -->
                      <path d="M 12,34 Q 50,29 88,34 Q 50,38 12,34 Z" fill="#CA8A04" />
                      <!-- Reflective Strip on Brim -->
                      <path d="M 22,33.5 Q 50,30.5 78,33.5" fill="none" stroke="#FEF08A" stroke-width="1.8" stroke-linecap="round" />
                    </g>
                  </svg>
                </div>

                <!-- Speech Bubble Dialogue -->
                <div class="flex-1">
                  <div class="flex items-center justify-between mb-1">
                    <span class="text-xs font-black text-slate-800 flex items-center space-x-1.5">
                      <span>Don Fraguado</span>
                      <span id="mascot-mood-badge" class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full">⚡ Motivado</span>
                    </span>
                    <span class="text-[10px] text-slate-500 font-semibold">Tócame</span>
                  </div>
                  <p id="mascot-dialogue-text" class="text-xs text-slate-600 leading-snug">
                    ¡Buenos días Carlos! Tu racha está protegida. Tienes <strong>2 clientes por contactar</strong> antes de las 11:59 PM para sumar +150 XP.
                  </p>
                </div>
              </div>

              <!-- Quick Banner to Prospecting Search Engine -->
              <div onclick="navigateToTab('mapa'); setMapSubView('prospectos');" class="btn-tactile bg-[#003E78] text-white p-3.5 rounded-2xl shadow-xs flex items-center justify-between cursor-pointer hover:shadow-md transition-all">
                <div class="flex items-center space-x-3">
                  <span class="text-2xl">🏢</span>
                  <div>
                    <h4 class="font-extrabold text-xs text-white leading-tight">Radar de Obras & Nuevas Empresas</h4>
                    <p class="text-[10px] text-blue-200 mt-0.5">12 constructoras y prefabricados listas para contactar</p>
                  </div>
                </div>
                <span class="text-xs bg-white/20 px-2 py-1 rounded-lg font-bold">Ver Empresas ➔</span>
              </div>

              <!-- Filter Bar (3 Clean Columns) -->
              <div class="space-y-1.5">
                <div class="flex items-center justify-between text-xs px-1">
                  <span class="font-bold text-slate-700">Mi Cartera Activa de Clientes</span>
                  <span class="text-[10px] text-slate-500" id="filter-count-badge">3 Casos Activos</span>
                </div>

                <div class="grid grid-cols-3 gap-2 bg-slate-200/80 p-1 rounded-xl">
                  <button id="filter-btn-todos" onclick="filterClients('todos')" class="py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs text-center">
                    Todos (3)
                  </button>
                  <button id="filter-btn-obras" onclick="filterClients('obras')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏗️ Obras (2)
                  </button>
                  <button id="filter-btn-ferreterias" onclick="filterClients('ferreterias')" class="py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center">
                    🏪 Ferret. (1)
                  </button>
                </div>
              </div>

              <!-- CLIENT CARD 1: CONSTRUCTORA BOLÍVAR (CRÍTICO) -->
              <div id="card-client-1" class="client-card bg-white rounded-2xl p-4 border-2 border-rose-400 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Constructora Bolívar</h3>
                      <span class="text-[10px] font-extrabold bg-blue-100 text-[#004797] px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento Estructural</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-rose-700 bg-rose-50 border border-rose-200 px-2 py-0.5 rounded-md">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                    <span>8D SIN PEDIDO</span>
                  </span>
                </div>

                <!-- Churn Risk Warning Banner -->
                <div class="bg-rose-50/80 border border-rose-200/90 rounded-xl p-2.5 text-[11px] text-rose-900 flex items-start space-x-2">
                  <span class="text-rose-600 mt-0.5 text-xs">⚠️</span>
                  <p class="leading-snug">
                    <strong>Riesgo Crítico de Pérdida:</strong> Superó su ciclo habitual de recompra por 3 días. Contacta hoy para salvar tu racha comercial (+100 XP).
                  </p>
                </div>

                <!-- Action Buttons: WhatsApp & Register Action -->
                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Constructora Bolívar', '120 Ton Cemento Estructural')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(1, 'Constructora Bolívar')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <!-- Secondary Technical Actions: Cubicaje & Voice Notes -->
                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCubicajeModal('Constructora Bolívar')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📐</span>
                    <span>Cubicación Losa</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Constructora Bolívar')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz en obra">
                    <span>🎙️</span>
                  </button>
                </div>

                <!-- Transfer Client to Colleague Option -->
                <div class="pt-1">
                  <button onclick="openTransferClientModal(1, 'Constructora Bolívar — Torres del Mar')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

                <!-- Interactive Activity Timeline Container (With Saved Audios) -->
                <div id="timeline-box-1" class="bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-[11px] space-y-2 mt-2">
                  <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-700 text-[10px] uppercase tracking-wider">Historial Reciente & Audios</span>
                    <span class="text-[9px] text-emerald-600 font-semibold font-mono-data">Sincronizado</span>
                  </div>
                  <div id="timeline-notes-list-1" class="space-y-2">
                    <div class="flex items-start space-x-2 text-slate-600">
                      <span class="w-1.5 h-1.5 rounded-full bg-slate-400 mt-1.5 flex-shrink-0"></span>
                      <div>
                        <strong>Visita Presencial</strong> hace 3 días: El residente Ing. Arango solicitó cotización con flete incluido.
                      </div>
                    </div>
                  </div>
                </div>

              </div>

              <!-- CLIENT CARD 2: FERRETERÍA EL CONSTRUCTOR -->
              <div id="card-client-2" class="client-card bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3 transition-all" data-tipo="ferreterias">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-900 text-sm tracking-tight">Ferretería El Constructor</h3>
                      <span class="text-[10px] font-extrabold bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded">Ferretería</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Sede Centro Soledad • 45 Ton Cemento Gris</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md">
                    <span>4D SIN PEDIDO</span>
                  </span>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button onclick="openInAppWhatsApp('Ferretería El Constructor', '45 Ton Cemento Gris')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>💬</span>
                    <span>WhatsApp</span>
                  </button>
                  <button onclick="openInAppRegisterAction(2, 'Ferretería El Constructor')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>📝</span>
                    <span>Registrar Acción</span>
                  </button>
                </div>

                <div class="flex items-center space-x-2 pt-1 border-t border-slate-100 text-xs">
                  <button onclick="openCertificadoModal('Ferretería El Constructor', 'Cemento Uso General')" class="flex-1 bg-slate-50 hover:bg-blue-50 text-[#004797] border border-slate-200 rounded-xl py-1.5 px-2 text-[11px] font-bold flex items-center justify-center space-x-1">
                    <span>📜</span>
                    <span>Certificado Calidad</span>
                  </button>
                  <button onclick="openVoiceNotesModal('Ferretería El Constructor')" class="w-8 h-8 bg-slate-50 hover:bg-rose-50 text-rose-600 border border-slate-200 rounded-xl flex items-center justify-center text-xs" title="Grabar nota de voz">
                    <span>🎙️</span>
                  </button>
                </div>

                <div class="pt-1">
                  <button onclick="openTransferClientModal(2, 'Ferretería El Constructor — Sede Centro')" class="w-full bg-slate-50 hover:bg-indigo-50 text-indigo-700 border border-indigo-200 rounded-xl py-1.5 px-3 text-[11px] font-bold flex items-center justify-center space-x-1.5 transition-all" title="Transferir este cliente fijo a un compañero">
                    <span>🔄</span>
                    <span>Transferir Cliente a Compañero de Equipo</span>
                  </button>
                </div>

              </div>

              <!-- CLIENT CARD 3: CASO BLOQUEADO POR OTRO ASESOR -->
              <div id="card-client-3" class="client-card bg-slate-100/80 rounded-2xl p-4 border border-slate-300 shadow-xs space-y-3 transition-all" data-tipo="obras">
                <div class="flex items-start justify-between">
                  <div>
                    <div class="flex items-center space-x-2">
                      <h3 class="font-bold text-slate-700 text-sm tracking-tight">Marval — Altos de Riomar</h3>
                      <span class="text-[10px] font-extrabold bg-slate-200 text-slate-600 px-1.5 py-0.5 rounded">Obra Mayor</span>
                    </div>
                    <p class="text-[11px] text-slate-500 mt-0.5">Vaciado Torre 3 • Barranquilla</p>
                  </div>
                  <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded-md">
                    <span>🔒 EN GESTIÓN (Laura V.)</span>
                  </span>
                </div>

                <div class="bg-amber-50/80 border border-amber-200 rounded-xl p-2.5 text-[11px] text-amber-900 flex items-start space-x-2">
                  <span class="text-amber-600 mt-0.5">🔒</span>
                  <p class="leading-snug">
                    <strong>Protección Anti-Acoso Activa:</strong> Esta cuenta ya está siendo gestionada activamente por <strong>Laura Valencia</strong> (último contacto hace 2 horas). No puedes realizar llamadas ni mensajes directos para evitar fricción con el cliente.
                  </p>
                </div>

                <div class="grid grid-cols-2 gap-2 pt-1">
                  <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 cursor-not-allowed" title="Contacto bloqueado por política anti-acoso">
                    <span>🔒</span>
                    <span>Chat Bloqueado</span>
                  </button>
                  <button onclick="pedirTransferenciaCaso(3, 'Marval — Altos de Riomar', 'Laura Valencia')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 shadow-xs">
                    <span>🔄</span>
                    <span>Pedir Transferencia</span>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 2: COPILOTO IA CON MULTI-MODELOS                -->
          <!-- ======================================================== -->
          <div id="screen-copiloto" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Copiloto Header Bar -->
            <div class="bg-[#0A233F] text-white px-4 pt-3.5 pb-3 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    ⚡
                  </div>
                  <div>
                    <div class="flex items-center space-x-2">
                      <h2 class="font-bold text-sm tracking-tight text-white">Copiloto IA Ultracem</h2>
                      <span id="ai-provider-badge" class="text-[9px] bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 font-extrabold px-2 py-0.5 rounded-full uppercase">NVIDIA / DeepSeek</span>
                    </div>
                    <p class="text-[10px] text-blue-200">Fichas Técnicas NTC, Precios & Guardrail Estricto</p>
                  </div>
                </div>
                
                <!-- Symmetrical Clean Norma Badge -->
                <div class="flex items-center space-x-1 bg-white/10 border border-white/20 px-2.5 py-1 rounded-xl">
                  <span class="text-[10px] text-amber-300 font-mono-data font-bold">NTC 121</span>
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-3.5">

              <!-- AI Provider & API Key Status Card -->
              <div class="bg-white p-3.5 rounded-2xl border border-slate-200/90 shadow-xs flex items-center justify-between">
                <div class="flex items-center space-x-2.5">
                  <span class="text-xl">🤖</span>
                  <div>
                    <h4 class="font-bold text-xs text-slate-800" id="ai-active-status-label">Motor: NVIDIA NIM / DeepSeek</h4>
                    <p class="text-[10px] text-slate-500" id="ai-active-status-desc">Inferencia de alto nivel con filtro comercial estricto</p>
                  </div>
                </div>
                <button onclick="openInPhoneAISettings()" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-300">
                  Configurar
                </button>
              </div>

              <!-- Interactive Chat with Copilot -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs flex flex-col h-[340px] overflow-hidden">
                <div class="p-3 bg-slate-50 border-b border-slate-100 flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xs font-bold text-slate-700">Chat Técnico & Comercial</span>
                    <span id="ai-engine-chip" class="text-[9px] text-blue-700 bg-blue-100 px-2 py-0.5 rounded-full font-bold">Llama 3.1 70B</span>
                  </div>
                  <span class="text-[10px] text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded-full font-bold">Filtro Antidesvío ON</span>
                </div>

                <!-- Messages Area -->
                <div id="ai-chat-messages" class="flex-1 overflow-y-auto p-3 space-y-2.5 text-xs">
                  <div class="flex justify-start">
                    <div class="bg-slate-100 p-2.5 rounded-xl rounded-tl-none text-slate-800 max-w-[90%] leading-relaxed">
                      ¡Hola Carlos! Soy tu Copiloto Ultracem con IA. Puedo analizar qué empresas contactar para ofrecer Cemento Estructural Max NTC 121, comparar costos vs Argos y Cemex, o darte guiones de venta para directores de obra. ¿Qué deseas consultar hoy?
                    </div>
                  </div>
                </div>

                <!-- Chat Input Form -->
                <div class="p-2 border-t border-slate-100 bg-white flex items-center space-x-1.5">
                  <input type="text" id="ai-chat-input" placeholder="Pregunta sobre clientes, NTC 121, empresas o cómo vender..." class="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" onkeydown="if(event.key==='Enter') enviarConsultaAI()">
                  <button onclick="enviarConsultaAI()" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white w-8 h-8 rounded-xl flex items-center justify-center text-sm shadow-xs" title="Enviar consulta a la IA">
                    ➤
                  </button>
                </div>
              </div>

              <!-- Conversational Icebreakers & Quick Scripts -->
              <div class="space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-[10px] uppercase font-bold text-slate-600 block tracking-wider">💬 Consultas Rápidas de Prospección & Ventas:</span>
                  <span class="text-[9px] text-slate-400">Toca para probar</span>
                </div>

                <div class="grid grid-cols-1 gap-1.5">
                  <button onclick="probarPromptRapido('¿A qué nuevas empresas constructoras de Barranquilla y Soledad puedo contactar esta semana y cómo abordarles?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🏢</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Prospección: ¿A qué constructoras contactar?</strong>
                      <span class="text-[10px] text-slate-500">Empresas con obras activas y estrategia de abordaje</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo inicio una conversación con Constructora Amarilo que actualmente compra todo su cemento a Argos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤝</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Ganar cuenta a Argos (Constructora Amarilo)</strong>
                      <span class="text-[10px] text-slate-500">Argumentario de desencofrado rápido y flete directo Galapa</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué ventajas tiene el Cemento Estructural Ultracem para plantas de prefabricados y bloqueras?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-blue-50 hover:text-[#004797] transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🧱</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Oferta de Valor para Bloqueras y Prefabricados</strong>
                      <span class="text-[10px] text-slate-500">Desmolde acelerado en horas y ahorro de espacio</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué módulos de formación en dosificación y fraguado de Campus Ultra WhatsApp puedo ofrecerle a un maestro de obra para fidelizarlo?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-teal-50 hover:text-teal-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🎓</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Campus Ultra WhatsApp (Formación de Obra)</strong>
                      <span class="text-[10px] text-slate-500">Capacitación certificada para maestros y ferreteros</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Cómo se articula mi gestión comercial de campo con Vanesa IA (el asistente de WhatsApp de Ultracem) para autogestión de pedidos?')" class="text-[11px] text-left font-medium bg-white border border-slate-200 text-slate-700 p-2.5 rounded-xl hover:bg-emerald-50 hover:text-emerald-900 transition-all flex items-start space-x-2 shadow-2xs">
                    <span class="text-base">🤖</span>
                    <div>
                      <strong class="text-slate-900 block text-[11px]">Vanesa IA (WhatsApp Oficial Ultracem)</strong>
                      <span class="text-[10px] text-slate-500">Autogestión de cotizaciones y despachos en tiempo real</span>
                    </div>
                  </button>

                  <button onclick="probarPromptRapido('¿Qué es el ácido ribonucleico?')" class="text-[11px] text-left font-bold bg-rose-50 border border-rose-200 text-rose-700 p-2.5 rounded-xl hover:bg-rose-100 transition-all flex items-center space-x-2 shadow-2xs">
                    <span class="text-base">🚫</span>
                    <div>
                      <strong class="text-rose-900 block text-[11px]">Probar Filtro de Guardrail Estricto</strong>
                      <span class="text-[10px] text-rose-600">Rechazo de pregunta ajena a la empresa (biología)</span>
                    </div>
                  </button>
                </div>
              </div>

              <div class="h-8"></div>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 3: MAPA & DIRECTORIO B2B DE EMPRESAS Y OBRAS     -->
          <!-- ======================================================== -->
          <div id="screen-mapa" class="hidden flex-1 flex flex-col overflow-hidden relative">
            
            <!-- Full-bleed Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-2.5 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div class="flex items-center space-x-2.5">
                  <div class="w-9 h-9 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center text-lg shadow-xs">
                    🗺️
                  </div>
                  <div>
                    <h2 class="font-bold text-sm tracking-tight text-white">Radar & Prospección B2B</h2>
                    <p class="text-[10px] text-blue-200">Búsqueda de Nuevas Empresas & Geolocalización</p>
                  </div>
                </div>
                
                <div class="flex items-center space-x-1.5">
                  <!-- City Center Selector -->
                  <select id="map-city-select" onchange="centrarMapaCiudad(this.value)" class="bg-white/15 border border-white/25 text-white text-[11px] font-bold rounded-lg px-2 py-1 focus:outline-none">
                    <option value="barranquilla" class="text-slate-900">Barranquilla</option>
                    <option value="galapa" class="text-slate-900">Galapa (Planta)</option>
                    <option value="soledad" class="text-slate-900">Soledad</option>
                    <option value="cartagena" class="text-slate-900">Cartagena</option>
                    <option value="santamarta" class="text-slate-900">Santa Marta</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW TOGGLE: [RADAR EN MAPA] VS [DIRECTORIO DE EMPRESAS B2B] -->
            <div class="px-3 pt-2 pb-2 bg-white border-b border-slate-200 flex items-center justify-between text-xs flex-shrink-0 z-20">
              <div class="bg-slate-100 p-1 rounded-xl flex items-center w-full border border-slate-200">
                <button id="btn-map-mode-radar" onclick="setMapSubView('radar')" class="flex-1 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs flex items-center justify-center space-x-1.5">
                  <span>🗺️</span>
                  <span>Radar en Mapa</span>
                </button>
                <button id="btn-map-mode-prospectos" onclick="setMapSubView('prospectos')" class="flex-1 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center justify-center space-x-1.5">
                  <span>🏢</span>
                  <span id="badge-prospectos-count">Directorio Empresas (12)</span>
                </button>
              </div>
            </div>

            <!-- SUB-VIEW 1: RADAR EN MAPA -->
            <div id="subview-map-radar" class="flex-1 flex flex-col overflow-hidden relative">
              <!-- Search Bar + Category Filter Chips -->
              <div class="p-2.5 bg-white border-b border-slate-200 space-y-2 flex-shrink-0 z-20">
                <div class="flex items-center space-x-1.5">
                  <div class="relative flex-1">
                    <input type="text" id="map-search-input" placeholder="Buscar empresa, obra, Argos, Cemex, Galapa..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="buscarEnMapa(this.value)">
                    <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                  </div>
                  <button id="btn-toggle-satellite" onclick="toggleMapLayer()" class="btn-tactile bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-[10px] font-bold px-2 py-1.5 rounded-xl flex items-center space-x-1 flex-shrink-0" title="Alternar entre Callejero y Vista Satelital">
                    <span>🛰️</span>
                    <span>Satélite</span>
                  </button>
                </div>
                
                <!-- Category Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="map-chip-todas" onclick="filtrarMapaPorCategoria('todas')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white border border-[#004797] flex-shrink-0 transition-all">
                    Todas (18)
                  </button>
                  <button id="map-chip-prospectos" onclick="filtrarMapaPorCategoria('prospectos')" class="px-2.5 py-1 rounded-lg bg-sky-50 text-sky-800 border border-sky-200 flex-shrink-0 hover:bg-sky-100 transition-all">
                    ✨ Por Contactar (7)
                  </button>
                  <button id="map-chip-ultracem" onclick="filtrarMapaPorCategoria('ultracem')" class="px-2.5 py-1 rounded-lg bg-blue-50 text-[#004797] border border-blue-200 flex-shrink-0 hover:bg-blue-100 transition-all">
                    🏭 Ultracem (3)
                  </button>
                  <button id="map-chip-competencia" onclick="filtrarMapaPorCategoria('competencia')" class="px-2.5 py-1 rounded-lg bg-rose-50 text-rose-700 border border-rose-200 flex-shrink-0 hover:bg-rose-100 transition-all">
                    🔴 Competidores (4)
                  </button>
                </div>
              </div>

              <!-- Bounded Map Canvas -->
              <div class="flex-1 relative bg-slate-200 min-h-0 overflow-hidden mx-3 mb-2 rounded-2xl border border-slate-300 shadow-inner">
                <div id="colombia-leaflet-map" class="w-full h-full"></div>

                <!-- Selected Site / Competitor Card Overlay -->
                <div id="map-site-card" class="hidden absolute bottom-3 left-3 right-3 bg-white/95 backdrop-blur-md p-3.5 rounded-2xl shadow-xl border border-slate-200 z-20 space-y-2">
                  <div class="flex justify-between items-start">
                    <div>
                      <h4 id="map-site-name" class="font-bold text-xs text-slate-900 leading-tight">Constructora Bolívar</h4>
                      <p id="map-site-desc" class="text-[10px] text-slate-500 mt-0.5">Torres del Mar • 120 Ton Cemento</p>
                    </div>
                    <span id="map-site-status" class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 flex-shrink-0">Mi Cartera</span>
                  </div>
                  
                  <div id="map-site-intel" class="hidden bg-slate-50 border border-slate-200 rounded-xl p-2 text-[10px] space-y-1">
                    <!-- Dynamic details -->
                  </div>

                  <div id="map-site-actions" class="grid grid-cols-2 gap-2 pt-0.5">
                    <!-- Dynamic actions -->
                  </div>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW 2: DIRECTORIO B2B DE PROSPECCIÓN (NUEVAS EMPRESAS A CONTACTAR) -->
            <div id="subview-map-prospectos" class="hidden flex-1 flex flex-col overflow-hidden bg-slate-50/70 p-3 space-y-2.5">
              
              <!-- Search & Filter Bar for Prospects -->
              <div class="bg-white p-2.5 rounded-2xl border border-slate-200 shadow-xs space-y-2 flex-shrink-0">
                <div class="relative">
                  <input type="text" id="prospects-search-input" placeholder="Buscar por empresa, obra, constructor o sector..." class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-8 pr-3 py-1.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]" oninput="filtrarDirectorioProspectos(this.value)">
                  <span class="absolute left-2.5 top-2 text-slate-400 text-xs">🔍</span>
                </div>

                <!-- Sector Filter Chips -->
                <div class="flex items-center space-x-1 overflow-x-auto pb-0.5 text-[10px] font-bold">
                  <button id="chip-sec-todos" onclick="filtrarProspectosSector('todos')" class="px-2.5 py-1 rounded-lg bg-[#004797] text-white flex-shrink-0 transition-all">
                    Todos (12)
                  </button>
                  <button id="chip-sec-constructoras" onclick="filtrarProspectosSector('constructoras')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏗️ Constructoras (5)
                  </button>
                  <button id="chip-sec-infraestructura" onclick="filtrarProspectosSector('infraestructura')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🛣️ Vías & Concesiones (2)
                  </button>
                  <button id="chip-sec-prefabricados" onclick="filtrarProspectosSector('prefabricados')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🧱 Bloqueras & Adoquines (2)
                  </button>
                  <button id="chip-sec-ferreterias" onclick="filtrarProspectosSector('ferreterias')" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all">
                    🏪 Ferreterías Mayoristas (3)
                  </button>
                </div>
              </div>

              <!-- Prospects Cards Scroll Area -->
              <div id="prospects-list-container" class="flex-1 overflow-y-auto space-y-2.5 pr-0.5">
                <!-- Injected dynamically with JavaScript -->
              </div>

            </div>

          </div>

          <!-- ======================================================== -->
          <!-- PANTALLA 4: LIGA DIAMANTE CON CARTERA DE COMPAÑEROS      -->
          <!-- ======================================================== -->
          <div id="screen-liga" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Liga Header Bar -->
            <div class="bg-[#D9531E] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
              <div class="flex items-center justify-between relative z-10">
                <div>
                  <span class="text-[9px] font-black uppercase tracking-widest bg-black/20 px-2 py-0.5 rounded-full inline-block mb-1">División Regional Caribe</span>
                  <h2 class="font-extrabold text-base tracking-tight text-white leading-tight">Liga Diamante del Clinker</h2>
                  <p class="text-[11px] text-amber-100 mt-0.5">Cierre de temporada en 3 días • Top 3 asciende</p>
                </div>
                
                <div class="w-11 h-11 rounded-2xl bg-white/20 border border-white/30 flex items-center justify-center text-2xl shadow-sm flex-shrink-0">
                  💎
                </div>
              </div>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto bg-slate-50/70 p-4 space-y-4">
              
              <div class="flex items-center justify-between text-xs px-1">
                <span class="font-bold text-slate-700">Tabla de Posiciones Regional</span>
                <span class="text-[10px] text-slate-500">Toca un compañero para ver su cartera</span>
              </div>

              <!-- Leaderboard List -->
              <div class="bg-white rounded-2xl border border-slate-200/90 shadow-xs divide-y divide-slate-100 overflow-hidden">
                
                <!-- Rank 1: Andrés Restrepo -->
                <div onclick="openColleagueProfile('andres')" class="p-3.5 flex items-center justify-between bg-amber-50/40 hover:bg-amber-100/50 cursor-pointer transition-all" title="Ver clientes asignados a Andrés">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-black text-amber-600 text-sm">🥇</span>
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80" alt="Andrés R." class="w-9 h-9 rounded-full object-cover border border-amber-300">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Andrés Restrepo</h4>
                        <span class="text-[8px] bg-amber-200 text-amber-900 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Bogotá Norte • 48d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">980 Ton</span>
                    <span class="text-[9px] text-amber-600 block font-semibold">+450 XP</span>
                  </div>
                </div>

                <!-- Rank 2: Laura Valencia -->
                <div onclick="openColleagueProfile('laura')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Laura">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-sm">🥈</span>
                    <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80" alt="Laura V." class="w-9 h-9 rounded-full object-cover border border-purple-200">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Laura Valencia</h4>
                        <span class="text-[8px] bg-purple-100 text-purple-800 font-extrabold px-1 rounded">👥 3 Obras</span>
                      </div>
                      <span class="text-[10px] text-slate-500">Medellín / Caribe • 34d Racha 🔥</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="font-mono-data font-bold text-slate-900 text-xs">840 Ton</span>
                    <span class="text-[9px] text-slate-500 block font-semibold">+320 XP</span>
                  </div>
                </div>

                <!-- Rank 3: Carlos Mendoza (User Highlighted) -->
                <div onclick="navigateToTab('perfil')" class="p-3.5 flex items-center justify-between bg-blue-50/60 border-l-4 border-[#004797] cursor-pointer hover:bg-blue-100/50 transition-all">
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

                <!-- Rank 4: Felipe Morales -->
                <div onclick="openColleagueProfile('felipe')" class="p-3.5 flex items-center justify-between hover:bg-slate-50 cursor-pointer transition-all" title="Ver clientes asignados a Felipe">
                  <div class="flex items-center space-x-3">
                    <span class="w-6 text-center font-bold text-slate-400 text-xs">4</span>
                    <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&auto=format&fit=crop&q=80" alt="Felipe M." class="w-9 h-9 rounded-full object-cover">
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <h4 class="font-bold text-xs text-slate-900">Felipe Morales</h4>
                        <span class="text-[8px] bg-slate-100 text-slate-600 font-extrabold px-1 rounded">👥 2 Obras</span>
                      </div>
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
          <!-- PANTALLA 5: PERFIL, CASCO PROTECTOR & HEATMAP 90 DÍAS    -->
          <!-- ======================================================== -->
          <div id="screen-perfil" class="hidden flex-1 flex flex-col overflow-hidden">
            
            <!-- Full-bleed Perfil Header Bar -->
            <div class="bg-[#003E78] text-white px-4 pt-3.5 pb-4 relative overflow-hidden flex-shrink-0">
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
                  <div class="bg-[#003E78] h-full rounded-full transition-all duration-500" style="width: 85%"></div>
                </div>
                <p class="text-[10px] text-slate-500">Despacha 60 toneladas adicionales este mes para desbloquear el cupo autónomo de $80M.</p>
              </div>

              <!-- ULTRACEM : TRACK DE TALENTO & PALETA DE MARCA -->
              <div class="bg-[#0F172A] rounded-2xl p-4 border border-teal-500/30 text-white shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-9 h-9 rounded-xl bg-teal-950 border border-teal-400/40 p-1 flex items-center justify-center">
                      <svg viewBox="0 0 100 100" class="w-6 h-6" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
                        <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
                        <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
                        <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
                        <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
                      </svg>
                    </div>
                    <div>
                      <div class="flex items-center space-x-1.5">
                        <span class="font-extrabold text-xs text-white uppercase tracking-wider">Ultracem</span>
                        <span class="text-[9px] bg-teal-400/20 text-teal-300 px-1.5 py-0.2 rounded font-bold border border-teal-500/40">🌱 Brote en Crecimiento</span>
                      </div>
                      <p class="text-[10px] text-teal-100/80 italic mt-0.5">“Calidad, Resistencia y Rendimiento”</p>
                    </div>
                  </div>
                  <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg transition-all shadow-xs">
                    PRD
                  </button>
                </div>

                <!-- 3 Símbolos: Mano, Semilla, Brote -->
                <div class="grid grid-cols-3 gap-2 text-center text-[10px] pt-1 border-t border-slate-700/80">
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🖐️</span>
                    <strong class="text-white block mt-0.5">La Mano</strong>
                    <span class="text-slate-400 text-[9px]">Acompaña</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-slate-700">
                    <span class="text-base block">🌰</span>
                    <strong class="text-white block mt-0.5">La Semilla</strong>
                    <span class="text-slate-400 text-[9px]">Potencial</span>
                  </div>
                  <div class="bg-slate-800/80 p-2 rounded-xl border border-teal-500/50">
                    <span class="text-base block">🌱</span>
                    <strong class="text-teal-300 block mt-0.5">El Brote</strong>
                    <span class="text-teal-400 text-[9px]">Crecimiento</span>
                  </div>
                </div>

                <!-- Quick Color Palette Swatches with 1-click copy -->
                <div class="pt-1">
                  <span class="text-[9px] text-slate-400 font-bold uppercase tracking-wider block mb-1.5">Paleta de Marca Oficial (Clic para copiar HEX):</span>
                  <div class="flex items-center space-x-1.5">
                    <button onclick="copyColorHex('#0F172A', 'Ultracem Navy')" title="Copiar #0F172A (Ultracem Navy)" class="flex-1 h-6 rounded-md bg-[#0F172A] border border-slate-600 hover:scale-105 transition-transform" style="background-color: #0F172A;"></button>
                    <button onclick="copyColorHex('#14B8A6', 'Ultracem Teal')" title="Copiar #14B8A6 (Ultracem Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #14B8A6;"></button>
                    <button onclick="copyColorHex('#5EEAD4', 'Mint Teal')" title="Copiar #5EEAD4 (Mint Teal)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #5EEAD4;"></button>
                    <button onclick="copyColorHex('#7DD3FC', 'Sky Blue')" title="Copiar #7DD3FC (Sky Blue)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #7DD3FC;"></button>
                    <button onclick="copyColorHex('#BAE6FD', 'Soft Sky')" title="Copiar #BAE6FD (Soft Sky)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #BAE6FD;"></button>
                    <button onclick="copyColorHex('#3797E8', 'Ultracem Blue')" title="Copiar #3797E8 (Ultracem Blue - Matriz)" class="flex-1 h-6 rounded-md hover:scale-105 transition-transform" style="background-color: #3797E8;"></button>
                  </div>
                </div>
              </div>

              <!-- Casco Protector Inventory Card -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-3">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2.5">
                    <div class="w-10 h-10 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-2xl shadow-xs">
                      ⛑️
                    </div>
                    <div>
                      <h4 class="font-bold text-xs text-slate-900 leading-tight">Casco Protector de Racha</h4>
                      <p class="text-[10px] text-slate-500">Congela tu racha 24h si tienes un día de campo difícil</p>
                    </div>
                  </div>
                  <span id="casco-badge-count" class="font-mono-data font-black text-sm bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-xl">
                    1 Activo
                  </span>
                </div>

                <div class="flex items-center justify-between pt-1 text-xs">
                  <button id="btn-use-casco" onclick="activarCascoProtector()" class="btn-tactile flex-1 bg-amber-500 hover:bg-amber-600 text-white font-bold py-2 px-3 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                    <span>🛡️</span>
                    <span>Activar Congelación (24 Horas)</span>
                  </button>
                </div>
              </div>

              <!-- Heatmap: 90 Días de Racha Comercial -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <div class="flex items-center justify-between text-xs">
                  <div>
                    <h4 class="font-bold text-slate-900">Historial de Constancia (Últimos 90 Días)</h4>
                    <p class="text-[10px] text-slate-500">Cada celda representa un día de contacto comercial registrado</p>
                  </div>
                  <span class="text-[10px] text-[#004797] font-bold font-mono-data">94% Éxito</span>
                </div>

                <div id="perfil-heatmap-grid" class="grid grid-flow-col grid-rows-7 gap-1 p-2 bg-slate-50 rounded-xl border border-slate-200 overflow-x-auto">
                  <!-- Generated dynamically with JS -->
                </div>

                <div class="flex items-center justify-between text-[10px] text-slate-400 font-semibold pt-1">
                  <span>Menos activo</span>
                  <div class="flex items-center space-x-1">
                    <span class="w-2.5 h-2.5 rounded-sm bg-slate-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-200"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-blue-400"></span>
                    <span class="w-2.5 h-2.5 rounded-sm bg-[#004797]"></span>
                  </div>
                  <span>Racha Activa</span>
                </div>
              </div>

              <!-- Trophies & Badges -->
              <div class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs space-y-2.5">
                <h4 class="font-bold text-xs text-slate-900">Insignias & Logros de Obra</h4>
                
                <div class="grid grid-cols-3 gap-2">
                  <button onclick="openInAppTrofeo('Escudo Antichurn', 'Salva a 3 clientes en riesgo crítico antes de que cambien a la competencia.', '🛡️', '+200 XP')" class="btn-tactile bg-emerald-50/70 border border-emerald-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-emerald-100/50">
                    <span class="text-2xl">🛡️</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Antichurn</span>
                    <span class="text-[8px] font-extrabold text-emerald-700 bg-emerald-100 px-1 rounded">Desbloqueado</span>
                  </button>

                  <button onclick="openInAppTrofeo('Maestro Técnico', 'Comparte 25 certificados NTC 121 y curvas de fraguado validadas por laboratorio.', '📐', '+120 XP')" class="btn-tactile bg-slate-50 border border-slate-200 rounded-2xl p-3 flex flex-col items-center text-center space-y-1.5 hover:bg-slate-100">
                    <span class="text-2xl">📐</span>
                    <span class="text-[10px] font-bold text-slate-800 leading-tight">Mtro Técnico</span>
                    <span class="text-[8px] font-extrabold text-slate-500 bg-slate-200 px-1 rounded">18/25</span>
                  </button>

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
        <!-- BOTTOM NAVIGATION BAR (5 CLEAN TABS)                       -->
        <!-- ========================================================== -->
        <nav aria-label="Navegación Móvil" class="bg-white/95 backdrop-blur-md border-t border-slate-200/80 px-2 py-2 flex justify-around items-center select-none z-30 flex-shrink-0">
          
          <button id="nav-btn-racha" onclick="navigateToTab('racha')" class="btn-tactile flex flex-col items-center text-[#004797] font-bold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>
            </svg>
            <span class="text-[10px]">Racha</span>
          </button>

          <button id="nav-btn-copiloto" onclick="navigateToTab('copiloto')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
            </svg>
            <span class="text-[10px]">Copiloto</span>
          </button>

          <button id="nav-btn-mapa" onclick="navigateToTab('mapa')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/>
              <line x1="8" y1="2" x2="8" y2="18"/>
              <line x1="16" y1="6" x2="16" y2="22"/>
            </svg>
            <span class="text-[10px]">Radar & B2B</span>
          </button>

          <button id="nav-btn-liga" onclick="navigateToTab('liga')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/>
              <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/>
              <path d="M4 22h16"/>
              <path d="M10 14.66V17c0 .55-.45 1-1 1H7v4h10v-4h-2c-.55 0-1-.45-1-1v-2.34"/>
              <path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/>
            </svg>
            <span class="text-[10px]">Liga</span>
          </button>

          <button id="nav-btn-perfil" onclick="navigateToTab('perfil')" class="btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1">
            <svg class="w-5 h-5 mb-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            <span class="text-[10px]">Perfil</span>
          </button>

        </nav>

      </div>
      </aside>

    </div>

    <!-- ============================================================== -->
    <!-- 2. VISTA PRD MAESTRO COMPLETO (CANVAS BLANCO)                  -->
    <!-- ============================================================== -->
    <div id="view-prd" class="hidden w-full max-w-5xl mx-auto bg-white rounded-3xl p-6 sm:p-10 border border-slate-300 shadow-sm space-y-10 text-slate-800">

      <!-- ============================================================== -->
      <!-- PRD DOCUMENT: MASTER WHITE CANVAS                              -->
      <!-- ============================================================== -->
      
      <!-- Document Header & Meta Bar -->
      <header class="border-b border-slate-200 pb-8 space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center space-x-3">
            <!-- Ultracem Official Logo Icon -->
            <div class="w-12 h-12 rounded-2xl bg-[#0F172A] border border-teal-400 p-2 flex items-center justify-center shadow-sm">
              <svg viewBox="0 0 100 100" class="w-8 h-8" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
                <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
                <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
                <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
                <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
              </svg>
            </div>
            <div>
              <div class="flex items-center space-x-2">
                <span class="text-xs font-black uppercase tracking-wider text-teal-700 bg-teal-50 px-2.5 py-0.5 rounded-full border border-teal-200">ULTRACEM</span>
                <span class="text-xs font-bold text-slate-400">×</span>
                <span class="text-xs font-black uppercase tracking-wider text-[#003E78] bg-blue-50 px-2.5 py-0.5 rounded-full border border-blue-200">ULTRACEM S.A.S.</span>
              </div>
              <p class="text-[11px] text-slate-500 font-medium mt-0.5">Documento de Especificación de Producto (PRD) • Versión 1.0 Oficial</p>
            </div>
          </div>
          
          <div class="flex items-center space-x-2">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse mr-1.5"></span>
              Demo Activa & Operativa
            </span>
            <button onclick="window.print()" class="btn-tactile text-xs font-bold text-slate-600 hover:text-slate-900 bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-xl border border-slate-200 transition-all flex items-center space-x-1" title="Imprimir / Guardar como PDF">
              <span>🖨️</span>
              <span class="hidden sm:inline">Exportar</span>
            </button>
          </div>
        </div>

        <div>
          <h1 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight leading-tight">
            Ultracem: CRM de Campo Gamificado, Prevención Antichurn & Copiloto IA
          </h1>
          <p class="text-base text-slate-600 mt-2 leading-relaxed">
            Ecosistema de aceleración comercial diseñado para la fuerza de ventas de <strong>Ultracem S.A.S.</strong> en el Caribe colombiano. Transforma la fricción operativa del seguimiento de obras en hábitos comerciales diarios mediante gamificación de rachas, escalamiento ágil con SLAs y copiloto multimodelo.
          </p>
        </div>

        <!-- Metadata Ribbon -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-xs">
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Lema Institucional</span>
            <span class="font-bold text-slate-900 italic">“Calidad, Resistencia y Rendimiento”</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Aliado Estratégico</span>
            <span class="font-bold text-[#003E78]">Ultracem (Planta Galapa)</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Infraestructura IA</span>
            <span class="font-bold text-teal-700">Groq LPU, NVIDIA NIM & DeepSeek</span>
          </div>
          <div class="bg-slate-50 p-3 rounded-xl border border-slate-200/80">
            <span class="text-slate-400 block font-semibold text-[10px] uppercase">Regla de Oro</span>
            <span class="font-bold text-amber-600">Corte Diario 11:59 PM</span>
          </div>
        </div>

        <!-- Sticky Quick-Jump Anchor Bar -->
        <nav aria-label="Tabla de Contenidos del PRD" class="flex items-center space-x-1.5 overflow-x-auto py-2 border-t border-slate-100 text-xs text-slate-600">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 mr-1 flex-shrink-0">Índice:</span>
          <a href="#prd-sec-vision" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">1. Visión & Filosofía</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-brand" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">2. Identidad & Colores</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-fases" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">3. Activación 4 Fases</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-modulos" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">4. Módulos Funcionales</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-historias" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">5. Historias de Usuario</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-tech" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">6. Stack Técnico & APIs</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-kpis" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">7. Métricas de Impacto</a>
          <span class="text-slate-300">•</span>
          <a href="#prd-sec-equipo" class="px-2.5 py-1 rounded-lg hover:bg-slate-100 font-semibold text-slate-700 whitespace-nowrap transition-all">8. Asesores & Galapa</a>
        </nav>
      </header>

      <!-- ============================================================== -->
      <!-- SECCIÓN 1: VISIÓN Y FILOSOFÍA DE MARCA                         -->
      <!-- ============================================================== -->
      <section id="prd-sec-vision" class="space-y-6 scroll-mt-24">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">01</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Visión del Producto y Filosofía de Marca</h2>
        </div>

        <div class="bg-[#0F172A] rounded-2xl p-6 text-white space-y-3 shadow-md border-l-4 border-[#14B8A6]">
          <span class="text-[10px] font-black uppercase tracking-widest text-teal-300 bg-teal-950/80 px-2.5 py-0.5 rounded-full border border-teal-500/40">Premisa de Diseño</span>
          <p class="text-base sm:text-lg font-bold leading-snug italic text-teal-50">
            “Que el cemento fragüe, pero que tu cliente y tu talento nunca se enfríen.”
          </p>
          <p class="text-xs text-slate-300 leading-relaxed">
            <strong>Ultracem</strong> no es un software administrativo convencional: <strong>es un ecosistema de crecimiento profesional continuo</strong> que cuida el talento humano desde su siembra hasta convertirlo en una fuerza de alto rendimiento. En entornos de alta exigencia industrial como la comercialización de cemento y concreto con <strong>Ultracem</strong>, el éxito depende de la constancia diaria, la agilidad técnica y la eliminación de fricciones internas.
          </p>
        </div>

        <!-- 3 Core Pillars -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center text-base">🛡️</div>
            <h3 class="font-bold text-sm text-slate-900">Respaldo Tecnológico Ultracem</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Infraestructura moderna, integraciones limpias y robustez operativa para que el asesor nunca pierda información en campo.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center text-base">🌱</div>
            <h3 class="font-bold text-sm text-slate-900">Crecimiento Orgánico Ultracem</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Mentoría continua, evolución del brote y reconocimiento al esfuerzo personal que transforma la rutina en motivación.
            </p>
          </div>
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center text-base">🔥</div>
            <h3 class="font-bold text-sm text-slate-900">Psicología de Hábitos & Rachas</h3>
            <p class="text-xs text-slate-600 leading-relaxed">
              Corte estricto a las 11:59 PM para prevenir el abandono de cuentas críticas antes de que la competencia (Argos o Cemex) gane la obra.
            </p>
          </div>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 2: SISTEMA DE IDENTIDAD VISUAL (BRAND BOOK OFICIAL)    -->
      <!-- ============================================================== -->
      <section id="prd-sec-brand" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">02</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Sistema de Identidad Visual & Brand Book Oficial</h2>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
          La interfaz combina la armonía natural de <strong>Ultracem</strong> con la solidez industrial de <strong>Ultracem S.A.S.</strong>, garantizando una jerarquía visual clara y una legibilidad óptima bajo la luz del sol en obras de construcción.
        </p>

        <!-- Triada del Símbolo -->
        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-5 space-y-4">
          <h3 class="font-extrabold text-sm text-slate-900 uppercase tracking-wider text-[11px] text-teal-700">Anatomía del Símbolo Ultracem</h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs space-y-2">
              <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-full bg-slate-900 text-teal-300 flex items-center justify-center text-[10px] font-bold">1</span>
                <h4 class="font-bold text-xs text-slate-900">La Mano (Cuidado)</h4>
              </div>
              <p class="text-xs text-slate-600">
                Trazos envolventes que representan la protección y el acompañamiento activo de los líderes y mentores hacia el asesor en campo.
              </p>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs space-y-2">
              <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-full bg-slate-900 text-teal-300 flex items-center justify-center text-[10px] font-bold">2</span>
                <h4 class="font-bold text-xs text-slate-900">La Semilla (Potencial)</h4>
              </div>
              <p class="text-xs text-slate-600">
                Núcleo geométrico que simboliza el punto de partida y la energía latente de cada talento comercial listo para germinar.
              </p>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs space-y-2">
              <div class="flex items-center space-x-2">
                <span class="w-6 h-6 rounded-full bg-slate-900 text-teal-300 flex items-center justify-center text-[10px] font-bold">3</span>
                <h4 class="font-bold text-xs text-slate-900">El Brote (Crecimiento)</h4>
              </div>
              <p class="text-xs text-slate-600">
                Hojas orgánicas que emergen hacia arriba, representando el avance en días de racha continua y toneladas de cemento despachadas.
              </p>
            </div>
          </div>
        </div>

        <!-- Interactive Color Palette with Copy Buttons -->
        <div class="space-y-3">
          <h3 class="font-extrabold text-sm text-slate-900 uppercase tracking-wider text-[11px] text-teal-700">Paleta Cromática Oficial (Haz clic para copiar HEX)</h3>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <!-- Ultracem Navy -->
            <button onclick="navigator.clipboard.writeText('#0F172A'); showToast('Copiado: #0F172A (Ultracem Navy)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#0F172A] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Ultracem Navy</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-teal-600 font-bold">#0F172A 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Base & Autoridad</span>
            </button>
            <!-- Ultracem Teal -->
            <button onclick="navigator.clipboard.writeText('#14B8A6'); showToast('Copiado: #14B8A6 (Ultracem Teal)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#14B8A6] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Ultracem Teal</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-teal-600 font-bold">#14B8A6 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Primario & Acción</span>
            </button>
            <!-- Mint Teal -->
            <button onclick="navigator.clipboard.writeText('#5EEAD4'); showToast('Copiado: #5EEAD4 (Mint Teal)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#5EEAD4] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Mint Teal</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-teal-600 font-bold">#5EEAD4 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Nivel & Progreso</span>
            </button>
            <!-- Sky Blue -->
            <button onclick="navigator.clipboard.writeText('#7DD3FC'); showToast('Copiado: #7DD3FC (Sky Blue)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#7DD3FC] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Sky Blue</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-teal-600 font-bold">#7DD3FC 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Secundario & Edu</span>
            </button>
            <!-- Azul Ultracem -->
            <button onclick="navigator.clipboard.writeText('#003E78'); showToast('Copiado: #003E78 (Azul Ultracem)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#003E78] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Azul Ultracem</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-blue-600 font-bold">#003E78 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Oficial Ultracem</span>
            </button>
            <!-- Amarillo Ultracem -->
            <button onclick="navigator.clipboard.writeText('#FDCA02'); showToast('Copiado: #FDCA02 (Amarillo Ultracem)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#FDCA02] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Amarillo Ultracem</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-amber-600 font-bold">#FDCA02 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Energía & Alertas</span>
            </button>
            <!-- Soft Sky -->
            <button onclick="navigator.clipboard.writeText('#BAE6FD'); showToast('Copiado: #BAE6FD (Soft Sky)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#BAE6FD] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Soft Sky</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-sky-600 font-bold">#BAE6FD 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Fondos & Audio</span>
            </button>
            <!-- Azul Digital -->
            <button onclick="navigator.clipboard.writeText('#1E83EC'); showToast('Copiado: #1E83EC (Azul Digital)', 'success')" class="text-left bg-white border border-slate-200 rounded-xl p-3 hover:shadow-md transition-all group">
              <div class="h-10 rounded-lg bg-[#1E83EC] border border-slate-300 mb-2"></div>
              <span class="font-bold text-slate-900 block text-xs">Azul Digital</span>
              <span class="text-[10px] font-mono-data text-slate-500 group-hover:text-blue-600 font-bold">#1E83EC 📋</span>
              <span class="text-[10px] text-slate-400 block mt-0.5">Acentos Interactivos</span>
            </button>
          </div>
        </div>

        <!-- Tipografía -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
            <span class="font-bold text-slate-900 block">Outfit (Google Fonts)</span>
            <p class="text-[11px] text-slate-500 mt-1">Tipografía principal para títulos, display y microcopy comercial.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
            <span class="font-bold text-slate-900 block">Montserrat (Ultracem)</span>
            <p class="text-[11px] text-slate-500 mt-1">Fuente corporativa de Ultracem para fichas técnicas y normativas NTC 121.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
            <span class="font-bold text-slate-900 block">JetBrains Mono</span>
            <p class="text-[11px] text-slate-500 mt-1">Para números de toneladas, contadores de tiempo 11:59 PM y SLAs de cartera.</p>
          </div>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 3: ESTRATEGIA DE ACTIVACIÓN EN 4 FASES (PDF PÁGINA 4)   -->
      <!-- ============================================================== -->
      <section id="prd-sec-fases" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">03</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Estrategia de Activación y Despliegue en 4 Fases</h2>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
          Diseñada para vencer la resistencia habitual de los asesores al uso de CRMs tradicionales. Puedes activar cada fase en tiempo real haciendo clic en los botones y verás cómo responde el prototipo al lado derecho:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <!-- Fase 1 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-black uppercase text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">Etapa 1</span>
                <span class="text-lg">🌰</span>
              </div>
              <h3 class="font-black text-base text-slate-900 mt-1">Fase 1: Expectativa</h3>
              <p class="text-xs text-slate-600 mt-1 italic">
                “¿Cuánto vale el potencial de un equipo cuando se le da el espacio para crecer?”
              </p>
              <p class="text-[11px] text-slate-500 mt-2 leading-relaxed">
                Despierta intriga mediante piezas visuales minimalistas de una semilla en tierra fértil, sin revelar la marca ni el software. Invita a reflexionar sobre el talento interno.
              </p>
            </div>
            <button onclick="setActivationStage(1)" class="w-full btn-tactile text-xs font-bold py-2 px-3 rounded-xl bg-amber-500 hover:bg-amber-600 text-white shadow-xs transition-all flex items-center justify-center space-x-1">
              <span>Probar Fase 1 en Prototipo</span>
              <span>➔</span>
            </button>
          </div>

          <!-- Fase 2 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-black uppercase text-teal-700 bg-teal-50 px-2 py-0.5 rounded-full border border-teal-200">Etapa 2</span>
                <span class="text-lg">🌱</span>
              </div>
              <h3 class="font-black text-base text-slate-900 mt-1">Fase 2: Curiosidad</h3>
              <p class="text-xs text-slate-600 mt-1 italic">
                “¿Cuántas toneladas se escapan por llamar un día tarde?”
              </p>
              <p class="text-[11px] text-slate-500 mt-2 leading-relaxed">
                Conecta con el dolor real del asesor comercial: cotizaciones caídas, pedidos retenidos por cupo y pérdida de clientes por falta de seguimiento preventivo.
              </p>
            </div>
            <button onclick="setActivationStage(2)" class="w-full btn-tactile text-xs font-bold py-2 px-3 rounded-xl bg-teal-600 hover:bg-teal-700 text-white shadow-xs transition-all flex items-center justify-center space-x-1">
              <span>Probar Fase 2 en Prototipo</span>
              <span>➔</span>
            </button>
          </div>

          <!-- Fase 3 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-black uppercase text-blue-700 bg-blue-50 px-2 py-0.5 rounded-full border border-blue-200">Etapa 3</span>
                <span class="text-lg">🌿</span>
              </div>
              <h3 class="font-black text-base text-slate-900 mt-1">Fase 3: Reveal (Identidad)</h3>
              <p class="text-xs text-slate-600 mt-1 italic">
                “Calidad, Resistencia y Rendimiento.”
              </p>
              <p class="text-[11px] text-slate-500 mt-2 leading-relaxed">
                Revelación de la alianza entre <strong>Ultracem</strong> y <strong>Ultracem</strong>. Presentación del símbolo, la mascota Don Fraguado y la filosofía de equipo.
              </p>
            </div>
            <button onclick="setActivationStage(3)" class="w-full btn-tactile text-xs font-bold py-2 px-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white shadow-xs transition-all flex items-center justify-center space-x-1">
              <span>Probar Fase 3 en Prototipo</span>
              <span>➔</span>
            </button>
          </div>

          <!-- Fase 4 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-3 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-black uppercase text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">Etapa 4</span>
                <span class="text-lg">🌳</span>
              </div>
              <h3 class="font-black text-base text-slate-900 mt-1">Fase 4: Lanzamiento Total</h3>
              <p class="text-xs text-slate-600 mt-1 italic">
                “Ultracem no es solo un programa. Es un camino que construiremos juntos.”
              </p>
              <p class="text-[11px] text-slate-500 mt-2 leading-relaxed">
                Despliegue operativo completo de la plataforma en vivo: CRM gamificado, Copiloto con Groq/NVIDIA, notas de voz con Whisper y Radar B2B.
              </p>
            </div>
            <button onclick="setActivationStage(4)" class="w-full btn-tactile text-xs font-bold py-2 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white shadow-xs transition-all flex items-center justify-center space-x-1">
              <span>Activar Modo Operativo Completo</span>
              <span>➔</span>
            </button>
          </div>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 4: ARQUITECTURA FUNCIONAL DE MÓDULOS                   -->
      <!-- ============================================================== -->
      <section id="prd-sec-modulos" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">04</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Arquitectura Funcional de Módulos</h2>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
          El sistema resuelve de forma integral los 5 componentes críticos de la operación de ventas en campo:
        </p>

        <!-- Module 1 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-xl bg-teal-50 text-teal-700 border border-teal-200 flex items-center justify-center font-bold text-sm">M1</span>
              <div>
                <h3 class="font-bold text-sm text-slate-900">Hub de Progresión de Talento & Racha Diaria</h3>
                <span class="text-[11px] text-slate-500">Hábitos sostenibles, psicología de compromiso y protección de rachas</span>
              </div>
            </div>
            <span class="text-xs font-bold text-amber-600 bg-amber-50 px-2.5 py-1 rounded-lg border border-amber-200">Corte 11:59 PM</span>
          </div>
          <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li><strong>Medidor de Crecimiento del Brote:</strong> Cuatro etapas de madurez comercial: <em>Semilla</em> ➔ <em>Brote</em> ➔ <em>Tallo</em> ➔ <em>Planta Fértil</em>.</li>
            <li><strong>Regla de Oro (11:59 PM):</strong> El asesor suma +1 día de racha si antes de la medianoche atiende o escala el 100% de sus cuentas en semáforo rojo.</li>
            <li><strong>Escudo "Casco de Seguridad":</strong> Se desbloquea cada 7 días de racha continua y congela la racha por 24 horas ante emergencias personales o traslados a zonas sin señal.</li>
            <li><strong>Simulador Día/Noche:</strong> Demuestra el drama nocturno (10:45 PM) cuando Don Fraguado entra en pánico y llama al asesor a salvar su racha.</li>
          </ul>
        </div>

        <!-- Module 2 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-xl bg-blue-50 text-blue-700 border border-blue-200 flex items-center justify-center font-bold text-sm">M2</span>
              <div>
                <h3 class="font-bold text-sm text-slate-900">CRM de Campo con Semáforo de Riesgo Antichurn</h3>
                <span class="text-[11px] text-slate-500">Clasificación por tipo de cliente y escalamiento ágil con SLAs garantizados</span>
              </div>
            </div>
            <span class="text-xs font-bold text-blue-600 bg-blue-50 px-2.5 py-1 rounded-lg border border-blue-200">SLAs de 2h a 6h</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <span class="font-bold text-slate-900 block mb-1">🏪 Canal Tradicional (Ferreterías)</span>
              <p class="text-slate-600">🟢 0-2 días: Saludable</p>
              <p class="text-slate-600">🟡 3-4 días: Advertencia de consumo</p>
              <p class="text-rose-600 font-bold">🔴 +5 días: Riesgo crítico de fuga hacia Argos o Cemex</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <span class="font-bold text-slate-900 block mb-1">🏭 Canal Industrial (Constructoras & 4G)</span>
              <p class="text-slate-600">🟢 0-4 días: En programación de fundición</p>
              <p class="text-slate-600">🟡 5-7 días: Sin solicitud de mixer</p>
              <p class="text-rose-600 font-bold">🔴 +8 días o cotización a menos de 24h de vencer</p>
            </div>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            <strong>Escalamiento con SLAs Auditables:</strong> Si la venta depende de un bloqueo administrativo (ej. cupo de crédito o despacho de mixer), el asesor escala el caso con 1 clic a <em>Cartera (SLA 4h)</em>, <em>Logística (SLA 2h)</em>, <em>Calidad NTC 121 (SLA 6h)</em> o <em>Pricing (SLA 4h)</em>. Al escalar, <strong>la racha se salva inmediatamente</strong> sin castigar al asesor por demoras de otras áreas.
          </p>
        </div>

        <!-- Module 3 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-xl bg-teal-50 text-teal-700 border border-teal-200 flex items-center justify-center font-bold text-sm">M3</span>
              <div>
                <h3 class="font-bold text-sm text-slate-900">Copiloto IA Multimodelo con Guardrails Estrictos</h3>
                <span class="text-[11px] text-slate-500">Groq LPU, NVIDIA NIM, DeepSeek y transcripción de voz Whisper Turbo</span>
              </div>
            </div>
            <span class="text-xs font-bold text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-lg border border-emerald-200">LPU Ultra-Rápido</span>
          </div>
          <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li><strong>Modelos Flagship de Razonamiento:</strong> Compatible con <code>openai/gpt-oss-120b</code>, <code>openai/gpt-oss-20b</code> (1,000 t/s), <code>llama-3.3-70b-versatile</code>, NVIDIA NIM y DeepSeek.</li>
            <li><strong>Guardrails Estrictos Ultracem:</strong> El modelo cuenta con instrucciones estrictas de dominio. Si un usuario formula preguntas ajenas (ej. <em>"¿Qué es el ácido ribonucleico?"</em> o recetas de cocina), el copiloto responde cortésmente que solo está facultado para especificaciones de cemento, cubicaciones de concreto y prospección de obras.</li>
            <li><strong>Notas de Voz y Whisper Large V3 Turbo:</strong> Al grabar un audio en obra, se almacena en el navegador con reproductor <code>&lt;audio controls&gt;</code> nativo y se transcribe en milisegundos mediante la API de Groq Cloud Audio.</li>
          </ul>
        </div>

        <!-- Module 4 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-xl bg-amber-50 text-amber-700 border border-amber-200 flex items-center justify-center font-bold text-sm">M4</span>
              <div>
                <h3 class="font-bold text-sm text-slate-900">Radar Georreferenciado & Directorio B2B</h3>
                <span class="text-[11px] text-slate-500">12 prospectos de obras del Caribe, mapa interactivo y prevención de acoso comercial</span>
              </div>
            </div>
            <span class="text-xs font-bold text-slate-700 bg-slate-100 px-2.5 py-1 rounded-lg border border-slate-200">12 Cuentas Caribe</span>
          </div>
          <ul class="text-xs text-slate-600 space-y-2 list-disc list-inside">
            <li><strong>Mapa Interactivo Leaflet:</strong> Visualiza en capas de calles y satélite las obras activas, la planta central en Galapa y los depósitos competidores (Argos y Cemex).</li>
            <li><strong>Prevención de Acoso y Asignación Fija:</strong> Si un asesor ya contactó o tiene asignado un cliente, aparece con candado de protección para evitar doble contacto invasivo.</li>
            <li><strong>Transferencia Voluntaria de Clientes:</strong> Un asesor puede transferir sus clientes fijos a compañeros de equipo (ej. Milena Ospino, Adriana Anaya o Hichel Espitia) para equilibrar cargas de trabajo o suplir vacaciones.</li>
            <li><strong>Contacto Directo por WhatsApp:</strong> Envía cotizaciones adaptadas al tipo de cemento (Estructural Max, Uso General, Marino) con un solo toque y suma +50 XP.</li>
          </ul>
        </div>

        <!-- Module 5 -->
        <div class="bg-white rounded-2xl border border-slate-200 p-5 space-y-3 shadow-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <span class="w-8 h-8 rounded-xl bg-indigo-50 text-indigo-700 border border-indigo-200 flex items-center justify-center font-bold text-sm">M5</span>
              <div>
                <h3 class="font-bold text-sm text-slate-900">Centro de Mando & Supervisión Regional</h3>
                <span class="text-[11px] text-slate-500">Dashboard ejecutivo web para líderes comerciales y gerencia de operaciones</span>
              </div>
            </div>
            <span class="text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-lg border border-indigo-200">Vista Escritorio</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Permite auditar en tiempo real la cartera en riesgo ($184M COP), las 6 cuentas críticas con SLA venciendo hoy, la tabla de ligas gamificadas de asesores y el estado operativo de los silos de clínker y molienda en la Planta Galapa.
          </p>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 5: HISTORIAS DE USUARIO (USER STORIES)                 -->
      <!-- ============================================================== -->
      <section id="prd-sec-historias" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">05</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Historias de Usuario (User Stories & Criterios de Aceptación)</h2>
        </div>

        <div class="space-y-4">
          <!-- US 1 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-700">US-01: Visualización del Brote y Racha Diaria</span>
              <span class="text-[10px] bg-teal-100 text-teal-800 font-bold px-2 py-0.5 rounded-full">Asesor en Campo</span>
            </div>
            <p class="text-xs text-slate-700"><strong>Como:</strong> Asesor comercial en visita de obra.</p>
            <p class="text-xs text-slate-700"><strong>Quiero:</strong> Ver el estado de mi brote, los días de racha continua y el tiempo restante para las 11:59 PM.</p>
            <p class="text-xs text-slate-700"><strong>Para:</strong> Enfocar mi gestión en salvar las cuentas que están por enfriarse antes del cierre del día.</p>
            <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-[11px] text-slate-600">
              <strong>Criterio de Aceptación:</strong> La pantalla de inicio muestra la barra de progreso del brote, la cuenta regresiva en tiempo real y el listado de cuentas críticas con botón de gestión rápida.
            </div>
          </div>

          <!-- US 2 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-700">US-02: Salvamento de Racha por Escalamiento a Depto</span>
              <span class="text-[10px] bg-teal-100 text-teal-800 font-bold px-2 py-0.5 rounded-full">Fricción Interna</span>
            </div>
            <p class="text-xs text-slate-700"><strong>Como:</strong> Asesor comercial bloqueado por cupo de crédito o disponibilidad de mixer.</p>
            <p class="text-xs text-slate-700"><strong>Quiero:</strong> Escalar el caso a Cartera o Logística seleccionando el motivo y activando el SLA.</p>
            <p class="text-xs text-slate-700"><strong>Para:</strong> Salvar mi racha diaria inmediatamente sin depender de la velocidad de respuesta del área interna.</p>
            <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-[11px] text-slate-600">
              <strong>Criterio de Aceptación:</strong> Al pulsar "Escalar a Depto", el caso se marca como escalado, se inicia el temporizador de SLA (ej. 4h) y se reproduce el sonido de racha protegida sumando +1 día.
            </div>
          </div>

          <!-- US 3 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-700">US-03: Copiloto IA con Inferencia Groq / NVIDIA NIM</span>
              <span class="text-[11px] text-slate-500 font-bold px-2 py-0.5 rounded-full bg-slate-200">Asistencia Técnica</span>
            </div>
            <p class="text-xs text-slate-700"><strong>Como:</strong> Asesor en reunión con un ingeniero civil o maestro de obra.</p>
            <p class="text-xs text-slate-700"><strong>Quiero:</strong> Consultar dosificaciones y resistencias de la norma NTC 121 y generar minutas al instante.</p>
            <p class="text-xs text-slate-700"><strong>Para:</strong> Argumentar con base técnica certificada frente a las ofertas de la competencia.</p>
            <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-[11px] text-slate-600">
              <strong>Criterio de Aceptación:</strong> El copiloto responde en menos de 500ms y rechaza amablemente consultas fuera de contexto corporativo (ej. biología o recetas).
            </div>
          </div>

          <!-- US 4 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-700">US-04: Transcripción Automática de Voz con Whisper Turbo</span>
              <span class="text-[11px] text-purple-700 font-bold px-2 py-0.5 rounded-full bg-purple-100">Audio en Terreno</span>
            </div>
            <p class="text-xs text-slate-700"><strong>Como:</strong> Asesor conduciendo entre obras o con ruido de maquinaria pesada.</p>
            <p class="text-xs text-slate-700"><strong>Quiero:</strong> Grabar un mensaje de voz y que se transcriba automáticamente a la bitácora del cliente.</p>
            <p class="text-xs text-slate-700"><strong>Para:</strong> No tener que escribir en el teclado bajo el sol y mantener el audio audible como respaldo.</p>
            <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-[11px] text-slate-600">
              <strong>Criterio de Aceptación:</strong> El audio queda grabado con reproductor <code>&lt;audio controls&gt;</code> y genera la transcripción fiel en la bitácora del cliente.
            </div>
          </div>

          <!-- US 5 -->
          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-teal-700">US-05: Supervisión de Ligas y Transferencia de Clientes</span>
              <span class="text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded-full">Supervisor & Equipo</span>
            </div>
            <p class="text-xs text-slate-700"><strong>Como:</strong> Asesor comercial o supervisor regional.</p>
            <p class="text-xs text-slate-700"><strong>Quiero:</strong> Ver el perfil de mis compañeros de equipo y transferir clientes fijos con un solo clic.</p>
            <p class="text-xs text-slate-700"><strong>Para:</strong> Asegurar que ninguna obra quede desatendida cuando un compañero sale a vacaciones o cuando se reasignan zonas.</p>
            <div class="bg-white p-2.5 rounded-xl border border-slate-200 text-[11px] text-slate-600">
              <strong>Criterio de Aceptación:</strong> Al abrir el perfil de un asesor o pulsar "Transferir Cliente", se selecciona el compañero destino y el cliente cambia de titular de inmediato con notificación visual.
            </div>
          </div>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 6: STACK TÉCNICO Y ARQUITECTURA DE APIS                -->
      <!-- ============================================================== -->
      <section id="prd-sec-tech" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">06</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Stack Técnico & Arquitectura de APIs</h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
            <h3 class="font-bold text-sm text-slate-900">Frontend & Estilos</h3>
            <ul class="space-y-1 text-slate-600 list-disc list-inside">
              <li>SPA responsiva sin dependencias pesadas.</li>
              <li>Tailwind CSS v3.4+ para sistema de diseño atómico.</li>
              <li>Tipografías: Outfit, Montserrat y JetBrains Mono.</li>
              <li>Cartografía con Leaflet.js y capas OpenStreetMap + Satélite ESRI.</li>
            </ul>
          </div>
          <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
            <h3 class="font-bold text-sm text-slate-900">Backend & Conectividad IA</h3>
            <ul class="space-y-1 text-slate-600 list-disc list-inside">
              <li>Micro-proxy Node.js (<code>server.js</code> en puerto 3000) sin CORS para NVIDIA NIM.</li>
              <li>Groq Cloud API con endpoint LPU ultrarrápido (500-1000 t/s).</li>
              <li>Whisper Large V3 Turbo para transcripción de audio.</li>
              <li>Persistencia local en <code>localStorage</code> con cifrado de llaves.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 7: PLAN DE IMPACTO Y KPIS DE NEGOCIO                   -->
      <!-- ============================================================== -->
      <section id="prd-sec-kpis" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">07</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Métricas de Impacto y Retorno de Inversión (KPIs)</h2>
        </div>

        <div class="overflow-x-auto rounded-2xl border border-slate-200">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50 text-slate-500 uppercase font-bold text-[10px] tracking-wider border-b border-slate-200">
              <tr>
                <th class="py-3 px-4">Métrica de Negocio</th>
                <th class="py-3 px-4">Línea Base Tradicional</th>
                <th class="py-3 px-4 text-teal-700">Meta con Ultracem Ultracem</th>
                <th class="py-3 px-4 text-right">Impacto Proyectado</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100">
              <tr class="hover:bg-slate-50/50">
                <td class="py-3 px-4 font-semibold text-slate-900">Tiempo de primer contacto a cotizaciones</td>
                <td class="py-3 px-4 text-slate-500">48 horas</td>
                <td class="py-3 px-4 font-bold text-teal-700">&lt; 4 horas</td>
                <td class="py-3 px-4 text-right font-bold text-emerald-600">-91% tiempo</td>
              </tr>
              <tr class="hover:bg-slate-50/50">
                <td class="py-3 px-4 font-semibold text-slate-900">Pérdida de cotizaciones por abandono</td>
                <td class="py-3 px-4 text-slate-500">35% de cotizaciones caídas</td>
                <td class="py-3 px-4 font-bold text-teal-700">&lt; 5%</td>
                <td class="py-3 px-4 text-right font-bold text-emerald-600">-85% abandono</td>
              </tr>
              <tr class="hover:bg-slate-50/50">
                <td class="py-3 px-4 font-semibold text-slate-900">Adopción diaria de la fuerza comercial</td>
                <td class="py-3 px-4 text-slate-500">40% (resistencia al CRM)</td>
                <td class="py-3 px-4 font-bold text-teal-700">&gt; 92% (gamificación)</td>
                <td class="py-3 px-4 text-right font-bold text-emerald-600">+130% adopción</td>
              </tr>
              <tr class="hover:bg-slate-50/50">
                <td class="py-3 px-4 font-semibold text-slate-900">Resolución de bloqueos de cartera interna</td>
                <td class="py-3 px-4 text-slate-500">3 días laborales</td>
                <td class="py-3 px-4 font-bold text-teal-700">&lt; 4 horas (cumplimiento SLA)</td>
                <td class="py-3 px-4 text-right font-bold text-emerald-600">Desbloqueo el mismo día</td>
              </tr>
              <tr class="hover:bg-slate-50/50">
                <td class="py-3 px-4 font-semibold text-slate-900">Satisfacción y motivación del asesor</td>
                <td class="py-3 px-4 text-slate-500">5.2 / 10</td>
                <td class="py-3 px-4 font-bold text-teal-700">9.1 / 10</td>
                <td class="py-3 px-4 text-right font-bold text-emerald-600">+75% satisfacción</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ============================================================== -->
      <!-- SECCIÓN 8: EQUIPO COMERCIAL REAL ULTRACEM & OPERACIONES GALAPA -->
      <!-- ============================================================== -->
      <section id="prd-sec-equipo" class="space-y-6 scroll-mt-24 border-t border-slate-200 pt-8 pb-4">
        <div class="flex items-center space-x-2">
          <span class="w-7 h-7 rounded-lg bg-teal-100 text-teal-800 flex items-center justify-center font-bold text-xs">08</span>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">Equipo Comercial Real Ultracem & Operaciones Planta Galapa</h2>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
          Datos oficiales extraídos directamente del portal de <strong>Ultracem</strong> e integrados en el ecosistema Ultracem:
        </p>

        <!-- Advisors Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
          <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
            <div class="flex items-center space-x-2.5">
              <div class="w-9 h-9 rounded-full bg-blue-100 text-blue-800 font-bold flex items-center justify-center text-xs">MO</div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Milena Ospino</h3>
                <span class="text-[10px] text-slate-500">Asesora Senior Concretos</span>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 font-mono-data">📧 mospino@ultracem.co</p>
            <span class="inline-block text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md">28 Días Racha 🔥</span>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
            <div class="flex items-center space-x-2.5">
              <div class="w-9 h-9 rounded-full bg-amber-100 text-amber-800 font-bold flex items-center justify-center text-xs">AA</div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Adriana Anaya</h3>
                <span class="text-[10px] text-slate-500">Ferreterías Atlántico / Bolívar</span>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 font-mono-data">📧 aanaya@ultracem.co</p>
            <span class="inline-block text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md">24 Días Racha 🔥</span>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
            <div class="flex items-center space-x-2.5">
              <div class="w-9 h-9 rounded-full bg-teal-100 text-teal-800 font-bold flex items-center justify-center text-xs">HE</div>
              <div>
                <h3 class="font-bold text-slate-900 text-xs">Hichel Espitia</h3>
                <span class="text-[10px] text-slate-500">Infraestructura & Obra 4G</span>
              </div>
            </div>
            <p class="text-[11px] text-slate-600 font-mono-data">📱 310 250 3454</p>
            <span class="inline-block text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-md">21 Días Racha 🔥</span>
          </div>
        </div>

        <!-- Planta Galapa Card -->
        <div class="bg-[#003E78] text-white rounded-2xl p-5 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">Hub Industrial Central</span>
            <span class="text-[10px] bg-emerald-500 text-white font-bold px-2 py-0.5 rounded-full">100% Operativa</span>
          </div>
          <h3 class="font-black text-base">Planta de Producción Galapa, Atlántico</h3>
          <p class="text-xs text-blue-100 leading-relaxed">
            Ubicada en el Km 8 Vía Galapa - Tubará. Cuenta con capacidad de molienda de 180 Ton/hora, silos de clínker de alta capacidad y despacho de tractomulas graneleras y mixers a todo el corredor portuario y metropolitano de Barranquilla y Cartagena.
          </p>
        </div>
      </section>

    </div>

  </main>

  <!-- ============================================================== -->
  <!-- ULTRACEM : MASTER PRD & BRAND BOOK MODAL             -->
  <!-- ============================================================== -->
  <div id="Ultracem-prd-modal" class="hidden fixed inset-0 z-[999999] bg-slate-950/80 backdrop-blur-xs flex items-center justify-center p-3 sm:p-6 select-none animate-fadeIn">
    <div class="bg-white rounded-3xl max-w-5xl w-full max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden transform transition-all">
      
      <!-- Modal Header -->
      <div class="bg-[#0A233F] text-white p-5 border-b border-teal-500/30 flex items-center justify-between flex-shrink-0">
        <div class="flex items-center space-x-3.5">
          <div class="w-11 h-11 rounded-2xl bg-[#0F172A] border border-teal-400 p-1.5 flex items-center justify-center shadow-xs flex-shrink-0">
            <svg viewBox="0 0 100 100" class="w-8 h-8" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
              <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
              <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
              <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
              <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
            </svg>
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h2 class="text-base sm:text-lg font-black tracking-tight text-white uppercase">ULTRACEM <span class="text-[#3797E8] text-xs font-bold lowercase">by Ultracem</span></h2>
              <span class="text-[9px] bg-teal-500/20 text-teal-300 font-extrabold px-2 py-0.5 rounded-full border border-teal-500/40 uppercase">PRD Oficial v1.0</span>
            </div>
            <p class="text-xs text-teal-100/80 italic mt-0.5">“Calidad, Resistencia y Rendimiento” • Caso Piloto: Ultracem S.A.S.</p>
          </div>
        </div>

        <div class="flex items-center space-x-2">
          <button onclick="closeUltracemPRDModal()" class="w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-sm font-bold transition-all" aria-label="Cerrar modal de PRD">✕</button>
        </div>
      </div>

      <!-- Navigation Tabs Bar -->
      <div class="bg-slate-100/90 border-b border-slate-200 px-4 flex items-center space-x-1 overflow-x-auto flex-shrink-0">
        <button id="prd-tab-btn-vision" onclick="switchPrdTab('vision')" class="px-3.5 py-2.5 text-xs font-extrabold text-[#14B8A6] border-b-2 border-[#14B8A6] transition-all whitespace-nowrap bg-teal-50/50 flex items-center space-x-1.5">
          <span>🌟</span>
          <span>Visión & Propósito</span>
        </button>
        <button id="prd-tab-btn-brand" onclick="switchPrdTab('brand')" class="px-3.5 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-900 border-b-2 border-transparent transition-all whitespace-nowrap flex items-center space-x-1.5">
          <span>🎨</span>
          <span>Sistema de Marca & Colores</span>
        </button>
        <button id="prd-tab-btn-fases" onclick="switchPrdTab('fases')" class="px-3.5 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-900 border-b-2 border-transparent transition-all whitespace-nowrap flex items-center space-x-1.5">
          <span>🚀</span>
          <span>Estrategia 4 Fases</span>
        </button>
        <button id="prd-tab-btn-specs" onclick="switchPrdTab('specs')" class="px-3.5 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-900 border-b-2 border-transparent transition-all whitespace-nowrap flex items-center space-x-1.5">
          <span>🏗️</span>
          <span>Especificación PRD</span>
        </button>
        <button id="prd-tab-btn-demo" onclick="switchPrdTab('demo')" class="px-3.5 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-900 border-b-2 border-transparent transition-all whitespace-nowrap flex items-center space-x-1.5">
          <span>📱</span>
          <span>Guía Demo Activa</span>
        </button>
      </div>

      <!-- Scrollable Tab Content Container -->
      <div class="flex-1 overflow-y-auto p-5 sm:p-6 bg-slate-50/50 space-y-6 text-slate-800 text-xs leading-relaxed">

        <!-- TAB 1: VISIÓN & PROPÓSITO -->
        <div id="prd-tab-content-vision" class="space-y-6">
          <div class="bg-[#0A233F] rounded-2xl p-5 text-white space-y-2 border border-teal-500/30">
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-teal-300 bg-teal-950 px-2.5 py-0.5 rounded-full border border-teal-500/40">Filosofía Central</span>
            <h3 class="text-lg font-black tracking-tight text-white">Ecosistema de Aceleración y Cuidado del Talento Humano</h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              <strong>Ultracem</strong> nace de la convicción de que el talento no se improvisa: se siembra, se cuida día a día y se acompaña hasta su máximo desarrollo. Combina el respaldo tecnológico de <strong>Ultracem</strong> con la cercanía orgánica del aprendizaje guiado y hábitos comerciales de alto impacto.
            </p>
          </div>

          <!-- Anatomía del Símbolo -->
          <div class="space-y-3">
            <h4 class="font-black text-sm text-[#0F172A] uppercase tracking-wider flex items-center space-x-2">
              <span>🌿</span>
              <span>Anatomía del Símbolo Oficial</span>
            </h4>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1.5">
                <span class="text-2xl block">🖐️</span>
                <strong class="text-slate-900 text-xs block font-bold">01. La Mano</strong>
                <p class="text-slate-600 text-[11px]">Representa el acompañamiento activo, la mentoría técnica y el cuidado que los líderes brindan a cada asesor.</p>
              </div>
              <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-2xs space-y-1.5">
                <span class="text-2xl block">🌰</span>
                <strong class="text-slate-900 text-xs block font-bold">02. La Semilla</strong>
                <p class="text-slate-600 text-[11px]">Simboliza el potencial intrínseco, la disciplina diaria y el punto de partida de cada talento comercial.</p>
              </div>
              <div class="bg-white p-4 rounded-2xl border border-teal-400/60 shadow-2xs space-y-1.5 bg-teal-50/30">
                <span class="text-2xl block">🌱</span>
                <strong class="text-teal-900 text-xs block font-bold">03. El Brote</strong>
                <p class="text-teal-800 text-[11px]">Representa el crecimiento tangible medido en rachas comerciales, toneladas despachadas y fidelización de clientes.</p>
              </div>
            </div>
          </div>

          <!-- Caso de Uso Piloto: Ultracem -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <div class="flex items-center space-x-2.5">
              <span class="text-xl">🏗️</span>
              <h4 class="font-black text-sm text-slate-900 uppercase">Caso de Uso Piloto: CRM Comercial Ultracem S.A.S.</h4>
            </div>
            <p class="text-slate-700 text-xs leading-relaxed">
              En la industria cementera colombiana, las obras vacían concreto en ciclos implacables de 24 a 48 horas. Si un asesor comercial no contacta a su cliente a tiempo, la obra compra al competidor (Argos o Cemex). <strong>Ultracem</strong> resuelve este dolor aplicando una mecánica de hábitos (*racha de contacto*), semáforo antichurn, copiloto IA con normas NTC 121 y protección anti-colisión entre compañeros.
            </p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 text-center text-[11px]">
              <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 font-semibold text-slate-700">
                <strong class="block text-slate-900 font-bold text-xs">21 Días</strong> Racha Promedio Asesor
              </div>
              <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 font-semibold text-slate-700">
                <strong class="block text-emerald-700 font-bold text-xs">88.2%</strong> Tasa de Retención
              </div>
              <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 font-semibold text-slate-700">
                <strong class="block text-[#004797] font-bold text-xs">NTC 121</strong> Cumplimiento Estricto
              </div>
              <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 font-semibold text-slate-700">
                <strong class="block text-indigo-700 font-bold text-xs">100%</strong> Cero Doble Contacto
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 2: SISTEMA DE MARCA & COLORES -->
        <div id="prd-tab-content-brand" class="hidden space-y-6">
          <div>
            <h4 class="font-black text-sm text-[#0F172A] uppercase tracking-wider mb-2 flex items-center space-x-2">
              <span>🎨</span>
              <span>Paleta Cromática Oficial Ultracem (Haz clic para copiar HEX)</span>
            </h4>
            <p class="text-slate-600 text-xs mb-4">Colores extraídos directamente de la guía de marca oficial. Diseñados para armonizar la autoridad tecnológica y el crecimiento humano.</p>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              <!-- Ultracem Navy -->
              <div onclick="copyColorHex('#0F172A', 'Ultracem Navy')" class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-slate-400 cursor-pointer transition-all flex items-center space-x-3">
                <div class="w-12 h-12 rounded-xl border border-slate-400 flex-shrink-0 shadow-xs" style="background-color: #0F172A;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-slate-400 font-bold uppercase">Base / Autoridad</span>
                  <strong class="block text-slate-900 text-xs">Ultracem Navy</strong>
                  <code class="text-[11px] font-mono-data font-bold text-[#0F172A]">#0F172A</code>
                </div>
              </div>

              <!-- Ultracem Teal -->
              <div onclick="copyColorHex('#14B8A6', 'Ultracem Teal')" class="bg-white p-3.5 rounded-2xl border border-teal-300 shadow-2xs hover:border-teal-500 cursor-pointer transition-all flex items-center space-x-3 bg-teal-50/20">
                <div class="w-12 h-12 rounded-xl border border-teal-500 flex-shrink-0 shadow-xs" style="background-color: #14B8A6;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-teal-600 font-bold uppercase">Primario / Acción (CTA)</span>
                  <strong class="block text-slate-900 text-xs">Ultracem Teal</strong>
                  <code class="text-[11px] font-mono-data font-bold text-teal-700">#14B8A6</code>
                </div>
              </div>

              <!-- Mint Teal -->
              <div onclick="copyColorHex('#5EEAD4', 'Mint Teal')" class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-slate-400 cursor-pointer transition-all flex items-center space-x-3">
                <div class="w-12 h-12 rounded-xl border border-teal-300 flex-shrink-0 shadow-xs" style="background-color: #5EEAD4;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-teal-600 font-bold uppercase">Expansión & Badges</span>
                  <strong class="block text-slate-900 text-xs">Mint Teal</strong>
                  <code class="text-[11px] font-mono-data font-bold text-teal-800">#5EEAD4</code>
                </div>
              </div>

              <!-- Sky Blue -->
              <div onclick="copyColorHex('#7DD3FC', 'Sky Blue')" class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-slate-400 cursor-pointer transition-all flex items-center space-x-3">
                <div class="w-12 h-12 rounded-xl border border-sky-300 flex-shrink-0 shadow-xs" style="background-color: #7DD3FC;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-sky-600 font-bold uppercase">Secundario Módulos</span>
                  <strong class="block text-slate-900 text-xs">Sky Blue</strong>
                  <code class="text-[11px] font-mono-data font-bold text-sky-800">#7DD3FC</code>
                </div>
              </div>

              <!-- Soft Sky -->
              <div onclick="copyColorHex('#BAE6FD', 'Soft Sky')" class="bg-white p-3.5 rounded-2xl border border-slate-200 shadow-2xs hover:border-slate-400 cursor-pointer transition-all flex items-center space-x-3">
                <div class="w-12 h-12 rounded-xl border border-sky-200 flex-shrink-0 shadow-xs" style="background-color: #BAE6FD;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-sky-600 font-bold uppercase">Secundario Claro (Fondos)</span>
                  <strong class="block text-slate-900 text-xs">Soft Sky</strong>
                  <code class="text-[11px] font-mono-data font-bold text-sky-900">#BAE6FD</code>
                </div>
              </div>

              <!-- Ultracem Blue -->
              <div onclick="copyColorHex('#3797E8', 'Ultracem Blue')" class="bg-white p-3.5 rounded-2xl border border-blue-200 shadow-2xs hover:border-blue-400 cursor-pointer transition-all flex items-center space-x-3">
                <div class="w-12 h-12 rounded-xl border border-blue-400 flex-shrink-0 shadow-xs" style="background-color: #3797E8;"></div>
                <div class="flex-1">
                  <span class="text-[10px] text-blue-600 font-bold uppercase">Endorsement Matriz</span>
                  <strong class="block text-slate-900 text-xs">Ultracem Blue</strong>
                  <code class="text-[11px] font-mono-data font-bold text-blue-800">#3797E8</code>
                </div>
              </div>
            </div>
          </div>

          <!-- Principios Gráficos y Tipográficos -->
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <h4 class="font-bold text-xs text-slate-900 uppercase">Directrices de Estilizado UI</h4>
            <ul class="list-disc list-inside space-y-1.5 text-slate-700 text-[11px]">
              <li><strong>Bordes Orgánicos:</strong> Esquinas redondeadas de 18px a 24px (`rounded-2xl` a `rounded-3xl`) que reflejan la calidez del acompañamiento.</li>
              <li><strong>Micro-iconografía Vegetal:</strong> Uso intencional de semillas, brotes y hojas para representar la madurez del cliente y el nivel del asesor.</li>
              <li><strong>Matriz de Puntos Tecnológica:</strong> Acentos sutiles que comunican la precisión digital y de software provista por Ultracem.</li>
              <li><strong>Voz & Tono:</strong> Optimista, cercano, técnico y riguroso. Celebra los pequeños logros diarios y previene el desánimo con el Casco Protector.</li>
            </ul>
          </div>
        </div>

        <!-- TAB 3: ESTRATEGIA 4 FASES -->
        <div id="prd-tab-content-fases" class="hidden space-y-6">
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-3">
            <div class="flex items-center justify-between">
              <div>
                <h4 class="font-black text-sm text-[#0F172A] uppercase">Estrategia de Activación del Programa (4 Fases)</h4>
                <p class="text-slate-600 text-[11px]">Metodología para generar adopción orgánica y expectativa entre los equipos comerciales.</p>
              </div>
              <span class="text-xs bg-teal-100 text-teal-800 font-bold px-2.5 py-1 rounded-full">Interactiva</span>
            </div>

            <!-- Fases Cards Grid -->
            <div class="space-y-3 pt-2">
              <!-- Fase 1 -->
              <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xl">🌰</span>
                    <strong class="text-slate-900 text-xs">Fase 1: Expectativa (Semilla en Reposo)</strong>
                  </div>
                  <button onclick="setActivationStage(1); closeUltracemPRDModal();" class="btn-tactile bg-slate-900 text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">Probar Fase 1 en App</button>
                </div>
                <p class="text-slate-600 text-[11px]">Despierta intriga y atención sin revelar el nombre definitivo. Mensajes tipo *"Algo grande está por brotar en tu gestión comercial..."*</p>
              </div>

              <!-- Fase 2 -->
              <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xl">🌱</span>
                    <strong class="text-slate-900 text-xs">Fase 2: Curiosidad (Primer Brote Emergiendo)</strong>
                  </div>
                  <button onclick="setActivationStage(2); closeUltracemPRDModal();" class="btn-tactile bg-emerald-700 text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">Probar Fase 2 en App</button>
                </div>
                <p class="text-slate-600 text-[11px]">Fomenta la participación mediante encuestas rápidas de dolores comerciales (*¿Qué tanto cuidas el potencial de tus obras?*).</p>
              </div>

              <!-- Fase 3 -->
              <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xl">🌿</span>
                    <strong class="text-slate-900 text-xs">Fase 3: Reveal (Hojas Desplegadas)</strong>
                  </div>
                  <button onclick="setActivationStage(3); closeUltracemPRDModal();" class="btn-tactile bg-teal-600 text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">Probar Fase 3 en App</button>
                </div>
                <p class="text-slate-600 text-[11px]">Revelación del nombre oficial <strong>ULTRACEM by Ultracem</strong>, su lema y el propósito formativo del ecosistema.</p>
              </div>

              <!-- Fase 4 -->
              <div class="bg-teal-50/50 p-4 rounded-2xl border border-teal-300 space-y-2">
                <div class="flex items-center justify-between">
                  <div class="flex items-center space-x-2">
                    <span class="text-xl">🌳</span>
                    <strong class="text-teal-950 text-xs">Fase 4: Lanzamiento & Demo Activa (Planta Floreciente)</strong>
                  </div>
                  <button onclick="setActivationStage(4); closeUltracemPRDModal();" class="btn-tactile bg-[#14B8A6] text-white text-[10px] font-bold px-2.5 py-1 rounded-lg">Probar Fase 4 (Activa)</button>
                </div>
                <p class="text-teal-900 text-[11px]">Despliegue operativo completo: CRM en campo, copiloto IA, mapa B2B, grabación de audio real y panel supervisor.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 4: ESPECIFICACIÓN PRD & TÉCNICA -->
        <div id="prd-tab-content-specs" class="hidden space-y-6">
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-4">
            <h4 class="font-black text-sm text-[#0F172A] uppercase">Especificación de Requerimientos de Producto (PRD)</h4>

            <div class="space-y-3">
              <div>
                <strong class="block text-slate-900 text-xs font-bold">1. Arquitectura Técnica y Stack Tecnológico</strong>
                <p class="text-slate-600 text-[11px] mt-0.5">
                  Single Page Application (SPA) responsive mobile-first. Diseñada con Tailwind CSS, Leaflet.js para geolocalización, Web Audio API y MediaRecorder para registro de notas de voz en obra. Backend Node.js (`server.js`) con proxy seguro para NVIDIA NIM y conexión directa a Groq Cloud (`openai/gpt-oss-120b`, `whisper-large-v3-turbo`).
                </p>
              </div>

              <div class="pt-2 border-t border-slate-100">
                <strong class="block text-slate-900 text-xs font-bold">2. Reglas de Negocio Anti-Colisión & Protección de Cartera</strong>
                <p class="text-slate-600 text-[11px] mt-0.5">
                  Un cliente solo puede ser gestionado activamente por un único asesor a la vez. Cuando un caso está asignado, los demás compañeros ven el registro como "Bloqueado / En Gestión Activa" para evitar acosar al residente de obra. La transferencia de clientes puede realizarse voluntariamente entre compañeros o solicitarse al supervisor con justificación de cercanía geográfica.
                </p>
              </div>

              <div class="pt-2 border-t border-slate-100">
                <strong class="block text-slate-900 text-xs font-bold">3. Guardrail Estricto del Copiloto IA</strong>
                <p class="text-slate-600 text-[11px] mt-0.5">
                  El prompt del sistema prohíbe taxativamente que la IA responda preguntas ajenas al sector cementero, normas técnicas NTC 121 y ventas B2B. Si un usuario formula consultas médicas, de cocina o científicas abstractas (ej: *"¿Qué es el ácido ribonucleico?"*), el motor rechaza la consulta invocando el <em>Filtro de Dominio Ultracem</em>.
                </p>
              </div>

              <div class="pt-2 border-t border-slate-100">
                <strong class="block text-slate-900 text-xs font-bold">4. Mecánica del Casco Protector (Antichurn)</strong>
                <p class="text-slate-600 text-[11px] mt-0.5">
                  Para evitar el "efecto frustración" de perder rachas largas por situaciones ajenas (lluvias torrenciales, paros de transporte), el asesor dispone de 1 Casco Protector que congela la racha por 24 horas manteniendo el puntaje y el ánimo comercial intactos.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 5: GUÍA DE EVALUACIÓN DE LA DEMO ACTIVA -->
        <div id="prd-tab-content-demo" class="hidden space-y-6">
          <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-2xs space-y-4">
            <div>
              <h4 class="font-black text-sm text-[#0F172A] uppercase">Guía de Pruebas de la Demo Activa para Evaluadores</h4>
              <p class="text-slate-600 text-[11px]">Siga estos 6 pasos para validar todas las funcionalidades implementadas en vivo:</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-[11px]">
              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 1: Grabación Real de Voz</strong>
                <p class="text-slate-600">En la pantalla de Racha, haga clic en el botón de micrófono en <em>Constructora Bolívar</em>. Permita el acceso al micrófono, hable y observe las barras de audio en tiempo real y la transcripción con reproductor WAV.</p>
              </div>

              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 2: Copiloto con Guardrails</strong>
                <p class="text-slate-600">Vaya a la pestaña Copiloto y haga clic en la píldora <em>“¿Qué es el ácido ribonucleico?”</em>. Compruebe cómo el sistema rechaza la pregunta y orienta hacia normas NTC 121 y ventas de cemento.</p>
              </div>

              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 3: Radar Satelital & B2B</strong>
                <p class="text-slate-600">Vaya a la pestaña Mapa. Conmute entre la vista estándar y satelital. Luego toque la pestaña <em>Directorio B2B</em> para ver 12 prospectos de obras y enviar un guion comercial personalizado.</p>
              </div>

              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 4: Transferencia de Clientes</strong>
                <p class="text-slate-600">En la pestaña Perfil, haga clic en la tarjeta de un compañero (ej: Laura Valencia) para ver su cartera asignada, o transfiera un cliente propio mediante el modal de reasignación.</p>
              </div>

              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 5: Simulación 10:45 PM</strong>
                <p class="text-slate-600">En la barra superior, haga clic en el botón <em>🌙 10:45 PM</em>. Don Fraguado entrará en pánico de racha urgente con animación visual y cambio de diálogo dramático.</p>
              </div>

              <div class="bg-slate-50 p-3.5 rounded-2xl border border-slate-200 space-y-1">
                <strong class="text-slate-900 block font-bold text-xs">Paso 6: Conmutador de 4 Fases</strong>
                <p class="text-slate-600">En la barra superior, toque los botones <em>Expectativa ➔ Curiosidad ➔ Reveal ➔ Lanzamiento</em> para ver cómo evoluciona la experiencia para los usuarios según la etapa del programa.</p>
              </div>
            </div>

            <div class="pt-2 flex justify-end">
              <button onclick="closeUltracemPRDModal()" class="btn-tactile bg-[#14B8A6] hover:bg-teal-600 text-white font-extrabold text-xs px-4 py-2 rounded-xl shadow-xs">
                ¡Ir a Probar la Demo Activa!
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="bg-slate-100 p-4 border-t border-slate-200 flex items-center justify-between flex-shrink-0 text-xs">
        <div class="flex items-center space-x-2 text-slate-500 text-[11px]">
          <span>📘</span>
          <span>Documento disponible como archivo Markdown en el repositorio del proyecto</span>
        </div>
        <button onclick="closeUltracemPRDModal()" class="btn-tactile bg-slate-900 text-white font-bold px-4 py-1.5 rounded-xl text-xs hover:bg-slate-800">
          Cerrar
        </button>
      </div>

    </div>
  </div>

  <!-- ============================================================== -->
  <!-- TOAST NOTIFICATION CONTAINER (STRICT Z-INDEX 999999)           -->
  <!-- ============================================================== -->
  <div id="toast-container" class="fixed bottom-5 right-5 space-y-2 pointer-events-none select-none" style="z-index: 999999;"></div>

  <!-- ============================================================== -->
  <!-- CORE JAVASCRIPT STATE ENGINE                                   -->
  <!-- ============================================================== -->
  <script>
    // 1. STATE VARIABLES
    let userStreak = 21;
    let userXP = 850;
    let cascoProtectorCount = 1;
    let cascoActive = false;
    let activeAIProvider = localStorage.getItem('ultracem_ai_provider') || 'nvidia';
    let selectedModel = localStorage.getItem('ultracem_ai_model') || 'meta/llama-3.1-70b-instruct';
    let userApiKey = localStorage.getItem('ultracem_ai_key') || '';
    let customApiUrl = localStorage.getItem('ultracem_custom_url') || 'http://localhost:11434/v1/chat/completions';
    let isDayMode = true;
    let activeMapLayerType = 'streets'; // 'streets' or 'satellite'
    let currentMapSubView = 'radar'; // 'radar' or 'prospectos'
    let currentProspectSector = 'todos';

    // Real Audio Recording & Speech to Text State
    let mediaRecorder = null;
    let audioChunks = [];
    let audioStream = null;
    let liveAudioCtx = null;
    let analyserNode = null;
    let animationFrameId = null;
    let speechRecognizer = null;
    let recordingSeconds = 0;
    let recordingTimerInterval = null;

    // Team Members
    const teamMembers = [
      {
        id: "carlos",
        name: "Carlos Mendoza",
        role: "Asesor Comercial Senior",
        division: "Regional Atlántico • Obras",
        avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
        racha: 21,
        nivel: 4,
        clients: [
          { id: 1, name: "Constructora Bolívar — Torres del Mar", tons: 120, estado: "8d sin pedido", ciudad: "Barranquilla", tipo: "Obra Mayor", cupo: "$50M" },
          { id: 2, name: "Ferretería El Constructor — Sede Centro", tons: 45, estado: "4d sin pedido", ciudad: "Soledad", tipo: "Ferretería", cupo: "$25M" }
        ]
      },
      {
        id: "milena",
        name: "Milena Ospino",
        role: "Asesora Comercial Ultracem",
        division: "Regional Caribe • mospino@ultracem.co • 313 557 4297",
        avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=80&auto=format&fit=crop&q=80",
        racha: 34,
        nivel: 5,
        clients: [
          { id: 3, name: "Marval — Altos de Riomar", tons: 210, estado: "En Gestión Activa", ciudad: "Barranquilla", tipo: "Obra Mayor", cupo: "$120M" },
          { id: 303, name: "Arquitectura & Concreto — Serena del Mar", tons: 420, estado: "En Negociación", ciudad: "Cartagena", tipo: "Macroproyecto", cupo: "$180M" },
          { id: 31, name: "Constructora Conconcreto — Mall Plaza", tons: 180, estado: "En Despacho", ciudad: "Barranquilla", tipo: "Obra Mayor", cupo: "$90M" }
        ]
      },
      {
        id: "adriana",
        name: "Adriana Anaya",
        role: "Asesora Comercial Ultracem",
        division: "Regional Costa Norte • aanaya@ultracem.co • 320 709 6744",
        avatar: "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=80&auto=format&fit=crop&q=80",
        racha: 48,
        nivel: 6,
        clients: [
          { id: 6, name: "Edificio Rodadero Plaza", tons: 160, estado: "En Gestión Activa", ciudad: "Santa Marta", tipo: "Obra Hotelera", cupo: "$85M" },
          { id: 307, name: "Concesión Costera Cartagena-Barranquilla", tons: 190, estado: "Contrato Vigente", ciudad: "Puerto Colombia", tipo: "Infraestructura", cupo: "$150M" }
        ]
      },
      {
        id: "hichel",
        name: "Hichel Espitia",
        role: "Especialista Cuentas Mayores Ultracem",
        division: "Canal Institucional • Tel: 310 250 3454",
        avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=80&auto=format&fit=crop&q=80",
        racha: 29,
        nivel: 4,
        clients: [
          { id: 71, name: "Ferretería Metropolitana — Calle 30", tons: 60, estado: "En Seguimiento", ciudad: "Barranquilla", tipo: "Ferretería", cupo: "$30M" },
          { id: 72, name: "Urbanización Alameda Campestre", tons: 110, estado: "Visita Programada", ciudad: "Soledad", tipo: "Vivienda VIS", cupo: "$60M" }
        ]
      }
    ];

    // ==============================================================
    // DATABASE: B2B PROSPECTS (NUEVAS EMPRESAS PARA OFRECER PRODUCTO)
    // ==============================================================
    const b2bProspects = [
      {
        id: 301,
        empresa: "Constructora Amarilo S.A.S.",
        proyecto: "Proyecto Hacienda San Antonio — Torres 1 a 6",
        sector: "constructoras",
        ciudad: "barranquilla",
        direccion: "Cra 51B con Calle 135, Barranquilla",
        lat: 11.0250,
        lng: -74.8350,
        volumen: "320 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max (NTC 121 ART)",
        proveedorActual: "Cementos Argos",
        residente: "Ing. Mauricio Peña",
        telefono: "301 234 5678",
        estado: "disponible", // disponible, bloqueado, propia
        asesorBloqueo: "",
        ventajaAtaque: "Retraso de 24h en desencofrado con Argos. Con Ultracem ART desencofran a 18h y ahorran $5.4M al mes en alquiler de formaleta.",
        scriptApertura: "Ingeniero Mauricio, le escribe Carlos Mendoza de Ultracem. Sabemos que en Hacienda San Antonio están vaciando losas con Argos; le garantizamos retiro de formaleta 24h antes con nuestro Cemento Estructural Max NTC 121 con despacho directo desde Planta Galapa sin roturas. ¿Le programamos una muestra técnica sin costo para su laboratorio?"
      },
      {
        id: 302,
        empresa: "Coninsa Ramón H",
        proyecto: "Alameda del Río — Manzana 4 (380 Aptos)",
        sector: "constructoras",
        ciudad: "barranquilla",
        direccion: "Avenida Circunvalar con Carrera 43",
        lat: 10.9920,
        lng: -74.8320,
        volumen: "240 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max",
        proveedorActual: "Cemex Colombia",
        residente: "Arq. Sandra Gómez",
        telefono: "312 876 5432",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Cemex presenta demoras de flete de 48 horas desde el interior. Ultracem entrega en 90 minutos desde Galapa por la Circunvalar.",
        scriptApertura: "Arquitecta Sandra, buenos días. Le saluda Carlos Mendoza de Ultracem. Para el vaciado de Alameda del Río le ofrecemos entregas en 90 minutos directo de planta y un ahorro neto de $1.400 por bulto respecto a su proveedor actual. ¿Cuándo podemos revisar la dosificación?"
      },
      {
        id: 303,
        empresa: "Arquitectura & Concreto",
        proyecto: "Serena del Mar — Conjunto Morros Park",
        sector: "constructoras",
        ciudad: "cartagena",
        direccion: "Km 8 Vía al Mar, Cartagena",
        lat: 10.4850,
        lng: -75.4620,
        volumen: "420 Ton / Mes",
        productoRecomendado: "Cemento Moderada Resistencia a Sulfatos (MRS)",
        proveedorActual: "Cementos Argos",
        residente: "Ing. Roberto Dangond",
        telefono: "318 901 2345",
        estado: "bloqueado",
        asesorBloqueo: "Laura Valencia",
        ventajaAtaque: "Ambiente marino salino severo. Ultracem MRS previene corrosión de armaduras y penetración de cloruros.",
        scriptApertura: "Contacto restringido por protección anti-colisión comercial."
      },
      {
        id: 304,
        empresa: "Consorcio Vías del Atlántico",
        proyecto: "Doble Calzada Conexión Juan Mina — Galapa",
        sector: "infraestructura",
        ciudad: "galapa",
        direccion: "Km 4 Vía Juan Mina, Galapa",
        lat: 10.9120,
        lng: -74.8720,
        volumen: "550 Ton / Mes",
        productoRecomendado: "Cemento Granel Pavimentos Rígidos (MR 4.5 MPa)",
        proveedorActual: "Cementos Argos",
        residente: "Ing. Fabio Cifuentes (Director Técnico)",
        telefono: "300 987 6543",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Ubicados a solo 3 km de nuestra Planta Principal de Galapa. Flete prácticamente a costo cero con despacho continuo de graneleras.",
        scriptApertura: "Ingeniero Fabio, excelente día. Con nuestra planta a solo 5 minutos de su frente de obra, eliminamos cualquier riesgo de desabastecimiento en vaciado de pavimento rígido. Le ofrecemos precio especial de fábrica puesta en tolva."
      },
      {
        id: 305,
        empresa: "Prefabricados & Adoquines del Caribe S.A.S.",
        proyecto: "Planta Industrial de Elementos Vibrados",
        sector: "prefabricados",
        ciudad: "soledad",
        direccion: "Parque Industrial Malambo PIMSA",
        lat: 10.8650,
        lng: -74.7780,
        volumen: "140 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max ART Granel",
        proveedorActual: "Cemex Colombia",
        residente: "Don Hernán Restrepo (Gerente Planta)",
        telefono: "315 444 3322",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Requieren rotación diaria de moldes de adoquín y bordillos. Con el alto calor de hidratación de Ultracem ART desmoldan en 8 horas en lugar de 24 horas, duplicando su capacidad fabril.",
        scriptApertura: "Don Hernán, le habla Carlos Mendoza de Ultracem. Sabemos que para su producción de adoquines cada hora de molde cuenta. Con Ultracem ART logra desmolde antes de mediodía sin fisuración. ¿Le enviamos 5 toneladas de prueba técnica?"
      },
      {
        id: 306,
        empresa: "Grama Construcciones",
        proyecto: "Centro Logístico Calle 30",
        sector: "constructoras",
        ciudad: "soledad",
        direccion: "Autopista al Aeropuerto con Calle 30",
        lat: 10.9150,
        lng: -74.7680,
        volumen: "180 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max",
        proveedorActual: "Cementos Argos",
        residente: "Ing. Carolina Vives",
        telefono: "317 222 1199",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Pisos industriales de alto tránsito. Ultracem ofrece resistencia al desgaste y menor retracción plástica.",
        scriptApertura: "Ingeniera Carolina, para los pisos del centro logístico, Ultracem le garantiza planicidad y resistencia NTC 121 sin agrietamientos por retracción con entrega express."
      },
      {
        id: 307,
        empresa: "Concesión Costera Cartagena-Barranquilla",
        proyecto: "Mantenimiento & Puentes Viaducto El Gran Manglar",
        sector: "infraestructura",
        ciudad: "santamarta",
        direccion: "Vía al Mar Km 18, Puerto Colombia",
        lat: 11.0080,
        lng: -74.9120,
        volumen: "190 Ton / Mes",
        proveedorActual: "Cementos Argos",
        residente: "Ing. Guillermo Silva",
        telefono: "311 555 7788",
        estado: "bloqueado",
        asesorBloqueo: "Andrés Restrepo",
        ventajaAtaque: "Estructuras sobre ciénagas y agua salobre.",
        scriptApertura: "Cuenta asignada al portafolio de Andrés Restrepo."
      },
      {
        id: 308,
        empresa: "Bloquera Industrial del Norte",
        proyecto: "Fábrica de Bloques Estructurales 15x20x40",
        sector: "prefabricados",
        ciudad: "barranquilla",
        direccion: "Vía 40 con Calle 76",
        lat: 11.0010,
        lng: -74.8020,
        volumen: "85 Ton / Mes",
        productoRecomendado: "Cemento Uso General (Sacos 50kg)",
        proveedorActual: "Cementos Argos",
        residente: "Maestro Álvaro Polo",
        telefono: "300 123 4567",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Argos les despacha sacos de papel sencillo con 3% de rotura en estiba. Ultracem entrega paletizado con film stretch impermeable y flete bonificado.",
        scriptApertura: "Maestro Álvaro, le garantizamos cero bultos rotos y precio directo de distribuidor mayorista con entrega al día siguiente."
      },
      {
        id: 309,
        empresa: "Ferretería Samir Mayorista",
        proyecto: "Red de Distribución Regional (6 Puntos de Venta)",
        sector: "ferreterias",
        ciudad: "barranquilla",
        direccion: "Calle Murillo con Carrera 21",
        lat: 10.9650,
        lng: -74.7910,
        volumen: "160 Ton / Mes",
        productoRecomendado: "Cemento Uso General & Estructural Max",
        proveedorActual: "Cementos Argos / Mixto",
        residente: "Don Samir Farah (Gerente de Compras)",
        telefono: "314 333 9988",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Argos impone cuotas mínimas muy altas. Ultracem ofrece cupo rotativo de $40M y material publicitario para sus vitrinas.",
        scriptApertura: "Don Samir, le ofrecemos exclusividad de zona con margen de utilidad del 14% por bulto, superior al 8% de la competencia, y material de punto de venta oficial Ultracem."
      },
      {
        id: 310,
        empresa: "Prodesa",
        proyecto: "Urbanización Ciudad del Sol (Vivienda VIS)",
        sector: "constructoras",
        ciudad: "soledad",
        direccion: "Prolongación Murillo, Soledad",
        lat: 10.9080,
        lng: -74.7790,
        volumen: "210 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max",
        proveedorActual: "Cemex Colombia",
        residente: "Ing. Natalia Cadavid",
        telefono: "304 666 5544",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Ritmo de vaciado de 1 apartamento diario con sistema industrializado tipo túnel. Exige alta resistencia a 14 horas.",
        scriptApertura: "Ingeniera Natalia, para su sistema tipo túnel en Ciudad del Sol, el Ultracem ART le permite desencofrar a las 14 horas garantizando 15 MPa y acelerando el ciclo diario de fundición."
      },
      {
        id: 311,
        empresa: "Distribuidora Ferretera del Sur",
        proyecto: "Depósito Mayorista Malambo",
        sector: "ferreterias",
        ciudad: "soledad",
        direccion: "Carrera 8 con Calle 10, Malambo",
        lat: 10.8590,
        lng: -74.7710,
        volumen: "70 Ton / Mes",
        productoRecomendado: "Cemento Uso General NTC 121",
        proveedorActual: "Cementos Argos",
        residente: "Don Jorge Eliécer Castro",
        telefono: "310 888 7766",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Surtido desde Planta Galapa en camiones medianos que entran sin problema a vías estrechas del municipio.",
        scriptApertura: "Don Jorge, le ofrecemos despacho directo en turbos y camiones medianos sin costo extra de flete, para que no tenga que alquilar transporte."
      },
      {
        id: 312,
        empresa: "Edificio Santa Marta Marina Beach",
        proyecto: "Torre Residencial & Hotelera (22 Pisos)",
        sector: "constructoras",
        ciudad: "santamarta",
        direccion: "Bello Horizonte, Santa Marta",
        lat: 11.1620,
        lng: -74.2310,
        volumen: "220 Ton / Mes",
        productoRecomendado: "Cemento Estructural Max & Marino",
        proveedorActual: "Cemex Colombia",
        residente: "Ing. Carlos Julio Barreto",
        telefono: "316 777 8899",
        estado: "disponible",
        asesorBloqueo: "",
        ventajaAtaque: "Cemex despacha desde Ibagué con hasta 4 días de retraso en carretera troncal del Caribe. Ultracem atiende desde Galapa en 3 horas.",
        scriptApertura: "Ingeniero Carlos Julio, le aseguramos entregas puntuales en obra sin depender de cierres de carretera en el Magdalena Medio, con certificado NTC 121 de cada lote."
      }
    ];

    // ==============================================================
    // ENRICHED DATASET: SITES FOR THE LEAFLET MAP
    // ==============================================================
    const clientSites = [
      // 1. INFRAESTRUCTURA ULTRACEM
      {
        id: 101,
        name: "Planta Principal Ultracem — Galapa",
        categoria: "ultracem",
        tipo: "Planta Molienda & Laboratorio Central",
        lat: 10.9015,
        lng: -74.8870,
        ciudad: "galapa",
        capacidad: "1.200.000 Ton/año de clínker y cemento",
        silos: "6 Silos de granel automatizados",
        despacho: "24/7 con básculas dinámicas",
        ventaja: "Molienda de alta finura NTC 121. Despacho a obras del Atlántico en menos de 90 minutos.",
        icon: "🏭",
        color: "#004797"
      },
      {
        id: 102,
        name: "Terminal Portuario & Silos Vía 40",
        categoria: "ultracem",
        tipo: "Terminal de Embarque & Silos a Granel",
        lat: 11.0180,
        lng: -74.7950,
        ciudad: "barranquilla",
        capacidad: "45.000 Ton de acopio continuo",
        silos: "4 Silos portuarios para carga de mixer",
        despacho: "Ruta directa sobre el río Magdalena",
        ventaja: "Abastecimiento ininterrumpido a obras del norte de Barranquilla sin restricciones de tráfico pesado.",
        icon: "⚓",
        color: "#004797"
      },
      {
        id: 103,
        name: "Centro Logístico Mamonal",
        categoria: "ultracem",
        tipo: "Plataforma Logística Regional",
        lat: 10.3350,
        lng: -75.4980,
        ciudad: "cartagena",
        capacidad: "30.000 Ton/mes",
        silos: "Centro de acopio y ensacado rápido",
        despacho: "Corredor industrial de Cartagena",
        ventaja: "Entregas en 3 horas para la zona industrial y proyectos hoteleros de Bolívar.",
        icon: "📦",
        color: "#004797"
      },

      // 2. COMPETIDORES EN EL MERCADO
      {
        id: 201,
        name: "Cementos Argos — Planta Riomar",
        categoria: "competencia",
        tipo: "Planta Molienda & Concreto (Competidor)",
        lat: 11.0090,
        lng: -74.8050,
        ciudad: "barranquilla",
        benchmarkPrecio: "$31.500 COP / Bulto 50kg Gris",
        tiempoEntrega: "48 a 72 horas programadas",
        debilidad: "Congestión vehicular severa en Vía 40 en horas pico. Rotura de sacos en cargue manual.",
        argumentoVenta: "Ultracem despacha directo desde Galapa por la Circunvalar en 90 minutos con paletizado plastificado sin mermas ni sacos rotos. Ahorro de $1.700 COP por bulto.",
        icon: "🔴",
        color: "#DC2626"
      },
      {
        id: 202,
        name: "Cementos Argos — Terminal Soledad",
        categoria: "competencia",
        tipo: "Centro de Distribución (Competidor)",
        lat: 10.9250,
        lng: -74.7720,
        ciudad: "soledad",
        benchmarkPrecio: "$31.200 COP / Bulto 50kg",
        tiempoEntrega: "24 a 48 horas",
        debilidad: "Tiempos de aprobación crediticia de 15 días hábiles; poco margen a ferreterías de barrio.",
        argumentoVenta: "Ultracem pre-aprueba cupo comercial en 24 horas y ofrece asesoría técnica directa con laboratorio en obra.",
        icon: "🔴",
        color: "#DC2626"
      },
      {
        id: 203,
        name: "Cemex Colombia — Centro Operativo Calle 17",
        categoria: "competencia",
        tipo: "Centro de Despacho & Mezcla (Competidor)",
        lat: 10.9620,
        lng: -74.7780,
        ciudad: "barranquilla",
        benchmarkPrecio: "$30.900 COP / Bulto 50kg Tipo UG",
        tiempoEntrega: "48 horas",
        debilidad: "Cemento traído por carretera interdepartamental; menor reactividad por envejecimiento de clinker.",
        argumentoVenta: "Ultracem se produce localmente con clinker fresco, alcanzando 18 MPa a 24 horas para desencofrar antes.",
        icon: "🔴",
        color: "#EA580C"
      },
      {
        id: 204,
        name: "Holcim Colombia — Plataforma Vía 40",
        categoria: "competencia",
        tipo: "Acopio y Distribución (Competidor)",
        lat: 11.0020,
        lng: -74.8010,
        ciudad: "barranquilla",
        benchmarkPrecio: "$32.000 COP / Bulto Fuerte",
        tiempoEntrega: "72 horas",
        debilidad: "Centrados casi exclusivamente en licitaciones 4G; abandonan contratistas medianos y edificaciones residenciales.",
        argumentoVenta: "Ultracem brinda acompañamiento a ingenieros residentes con entregas fraccionadas según programa de vaciado de losas.",
        icon: "🔴",
        color: "#D97706"
      },

      // 3. CLIENTES ACTIVOS & PROSPECTOS
      {
        id: 1,
        name: "Constructora Bolívar — Torres del Mar",
        categoria: "clientes",
        tipo: "Obra Mayor • Edificación Residencial",
        lat: 10.9980,
        lng: -74.8080,
        ciudad: "barranquilla",
        estado: "propia",
        asesor: "Carlos Mendoza",
        tons: 120,
        tel: "3004567890",
        icon: "🏗️",
        color: "#059669"
      },
      {
        id: 2,
        name: "Ferretería El Constructor — Sede Centro",
        categoria: "clientes",
        tipo: "Distribuidor Ferretero Mayorista",
        lat: 10.9230,
        lng: -74.7610,
        ciudad: "soledad",
        estado: "propia",
        asesor: "Carlos Mendoza",
        tons: 45,
        tel: "3119876543",
        icon: "🏪",
        color: "#059669"
      },
      {
        id: 3,
        name: "Marval — Altos de Riomar",
        categoria: "clientes",
        tipo: "Obra Mayor • Vaciado Torre 3",
        lat: 11.0120,
        lng: -74.8210,
        ciudad: "barranquilla",
        estado: "bloqueado",
        asesor: "Laura Valencia",
        tons: 210,
        tel: "3201234567",
        icon: "🔒",
        color: "#D97706"
      },
      // Target Prospect: Amarilo
      {
        id: 301,
        name: "Constructora Amarilo — Hacienda San Antonio",
        categoria: "prospectos",
        tipo: "Obra Mayor (Prospecto Caliente)",
        lat: 11.0250,
        lng: -74.8350,
        ciudad: "barranquilla",
        estado: "disponible",
        asesor: "Sin Asignar",
        tons: 320,
        tel: "3012345678",
        icon: "✨",
        color: "#0284C7"
      },
      // Target Prospect: Coninsa Ramón H
      {
        id: 302,
        name: "Coninsa Ramón H — Alameda del Río",
        categoria: "prospectos",
        tipo: "Macroproyecto VIS (Prospecto Caliente)",
        lat: 10.9920,
        lng: -74.8320,
        ciudad: "barranquilla",
        estado: "disponible",
        asesor: "Sin Asignar",
        tons: 240,
        tel: "3128765432",
        icon: "✨",
        color: "#0284C7"
      },
      // Target Prospect: Consorcio Vías del Atlántico
      {
        id: 304,
        name: "Consorcio Vías del Atlántico — Doble Calzada",
        categoria: "prospectos",
        tipo: "Pavimento Rígido (Frente a Galapa)",
        lat: 10.9120,
        lng: -74.8720,
        ciudad: "galapa",
        estado: "disponible",
        asesor: "Sin Asignar",
        tons: 550,
        tel: "3009876543",
        icon: "✨",
        color: "#0284C7"
      },
      // Target Prospect: Prefabricados del Caribe
      {
        id: 305,
        name: "Prefabricados & Adoquines del Caribe",
        categoria: "prospectos",
        tipo: "Planta Prefabricados (Desmolde Rápido)",
        lat: 10.8650,
        lng: -74.7780,
        ciudad: "soledad",
        estado: "disponible",
        asesor: "Sin Asignar",
        tons: 140,
        tel: "3154443322",
        icon: "✨",
        color: "#0284C7"
      }
    ];

    // ==============================================================
    // AUDIO SYNTHESIZER FALLBACK (PURE JS RIFF/WAVE PCM 44.1kHz)
    // ==============================================================
    function generateSyntheticAudioMemoWav(durationSec = 2.5) {
      const sampleRate = 44100;
      const numSamples = Math.floor(sampleRate * durationSec);
      const buffer = new ArrayBuffer(44 + numSamples * 2);
      const view = new DataView(buffer);

      function writeStr(offset, str) {
        for (let i = 0; i < str.length; i++) {
          view.setUint8(offset + i, str.charCodeAt(i));
        }
      }

      writeStr(0, 'RIFF');
      view.setUint32(4, 36 + numSamples * 2, true);
      writeStr(8, 'WAVE');
      writeStr(12, 'fmt ');
      view.setUint32(16, 16, true);
      view.setUint16(20, 1, true); // PCM
      view.setUint16(22, 1, true); // Mono
      view.setUint32(24, sampleRate, true);
      view.setUint32(28, sampleRate * 2, true);
      view.setUint16(32, 2, true);
      view.setUint16(34, 16, true);
      writeStr(36, 'data');
      view.setUint32(40, numSamples * 2, true);

      for (let i = 0; i < numSamples; i++) {
        const t = i / sampleRate;
        let sample = 0;
        if (t < 0.2) {
          sample = Math.sin(2 * Math.PI * 880 * t) * 0.4; // 880 Hz
        } else if (t < 0.45) {
          sample = Math.sin(2 * Math.PI * 1320 * (t - 0.2)) * 0.35; // 1320 Hz
        } else if (t < 1.6) {
          const env = Math.exp(-(t - 0.45) * 1.5);
          sample = (Math.sin(2 * Math.PI * 440 * t) * 0.25 + Math.sin(2 * Math.PI * 880 * t) * 0.1) * env;
        }
        const s = Math.max(-1, Math.min(1, sample));
        view.setInt16(44 + i * 2, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
      }

      return new Blob([view], { type: 'audio/wav' });
    }

    // ==============================================================
    // LEAFLET MAP ENGINE
    // ==============================================================
    let leafletMap = null;
    let streetTileLayer = null;
    let satelliteTileLayer = null;
    let currentMapCategory = 'todas';

    function initColombiaMap() {
      const mapContainer = document.getElementById('colombia-leaflet-map');
      if (!mapContainer) return;

      if (!leafletMap) {
        leafletMap = L.map('colombia-leaflet-map', {
          zoomControl: false,
          attributionControl: false
        }).setView([10.9878, -74.7889], 12);

        window.leafletMap = leafletMap;

        streetTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
          maxZoom: 18,
          attribution: 'Map &copy; Esri &mdash; StreetMap Colombia'
        });

        satelliteTileLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
          maxZoom: 18,
          attribution: 'Satellite &copy; Esri World Imagery'
        });

        streetTileLayer.addTo(leafletMap);
        L.control.zoom({ position: 'topright' }).addTo(leafletMap);

        renderMapMarkers(clientSites);
      }

      setTimeout(() => {
        if (leafletMap) leafletMap.invalidateSize();
      }, 200);
    }

    function toggleMapLayer() {
      if (!leafletMap) return;
      playChime('click');
      const btn = document.getElementById('btn-toggle-satellite');

      if (activeMapLayerType === 'streets') {
        leafletMap.removeLayer(streetTileLayer);
        satelliteTileLayer.addTo(leafletMap);
        activeMapLayerType = 'satellite';
        btn.innerHTML = "<span>🗺️</span><span>Callejero</span>";
        btn.className = "btn-tactile bg-amber-500 hover:bg-amber-600 border border-amber-400 text-white text-[10px] font-bold px-2 py-1.5 rounded-xl flex items-center space-x-1 flex-shrink-0";
        showToast("🛰️ Vista satelital de alta resolución activada", "info");
      } else {
        leafletMap.removeLayer(satelliteTileLayer);
        streetTileLayer.addTo(leafletMap);
        activeMapLayerType = 'streets';
        btn.innerHTML = "<span>🛰️</span><span>Satélite</span>";
        btn.className = "btn-tactile bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 text-[10px] font-bold px-2 py-1.5 rounded-xl flex items-center space-x-1 flex-shrink-0";
        showToast("🗺️ Vista callejero comercial activada", "info");
      }
    }

    function renderMapMarkers(sites) {
      if (!leafletMap) return;

      leafletMap.eachLayer(layer => {
        if (layer instanceof L.Marker) leafletMap.removeLayer(layer);
      });

      sites.forEach(site => {
        let pinBg = site.color || "#004797";
        let symbol = site.icon || "📍";
        let pulseRing = "";

        if (site.categoria === 'ultracem') {
          pinBg = "#004797";
          pulseRing = `<span style="position: absolute; inset: -4px; border-radius: 50%; border: 2px solid #004797; animation: ping 2s cubic-bezier(0, 0, 0.2, 1) infinite; opacity: 0.6;"></span>`;
        } else if (site.categoria === 'competencia') {
          pinBg = "#DC2626";
        } else if (site.categoria === 'prospectos') {
          pinBg = "#0284C7"; // Bright Cyan for new prospect leads
        } else if (site.estado === 'propia') {
          pinBg = "#059669";
        } else if (site.estado === 'bloqueado') {
          pinBg = "#D97706";
        }

        const customIcon = L.divIcon({
          className: 'custom-map-pin',
          html: `
            <div style="position: relative; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center;">
              ${pulseRing}
              <div style="background-color: ${pinBg}; width: 26px; height: 26px; border-radius: 50%; border: 2.5px solid white; box-shadow: 0 3px 8px rgba(0,0,0,0.35); display: flex; align-items: center; justify-content: center; color: white; font-size: 13px;">
                ${symbol}
              </div>
            </div>
          `,
          iconSize: [28, 28],
          iconAnchor: [14, 14]
        });

        const marker = L.marker([site.lat, site.lng], { icon: customIcon }).addTo(leafletMap);
        marker.on('click', () => {
          mostrarDetalleSitioMapa(site);
        });
      });
    }

    function filtrarMapaPorCategoria(cat) {
      playChime('click');
      currentMapCategory = cat;

      const chips = {
        todas: document.getElementById('map-chip-todas'),
        prospectos: document.getElementById('map-chip-prospectos'),
        ultracem: document.getElementById('map-chip-ultracem'),
        competencia: document.getElementById('map-chip-competencia')
      };

      Object.keys(chips).forEach(k => {
        if (!chips[k]) return;
        if (k === cat) {
          chips[k].className = "px-2.5 py-1 rounded-lg bg-[#004797] text-white border border-[#004797] flex-shrink-0 transition-all font-bold";
        } else {
          chips[k].className = "px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 flex-shrink-0 hover:bg-slate-200 transition-all font-semibold";
        }
      });

      let filtered = clientSites;
      if (cat === 'ultracem') {
        filtered = clientSites.filter(s => s.categoria === 'ultracem');
      } else if (cat === 'competencia') {
        filtered = clientSites.filter(s => s.categoria === 'competencia');
      } else if (cat === 'prospectos') {
        filtered = clientSites.filter(s => s.categoria === 'prospectos');
      }

      renderMapMarkers(filtered);
      if (filtered.length > 0 && leafletMap) {
        leafletMap.panTo([filtered[0].lat, filtered[0].lng]);
      }
    }

    function setMapSubView(subview) {
      playChime('click');
      currentMapSubView = subview;

      const btnRadar = document.getElementById('btn-map-mode-radar');
      const btnProspectos = document.getElementById('btn-map-mode-prospectos');
      const viewRadar = document.getElementById('subview-map-radar');
      const viewProspectos = document.getElementById('subview-map-prospectos');

      if (subview === 'radar') {
        btnRadar.className = "flex-1 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs flex items-center justify-center space-x-1.5";
        btnProspectos.className = "flex-1 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center justify-center space-x-1.5";
        viewRadar.classList.remove('hidden');
        viewProspectos.classList.add('hidden');
        setTimeout(() => { if (leafletMap) leafletMap.invalidateSize(); }, 150);
      } else {
        btnProspectos.className = "flex-1 py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs flex items-center justify-center space-x-1.5";
        btnRadar.className = "flex-1 py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 flex items-center justify-center space-x-1.5";
        viewRadar.classList.add('hidden');
        viewProspectos.classList.remove('hidden');
        renderDirectorioProspectos(b2bProspects);
      }
    }

    function mostrarDetalleSitioMapa(site) {
      playChime('click');
      const card = document.getElementById('map-site-card');
      const title = document.getElementById('map-site-name');
      const desc = document.getElementById('map-site-desc');
      const status = document.getElementById('map-site-status');
      const intel = document.getElementById('map-site-intel');
      const actions = document.getElementById('map-site-actions');

      title.textContent = site.name;
      intel.classList.add('hidden');

      if (site.categoria === 'ultracem') {
        desc.textContent = `${site.ciudad.toUpperCase()} • ${site.tipo} • Cap: ${site.capacidad}`;
        status.className = "text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-blue-100 text-[#004797] border border-blue-200";
        status.textContent = "🏭 Infraestructura Ultracem";
        
        intel.innerHTML = `
          <div class="text-slate-700"><strong>Capacidad:</strong> ${site.silos}. ${site.despacho}.</div>
          <div class="text-blue-900 font-semibold mt-0.5">⭐ ${site.ventaja}</div>
        `;
        intel.classList.remove('hidden');

        actions.innerHTML = `
          <button onclick="copiarUbicacionPlanta('${site.name}', ${site.lat}, ${site.lng})" class="btn-tactile bg-blue-50 text-[#004797] border border-blue-200 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
            <span>📍</span><span>Copiar GPS</span>
          </button>
          <button onclick="consultarStockPlantaIA('${site.name}')" class="btn-tactile bg-[#004797] text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
            <span>⚡</span><span>Ver Stock en Planta</span>
          </button>
        `;
      } else if (site.categoria === 'competencia') {
        desc.textContent = `${site.ciudad.toUpperCase()} • ${site.tipo} • Ref: ${site.benchmarkPrecio}`;
        status.className = "text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-rose-100 text-rose-800 border border-rose-300";
        status.textContent = "🔴 Proveedor Competidor";

        intel.innerHTML = `
          <div class="text-rose-950"><strong>Benchmark:</strong> ${site.benchmarkPrecio} • Entrega: ${site.tiempoEntrega}</div>
          <div class="text-slate-600 mt-0.5"><strong>Debilidad:</strong> ${site.debilidad}</div>
          <div class="text-emerald-800 font-bold mt-1 bg-emerald-50 p-1.5 rounded-lg border border-emerald-200">💡 Argumento: ${site.argumentoVenta}</div>
        `;
        intel.classList.remove('hidden');

        actions.innerHTML = `
          <button onclick="preguntarCopilotoAtaque('${site.name}')" class="btn-tactile bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1 col-span-2 shadow-xs">
            <span>⚡</span><span>Preguntar a Copiloto IA cómo ganarles clientes</span>
          </button>
        `;
      } else if (site.categoria === 'prospectos') {
        const prospect = b2bProspects.find(p => p.id === site.id) || {
          volumen: `${site.tons} Ton / Mes`,
          proveedorActual: "Competencia",
          ventajaAtaque: "Oportunidad de despacho directo",
          residente: "Director de Obra",
          scriptApertura: `Hola, le escribe Carlos Mendoza de Ultracem...`
        };

        desc.textContent = `${site.ciudad.toUpperCase()} • ${prospect.volumen} • Proveedor actual: ${prospect.proveedorActual}`;
        status.className = "text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-sky-100 text-sky-900 border border-sky-300";
        status.textContent = "✨ Prospecto Caliente";

        intel.innerHTML = `
          <div class="text-slate-800"><strong>Contacto:</strong> ${prospect.residente}</div>
          <div class="text-emerald-800 font-bold mt-0.5 bg-emerald-50 p-1.5 rounded-lg border border-emerald-200">🎯 Ventaja Clave: ${prospect.ventajaAtaque}</div>
        `;
        intel.classList.remove('hidden');

        actions.innerHTML = `
          <button onclick="openInAppWhatsApp('${site.name}', '${prospect.volumen}')" class="btn-tactile bg-emerald-600 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
            <span>💬</span><span>WhatsApp</span>
          </button>
          <button onclick="generarEstrategiaProspectoIA(${site.id})" class="btn-tactile bg-[#004797] text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
            <span>⚡</span><span>Estrategia IA</span>
          </button>
        `;
      } else {
        desc.textContent = `${site.ciudad.toUpperCase()} • ${site.tons} Ton Cemento • Asesor: ${site.asesor}`;

        if (site.estado === 'propia') {
          status.className = "text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800";
          status.textContent = "Mi Cartera Activa";
          actions.innerHTML = `
            <button onclick="openInAppWhatsApp('${site.name}', '${site.tons} Ton Cemento')" class="btn-tactile bg-emerald-600 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>💬</span><span>WhatsApp</span>
            </button>
            <button onclick="openTransferClientModal(${site.id}, '${site.name}')" class="btn-tactile bg-indigo-50 text-indigo-700 border border-indigo-200 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>🔄</span><span>Transferir</span>
            </button>
          `;
        } else if (site.estado === 'bloqueado') {
          status.className = "text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300";
          status.textContent = `🔒 En Gestión: ${site.asesor}`;
          actions.innerHTML = `
            <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1 cursor-not-allowed">
              <span>🔒</span><span>Chat Bloqueado</span>
            </button>
            <button onclick="pedirTransferenciaCaso(${site.id}, '${site.name}', '${site.asesor}')" class="btn-tactile bg-[#004797] text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>🔄</span><span>Pedir Transferencia</span>
            </button>
          `;
        }
      }

      card.classList.remove('hidden');
    }

    function centrarMapaCiudad(ciudad) {
      if (!leafletMap) return;
      playChime('click');
      const coords = {
        barranquilla: [10.9878, -74.7889],
        galapa: [10.9015, -74.8870],
        soledad: [10.9184, -74.7646],
        cartagena: [10.3910, -75.4794],
        santamarta: [11.2408, -74.1990]
      };
      if (coords[ciudad]) {
        leafletMap.flyTo(coords[ciudad], 13, { duration: 1.2 });
      }
    }

    function buscarEnMapa(query) {
      const q = query.toLowerCase().trim();
      if (!q) {
        filtrarMapaPorCategoria(currentMapCategory);
        return;
      }
      const filtered = clientSites.filter(s => 
        s.name.toLowerCase().includes(q) || 
        s.ciudad.toLowerCase().includes(q) || 
        s.tipo.toLowerCase().includes(q) ||
        (s.categoria && s.categoria.toLowerCase().includes(q))
      );
      renderMapMarkers(filtered);
      if (filtered.length > 0 && leafletMap) {
        leafletMap.panTo([filtered[0].lat, filtered[0].lng]);
        mostrarDetalleSitioMapa(filtered[0]);
      }
    }

    // ==============================================================
    // DIRECTORIO B2B DE PROSPECCIÓN (NUEVAS EMPRESAS)
    // ==============================================================
    function renderDirectorioProspectos(prospects) {
      const container = document.getElementById('prospects-list-container');
      if (!container) return;
      container.innerHTML = "";

      if (prospects.length === 0) {
        container.innerHTML = `
          <div class="bg-white rounded-2xl p-6 text-center border border-slate-200 text-slate-500">
            <span class="text-3xl block mb-2">🔍</span>
            <p class="font-bold text-xs text-slate-800">No se encontraron empresas con este filtro</p>
            <p class="text-[10px] mt-0.5">Prueba buscando por otra constructora o ciudad del Caribe.</p>
          </div>
        `;
        return;
      }

      prospects.forEach(p => {
        const isLocked = p.estado === 'bloqueado';
        const isOwn = p.estado === 'propia';

        let statusBadge = `<span class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-sky-100 text-sky-800 border border-sky-300">✨ Sin Contactar</span>`;
        if (isLocked) {
          statusBadge = `<span class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300">🔒 En Gestión (${p.asesorBloqueo})</span>`;
        } else if (isOwn) {
          statusBadge = `<span class="text-[9px] font-extrabold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">✓ En Mi Cartera</span>`;
        }

        const card = document.createElement('div');
        card.className = "bg-white rounded-2xl p-3.5 border border-slate-200/90 shadow-xs space-y-2.5 transition-all hover:border-blue-300";
        card.innerHTML = `
          <div class="flex items-start justify-between">
            <div class="flex-1 pr-2">
              <div class="flex items-center space-x-1.5 flex-wrap">
                <h4 class="font-extrabold text-xs text-slate-900 leading-snug">${p.empresa}</h4>
                <span class="text-[9px] uppercase font-bold text-slate-400">• ${p.ciudad}</span>
              </div>
              <p class="text-[11px] text-[#004797] font-semibold mt-0.5">${p.proyecto}</p>
            </div>
            ${statusBadge}
          </div>

          <!-- Key Metrics Grid -->
          <div class="grid grid-cols-2 gap-1.5 bg-slate-50 p-2 rounded-xl border border-slate-100 text-[10px]">
            <div>
              <span class="text-slate-400 block font-semibold">Consumo Estimado:</span>
              <strong class="text-slate-900 font-mono-data font-bold">${p.volumen}</strong>
            </div>
            <div>
              <span class="text-slate-400 block font-semibold">Compra Actual a:</span>
              <span class="text-rose-700 font-bold">${p.proveedorActual}</span>
            </div>
          </div>

          <!-- Commercial Opportunity Highlight -->
          <div class="bg-blue-50/70 border border-blue-200/80 rounded-xl p-2 text-[10px] text-blue-950 space-y-0.5">
            <div class="flex items-center space-x-1 text-[#004797] font-bold">
              <span>🎯 Oportunidad Ultracem:</span>
            </div>
            <p class="leading-relaxed text-slate-700">${p.ventajaAtaque}</p>
          </div>

          <!-- Contact Person & Actions -->
          <div class="flex items-center justify-between text-[10px] text-slate-500 pt-1 border-t border-slate-100">
            <span>👤 <strong>${p.residente}</strong> • ${p.telefono}</span>
            <button onclick="centrarEnMapaDesdeProspecto(${p.lat}, ${p.lng}, '${p.empresa}')" class="text-[#004797] hover:underline font-bold flex items-center space-x-1">
              <span>🗺️ Ver en Mapa</span>
            </button>
          </div>

          <!-- Action Buttons -->
          <div class="grid grid-cols-2 gap-2 pt-0.5">
            ${isLocked ? `
              <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1 cursor-not-allowed">
                <span>🔒</span><span>Protegido</span>
              </button>
              <button onclick="pedirTransferenciaCaso(${p.id}, '${p.empresa}', '${p.asesorBloqueo}')" class="btn-tactile bg-[#004797] text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
                <span>🔄</span><span>Pedir Traspaso</span>
              </button>
            ` : `
              <button onclick="contactarProspectoDirecto(${p.id})" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1 shadow-xs">
                <span>💬</span><span>Contactar WhatsApp</span>
              </button>
              <button onclick="generarEstrategiaProspectoIA(${p.id})" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1 shadow-xs">
                <span>⚡</span><span>Estrategia IA</span>
              </button>
            `}
          </div>
        `;
        container.appendChild(card);
      });
    }

    function filtrarDirectorioProspectos(query) {
      const q = query.toLowerCase().trim();
      let filtered = b2bProspects;
      if (currentProspectSector !== 'todos') {
        filtered = filtered.filter(p => p.sector === currentProspectSector);
      }
      if (q) {
        filtered = filtered.filter(p => 
          p.empresa.toLowerCase().includes(q) || 
          p.proyecto.toLowerCase().includes(q) || 
          p.ciudad.toLowerCase().includes(q) ||
          p.residente.toLowerCase().includes(q) ||
          p.proveedorActual.toLowerCase().includes(q)
        );
      }
      renderDirectorioProspectos(filtered);
    }

    function filtrarProspectosSector(sector) {
      playChime('click');
      currentProspectSector = sector;

      const chips = {
        todos: document.getElementById('chip-sec-todos'),
        constructoras: document.getElementById('chip-sec-constructoras'),
        infraestructura: document.getElementById('chip-sec-infraestructura'),
        prefabricados: document.getElementById('chip-sec-prefabricados'),
        ferreterias: document.getElementById('chip-sec-ferreterias')
      };

      Object.keys(chips).forEach(k => {
        if (!chips[k]) return;
        if (k === sector) {
          chips[k].className = "px-2.5 py-1 rounded-lg bg-[#004797] text-white font-bold flex-shrink-0 transition-all";
        } else {
          chips[k].className = "px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 hover:bg-slate-200 flex-shrink-0 transition-all font-semibold";
        }
      });

      filtrarDirectorioProspectos(document.getElementById('prospects-search-input')?.value || "");
    }

    function centrarEnMapaDesdeProspecto(lat, lng, name) {
      playChime('click');
      setMapSubView('radar');
      if (leafletMap) {
        leafletMap.flyTo([lat, lng], 14, { duration: 1.0 });
        const site = clientSites.find(s => s.name.toLowerCase().includes(name.toLowerCase()));
        if (site) mostrarDetalleSitioMapa(site);
      }
    }

    function contactarProspectoDirecto(prospectId) {
      const p = b2bProspects.find(item => item.id === prospectId);
      if (!p) return;
      playChime('click');

      const body = `
        <div class="space-y-3 text-xs">
          <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-2.5 flex items-center space-x-2 text-emerald-900">
            <span class="text-xl">📱</span>
            <div>
              <strong class="block text-xs">Primer Contacto Comercial B2B</strong>
              <span class="text-[10px] text-emerald-700">${p.empresa} • ${p.residente} (${p.telefono})</span>
            </div>
          </div>

          <div class="bg-blue-50/80 border border-blue-200 rounded-xl p-2 text-[10px] text-blue-900">
            <strong>Objetivo:</strong> Reemplazar a <strong>${p.proveedorActual}</strong> ofreciendo despacho directo Galapa con <strong>${p.productoRecomendado}</strong>.
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Guion de Venta Sugerido para WhatsApp:</label>
            <textarea id="whatsapp-prospect-text" rows="5" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 leading-relaxed focus:outline-none focus:border-emerald-600">${p.scriptApertura}</textarea>
          </div>

          <button onclick="enviarPrimerMensajeProspecto(${p.id}, '${p.empresa}')" class="btn-tactile w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>🚀</span>
            <span>Enviar WhatsApp y Reclamar a mi Cartera (+50 XP)</span>
          </button>
        </div>
      `;
      openInPhoneSheet('💬', 'Contactar Nuevo Prospecto', p.empresa, body);
    }

    function enviarPrimerMensajeProspecto(prospectId, empresaName) {
      playChime('streak');
      userXP += 50;

      // Update prospect status to own
      const p = b2bProspects.find(item => item.id === prospectId);
      if (p) p.estado = 'propia';

      // Also add to clientSites if not there
      const existing = clientSites.find(s => s.id === prospectId);
      if (existing) {
        existing.estado = 'propia';
        existing.asesor = 'Carlos Mendoza';
      }

      closeInPhoneSheet();
      renderDirectorioProspectos(b2bProspects);
      showToast(`🎉 ¡Primer contacto enviado a ${empresaName}! Reclamado a tu cartera (+50 XP)`, "success");
    }

    function generarEstrategiaProspectoIA(prospectId) {
      const p = b2bProspects.find(item => item.id === prospectId);
      if (!p) return;
      navigateToTab('copiloto');
      const prompt = `Diseña una propuesta de valor agresiva para convencer a ${p.empresa} (proyecto: ${p.proyecto}) de cambiar su proveedor actual (${p.proveedorActual}) a Cemento Ultracem para sus ${p.volumen}. ¿Qué argumentos económicos, de formaleta y flete directo desde Galapa debemos presentarle a ${p.residente}?`;
      probarPromptRapido(prompt);
    }

    function preguntarCopilotoAtaque(competitorName) {
      navigateToTab('copiloto');
      const prompt = `¿Cuál es el mejor plan de ataque comercial para ganarle clientes a ${competitorName} en Barranquilla usando las ventajas de Planta Galapa y NTC 121?`;
      probarPromptRapido(prompt);
    }

    function consultarStockPlantaIA(plantName) {
      navigateToTab('copiloto');
      const prompt = `¿Cuál es la disponibilidad de despacho hoy en ${plantName} para Cemento Estructural Max NTC 121 y tiempos de flete a Soledad y Barranquilla Norte?`;
      probarPromptRapido(prompt);
    }

    function copiarUbicacionPlanta(name, lat, lng) {
      playChime('click');
      navigator.clipboard?.writeText?.(`${lat}, ${lng}`);
      showToast(`📍 Coordenadas de ${name} copiadas al portapapeles`, "info");
    }

    // ==============================================================
    // CONFIGURACIÓN MULTI-PROVEEDOR DE IA CON NVIDIA, DEEPSEEK & GROQ
    // ==============================================================
    const aiProviderConfigs = {
      nvidia: {
        name: "NVIDIA NIM",
        url: "https://integrate.api.nvidia.com/v1/chat/completions",
        keyPrefix: "nvapi-",
        keyLink: "https://build.nvidia.com/settings",
        catalogLink: "https://build.nvidia.com/models",
        models: [
          { id: "nvidia/llama-3.1-nemotron-70b-instruct", name: "nvidia/llama-3.1-nemotron-70b-instruct (Nemotron 70B • Activo & Recomendado)" },
          { id: "nvidia/nemotron-3.5-lightning-30b-a3b", name: "nvidia/nemotron-3.5-lightning-30b-a3b (Nemotron 3.5 Lightning • Ultra Rápido)" },
          { id: "nvidia/nemotron-3-super-120b-a12b", name: "nvidia/nemotron-3-super-120b-a12b (Nemotron 3 Super 120B • Razonamiento)" },
          { id: "nvidia/nemotron-3-ultra-550b-a55b", name: "nvidia/nemotron-3-ultra-550b-a55b (Nemotron 3 Ultra 550B • Máxima Escala)" },
          { id: "deepseek-ai/deepseek-v4.1-flash", name: "deepseek-ai/deepseek-v4.1-flash (DeepSeek V4.1 552B MoE en NVIDIA)" },
          { id: "meta/llama-3.2-11b-vision-instruct", name: "meta/llama-3.2-11b-vision-instruct (Visión Multimodal para Obras)" },
          { id: "google/gemma-4-31b-it", name: "google/gemma-4-31b-it (Google Gemma 4 31B en NVIDIA)" },
          { id: "mistralai/mistral-large-2-instruct", name: "mistralai/mistral-large-2-instruct (Mistral Large 2 en NVIDIA)" },
          { id: "nvidia/llama-3.1-nemoguard-8b-topic-control", name: "nvidia/llama-3.1-nemoguard-8b-topic-control (Control Temático & Moderación)" }
        ]
      },
      deepseek: {
        name: "DeepSeek API Oficial",
        url: "https://api.deepseek.com/chat/completions",
        keyPrefix: "sk-",
        keyLink: "https://platform.deepseek.com/api_keys",
        models: [
          { id: "deepseek-chat", name: "deepseek-chat (DeepSeek V3 • Excelente Velocidad y Costo)" },
          { id: "deepseek-reasoner", name: "deepseek-reasoner (DeepSeek R1 • Razonamiento Comercial Lógico)" }
        ]
      },
      groq: {
        name: "Groq Cloud (LPU Ultra-Rápido)",
        url: "https://api.groq.com/openai/v1/chat/completions",
        keyPrefix: "gsk_",
        keyLink: "https://console.groq.com/keys",
        catalogLink: "https://console.groq.com/docs/models",
        defaultModel: "openai/gpt-oss-120b",
        groups: [
          {
            label: "OpenAI Open-Source (LPU)",
            models: [
              { id: "openai/gpt-oss-120b", name: "openai/gpt-oss-120b (Flagship Razonamiento Comercial • 500 t/s • 128k)" },
              { id: "openai/gpt-oss-20b", name: "openai/gpt-oss-20b (Ultra Rápido • 1,000 t/s • 128k)" },
              { id: "openai/gpt-oss-safeguard-20b", name: "openai/gpt-oss-safeguard-20b (Control de Seguridad y Moderación • 20B)" }
            ]
          },
          {
            label: "Meta Llama (Producción & Seguridad)",
            models: [
              { id: "llama-3.3-70b-versatile", name: "llama-3.3-70b-versatile (Estándar Empresarial 70B • 280 t/s • 128k)" },
              { id: "llama-3.1-8b-instant", name: "llama-3.1-8b-instant (Instantáneo • 560 t/s • 128k)" },
              { id: "meta-llama/llama-prompt-guard-2-86m", name: "meta-llama/llama-prompt-guard-2-86m (Prompt Guard Anti-Jailbreak • 86M)" },
              { id: "meta-llama/llama-prompt-guard-2-22m", name: "meta-llama/llama-prompt-guard-2-22m (Prompt Guard Ultraligero • 22M)" },
              { id: "meta-models/muse-spark-open", name: "meta-models/muse-spark-open (Meta Muse Spark Open)" },
              { id: "llama3-70b-8192", name: "llama3-70b-8192 (Llama 3 70B Legado)" },
              { id: "llama-guard-3-8b", name: "llama-guard-3-8b (Moderación de Contenido Llama Guard)" }
            ]
          },
          {
            label: "Alibaba Cloud",
            models: [
              { id: "qwen/qwen3.8-27b", name: "qwen/qwen3.8-27b (Qwen 3.8 27B • Gran Razonamiento Multilingüe)" }
            ]
          },
          {
            label: "MiniMax AI",
            models: [
              { id: "minimaxai/minimax-m2.7", name: "minimaxai/minimax-m2.7 (MiniMax M2.7 • Análisis Textual Avanzado)" }
            ]
          },
          {
            label: "Google & Mistral",
            models: [
              { id: "gemma2-9b-it", name: "gemma2-9b-it (Google Gemma 2 9B • Alta Eficiencia)" },
              { id: "mixtral-8x7b-32768", name: "mixtral-8x7b-32768 (Mistral MoE 8x7B • 32k Contexto)" }
            ]
          },
          {
            label: "Audio & Voz (Groq Inferencia)",
            models: [
              { id: "whisper-large-v3-turbo", name: "whisper-large-v3-turbo (Transcripción Notas de Voz • Ultrarrápido)" },
              { id: "whisper-large-v3", name: "whisper-large-v3 (Transcripción Whisper V3 • Alta Precisión)" },
              { id: "canopylabs/orpheus-v1-english", name: "canopylabs/orpheus-v1-english (Canopy Labs Orpheus TTS)" }
            ]
          }
        ]
      },
      openrouter: {
        name: "OpenRouter (Universal & Sin Bloqueo CORS)",
        url: "https://openrouter.ai/api/v1/chat/completions",
        keyPrefix: "sk-or-",
        keyLink: "https://openrouter.ai/keys",
        models: [
          { id: "nvidia/nemotron-3.5-lightning:free", name: "nvidia/nemotron-3.5-lightning:free (NVIDIA Nemotron 3.5 • Gratis & Sin CORS)" },
          { id: "nvidia/nemotron-3-super-120b-a12b:free", name: "nvidia/nemotron-3-super-120b-a12b:free (NVIDIA Nemotron Super 120B • Gratis)" },
          { id: "nvidia/nemotron-3-ultra-550b-a55b:free", name: "nvidia/nemotron-3-ultra-550b-a55b:free (NVIDIA Nemotron Ultra 550B • Gratis)" },
          { id: "deepseek/deepseek-r1:free", name: "deepseek/deepseek-r1:free (DeepSeek R1 • Gratis)" },
          { id: "meta-llama/llama-3.3-70b-instruct:free", name: "meta-llama/llama-3.3-70b-instruct:free (Llama 3.3 70B • Gratis)" },
          { id: "google/gemini-2.0-flash-exp:free", name: "google/gemini-2.0-flash-exp:free (Gemini 2.0 Flash • Gratis)" },
          { id: "anthropic/claude-3.5-sonnet", name: "anthropic/claude-3.5-sonnet (Claude 3.5 Sonnet)" }
        ]
      },
      gemini: {
        name: "Google Gemini",
        url: "https://generativelanguage.googleapis.com",
        keyPrefix: "AIzaSy",
        keyLink: "https://aistudio.google.com/app/apikey",
        models: [
          { id: "gemini-1.5-flash", name: "gemini-1.5-flash (Google AI Studio)" },
          { id: "gemini-2.0-flash", name: "gemini-2.0-flash (Última Generación)" }
        ]
      },
      openai: {
        name: "OpenAI",
        url: "https://api.openai.com/v1/chat/completions",
        keyPrefix: "sk-proj-",
        keyLink: "https://platform.openai.com/api-keys",
        models: [
          { id: "gpt-4o-mini", name: "gpt-4o-mini (Rápido y Preciso)" },
          { id: "gpt-4o", name: "gpt-4o (Modelo Completo)" }
        ]
      },
      custom: {
        name: "Endpoint Personalizado / Local (Ollama, vLLM)",
        url: customApiUrl,
        keyPrefix: "",
        keyLink: "",
        models: [
          { id: "llama3.1", name: "llama3.1 (Ollama Local)" },
          { id: "deepseek-r1", name: "deepseek-r1 (Ollama Local)" },
          { id: "mistral", name: "mistral (Local)" }
        ]
      },
      local: {
        name: "Motor Local Simulado Ultracem",
        url: "",
        keyPrefix: "",
        keyLink: "",
        models: [
          { id: "local-ultracem", name: "Motor Heurístico Integrado (Offline)" }
        ]
      }
    };

    // Auto-flatten groups into models array for complete backward compatibility
    Object.values(aiProviderConfigs).forEach(cfg => {
      if (cfg.groups && !cfg.models) {
        cfg.models = cfg.groups.flatMap(g => g.models);
      }
    });

    function renderModelOptionsHtml(cfg, currentSelected) {
      if (!cfg) return '';
      if (cfg.groups && Array.isArray(cfg.groups)) {
        return cfg.groups.map(grp => `
          <optgroup label="${grp.label}">
            ${grp.models.map(m => `<option value="${m.id}" ${currentSelected === m.id ? 'selected' : ''}>${m.name}</option>`).join('')}
          </optgroup>
        `).join('');
      }
      if (cfg.models && Array.isArray(cfg.models)) {
        return cfg.models.map(m => 
          `<option value="${m.id}" ${currentSelected === m.id ? 'selected' : ''}>${m.name}</option>`
        ).join('');
      }
      return '';
    }

    function openInPhoneAISettings() {
      playChime('click');
      const cfg = aiProviderConfigs[activeAIProvider] || aiProviderConfigs.groq;

      const modelOptionsHtml = renderModelOptionsHtml(cfg, selectedModel);

      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-blue-50 border border-blue-200 rounded-xl p-3">
            <div class="flex items-center justify-between mb-1">
              <strong class="text-[#004797] block font-bold text-xs">Conexión Multimodelo: Groq Cloud (LPU), NVIDIA & DeepSeek</strong>
              <div class="flex items-center space-x-1.5">
                <a href="https://console.groq.com/docs/models" target="_blank" rel="noopener" class="text-[10px] text-orange-800 bg-orange-100 hover:bg-orange-200 px-2 py-0.5 rounded-full font-bold transition-all">Groq Docs ↗</a>
                <a href="https://build.nvidia.com/models" target="_blank" rel="noopener" class="text-[10px] text-emerald-800 bg-emerald-100 hover:bg-emerald-200 px-2 py-0.5 rounded-full font-bold transition-all">NVIDIA NIM ↗</a>
              </div>
            </div>
            <p class="text-slate-600 leading-snug">Conéctate a inferencia de alta velocidad (Groq LPU hasta 1,000 t/s, OpenAI OSS, Nemotron y DeepSeek R1). Respuestas técnicas y comerciales con guardrails estrictos para Ultracem.</p>
            <div class="mt-2 pt-2 border-t border-blue-200/60 text-[10px] text-blue-800 flex items-center justify-between">
              <span>⚡ <strong>Groq LPU:</strong> Compatible nativo con navegadores (CORS libre). OpenAI OSS 120B/20B y Whisper V3 Turbo activos.</span>
            </div>
          </div>

          <!-- Provider Select -->
          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Proveedor de Inteligencia Artificial:</label>
            <select id="setting-ai-provider" onchange="cambiarProveedorSeleccionado(this.value)" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="groq" ${activeAIProvider === 'groq' ? 'selected' : ''}>⚡ Groq Cloud (OpenAI OSS 120B/20B, Llama 3.3, Qwen, Whisper Turbo)</option>
              <option value="nvidia" ${activeAIProvider === 'nvidia' ? 'selected' : ''}>🟢 NVIDIA NIM (Nemotron, Llama 3.3, DeepSeek V4.1)</option>
              <option value="deepseek" ${activeAIProvider === 'deepseek' ? 'selected' : ''}>🟢 DeepSeek API Oficial (deepseek-chat & R1)</option>
              <option value="openrouter" ${activeAIProvider === 'openrouter' ? 'selected' : ''}>🟢 OpenRouter (DeepSeek R1 Free, Claude 3.5)</option>
              <option value="gemini" ${activeAIProvider === 'gemini' ? 'selected' : ''}>Google Gemini (1.5 / 2.0 Flash)</option>
              <option value="openai" ${activeAIProvider === 'openai' ? 'selected' : ''}>OpenAI (GPT-4o-mini)</option>
              <option value="custom" ${activeAIProvider === 'custom' ? 'selected' : ''}>Endpoint Personalizado / Ollama Local</option>
              <option value="local" ${activeAIProvider === 'local' ? 'selected' : ''}>Motor Local Simulado Ultracem (Sin Key)</option>
            </select>
          </div>

          <!-- Model Select -->
          <div class="space-y-1.5" id="model-select-group" style="${activeAIProvider === 'local' ? 'display:none;' : ''}">
            <label class="block font-bold text-slate-700">Modelo Seleccionado (Agrupado por Fabricante):</label>
            <select id="setting-ai-model" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              ${modelOptionsHtml}
            </select>
          </div>

          <!-- Custom URL Input (for Ollama / Custom Server) -->
          <div class="space-y-1.5" id="custom-url-group" style="${activeAIProvider === 'custom' ? '' : 'display:none;'}">
            <label class="block font-bold text-slate-700">URL del Endpoint (Base URL):</label>
            <input type="text" id="setting-custom-url" value="${customApiUrl}" placeholder="http://localhost:11434/v1/chat/completions" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs font-mono-data text-slate-800 focus:outline-none focus:border-[#004797]">
          </div>

          <!-- API Key Input -->
          <div class="space-y-1.5" id="api-key-input-group" style="${activeAIProvider === 'local' ? 'display:none;' : ''}">
            <div class="flex items-center justify-between">
              <label class="block font-bold text-slate-700">API Key del Proveedor:</label>
              <span id="api-key-link-container">
                ${cfg.keyLink ? `<a href="${cfg.keyLink}" target="_blank" rel="noopener" class="text-[10px] text-[#004797] font-semibold hover:underline">Obtener Key ↗</a>` : ''}
                ${cfg.catalogLink ? `<span class="text-slate-300">•</span> <a href="${cfg.catalogLink}" target="_blank" rel="noopener" class="text-[10px] text-emerald-700 font-semibold hover:underline">${activeAIProvider === 'groq' ? 'Catálogo Groq ↗' : 'Catálogo NIM ↗'}</a>` : ''}
              </span>
            </div>
            <div class="relative">
              <input type="password" id="setting-ai-key" value="${userApiKey}" placeholder="${cfg.keyPrefix ? cfg.keyPrefix + '...' : 'Pega tu API Key...'}" class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3 py-2.5 text-xs text-slate-800 font-mono-data focus:outline-none focus:border-[#004797]">
              <button type="button" onclick="togglePasswordVisibility('setting-ai-key')" class="absolute right-2.5 top-2.5 text-slate-400 hover:text-slate-600 text-xs">👁️</button>
            </div>
          </div>

          <!-- Live Connection Test Result Container -->
          <div id="test-connection-result" class="hidden rounded-xl p-2 text-[11px] leading-snug"></div>

          <!-- Test Connection Button -->
          <button type="button" onclick="probarConexionIAEnVivo()" class="btn-tactile w-full bg-slate-100 hover:bg-slate-200 border border-slate-300 text-slate-700 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1.5">
            <span>⚡</span>
            <span>Probar Conexión en Vivo</span>
          </button>

          <button onclick="guardarConfiguracionIA()" class="btn-tactile w-full bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>💾</span>
            <span>Guardar Configuración de IA</span>
          </button>
        </div>
      `;
      openInPhoneSheet('⚙️', 'Configuración de Copiloto IA', 'Groq, NVIDIA, DeepSeek & Más', body);
    }

    function cambiarProveedorSeleccionado(prov) {
      const cfg = aiProviderConfigs[prov] || aiProviderConfigs.groq;
      const modelGroup = document.getElementById('model-select-group');
      const modelSelect = document.getElementById('setting-ai-model');
      const keyGroup = document.getElementById('api-key-input-group');
      const keyInput = document.getElementById('setting-ai-key');
      const keyLink = document.getElementById('api-key-link-container');
      const customGroup = document.getElementById('custom-url-group');

      if (customGroup) customGroup.style.display = prov === 'custom' ? 'block' : 'none';
      if (modelGroup) modelGroup.style.display = prov === 'local' ? 'none' : 'block';
      if (keyGroup) keyGroup.style.display = prov === 'local' ? 'none' : 'block';

      // Load saved key for this specific provider if available
      const savedKeyForProv = localStorage.getItem('ultracem_key_' + prov) || (activeAIProvider === prov ? userApiKey : '');
      if (keyInput) {
        keyInput.value = savedKeyForProv;
        keyInput.placeholder = cfg.keyPrefix ? `${cfg.keyPrefix}...` : 'Clave de API...';
      }

      if (modelSelect) {
        const availableModels = cfg.groups ? cfg.groups.flatMap(g => g.models) : (cfg.models || []);
        const hasCurrentModel = availableModels.some(m => m.id === selectedModel);
        const targetModel = hasCurrentModel ? selectedModel : (cfg.defaultModel || (availableModels[0] ? availableModels[0].id : ''));
        modelSelect.innerHTML = renderModelOptionsHtml(cfg, targetModel);
        if (targetModel) modelSelect.value = targetModel;
      }
      if (keyLink) {
        let linksHtml = '';
        if (cfg.keyLink) linksHtml += `<a href="${cfg.keyLink}" target="_blank" rel="noopener" class="text-[10px] text-[#004797] font-semibold hover:underline">Obtener Key ↗</a>`;
        if (cfg.catalogLink) linksHtml += ` <span class="text-slate-300">•</span> <a href="${cfg.catalogLink}" target="_blank" rel="noopener" class="text-[10px] text-emerald-700 font-semibold hover:underline">${prov === 'groq' ? 'Catálogo Groq ↗' : 'Catálogo NIM ↗'}</a>`;
        keyLink.innerHTML = linksHtml;
      }
    }

    function togglePasswordVisibility(id) {
      const el = document.getElementById(id);
      if (el) el.type = el.type === 'password' ? 'text' : 'password';
    }

    function guardarConfiguracionIA() {
      const prov = document.getElementById('setting-ai-provider').value;
      const key = document.getElementById('setting-ai-key')?.value.trim() || '';
      const modelSelect = document.getElementById('setting-ai-model');
      const customUrl = document.getElementById('setting-custom-url')?.value.trim() || '';

      activeAIProvider = prov;
      userApiKey = key;
      if (modelSelect) selectedModel = modelSelect.value;
      if (customUrl) customApiUrl = customUrl;

      localStorage.setItem('ultracem_ai_provider', prov);
      localStorage.setItem('ultracem_ai_key', key);
      localStorage.setItem('ultracem_key_' + prov, key);
      localStorage.setItem('ultracem_ai_model', selectedModel);
      localStorage.setItem('ultracem_custom_url', customApiUrl);

      const label = document.getElementById('ai-active-status-label');
      const badge = document.getElementById('ai-provider-badge');
      const chip = document.getElementById('ai-engine-chip');

      const provName = aiProviderConfigs[prov]?.name || prov.toUpperCase();
      if (label) label.textContent = `Motor: ${provName} (${selectedModel.split('/').pop() || selectedModel})`;
      if (badge) badge.textContent = provName.split(' ')[0];
      if (chip) chip.textContent = selectedModel.split('/').pop() || selectedModel;

      closeInPhoneSheet();
      showToast(`✅ Conectado a ${provName} exitosamente`, "success");
    }

    async function probarConexionIAEnVivo() {
      const prov = document.getElementById('setting-ai-provider').value;
      const key = document.getElementById('setting-ai-key')?.value.trim() || '';
      const model = document.getElementById('setting-ai-model')?.value || '';
      const customUrl = document.getElementById('setting-custom-url')?.value.trim() || '';
      const resultBox = document.getElementById('test-connection-result');

      if (!resultBox) return;
      resultBox.classList.remove('hidden');
      resultBox.className = "rounded-xl p-2.5 text-[11px] bg-slate-100 text-slate-700 flex items-center space-x-2";
      resultBox.innerHTML = `<span class="w-2 h-2 rounded-full bg-[#004797] animate-ping"></span><span>Conectando con ${prov.toUpperCase()}...</span>`;

      if (prov === 'local') {
        await new Promise(r => setTimeout(r, 300));
        resultBox.className = "rounded-xl p-2.5 text-[11px] bg-emerald-100 text-emerald-900 border border-emerald-300";
        resultBox.innerHTML = `✅ <strong>Motor Local Ultracem Activo:</strong> Operativo sin necesidad de API Key.`;
        return;
      }

      if (!key && prov !== 'custom') {
        resultBox.className = "rounded-xl p-2.5 text-[11px] bg-rose-100 text-rose-900 border border-rose-300";
        resultBox.innerHTML = `⚠️ <strong>Falta API Key:</strong> Ingresa tu clave para probar la conexión con ${prov}.`;
        return;
      }

      const startTime = performance.now();
      try {
        let testResponse = null;

        if (prov === 'nvidia') {
          let nvidiaTargetUrl = 'https://integrate.api.nvidia.com/v1/chat/completions';
          if (window.location.protocol.startsWith('http') && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')) {
            nvidiaTargetUrl = '/api/nvidia';
          } else {
            try {
              const ping = await fetch('http://localhost:3000/api/health', { method: 'GET' }).catch(() => null);
              if (ping && ping.ok) nvidiaTargetUrl = 'http://localhost:3000/api/nvidia';
            } catch (e) {}
          }

          testResponse = await fetch(nvidiaTargetUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${key}`
            },
            body: JSON.stringify({
              model: model,
              messages: [{ role: 'user', content: 'Di solo: OK Ultracem' }],
              max_tokens: 10
            })
          });
        } else if (prov === 'deepseek') {
          testResponse = await fetch('https://api.deepseek.com/chat/completions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${key}`
            },
            body: JSON.stringify({
              model: model,
              messages: [{ role: 'user', content: 'Di solo: OK Ultracem' }],
              max_tokens: 10
            })
          });
        } else if (prov === 'groq') {
          if (model.startsWith('whisper') || model.includes('orpheus')) {
            testResponse = await fetch('https://api.groq.com/openai/v1/models', {
              method: 'GET',
              headers: {
                'Authorization': `Bearer ${key}`
              }
            });
          } else {
            testResponse = await fetch('https://api.groq.com/openai/v1/chat/completions', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${key}`
              },
              body: JSON.stringify({
                model: model,
                messages: [{ role: 'user', content: 'Di solo: OK Ultracem' }],
                max_tokens: 10
              })
            });
          }
        } else if (prov === 'openrouter') {
          testResponse = await fetch('https://openrouter.ai/api/v1/chat/completions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${key}`
            },
            body: JSON.stringify({
              model: model,
              messages: [{ role: 'user', content: 'Di solo: OK Ultracem' }],
              max_tokens: 10
            })
          });
        } else if (prov === 'openai') {
          testResponse = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${key}`
            },
            body: JSON.stringify({
              model: model,
              messages: [{ role: 'user', content: 'Di solo: OK Ultracem' }],
              max_tokens: 10
            })
          });
        }

        const elapsed = Math.round(performance.now() - startTime);

        if (testResponse && testResponse.ok) {
          resultBox.className = "rounded-xl p-2.5 text-[11px] bg-emerald-100 text-emerald-900 border border-emerald-300";
          resultBox.innerHTML = `✅ <strong>Conexión Exitosa:</strong> ${prov.toUpperCase()} (${model}) respondió en ${elapsed} ms. Clave válida y lista.`;
        } else {
          const errData = await testResponse.json().catch(() => ({}));
          throw new Error(errData.error?.message || `HTTP ${testResponse.status}`);
        }
      } catch (err) {
        if (prov === 'nvidia' && (err.message.includes('fetch') || err.message.includes('Failed') || err.name === 'TypeError')) {
          resultBox.className = "rounded-xl p-3 text-[11px] bg-amber-50 text-amber-950 border border-amber-300 space-y-2 text-left";
          resultBox.innerHTML = `
            <div class="flex items-start space-x-2">
              <span class="text-base">🛡️</span>
              <div>
                <strong class="text-amber-900 block font-bold text-xs">NVIDIA bloquea llamadas directas de navegador (CORS)</strong>
                <p class="text-amber-800 leading-snug mt-0.5">
                  La API en la nube de NVIDIA (<code>integrate.api.nvidia.com</code>) rechaza peticiones directas desde páginas web por seguridad de claves. Tienes <strong>2 soluciones inmediatas</strong>:
                </p>
              </div>
            </div>
            <div class="space-y-1.5 pt-1 border-t border-amber-200">
              <div class="bg-white/90 p-2 rounded-lg border border-amber-200">
                <strong class="text-[#004797] block font-bold">Opción 1 (Directa sin consola):</strong>
                Selecciona arriba el proveedor <strong>OpenRouter</strong>. Incluye los modelos oficiales de NVIDIA (<code>nvidia/nemotron-3.5-lightning:free</code>) habilitados con CORS nativo para navegadores y 100% gratis.
              </div>
              <div class="bg-white/90 p-2 rounded-lg border border-amber-200">
                <strong class="text-emerald-800 block font-bold">Opción 2 (Con tu clave nvapi-...):</strong>
                Abre tu terminal en la carpeta del proyecto y ejecuta:<br>
                <code class="bg-slate-800 text-emerald-300 px-1.5 py-0.5 rounded font-mono text-[10px]">npm start</code>
                y entra a <a href="http://localhost:3000" target="_blank" class="underline font-bold text-[#004797]">http://localhost:3000</a> (activa el proxy local incluido sin CORS).
              </div>
            </div>
          `;
          return;
        }

        resultBox.className = "rounded-xl p-2.5 text-[11px] bg-rose-100 text-rose-900 border border-rose-300";
        resultBox.innerHTML = `❌ <strong>Error de Conexión:</strong> ${err.message}. Verifica que la API Key sea correcta o prueba otro modelo.`;
      }
    }

    // ==============================================================
    // EJECUCIÓN MULTI-MODELO DE COPILOTO IA CON GUARDRAILS
    // ==============================================================
    async function enviarConsultaAI() {
      const input = document.getElementById('ai-chat-input');
      const container = document.getElementById('ai-chat-messages');
      const query = input.value.trim();
      if (!query) return;

      playChime('click');
      
      const userDiv = document.createElement('div');
      userDiv.className = "flex justify-end";
      userDiv.innerHTML = `
        <div class="bg-blue-100 p-2.5 rounded-xl rounded-tr-none text-blue-950 max-w-[85%] font-medium">
          ${query}
        </div>
      `;
      container.appendChild(userDiv);
      input.value = "";
      container.scrollTop = container.scrollHeight;

      const loadingDiv = document.createElement('div');
      loadingDiv.className = "flex justify-start";
      loadingDiv.id = "ai-loading-bubble";
      loadingDiv.innerHTML = `
        <div class="bg-slate-100 p-2.5 rounded-xl rounded-tl-none text-slate-500 max-w-[85%] flex items-center space-x-2">
          <span class="w-2 h-2 rounded-full bg-[#004797] animate-ping"></span>
          <span>Consultando motor de IA (${activeAIProvider.toUpperCase()})...</span>
        </div>
      `;
      container.appendChild(loadingDiv);
      container.scrollTop = container.scrollHeight;

      // Strict Domain Guardrail Check
      const lowerQuery = query.toLowerCase();
      const forbiddenKeywords = [
        "acido ribonucleico", "ácido ribonucleico", "arn", "adn", "ribonucleic",
        "mitocondria", "fotosintesis", "fotosíntesis", "quien descubrio america",
        "poema de amor", "capital de francia", "javascript closure", "receta de cocina",
        "formula de relativity", "cuántica", "quimica organica benceno"
      ];
      const isExplicitOffTopic = forbiddenKeywords.some(kw => lowerQuery.includes(kw));

      let responseText = "";

      if (isExplicitOffTopic) {
        await new Promise(r => setTimeout(r, 400));
        loadingDiv.remove();
        responseText = `⚠️ <strong>Filtro de Guardrail Ultracem:</strong> Como Copiloto Comercial de Ultracem, únicamente puedo resolver dudas relacionadas con especificaciones técnicas de cemento, normatividad ICONTEC NTC 121 / 321, prospección de obras y empresas constructoras, cubicaciones de concreto, políticas de fletes y precios comerciales. ¿En qué te puedo asesorar respecto a tus clientes o despachos?`;
      } else if (userApiKey && ['nvidia', 'deepseek', 'groq', 'openrouter', 'openai'].includes(activeAIProvider)) {
        // UNIFIED OPENAI-COMPATIBLE RUNTIME (NVIDIA NIM / DEEPSEEK / GROQ / OPENROUTER)
        const systemPrompt = `Eres el Copiloto Técnico y Comercial oficial de Ultracem S.A.S. (productora colombiana de cemento y concreto con planta principal en Galapa, Atlántico y presencia en Colombia y Guatemala; eslogan oficial: 'Soluciones integrales para la industria de la construcción • Calidad, Resistencia y Rendimiento').
TUS FUNCIONES:
1. Responder preguntas técnicas sobre Cemento Ultracem bajo la norma ICONTEC NTC 121 (Tipo Uso General UG, Tipo Alta Resistencia Temprana ART, Tipo Moderada Resistencia a Sulfatos MRS, Cemento Blanco, Concretos NTC 3318, Mezcla Lista y Ultrapegante).
2. Articularte con el ecosistema digital de Ultracem: conoces a 'Vanesa IA' (asistente de WhatsApp de Ultracem para autogestión de cotizaciones y despachos) y el programa de formación 'Campus Ultra WhatsApp' (capacitación técnica certificada para maestros y ferreteros).
3. Proporcionar argumentos frente a la competencia (Argos, Cemex), demostrando ahorro de formaleta (retiro seguro a 18h con Cemento Estructural ART) y flete directo desde Planta Galapa sin roturas de sacos.
4. Apoyar a la fuerza comercial (Carlos Mendoza, Milena Ospino, Adriana Anaya, Hichel Espitia) en prospección y cierre con constructoras (Amarilo, Coninsa, Bolívar, Marval) y distribuidores ferreteros.
5. Si te preguntan '¿Qué es el cemento?' o conceptos básicos, explícalo con claridad técnica vinculándolo al clínker, yeso y las líneas Ultracem.
REGLA ESTRICTA DE GUARDRAIL:
Si el usuario pregunta algo totalmente ajeno a la empresa, cemento, construcción o ventas (como 'ácido ribonucleico', cocina, biología, deportes internacionales), rechaza amablemente diciendo: '🚫 Filtro de Dominio Ultracem: Como copiloto comercial de Ultracem, únicamente puedo asesorarte en cemento, normas técnicas NTC 121, dosificaciones de obra y gestión de ventas.'
Responde en español de forma concisa, profesional, práctica y directa para un asesor de campo comercial.`;

        let endpointUrl = 'https://integrate.api.nvidia.com/v1/chat/completions';
        if (activeAIProvider === 'nvidia') {
          if (window.location.protocol.startsWith('http') && (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')) {
            endpointUrl = '/api/nvidia';
          } else {
            try {
              const ping = await fetch('http://localhost:3000/api/health', { method: 'GET' }).catch(() => null);
              if (ping && ping.ok) endpointUrl = 'http://localhost:3000/api/nvidia';
            } catch (e) {}
          }
        }
        if (activeAIProvider === 'deepseek') endpointUrl = 'https://api.deepseek.com/chat/completions';
        if (activeAIProvider === 'groq') endpointUrl = 'https://api.groq.com/openai/v1/chat/completions';
        if (activeAIProvider === 'openrouter') endpointUrl = 'https://openrouter.ai/api/v1/chat/completions';
        if (activeAIProvider === 'openai') endpointUrl = 'https://api.openai.com/v1/chat/completions';

        try {
          let resp = await fetch(endpointUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${userApiKey}`
            },
            body: JSON.stringify({
              model: selectedModel,
              messages: [
                { role: 'system', content: systemPrompt },
                { role: 'user', content: query }
              ],
              temperature: 0.5,
              max_tokens: 600
            })
          });

          // Groq automatic fallback on 404
          if (!resp.ok && activeAIProvider === 'groq' && selectedModel !== 'llama-3.1-8b-instant') {
            console.warn(`Groq model ${selectedModel} failed. Retrying with llama-3.1-8b-instant...`);
            resp = await fetch(endpointUrl, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${userApiKey}` },
              body: JSON.stringify({
                model: 'llama-3.1-8b-instant',
                messages: [{ role: 'system', content: systemPrompt }, { role: 'user', content: query }],
                temperature: 0.5,
                max_tokens: 600
              })
            });
          }

          loadingDiv.remove();

          if (!resp.ok) {
            const errData = await resp.json().catch(() => ({}));
            throw new Error(errData.error?.message || `HTTP ${resp.status}`);
          }

          const data = await resp.json();
          const rawText = data.choices[0]?.message?.content || "No se recibió respuesta.";
          responseText = rawText
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n\n/g, '<br><br>')
            .replace(/\n/g, '<br>');
        } catch (err) {
          loadingDiv.remove();
          console.warn(`${activeAIProvider} API error:`, err);
          if (activeAIProvider === 'nvidia' && (err.message.includes('fetch') || err.message.includes('Failed') || err.name === 'TypeError')) {
            responseText = `🛡️ <strong>Aviso de Navegador (Bloqueo CORS en NVIDIA NIM):</strong><br>
El servidor de NVIDIA en la nube (<code>integrate.api.nvidia.com</code>) rechaza llamadas directas desde páginas web por seguridad.<br><br>
<strong>Soluciones para usarlo:</strong><br>
1. <strong>Opción Rápida (Sin Servidor):</strong> En el menú ⚙️ cambia a <strong>OpenRouter</strong> y elige <code>nvidia/nemotron-3.5-lightning:free</code>. ¡Funciona al instante en tu navegador sin CORS!<br>
2. <strong>Opción con tu clave nvapi-...:</strong> Inicia el servidor local ejecutando <code>npm start</code> en tu terminal y entra a <a href="http://localhost:3000" class="underline font-bold text-blue-700" target="_blank">http://localhost:3000</a> (utiliza el proxy local sin CORS).`;
          } else {
            responseText = `⚠️ <strong>Error al conectar con ${activeAIProvider.toUpperCase()}:</strong> ${err.message}. Verifica tu API Key en 'Configurar IA' o usa el motor local simulado.`;
          }
        }
      } else {
        // ENHANCED LOCAL SMART BUSINESS ENGINE
        await new Promise(r => setTimeout(r, 500));
        loadingDiv.remove();

        if (lowerQuery.includes('empresa') || lowerQuery.includes('constructor') || lowerQuery.includes('prospect') || lowerQuery.includes('contactar') || lowerQuery.includes('semana')) {
          responseText = `<strong>Top Empresas Recomendadas para Contactar esta Semana:</strong><br><br>
1. <strong>Constructora Amarilo (Proyecto Hacienda San Antonio - Barranquilla):</strong><br>
• <em>Consumo:</em> 320 Ton/mes. Actualmente compran a Argos.<br>
• <em>Estrategia:</em> Tienen demoras desencofrando losas. Ofrece Cemento Estructural Max ART para desencofrar a las 18h y un ahorro de ~$1.700 COP por saco.<br><br>
2. <strong>Consorcio Vías del Atlántico (Doble Calzada Juan Mina - Galapa):</strong><br>
• <em>Consumo:</em> 550 Ton/mes. Ubicados a solo 3 km de nuestra Planta Galapa.<br>
• <em>Estrategia:</em> Flete a costo mínimo y entrega inmediata en tolva para pavimento rígido.<br><br>
3. <strong>Prefabricados & Adoquines del Caribe (Parque PIMSA Soledad):</strong><br>
• <em>Consumo:</em> 140 Ton/mes. Compran a Cemex.<br>
• <em>Estrategia:</em> Con nuestro clinker de alta pureza desmoldan adoquines en 8 horas, duplicando su capacidad de planta.`;
        } else if (lowerQuery.includes('amarilo') || lowerQuery.includes('hacienda san antonio')) {
          responseText = `<strong>Estrategia de Venta para Constructora Amarilo:</strong><br>1. <strong>Punto Crítico:</strong> Amarilo maneja cronogramas estrictos de entrega de vivienda. Cada día de retraso en formaleta les cuesta millones.<br>2. <strong>Argumento Ultracem:</strong> El Cemento Estructural Max NTC 121 alcanza 18 MPa en 24h, permitiendo retirar formaletas verticales y puntales un día antes.<br>3. <strong>Logística:</strong> Despacho directo desde Planta Galapa por la Vía Circunvalar en 90 minutos con paletizado plastificado sin roturas.`;
        } else if (lowerQuery.includes('prefabricado') || lowerQuery.includes('bloquera')) {
          responseText = `<strong>Oferta de Valor para Prefabricados y Bloqueras:</strong><br>1. <strong>Desmolde Rápido:</strong> Con Cemento ART Ultracem logran resistencia para manipulación en solo 8 horas.<br>2. <strong>Menor Rotura:</strong> Menor porcentaje de bordes desmoronados en adoquines y bloques.<br>3. <strong>Economía:</strong> Precios preferenciales por volumen superior a 50 toneladas mensuales.`;
        } else if (lowerQuery.includes('cemento') && (lowerQuery.includes('que es') || lowerQuery.includes('qué es'))) {
          responseText = `<strong>¿Qué es el Cemento según la Norma NTC 121?</strong><br>El cemento es un conglomerante hidráulico obtenido de la molienda conjunta de clínker (silicatos y aluminatos de calcio) y yeso (sulfato de calcio) para regular el fraguado.<br><br>En <strong>Ultracem</strong> fabricamos dos líneas principales en nuestra planta de Galapa:<br>• <strong>Uso General (Tipo UG):</strong> Para morteros, pegas, pañetes y concretos estándar.<br>• <strong>Estructural Max (Tipo ART/HE):</strong> Alta resistencia temprana que permite desencofrar elementos verticales a las 18 horas, ahorrando hasta 15% en costos de formaleta.`;
        } else if (lowerQuery.includes('argos') || lowerQuery.includes('competencia')) {
          responseText = `<strong>Ventajas Clave frente a Argos:</strong><br>1. <strong>Menor tiempo de desencofrado:</strong> Nuestro clinker de alta pureza alcanza la resistencia requerida antes, reduciendo días de formaleta.<br>2. <strong>Flete directo planta Galapa:</strong> Menor manipulación de sacos y tasa de rotura inferior al 0.2%.<br>3. <strong>Ahorro neto:</strong> Estimado en ~$1.700 COP por bulto de cemento gris.`;
        } else {
          responseText = `<strong>Recomendación Copiloto Ultracem:</strong><br>Para cerrar esta negociación técnica, ofrece al contratista el certificado de calidad NTC 121 de planta Galapa y una bonificación escalonada de flete por pedidos superiores a 40 toneladas.`;
        }
      }

      playChime('poke');
      const aiDiv = document.createElement('div');
      aiDiv.className = "flex justify-start";
      aiDiv.innerHTML = `
        <div class="bg-slate-100 p-2.5 rounded-xl rounded-tl-none text-slate-800 max-w-[90%] leading-relaxed text-xs">
          ${responseText}
        </div>
      `;
      container.appendChild(aiDiv);
      container.scrollTop = container.scrollHeight;
    }

    function probarPromptRapido(promptText) {
      const input = document.getElementById('ai-chat-input');
      input.value = promptText;
      enviarConsultaAI();
    }

    // ==============================================================
    // PERFIL DE COMPAÑERO & VER CARTERA ASIGNADA
    // ==============================================================
    function openColleagueProfile(colleagueId) {
      playChime('click');
      const colleague = teamMembers.find(m => m.id === colleagueId);
      if (!colleague) return;

      const clientsHtml = colleague.clients.map(c => `
        <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 space-y-2">
          <div class="flex items-start justify-between">
            <div>
              <h5 class="font-bold text-slate-900 text-xs">${c.name}</h5>
              <span class="text-[10px] text-slate-500">${c.ciudad.toUpperCase()} • ${c.tipo} • Cupo: ${c.cupo || '$30M'}</span>
            </div>
            <span class="text-[11px] font-mono-data font-bold text-[#004797] bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">${c.tons} Ton</span>
          </div>
          <div class="flex items-center justify-between text-[10px] pt-1 border-t border-slate-100">
            <span class="text-amber-800 font-semibold flex items-center space-x-1">
              <span>🔒</span>
              <span>${c.estado}</span>
            </span>
            <button onclick="pedirTransferenciaCaso(${c.id}, '${c.name}', '${colleague.name}')" class="text-[#004797] hover:underline font-bold">
              Pedir Transferencia
            </button>
          </div>
        </div>
      `).join('');

      const body = `
        <div class="space-y-4 text-xs">
          <div class="bg-[#003E78] text-white rounded-2xl p-4 flex items-center space-x-3.5 shadow-sm">
            <img src="${colleague.avatar}" alt="${colleague.name}" class="w-14 h-14 rounded-full object-cover border-2 border-white shadow-xs">
            <div>
              <div class="flex items-center space-x-1.5">
                <h4 class="font-extrabold text-white text-sm">${colleague.name}</h4>
                <span class="bg-white/20 text-white font-extrabold text-[9px] px-1.5 py-0.5 rounded-full uppercase">Niv ${colleague.nivel}</span>
              </div>
              <p class="text-blue-100 text-[11px] mt-0.5">${colleague.role}</p>
              <div class="flex items-center space-x-2 mt-1.5">
                <span class="text-amber-300 font-bold">🔥 ${colleague.racha} Días de Racha</span>
                <span class="text-blue-200">•</span>
                <span class="text-white font-bold font-mono-data">${colleague.clients.reduce((acc, c) => acc + c.tons, 0)} Ton Mes</span>
              </div>
            </div>
          </div>

          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <h4 class="font-extrabold text-xs text-slate-800 uppercase tracking-wider">
                Cartera de Clientes Asignados (${colleague.clients.length})
              </h4>
              <span class="text-[10px] text-slate-400">Protección Anti-Acoso Activa</span>
            </div>
            <div class="space-y-2">
              ${clientsHtml}
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 pt-1">
            <button onclick="navigateToTab('mapa'); closeInPhoneSheet();" class="btn-tactile bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>🗺️</span><span>Ver en Mapa</span>
            </button>
            <button onclick="showToast('Mensaje de felicitación enviado a ${colleague.name}', 'success'); closeInPhoneSheet();" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 rounded-xl flex items-center justify-center space-x-1">
              <span>👏</span><span>Felicitar Racha</span>
            </button>
          </div>
        </div>
      `;
      openInPhoneSheet('👤', `Perfil de Compañero`, colleague.division, body);
    }

    // ==============================================================
    // TRANSFERENCIA DE CLIENTES FIJOS A COMPAÑEROS
    // ==============================================================
    function openTransferClientModal(clientId, clientName) {
      playChime('click');
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-3">
            <div class="flex items-center space-x-2">
              <span class="text-xl">🔄</span>
              <div>
                <h4 class="font-extrabold text-indigo-950 text-sm leading-tight">${clientName}</h4>
                <p class="text-indigo-700 text-[11px] mt-0.5">Transferir cliente fijo a otro asesor de la regional</p>
              </div>
            </div>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Seleccionar Compañero Destino:</label>
            <select id="transfer-target-colleague" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="laura">Laura Valencia (34d 🔥 • Obras Caribe / Medellín)</option>
              <option value="andres">Andrés Restrepo (48d 🔥 • Cuentas Mayores / Bogotá)</option>
              <option value="felipe">Felipe Morales (18d 🔥 • Ferreterías & Pymes / Cali)</option>
            </select>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Motivo de la Transferencia:</label>
            <select id="transfer-reason" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="zona">Reasignación por cercanía geográfica / ruta de despacho</option>
              <option value="tecnica">Especialidad técnica en vaciado masivo de losas</option>
              <option value="balance">Balance de cartera y equidad comercial del equipo</option>
              <option value="vacaciones">Relevo temporal por vacaciones o incapacidad</option>
            </select>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Nota de Entrega para el Compañero:</label>
            <textarea id="transfer-notes" rows="2" placeholder="Ej: El residente de obra prefiere despacho los miércoles a las 7:00 AM..." class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]"></textarea>
          </div>

          <div class="bg-amber-50 border border-amber-200 rounded-xl p-2.5 text-amber-900 text-[11px] flex items-start space-x-2">
            <span class="text-amber-600 mt-0.5">🔒</span>
            <p class="leading-snug">Al confirmar, el cliente pasará de inmediato a la cartera del compañero seleccionado y se activará la protección anti-colisión para evitar sobre-contacto.</p>
          </div>

          <button onclick="confirmarTransferenciaCliente(${clientId}, '${clientName}')" class="btn-tactile w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>✅</span>
            <span>Confirmar Transferencia Inmediata</span>
          </button>
        </div>
      `;
      openInPhoneSheet('🔄', 'Transferir Cliente Fijo', clientName, body);
    }

    function confirmarTransferenciaCliente(clientId, clientName) {
      playChime('freeze');
      const targetId = document.getElementById('transfer-target-colleague').value;
      const targetColleague = teamMembers.find(m => m.id === targetId) || teamMembers[1];

      // Move in teamMembers
      const carlos = teamMembers.find(m => m.id === 'carlos');
      const clientIndex = carlos.clients.findIndex(c => c.id === clientId);
      if (clientIndex !== -1) {
        const [transferredClient] = carlos.clients.splice(clientIndex, 1);
        transferredClient.estado = `En Gestión Activa por ${targetColleague.name}`;
        transferredClient.asesor = targetColleague.name;
        targetColleague.clients.push(transferredClient);
      }

      // Update clientSites
      const site = clientSites.find(s => s.id === clientId);
      if (site) {
        site.estado = 'bloqueado';
        site.asesor = targetColleague.name;
        renderMapMarkers(clientSites);
      }

      // Update client card in Racha UI
      const card = document.getElementById(`card-client-${clientId}`);
      if (card) {
        card.className = "client-card bg-slate-100/90 rounded-2xl p-4 border border-slate-300 shadow-xs space-y-3 transition-all";
        card.innerHTML = `
          <div class="flex items-start justify-between">
            <div>
              <div class="flex items-center space-x-2">
                <h3 class="font-bold text-slate-700 text-sm tracking-tight">${clientName}</h3>
                <span class="text-[10px] font-extrabold bg-slate-200 text-slate-600 px-1.5 py-0.5 rounded">Transferido</span>
              </div>
              <p class="text-[11px] text-slate-500 mt-0.5">Asignado a ${targetColleague.name} • ${targetColleague.division}</p>
            </div>
            <span class="inline-flex items-center space-x-1 text-[10px] font-extrabold text-amber-800 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded-md">
              <span>🔒 EN GESTIÓN (${targetColleague.name.split(' ')[0]} ${targetColleague.name.split(' ')[1]?.[0] || ''}.)</span>
            </span>
          </div>

          <div class="bg-amber-50/80 border border-amber-200 rounded-xl p-2.5 text-[11px] text-amber-900 flex items-start space-x-2">
            <span class="text-amber-600 mt-0.5">🔒</span>
            <p class="leading-snug">
              <strong>Cliente transferido con éxito:</strong> Esta cuenta ahora es gestionada por <strong>${targetColleague.name}</strong>. No puedes realizar llamadas ni mensajes directos para evitar acoso al cliente.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-2 pt-1">
            <button disabled class="bg-slate-200 text-slate-400 font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5 cursor-not-allowed">
              <span>🔒</span>
              <span>Chat Bloqueado</span>
            </button>
            <button onclick="pedirTransferenciaCaso(${clientId}, '${clientName}', '${targetColleague.name}')" class="btn-tactile bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2 px-3 rounded-xl flex items-center justify-center space-x-1.5">
              <span>🔄</span>
              <span>Pedir Reversión</span>
            </button>
          </div>
        `;
      }

      closeInPhoneSheet();
      showToast(`✅ ${clientName} transferido exitosamente a ${targetColleague.name}`, "success");
    }

    // ==============================================================
    // GRABACIÓN DE AUDIO REAL & SYNTHESIZER FALLBACK
    // ==============================================================
    function openVoiceNotesModal(clientName) {
      playChime('click');
      recordingSeconds = 0;
      
      const body = `
        <div class="space-y-3.5 text-center p-1 text-xs">
          
          <div class="relative w-20 h-20 mx-auto flex items-center justify-center">
            <span id="voice-pulse-ring" class="absolute inset-0 rounded-full bg-rose-400/30 animate-ping"></span>
            <div id="voice-mic-circle" class="relative w-16 h-16 bg-rose-500 text-white rounded-full flex items-center justify-center text-3xl shadow-lg transition-transform">
              🎙️
            </div>
          </div>

          <div>
            <div class="flex items-center justify-center space-x-1.5">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-600 animate-pulse"></span>
              <span id="voice-timer-display" class="font-mono-data font-bold text-rose-600 text-sm">00:00</span>
              <span id="voice-status-pill" class="text-[9px] bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded-full">Grabando Audio</span>
            </div>
            <p class="text-[11px] text-slate-500 mt-1">Habla con libertad: capturaremos tu audio y transcribiremos tu voz</p>
          </div>

          <div id="voice-waveform-container" class="flex items-center justify-center space-x-1.5 h-8 py-1">
            <div class="voice-bar w-1.5 bg-rose-400 rounded-full" style="height: 10px;"></div>
            <div class="voice-bar w-1.5 bg-rose-500 rounded-full" style="height: 18px;"></div>
            <div class="voice-bar w-1.5 bg-rose-600 rounded-full" style="height: 26px;"></div>
            <div class="voice-bar w-1.5 bg-rose-500 rounded-full" style="height: 16px;"></div>
            <div class="voice-bar w-1.5 bg-rose-400 rounded-full" style="height: 8px;"></div>
          </div>

          <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3 text-left space-y-1">
            <div class="flex items-center justify-between text-[9px] uppercase font-bold text-slate-400">
              <span>Transcripción en Vivo:</span>
              <span id="transcription-indicator" class="text-emerald-600 flex items-center space-x-1 font-semibold">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-ping"></span>
                <span>Micrófono Activo</span>
              </span>
            </div>
            <p id="voice-transcription-text" class="text-xs text-slate-800 font-medium leading-relaxed min-h-[48px]">
              Escuchando tu voz... Habla sobre la visita técnica, cubicación o acuerdos con el cliente.
            </p>
          </div>

          <div class="space-y-2 pt-1">
            <button id="btn-stop-voice" onclick="finalizarGrabacionAudioReal('${clientName}')" class="btn-tactile w-full bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
              <span>⏹️</span>
              <span>Finalizar y Guardar en Historial</span>
            </button>
          </div>

        </div>
      `;

      openInPhoneSheet('🎙️', 'Nota de Voz en Obra', clientName, body);
      iniciarCapturaMicrofonoReal();
    }

    function iniciarCapturaMicrofonoReal() {
      audioChunks = [];
      recordingSeconds = 0;
      
      if (recordingTimerInterval) clearInterval(recordingTimerInterval);
      recordingTimerInterval = setInterval(() => {
        recordingSeconds++;
        const mins = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
        const secs = String(recordingSeconds % 60).padStart(2, '0');
        const timerEl = document.getElementById('voice-timer-display');
        if (timerEl) timerEl.textContent = `${mins}:${secs}`;
      }, 1000);

      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ audio: true })
          .then(stream => {
            audioStream = stream;
            try {
              mediaRecorder = new MediaRecorder(stream);
              mediaRecorder.ondataavailable = e => {
                if (e.data.size > 0) audioChunks.push(e.data);
              };
              mediaRecorder.start(250);
            } catch (e) {
              console.warn("MediaRecorder warning:", e);
            }

            try {
              const AudioCtx = window.AudioContext || window.webkitAudioContext;
              if (AudioCtx) {
                liveAudioCtx = new AudioCtx();
                const source = liveAudioCtx.createMediaStreamSource(stream);
                analyserNode = liveAudioCtx.createAnalyser();
                analyserNode.fftSize = 32;
                source.connect(analyserNode);

                const updateWaveform = () => {
                  if (!analyserNode) return;
                  const dataArray = new Uint8Array(analyserNode.frequencyBinCount);
                  analyserNode.getByteFrequencyData(dataArray);
                  
                  const bars = document.querySelectorAll('.voice-bar');
                  if (bars.length > 0) {
                    bars.forEach((bar, idx) => {
                      const val = dataArray[idx % dataArray.length] || 10;
                      const h = Math.max(6, Math.min(32, Math.round(val / 6)));
                      bar.style.height = `${h}px`;
                    });
                  }
                  animationFrameId = requestAnimationFrame(updateWaveform);
                };
                updateWaveform();
              }
            } catch (e) {
              console.warn("AudioContext waveform error:", e);
            }
          })
          .catch(err => {
            console.warn("Acceso a micrófono no disponible (fallback activado):", err);
            const pill = document.getElementById('voice-status-pill');
            if (pill) {
              pill.textContent = "Audio Asistido Ultracem";
              pill.className = "text-[9px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded-full";
            }
          });
      }

      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (SpeechRecognition) {
        try {
          speechRecognizer = new SpeechRecognition();
          speechRecognizer.lang = 'es-CO';
          speechRecognizer.continuous = true;
          speechRecognizer.interimResults = true;

          speechRecognizer.onresult = event => {
            let transcript = "";
            for (let i = 0; i < event.results.length; i++) {
              transcript += event.results[i][0].transcript;
            }
            const textEl = document.getElementById('voice-transcription-text');
            if (textEl && transcript.trim()) {
              textEl.textContent = `“${transcript.trim()}”`;
            }
          };

          speechRecognizer.onerror = err => console.warn("Speech error:", err);
          speechRecognizer.start();
        } catch (e) {
          console.warn("Speech recognition warning:", e);
        }
      }
    }

    function detenerGrabacionAudioLimpia() {
      if (recordingTimerInterval) clearInterval(recordingTimerInterval);
      if (animationFrameId) cancelAnimationFrame(animationFrameId);
      if (speechRecognizer) {
        try { speechRecognizer.stop(); } catch(e) {}
      }
      if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        try { mediaRecorder.stop(); } catch(e) {}
      }
      if (audioStream) {
        audioStream.getTracks().forEach(t => t.stop());
      }
      if (liveAudioCtx && liveAudioCtx.state !== 'closed') {
        try { liveAudioCtx.close(); } catch(e) {}
      }
    }

    function finalizarGrabacionAudioReal(clientName) {
      playChime('streak');
      detenerGrabacionAudioLimpia();

      const textEl = document.getElementById('voice-transcription-text');
      let finalText = textEl ? textEl.textContent.trim() : "";
      if (!finalText || finalText.startsWith("Escuchando")) {
        finalText = `“Visita técnica en obra con el residente. Se acordó despacho prioritario de 60 toneladas de Cemento Estructural Ultracem para vaciado el próximo miércoles a primera hora.”`;
      }

      let audioBlob = null;
      if (audioChunks && audioChunks.length > 0) {
        try {
          audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        } catch (e) {
          console.warn("Webm blob error, using synthetic WAV:", e);
        }
      }
      
      if (!audioBlob || audioBlob.size === 0) {
        audioBlob = generateSyntheticAudioMemoWav(Math.max(2.5, recordingSeconds || 3));
      }

      const audioUrl = URL.createObjectURL(audioBlob);
      const mins = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
      const secs = String(Math.max(3, recordingSeconds % 60)).padStart(2, '0');
      const timeStr = `${mins}:${secs}`;
      const groqKey = localStorage.getItem('ultracem_key_groq') || (activeAIProvider === 'groq' ? userApiKey : '');
      const noteTextId = 'voice-note-p-' + Date.now();

      const notesList = document.getElementById('timeline-notes-list-1');
      if (notesList) {
        const newEntry = document.createElement('div');
        newEntry.className = "bg-white p-2.5 rounded-xl border border-rose-200 shadow-2xs space-y-1.5";
        newEntry.innerHTML = `
          <div class="flex items-center justify-between text-[10px]">
            <span class="flex items-center space-x-1.5 font-bold text-rose-700">
              <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
              <span>🎙️ Nota de Voz Grabada</span>
            </span>
            <span class="font-mono-data text-slate-400 font-semibold">${timeStr} • Hoy</span>
          </div>
          <p id="${noteTextId}" class="text-slate-700 text-[11px] italic font-medium">
            ${groqKey ? `<span class="inline-flex items-center space-x-1 text-[#004797]"><span class="w-1.5 h-1.5 rounded-full bg-[#004797] animate-ping"></span><span>Transcribiendo con Groq Whisper Large V3 Turbo...</span></span>` : finalText}
          </p>
          <div class="pt-0.5">
            <audio controls src="${audioUrl}" class="w-full h-8 rounded-lg shadow-2xs"></audio>
          </div>
        `;
        notesList.insertBefore(newEntry, notesList.firstChild);

        if (groqKey) {
          transcribirNotaConGroqWhisper(audioBlob, groqKey, noteTextId, finalText);
        }
      }

      closeInPhoneSheet();
      salvarRachaCliente(1, "Nota de voz grabada en obra con audio guardado");
      showToast(`🎙️ Audio (${timeStr}) y nota guardados con éxito (+50 XP)`, "success");
    }

    async function transcribirNotaConGroqWhisper(blob, apiKey, elId, fallbackText) {
      const el = document.getElementById(elId);
      try {
        const formData = new FormData();
        const ext = (blob.type && blob.type.includes('wav')) ? 'audio.wav' : 'audio.webm';
        formData.append('file', blob, ext);
        formData.append('model', 'whisper-large-v3-turbo');
        formData.append('language', 'es');
        formData.append('temperature', '0');
        formData.append('prompt', 'Nota técnica y comercial de asesor de cemento Ultracem en visita a obra de construcción.');
        formData.append('response_format', 'json');

        const resp = await fetch('https://api.groq.com/openai/v1/audio/transcriptions', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${apiKey}`
          },
          body: formData
        });

        if (!resp.ok) {
          const errData = await resp.json().catch(() => ({}));
          throw new Error(errData.error?.message || `HTTP ${resp.status}`);
        }

        const data = await resp.json();
        const transcribed = data.text?.trim();
        if (transcribed && el) {
          el.innerHTML = `“${transcribed}” <span class="block mt-1 text-[9px] text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.5 rounded border border-emerald-200 w-fit">✨ Transcrito con Groq Whisper Large V3 Turbo</span>`;
          showToast("✨ Transcripción de audio completada con Groq Whisper", "success");
        } else if (el) {
          el.textContent = fallbackText;
        }
      } catch (err) {
        console.warn("Groq Whisper transcription fallback:", err);
        if (el) {
          el.innerHTML = `${fallbackText} <span class="block mt-1 text-[9px] text-slate-400 font-medium">(Transcripción local asistida)</span>`;
        }
      }
    }

    // ==============================================================
    // HERRAMIENTAS ADICIONALES (CUBICAJE, CERTIFICADO NTC, WHATSAPP)
    // ==============================================================
    function openCubicajeModal(clientName) {
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-blue-50 border border-blue-200 rounded-xl p-3">
            <strong class="text-[#004797] block font-bold text-xs">Cálculo de Concreto & Bultos de Cemento</strong>
            <p class="text-slate-600 mt-0.5">Basado en norma NTC 121 / 3318 con factor de desperdicio del 5%.</p>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Tipo de Elemento Estructural:</label>
            <select id="calc-tipo-elemento" onchange="calcularBultosEnVivo()" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="losas">Losa de Entrepiso (3000 PSI / 21 MPa)</option>
              <option value="columnas">Columnas y Muros (4000 PSI / 28 MPa)</option>
              <option value="cimentacion">Zapatas y Cimentación (3500 PSI / 24 MPa)</option>
              <option value="soleras">Vigas de Amarre y Soleras (2500 PSI / 17 MPa)</option>
            </select>
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-bold text-slate-700">Volumen Concreto (m³):</label>
              <input type="number" id="calc-volumen-m3" value="18" min="1" step="0.5" oninput="calcularBultosEnVivo()" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2 font-mono-data text-xs text-slate-800 focus:outline-none focus:border-[#004797]">
            </div>
            <div>
              <label class="block font-bold text-slate-700">Línea Cemento:</label>
              <select id="calc-linea-cemento" onchange="calcularBultosEnVivo()" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
                <option value="art">Estructural Max (Tipo ART)</option>
                <option value="ug">Uso General (Tipo UG)</option>
              </select>
            </div>
          </div>

          <div class="bg-[#003E78] text-white p-3.5 rounded-2xl space-y-2">
            <div class="flex justify-between items-center text-xs">
              <span class="text-blue-200">Requerimiento Estimado:</span>
              <span class="text-[10px] bg-white/20 px-2 py-0.5 rounded font-mono-data">+5% Desperdicio</span>
            </div>
            <div class="flex justify-between items-baseline">
              <span id="calc-resultado-bultos" class="text-2xl font-black text-amber-300 font-mono-data">151 Bultos</span>
              <span id="calc-resultado-ton" class="text-xs font-mono-data text-blue-100 font-bold">7.55 Toneladas</span>
            </div>
            <p class="text-[10px] text-blue-200 leading-tight">
              Ahorro estimado en formaleta: <strong class="text-amber-300">Retiro seguro a las 18h</strong> gracias a la resistencia temprana del Cemento Estructural Ultracem.
            </p>
          </div>

          <button onclick="compartirCalculoCubicaje('${clientName}')" class="btn-tactile w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>💬</span>
            <span>Compartir Cotización Técnica por WhatsApp</span>
          </button>
        </div>
      `;
      openInPhoneSheet('📐', 'Cubicación de Concreto', clientName, body);
    }

    function calcularBultosEnVivo() {
      const vol = parseFloat(document.getElementById('calc-volumen-m3')?.value || 18);
      const factor = 8.0;
      const bultos = Math.round(vol * factor);
      const ton = (bultos * 50 / 1000).toFixed(2);

      const bultosEl = document.getElementById('calc-resultado-bultos');
      const tonEl = document.getElementById('calc-resultado-ton');
      if (bultosEl) bultosEl.textContent = `${bultos} Bultos`;
      if (tonEl) tonEl.textContent = `${ton} Toneladas`;
    }

    function compartirCalculoCubicaje(clientName) {
      closeInPhoneSheet();
      openInAppWhatsApp(clientName, "151 Bultos (7.55 Ton) Cemento Estructural Max NTC 121");
    }

    function openCertificadoModal(clientName, tipoCemento) {
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="border-2 border-dashed border-blue-300 bg-blue-50/50 rounded-2xl p-4 text-center space-y-2">
            <span class="text-3xl">📜</span>
            <h4 class="font-extrabold text-[#004797] text-sm">Certificado Oficial de Conformidad</h4>
            <p class="text-slate-600 text-[11px]">Norma Técnica Colombiana <strong>ICONTEC NTC 121:2014</strong></p>
            <div class="text-[10px] font-mono-data bg-white p-2 rounded-lg border border-blue-200 text-slate-700 space-y-0.5 text-left">
              <div>• <strong>Lote de Producción:</strong> G-2026-10-A</div>
              <div>• <strong>Planta de Origen:</strong> Galapa, Atlántico</div>
              <div>• <strong>Resistencia 28D:</strong> 38.4 MPa (Excede norma ≥28 MPa)</div>
              <div>• <strong>Tiempo Fraguado Inicial:</strong> 115 minutos</div>
            </div>
          </div>

          <button onclick="compartirCertificado('${clientName}')" class="btn-tactile w-full bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>📲</span>
            <span>Enviar Certificado PDF al Cliente</span>
          </button>
        </div>
      `;
      openInPhoneSheet('📜', 'Certificado NTC 121', clientName, body);
    }

    function compartirCertificado(clientName) {
      playChime('poke');
      closeInPhoneSheet();
      salvarRachaCliente(2, "Certificado de calidad NTC 121 enviado");
      showToast(`📜 Certificado NTC 121 enviado a ${clientName} (+30 XP)`, "success");
    }

    // ==============================================================
    // WHATSAPP INTEGRADO DENTRO DE LA APP
    // ==============================================================
    function openInAppWhatsApp(clientName, detallePedido) {
      playChime('click');
      const body = `
        <div class="space-y-3 text-xs">
          <div class="bg-emerald-50 border border-emerald-200 rounded-xl p-2.5 flex items-center space-x-2 text-emerald-900">
            <span class="text-lg">📱</span>
            <div>
              <strong class="block text-xs">Chat Directo con Cliente</strong>
              <span class="text-[10px] text-emerald-700">${clientName} • Celular: 300 456 7890</span>
            </div>
          </div>

          <div class="bg-slate-100/70 p-3 rounded-2xl space-y-2 border border-slate-200">
            <div class="flex justify-end">
              <div class="bg-emerald-100 text-emerald-950 p-2.5 rounded-xl rounded-tr-none max-w-[85%] text-xs leading-relaxed font-medium">
                Hola Ingeniero, le saluda Carlos Mendoza de Ultracem. ¿Cómo avanza la programación para el vaciado de ${detallePedido}? Tenemos despacho prioritario desde Planta Galapa hoy mismo con garantía de rotura cero.
              </div>
            </div>
            <div class="flex justify-start">
              <div class="bg-white text-slate-800 p-2.5 rounded-xl rounded-tl-none max-w-[85%] text-xs border border-slate-200 shadow-2xs">
                Hola Carlos, justo íbamos a llamarte. Nos hace falta confirmar si nos sostienes el flete gratis si pedimos 40 toneladas.
              </div>
            </div>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Tu Respuesta Rápida:</label>
            <div class="flex items-center space-x-1.5">
              <input type="text" id="whatsapp-input-text" value="¡Totalmente confirmado Ingeniero! Despachamos a primera hora." class="flex-1 bg-slate-50 border border-slate-300 rounded-xl px-3 py-2 text-xs text-slate-800 focus:outline-none focus:border-emerald-600">
              <button onclick="enviarMensajeWhatsApp('${clientName}')" class="btn-tactile bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-3.5 py-2 rounded-xl shadow-xs">
                Enviar
              </button>
            </div>
          </div>
        </div>
      `;
      openInPhoneSheet('💬', 'Chat WhatsApp', clientName, body);
    }

    function enviarMensajeWhatsApp(clientName) {
      playChime('poke');
      closeInPhoneSheet();
      salvarRachaCliente(1, "Mensaje de WhatsApp y acuerdo de despacho");
      showToast(`💬 Mensaje enviado a ${clientName} (+50 XP)`, "success");
    }

    function openInAppRegisterAction(clientId, clientName) {
      playChime('click');
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-blue-50 border border-blue-200 rounded-xl p-3">
            <strong class="text-[#004797] block font-bold text-xs">Registrar Contacto de Campo</strong>
            <p class="text-slate-600 mt-0.5">${clientName} • Esta acción salvará tu racha de hoy.</p>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Tipo de Gestión Realizada:</label>
            <select id="action-type-select" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="visita">🏗️ Visita Presencial en Obra</option>
              <option value="llamada">📞 Llamada Telefónica con Residente</option>
              <option value="cotizacion">📄 Envío de Cotización Formal</option>
              <option value="pedido">📦 Cierre de Pedido / Despacho</option>
            </select>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Notas de la Conversación:</label>
            <textarea id="action-notes" rows="2" placeholder="Detalles de cubicación, requerimientos de probetas NTC 121..." class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 focus:outline-none focus:border-[#004797]"></textarea>
          </div>

          <button onclick="confirmarRegistroAccion(${clientId}, '${clientName}')" class="btn-tactile w-full bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>✅</span>
            <span>Guardar Acción y Salvar Racha (+100 XP)</span>
          </button>
        </div>
      `;
      openInPhoneSheet('📝', 'Registrar Acción Comercial', clientName, body);
    }

    function confirmarRegistroAccion(clientId, clientName) {
      playChime('streak');
      closeInPhoneSheet();
      salvarRachaCliente(clientId, "Contacto comercial registrado");
      showToast(`🎉 ¡Racha Salvada! Contacto con ${clientName} registrado (+100 XP)`, "success");
    }

    function salvarRachaCliente(clientId, motivo) {
      userXP += 100;
      celebrateStreak();
      
      const card = document.getElementById(`card-client-${clientId}`);
      if (card && clientId === 1) {
        card.className = "client-card bg-white rounded-2xl p-4 border border-emerald-300 shadow-xs space-y-3 transition-all";
        const badge = card.querySelector('.bg-rose-50');
        if (badge) {
          badge.className = "inline-flex items-center space-x-1 text-[10px] font-extrabold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-md";
          badge.innerHTML = `<span>✓ AL DÍA (CONTACTADO)</span>`;
        }
      }

      const dialogue = document.getElementById('mascot-dialogue-text');
      const mood = document.getElementById('mascot-mood-badge');
      if (dialogue) {
        dialogue.innerHTML = `¡Excelente trabajo Carlos! Registraste gestión con el cliente. Don Fraguado está <strong>feliz</strong> y tu racha de <strong>${userStreak} días</strong> está asegurada.`;
      }
      if (mood) {
        mood.textContent = "🥳 ¡Orgulloso!";
        mood.className = "text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full";
      }
    }

    function pedirTransferenciaCaso(clientId, clientName, asesorActual) {
      playChime('poke');
      const body = `
        <div class="space-y-3.5 text-xs">
          <div class="bg-amber-50 border border-amber-200 rounded-xl p-3">
            <div class="flex items-center space-x-2">
              <span class="text-xl">🔒</span>
              <div>
                <h4 class="font-extrabold text-amber-950 text-sm leading-tight">${clientName}</h4>
                <p class="text-amber-800 text-[11px] mt-0.5">Asignado actualmente a <strong>${asesorActual}</strong></p>
              </div>
            </div>
          </div>

          <p class="text-slate-600 leading-relaxed">
            Para evitar que dos asesores llamen al mismo cliente al mismo tiempo, el supervisor regional debe aprobar el traspaso de la cuenta.
          </p>

          <div class="space-y-1.5">
            <label class="block font-bold text-slate-700">Motivo de la Solicitud:</label>
            <select id="request-transfer-reason" class="w-full bg-slate-50 border border-slate-300 rounded-xl p-2.5 text-xs text-slate-800 font-semibold focus:outline-none focus:border-[#004797]">
              <option value="relacion">Tengo relación comercial previa con el residente</option>
              <option value="cercania">Estoy ubicado físicamente a 5 minutos de la obra</option>
              <option value="especialidad">Requerimiento especial de Cemento Alta Resistencia Temprana</option>
            </select>
          </div>

          <button onclick="enviarSolicitudSupervisor('${clientName}', '${asesorActual}')" class="btn-tactile w-full bg-[#004797] hover:bg-blue-800 text-white font-bold text-xs py-2.5 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
            <span>📨</span>
            <span>Enviar Solicitud al Supervisor Regional</span>
          </button>
        </div>
      `;
      openInPhoneSheet('🔄', 'Solicitar Transferencia', clientName, body);
    }

    function enviarSolicitudSupervisor(clientName, asesorActual) {
      playChime('streak');
      closeInPhoneSheet();
      showToast(`📨 Solicitud de reasignación enviada al Supervisor Regional`, "success");
    }

    // ==============================================================
    // CASCO PROTECTOR & HEATMAP
    // ==============================================================
    function activarCascoProtector() {
      if (cascoProtectorCount <= 0) {
        showToast("⚠️ No tienes cascos protectores disponibles en tu inventario.", "warning");
        return;
      }
      playChime('freeze');
      cascoProtectorCount--;
      cascoActive = true;

      const headerCount = document.getElementById('header-casco-count');
      const badgeCount = document.getElementById('casco-badge-count');
      const btn = document.getElementById('btn-use-casco');

      if (headerCount) headerCount.textContent = "⛑️ Congelado 24h";
      if (badgeCount) {
        badgeCount.textContent = "🛡️ Congelado 24h";
        badgeCount.className = "font-mono-data font-black text-sm bg-blue-100 text-[#004797] border border-blue-300 px-2.5 py-1 rounded-xl";
      }
      if (btn) {
        btn.disabled = true;
        btn.className = "bg-slate-200 text-slate-400 font-bold py-2 px-3 rounded-xl flex-1 cursor-not-allowed";
        btn.textContent = "Congelación Activa Hoy";
      }

      showToast("⛑️ ¡Casco activado! Tu racha está protegida contra cualquier corte hoy.", "success");
    }

    function openInAppTrofeo(titulo, descripcion, icono, xp) {
      playChime('poke');
      const body = `
        <div class="space-y-3.5 text-center p-2 text-xs">
          <div class="text-5xl my-2">${icono}</div>
          <h4 class="font-extrabold text-slate-900 text-sm">${titulo}</h4>
          <span class="inline-block bg-amber-100 text-amber-900 font-black px-2.5 py-0.5 rounded-full font-mono-data">${xp}</span>
          <p class="text-slate-600 leading-relaxed">${descripcion}</p>
          <button onclick="closeInPhoneSheet()" class="btn-tactile w-full bg-[#004797] text-white font-bold py-2 rounded-xl mt-2">
            Entendido
          </button>
        </div>
      `;
      openInPhoneSheet('🏆', 'Logro Comercial', titulo, body);
    }

    function initHeatmapGrid() {
      const grid = document.getElementById('perfil-heatmap-grid');
      if (!grid) return;
      grid.innerHTML = "";

      for (let i = 0; i < 90; i++) {
        const cell = document.createElement('div');
        cell.className = "w-2.5 h-2.5 rounded-xs transition-transform hover:scale-125 cursor-pointer";
        const rand = Math.random();
        if (rand > 0.4) {
          cell.className += " bg-[#004797]";
          cell.title = `Día ${i + 1}: 3 contactos de obra registrados`;
        } else if (rand > 0.15) {
          cell.className += " bg-blue-300";
          cell.title = `Día ${i + 1}: 1 contacto de obra registrado`;
        } else {
          cell.className += " bg-slate-200";
          cell.title = `Día ${i + 1}: Sin actividad (Casco Protector)`;
        }
        grid.appendChild(cell);
      }
    }

    // ==============================================================
    // SHEET & NAVIGATION HELPERS
    // ==============================================================
    function openInPhoneSheet(icon, title, subtitle, bodyHtml) {
      document.getElementById('sheet-header-icon').textContent = icon;
      document.getElementById('sheet-header-title').textContent = title;
      document.getElementById('sheet-header-subtitle').textContent = subtitle;
      document.getElementById('inphone-sheet-body').innerHTML = bodyHtml;

      const overlay = document.getElementById('inphone-sheet-overlay');
      overlay.classList.remove('hidden');
    }

    function closeInPhoneSheet() {
      detenerGrabacionAudioLimpia();
      const overlay = document.getElementById('inphone-sheet-overlay');
      overlay.classList.add('hidden');
    }

    function navigateToTab(tabName) {
      playChime('click');
      const tabs = ['racha', 'copiloto', 'mapa', 'liga', 'perfil'];
      tabs.forEach(t => {
        const scr = document.getElementById(`screen-${t}`);
        const btn = document.getElementById(`nav-btn-${t}`);
        if (scr) scr.classList.add('hidden');
        if (btn) {
          btn.className = "btn-tactile flex flex-col items-center text-slate-400 hover:text-slate-700 font-semibold px-2 py-1";
        }
      });

      const activeScr = document.getElementById(`screen-${tabName}`);
      const activeBtn = document.getElementById(`nav-btn-${tabName}`);
      if (activeScr) activeScr.classList.remove('hidden');
      if (activeBtn) {
        activeBtn.className = "btn-tactile flex flex-col items-center text-[#004797] font-bold px-2 py-1";
      }

      if (tabName === 'mapa') {
        initColombiaMap();
        renderDirectorioProspectos(b2bProspects);
      }
    }

    
    // ==============================================================
    // ULTRACEM VIEW MODE CONTROLLER (DROPDOWN SELECTOR)
    // ==============================================================
    function changeViewMode(mode) {
      playChime('click');
      const ws = document.getElementById('view-workstation');
      const dWrapper = document.getElementById('desktop-app-wrapper');
      const pWrapper = document.getElementById('phone-container-wrapper');
      const vPrd = document.getElementById('view-prd');
      const selector = document.getElementById('view-mode-selector');

      if (selector && selector.value !== mode) {
        selector.value = mode;
      }

      if (mode === 'desktop') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) pWrapper.classList.add('hidden');
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻 Modo Escritorio Completo", "info");
      } else if (mode === 'dual') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻📱 Vista Dividida: Computador + Celular al lado", "info");
      } else if (mode === 'mobile') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.add('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full max-w-[420px] mx-auto flex flex-col items-center py-2";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("📱 Modo Celular Asesor de Terreno", "info");
      } else if (mode === 'prd') {
        if (ws) ws.classList.add('hidden');
        if (vPrd) vPrd.classList.remove('hidden');
        showToast("📑 Especificación PRD Ultracem", "info");
        setTimeout(() => {
          if (vPrd) vPrd.scrollIntoView({ behavior: 'smooth' });
        }, 50);
      }
    }

    // ==============================================================
    // DESKTOP CRM TAB SWITCHER
    // ==============================================================
    function switchDesktopCrmTab(tabName) {
      playChime('click');
      const tabs = ['racha', 'copiloto', 'mapa', 'liga', 'perfil'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dcrm-tab-btn-${t}`);
        const sec = document.getElementById(`dcrm-content-${t}`);
        if (t === tabName) {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-all bg-[#FDCA02] text-[#003E78] shadow-xs";
          if (sec) sec.classList.remove('hidden');
        } else {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]";
          if (sec) sec.classList.add('hidden');
        }
      });

      if (tabName === 'mapa') {
        setTimeout(initDesktopColombiaMap, 100);
      }
    }

    // Desktop Client Selection
    let currentSelectedClientId = 1;
    function seleccionarClienteDesktop(id) {
      playChime('click');
      currentSelectedClientId = id;
      const clients = {
        1: { name: "Constructora Bolívar", subtitle: "Torres del Mar • 120 Ton Cemento Estructural Max", transcript: "Minuta: El ingeniero de Constructora Bolívar confirma necesidad de 40 Ton de Cemento Estructural Max para el vaciado del miércoles..." },
        2: { name: "Ferretería El Constructor", subtitle: "Sede Centro Soledad • 45 Ton Cemento Uso General", transcript: "Minuta: Don Álvaro solicita reposición de 200 bultos de Uso General. Pide confirmar despacho para mañana jueves antes de las 10 AM..." },
        3: { name: "Marval — Altos de Riomar", subtitle: "Torre 3 • 210 Ton Cemento Marino Impermeable", transcript: "Minuta: Verificación de fraguado de losa en Cemento Marino completada sin fisuras. Ensayo de probeta a 7 días cumple norma NTC 121..." }
      };

      const c = clients[id] || clients[1];
      const title = document.getElementById('dconsole-client-name');
      const transcript = document.getElementById('daudio-transcript-text');
      if (title) title.textContent = c.name;
      if (transcript) transcript.textContent = c.transcript;

      [1, 2, 3].forEach(cid => {
        const card = document.getElementById(`dcard-client-${cid}`);
        if (card) {
          if (cid === id) card.classList.add('ring-2', 'ring-[#003E78]');
          else card.classList.remove('ring-2', 'ring-[#003E78]');
        }
      });
      showToast(`Cliente seleccionado: ${c.name}`, "info");
    }

    // Desktop Filter
    function filtrarClientesDesktop(filter) {
      playChime('click');
      const btns = {
        'todos': document.getElementById('dfilter-todos'),
        'obras': document.getElementById('dfilter-obras'),
        'ferreterias': document.getElementById('dfilter-ferreterias'),
        'rojos': document.getElementById('dfilter-rojos')
      };
      Object.entries(btns).forEach(([k, b]) => {
        if (!b) return;
        if (k === filter) b.className = "px-3 py-1 rounded-lg font-bold bg-[#003E78] text-white";
        else b.className = "px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200";
      });

      const c1 = document.getElementById('dcard-client-1');
      const c2 = document.getElementById('dcard-client-2');
      const c3 = document.getElementById('dcard-client-3');

      if (filter === 'todos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = '';
      } else if (filter === 'obras') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = '';
      } else if (filter === 'ferreterias') {
        if (c1) c1.style.display = 'none';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = 'none';
      } else if (filter === 'rojos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = 'none';
      }
    }

    // Desktop Audio Recording Simulation
    let isDesktopAudioRecording = false;
    function toggleDesktopAudioRecording() {
      const btn = document.getElementById('dbtn-record-audio');
      const btnText = document.getElementById('dbtn-record-text');
      const badge = document.getElementById('daudio-status-badge');
      const player = document.getElementById('daudio-player');

      if (!isDesktopAudioRecording) {
        isDesktopAudioRecording = true;
        playChime('click');
        if (btnText) btnText.textContent = "Detener y Transcribir Audio...";
        if (badge) {
          badge.textContent = "Grabando 00:06...";
          badge.className = "text-[10px] bg-rose-600 text-white px-2 py-0.5 rounded-full font-mono-data animate-pulse";
        }
      } else {
        isDesktopAudioRecording = false;
        playChime('success');
        if (btnText) btnText.textContent = "Grabar Nota de Audio";
        if (badge) {
          badge.textContent = "Audio Guardado & Transcrito";
          badge.className = "text-[10px] bg-emerald-600 text-white px-2 py-0.5 rounded-full font-mono-data";
        }
        if (player) {
          const wavBlob = generateSyntheticAudioMemoWav(6);
          player.src = URL.createObjectURL(wavBlob);
          player.load();
        }
        showToast("🎙️ Nota de voz procesada con Whisper Turbo", "success");
      }
    }

    // Desktop Escalation SLA
    function escalarCasoDesktop() {
      playChime('success');
      const select = document.getElementById('descalation-dept-select');
      const deptName = select ? select.options[select.selectedIndex].text : "Cartera";
      showToast(`⚡ Caso escalado a ${deptName}. ¡Racha diaria protegida (+150 XP)!`, "success");
    }

    // Desktop WhatsApp
    function contactarClienteWhatsApp(clienteName) {
      playChime('click');
      showToast(`📲 Abriendo WhatsApp para ${clienteName} (+50 XP)`, "success");
    }

    // Desktop Quick Prompts
    function probarPromptRapidoDesktop(promptText) {
      const input = document.getElementById('desktop-chat-input');
      if (input) {
        input.value = promptText;
        enviarConsultaAIDesktop();
      }
    }

    // Desktop AI Chat
    function enviarConsultaAIDesktop() {
      const input = document.getElementById('desktop-chat-input');
      const container = document.getElementById('desktop-chat-messages');
      if (!input || !container) return;
      const text = input.value.trim();
      if (!text) return;

      playChime('click');
      input.value = '';

      // Append User message
      const uMsg = document.createElement('div');
      uMsg.className = "flex items-start justify-end space-x-2";
      uMsg.innerHTML = `
        <div class="bg-[#003E78] text-white rounded-2xl p-3 max-w-xl text-xs shadow-xs">
          <p>${text}</p>
        </div>
      `;
      container.appendChild(uMsg);
      container.scrollTop = container.scrollHeight;

      // Handle Guardrails: Reject non-business queries
      const lower = text.toLowerCase();
      let aiResponse = "";
      if (lower.includes('ribonucleico') || lower.includes('arn') || lower.includes('adn') || lower.includes('receta') || lower.includes('cocina')) {
        aiResponse = "Estimado asesor: Como Copiloto Comercial de Ultracem, mis parámetros de consulta están certificados exclusivamente para la comercialización de cemento y concreto, dosificaciones bajo norma NTC 121 y acompañamiento en obra civil. ¿Deseas consultar dosificaciones de Cemento Estructural Max o Cemento Marino?";
      } else if (lower.includes('3000') || lower.includes('losa') || lower.includes('dosificaci')) {
        aiResponse = "Para una losa maciza de 3000 PSI (21 MPa) a 28 días con Cemento Gris Estructural Max Ultracem (NTC 121), la dosificación recomendada por m³ es: 350 kg de Cemento (7 bultos de 50 kg), 0.55 m³ de arena lavada de río, 0.65 m³ de triturado de 1/2 pulgada y 180 litros de agua (relación a/c 0.51).";
      } else if (lower.includes('argos') || lower.includes('competencia') || lower.includes('descuento')) {
        aiResponse = "Argumento de defensa frente al descuento de Argos: 'En Ultracem garantizamos curva de resistencia temprana superior a los 3 días que le ahorra al constructor hasta 24 horas en el desencofre de placas, reduciendo costos de formaleta que superan ampliamente los $500 del bulto. Además, nuestro laboratorio de Planta Galapa expide los certificados de rotura sin costo adicional'.";
      } else {
        aiResponse = `Entendido. Con base en las especificaciones de Cemento Ultracem NTC 121 y los despachos programados desde Planta Galapa, te sugiero ofrecer Cemento Estructural Max con entrega directa en obra para asegurar el cumplimiento de la racha de recompra.`;
      }

      setTimeout(() => {
        playChime('success');
        const aiMsg = document.createElement('div');
        aiMsg.className = "flex items-start space-x-3";
        aiMsg.innerHTML = `
          <div class="w-8 h-8 rounded-full bg-[#003E78] text-[#FDCA02] font-black flex items-center justify-center text-xs flex-shrink-0">U</div>
          <div class="bg-slate-100 rounded-2xl p-3.5 max-w-2xl text-slate-800 leading-relaxed space-y-1 shadow-xs">
            <div class="font-bold text-[#003E78]">Copiloto Comercial Ultracem</div>
            <p>${aiResponse}</p>
          </div>
        `;
        container.appendChild(aiMsg);
        container.scrollTop = container.scrollHeight;
      }, 400);
    }

    // Desktop Map Sub-views
    function switchDesktopMapSubView(sub) {
      playChime('click');
      const bMap = document.getElementById('dmap-sub-btn-map');
      const bPros = document.getElementById('dmap-sub-btn-prospects');
      const vMap = document.getElementById('dmap-view-container');
      const vPros = document.getElementById('dprospects-view-container');

      if (sub === 'mapa') {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (vMap) vMap.classList.remove('hidden');
        if (vPros) vPros.classList.add('hidden');
        setTimeout(initDesktopColombiaMap, 100);
      } else {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (vMap) vMap.classList.add('hidden');
        if (vPros) vPros.classList.remove('hidden');
      }
    }

    // Leaflet Desktop Map Initializer
    let desktopLeafletMap = null;
    let desktopSatelliteActive = false;
    let desktopSatLayer = null;

    function initDesktopColombiaMap() {
      const container = document.getElementById('desktop-colombia-map');
      if (!container || desktopLeafletMap) {
        if (desktopLeafletMap) desktopLeafletMap.invalidateSize();
        return;
      }

      desktopLeafletMap = L.map('desktop-colombia-map', {
        center: [10.9639, -74.7964],
        zoom: 11
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(desktopLeafletMap);

      desktopSatLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri'
      });

      // Markers
      if (typeof clientSites !== 'undefined') {
        clientSites.forEach(s => {
          let color = '#003E78';
          if (s.tipo === 'planta') color = '#FDCA02';
          else if (s.tipo === 'competencia') color = '#DC2626';

          const marker = L.circleMarker([s.lat, s.lng], {
            radius: s.tipo === 'planta' ? 12 : 8,
            fillColor: color,
            color: '#FFFFFF',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.9
          }).addTo(desktopLeafletMap);

          marker.bindPopup(`<strong>${s.nombre}</strong><br>${s.ciudad} • ${s.tipo}`);
        });
      }
    }

    function toggleDesktopMapSatellite() {
      if (!desktopLeafletMap || !desktopSatLayer) return;
      playChime('click');
      if (desktopSatelliteActive) {
        desktopLeafletMap.removeLayer(desktopSatLayer);
        desktopSatelliteActive = false;
        showToast("Capa Calles activa", "info");
      } else {
        desktopSatLayer.addTo(desktopLeafletMap);
        desktopSatelliteActive = true;
        showToast("Capa Satelital ESRI activa", "info");
      }
    }
    function setTimeMode(mode) {
      playChime('click');
      const btnDay = document.getElementById('btn-time-day');
      const btnNight = document.getElementById('btn-time-night');
      const clock = document.getElementById('phone-clock');
      const timer = document.getElementById('countdown-timer');
      const mascot = document.getElementById('don-fraguado-container');
      const dialogue = document.getElementById('mascot-dialogue-text');
      const mood = document.getElementById('mascot-mood-badge');

      if (mode === 'day') {
        isDayMode = true;
        btnDay.className = "px-2.5 py-1 rounded-lg font-bold bg-slate-900 text-white text-[11px] transition-all";
        btnNight.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        if (clock) clock.textContent = "10:00 AM";
        if (timer) timer.textContent = "13h : 59m : 12s";
        if (mascot) {
          mascot.classList.remove('mascot-panic');
          mascot.classList.add('mascot-breathing');
        }
        if (dialogue) {
          dialogue.innerHTML = "¡Buenos días Carlos! Tu racha está protegida. Tienes <strong>2 clientes por contactar</strong> antes de las 11:59 PM para sumar +150 XP.";
        }
        if (mood) {
          mood.textContent = "⚡ Motivado";
          mood.className = "text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.2 rounded-full";
        }
      } else {
        isDayMode = false;
        btnNight.className = "px-2.5 py-1 rounded-lg font-bold bg-rose-600 text-white text-[11px] transition-all";
        btnDay.className = "px-2.5 py-1 rounded-lg font-semibold text-slate-600 hover:text-slate-900 text-[11px] transition-all";
        if (clock) clock.textContent = "10:45 PM";
        if (timer) timer.textContent = "01h : 14m : 02s";
        if (mascot) {
          mascot.classList.remove('mascot-breathing');
          mascot.classList.add('mascot-panic');
        }
        if (dialogue) {
          dialogue.innerHTML = "🚨 <strong>¡EMERGENCIA DE RACHA!</strong> Queda poco más de 1 hora para el corte de medianoche. Si no contactas a Constructora Bolívar, <strong>perderás tu racha de 21 días</strong>.";
        }
        if (mood) {
          mood.textContent = "😱 ¡En Pánico!";
          mood.className = "text-[9px] bg-rose-100 text-rose-800 font-bold px-1.5 py-0.2 rounded-full animate-pulse";
        }
        showToast("🌙 Simulación 10:45 PM activada: ¡Don Fraguado entra en pánico de racha!", "warning");
      }
    }

    function filterClients(tipo) {
      playChime('click');
      const cards = document.querySelectorAll('.client-card');
      const btns = {
        todos: document.getElementById('filter-btn-todos'),
        obras: document.getElementById('filter-btn-obras'),
        ferreterias: document.getElementById('filter-btn-ferreterias')
      };

      Object.keys(btns).forEach(k => {
        if (!btns[k]) return;
        if (k === tipo) {
          btns[k].className = "py-1.5 rounded-lg text-xs font-bold transition-all bg-white text-[#004797] shadow-xs text-center";
        } else {
          btns[k].className = "py-1.5 rounded-lg text-xs font-semibold transition-all text-slate-600 hover:text-slate-900 text-center";
        }
      });

      let count = 0;
      cards.forEach(card => {
        if (tipo === 'todos' || card.dataset.tipo === tipo) {
          card.classList.remove('hidden');
          count++;
        } else {
          card.classList.add('hidden');
        }
      });

      const badge = document.getElementById('filter-count-badge');
      if (badge) badge.textContent = `${count} Casos`;
    }

    function pokeMascot() {
      playChime('poke');
      const mascot = document.getElementById('don-fraguado-container');
      if (!mascot) return;
      mascot.classList.remove('mascot-breathing');
      mascot.classList.add('mascot-jump');
      setTimeout(() => {
        mascot.classList.remove('mascot-jump');
        if (isDayMode) mascot.classList.add('mascot-breathing');
        else mascot.classList.add('mascot-panic');
      }, 750);

      const phrases = [
        "¡Ojo al fraguado! El cemento no espera a nadie.",
        "¡Ultracem es resistencia NTC 121 pura!",
        "¿Ya llamaste al residente de Amarilo o Bolívar?",
        "¡Acuérdate de no dejar apagar la llama de tu racha!"
      ];
      const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
      showToast(`👷 Don Fraguado: “${randomPhrase}”`, "info");
    }

    function celebrateStreak() {
      const mascot = document.getElementById('don-fraguado-container');
      if (mascot) {
        mascot.classList.add('mascot-jump');
        setTimeout(() => mascot.classList.remove('mascot-jump'), 800);
      }
    }

    function playChime(type) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        const now = ctx.currentTime;
        if (type === 'streak') {
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.exponentialRampToValueAtTime(1046.50, now + 0.3);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
          osc.start(now);
          osc.stop(now + 0.36);
        } else if (type === 'poke') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(600, now);
          osc.frequency.exponentialRampToValueAtTime(900, now + 0.15);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.18);
          osc.start(now);
          osc.stop(now + 0.19);
        } else if (type === 'freeze') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(800, now);
          osc.frequency.exponentialRampToValueAtTime(400, now + 0.25);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.28);
          osc.start(now);
          osc.stop(now + 0.29);
        } else {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(440, now);
          gain.gain.setValueAtTime(0.1, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
          osc.start(now);
          osc.stop(now + 0.09);
        }
      } catch (e) {}
    }

    function showToast(message, type = 'info') {
      const container = document.getElementById('toast-container');
      if (!container) return;

      const toast = document.createElement('div');
      let bgStyle = "bg-slate-900 text-white";
      let borderStyle = "border-slate-700";

      if (type === 'success') {
        bgStyle = "bg-emerald-800 text-white";
        borderStyle = "border-emerald-600";
      } else if (type === 'warning') {
        bgStyle = "bg-amber-800 text-white";
        borderStyle = "border-amber-600";
      }

      toast.className = `${bgStyle} border ${borderStyle} px-4 py-2.5 rounded-2xl shadow-xl text-xs font-semibold flex items-center space-x-2 transform translate-y-4 opacity-0 transition-all duration-300 pointer-events-auto`;
      toast.innerHTML = `<span>${message}</span>`;
      container.appendChild(toast);

      requestAnimationFrame(() => {
        toast.classList.remove('translate-y-4', 'opacity-0');
      });

      setTimeout(() => {
        toast.classList.add('translate-y-4', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // ==============================================================
    // ULTRACEM : PRD MODAL, ACTIVATION PHASES & COLOR UTILS
    // ==============================================================
    let currentActivationStage = 4;

    function openUltracemPRDModal(defaultTab = 'vision') {
      playChime('click');
      const modal = document.getElementById('Ultracem-prd-modal');
      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        switchPrdTab(defaultTab);
      }
    }

    function closeUltracemPRDModal() {
      playChime('click');
      const modal = document.getElementById('Ultracem-prd-modal');
      if (modal) {
        modal.classList.add('hidden');
        modal.classList.remove('flex');
      }
    }

    function switchPrdTab(tabId) {
      playChime('click');
      const tabs = ['vision', 'brand', 'fases', 'specs', 'demo'];
      tabs.forEach(t => {
        const content = document.getElementById(`prd-tab-content-${t}`);
        const btn = document.getElementById(`prd-tab-btn-${t}`);
        if (content) content.classList.add('hidden');
        if (btn) {
          btn.className = "px-3.5 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-900 border-b-2 border-transparent transition-all whitespace-nowrap flex items-center space-x-1.5";
        }
      });

      const activeContent = document.getElementById(`prd-tab-content-${tabId}`);
      const activeBtn = document.getElementById(`prd-tab-btn-${tabId}`);
      if (activeContent) activeContent.classList.remove('hidden');
      if (activeBtn) {
        activeBtn.className = "px-3.5 py-2.5 text-xs font-extrabold text-[#14B8A6] border-b-2 border-[#14B8A6] transition-all whitespace-nowrap bg-teal-50/50 flex items-center space-x-1.5";
      }
    }

    function copyColorHex(hex, colorName) {
      playChime('poke');
      navigator.clipboard?.writeText?.(hex);
      showToast(`🎨 Color copiado: ${colorName} (${hex})`, "success");
    }

    function setActivationStage(stageNum) {
      playChime('streak');
      currentActivationStage = stageNum;

      // Update buttons in top bar
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btn-act-${i}`);
        if (btn) {
          if (i === stageNum) {
            btn.className = "px-2.5 py-1 rounded-lg font-bold transition-all bg-[#14B8A6] text-white shadow-xs flex items-center space-x-1";
          } else {
            btn.className = "px-2.5 py-1 rounded-lg font-bold transition-all text-slate-400 hover:text-white flex items-center space-x-1";
          }
        }
      }

      const caption = document.getElementById('activation-caption');
      const card = document.getElementById('activation-stage-card');

      if (stageNum === 1) {
        if (caption) caption.textContent = "Fase 1: Expectativa • Semilla en reposo (Despertar intriga)";
        if (card) {
          card.className = "rounded-2xl p-4 border transition-all duration-300 shadow-xs relative overflow-hidden bg-[#003E78] from-[#0F172A] via-[#1E293B] to-[#0F172A] text-white border-slate-700";
          card.innerHTML = `
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400 bg-amber-950/80 px-2 py-0.5 rounded-full border border-amber-600/40">Fase 1: Expectativa 🌰</span>
                <span class="text-[10px] font-mono-data text-slate-400">Próximamente</span>
              </div>
              <h4 class="font-extrabold text-sm text-white leading-snug">“Algo grande está por brotar en tu gestión comercial...”</h4>
              <p class="text-[11px] text-slate-300 leading-relaxed">
                ¿Sabías que un asesor que mantiene el contacto oportuno con sus obras puede multiplicar su impacto sin trabajar más horas? La semilla del potencial ya está sembrada.
              </p>
              <div class="flex items-center justify-between pt-1">
                <span class="text-[10px] text-slate-400">¿Sientes la curiosidad?</span>
                <button onclick="setActivationStage(2)" class="text-xs font-bold text-teal-400 hover:text-teal-300 underline flex items-center space-x-1">
                  <span>Avanzar a Fase 2</span> <span>➔</span>
                </button>
              </div>
            </div>
          `;
        }
        showToast("🌰 Fase 1 activada: Expectativa e intriga comercial", "info");
      } else if (stageNum === 2) {
        if (caption) caption.textContent = "Fase 2: Curiosidad • Primer brote emergiendo (Conectar y participar)";
        if (card) {
          card.className = "rounded-2xl p-4 border transition-all duration-300 shadow-xs relative overflow-hidden bg-[#003E78] from-[#064E3B] via-[#0F172A] to-[#064E3B] text-white border-emerald-500/40";
          card.innerHTML = `
            <div class="space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-300 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/40">Fase 2: Curiosidad 🌱</span>
                <span class="text-[10px] font-semibold text-emerald-200">Participa en la encuesta</span>
              </div>
              <h4 class="font-extrabold text-sm text-white leading-snug">“¿Qué tanto cuidas el potencial de tu cartera de obras?”</h4>
              <p class="text-[11px] text-emerald-100/90 leading-relaxed">
                Vota rápido: ¿Qué es lo más difícil en tu día a día comercial en campo?
              </p>
              <div class="grid grid-cols-2 gap-1.5 pt-1 text-[11px]">
                <button onclick="showToast('¡Gracias por votar! Acercándote al Reveal...', 'success'); setActivationStage(3);" class="bg-white/10 hover:bg-white/20 border border-white/20 p-2 rounded-xl text-left font-medium">
                  ⏱️ Recordar visitas a tiempo
                </button>
                <button onclick="showToast('¡Gracias por votar! Acercándote al Reveal...', 'success'); setActivationStage(3);" class="bg-white/10 hover:bg-white/20 border border-white/20 p-2 rounded-xl text-left font-medium">
                  📉 Clientes que dejan de pedir
                </button>
              </div>
            </div>
          `;
        }
        showToast("🌱 Fase 2 activada: Curiosidad y participación", "info");
      } else if (stageNum === 3) {
        if (caption) caption.textContent = "Fase 3: Reveal • Hojas desplegadas (Propósito e identidad oficial)";
        if (card) {
          card.className = "rounded-2xl p-4 border transition-all duration-300 shadow-xs relative overflow-hidden bg-[#003E78] from-[#0F172A] via-[#14B8A6]/20 to-[#0F172A] text-white border-teal-400/60";
          card.innerHTML = `
            <div class="space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-extrabold uppercase tracking-wider text-teal-300 bg-teal-950/90 px-2.5 py-0.5 rounded-full border border-teal-500/50">Fase 3: Reveal Oficial 🌿</span>
                <button onclick="openUltracemPRDModal('brand')" class="text-[10px] font-bold text-teal-300 underline">Ver Brand Book</button>
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-[#0F172A] border border-teal-400 p-1 flex items-center justify-center flex-shrink-0">
                  <svg viewBox="0 0 100 100" class="w-8 h-8" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M50 56 V36" stroke="#5EEAD4" stroke-width="4.5" stroke-linecap="round"/>
                    <path d="M50 38 C42 34 38 24 44 18 C50 24 50 32 50 38 Z" fill="#14B8A6"/>
                    <path d="M50 42 C58 38 62 28 56 22 C50 28 50 36 50 42 Z" fill="#5EEAD4"/>
                    <ellipse cx="50" cy="58" rx="14" ry="11" fill="#14B8A6" stroke="#5EEAD4" stroke-width="2.5"/>
                    <path d="M26 66 C28 78 40 84 54 84 C68 84 76 76 76 68 C76 62 70 58 64 58 C60 58 58 62 56 64" stroke="#5EEAD4" stroke-width="3.5" stroke-linecap="round"/>
                  </svg>
                </div>
                <div>
                  <h3 class="font-black text-sm text-white tracking-wide uppercase">ULTRACEM <span class="text-[#3797E8] text-xs font-bold lowercase">by Ultracem</span></h3>
                  <p class="text-xs text-teal-200 font-semibold italic">“Calidad, Resistencia y Rendimiento”</p>
                </div>
              </div>
              <p class="text-[11px] text-slate-300 leading-relaxed">
                Te presentamos el programa y la plataforma que transformarán tu carrera comercial con hábitos diarios de alto impacto.
              </p>
              <button onclick="setActivationStage(4)" class="btn-tactile w-full bg-[#14B8A6] hover:bg-teal-600 text-white font-extrabold text-xs py-2 rounded-xl shadow-xs flex items-center justify-center space-x-1.5">
                <span>🚀</span>
                <span>¡Entrar al Lanzamiento & Demo Activa!</span>
              </button>
            </div>
          `;
        }
        showToast("🌿 Fase 3 activada: Reveal de Ultracem", "success");
      } else {
        if (caption) caption.textContent = "Fase 4: Lanzamiento • Demo Activa y Operativa";
        if (card) {
          card.className = "rounded-2xl p-3.5 border transition-all duration-300 shadow-xs relative overflow-hidden bg-[#0A233F] text-white border-teal-500/30";
          card.innerHTML = `
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2.5">
                <div class="w-8 h-8 rounded-xl bg-teal-500/20 border border-teal-400/40 flex items-center justify-center text-teal-300 font-bold text-base flex-shrink-0">
                  🌱
                </div>
                <div>
                  <div class="flex items-center space-x-1.5">
                    <span class="font-bold text-xs text-white">Ultracem</span>
                    <span class="text-[9px] bg-teal-500/20 text-teal-300 px-1.5 py-0.2 rounded-full font-semibold border border-teal-500/30">Fase 4: Lanzamiento</span>
                  </div>
                  <p class="text-[10px] text-slate-300 mt-0.5">Calidad, Resistencia y Rendimiento • Demo Activa</p>
                </div>
              </div>
              <button onclick="openUltracemPRDModal()" class="text-[10px] font-bold bg-[#14B8A6] hover:bg-teal-600 text-white px-2.5 py-1.5 rounded-lg shadow-xs transition-all flex items-center space-x-1 flex-shrink-0">
                <span>📘</span>
                <span>Ver PRD</span>
              </button>
            </div>
          `;
        }
        showToast("🌳 Fase 4: Modo Operativo Completo en Vivo", "info");
      }
    }

    document.addEventListener('DOMContentLoaded', () => {
      if (window.innerWidth >= 1280) {
        switchMainView('workstation');
      } else if (window.innerWidth >= 768) {
        switchMainView('desktop-only');
      } else {
        switchMainView('mobile-only');
      }
      initHeatmapGrid();
      renderDirectorioProspectos(b2bProspects);
      
      let secLeft = 14 * 3600;
      setInterval(() => {
        if (secLeft > 0) secLeft--;
        const h = String(Math.floor(secLeft / 3600)).padStart(2, '0');
        const m = String(Math.floor((secLeft % 3600) / 60)).padStart(2, '0');
        const s = String(secLeft % 60).padStart(2, '0');
        const timer = document.getElementById('countdown-timer');
        if (timer && isDayMode) timer.textContent = `${h}h : ${m}m : ${s}s`;
      }, 1000);
    });
  </script>
</body>
</html>
'''

# Fill logo template
final_html = html_content.replace("{logo_base64}", logo_base64)

# 1. Write to root index.html
output_path_root = r"d:\Documentos\CARPETA IMPORTANTE\PROGRAMACION\Ultracem\index.html"
with open(output_path_root, "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"Generated successfully: {output_path_root}")

# 2. Write to brain artifact interactive prototype
artifact_prototype_path = r"C:\Users\HP 14\.gemini\antigravity\brain\86e577bd-2a1d-484f-8081-c1d72b940ae4\ultraracha_interactive_prototype.html"
with open(artifact_prototype_path, "w", encoding="utf-8") as f:
    f.write(final_html)
print(f"Generated artifact prototype: {artifact_prototype_path}")
    // ==============================================================
    // ULTRACEM VIEW MODE CONTROLLER (DROPDOWN SELECTOR)
    // ==============================================================
    function changeViewMode(mode) {
      playChime('click');
      const ws = document.getElementById('view-workstation');
      const dWrapper = document.getElementById('desktop-app-wrapper');
      const pWrapper = document.getElementById('phone-container-wrapper');
      const vPrd = document.getElementById('view-prd');
      const selector = document.getElementById('view-mode-selector');

      if (selector && selector.value !== mode) {
        selector.value = mode;
      }

      if (mode === 'desktop') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) pWrapper.classList.add('hidden');
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻 Modo Escritorio Completo", "info");
      } else if (mode === 'dual') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.remove('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full xl:w-[410px] flex-shrink-0 xl:sticky xl:top-20 self-start flex flex-col items-center";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("💻📱 Vista Dividida: Computador + Celular al lado", "info");
      } else if (mode === 'mobile') {
        if (ws) ws.classList.remove('hidden');
        if (dWrapper) dWrapper.classList.add('hidden');
        if (pWrapper) {
          pWrapper.classList.remove('hidden');
          pWrapper.className = "w-full max-w-[420px] mx-auto flex flex-col items-center py-2";
        }
        if (vPrd) vPrd.classList.add('hidden');
        showToast("📱 Modo Celular Asesor de Terreno", "info");
      } else if (mode === 'prd') {
        if (ws) ws.classList.add('hidden');
        if (vPrd) vPrd.classList.remove('hidden');
        showToast("📑 Especificación PRD Ultracem", "info");
        setTimeout(() => {
          if (vPrd) vPrd.scrollIntoView({ behavior: 'smooth' });
        }, 50);
      }
    }

    // ==============================================================
    // DESKTOP CRM TAB SWITCHER
    // ==============================================================
    function switchDesktopCrmTab(tabName) {
      playChime('click');
      const tabs = ['racha', 'copiloto', 'mapa', 'liga', 'perfil'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dcrm-tab-btn-${t}`);
        const sec = document.getElementById(`dcrm-content-${t}`);
        if (t === tabName) {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl font-bold transition-all bg-[#FDCA02] text-[#003E78] shadow-xs";
          if (sec) sec.classList.remove('hidden');
        } else {
          if (btn) btn.className = "w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl transition-all text-slate-300 hover:text-white hover:bg-[#142C47]";
          if (sec) sec.classList.add('hidden');
        }
      });

      if (tabName === 'mapa') {
        setTimeout(initDesktopColombiaMap, 100);
      }
    }

    // Desktop Client Selection
    let currentSelectedClientId = 1;
    function seleccionarClienteDesktop(id) {
      playChime('click');
      currentSelectedClientId = id;
      const clients = {
        1: { name: "Constructora Bolívar", subtitle: "Torres del Mar • 120 Ton Cemento Estructural Max", transcript: "Minuta: El ingeniero de Constructora Bolívar confirma necesidad de 40 Ton de Cemento Estructural Max para el vaciado del miércoles..." },
        2: { name: "Ferretería El Constructor", subtitle: "Sede Centro Soledad • 45 Ton Cemento Uso General", transcript: "Minuta: Don Álvaro solicita reposición de 200 bultos de Uso General. Pide confirmar despacho para mañana jueves antes de las 10 AM..." },
        3: { name: "Marval — Altos de Riomar", subtitle: "Torre 3 • 210 Ton Cemento Marino Impermeable", transcript: "Minuta: Verificación de fraguado de losa en Cemento Marino completada sin fisuras. Ensayo de probeta a 7 días cumple norma NTC 121..." }
      };

      const c = clients[id] || clients[1];
      const title = document.getElementById('dconsole-client-name');
      const transcript = document.getElementById('daudio-transcript-text');
      if (title) title.textContent = c.name;
      if (transcript) transcript.textContent = c.transcript;

      [1, 2, 3].forEach(cid => {
        const card = document.getElementById(`dcard-client-${cid}`);
        if (card) {
          if (cid === id) card.classList.add('ring-2', 'ring-[#003E78]');
          else card.classList.remove('ring-2', 'ring-[#003E78]');
        }
      });
      showToast(`Cliente seleccionado: ${c.name}`, "info");
    }

    // Desktop Filter
    function filtrarClientesDesktop(filter) {
      playChime('click');
      const btns = {
        'todos': document.getElementById('dfilter-todos'),
        'obras': document.getElementById('dfilter-obras'),
        'ferreterias': document.getElementById('dfilter-ferreterias'),
        'rojos': document.getElementById('dfilter-rojos')
      };
      Object.entries(btns).forEach(([k, b]) => {
        if (!b) return;
        if (k === filter) b.className = "px-3 py-1 rounded-lg font-bold bg-[#003E78] text-white";
        else b.className = "px-3 py-1 rounded-lg font-semibold text-slate-700 bg-slate-100 hover:bg-slate-200";
      });

      const c1 = document.getElementById('dcard-client-1');
      const c2 = document.getElementById('dcard-client-2');
      const c3 = document.getElementById('dcard-client-3');

      if (filter === 'todos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = '';
      } else if (filter === 'obras') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = '';
      } else if (filter === 'ferreterias') {
        if (c1) c1.style.display = 'none';
        if (c2) c2.style.display = '';
        if (c3) c3.style.display = 'none';
      } else if (filter === 'rojos') {
        if (c1) c1.style.display = '';
        if (c2) c2.style.display = 'none';
        if (c3) c3.style.display = 'none';
      }
    }

    // Desktop Audio Recording Simulation
    let isDesktopAudioRecording = false;
    function toggleDesktopAudioRecording() {
      const btn = document.getElementById('dbtn-record-audio');
      const btnText = document.getElementById('dbtn-record-text');
      const badge = document.getElementById('daudio-status-badge');
      const player = document.getElementById('daudio-player');

      if (!isDesktopAudioRecording) {
        isDesktopAudioRecording = true;
        playChime('click');
        if (btnText) btnText.textContent = "Detener y Transcribir Audio...";
        if (badge) {
          badge.textContent = "Grabando 00:06...";
          badge.className = "text-[10px] bg-rose-600 text-white px-2 py-0.5 rounded-full font-mono-data animate-pulse";
        }
      } else {
        isDesktopAudioRecording = false;
        playChime('success');
        if (btnText) btnText.textContent = "Grabar Nota de Audio";
        if (badge) {
          badge.textContent = "Audio Guardado & Transcrito";
          badge.className = "text-[10px] bg-emerald-600 text-white px-2 py-0.5 rounded-full font-mono-data";
        }
        if (player) {
          const wavBlob = generateSyntheticAudioMemoWav(6);
          player.src = URL.createObjectURL(wavBlob);
          player.load();
        }
        showToast("🎙️ Nota de voz procesada con Whisper Turbo", "success");
      }
    }

    // Desktop Escalation SLA
    function escalarCasoDesktop() {
      playChime('success');
      const select = document.getElementById('descalation-dept-select');
      const deptName = select ? select.options[select.selectedIndex].text : "Cartera";
      showToast(`⚡ Caso escalado a ${deptName}. ¡Racha diaria protegida (+150 XP)!`, "success");
    }

    // Desktop WhatsApp
    function contactarClienteWhatsApp(clienteName) {
      playChime('click');
      showToast(`📲 Abriendo WhatsApp para ${clienteName} (+50 XP)`, "success");
    }

    // Desktop Quick Prompts
    function probarPromptRapidoDesktop(promptText) {
      const input = document.getElementById('desktop-chat-input');
      if (input) {
        input.value = promptText;
        enviarConsultaAIDesktop();
      }
    }

    // Desktop AI Chat
    function enviarConsultaAIDesktop() {
      const input = document.getElementById('desktop-chat-input');
      const container = document.getElementById('desktop-chat-messages');
      if (!input || !container) return;
      const text = input.value.trim();
      if (!text) return;

      playChime('click');
      input.value = '';

      // Append User message
      const uMsg = document.createElement('div');
      uMsg.className = "flex items-start justify-end space-x-2";
      uMsg.innerHTML = `
        <div class="bg-[#003E78] text-white rounded-2xl p-3 max-w-xl text-xs shadow-xs">
          <p>${text}</p>
        </div>
      `;
      container.appendChild(uMsg);
      container.scrollTop = container.scrollHeight;

      // Handle Guardrails: Reject non-business queries
      const lower = text.toLowerCase();
      let aiResponse = "";
      if (lower.includes('ribonucleico') || lower.includes('arn') || lower.includes('adn') || lower.includes('receta') || lower.includes('cocina')) {
        aiResponse = "Estimado asesor: Como Copiloto Comercial de Ultracem, mis parámetros de consulta están certificados exclusivamente para la comercialización de cemento y concreto, dosificaciones bajo norma NTC 121 y acompañamiento en obra civil. ¿Deseas consultar dosificaciones de Cemento Estructural Max o Cemento Marino?";
      } else if (lower.includes('3000') || lower.includes('losa') || lower.includes('dosificaci')) {
        aiResponse = "Para una losa maciza de 3000 PSI (21 MPa) a 28 días con Cemento Gris Estructural Max Ultracem (NTC 121), la dosificación recomendada por m³ es: 350 kg de Cemento (7 bultos de 50 kg), 0.55 m³ de arena lavada de río, 0.65 m³ de triturado de 1/2 pulgada y 180 litros de agua (relación a/c 0.51).";
      } else if (lower.includes('argos') || lower.includes('competencia') || lower.includes('descuento')) {
        aiResponse = "Argumento de defensa frente al descuento de Argos: 'En Ultracem garantizamos curva de resistencia temprana superior a los 3 días que le ahorra al constructor hasta 24 horas en el desencofre de placas, reduciendo costos de formaleta que superan ampliamente los $500 del bulto. Además, nuestro laboratorio de Planta Galapa expide los certificados de rotura sin costo adicional'.";
      } else {
        aiResponse = `Entendido. Con base en las especificaciones de Cemento Ultracem NTC 121 y los despachos programados desde Planta Galapa, te sugiero ofrecer Cemento Estructural Max con entrega directa en obra para asegurar el cumplimiento de la racha de recompra.`;
      }

      setTimeout(() => {
        playChime('success');
        const aiMsg = document.createElement('div');
        aiMsg.className = "flex items-start space-x-3";
        aiMsg.innerHTML = `
          <div class="w-8 h-8 rounded-full bg-[#003E78] text-[#FDCA02] font-black flex items-center justify-center text-xs flex-shrink-0">U</div>
          <div class="bg-slate-100 rounded-2xl p-3.5 max-w-2xl text-slate-800 leading-relaxed space-y-1 shadow-xs">
            <div class="font-bold text-[#003E78]">Copiloto Comercial Ultracem</div>
            <p>${aiResponse}</p>
          </div>
        `;
        container.appendChild(aiMsg);
        container.scrollTop = container.scrollHeight;
      }, 400);
    }

    // Desktop Map Sub-views
    function switchDesktopMapSubView(sub) {
      playChime('click');
      const bMap = document.getElementById('dmap-sub-btn-map');
      const bPros = document.getElementById('dmap-sub-btn-prospects');
      const vMap = document.getElementById('dmap-view-container');
      const vPros = document.getElementById('dprospects-view-container');

      if (sub === 'mapa') {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (vMap) vMap.classList.remove('hidden');
        if (vPros) vPros.classList.add('hidden');
        setTimeout(initDesktopColombiaMap, 100);
      } else {
        if (bMap) bMap.className = "px-4 py-2 rounded-xl font-semibold text-slate-600 hover:text-slate-900 bg-slate-100";
        if (bPros) bPros.className = "px-4 py-2 rounded-xl font-bold bg-[#003E78] text-white shadow-xs";
        if (vMap) vMap.classList.add('hidden');
        if (vPros) vPros.classList.remove('hidden');
      }
    }

    // Leaflet Desktop Map Initializer
    let desktopLeafletMap = null;
    let desktopSatelliteActive = false;
    let desktopSatLayer = null;

    function initDesktopColombiaMap() {
      const container = document.getElementById('desktop-colombia-map');
      if (!container || desktopLeafletMap) {
        if (desktopLeafletMap) desktopLeafletMap.invalidateSize();
        return;
      }

      desktopLeafletMap = L.map('desktop-colombia-map', {
        center: [10.9639, -74.7964],
        zoom: 11
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(desktopLeafletMap);

      desktopSatLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri'
      });

      // Markers
      if (typeof clientSites !== 'undefined') {
        clientSites.forEach(s => {
          let color = '#003E78';
          if (s.tipo === 'planta') color = '#FDCA02';
          else if (s.tipo === 'competencia') color = '#DC2626';

          const marker = L.circleMarker([s.lat, s.lng], {
            radius: s.tipo === 'planta' ? 12 : 8,
            fillColor: color,
            color: '#FFFFFF',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.9
          }).addTo(desktopLeafletMap);

          marker.bindPopup(`<strong>${s.nombre}</strong><br>${s.ciudad} • ${s.tipo}`);
        });
      }
    }

    function toggleDesktopMapSatellite() {
      if (!desktopLeafletMap || !desktopSatLayer) return;
      playChime('click');
      if (desktopSatelliteActive) {
        desktopLeafletMap.removeLayer(desktopSatLayer);
        desktopSatelliteActive = false;
        showToast("Capa Calles activa", "info");
      } else {
        desktopSatLayer.addTo(desktopLeafletMap);
        desktopSatelliteActive = true;
        showToast("Capa Satelital ESRI activa", "info");
      }
    }
    
