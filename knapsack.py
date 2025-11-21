memo = {}

def knapsack(i, energia_restante, items):
    if i == len(items) or energia_restante == 0:
        return 0

    if (i, energia_restante) in memo:
        return memo[(i, energia_restante)]

    nome, energia, co2, processamento, custo = items[i]

    if energia > energia_restante:
        resultado = knapsack(i+1, energia_restante, items)
    else:
        incluir = processamento + knapsack(i+1, energia_restante - energia, items)
        excluir = knapsack(i+1, energia_restante, items)
        resultado = max(incluir, excluir)

    memo[(i, energia_restante)] = resultado
    return resultado
