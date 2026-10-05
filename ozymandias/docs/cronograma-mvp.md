# Cronograma: da semana 0 ao MVP

Plano pessoal de execução. As histórias (H1–H14) e as transições (T1–T13) estão em [mvp.md](mvp.md).

## Como usar

- **Avance por critério, não por calendário.** Uma semana só termina quando todos os itens de
  "Pronto para avançar" estão marcados. As datas servem para medir atraso, não para pular etapa
- **Ritmo de referência: cerca de 12 horas por semana**, por exemplo 3 noites de 2 h + 6 h no fim de semana.
  Se o seu ritmo real for outro, as semanas esticam ou encolhem, mas a ordem não muda
- **Atraso:** se uma semana passar 3 dias do previsto, consuma a folga da semana 6. Se a folga acabar, corte nesta
  ordem: mensagens de erro refinadas → H14 completo (fica só o admin por CLI) → H13. **Nunca corte** os testes da
  tabela de transições nem o webhook idempotente
- **Toda sessão termina com:** um commit pequeno, o CI verde e uma linha no `docs/diario.md` (o que fiz, o que
  quebrou, o que aprendi)
- **Revisão de domingo (30 min):** marque os critérios, escreva o resumo da semana no diário e decida se avança

### Definição de pronto de qualquer tarefa

- [ ] Tem teste automatizado e ele passa
- [ ] CI verde no GitLab (ruff, mypy, pytest)
- [ ] Sem segredo no código (senhas e chaves só no `.env`, que não vai para o repositório)
- [ ] Se tomou uma decisão de arquitetura, ela virou ADR em `docs/adr/`

---

## Semana 0 — Preparação (sem código do produto)

**Começa quando:** você aceitar o contrato (`ozymandias-contrato.pptx`, último slide).

**Objetivo:** máquina pronta, contas criadas e o projeto entendido de ponta a ponta.

Ferramentas
- [ ] Python 3.13 e **uv** (gerenciador de pacotes e ambientes)
- [ ] Docker Desktop funcionando (`docker run hello-world`)
- [ ] Git configurado com nome e e-mail
- [ ] VS Code com as extensões de Python, Ruff e Docker
- [ ] Stripe CLI instalada

Contas
- [ ] GitLab: projeto `ozymandias` criado (privado por enquanto)
- [ ] GitHub: repositório vazio `ozymandias` para o espelho
- [ ] Stripe: conta criada, **somente modo teste**
- [ ] AWS: conta pessoal nova, criada só na semana 1b (os créditos começam a contar na criação)

Estudo (cerca de 6 h)
- [ ] Ler `docs/mvp.md` inteiro e anotar dúvidas
- [ ] FastAPI do Zero (Eduardo Mendes): capítulos de introdução, rotas, Pydantic e banco de dados
- [ ] Tutorial do SQLAlchemy 2.0: ORM, sessão e transação

**Pronto para avançar quando:**
- [ ] `python --version`, `uv --version`, `docker run hello-world` e `stripe --version` funcionam no terminal
- [ ] As contas do GitLab, do GitHub e do Stripe (teste) existem
- [ ] As dúvidas sobre o `mvp.md` foram respondidas ou anotadas no diário

---

## Semana 1 — Peça 0: fundação

**Começa quando:** a semana 0 estiver concluída.

**Objetivo:** esqueleto que sobe com um comando e um pipeline que valida tudo a cada push.

- [ ] Estrutura do repositório: `src/ozymandias/` (rotas, serviços, repositórios, modelos), `tests/`, `docs/`
- [ ] `pyproject.toml` com uv; ruff, mypy e pytest configurados
- [ ] Configuração por variáveis de ambiente com `pydantic-settings`; `.env.example` versionado, `.env` no `.gitignore`
- [ ] FastAPI com `GET /health` que também testa a conexão com o banco
- [ ] `Dockerfile` (multi-stage) e `docker-compose.yml` com API, PostgreSQL 16 e Mailpit
- [ ] Alembic iniciado e primeira migration com as tabelas base: `usuario`, `cliente`, `projeto`, `evento`
- [ ] Primeiro teste com testcontainers: sobe um Postgres real, aplica as migrations e chama `/health`
- [ ] `.gitlab-ci.yml` com as etapas lint (ruff), tipos (mypy) e testes (pytest)
- [ ] Etapa de build: imagem publicada no Container Registry do GitLab a cada merge na `main`
- [ ] Espelhamento automático (push mirror) do GitLab para o GitHub configurado
- [ ] README em inglês, por enquanto só com: o que é, como rodar e a stack
- [ ] `docs/adr/0001-stack.md` e `docs/adr/0002-maquina-de-estados-como-dado.md`
- [ ] `docs/diario.md` criado

**Pronto para avançar quando:**
- [ ] Clonando o repositório do zero, `docker compose up` sobe tudo e `/health` responde 200
- [ ] As migrations aplicam num banco vazio sem erro
- [ ] O pipeline do GitLab passa verde
- [ ] A imagem da `main` aparece no Container Registry
- [ ] O código aparece no GitHub sem você ter feito push lá

---

## Semana 1b — Deploy do esqueleto na AWS (decisão de 05/10/2026)

**Começa quando:** a Peça 0 estiver verde e a imagem estiver no Container Registry.

**Objetivo:** completar o walking skeleton com o deploy: um merge na `main` chega sozinho a um servidor público.
Antecipa o maior risco da semana 9 enquanto o sistema ainda é só o `/health`.

**Teto:** uma semana. Se não fechar, registre no diário onde travou e siga para a semana 2.

Entra
- [ ] Conta AWS pessoal: MFA no root, alerta de orçamento (R$ 60, avisos em 50/80/100%), usuário administrador pelo IAM Identity Center; root guardado
- [ ] Conferir os créditos de conta nova em Billing
- [ ] EC2 pequena com Docker; security group abrindo só a porta da aplicação e o SSH restrito ao seu IP
- [ ] Credencial **somente leitura** do Container Registry no servidor (deploy token do GitLab), fora do código
- [ ] Etapa de deploy no pipeline pelo caminho mais simples: o runner entra por SSH e troca o container (chave em variável protegida e mascarada)
- [ ] `docs/adr/0003-deploy-antecipado-e-metodo.md` e o custo real anotado no README

Fica para a semana 9
- Domínio e HTTPS, OIDC, runner na EC2, deploy sem downtime, S3

**Pronto para avançar quando:**
- [ ] Um merge na `main` muda a resposta do `/health` no endereço público, sem você entrar no servidor
- [ ] O alerta de orçamento está ativo e nenhuma chave aparece no repositório
- [ ] A EC2 é parada quando não está em uso (anote no diário quanto isso economiza)

---

## Semana 2 — Autenticação (H1, H2, H3)

**Começa quando:** a Peça 0 estiver verde.

**Objetivo:** contas seguras: cadastro, verificação de e-mail, login e sessão.

- [ ] Migration: credenciais em `usuario`, `sessao_refresh`, `token_email`
- [ ] **H1** `POST /v1/auth/registrar`: senha em argon2id, regra de tamanho, resposta igual para e-mail novo ou existente
- [ ] **H2** verificação de e-mail com token de 24 h (o e-mail chega no Mailpit) e reenvio que invalida o anterior
- [ ] **H3** login com access token (15 min) e refresh token (7 dias, guardado só como hash)
- [ ] Rotação do refresh, detecção de reuso (revoga a família inteira) e logout
- [ ] Bloqueio após 5 tentativas erradas em 15 min (`429`)
- [ ] Formato único de erro em JSON (RFC 9457) para toda a API
- [ ] Testes de cada critério de aceite de H1, H2 e H3

**Pronto para avançar quando:**
- [ ] Todos os critérios de H1, H2 e H3 têm teste passando
- [ ] O teste de reuso do refresh token passa
- [ ] Nenhuma senha ou token aparece nos logs (verificado por teste ou inspeção)

---

## Semana 3 — Papéis, cadastro e solicitação (H14, H4, H5, H6)

**Começa quando:** um usuário consegue se registrar, verificar o e-mail e fazer login.

**Objetivo:** quem é quem no sistema e o primeiro passo da jornada.

- [ ] Dependência de autorização por papel (RBAC) reutilizável nas rotas
- [ ] **H14** comando `python -m ozymandias criar-admin`; `POST` e `PATCH /v1/usuarios` para a equipe interna
- [ ] **H4** `GET` e `PUT /v1/me`: cadastro do cliente com upsert e evento `cliente_cadastrado`
- [ ] Catálogo de serviços (tabela `servico`) com dados iniciais
- [ ] **H5** `POST /v1/projetos`: exige cadastro completo e e-mail verificado; grava `projeto_solicitado` (T1)
- [ ] **H6** listagem paginada só dos meus projetos e histórico por `seq`
- [ ] Teste: projeto de outro cliente devolve `404`, nunca `403`

**Pronto para avançar quando:**
- [ ] Os critérios de H4, H5, H6 e H14 têm teste passando
- [ ] Existe um teste para cada combinação papel × rota que deve ser negada
- [ ] Um cliente consegue, pelo Swagger, criar conta, se cadastrar e solicitar um orçamento

---

## Semana 4 — O coração: máquina de estados e propostas (T1–T7, T13; H7–H10, H13)

**Começa quando:** existe um projeto em `solicitado` criado pela API.

**Objetivo:** a regra de negócio central, testada à exaustão.

- [ ] Tabela de transições como dado: tuplas `(de, para, papel)` com a versão em que valem
- [ ] Serviço `transicionar`: `SELECT ... FOR UPDATE`, valida, atualiza `estado` e `versao`, grava o evento; tudo numa transação
- [ ] Migration: tabela `proposta` com versões
- [ ] **H7** fila do comercial
- [ ] **H8** enviar proposta (nova versão; a anterior vira `substituida`)
- [ ] **H9** aceitar, com `409 proposta_expirada` quando a validade passou
- [ ] **H10** recusar com motivo ou pedir revisão com comentário
- [ ] **H13** encerramento pelo admin, com motivo obrigatório
- [ ] Testes parametrizados: **cada linha da tabela passa** e **cada par fora dela falha**, inclusive com o papel errado
- [ ] Teste de concorrência: duas aceitações simultâneas, só uma vence
- [ ] `docs/adr/0004-transacao-e-lock-pessimista.md`

**Pronto para avançar quando:**
- [ ] 100% das transições do MVP cobertas por teste, nos dois sentidos (válida e inválida)
- [ ] O teste de concorrência passa 20 vezes seguidas
- [ ] O histórico mostra a jornada solicitação → proposta → revisão → nova proposta → aceite

---

## Semana 5 — Dinheiro: sinal de 50% pelo Stripe (H11, H12; T7)

**Começa quando:** um projeto chega a `aguardando_sinal`.

**Objetivo:** cobrança idempotente e confirmação só pelo gateway.

- [ ] Migrations: `pagamento` (com índice único parcial: no máximo uma cobrança pendente por projeto e tipo) e `webhook_recebido`
- [ ] Interface `Gateway` com a implementação do Stripe e uma falsa para os testes
- [ ] **H11** `POST /v1/projetos/{id}/pagamentos`: sinal de `floor(valor / 2)`, URL do Stripe Checkout e chave de idempotência
- [ ] Chamar de novo devolve a mesma cobrança; sessão expirada gera uma nova
- [ ] **H12** `POST /v1/webhooks/stripe`: valida a assinatura, grava o payload e confirma numa transação (T7)
- [ ] Mesmo evento repetido → `200` sem efeito; valor divergente → registrado, projeto não muda
- [ ] Teste de ponta a ponta local com `stripe listen` encaminhando o webhook para a API
- [ ] `docs/adr/0005-idempotencia-de-pagamento.md`

**Pronto para avançar quando:**
- [ ] Teste automatizado: webhook repetido não paga duas vezes
- [ ] Teste automatizado: assinatura inválida não grava nada
- [ ] Manualmente, com o cartão de teste `4242 4242 4242 4242`, o projeto vai para `em_desenvolvimento`

---

## Semana 6 — Folga e acabamento do MVP

**Começa quando:** a semana 5 estiver concluída, ou antes, se precisar recuperar atraso.

**Objetivo:** fechar pontas, documentar e começar a usar o projeto nas candidaturas.

- [ ] Recuperar o que atrasou nas semanas 1 a 5
- [ ] Cobertura de pelo menos 85% em `servicos/` (o CI falha abaixo disso)
- [ ] mypy estrito em `servicos/` e `repositorios/`
- [ ] Revisar mensagens e códigos de erro de todas as rotas
- [ ] README em inglês: diagrama da arquitetura, máquina de estados, como rodar, como testar e decisões principais
- [ ] Revisar os ADRs e o diário
- [ ] Gravar um vídeo de 2 minutos com a jornada pelo Swagger (opcional, mas ajuda muito)
- [ ] Tag `v0.1.0-mvp` no GitLab
- [ ] Atualizar o currículo de back-end com o link do repositório

**MVP pronto quando (é o critério do contrato):**
- [ ] A jornada solicitação → proposta → aceite → sinal pago roda inteira pela API
- [ ] Todas as transições do MVP estão cobertas por teste e o CI está verde
- [ ] Qualquer pessoa clona o repositório, roda `docker compose up` e segue o README sem ajuda

**Depois do MVP:** começar as candidaturas e a semana 7 (v1). O cronograma da v1 se escreve ao fim desta semana,
com o que você aprendeu sobre o seu ritmo real.

---

## Visão geral

| Semana | Foco | Histórias | Marco |
|---|---|---|---|
| 0 | Preparação | — | Ferramentas e contas |
| 1 | Fundação | — | **Peça 0** |
| 1b | Deploy do esqueleto na AWS | — | **Walking skeleton** |
| 2 | Autenticação | H1, H2, H3 | |
| 3 | Papéis, cadastro, solicitação | H4, H5, H6, H14 | |
| 4 | Máquina de estados e propostas | H7–H10, H13 | |
| 5 | Pagamento do sinal | H11, H12 | |
| 6 | Folga e acabamento | — | **MVP** (`v0.1.0-mvp`) |

Com a semana 1b, o MVP sai uma semana depois do previsto no contrato (sétima semana de trabalho).
