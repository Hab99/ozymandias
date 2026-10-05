from fastapi.testclient import TestClient
from ozymandias.main import app


def test_health_responde_ok():
    # Preparar: um cliente que conversa com a API sem subir servidor
    cliente = TestClient(app)

    # Agir: faz a requisição
    resposta = cliente.get("/health")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok", "version": "0.1.0"}
