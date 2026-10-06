from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ozymandias.config import settings

# Criada uma vez: mantém o pool de conexões
engine = create_engine(settings.database_url, pool_pre_ping=True)

# Fábrica de sessões ligada ao engine
SessionLocal = sessionmaker(bind=engine)


def get_sessao() -> Iterator[Session]:
    # Antes do yield: abre a sessão. Depois: fecha, mesmo se der erro
    with SessionLocal() as sessao:
        yield sessao
