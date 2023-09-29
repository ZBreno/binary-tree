from main import BinaryTree, Node
import time
import random
from PrettyPrint import PrettyPrintTree

min = 0
max = 10000

listOfNumbers = random.sample(range(min, max+1), 10000)


def bubble_sort(listOfNumbers, sort=False):
    while not sort:
        sort = True
        for i in range(len(listOfNumbers)-1):
            if (listOfNumbers[i] > listOfNumbers[i+1]):
                aux = listOfNumbers[i+1]
                listOfNumbers[i+1] = listOfNumbers[i]
                listOfNumbers[i] = aux
                sort = False


def quicksort(values, start = 0, end = None):
    if (not end):
        end = len(values)-1
    
    if (start < end):
        pivot = partition(values, start, end)
        quicksort(values, start, pivot-1)
        quicksort(values, pivot+1, end)


def partition(values, start, end):
    pivot = values[end]
    start_partition = start
    
    for i in range (start, end):
        if (values[i] >= pivot):
            aux = values[i]
            values[i] = values[start_partition]
            values[start_partition] = aux
            start_partition += 1
    
    aux = values[start_partition]
    values[start_partition] = values[end]
    values[end] = aux    

    return start_partition

def printTree(source):
    ptt = PrettyPrintTree(
        lambda x: [x for x in [x.smaller, x.bigger] if x is not None],
        lambda x: x.value
    )

    ptt(source)


# start = time.time()
# bubble_sort(listOfNumbers)
# end = time.time()
# print(f"{round(end-start, 2)} Segundos")

start = time.time()
quicksort(listOfNumbers)
end = time.time()
print(f"{round(end-start, 2)} Segundos")
