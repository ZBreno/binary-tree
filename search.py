import time
import random

min = 0
max = 1000000

quantityValues = 10000
values = random.sample(range(min, max+1), quantityValues)


def bubble_sort(values, sort=False):
    while not sort:
        sort = True
        for i in range(len(values)-1):
            if (values[i] > values[i+1]):
                aux = values[i+1]
                values[i+1] = values[i]
                values[i] = aux
                sort = False


def quicksort(values, start=0, end=None):
    if (end is None):
        end = len(values)-1

    if (start < end):
        partitions = partition(values, start, end)
        quicksort(values, start, partitions-1)
        quicksort(values, partitions+1, end)


def partition(values, start, end):
    pivot = values[end]
    start_partition = start

    for i in range(start, end):
        if (values[i] <= pivot):
            aux = values[i]
            values[i] = values[start_partition]
            values[start_partition] = aux
            start_partition += 1

    aux = values[start_partition]
    values[start_partition] = values[end]
    values[end] = aux

    return start_partition


def linear_search(values, value):
    for i in values:
        if (i == value):
            return value


def binary_search(values, value, start, end):

    if (value == values[len(values)-1] or value == values[0]):
        return value

    while True:
        middle = (start+end)//2
        if (value == values[middle]):
            return value

        if (value < values[middle]):
            end = middle

        elif (value > values[middle]):
            start = middle


# start = time.time()
# bubble_sort(values)
# end = time.time()
# print(f"bubblesort: {round(end-start, 2)} Segundos")

start = time.time()
quicksort(values)
end = time.time()
print(f"quicksort: {round(end-start, 2)} Segundos")

start = time.time()
binary_search(values, values[random.randint(
    min, quantityValues-1)], 0, len(values)-1)
end = time.time()
print(f"Busca binária: {round(end-start, 5)} Segundos")


start = time.time()
linear_search(values, values[random.randint(
    min, quantityValues-1)])
end = time.time()
print(f"Busca linear: {round(end-start, 5)} Segundos")
