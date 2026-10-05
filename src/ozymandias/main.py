from fastapi import FastAPI, status
from pydantic import BaseModel


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
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok", version="0.1.0")
