# Registro de Bugs e Débitos Técnicos

atualizado: 2026-09-08

---

## Abertos

- *Nenhum bug crítico impeditivo em aberto no momento.*

---

## Corrigidos

- [x] **Ausência de Favicon e Metadados Open Graph:**
  - *Problema:* O site não possuía Favicon definido nem tags Open Graph/Twitter, gerando 404 em `/favicon.ico` e compartilhamentos sem prévia rica no WhatsApp e redes sociais.
  - *Solução:* Geração de favicons múltiplos (`.ico`, `.png`, `apple-touch-icon`), card social 1200x630 e Schema.org JSON-LD para as unidades Plaza e Tapanã.
- [x] **Banners em PNG Pesados no Carrossel e Seções:**
  - *Problema:* Os 19 banners de ofertas e institucionais estavam em PNG ocupando quase 10 MB.
  - *Solução:* Conversão de todos os banners para WebP Lanczos (qualidade 85), reduzindo o payload em 80.7% (para 1.93 MB) e atualizando o HTML.
- [x] **Duplicação de Arquivos de Fontes:**
  - *Problema:* A pasta `src/lufga_fonts/` duplicava 100% dos arquivos de `assets/fonts/`.
  - *Solução:* Remoção da pasta redundante `src/`, mantendo o repositório enxuto e consistente.
- [x] **Inconsistência de Identidade Visual e Cores Legadas:**
  - *Problema:* O wireframe e o design preview anteriores utilizavam referências legadas (Airbnb Cereal, cor Rausch `#ff385c`, tokens inexistentes).
  - *Solução:* Migração completa para o Design System oficial da +B FARMA (`#E92125`, `#32343D`, `#E7E7E7`, `#FFFFFF`, `#1C1D22` e tipografia `Lufga`).
- [x] **Imagens Pesadas e Carregamento Lento:**
  - *Problema:* As fotos originais das filiais ocupavam mais de 242 MB em formato JPEG não otimizado.
  - *Solução:* Conversão de todas as fotos para WebP Full HD com compressão Lanczos (redução para ~7.4 MB).
- [x] **Falta de Responsividade no Menu e Layout:**
  - *Problema:* Menus e carrossel quebravam em telas móveis abaixo de 768px.
  - *Solução:* Implementação do drawer mobile menu, controle responsivo de padding e carrossel adaptado.

---

## Em investigação

- [ ] Validar oficialmente horários, regras de retirada, formas de pagamento e dados das avaliações antes de publicar afirmações operacionais.
- [ ] Confirmar com a operação se a campanha recorrente de quinta-feira continua vigente antes de manter a arte correspondente no hero.
- [ ] Inserir 3 ou 4 avaliações verificadas no lugar do template legado, sem avatares de banco de imagens.
- [x] Revisar os links do Linktree no header/footer e ocultar a seção duplicada “Como você quer comprar?”.
- [ ] Configurar GA4/GTM somente depois de receber o ID oficial de mensuração.
- [x] Fazer a revisão visual final nos viewports de 360px, 390px e 430px; cabeçalho, hero, grid de vantagens e overflow horizontal conferidos em navegador local.
- [ ] Confirmar o mix comercial das categorias Mamãe & Bebê e Vitaminas & Suplementos.

- [ ] **Desempenho de carregamento de fontes Lufga em conexões lentas:**
  - *Investigação:* Monitorar se o fallback para `system-ui` / `Plus Jakarta Sans` evita FOIT (Flash of Invisible Text) através de `font-display: swap`.

---

## Não reproduzidos

- *Nenhum item registrado.*

---

## Obsoletos

- *Bugs e inconsistências do template anterior foram invalidados pela migração para a nova arquitetura.*
