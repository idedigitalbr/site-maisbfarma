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

### Via Docker / Nginx na VPS

1. Sincronizar os arquivos do projeto para o diretório de produção na VPS:
   ```bash
   rsync -avz --exclude '.git' --exclude '.MD' ./ usuario@vps:/var/www/site-maisb-farma/
   ```
2. Recarregar o serviço Nginx para aplicar eventuais regras de cache:
   ```bash
   docker exec nginx-proxy nginx -s reload
   ```
3. Limpar o cache na Cloudflare para propagação imediata da nova versão.

---

## 4. Checklist Pós-Deploy

- [ ] Acessar a URL de produção via HTTPS e verificar certificado SSL ativo.
- [ ] Testar navegação dos links do menu e âncoras da página.
- [ ] Testar o carrossel Hero (troca de slides e responsividade).
- [ ] Testar a abertura e fechamento dos acordeões de FAQ.
- [ ] Verificar o carregamento de todas as fotos e logotipos WebP.
- [ ] Testar o comportamento em dispositivo móvel (375px e 430px).
