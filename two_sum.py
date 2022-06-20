#Dada una lista y un objetivo, devuelve los indices de los dos valores en la lista que suman el valor objetivo, considerando que solo hay una solucion
nums = [2,7,11,15]
target = 26
def two_sum(list, target):
    for index, element in enumerate(list):
        for index2, other_element in enumerate(list):
            if element + other_element == target:
                return [index, index2]
    return False

print(two_sum(nums, target))

