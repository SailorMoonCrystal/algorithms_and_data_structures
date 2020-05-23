# author Kristina Alekseyenko

#Zwraca pierwszy najdzłuższy palindrom. Skrypt może byc rozszerzony o zwracanie wszystkich najdłuższych palindromow.
def find_palindrome(arr):
    for i, _ in enumerate(arr):
        for j in range(i + 1):
            m = arr[j: len(arr) - i + j]
            if is_palindrome(m):
                # print("FOUND IT")
                # print(m)
                return m


def is_palindrome(m):
    if len(m) > 1:
        return m == m[::-1]
    else:
        return False
