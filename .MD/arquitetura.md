# Arquitetura do Projeto

atualizado: 2026-08-28

---

## 1. Visão Geral

O projeto **+B FARMA** é estruturado como uma aplicação Web institucional estática (*Single Page Application / Static Site*), projetada com foco em máxima velocidade de carregamento, responsividade fluida, SEO local e aderência total ao Design System oficial.

---

## 2. Estrutura Real de Diretórios

```
site-maisb-farma/
├── index.html                   # Página principal institucional e catálogo (100% responsiva)
├── design-system-preview.html   # Showcase e UI kit interativo (getdesign.md)
├── DESIGN-maisbfarma.md         # CONTRATO VISUAL DO PROJETO
├── assets/
│   ├── fonts/                               # Família tipográfica Lufga completa (18 pesos em .otf)
│   ├── Logos/
│   │   ├── logo-maisb-farma.webp            # Logo principal horizontal
│   │   ├── logo-farmacia-branca.webp        # Versão branca para fundos escuros
│   │   ├── logo-maisb-farma-vertical.webp   # Versão selo vertical
│   │   └── logo-maisb-farma-alt.webp        # Variante alternativa
│   └── Fotografias/
│       ├── Und. Plaza/                      # 19 fotografias Full HD WebP da filial Plaza
│       └── Und. Tapanã/                     # 14 fotografias Full HD WebP da filial Tapanã
├── .MD/                                     # Documentação técnica e Obsidian
│   ├── README.md                            # Documento mestre de apresentação
│   ├── arquitetura.md                       # Este arquivo (Contrato Arquitetural)
│   ├── stack.md                             # Tecnologias reais do projeto
│   ├── features.md                          # Funcionalidades implementadas e status
│   ├── bugs.md                              # Histórico e auditoria de bugs
│   ├── deploy.md                            # Pipeline de publicação e VPS
│   ├── notas.md                             # Notas e decisões de arquitetura
│   ├── notion.md                            # Mapeamento do DB_IDE no Notion
│   ├── changelog.md                         # Histórico cronológico de alterações
│   └── plus/                                # Manuais de identidade visual em PDF
└── .gitignore                               # Regras de exclusão do controle de versão
```

---

## 3. Camadas e Módulos do Front-End

### 3.1 Camada de Apresentação (UI & Layout)
- **Estrutura HTML5 Semântica:** Utilização de tags semânticas (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **Design Tokens:** Centralizados em CSS Custom Properties (`:root`) no topo dos documentos e integrados ao tema do Tailwind CSS via script inline.
- **Tipografia:** Família `Lufga` com fallback para `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.

### 3.2 Componentes Globais & Seções Padronizadas
1. **Header & Top Bar:** Faixa superior vermelha (`#E92125`), barra de navegação branca (`#FFFFFF`) com logo horizontal e menu responsivo.
2. **Hero / Carrossel:** Carrossel dinâmico com fotos reais em WebP das filiais Plaza e Tapanã, títulos de destaque e CTAs de ação.
3. **Benefícios Flutuantes:** Container com 5 colunas de vantagens destacando entrega expressa, compre & retire, farmacêutico de plantão, Clube +B e atendimento via WhatsApp.
4. **Sobre Nós:** Apresentação da rede e foto institucional da loja física.
5. **Indicadores:** Bloco numérico com estatísticas de mercado (+50 unidades, +500 mil clientes atendidos, +10 anos de atuação).
6. **Ofertas da Semana:** Cards de campanhas promocionais e encartes.
7. **Clube +B:** Seção explicativa sobre as vantagens do programa de fidelidade.
8. **FAQ Acordeão:** Seção interativa com respostas às principais dúvidas dos clientes.
9. **Prova Social & Avaliações:** Seção em fundo escuro (`#1C1D22`) com depoimentos 5 estrelas verificados no Google Meu Negócio.
10. **Reputação & Filiais:** Cards dedicados às unidades Plaza e Tapanã com status de funcionamento e rotas.
11. **Footer Institucional:** Rodapé escuro com logo branca, redes sociais e faixa inferior de direitos autorais.

### 3.3 Camada de Lógica & Interatividade (Vanilla JS)
- **FAQ Accordion Controller:** Função `toggleFaq(button)` que gerencia a expansão e o fechamento acessível de perguntas.
- **Hero Carousel Engine:** Controle de slides, botões anterior/próximo, indicadores em pontos (dots) e autoplay temporizado a cada 6 segundos.
- **Mobile Menu Drawer:** Alternância do menu responsivo para telas móveis.

---

## 4. Otimização de Mídias & Performance

- **WebP Otimizado:** Todas as imagens foram processadas com compressão de alta fidelidade e interpolação Lanczos, gerando redução de 96.9% no payload total (~7.4 MB).
- **Sem Dependências Pesadas:** Zero dependências de runtime em Node.js ou bundlers pesados, garantindo tempo de resposta quase instantâneo e pontuação máxima no Google PageSpeed Insights.

---

## 5. Regras para Novas Páginas e Componentes

Qualquer nova página ou componente deve seguir obrigatoriamente:
1. Contrato Visual: [`DESIGN-maisbfarma.md`](../DESIGN-maisbfarma.md).
2. Manter a paleta `#E92125`, `#32343D`, `#E7E7E7`, `#FFFFFF` e `#1C1D22`.
3. Usar a tipografia `Lufga` com os pesos mapeados.
4. **Iconografia Estrita:** Utilizar exclusivamente ícones do pacote **[Lucide Icons](https://lucide.dev/icons/)** (SVG `stroke-width="2"`, `viewBox="0 0 24 24"`). É proibido misturar outros pacotes ou emojis na interface.
5. Reutilizar os componentes de container, grid, botões e cards documentados.
