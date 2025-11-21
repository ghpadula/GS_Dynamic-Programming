from data import gerar_datacenters
from merge_sort import merge_sort
from knapsack import knapsack, memo
from relatorio import gerar_relatorio

def main():
    df = gerar_datacenters()
    items = df.values.tolist()

    
    ordenados = merge_sort(items, key=2)

    limite_energia = 2000  # Exemplo de limite energético
    processamento_total = knapsack(0, limite_energia, ordenados)

    print("Processamento máximo possível:", processamento_total)

    escolhidos = []
    energia_restante = limite_energia

    for i in range(len(ordenados)):
        if knapsack(i, energia_restante, ordenados) != knapsack(i+1, energia_restante, ordenados):
            escolhidos.append(ordenados[i])
            energia_restante -= ordenados[i][1]

    gerar_relatorio(escolhidos)

main()
