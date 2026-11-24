# API de Transações e Estatísticas em Tempo Real

API REST desenvolvida em **Python** com **FastAPI** que recebe transações financeiras e calcula métricas estatísticas em tempo real referentes aos últimos 60 segundos. Projeto inspirado em desafios técnicos de engenharia de software para vagas Backend.

## Tecnologias Utilizadas
* **Python 3.11+**
* **FastAPI** (Framework web e documentação automática via Swagger)
* **Pydantic** (Validação e serialização de dados)
* **Pytest & HTTPX** (Testes automatizados de integração)

## Endpoints da API
* `POST /transacao` — Registra uma nova transação (`valor` e `dataHora` em ISO 8601). Retorna `201 Created`, `422 Unprocessable Entity` (para valores negativos ou datas futuras) ou `400 Bad Request`.
* `GET /estatistica` — Retorna `count`, `sum`, `avg`, `min` e `max` das transações ocorridas nos últimos 60 segundos.
* `DELETE /transacao` — Limpa todas as transações armazenadas na memória.

## Como Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com
cd api---transacoes---python

# Criar ambiente virtual e instalar dependências
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Iniciar o servidor
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: `http://localhost:8000/docs`

## Executar Testes Automatizados

```bash
pytest
```
