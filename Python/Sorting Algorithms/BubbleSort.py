from numpy import random

def genetrateArray(length):
    n = length
    arr = random.randint(100, size=n)
    return arr

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

l = random.randint(10, 20)
a = genetrateArray(l)

print("Array before aorting: ")
print(a)

bubbleSort(a)

print("Array After Sorting: ")
print(a)