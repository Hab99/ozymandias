# ---------- Estágio 1: build ----------
FROM python:3.13-slim AS build

# Traz o binário do uv da imagem oficial, com a versão fixada
COPY --from=ghcr.io/astral-sh/uv:0.12.10 /uv /bin/uv

# Pré-compila o Python: o container inicia mais rápido
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

# Camada de dependências: só é refeita quando o uv.lock muda
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

# Camada do código: muda sempre, por isso vem depois
COPY README.md ./
COPY src ./src
RUN uv sync --locked --no-dev --no-editable


# ---------- Estágio 2: imagem final ----------
FROM python:3.13-slim

# Usuário sem privilégios de administrador
RUN useradd --create-home app

WORKDIR /app

# Só o ambiente pronto vem do estágio anterior
COPY --from=build /app/.venv /app/.venv

# Coloca o .venv no PATH para achar o uvicorn
ENV PATH="/app/.venv/bin:$PATH"

USER app
EXPOSE 8000

# 0.0.0.0: aceita conexões de fora do container
CMD ["uvicorn", "ozymandias.main:app", "--host", "0.0.0.0", "--port", "8000"]










