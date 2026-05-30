from modelos.imovel import Imovel


class Estudio(Imovel):
    def __init__(self, qtd_vagas: int):
        super().__init__(tipo="Estúdio", valor_base=1200.00)
        self.qtd_vagas = qtd_vagas

    def calcular_aluguel_mensal(self) -> float:
        total = self.valor_base

        if self.qtd_vagas > 0:
            total += 250.00

            if self.qtd_vagas > 2:
                vagas_extras = self.qtd_vagas - 2
                total += vagas_extras * 60.00

        return total
