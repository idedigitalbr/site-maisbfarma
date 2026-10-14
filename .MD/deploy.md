# Procedimento de Deploy

atualizado: 2026-08-28

---

## 1. Ambiente de Produção

- **Infraestrutura:** Servidor VPS Ubuntu com Docker e Nginx Reverse Proxy.
- **DNS & CDN:** Cloudflare com Proxy ativo (Nuvem Laranja), SSL/TLS Full (Strict) e minificação automática.
- **Diretório Web no Servidor:** `/var/www/site-maisb-farma/` ou container Docker dedicado.

---

## 2. Pré-Requisitos de Deploy

1. Verificar se todos os arquivos HTML (`index.html`, `design-system-preview.html`) estão salvos e validados.
2. Garantir que as imagens referenciadas em `assets/` estão presentes e em formato `.webp`.
3. Validar se não há caminhos absolutos locais de desenvolvimento (ex.: `G:\Meu Drive\...`) nas tags `src` ou `href`.

---

## 3. Fluxo de Publicação

### Via Docker Compose & Traefik

1. **Repositório:** `https://github.com/idedigitalbr/site-maisbfarma`
2. **Diretório do Projeto:** `/opt/site-maisbfarma/app`
3. **Build e Execução:**
   ```bash
   cd /opt/site-maisbfarma/app
   git pull origin main
   docker compose -p site-maisbfarma up -d --build
   ```
4. **Porta direta:** `8086`
5. **Roteamento Traefik:** `maisbfarma.suporteide.digital`, `maisbfarma.com.br`, `www.maisbfarma.com.br`

---

## 4. Checklist Pós-Deploy

- [ ] Acessar a URL de produção via HTTPS e verificar certificado SSL ativo.
- [ ] Testar navegação dos links do menu e âncoras da página.
- [x] Testar o carrossel Hero (troca de slides, autoplay, navegação manual e responsividade visual nos tamanhos revisados).
- [ ] Testar a abertura e fechamento dos acordeões de FAQ.
- [ ] Verificar o carregamento de todas as fotos e logotipos WebP.
- [ ] Testar o comportamento em dispositivo móvel (375px e 430px).
