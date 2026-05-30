from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, tipo: str, valor_base: float):
        self.tipo = tipo
        self.valor_base = valor_base
        self.taxa_contrato_total = 2000.00

    @abstractmethod
    def calcular_aluguel_mensal(self) -> float:
        pass
