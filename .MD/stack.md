# Stack Tecnológica

atualizado: 2026-08-28

---

## Frontend

- **Estrutura:** HTML5 Semântico com foco em acessibilidade e SEO local.
- **Estilização:** 
  - CSS Custom Properties (`:root`) para centralização de Design Tokens.
  - Tailwind CSS via CDN integrado à paleta e raios oficiais.
- **Tipografia:** 
  - Fonte principal: **Lufga** (Pesos 400 Regular, 500 Medium, 500 Medium Italic, 600 Semibold, 700 Bold).
  - Fallback semântico: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`.
- **Iconografia Obrigatória:** **[Lucide Icons](https://lucide.dev/icons/)** (SVG nativo, `stroke="currentColor"`, `stroke-width="2"`, `viewBox="0 0 24 24"`). Proibido o uso de outros pacotes ou emojis em componentes de interface.
- **Interatividade:** JavaScript Vanilla (ES6+) sem dependências de frameworks pesados.
- **Mídia:** Imagens no formato moderno `.webp` Full HD (1920px máx) com interpolação Lanczos e preservação de transparência alfa nos logos.

---

## Backend & Dados

- **Arquitetura:** Estática (*Static Site / Jamstack*).
- **Banco de Dados:** N/A (Consumo direto de assets estáticos e links de ação para WhatsApp / Google Maps).

---

## Build & Ferramental

- **Servidor Local de Testes:** Python `http.server` / Node.js `serve` / VS Code Live Server.
- **Otimização de Assets:** Processamento prévio de mídia para formato WebP de alta eficiência.

---

## Infraestrutura & Deploy

- **DNS & CDN:** Cloudflare (gerenciamento de DNS, proteção DDoS e terminação SSL/TLS).
- **Servidor de Produção:** Nginx em container Docker na VPS da agência.
- **Controle de Versão:** Git local e sincronização Obsidian (`.MD/`) e Notion (`DB_IDE`).
