# ProjetoCloud2050 - Global Solution: Otimização de Data Centers Sustentáveis

## Visão Geral do Projeto

O **ProjetoCloud2050 - Global Solution** é uma prova de conceito desenvolvida em Python para simular a otimização da seleção de *data centers* com foco em sustentabilidade e eficiência. O objetivo principal é maximizar a capacidade total de processamento, respeitando um limite estrito de consumo de energia.

O projeto modela este desafio como um **Problema da Mochila (Knapsack Problem)**, onde:
*   O **"peso"** é o consumo de energia (recurso limitado).
*   O **"valor"** é a capacidade de processamento (o que se deseja maximizar).
*   Cada *data center* é um item que pode ser incluído ou excluído (modelo 0/1).

##Funcionalidades Principais

1.  **Geração de Dados:** Simulação de um conjunto de *data centers* com atributos como nome, consumo de energia, emissão de CO2, capacidade de processamento e custo.
2.  **Algoritmo de Ordenação:** Utilização do algoritmo **Merge Sort** para ordenar os *data centers* com base em um critério (por exemplo, a razão processamento/energia, embora a implementação atual ordene apenas por processamento).
3.  **Otimização (Knapsack):** Aplicação de uma solução de **Programação Dinâmica com Memoização** para o Problema da Mochila, garantindo a seleção ideal de *data centers* dentro do limite energético.
4.  **Geração de Relatório:** Emissão de um relatório final detalhando os *data centers* selecionados e os totais agregados de energia, processamento, CO2 e custo.

## Estrutura do Repositório

O projeto é composto pelos seguintes arquivos Python:

| Arquivo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada do programa. Orquestra a geração de dados, ordenação, otimização e geração de relatório. |
| `data.py` | Módulo responsável por gerar o conjunto de dados simulados dos *data centers* utilizando a biblioteca `pandas`. |
| `knapsack.py` | Implementação do algoritmo de **Programação Dinâmica** para resolver o Problema da Mochila (0/1). |
| `merge_sort.py` | Implementação do algoritmo de ordenação **Merge Sort**. |
| `relatorio.py` | Módulo para processar e exibir o relatório final dos *data centers* selecionados. |

## Como Executar

### Pré-requisitos

O projeto requer a instalação da biblioteca `pandas` para manipulação dos dados.

```bash
pip install pandas
```

### Execução

Para rodar o projeto, execute o arquivo principal `main.py` a partir do terminal:

```bash
python main.py
```

O programa irá imprimir o processamento máximo possível e, em seguida, o relatório detalhado dos *data centers* selecionados.

### Exemplo de Saída

A saída do programa incluirá o processamento máximo alcançado e uma tabela de relatório similar a esta:

```
Processamento máximo possível: [Valor Calculado]

=== RELATÓRIO FINAL ===

             nome  energia  co2  processamento    custo
0   FusionCore_1      350   10            250   150000
1    SolarCloud_A1      500   50            200   100000
...
Total energia: [Soma da Energia]
Total processamento: [Soma do Processamento]
Total CO2: [Soma do CO2]
Total custo: [Soma do Custo]
```

## Tecnologias Utilizadas

*   **Python 3.x**
*   **Pandas** (para manipulação de dados)

## Link do video explicando cada funcao: https://www.youtube.com/watch?v=oBtppuQZiqI
