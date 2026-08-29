# Notas e Decisões de Engenharia

atualizado: 2026-08-28

---

## Decisões Técnicas

1. **Adoção do Design System Oficial (+B FARMA):**
   - Eliminação de qualquer dependência visual legada anterior.
   - Centralização do contrato visual em `DESIGN-maisbfarma.md`.
   - Aplicação consistente da tríade de cores: Vermelho Primário (`#E92125`), Grafite de Alto Contraste (`#32343D`) e Cinza Neutro (`#E7E7E7`).

2. **Tipografia Lufga:**
   - Padronização em toda a interface institucional, garantindo personalidade moderna, autoridade médica/farmacêutica e alta legibilidade.
   - Configuração de `@font-face` com suporte a fallback imediato via `font-display: swap`.

3. **Arquitetura Estática & Otimização Extrema de Mídia:**
   - Opção por site estático puro (HTML5 + Tailwind CDN + Vanilla JS), eliminando overhead de build em Node.js e proporcionando carregamento instantâneo.
   - Conversão de todas as fotografias institucionais para WebP Full HD, diminuindo a carga de rede de 242.5 MB para ~7.4 MB (redução de 96.9%).

---

## Pendências e Próximos Passos

- [ ] Definir o número oficial de WhatsApp com link direto de atendimento para cada uma das filiais (Plaza e Tapanã).
- [ ] Inserir os códigos oficiais de Google Analytics 4 (GA4) e Meta Pixel antes da campanha de lançamento.
