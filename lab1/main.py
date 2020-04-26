# author Kristina Alekseyenko

from numpy.random import seed
from numpy.random import randint
from min_max import find_minmax
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from binary_search import find_index

seed(1)
random_int_arr = randint(-5, 25, 10)

# Zadanie 1. Znalezienie wartości min i max
minmax = find_minmax(random_int_arr, len(random_int_arr))
print(random_int_arr)
print(minmax.min, minmax.max)

# Zadanie 2. Bubble sort
print("Bubble sort")
arr = random_int_arr.copy()
print(arr)
bubble_sort(arr)
print(arr)

# Zadanie 3. Insertion sort
print("Insertion sort")
arr = random_int_arr.copy()
print(arr)
insertion_sort(arr)
print(arr)

# Zadanie 4. Binary search on sorted set
print("Binary search")
print(arr)
res = find_index(arr, 10)
print(res)
res = find_index(arr, 0)
print(res)
res = find_index(arr, -5)
print(res)
res = find_index(arr, 50)
print(res)
