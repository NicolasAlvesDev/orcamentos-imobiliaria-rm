import csv
from modelos.imovel import Imovel


class ExportadorOrcamento:
    @staticmethod
    def gerar_csv(filename: str, imovel: Imovel, parcelas_contrato: int):
        aluguel_mensal = imovel.calcular_aluguel_mensal()
        valor_parcela_contrato = imovel.taxa_contrato_total / parcelas_contrato

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Parcela', 'Tipo Imóvel', 'Aluguel Mensal (R$)',
                            'Parcela Contrato (R$)', 'Total Mensal (R$)'])

            for i in range(1, 13):
                p_contrato = valor_parcela_contrato if i <= parcelas_contrato else 0.00
                total_mes = aluguel_mensal + p_contrato

                writer.writerow([
                    f"Mês {i:02d}",
                    imovel.tipo,
                    f"{aluguel_mensal:.2f}",
                    f"{p_contrato:.2f}",
                    f"{total_mes:.2f}"
                ])
