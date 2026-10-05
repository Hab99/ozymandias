# Pesquisa de mercado: back-end Python (out/2026)

Coleta feita em 04/10/2026. Objetivo: descobrir o que as vagas cobram e transformar isso em requisitos
para um portfólio que gere entrevistas em até 3 meses.

## Método e fontes

Só texto original de vaga, direto do portal da empresa. Nada de blog ou agregador que resume vaga.

| Fonte | O que foi coletado |
|---|---|
| [Gupy](https://portal.gupy.io) (API pública do portal de busca) | 138 vagas únicas de back-end/software publicadas entre jul e out/2026, texto completo. Termos: python, fastapi, django, backend, engenheiro de software, software engineer |
| [Itaú Carreiras](https://carreiras.itau.com.br/busca-de-vagas) | As vagas de engenharia abertas (139 vagas no portal inteiro), leitura do texto completo |
| Quadros Greenhouse de ~40 empresas de tecnologia (Stripe, Datadog, Cloudflare, Adyen, Coinbase, Affirm, Airbnb, Databricks, Toast, Samsara, SeatGeek, N26, Monzo, Cabify...) | Todas as vagas abertas (~9.000), filtradas por júnior / new grad / early career / "Engineer I" |
| [Google Careers](https://www.google.com/about/careers/applications/jobs/results/?target_level=EARLY&q=software%20engineer) | Vagas Early Career de Software Engineer no Brasil, Canadá e Espanha |
| [Stanford Digital Economy Lab — Canaries in the Coal Mine](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf) | Dado de contexto sobre emprego de entrada em software |

Limitações:
- Contagem por palavra-chave (regex) no texto da vaga: é aproximada, serve para ranking, não para casa decimal
- A Gupy tem viés para algumas empresas que publicam muito (Stefanini, SysMap, PagBank)
- **Bradesco e Santander não apareceram** na Gupy nem foram cobertos: precisam de busca logada no LinkedIn
- Nubank e Mercado Livre estavam sem vaga pública no Greenhouse no dia da coleta

## Achado 1: vaga de júnior em back-end é rara

| Amostra | Júnior | Pleno | Sênior/especialista | Não informado |
|---|---|---|---|---|
| Gupy, 138 vagas de back-end/software | **5 (4%)** | 34 | 66 | 33 |

Nas ~9.000 vagas dos quadros internacionais, cerca de **15** são de entrada em engenharia de software.
O estudo de Stanford (dados de folha de pagamento da ADP, EUA) mostra queda relativa de emprego para
desenvolvedores de 22 a 25 anos desde a popularização da IA generativa, enquanto o emprego dos mais
experientes se manteve.

**Consequência:** o portfólio precisa colocar você na conversa de **pleno**. Seus 1 ano e 5 meses de
desenvolvimento com operação em produção contam como experiência; o projeto prova o resto.

## Achado 2: linguagens

Gupy, 138 vagas (uma vaga pode citar mais de uma):

| Linguagem | Vagas | % |
|---|---|---|
| Java / Kotlin | 64 | 46% |
| Node / TypeScript | 54 | 39% |
| **Python** | 47 | **34%** |
| .NET / C# | 31 | 22% |
| Go | 15 | 10% |

No Itaú, o back-end de produto é Java (Custódia, Java Sênior AWS/Kafka; Java Pleno). Python aparece em
**finanças e dados**: "Engenharia de Software Júnior – Python/AWS – Comunidade Finanças" (AWS Glue,
Athena, Python, SQL, Clean Architecture, Git e code review) e "Engenharia TI Jr – Dados" (Python, AWS,
SQL, GitHub Actions; diferenciais: APIs, microsserviços, observabilidade e resiliência).

Python em back-end puro aparece em fintech e produto digital: PagBank (Python Sr: asyncio, FastAPI,
Kafka, Oracle/MySQL/Mongo, Linux), Afya (Backend Pleno Python), Grupo Boticário, Montreal, SysMap.

**Consequência:** Python continua viável e é o seu ponto forte. Java fica como segunda língua para
depois do projeto, não agora.

## Achado 3: o que as vagas brasileiras cobram

Gupy, 138 vagas de back-end, % das vagas que citam o tema:

| Tema | Todas | Só as que citam Python (47) |
|---|---|---|
| APIs REST | 88% | 87% |
| SQL / banco relacional | 86% | 89% |
| Testes automatizados | 71% | 78% |
| Escalabilidade, resiliência, alta disponibilidade | 67% | 53% |
| CI/CD | 64% | 72% |
| Git | 62% | 65% |
| Mensageria (Kafka, RabbitMQ, SQS, eventos) | 55% | 42% |
| Observabilidade (logs, métricas, tracing) | 53% | 55% |
| Microsserviços | 52% | 44% |
| Segurança (OAuth, JWT, autenticação) | 51% | 48% |
| AWS | 45% | 51% |
| Docker | 44% | 46% |
| IA / LLM | 41% | 48% |
| Clean Architecture, SOLID, design patterns | 36% | 31% |
| Kafka especificamente | 31% | — |
| Azure | 30% | 34% |
| Kubernetes | 29% | 25% |
| Inglês | 18% | 27% |
| Terraform / IaC | 10% | — |
| FastAPI | 7% | 23% |

Exemplo representativo (Afya, Backend Pleno Python): Python/Go/Node; FastAPI ou similar; microsserviços
e sistemas distribuídos; Kafka ou RabbitMQ; PostgreSQL, MongoDB e Redis; Docker e CI/CD; testes
automatizados; **analisar trade-offs de performance, escalabilidade, custo e segurança**; code review.
Diferenciais: alta disponibilidade, integrações (APIs externas, autenticação, **billing**, sistemas
legados).

## Achado 4: o que as empresas internacionais cobram de um júnior

| Vaga | Onde | Pontos-chave |
|---|---|---|
| [Stripe — Software Engineer, New Grad / Early Career](https://stripe.com/jobs/search?gh_jid=8130881) | Dublin, Londres, Toronto, EUA, Barcelona (frontend) | Até 18 meses de experiência; projetos próprios ou em equipe; aprender sistema desconhecido; **comunicação escrita clara**; **usar IA para acelerar com julgamento crítico**. Desejável: code review, "atualizar produção com segurança", base de código grande |
| [Affirm — Software Engineer I, Backend](https://job-boards.greenhouse.io/affirm/jobs/7807506003) | Remoto Espanha / Polônia | **Python** ou Kotlin; AWS, MySQL, Kubernetes; blocos de sistemas distribuídos; código testado e extensível; code review; **plantão (on-call)** |
| [Toast — Software Engineer I](https://careers.toasttab.com/jobs?gh_jid=8185438) | Dublin | Kotlin/Java; testes e clean code; **Claude Code e agentes de IA no dia a dia**; PostgreSQL e DynamoDB |
| [Samsara — Software Engineer I](https://www.samsara.com/company/careers/roles/8210695?gh_jid=8210695) | Remoto Polônia | **Estruturas de dados e algoritmos**; projetos funcionando; "explicar o código e as escolhas"; **AI-native**; diferenciais: APIs públicas, eventos, permissões e controle de acesso |
| [SeatGeek — Software Engineer, New Grad](https://seatgeek.com/jobs/8227548?gh_jid=8227548) | Nova York | Backend em Python, Go ou C#; plataforma com AWS, Docker e Python; ferramentas de IA |
| [Google — Software Engineer II, Early](https://www.google.com/about/careers/applications/jobs/results/?target_level=EARLY&q=software%20engineer&location=Canada&location=Spain) | Málaga | 1 ano de software, 1 ano de sistemas distribuídos, 1 ano de **estruturas de dados e algoritmos** |
| [Airbnb — Early Career Software Engineer, Quality Engineering](https://careers.airbnb.com/positions/8154749?gh_jid=8154749) | **São Paulo** | Até 2 anos; linguagem web + back-end (Python ok); **Playwright**; testes no CI/CD; métricas de qualidade (cobertura, testes instáveis); IA aplicada a testes; **inglês** |

Padrões que se repetem:
1. **IA no fluxo de trabalho virou requisito explícito** (Stripe, Toast, Samsara, SeatGeek, Airbnb), sempre
   com "julgamento crítico sobre a saída"
2. **Fundamentos**: algoritmos e estruturas de dados aparecem nas vagas de Google e Samsara e são a
   base das entrevistas de big tech
3. **Comunicação em inglês, principalmente escrita**
4. **Produção**: code review, deploy seguro, plantão, dono do que entrega

Realidade de visto: vagas no exterior normalmente exigem autorização de trabalho no país. O caminho mais
curto para empresa internacional é o **escritório brasileiro** (Google em BH/SP, Airbnb em SP) ou vaga
remota para o Brasil.

## Encaixe com o seu perfil

| Pedido do mercado | Você já tem | Falta provar |
|---|---|---|
| APIs REST, SQL | Consome FastAPI, SQL Server | **Construir** uma API com banco modelado |
| Testes | 145 testes nos projetos de RPA, mocks | Testes de API com banco real, testes de integração |
| Mensageria / Kafka | ~1 ano produzindo e consumindo | Arquitetura orientada a eventos desenhada por você |
| Resiliência, reprocessamento | Checkpoint, deduplicação, reprocessamento em lote | O mesmo raciocínio num back-end (idempotência, outbox, DLQ) |
| Operação em produção | Monitoramento e falhas diárias | Observabilidade (logs, métricas, tracing) |
| Playwright, automação de testes | Sim, forte | Testes E2E de um produto seu no CI |
| Domínio bancário | 5 anos em esteiras de bancos | Contar isso no README e nas entrevistas |
| CI/CD, Docker, AWS | GitLab CI, Docker básico | Esteira completa e deploy na nuvem |
| IA com julgamento | Usa Claude Code com arquivos de contexto | Mostrar o processo (decisões, revisão, testes) |
| Inglês | Básico, leitura | **Lacuna principal para as internacionais** |
| Algoritmos | — | **Lacuna para big tech** |

## Vagas para olhar de perto

- **Airbnb — Early Career SE, Quality Engineering (São Paulo)**: Playwright + back-end + CI + IA. É a vaga
  internacional mais próxima do seu perfil
- **Itaú — Engenharia de Software Júnior Python/AWS (Comunidade Finanças)** e **Engenharia TI Jr – Dados**
- **PagBank, Afya, Grupo Boticário**: back-end Python em pleno/sênior; servem de régua

## O que fica com você (pesquisa de campo)

1. LinkedIn logado: buscar "Python" + "back-end" em **Bradesco, Santander, BTG, XP, Nubank, Mercado Livre e
   iFood** e salvar 15–20 vagas
2. Salário: Glassdoor e conversas para ter a faixa de júnior e pleno nessas empresas
3. Duas ou três conversas curtas com devs dessas empresas: "o que vocês olham no GitHub de um candidato?"
