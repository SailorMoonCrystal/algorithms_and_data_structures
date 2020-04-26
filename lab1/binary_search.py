# author Kristina Alekseyenko


def find_index(elements, value):
    left, right = 0, len(elements)-1

    while left <= right:
        middle = (left + right)//2

        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle+1

        elif elements[middle] > value:
            right = middle-1
