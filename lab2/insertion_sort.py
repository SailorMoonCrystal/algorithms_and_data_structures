# author Kristina Alekseyenko

from str_comparator import compare


def insertion_sort(arr):
    if isinstance(arr[0], str):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and (compare(key, arr[j]) is False):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    else:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
