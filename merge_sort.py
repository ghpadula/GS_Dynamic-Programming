def merge_sort(lista, key):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], key)
    direita = merge_sort(lista[meio:], key)

    return merge(esquerda, direita, key)


def merge(esq, dir, key):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i][key] <= dir[j][key]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado
