# +B FARMA

Site institucional oficial e catálogo da rede de farmácias **+B FARMA** (Grupo Mais Barato), destacando as unidades **Plaza** e **Tapanã**.

---

## Sobre o projeto

A **+B FARMA** é a rede de farmácias do Grupo Mais Barato, projetada para entregar assistência à saúde com qualidade farmacêutica, acolhimento, conveniência de compra e economia garantida.

O projeto consiste em um site institucional de alta performance (One Page), focado na apresentação das unidades físicas, catálogo de vantagens, clube de fidelidade e prova social com avaliações verificadas do Google Meu Negócio.

---

## Stack

- **Linguagens:** HTML5 Semântico, CSS3 Moderno, JavaScript Vanilla (ES6+)
- **Estilização & Grid:** Tailwind CSS (via CDN) + CSS Custom Properties (`:root`)
- **Tipografia Exclusiva:** **Lufga** (pesos 400, 500, 500 italic, 600 e 700) com arquivos `.otf` locais em `assets/fonts/`.
- **Iconografia Oficial:** **[Lucide Icons](https://lucide.dev/icons/)** (SVG nativo, `stroke-width="2"`, sem emojis na interface).
- **Mídia Otimizada:** Imagens das filiais Plaza e Tapanã em **WebP Full HD** (1920px max) de alta fidelidade.
- **Deploy & Hospedagem:** Servidor Web Nginx / Docker em VPS com Cloudflare DNS e SSL

---

## Requisitos

- Qualquer navegador moderno (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari)
- Servidor web estático local (ex.: Live Server do VS Code, Python `http.server` ou Node.js `serve`)

---

## Instalação & Desenvolvimento

Clone ou acerte o diretório do projeto e execute um servidor local:

```bash
# Opção 1: Usando Python
python -m http.server 8000

# Opção 2: Usando Node.js npx
npx serve .
```

Abra o navegador em `http://localhost:8000` para visualizar o site (`index.html`) ou `design-system-preview.html` para consultar a biblioteca de componentes.

---

## Build & Otimização

Como o projeto utiliza tecnologias estáticas nativas (HTML5 / Tailwind CDN / WebP), não há etapa complexa de compilação.
- Todos os assets de imagem e logotipos já se encontram otimizados em `.webp` no diretório `assets/`.

---

## Estrutura de Diretórios

```
site-maisb-farma/
├── index.html                   # Página institucional oficial de produção (100% responsiva)
├── design-system-preview.html   # Showcase e documentação visual interativa (getdesign.md)
├── DESIGN-maisbfarma.md         # CONTRATO VISUAL DO PROJETO (Fonte única de verdade para UI)
├── assets/
│   ├── fonts/                   # Arquivos de fonte Lufga (.otf)
│   ├── Logos/                   # Logotipos oficiais em WebP transparente
│   └── Fotografias/             # Fotos Full HD das filiais (Und. Plaza e Und. Tapanã)
├── .MD/
│   ├── README.md                # Porta de entrada e documentação geral
│   ├── arquitetura.md           # Contrato arquitetural do projeto
│   ├── stack.md                 # Referência tecnológica detalhada
│   ├── features.md              # Estado funcional dos módulos
│   ├── bugs.md                  # Rastreamento de inconsistências e débitos
│   ├── deploy.md                # Procedimento de entrega e publicação
│   ├── notas.md                 # Notas técnicas e decisões de produto
│   ├── notion.md                # Integração com banco DB_IDE no Notion
│   ├── changelog.md             # Histórico de alterações do projeto
│   └── plus/                    # Manuais de identidade visual e briefing
└── .gitignore                   # Regras de exclusão do Git
```

---

## Design System

O arquivo [`DESIGN-maisbfarma.md`](../DESIGN-maisbfarma.md) é o **CONTRATO VISUAL E FONTE ÚNICA DE VERDADE PARA UI** deste projeto.

- **Cor Primária:** `#E92125` (Vermelho Oficial +B FARMA)
- **Cores Neutras:** `#FFFFFF` (Canvas), `#32343D` (Grafite Ink), `#555866` (Texto Body), `#E7E7E7` (Cinza Hairline)
- **Dark Surface:** `#1C1D22` (Footer & Prova Social), `#25272E` (Cards Dark)

Qualquer nova página, componente ou ajuste visual deve seguir rigorosamente as diretrizes documentadas em `DESIGN-maisbfarma.md`.

---

## Tipografia

Toda a interface é tipografada com a família **Lufga**:

- **Lufga Regular (400):** Textos corridos, parágrafos, FAQs
- **Lufga Medium (500):** Labels e subtítulos
- **Lufga Medium Italic (500 italic):** Depoimentos e citações
- **Lufga Semibold (600):** Botões, links, títulos de cards
- **Lufga Bold (700):** Títulos principais (H1, H2) e indicadores

---

## Deploy

O deploy é realizado via VPS com Docker/Nginx com apontamento de DNS e SSL gerenciados pela Cloudflare. Para detalhes operacionais, consulte [`.MD/deploy.md`](./deploy.md).

---

## Documentação

- [`.MD/arquitetura.md`](./arquitetura.md): Arquitetura de software e mídia
- [`.MD/stack.md`](./stack.md): Stack detalhada
- [`.MD/features.md`](./features.md): Mapa de funcionalidades
- [`.MD/bugs.md`](./bugs.md): Controle de pendências
- [`.MD/notion.md`](./notion.md): Sincronização Notion (DB_IDE)
- [`.MD/changelog.md`](./changelog.md): Histórico de versões
