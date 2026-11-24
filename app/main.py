from fastapi import FastAPI, HTTPException, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models import TransacaoInput, EstatisticaOutput
from app.service import TransacaoService

app = FastAPI(
    title="API de Transações e Estatísticas",
    description="Desafio Técnico Backend - Cálculo de métricas em tempo real",
    version="1.0.0"
)

service = TransacaoService()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "JSON inválido"})

@app.post("/transacao", status_code=status.HTTP_201_CREATED)
def criar_transacao(transacao: TransacaoInput):
    try:
        service.adicionar(transacao)
        return Response(status_code=status.HTTP_201_CREATED)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.delete("/transacao", status_code=status.HTTP_200_OK)
def limpar_transacoes():
    service.limpar()
    return Response(status_code=status.HTTP_200_OK)

@app.get("/estatistica", response_model=EstatisticaOutput, status_code=status.HTTP_200_OK)
def obter_estatisticas():
    return service.calcular_estatisticas(segundos=60)
