# Checklist de execução — Site +B Farma

Fonte: checklist revisado enviado pelo usuário em 2026-09-08.

Status desta pausa (2026-09-08): **39 itens concluídos · 5 pendentes**.

## Fluxo de trabalho

- `/go` retoma a implementação a partir do próximo item aberto.
- `[x]` só é marcado após validação no código ou no navegador.
- Itens que dependem de confirmação comercial permanecem `[ ]` com motivo registrado em `.MD/bugs.md`.
- Commit e push somente quando solicitados pelo usuário.

## Regra e direção do produto

- [x] Manter o site institucional/comercial, sem e-commerce.
- [x] Preservar a estrutura existente e a identidade visual +B Farma.
- [x] Reduzir áreas extensas em `#F4FEFD` para priorizar branco e `#F8F9FA`.

## Header e conversão

- [x] Menu principal com Início, Ofertas, Categorias, Vantagens, Lojas e Sobre.
- [x] Botão PEDIR AGORA abrindo seletor de canal e unidade.
- [x] WhatsApp Plaza e Tapanã com números separados e conferidos no Linktree oficial.
- [x] iFood Plaza e Tapanã com links diretos oficiais.
- [x] Redes sociais oficiais: Instagram, TikTok e Facebook.
- [x] Remover os últimos links residuais do Linktree no header/footer e dados estruturados.

## Hero e performance

- [x] Hero reduzido para 3 slides.
- [x] Artes do hero alinhadas ao material original: 01 institucional, 03 proximidade e 08 campanha.
- [x] CTAs HTML reais nos slides.
- [x] Primeiro slide eager e demais lazy.
- [x] Modal de pedido aberto e fechado com sucesso no navegador local.
- [x] Validar pausa no hover, interação, autoplay de 6 segundos e prefers-reduced-motion (código revisado; autoplay e navegação manual conferidos no navegador local).

## Facilidades, ofertas e categorias

- [x] Atalhos de WhatsApp, iFood, Lojas, Clube +B e atendimento.
- [x] Remover “Baixe o App”, “Frete grátis” e promessas de serviço não confirmadas dos atalhos.
- [x] Atalhos desktop e mobile funcionam como ações/links; mobile usa grid de 2 colunas.
- [x] Seção de categorias presente após ofertas.
- [x] Categorias abrem o seletor de unidade/canal para evitar direcionamento automático a uma única filial.
- [x] Ocultar a seção duplicada “Como você quer comprar?” e consolidar Vantagens como S2.
- [x] Tornar todos os banners de ofertas clicáveis com destinos de categorias, vantagens ou canais.
- [x] Limitar S3 a quatro campanhas visíveis, sem catálogo ou preços individuais.
- [ ] Confirmar com a operação se Mamãe & Bebê e Vitaminas & Suplementos fazem parte do mix antes da publicação definitiva.

## Conteúdo institucional e FAQ

- [x] Texto institucional revisado.
- [x] Números não validados substituídos por atributos da marca.
- [x] FAQ sem promessas operacionais não confirmadas de retirada, entrega, pagamento ou Clube +B.
- [x] FAQ ampliado para seis dúvidas úteis, incluindo pedido pelo WhatsApp e localização das unidades.
- [ ] Confirmar horários, pagamentos e demais regras operacionais.
- [ ] Confirmar se a campanha recorrente de quinta-feira continua vigente antes de publicar a arte 08 como campanha atual.

## Avaliações e lojas

- [x] Remover o marquee de avaliações e o markup legado da interface; a seção mantém apenas links para as fichas oficiais.
- [ ] Substituir avaliações repetidas por 3 ou 4 avaliações verificadas das unidades.
- [x] Remover avatares de banco de imagens.
- [x] Remover frases de reputação não comprovadas; notas e estrelas agora são consultadas diretamente no Google.
- [x] Adicionar CTAs diretos de rota, WhatsApp e iFood nos cards das lojas.
- [x] Adicionar faixa final com CTA de WhatsApp após os cards das lojas.

## Banners, footer e conversão

- [x] S6 convertido de carrossel para dois cards independentes (Clube +B e iFood), responsivos em coluna no mobile.
- [x] CTA do iFood em S6 abre o seletor Plaza/Tapanã; não depende de Linktree.
- [x] Footer organizado em +B Farma, Atendimento e Institucional, com links oficiais e sem links vazios.
- [x] FAB do WhatsApp abre seletor de unidade e não escolhe Plaza automaticamente.

## SEO, analytics e revisão final

- [x] Favicon, Open Graph, canonical e Schema.org existentes.
- [x] Criar `sitemap.xml` e `robots.txt`.
- [ ] Configurar GA4/GTM somente com o ID oficial fornecido.
- [x] Revisar visualmente em 360px, 390px e 430px; cabeçalho, hero, grid de vantagens e overflow horizontal conferidos em navegador local.
