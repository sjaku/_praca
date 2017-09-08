__author__ = 'sjaku'

def quicksort(list):
    if len(list)<=1:
        return list
    pivot = list[len(list) // 3]
    print(pivot)

quicksort([3,4,5])