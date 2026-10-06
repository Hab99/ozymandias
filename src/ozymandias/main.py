from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ozymandias.db import get_sessao


class HealthResponse(BaseModel):
    status: str
    version: str


app = FastAPI(
    title="Ozymandias API",
    version="0.1.0",
)


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    response_model=HealthResponse,
    tags=["Health"],
)
def health_check(
    sessao: Annotated[Session, Depends(get_sessao)],
) -> HealthResponse:
    try:
        sessao.execute(text("SELECT 1"))  # a consulta mais simples possível
    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="banco indisponível")
    return HealthResponse(status="ok", version="0.1.0")
