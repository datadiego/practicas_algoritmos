#Dada una lista de ints:
#1. Reemplaza los ints divisibles entre 3 por fizz 
#2. Reemplaza los ints divisibles entre 5 por buzz
#3. Reemplaza los ints divisibles entre 3 y 5 por fizzbuzz

numeros = [45, 22, 3, 14, 65, 97, 72, 12]

def fizzbuzz(list):
    for i, element in enumerate(list):
        if element % 3 == 0:
            list[i] = "fizz"
        if element % 5 == 0:
            list[i] = "buzz"
        if element % 3 == 0 and element % 5 == 0:
            list[i] == "fizzbuzz"
    return list

lista = fizzbuzz(numeros)
print(lista)