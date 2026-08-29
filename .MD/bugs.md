# Registro de Bugs e Débitos Técnicos

atualizado: 2026-08-28

---

## Abertos

- *Nenhum bug crítico impeditivo em aberto no momento.*

---

## Corrigidos

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

- [ ] **Desempenho de carregamento de fontes Lufga em conexões lentas:**
  - *Investigação:* Monitorar se o fallback para `system-ui` / `Plus Jakarta Sans` evita FOIT (Flash of Invisible Text) através de `font-display: swap`.

---

## Não reproduzidos

- *Nenhum item registrado.*

---

## Obsoletos

- *Bugs e inconsistências do template anterior foram invalidados pela migração para a nova arquitetura.*
