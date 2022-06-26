def bubble_sort(arr):
    loop = True
    while loop:
        loop = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                save = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = save
                loop = True
    return arr