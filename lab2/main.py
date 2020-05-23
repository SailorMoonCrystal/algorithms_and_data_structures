# author Kristina Alekseyenko

from numpy.random import seed
from numpy.random import randint
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from brute_force import find_seq
from palindrome import find_palindrome
from file_reader import read_from_file

seed(1)
random_int_arr = randint(-5, 25, 10)
file_name = "lab2/data.txt"

# Zadanie 1. Selection sort
print("\nSelection sort")
print(random_int_arr)
arr = random_int_arr.copy()
selection_sort(arr)
print(arr)

# Zadanie 2. Insertion sort na tablicy ciagow znakow. Ciagi sa porownywane na podstawie dlugosci. Jesli dlugosc jest taka sama - dodatkowo alfabetycznie
print("\nInsertion sort")
str_arr=read_from_file(file_name)
print(str_arr)
arr = str_arr.copy()
insertion_sort(arr)
print(arr)

# Zadanie 3. Brute force
sequence = "aab"
where_arr = "baababaaabbaab"
assert find_seq(sequence, where_arr)==[1,7,11]

sequence = "aabb"
where_arr = "aaabbabbaabbaaaabb"
assert  find_seq(sequence, where_arr)==[1,8,14]

sequence = "aab"
where_arr = "aaccca"
assert find_seq(sequence, where_arr)==[]

sequence = "aab"
where_arr = ""
assert find_seq(sequence, where_arr)==[]

# Zadanie 4. Znajdywanie palindromow
test_str = "abacabcbacaac"
assert find_palindrome(test_str)=="acabcbaca"

test_str = ""
assert find_palindrome(test_str)==None

test_str = "a"
assert find_palindrome(test_str)==None

test_str = "aba"
assert find_palindrome(test_str)=="aba"
