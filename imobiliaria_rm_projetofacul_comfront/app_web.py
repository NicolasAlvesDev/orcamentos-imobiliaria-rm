from flask import Flask, render_template, request
from modelos.apartamento import Apartamento
from modelos.casa import Casa
from modelos.estudio import Estudio
from servicos.exportador import ExportadorOrcamento

app = Flask(__name__)


def montar_imovel(tipo, quartos, vagas, garagem, criancas):
    if tipo == "1":
        return Apartamento(int(quartos), garagem == 'S', criancas == 'S')
    if tipo == "2":
        return Casa(int(quartos), garagem == 'S')
    if tipo == "3":
        return Estudio(int(vagas))


def montar_tabela(imovel, parcelas):
    aluguel = imovel.calcular_aluguel_mensal()
    parc = imovel.taxa_contrato_total / parcelas
    tabela = []

    for i in range(1, 13):
        contrato = parc if i <= parcelas else 0.0
        tabela.append({
            "parcela": f"Mês {i:02d}",
            "tipo": imovel.tipo,
            "aluguel": f"R$ {aluguel:.2f}",
            "contrato": f"R$ {contrato:.2f}",
            "total": f"R$ {aluguel + contrato:.2f}"
        })

    return aluguel, parc, tabela


@app.route('/')
def index():
    return render_template('index.html', resultado=None)


@app.route('/calcular', methods=['POST'])
def calcular():
    tipo = request.form.get('tipo')
    quartos = request.form.get('quartos', 1)
    vagas = request.form.get('vagas', 0)
    garagem = request.form.get('garagem', 'N')
    criancas = request.form.get('criancas', 'N')
    parcelas = int(request.form.get('parcelas', 5))

    imovel = montar_imovel(tipo, quartos, vagas, garagem, criancas)
    aluguel, parc, tabela = montar_tabela(imovel, parcelas)

    resultado = {
        "aluguel": aluguel,
        "parcela_contrato": parc,
        "total_inicial": aluguel + parc
    }

    return render_template('index.html',
                           tipo=tipo, quartos=int(quartos), vagas=int(vagas),
                           garagem=(garagem == 'S'), criancas=(criancas == 'S'),
                           parcelas=parcelas, resultado=resultado, tabela=tabela
                           )


@app.route('/exportar', methods=['POST'])
def exportar():
    tipo = request.form.get('tipo_imovel')
    quartos = request.form.get('quartos')
    vagas = request.form.get('vagas')
    garagem = request.form.get('garagem')
    criancas = request.form.get('criancas')
    parcelas = int(request.form.get('parcelas'))

    imovel = montar_imovel(tipo, quartos, vagas, garagem, criancas)
    ExportadorOrcamento.gerar_csv("orcamento_web.csv", imovel, parcelas)

    aluguel, parc, tabela = montar_tabela(imovel, parcelas)

    resultado = {
        "aluguel": aluguel,
        "parcela_contrato": parc,
        "total_inicial": aluguel + parc
    }

    return render_template('index.html',
                           tipo=tipo, quartos=int(quartos), vagas=int(vagas),
                           garagem=(garagem == 'S'), criancas=(criancas == 'S'),
                           parcelas=parcelas, resultado=resultado, tabela=tabela,
                           msg_sucesso="Arquivo 'orcamento_web.csv' gerado com sucesso!"
                           )


if __name__ == '__main__':
    app.run(debug=True)
