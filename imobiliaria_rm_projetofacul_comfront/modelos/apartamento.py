from modelos.imovel import Imovel


class Apartamento(Imovel):
    def __init__(self, qtd_quartos: int, possui_garagem: bool, possui_criancas: bool):
        super().__init__(tipo="Apartamento", valor_base=700.00)
        self.qtd_quartos = qtd_quartos
        self.possui_garagem = possui_garagem
        self.possui_criancas = possui_criancas

    def calcular_aluguel_mensal(self) -> float:
        total = self.valor_base
        if self.qtd_quartos == 2:
            total += 200.00
        if self.possui_garagem:
            total += 300.00
        if not self.possui_criancas:
            total *= 0.95
        return total
