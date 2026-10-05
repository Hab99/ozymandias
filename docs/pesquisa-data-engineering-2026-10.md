# Pesquisa de mercado: engenharia de dados (out/2026)

Coleta feita em 04/10/2026, com o mesmo método da [pesquisa de back-end](pesquisa-de-mercado-2026-10.md):
só o texto original das vagas, direto do portal da empresa.

| Fonte | O que foi coletado |
|---|---|
| [Gupy](https://portal.gupy.io) | 89 vagas únicas de engenharia de dados / analytics engineer publicadas entre jul e out/2026, texto completo (estágio, coordenação, cientista de dados e plataforma de IA excluídos) |
| Quadros Greenhouse de 45 empresas de tecnologia (Stripe, Databricks, Figma, Lyft, Brex, Affirm, Asana, Instacart, Samsara, Coinbase, N26, HelloFresh...) | 85 vagas de data engineer, analytics engineer e data platform |

Limitações: contagem por palavra-chave, aproximada. Temas genéricos (governança, IA, qualidade) aparecem
inflados porque as palavras também surgem no texto institucional das vagas; por isso ficam fora do ranking abaixo.

## Achado 1: júnior em dados é ainda mais raro que em back-end

| Amostra | Júnior | Pleno | Sênior/especialista | Não informado |
|---|---|---|---|---|
| Gupy, 89 vagas de dados | **2** | 22 | 42 | 23 |
| Greenhouse, 85 vagas de dados | **0** (só estágio) | 25 (pleno ou sem nível) | 60 | — |

As vagas internacionais pedem de 3 a 4 anos de experiência: Brex (São Paulo e São Francisco, 3+ anos),
Asana (Varsóvia, 3+ anos), Lyft (Toronto, 4+ anos), Affirm (Analytics Engineer II, Espanha, 3+ anos).

Uma das duas vagas júnior do Brasil é a [ANL Engenharia TI Jr – Dados do Itaú](https://carreiras.itau.com.br/vaga/sao-paulo/anl-engenharia-ti-jr-dados/35299/101004728032):
na descrição completa, é **back-end Python (microsserviços) dentro da comunidade de Dados**, construindo o
catálogo corporativo de dados.

**Consequência:** engenharia de dados raramente é porta de entrada. O caminho comum é entrar por back-end ou
analytics e migrar. O Ozymandias atende exatamente esse caminho: back-end primeiro, dados na v3.

## Achado 2: o que as vagas brasileiras de dados pedem

Gupy, 89 vagas, % das vagas que citam o tema:

| Tema | % |
|---|---|
| SQL | 84% |
| Python | 83% |
| Data warehouse / modelagem de dados | 58% |
| ETL / ELT | 52% |
| **Spark / PySpark** | **51%** (PySpark citado explicitamente em 39%) |
| AWS | 50% |
| CI/CD | 50% |
| Lakehouse / Delta / Iceberg | 46% |
| Git | 44% |
| **Databricks** | **43%** |
| Azure | 39% |
| **Airflow** | **38%** |
| Streaming (Kafka, Kinesis, Pub/Sub, tempo real) | 37% |
| APIs (consumo e construção) | 37% |
| Testes | 35% |
| Power BI / BI | 35% |
| Qualidade de dados | 31% |
| GCP | 29% |
| Terraform / IaC | 28% |
| Arquitetura medalhão (bronze/silver/gold) citada | 22% |
| BigQuery | 20% |
| **dbt** | **19%** |
| AWS Glue / S3 / Athena | 15% / 15% / 10% |
| Snowflake | 14% |
| Kafka | 13% |
| Docker | 12% |
| **FastAPI / Pydantic / SQLAlchemy** | **0%** |

## Achado 3: o que as vagas internacionais de dados pedem

Greenhouse, 85 vagas: Python 56%, streaming 56%, SQL 54%, modelagem de dados 51%, testes 47%, sistemas
distribuídos 45%, **Snowflake 37%**, **Kafka 36%**, Spark 35%, **Airflow 34%**, Databricks 31%, **dbt 30%**,
AWS 30%, Java 29%, Iceberg/Delta 28%.

Diferença para o Brasil: lá fora pesam mais **dbt, Snowflake, Kafka e streaming**; aqui pesam mais
**Spark/PySpark, Databricks e nuvem (AWS e Azure)**. Uso de IA no fluxo de trabalho aparece de novo de forma
explícita (Brex pede "agentic AI"; Affirm pede camada semântica para IA e uso de IA no dia a dia).

## O que isso significa para o Ozymandias

**Já coberto pelo projeto (camada analítica existente + v3):** SQL, Python, **PySpark** (a silver já é escrita
em PySpark no Lakeflow), Databricks, lakehouse com Delta, arquitetura medalhão, qualidade de dados com
expectativas, governança e LGPD no Unity Catalog, CI/CD via Asset Bundles, S3 e IAM.

**Pydantic e SQLAlchemy** não aparecem em vaga de dados: são ferramentas de back-end e continuam na API. Um uso
que conecta os dois mundos: o **schema de cada evento definido em Pydantic** (com `versao_schema`) vira o
**contrato de dados** entre a API e o pipeline. É prática real de engenharia de dados (data contracts).

**Lacunas, em ordem de prioridade para a v3:**

| Lacuna | Peso no mercado | Proposta |
|---|---|---|
| Modelagem dimensional explícita | 58% (DW / modelagem) | Gold com fatos e dimensões nomeados (`fato_transicao`, `dim_cliente`, `dim_data`) |
| Orquestração com Airflow | 38% BR, 34% internacional | Uma DAG que extrai eventos do Postgres para o S3 e dispara o Job do Databricks. Roda no Docker local, não na EC2 de 1 GB |
| Contrato de dados | — (diferencial) | Schema Pydantic dos eventos publicado e validado na exportação |
| dbt | 19% BR, 30% internacional | Opcional: reescrever parte da gold em dbt |
| Streaming / Kafka | 37% / 13% BR; 56% / 36% internacional | Fora: o currículo já tem Kafka da experiência profissional |
| Athena / Glue | 10–15% | Fora: seria um quarto serviço AWS |

## Fontes

- [Gupy — busca de vagas](https://portal.gupy.io)
- [Itaú — ANL Engenharia TI Jr – Dados](https://carreiras.itau.com.br/vaga/sao-paulo/anl-engenharia-ti-jr-dados/35299/101004728032)
- [Brex — Data Engineer (São Paulo)](https://www.brex.com/careers/8523806002?gh_jid=8523806002)
- [Lyft — Data Engineer (Toronto)](https://app.careerpuck.com/job-board/lyft/job/8662205002?gh_jid=8662205002)
- [Asana — Data Engineer (Varsóvia)](https://www.asana.com/jobs/apply/8131896?gh_jid=8131896)
- [Affirm — Analytics Engineer II (Espanha)](https://job-boards.greenhouse.io/affirm/jobs/7916080003)
