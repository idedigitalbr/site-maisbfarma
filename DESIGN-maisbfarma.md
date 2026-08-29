---
version: 1.0.0
name: maisbfarma-design-system
description: Sistema de design oficial, moderno e acolhedor para a rede de farmácias +B FARMA (Grupo Mais Barato). Ancorado em uma base limpa (#FFFFFF), tipografia geométrica Lufga, contraste grafite (#32343D), cinza neutro complementar (#E7E7E7) e a energia da cor de marca Vermelho +B (#E92125) para ações, CTAs e momentos estratégicos de destaque institucional.

colors:
  primary: "#E92125"
  primary-hover: "#C8161A"
  primary-active: "#A81014"
  primary-disabled: "#FBD1D3"
  primary-light: "#FDE8E9"
  primary-error: "#C8161A"
  primary-error-bg: "#FDE8E9"
  
  # Neutros e Textos
  ink: "#32343D"
  body: "#555866"
  muted: "#7B7E8C"
  muted-light: "#A0A3B1"
  
  # Superfícies e Linhas
  canvas: "#FFFFFF"
  surface-soft: "#F8F9FA"
  surface-card: "#FFFFFF"
  surface-strong: "#F0F2F5"
  surface-dark: "#1C1D22"
  surface-dark-card: "#25272E"
  
  hairline: "#E7E7E7"
  hairline-soft: "#F0F2F5"
  border-strong: "#D4D5DC"
  
  # Semânticos
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#10B981"
  success-bg: "#ECFDF5"
  warning: "#F59E0B"
  warning-bg: "#FFFBEB"
  star-rating: "#F59E0B"
  scrim: "rgba(28, 29, 34, 0.6)"

typography:
  fontFamily: "'Lufga', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
  
  weights:
    regular: 400
    medium: 500
    medium-italic: 500
    semibold: 600
    bold: 700
    
  scale:
    display-2xl:
      fontSize: "48px"
      fontWeight: 700
      lineHeight: "1.15"
      letterSpacing: "-0.02em"
    display-xl:
      fontSize: "40px"
      fontWeight: 700
      lineHeight: "1.2"
      letterSpacing: "-0.02em"
    display-lg:
      fontSize: "32px"
      fontWeight: 700
      lineHeight: "1.25"
      letterSpacing: "-0.015em"
    display-md:
      fontSize: "28px"
      fontWeight: 600
      lineHeight: "1.3"
      letterSpacing: "-0.01em"
    title-xl:
      fontSize: "24px"
      fontWeight: 600
      lineHeight: "1.35"
      letterSpacing: "-0.01em"
    title-lg:
      fontSize: "20px"
      fontWeight: 600
      lineHeight: "1.4"
      letterSpacing: "0"
    title-md:
      fontSize: "18px"
      fontWeight: 600
      lineHeight: "1.4"
      letterSpacing: "0"
    title-sm:
      fontSize: "16px"
      fontWeight: 600
      lineHeight: "1.45"
      letterSpacing: "0"
    body-lg:
      fontSize: "18px"
      fontWeight: 400
      lineHeight: "1.6"
      letterSpacing: "0"
    body-md:
      fontSize: "16px"
      fontWeight: 400
      lineHeight: "1.5"
      letterSpacing: "0"
    body-sm:
      fontSize: "14px"
      fontWeight: 400
      lineHeight: "1.5"
      letterSpacing: "0"
    caption:
      fontSize: "13px"
      fontWeight: 500
      lineHeight: "1.4"
      letterSpacing: "0.01em"
    micro:
      fontSize: "11px"
      fontWeight: 600
      lineHeight: "1.3"
      letterSpacing: "0.05em"
      textTransform: "uppercase"
    button-lg:
      fontSize: "16px"
      fontWeight: 600
      lineHeight: "1.25"
      letterSpacing: "0"
    button-md:
      fontSize: "14px"
      fontWeight: 600
      lineHeight: "1.25"
      letterSpacing: "0"
    button-sm:
      fontSize: "13px"
      fontWeight: 600
      lineHeight: "1.2"
      letterSpacing: "0"

rounded:
  none: "0px"
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  2xl: "32px"
  full: "9999px"

spacing:
  xxs: "2px"
  xs: "4px"
  sm: "8px"
  md: "12px"
  base: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "64px"
  section: "80px"
  section-lg: "96px"

shadows:
  xs: "0 1px 2px 0 rgba(50, 52, 61, 0.04)"
  sm: "0 2px 8px 0 rgba(50, 52, 61, 0.06), 0 0 1px 0 rgba(50, 52, 61, 0.1)"
  card: "0 4px 16px -2px rgba(50, 52, 61, 0.06), 0 0 1px 0 rgba(50, 52, 61, 0.12)"
  floating: "0 20px 35px -10px rgba(50, 52, 61, 0.08), 0 1px 3px 0 rgba(50, 52, 61, 0.04)"
  elevated: "0 25px 50px -12px rgba(50, 52, 61, 0.14)"

container:
  maxWidth: "1280px"
  padding: "24px"

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: "14px 24px"
    height: "48px"
    transition: "all 0.2s cubic-bezier(0.4, 0, 0.2, 1)"
    
  button-secondary:
    backgroundColor: "{colors.canvas}"
    hoverBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: "13px 23px"
    height: "48px"
    
  button-tertiary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    hoverTextColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: "8px 12px"
    
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    
  top-header-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    height: "36px"
    
  navbar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "76px"
    borderBottom: "1px solid {colors.hairline}"
    
  card-feature:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    shadow: "{shadows.sm}"
    
  card-branch:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg}"
    shadow: "{shadows.card}"
    
  accordion-faq:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
    
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    subBarBackgroundColor: "{colors.primary}"
---

# Design System +B FARMA

Documentação oficial da linguagem visual e padrões de engenharia front-end para o site institucional da **+B FARMA**.

---

## 1. Visão Geral & Filosofia

O site da **+B FARMA** combina a credibilidade da área farmacêutica e médica com o acolhimento, agilidade e economia do Grupo Mais Barato.

### Princípios Visuais:
1. **Clareza e Confiança:** Canvas predominantemente branco (`#FFFFFF`) e tipografia em grafite escuro (`#32343D`), transmitindo legibilidade e sobriedade.
2. **Energia e Ação Direcionada:** O vermelho oficial da marca (`#E92125`) é reservado para ações primárias (CTAs), logotipos, selos e elementos que demandam conversão e destaque.
3. **Harmonia Estrutural:** Linhas neutras e divisores em cinza complementar (`#E7E7E7`), raios suaves (`8px` a `24px`) e sombras refinadas sem peso excessivo.
4. **Tipografia Lufga:** Tipografia geométrica contemporânea, equilibrando personalidade com legibilidade cirúrgica.

---

## 2. Paleta de Cores Oficial

### Cor Primária (Marca e Conversão)
- **Vermelho +B Principal:** `#E92125` — Utilizado no botão primário, faixa superior, badges estratégicos e logo.
- **Vermelho Hover:** `#C8161A` — Estado hover em botões e links primários.
- **Vermelho Active / Pressed:** `#A81014` — Estado ativo de clique.
- **Vermelho Soft / Fundo Leve:** `#FDE8E9` — Fundos de ícones e destaques sutis.
- **Vermelho Desabilitado:** `#FBD1D3` — Botões e controles inativos.

### Cores Neutras e Textos
- **Grafite Principal (Ink):** `#32343D` — Headings, títulos de seção, texto de alto contraste e menus.
- **Cinza Texto (Body):** `#555866` — Parágrafos, descrições e legendas explicativas.
- **Cinza Muted (Apoio):** `#7B7E8C` — Metadados, horários, categorias e ícones secundários.
- **Cinza Claro Neutro (Hairline):** `#E7E7E7` — Bordas de cards, divisores, inputs e contornos.
- **Cinza Soft Surface:** `#F8F9FA` — Alternância de seções e fundos de cards leves.

### Fundo Escuro (Footer & Prova Social)
- **Grafite Noturno (Dark Surface):** `#1C1D22` — Fundo do rodapé e bloco de prova social.
- **Card Dark Surface:** `#25272E` — Cards de depoimentos sobre fundo escuro.

---

## 3. Tipografia Oficial: Lufga

Toda a interface deve utilizar exclusivamente a família tipográfica **Lufga** com os seguintes pesos semânticos:

| Peso | Nome no Sistema | Uso Principal |
| :--- | :--- | :--- |
| **400** | Lufga Regular | Corpo de texto, parágrafos, inputs, FAQs |
| **500** | Lufga Medium | Subtítulos, labels de formulário, microcopy |
| **500 (italic)** | Lufga Medium Italic | Citações, depoimentos de clientes e observações |
| **600** | Lufga Semibold | Títulos de cards, botões, links de menu, badges |
| **700** | Lufga Bold | Títulos principais (H1, H2), números de indicadores, métricas |

**Pilha e Declaração @font-face Oficial:**
```css
@font-face {
  font-family: 'Lufga';
  src: url('assets/fonts/Lufga-Regular.otf') format('opentype'),
       local('Lufga Regular'), local('Lufga-Regular');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'Lufga';
  src: url('assets/fonts/Lufga-Medium.otf') format('opentype'),
       local('Lufga Medium'), local('Lufga-Medium');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'Lufga';
  src: url('assets/fonts/Lufga-MediumItalic.otf') format('opentype'),
       local('Lufga Medium Italic'), local('Lufga-MediumItalic');
  font-weight: 500;
  font-style: italic;
  font-display: swap;
}
@font-face {
  font-family: 'Lufga';
  src: url('assets/fonts/Lufga-SemiBold.otf') format('opentype'),
       local('Lufga SemiBold'), local('Lufga-SemiBold');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'Lufga';
  src: url('assets/fonts/Lufga-Bold.otf') format('opentype'),
       local('Lufga Bold'), local('Lufga-Bold');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

font-family: 'Lufga', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
```

---

## 4. Escala de Espaçamento e Grids

- **Base do Grid:** Múltiplos de 4px / 8px.
- **Container Máximo:** `1280px` centralizado (`margin: 0 auto; width: 90%; max-width: 1280px;`).
- **Padding Vertical de Seções:**
  - Seções Standard: `80px` (desktop) / `48px` (mobile).
  - Seções Compactas (Indicadores/Benefícios): `48px` (desktop) / `32px` (mobile).
- **Gutter entre Colunas:** `24px` a `32px` em desktop, `16px` em mobile.

---

## 5. Raios de Borda (Border Radius)

- **`8px` (sm):** Inputs, selects, tags compactas.
- **`12px` (md):** Botões principais, acordeões de FAQ, banners médios.
- **`16px` (lg):** Cards de benefícios, cards de depoimentos, popovers.
- **`24px` (xl):** Containers de destaque (Sobre, Clube +B, Reputação).
- **`32px` (2xl):** Arredondamento inferior do Hero e superior do Footer.
- **`9999px` (full):** Pills, avatares circulares, badges e orbs de ação.

---

## 7. Iconografia Oficial: Lucide Icons (Obrigatório)

> [!IMPORTANT]
> **REGRA DE OURO DE ICONOGRAFIA:** Toda e qualquer representação visual de ícone no projeto +B FARMA DEVE utilizar exclusivamente o pacote oficial **[Lucide Icons](https://lucide.dev/icons/)**. É expressamente proibido misturar pacotes de ícones divergentes, ícones com preenchimentos heterogêneos ou emojis em componentes funcionais de interface.

### Padrão Técnico de SVG dos Lucide Icons:
- **ViewBox:** `0 0 24 24`
- **Fill:** `none`
- **Stroke:** `currentColor`
- **Stroke Width:** `2` (Padrão) ou `1.75` (para ícones em títulos grandes)
- **Stroke Linecap / Linejoin:** `round`
- **Escala de Tamanhos:**
  - `14px` / `16px` (`w-3.5 h-3.5` / `w-4 h-4`) — Metadados, badges e chips.
  - `20px` (`w-5 h-5`) — Botões, inputs e navegação.
  - `24px` (`w-6 h-6`) — Cards de benefícios e títulos de seções.
  - `32px` / `40px` (`w-8 h-8` / `w-10 h-10`) — Destaques heroicos.

### Mapeamento Canônico de Ícones Lucide no Projeto:
| Componente / Função | Nome do Ícone Lucide | Código / Visualização |
| :--- | :--- | :--- |
| **Entrega Expressa** | `truck` / `package` | Entrega rápida em domicílio |
| **Compre & Retire** | `shopping-bag` / `store` | Retirada na loja física |
| **Atenção Farmacêutica** | `cross` / `stethoscope` / `heart-pulse` | Orientação e saúde |
| **Clube +B** | `tag` / `sparkles` / `badge-percent` | Descontos e promoções |
| **Atendimento Direto** | `message-circle` / `phone` | Canal WhatsApp / Telefone |
| **Localização / Filiais** | `map-pin` | Endereços Plaza e Tapanã |
| **Horário de Funcionamento** | `clock` | Horários de atendimento |
| **Busca Global** | `search` | Barra de pesquisa |
| **Avaliação / Estrelas** | `star` | Prova social Google |
| **Checagens & Vantagens** | `check` / `check-circle-2` | Listas de benefícios |
| **Navegação & Carrossel** | `chevron-left` / `chevron-right` / `chevron-down` | Slides e Accordions |

---

## 8. Biblioteca de Componentes Oficiais

### 6.1 Botões
- **Primary:** Fundo `#E92125`, texto `#FFFFFF`, Lufga Semibold (600), raio `12px`, padding `14px 24px`, hover `#C8161A`.
- **Secondary:** Fundo `#FFFFFF`, borda `1px solid #D4D5DC`, texto `#32343D`, hover `#F8F9FA`.
- **Tertiary:** Fundo transparente, texto `#32343D`, hover `#E92125`.

### 6.2 Header & Navegação
- **Faixa Superior:** Altura `36px`, fundo `#E92125`, texto `#FFFFFF`, redes sociais à esquerda e links institucionais / Clube +B à direita.
- **Barra de Navegação Principal:** Altura `76px`, fundo `#FFFFFF`, borda inferior `1px solid #E7E7E7`, logo oficial horizontal centralizada/à esquerda, links com hover suave em `#E92125` e botão de ação "Minha Conta / Atendimento".

### 6.3 Hero Section
- Fundo em degradê suave (`#F8F9FA` a `#F0F2F5`), raio inferior de `32px`, headline assertiva em Lufga Bold, badges com ponto vermelho `#E92125` e carrossel de fotos reais das unidades.

### 6.4 Cards de Benefícios
- Container flutuante sobreposto (`margin-top: -48px`), fundo `#FFFFFF`, borda `1px solid #E7E7E7`, sombra `shadow-floating`, 5 colunas com ícones destacados em `#E92125` e `#32343D`.

### 6.5 Filiais e Reputação Google
- Prova social com estrelas em `#F59E0B` (4.9 / 5.0), selos verificados e cards dedicados das unidades **Plaza** e **Tapanã** com fotos reais, endereço e status de funcionamento.

### 6.6 FAQ (Perguntas Frequentes)
- Acordeões interativos com fundo `#FFFFFF`, borda `1px solid #E7E7E7`, abertura suave e suporte a teclado/acessibilidade.

### 6.7 Footer
- Fundo escuro `#1C1D22`, tipografia clara, logo branca em contraste e sub-faixa inferior fina em `#E92125` com direitos autorais e links legais.

---

## 7. Regras de Engenharia & Acessibilidade

1. **Contraste Mínimo WCAG AA:** Todo texto corrido sobre fundo claro deve possuir contraste mínimo de 4.5:1 (utilizando `#32343D` e `#555866`).
2. **Semântica HTML5:** Uso rigoroso de `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<button>` e `<a>`.
3. **Responsividade Multi-Dispositivo:** Testado em `320px`, `375px`, `768px`, `1024px`, `1280px` e `1440px+`.
4. **Proibição de Estilos Legados:** É terminantemente proibido o uso de `#ff385c`, `#e00b41`, `Airbnb Cereal`, `Circular` ou variáveis legadas. Toda nova tela deve consultar este documento como fonte única de verdade visual.
