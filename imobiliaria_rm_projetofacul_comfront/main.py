from modelos.apartamento import Apartamento
from modelos.casa import Casa
from modelos.estudio import Estudio
from servicos.exportador import ExportadorOrcamento

def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, digite um numero inteiro valido.")

def executar_sistema():
    print("-" * 50)
    print("      SISTEMA DE ORCAMENTOS - IMOBILIÁRIA R.M      ")
    print("-" * 50)

    print("Selecione o tipo de imovel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estudio")
    opcao = input("Opcao desejada: ").strip()

    imovel = None

    if opcao == "1":
        quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ")
        garagem = input("Deseja vaga de garagem? (S/N): ").strip().upper() == "S"
        criancas = input("Possui criancas residindo? (S/N): ").strip().upper() == "S"
        imovel = Apartamento(quartos, garagem, criancas)

    elif opcao == "2":
        quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ")
        garagem = input("Deseja vaga de garagem? (S/N): ").strip().upper() == "S"
        imovel = Casa(quartos, garagem)

    elif opcao == "3":
        vagas = ler_inteiro("Quantidade de vagas de estacionamento desejadas: ")
        imovel = Estudio(vagas)

    else:
        print("Opcao invalida! Encerrando...")
        return

    aluguel_mensal = imovel.calcular_aluguel_mensal()

    print("\n" + "=" * 40)
    print("CONFIRMACAO DO CONTRATO")
    print("=" * 40)
    
    parcelas_contrato = ler_inteiro("Em quantas vezes deseja parcelar a taxa de contrato (R$ 2.000,00) [Max 5x]? ")
    if parcelas_contrato < 1 or parcelas_contrato > 5:
        print("Quantidade invalida. Definindo padrao para 5x.")
        parcelas_contrato = 5

    parc_contrato_valor = imovel.taxa_contrato_total / parcelas_contrato

    print("\n" + "-" * 40)
    print("          RESULTADO DO ORCAMENTO          ")
    print("-" * 40)
    print(f"Tipo de Imovel:  {imovel.tipo}")
    print(f"Aluguel Mensal:  R$ {aluguel_mensal:.2f}")
    print(f"Taxa de Contrato: {parcelas_contrato}x de R$ {parc_contrato_valor:.2f}")
    print(f"Total nos primeiros meses: R$ {(aluguel_mensal + parc_contrato_valor):.2f}")
    print("-" * 40)

    gerar_arquivo = input("Deseja gerar o arquivo '.csv' com as 12 parcelas? (S/N): ").strip().upper()
    if gerar_arquivo == "S":
        ExportadorOrcamento.gerar_csv("orcamento.csv", imovel, parcelas_contrato)
        print("\nSucesso! Arquivo 'orcamento.csv' gerado.")

    print("\nObrigado por utilizar o sistema!")

if __name__ == "__main__":
    executar_sistema()