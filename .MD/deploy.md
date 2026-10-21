# Procedimento de Deploy e Infraestrutura CI/CD

**Última atualização:** 2026-10-21  
**Projeto:** +B Farma — Grupo Mais Barato  
**Repositório:** [idedigitalbr/site-maisbfarma](https://github.com/idedigitalbr/site-maisbfarma)  

---

## 1. Ambientes e Infraestrutura

- **Servidor VPS de Produção:** Hostinger (`179.236.75.128` - `srv2023103`), Ubuntu com Docker.
- **Painel Docker / Portainer:** `docker.grupomaisbarato.com.br`
- **Roteador / Reverse Proxy:** Traefik v2.11 conectado à rede Docker `proxy`.
- **Servidor Web do Container:** Nginx Alpine ultraleve (`maisbfarma-web`).
- **Diretório da Aplicação na VPS:** `/opt/site-maisbfarma/app`
- **Porta Direta de Preview:** `8086` (`http://179.236.75.128:8086`)
- **Roteamento HTTPS (Traefik):**
  - `maisbfarma.com.br`
  - `www.maisbfarma.com.br`
  - `maisbfarma.suporteide.digital`
- **Certificados SSL:** Let's Encrypt automático via Traefik (`certresolver=letsencrypt`).
- **CDN / DNS:** Cloudflare com Proxy ativo (Full Strict).

---

## 2. GitHub Actions (CI/CD Automático)

O fluxo de publicação é gerenciado pelo arquivo [deploy-vps.yml](file:///.github/workflows/deploy-vps.yml).

### Gatilhos
1. **Push na branch `main`:** Disparo automático imediato.
2. **Execução manual (`workflow_dispatch`):** Permite disparar o deploy a qualquer momento pela aba *Actions* no GitHub.

### Proteção de Concorrência
- O grupo `deploy-vps-maisbfarma` com `cancel-in-progress: false` garante que deploys simultâneos sejam enfileirados e executados em ordem estrita, evitando builds interrompidos ou inconsistência de estado.

### Segredos Configurados no Repositório (GitHub Secrets)
- `VPS_HOST`: IP do servidor de produção (`179.236.75.128`).
- `VPS_USER`: Usuário de deploy com permissão Docker (`root`).
- `VPS_SSH_PORT`: Porta SSH (`22`).
- `VPS_SSH_KEY`: Chave privada SSH autorizada no servidor.
- `VPS_SSH_FINGERPRINT`: Fingerprint SHA256 da chave de host (`SHA256:mq8COg7DKr2CSTiuioJCov0JMs3+YBkTzjPXZtUfh8E`).

---

## 3. Etapas do Pipeline de Deploy

1. **Checkout:** Baixa o código do commit validado.
2. **Validação de Arquivos Estruturais:** Verifica a existência de `Dockerfile`, `docker-compose.yml`, `nginx.conf`, `index.html` e assets vitais.
3. **Autenticação SSH com Verificação de Identidade:**
   - Efetua `ssh-keyscan` do servidor.
   - Compara o fingerprint SHA256 com o segredo `VPS_SSH_FINGERPRINT` antes de qualquer conexão para blindagem contra ataques *Man-in-the-Middle*.
   - Inicia `ssh-agent` temporário com destruição no trap de saída (`EXIT`).
4. **Publicação Atômica na VPS:**
   - Valida a segurança do diretório `/opt/site-maisbfarma/app`.
   - Armazena o SHA do commit anterior para caso de emergência.
   - Executa `git fetch origin main && git reset --hard <COMMIT_SHA> && git clean -fd`.
   - Executa `docker compose up -d --build --remove-orphans`.
   - Testa a resposta interna do Nginx localmente na VPS até confirmar `200 OK`.
5. **Rollback Automático:**
   - Em caso de falha no build ou na resposta do container, o pipeline restaura o commit anterior (`PREV_SHA`) e reconstrói o container seguro anterior antes de reportar falha no workflow.
6. **Validação Externa:**
   - Testa o endpoint direto `http://<VPS_HOST>:8086/`.
   - Valida a rota Traefik com cabeçalho `Host: maisbfarma.com.br`.

---

## 4. Comandos para Manutenção Manual na VPS

Se houver necessidade de operação manual no servidor:

```bash
# Conectar à VPS
ssh -i ~/.ssh/id_vps root@179.236.75.128

# Acessar pasta do projeto
cd /opt/site-maisbfarma/app

# Verificar status do container
docker compose ps

# Visualizar logs em tempo real
docker compose logs -f web

# Reconstruir manualmente
git pull origin main
docker compose up -d --build --remove-orphans
```

---

## 5. Procedimento de Rollback Manual

Caso seja necessário reverter uma versão específica manualmente:

```bash
cd /opt/site-maisbfarma/app
git log --oneline -n 5
git reset --hard <COMMIT_HASH_DESEJADO>
docker compose up -d --build --remove-orphans
```

---

## 6. Situação GitHub Pages vs VPS

- **VPS (Ambiente Principal):** Hospeda a versão oficial de produção, servida via Nginx/Docker/Traefik com controle de cache, headers de segurança e alta performance.
- **GitHub Pages:** Mantido ativo sem domínio customizado (`https://idedigitalbr.github.io/site-maisbfarma/`) como ambiente de contingência e visualização estática rápida, sem gerar qualquer conflito com o domínio oficial `maisbfarma.com.br`.
