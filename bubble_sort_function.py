def bubble_sort_0(arr):
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

def bubble_sort_1(list):
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp