# Continuação da restauração — 09/09/2026

## Situação atual

- O projeto é `C:\.PROJETOS - Sites 2026\site-maisb-farma`.
- Não existe commit local com a versão correta para restaurar.
- Por volta de 19:52 de 08/09/2026, o `index.html` foi substituído por uma versão antiga.
- A versão visual correta ainda estava carregada no navegador e foi capturada em `pagina-correta-recuperada-do-navegador.html`.
- O `index.html` atual está em estado híbrido: contém a seção de categorias nova e sua ordem já foi movida para antes de Ofertas, mas o restante da página ainda é a versão antiga/regredida.
- Nenhum commit, push ou deploy foi executado.

## Arquivos preservados

- `pagina-correta-recuperada-do-navegador.html`: DOM/CSS completo da página visualmente correta antes da regressão. A captura não contém os scripts executados do final do body e pode não conter `</body>`.
- `index-antes-da-restauracao-backup.html`: backup do arquivo que estava no disco antes da tentativa de restauração.
- `index-estado-atual-hibrido.html`: cópia exata do `index.html` atual.

## Resultado desejado

Restaurar a página inteira para o visual capturado, mantendo a seção circular de Categorias antes da seção:

`NÃO PERCA — Ofertas que rendem mais pra você.`

Não restaurar somente Categorias. Preservar os scripts funcionais e usar os arquivos de hero existentes atualmente:

- `assets/Pagina/S1 TOPO HERO/1-banner-topo.webp`
- `assets/Pagina/S1 TOPO HERO/2-banner-topo.webp`
- `assets/Pagina/S1 TOPO HERO/3-banner-topo.webp`

## Checklist de execução

- [ ] Ler este arquivo e verificar `git status --short`.
- [ ] Não apagar nem sobrescrever os três arquivos preservados em `.recovery/2026-09-08-1952`.
- [ ] Usar `pagina-correta-recuperada-do-navegador.html` como fonte do HTML e CSS da página inteira.
- [ ] Na captura, mover o bloco `S4 — CATEGORIAS CIRCULARES` para antes de `S3 — CARROSSEL DE BANNERS / CAMPANHAS EM DESTAQUE`.
- [ ] Trocar os três caminhos antigos do hero (`0-banner-topo.webp`, `banners (2).webp`, `banners (7).webp`) pelos arquivos `1-banner-topo.webp`, `2-banner-topo.webp` e `3-banner-topo.webp`.
- [ ] Recuperar do `index.html` atual todos os scripts que aparecem depois de `</main>` e inseri-los no documento restaurado antes de `</body>`.
- [ ] Manter a função global `scrollCategoryRail(direction)` para os botões da seção de categorias.
- [ ] Restaurar as funções globais do carrossel horizontal usadas por `onclick`: `nextHSlide`, `prevHSlide` e `setHSlide`.
- [ ] Garantir fechamento válido com `</body>` e `</html>`.
- [ ] Verificar todos os caminhos locais de `src` e eliminar erros 404.
- [ ] Rodar `python -m unittest tests/test_category_section.py -v`.
- [ ] Rodar `git diff --check`.
- [ ] Abrir/recarregar `http://127.0.0.1:8765/index.html` e conferir desktop e mobile.
- [ ] Conferir no navegador a ordem: Hero → Vantagens → Categorias → Ofertas → restante da página.
- [ ] Conferir menu, hero, carrosséis, FAQ, modais, botões das categorias e responsividade.
- [ ] Só declarar concluído depois de validar visualmente a página inteira.
- [ ] Não fazer commit, push ou deploy sem pedido explícito.

## Prompt para colar amanhã

```text
Continue a restauração do projeto C:\.PROJETOS - Sites 2026\site-maisb-farma exatamente de onde paramos.

Leia primeiro o arquivo:
C:\.PROJETOS - Sites 2026\site-maisb-farma\.recovery\2026-09-08-1952\CONTINUAR-AMANHA.md

Contexto: não existe commit local com a versão correta. Às 19:52 de 08/09/2026 o index.html foi substituído por uma versão antiga. A página inteira correta foi recuperada da aba do navegador e está em:
C:\.PROJETOS - Sites 2026\site-maisb-farma\.recovery\2026-09-08-1952\pagina-correta-recuperada-do-navegador.html

O index.html atual é híbrido e não é o resultado final. Restaure a página INTEIRA a partir da captura recuperada, não apenas a seção Categorias. Mantenha Categorias antes de “NÃO PERCA — Ofertas que rendem mais pra você”. Preserve/recoloque os scripts funcionais do index atual, corrija o carrossel horizontal e use os três assets atuais do hero: 1-banner-topo.webp, 2-banner-topo.webp e 3-banner-topo.webp.

Antes de editar, verifique git status. Não apague os arquivos da pasta de recovery. Depois, valide todos os caminhos de assets, rode os testes de categorias, git diff --check e faça conferência visual completa em desktop e mobile. Não faça commit, push ou deploy. Ao finalizar, informe exatamente os arquivos alterados, testes executados e qualquer pendência.
```
