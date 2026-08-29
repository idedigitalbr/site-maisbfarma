# Changelog

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
