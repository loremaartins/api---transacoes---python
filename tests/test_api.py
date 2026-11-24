from datetime import datetime, timedelta, timezone
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fluxo_completo_transacoes():
    res_delete = client.delete("/transacao")
    assert res_delete.status_code == 200

    agora = datetime.now(timezone.utc).isoformat()
    res_post = client.post("/transacao", json={"valor": 100.50, "dataHora": agora})
    assert res_post.status_code == 201

    res_get = client.get("/estatistica")
    assert res_get.status_code == 200
    dados = res_get.json()
    assert dados["count"] == 1
    assert dados["sum"] == 100.50
    assert dados["avg"] == 100.50

def test_rejeitar_transacao_futura():
    futuro = (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat()
    res = client.post("/transacao", json={"valor": 50.0, "dataHora": futuro})
    assert res.status_code == 422

def test_rejeitar_valor_negativo():
    agora = datetime.now(timezone.utc).isoformat()
    res = client.post("/transacao", json={"valor": -10.0, "dataHora": agora})
    assert res.status_code == 422
