from datetime import datetime
from pydantic import BaseModel

class TransacaoInput(BaseModel):
    valor: float
    dataHora: datetime

class EstatisticaOutput(BaseModel):
    count: int
    sum: float
    avg: float
    min: float
    max: float
