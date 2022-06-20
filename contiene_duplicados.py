#La funcion debe devolver True si hay un elemento duplicado en la lista y False en caso contrario
#Hacemos una comparacion entre la longitud de la lista y la longitud de un set de la misma, los sets no pueden contener elementos duplicados, asi que eliminará los mismos cambiando su longitud final

lista0 = [2,2,4,3,1]
lista1 = [1,2,4,7,9]
def contiene_duplicados(list):
    return len(list) == len(set(list))

print(contiene_duplicados(lista0))
print(contiene_duplicados(lista1))
