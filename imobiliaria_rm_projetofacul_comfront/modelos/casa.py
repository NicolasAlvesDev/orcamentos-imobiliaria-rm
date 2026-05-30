from modelos.imovel import Imovel

class Casa(Imovel):
    def __init__(self, qtd_quartos: int, possui_garagem: bool):
        super().__init__(tipo="Casa", valor_base=900.00)
        self.qtd_quartos = qtd_quartos
        self.possui_garagem = possui_garagem

    def calcular_aluguel_mensal(self) -> float:
        total = self.valor_base
        if self.qtd_quartos == 2:
            total += 250.00
        if self.possui_garagem:
            total += 300.00
        return total