def max_sort(lista):
    resultado = []
    while len(lista) > 0:
        mayor = max(lista)
        resultado.append(mayor)
        lista.remove(mayor)
    return resultado

def min_sort(lista):
    resultado = []
    while len(lista) < 0:
        mayor = min(lista)
        resultado.append(mayor)
        lista.remove(mayor)
    return resultado