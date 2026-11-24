from datetime import datetime, timedelta, timezone
from typing import List
from app.models import TransacaoInput, EstatisticaOutput

class TransacaoService:
    def __init__(self):
        self.transacoes: List[TransacaoInput] = []

    def adicionar(self, transacao: TransacaoInput) -> None:
        agora = datetime.now(timezone.utc)
        data_transacao = transacao.dataHora

        if data_transacao.tzinfo is None:
            data_transacao = data_transacao.replace(tzinfo=timezone.utc)

        if data_transacao > agora or transacao.valor < 0:
            raise ValueError("Transação inválida: data futura ou valor negativo.")

        self.transacoes.append(transacao)

    def limpar(self) -> None:
        self.transacoes.clear()

    def calcular_estatisticas(self, segundos: int = 60) -> EstatisticaOutput:
        limite = datetime.now(timezone.utc) - timedelta(seconds=segundos)
        
        valores_recentes = []
        for t in self.transacoes:
            dt = t.dataHora if t.dataHora.tzinfo else t.dataHora.replace(tzinfo=timezone.utc)
            if dt >= limite:
                valores_recentes.append(t.valor)

        if not valores_recentes:
            return EstatisticaOutput(count=0, sum=0.0, avg=0.0, min=0.0, max=0.0)

        quantidade = len(valores_recentes)
        soma = sum(valores_recentes)

        return EstatisticaOutput(
            count=quantidade,
            sum=round(soma, 2),
            avg=round(soma / quantidade, 2),
            min=min(valores_recentes),
            max=max(valores_recentes),
        )
