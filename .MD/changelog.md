# Changelog

## 2026-08-31 — Reformulação da Seção de Reputação Google & Cards das Filiais (Alinhamento com Anexo 2 & Anexo 3)

### Front-End & Layout da Seção de Reputação (#filiais)
- **Faixa Branca Full-Width Encostada nas Laterais:** A cápsula/faixa branca de reputação do Google agora ocupa 100% da largura da tela (`w-full px-0`) sem gaps escuros laterais, mantendo altura compacta e esticada na horizontal (`py-4 lg:py-6`).
- **Destaque do Ícone Oficial da Marca:** Redimensionamento e ampliação do ícone outline oficial da +B Farma (`assets/Logos/icone-b-farma.png` com `w-36` a `xl:w-64`) na lateral esquerda, com espaçamento generoso (`gap-10` a `gap-14`) empurrando o título institucional e as 5 estrelas do Google para a direita.
- **Cards Google Maps com Largura Fixa e Travada:** Os cards das filiais Plaza e Tapanã foram travados com largura fixa (`w-[275px] sm:w-[285px] max-w-[285px] flex-shrink-0`), garantindo proporções de smartphone sem distorção em telas ultrawide.
- **Foto Real da Fachada Tapanã:** Atualizada a imagem do Card 2 com a fotografia real da fachada externa com o logotipo +B (`assets/images/farma-tapana.webp`), alinhando com a foto interior do Plaza (`farma-plaza.webp`).
- **Painel Vermelho Flutuante com Deslocamento Vertical:** Container vermelho com elevação (`-my-12 xl:-my-14`) projetando-se para fora da faixa branca e acomodando os 2 cards em layout escalonado (Plaza com elevação superior `-translate-y-7` e Tapanã alinhado na base).
- **Rodapé Institucional (#1C1D22):** Fundo escuro unificado contínuo, logotipo branco centralizado com slogan, texto institucional, 4 botões de redes sociais (incluindo LinkedIn) e sub-faixa vermelha de copyright com assinatura `idedigital`.

## 2026-08-31 — Implementação do Carrossel Duplo de Avaliações do Google Maps (Prova Social)

### Front-End & Prova Social / Avaliações (S8)
- **Carrossel Duplo Infinito (Dual-Row Infinite Marquee):** Implementada a nova seção de avaliações inspirada no layout escuro de referência (**Anexo 2**), substituindo o grid estático por dois trilhos contínuos com direções complementares (`animate-marquee-left` e `animate-marquee-right`).
- **Eliminação de Sombras Brancas e Conflitos:** Removida sobreposição negativa com a seção de filiais e ajustada a paleta para `#1E212A` com cards `#282B35` limpos e elegantes.
- **Fotos de Perfil Reais e Avatares Coloridos:** Fotos reais de alta qualidade para clientes como Luciana Nascimento, Tamires Mesquita, Adriano Branco e Alfredo Maidana, além de avatares com as cores oficiais do Google Maps.
- **Tradução Completa para Português (PT-BR) & Remoção de Badges 'NOVO':** Todos os termos em inglês presentes nos cards de depoimento foram traduzidos para português nativo (`1 avaliação`, `2 avaliações`, `Guia Local`, `há 2 semanas`, `há 1 semana`, `há 3 meses`), e as tags "NOVO" foram completamente removidas para um design mais limpo e minimalista.
- **Cards de Depoimento Limpos e Elegantes:** Removidos os links individuais e ícones de tooltip de todos os cards de depoimento (incluindo Tamires), mantendo os cards 100% focados na leitura do depoimento visual e prova social contínua.
- **Botões Oficiais de Ação no Google Maps:** Mantidos apenas os botões pílula centrais de ação na base da seção para quem deseja abrir a ficha completa do Google Maps da unidade Plaza ou Tapanã.

## 2026-08-31 — Implementação e Refinamento do Modal de Vídeo Institucional

### Front-End & Vídeo / Seção Sobre (S4)
- **Refinamento do Botão de Play:** Reduzido o diâmetro do botão (`w-12` a `w-16`) e do ícone (`w-5` a `w-7`), com blur sutil e leve (`backdrop-blur-[2px]` e `bg-white/30`) para um visual minimalista e elegante sem ofuscar as pessoas na foto.
- **Proporção Vertical 9:16 (Stories/Reels):** Ajustado o contêiner do modal para formato vertical (`aspect-ratio: 9/16`, `max-w-[430px]`, `max-h-[88vh]`), com enquadramento `object-cover` e cantos arredondados, exibindo o vídeo gravado em orientação portrait com qualidade máxima sem faixas pretas laterais desnecessárias.
- **Correção da Reprodução e Modal:** 
  - Reposicionado o elemento `<div id="videoModal">` e funções JS para vinculação direta com escopo global `window.openVideoModal` / `window.closeVideoModal`;
  - Definido `src` direto no elemento `<video>` com `preload="auto"`, iniciando o vídeo a partir do início (`currentTime = 0`) no momento da abertura do popup;
  - Bloqueio de scroll de página quando ativo (`overflow: hidden`);
  - Fechamento com reset/pausa através do botão `X`, clique no backdrop escurecido (`bg-black/85`) e tecla `ESC`.

## 2026-08-31 — Atualização da Foto da Seção Sobre

### Front-End & Seção Sobre (S4)
- **Nova Imagem Institucional da Equipe:** Substituída a foto antiga pela nova imagem oficial da equipe farmacêutica em alta resolução (`assets/Pagina/S3 SOBRE/sobre-farma.png`), transmitindo ainda mais proximidade, credibilidade e atendimento humanizado.

## 2026-08-31 — Atualização dos Banners Horizontais (S4 / Antes do FAQ)

### Front-End & Assets
- **Sincronização dos Arquivos de Imagem:** Atualizados os caminhos do carrossel de banners horizontais (S4/S6) no `index.html` para apontar para as novas artes oficiais:
  - `assets/Pagina/S4 BANNERS HORIZONTAIS/1-BANNER-HORIZONTALL.png` (Clube +B: Mais vantagens para você, todos os dias)
  - `assets/Pagina/S4 BANNERS HORIZONTAIS/2-banner-ifood.png` (Estamos no iFood: Compre on-line pelo app e receba no conforto da sua casa - Filiais Plaza e Tapanã)


### Front-End & FAQ / Acessibilidade
- **Setas do Acordeão em Vermelho Oficial:** Substituída a cor neutra/acinzentada (`text-bf-muted`) das setas/chevrons dos 4 acordeões de Dúvidas Frequentes pela cor vermelha oficial da rede +B Farma (`text-brand-red` / `#E92125`), aumentando o destaque visual e alinhamento com a identidade cromática da marca.
- **Regra CSS Global:** Declarada a cor explícita `.faq-chevron { color: #E92125; }` no bloco de estilos para consistência e renderização uniforme.

## 2026-08-29 — Implementação do Carrossel de Banners Horizontais (Clube +B e iFood)

### Front-End & Banners Horizontais (S6)
- **Substituição do Bloco Estático por Carrossel:** Substituído o bloco de texto/card estático do Clube +B pelo novo carrossel dinâmico e responsivo com as imagens da pasta `assets/Pagina/S4 BANNERS HORIZONTAIS`:
  - `1-BANNER-HORIZONTAL.png` (Clube +B: Mais vantagens para você economizar todos os dias)
  - `2-banner-ifod.png` (iFood & Pedidos Online: Peça e receba em minutos)
- **Interatividade & Usabilidade:** Suporte a transição suave horizontal (`translateX`), botões de navegação lateral (prev/next) com efeito glassmorphism e hover na cor de marca, indicadores pill/dots de paginação com indicador ativo em vermelho, rotação automática com pausa no hover e suporte completo a gestos touch/swipe no mobile.
- **Preservação de Navegação:** Mantido o identificador `#clube` no contêiner com compensação de scroll para garantir navegação fluida a partir do menu.

### Front-End & Benefícios
- **Título Sucinto:** Ajustado o título do 4º card na barra rápida de vantagens de *"Programa de Benefícios"* para apenas **"Benefícios"**, mantendo padronização e objetividade visual.

## 2026-08-29 — Alinhamento dos Menus da Navbar para as Extremidades (Esquerda e Direita)

### Front-End & Header
- **Distribuição Ampla dos Links:** Menu da esquerda (*Início*, *Sobre*, *Nossas Lojas*) alinhado à esquerda (`justify-start`) e menu da direita (*Ofertas*, *Clube +B*) alinhado à direita (`justify-end`), com a logomarca no centro.

## 2026-08-29 — Refinamento Tipográfico dos Links da Faixa Superior (11px / Peso 400 Regular)

### Front-End & Header
- **Tipografia Discreta & Menos Destacada:** Links institucionais da faixa superior vermelha (*Depoimentos*, *Grupo de Ofertas*, *Vendas no Atacado*, *Trabalhe Conosco*) configurados em `text-[11px]`, peso `400` (`font-normal`) e cor suave `text-white/85` (hover `text-white`), garantindo hierarquia sutil e elegante.

## 2026-08-29 — Atualização dos Ícones Contextuais do Menu, Layout Centralizado e Calibragem de Links Âncora

### Front-End & Header / Navegação
- **Ícones Contextuais Distintos (Lucide):** Substituídos os ícones repetidos de sacola por ícones semânticos para cada destino de navegação (Início: *Home*, Sobre: *Heart/Cuidado*, Nossas Lojas: *MapPin/Localização*, Ofertas: *Tag de Desconto*, Clube +B: *Sparkles*, Dúvidas Frequentes: *HelpCircle*, Depoimentos: *MessageSquare*).
- **Layout Harmônico e Centralizado:** Reconfigurado o alinhamento da navbar desktop para agrupar os links de forma simétrica e aconchegante ao redor do logotipo central (`justify-end pr-6` na esquerda e `justify-start pl-6` na direita), eliminando o espaçamento excessivo nas extremidades.
- **Compensação Global de Scroll Âncora (`scroll-padding-top` & `scroll-mt`):** Adicionado `scroll-padding-top: 96px` (desktop) / `80px` (mobile) e `scroll-mt-24 md:scroll-mt-28` em todas as seções alvo (`#home`, `#beneficios`, `#ofertas`, `#sobre`, `#clube`, `#faq`, `#depoimentos`, `#filiais`), garantindo que o scroll suave pare com espaçamento para não cortar títulos sob o cabeçalho fixo.

## 2026-08-29 — Calibragem da Altura do Carrossel Hero Topo para 79vh

### Front-End & Hero Section (S1)
- **Altura Calibrada para 79vh (`79dvh`):** Atualizada a altura do carrossel principal (`.hero-carousel`) de `82vh` para `79vh` (`79dvh`), proporcionando uma proporção de tela mais equilibrada e aproximando a barra de benefícios flutuante e a seção de ofertas no primeiro scroll.

## 2026-08-29 — Atualização da Cor de Fundo da Página (`#FFEDEE`)

### Design System & Visual
- **Novo Tom de Fundo Institucional (`#FFEDEE`):** Atualizada a cor de fundo padrão da página de `#FFF5F6` para `#FFEDEE` (tom rosado suave/quente).
- **Aplicação Global:** Atualizadas as definições de `tailwind.config` (`bf.bg`), variáveis CSS (`--color-bg-page`), regra `html, body`, seções institucionais (`#ofertas`, `#sobre`, `#faq`, badge Clube +B) e o contrato visual `DESIGN-maisbfarma.md`.

## 2026-08-29 — Definição Exata da Altura da Navbar Branca em 67px no Desktop

### Front-End & Header
- **Navbar Principal Branca:** Altura fixada exatamente em **67px** no desktop (`md:h-[67px]`) e **56px** no mobile/tablet (`h-[56px]`), com centralização vertical perfeita (`flex items-center`) dos links com ícones de sacola e da logomarca oficial (`md:h-[48px]`).
- **Mobile Menu Drawer:** Posição top sincronizada (`top-[84px]`).

## 2026-08-29 — Compactação & Redução de Altura do Header (Faixa Vermelha e Navbar Branca)

### Front-End & Header
- **Faixa Superior Vermelha:** Altura compactada (`py-1`, ícones `w-3.5 h-3.5` e tipografia `text-xs/text-[11px]`), resultando em uma barra discreta e elegante de ~28px.
- **Navbar Principal Branca:** Padding vertical reduzido para `py-1 sm:py-1.5` com a logo centralizada otimizada para `h-9 sm:h-10 md:h-11`, reduzindo a altura total combinada do topo para ~80px (mais espaço útil para o conteúdo e navegação fluida).
- **Mobile Menu Drawer:** Posição top recalibrada (`top-[66px] sm:top-[74px]`).

## 2026-08-29 — Reformulação do Header (Novo Layout com Logo Central e Ícones de Sacola)

### Front-End & Header
- **Faixa Superior Vermelha (+B Red):**
  - Alinhamento de redes sociais à esquerda (Instagram, Facebook, YouTube) com ícones vetoriais limpos e efeitos suaves de hover.
  - Links institucionais à direita: `Depoimentos` (com scroll suave para a seção `#depoimentos`), `Grupo de Ofertas`, `Vendas no Atacado` e `Trabalhe Conosco` (com redirecionamentos estratégicos para atendimento e RH no WhatsApp).
- **Navbar Principal Branca:**
  - **Disposição Dividida com Logo Central:** Logotipo vertical oficial `logo-maisb-farma-vertical.webp` centralizado no header.
  - **Menu Esquerdo:** Links `Início` (`#home`), `Sobre` (`#sobre`) e `Nossas Lojas` (`#filiais`), cada um acompanhado pelo ícone de sacola de compras com tipografia bold/semibold.
  - **Menu Direito:** Links `Ofertas` (`#ofertas`) e `Clube +B` (`#clube`), mantendo a mesma padronização com ícones de sacola.
- **Gaveta Mobile (`#mobileMenu`):**
  - Atualização do menu mobile drawer com todos os links organizados por categorias, ícones de sacola, links da faixa superior e botão CTA destacado de WhatsApp.

## 2026-08-29 — Auditoria Cromática & Conformidade Estrita com o Design System

### Design System & Consistência Visual
- **Eliminação de Cores Arbitrárias:** Removida a cor ocre/dourada `#D97706` da tag `DIAS DA SEMANA`, padronizando-a estritamente com o token oficial `text-brand-red` (`#E92125`), mantendo coerência com todas as demais seções do site (`SOBRE A +B FARMA`, `CLUBE +B`, `DÚVIDAS FREQUENTES`, `PROVA SOCIAL`).
- **Validação de 100% dos Tokens:** Varredura global executada em `index.html` confirmando que todos os 17 valores hexadecimais correspondem exatamente ao contrato visual estabelecido em `DESIGN-maisbfarma.md`.

## 2026-08-29 — Reformulação da Seção "Sobre a +B Farma" e Indicadores da Rede

### Front-End & Layout
- **Novo Layout da Seção Sobre:** Alinhamento fiel com a identidade visual do print fornecido:
  - **Título & Tipografia:** Destaque de marca em *"seu dia a dia."* com vermelho +B (`#E92125`), texto principal em grafite escuro (`#32343D`) e parágrafo institucional ajustado.
  - **Ícones de Vantagens:** Bullets estilizados com badges circulares vermelhos e cruzes/símbolos de mais brancos.
  - **Botão CTA:** Pílula arredondada vermelha (`rounded-full`) com *"Saiba mais sobre nós"* e ícone de seta direcionadora.
  - **Fotografia Institucional:** Inclusão da fotografia acolhedora de atendimento em família com bordas super arredondadas (`rounded-[32px]`) e sombra sutil.
- **Card Flutuante de Indicadores:** Barra unificada em contêiner branco com divisórias verticais e 4 métricas de impacto (+50 Unidades, +500 mil Clientes, +10 anos Cuidando de você, +100 bairros Atendidos em Belém).

## 2026-08-29 — Carrossel de Bannerzinhos em Largura Total (Edge-to-Edge)

### Front-End & Layout
- **Largura 100% (Edge-to-Edge):** Removido o limite de largura restrita (`max-w`), permitindo que os banners fluam de ponta a ponta na tela sem cortes laterais abruptos.
- **Scroll e Alinhamento:** Ajustados os espaçamentos horizontais e pontos magnéticos de parada (`snap-start`), com os botões de navegação posicionados estrategicamente nas extremidades da tela.

## 2026-08-29 — Atualização dos Banners do Topo Hero com Novo Conjunto PNG

### Front-End & Mídias
- **Novo Conjunto de 10 Banners PNG:** Atualizada a lista de imagens do carrossel Hero (`#home`) para os novos arquivos em alta definição da pasta `assets/Pagina/S1 TOPO HERO/`:
  - `0-banner-topo.png`
  - `banners (1).png` até `banners (9).png`
- **Alinhamento Visual & Responsividade:** Configurado `object-position: left center;` com `object-fit: cover;` para enquadramento dos títulos, logotipo e elementos gráficos.
- **Sincronização:** Atualizados os caminhos e descrições semânticas de acessibilidade (`alt`) em `index.html`.

## 2026-08-29 — Atualização da Cor de Fundo da Página (`#FFF5F6`)

### Design System & Visual
- **Novo Fundo Institucional (`#FFF5F6`):** Atualizada a cor de fundo padrão da página de `#FFFFFF` para `#FFF5F6` (tom suave de acolhimento derivado da paleta oficial +B).
- **Aplicação Global:** Atualizado `html, body`, classes no Tailwind config e seções institucionais em `index.html` e no contrato de design `DESIGN-maisbfarma.md`.

## 2026-08-29 — Carrossel Hero 82vh: Ajuste Fino dos Indicadores (*Dots*)

### Front-End & Hero Section (S1)
- **Ajuste Fino de Posicionamento dos Dots:** Calibragem precisa para `bottom-10 sm:bottom-13 md:bottom-16`, posicionando a barra de pontos logo acima da linha superior do card de benefícios com espaçamento harmônico e equilibrado.
- **Alinhamento das Imagens:** Configurado `object-position: left top;` com `object-fit: cover;` para preenchimento integral com foco fixado no canto superior esquerdo dos banners.
- **Carrossel 82vh (`82dvh`) com Cantos Arredondados:** Altura ajustada com curvatura responsiva nas bordas inferiores (`border-radius: 0 0 28px 28px` no mobile, `36px` em tablets e `44px` no desktop com `isolation: isolate;`).
- **Integração de 10 Banners Promocionais e Institucionais:** Inclusão de todas as mídias WebP da pasta `assets/Pagina/S1 TOPO HERO/` (`1-TOPO-HERO.webp` e `banner-farm-ia (1)` a `(9)`).
- **Transições e Efeitos Visuais:** Transição suave com `opacity` e `transform: scale()`, mantendo alta fidelidade visual e legibilidade.
- **Controles Interativos Aprimorados:**
  - Botões laterais flutuantes com efeito *glassmorphism* e ícones Lucide.
  - Indicadores de ponto (*dots*) com badge de vidro e formato dinâmico para o slide ativo.
  - Suporte a gestos de deslizamento (*touch swipe*) em dispositivos móveis.
  - Pausa inteligente do autoplay no *hover* e suporte a navegação por teclado (setas direcionais).

## 2026-08-28 — Migração Completa para o Design System +B FARMA & Padronização

### Design System & Identidade Visual
- **Novo Contrato Visual:** Criação do arquivo oficial `DESIGN-maisbfarma.md` na raiz do projeto como fonte única de verdade visual.
- **Paleta Oficial +B FARMA:** Adoção estrita das cores oficiais: Vermelho Primário (`#E92125`), Vermelho Hover (`#C8161A`), Vermelho Light (`#FDE8E9`), Grafite Ink (`#32343D`), Cinza Body (`#555866`), Cinza Hairline (`#E7E7E7`), Fundo Escuro (`#1C1D22`) e Dark Card (`#25272E`).
- **Iconografia Oficial e Estrita:** Adoção obrigatória do pacote **[Lucide Icons](https://lucide.dev/icons/)** em toda a interface e documentação, com padronização técnica de SVGs (`stroke-width="2"`, `viewBox="0 0 24 24"`), eliminação total de emojis e pacotes heterogêneos.
- **Padronização Tipográfica:** Inclusão dos 18 arquivos físicos `.otf` da família **Lufga** no diretório `assets/fonts/` (Regular, Medium, Medium Italic, SemiBold, Bold, etc.) com declarações `@font-face` locais (`format('opentype')`) e fallback semântico robusto.
- **Remoção de Resíduos Legados:** Eliminação total de estilos, tokens e referências antigas (Airbnb, Rausch `#ff385c`, Airbnb Cereal, Circular).

### Front-End & Componentes
- **Criação do `index.html`:** Implementação da página principal institucional de produção com layout responsivo, integração de assets reais WebP, carrossel de fotos, bloco flutuante de benefícios, sobre nós, indicadores de mercado, ofertas da semana, Clube +B, FAQ interativo, prova social Google Meu Negócio e cards das filiais Plaza e Tapanã.
- **Unificação & Eliminação de Duplicatas:** Consolidação definitiva em `index.html` como página única de produção e remoção de `wireframe-desktop.html` para evitar duplicidade de manutenção.
- **Showcase `design-system-preview.html`:** Atualização integral do catálogo interativo de componentes, paleta de cores, escala tipográfica, botões, formulários, cards e mídias.

### Mídias & Otimização
- **Conversão WebP:** 33 fotografias Full HD (Unidades Plaza e Tapanã) e 4 variantes de logotipos com transparência otimizados (redução de 242.5 MB para ~7.4 MB — economia de 96.9%).

### Documentação Técnica
- **Revisão e Atualização Global dos Markdown (`.MD/`):**
  - `README.md`: Reformulado com a apresentação oficial da rede +B FARMA, stack, estrutura e comandos.
  - `arquitetura.md`: Atualizado com a arquitetura real, componentes e regras de layout.
  - `stack.md`: Atualizado com as tecnologias reais e sem resíduos não utilizados.
  - `features.md`: Mapeamento das funcionalidades implementadas, em andamento e planejadas.
  - `bugs.md`: Registro de débitos técnicos e correções efetuadas.
  - `deploy.md`: Procedimentos reais de entrega via VPS Docker/Nginx e Cloudflare.
  - `notas.md`: Registro das decisões de engenharia.
  - `notion.md`: Sincronização com o painel DB_IDE do Notion.
