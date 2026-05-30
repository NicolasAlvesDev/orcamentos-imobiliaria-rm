# 🏢 Sistema de Automação de Orçamentos — Imobiliária R.M

O objetivo principal é automatizar, organizar e agilizar o processo de geração de orçamentos de locação residencial,
cobrindo três categorias de imóveis: Apartamentos, Casas e Estúdios.

## 📺 Vídeo de Apresentação (Pitch)
> 🎥 **Assista ao vídeo demonstrativo do sistema clicando no link abaixo:**
> 
> 👉 [**[CLIQUE AQUI PARA ASSISTIR AO VÍDEO PITCH]**](LINK_DO_YOUTUBE_EM_BREVE)

## 📋 Funcionalidades e Regras de Negócio
Tabela Base: Apartamentos (R$ 700,00), Casas (R$ 900,00) e Estúdios (R$ 1.200,00).
Módulo de Apartamentos: Acréscimo de R$ 200,00 para 2º quarto, R$ 300,00 para garagem e **desconto de 5%** caso o locatário não possua crianças na familia.
Módulo de Casas: Acréscimo de R$ 250,00 para 2º quarto e R$ 300,00 para inclusão de garagem.
Módulo de Estúdios: Inclusão de pacote básico de estacionamento contendo 2 vagas por R$ 250,00, com taxa de R$ 60,00 por cada vaga adicional contratada.
Taxa Contratual: Incorporação do valor obrigatório de contrato imobiliário no total de R$ 2.000,00, com simulação de parcelamento em até 5 vezes.
Persistência de Dados: Funcionalidade que permite ao usuário exportar um arquivo `.csv` com o planejamento anual detalhado contendo as 12 parcelas mensais.

## 📊 Estrutura Lógica e Pensamento Computacional
O desenvolvimento do algoritmo foi guiado pelos quatro pilares do pensamento computacional.
1. Decomposição: O problema complexo foi dividido em módulos menores. Cada tipo de imóvel recebeu seu próprio arquivo e regras na pasta `modelos`.
2. Reconhecimento de Padrões: Identificação de que a consolidação financeira, o parcelamento do contrato e a geração do arquivo `.csv` seguiam a mesma rotina, unificando o fluxo final.
3. Abstração: Foco exclusivo nas variáveis que impactam diretamente a precificação do orçamento, omitindo detalhes operacionais secundários da imobiliária.
4. Design de Algoritmos: Implementação ordenada de estruturas condicionais encadeadas para garantir uma execução precisa e segura dentro das regras do negócio.

> 🗺️ **Documentação Teórica:** O arquivo contendo a descrição sucinta da lógica e o desenho do **Fluxograma** está anexado diretamente na raiz deste repositório com o nome `FLUXOGRAMA + TEXTO.pdf`.

## 🛠️ Tecnologias Utilizadas
*   **Python** (Estrutura principal baseada em Orientação a Objetos)[cite: 2]
*   **Flask / HTML5 / CSS3** (Interface gráfica web desenvolvida para navegação do usuário)

## ⚙️ Como Executar o Projeto

Como o repositório foi estruturado com os ambientes separados, você pode rodar o projeto de duas formas:

1.  **Para rodar a versão Web (Interface Flask):**

Só selecionar o arquivo app_web.py e apertar run.

2.  **Para rodar a versão via Terminal:**

    Run Python File in dedicated Terminal
