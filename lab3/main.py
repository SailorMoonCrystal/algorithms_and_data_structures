# author Kristina Alekseyenko

from convert_number import *
from cesar_code import decode, encode
from series_length_encode import encode_serie

# Zadanie 1.Konwersja liczby dziesiętnej na dowolny system liczbowy
assert convert_from_decimal(123, 12) == "a3"
assert convert_from_decimal(150, 13) == "b7"

# Zadanie 2. Konwersja liczby zapisanej w dowolnym systemie liczbowym na system dziesiętny
assert convert_to_decimal("B7", 13) == 150
assert convert_to_decimal("a3", 12) == 123

# Zadanie 3. Szyfr Cezara
input_string = input("Wprowadź tekst zadany: ")
shift = int(input("Wprowadź klucz: "))
print("Tekst zaszyfrowany: " + encode(input_string, shift))

input_string = input("Wprowadź tekst zaszyfrowany: ")
shift = int(input("Wprowadź klucz: "))
print("Tekst oryginalny: " + decode(input_string, shift))

#Zadanie 4.Kodowanie dugosci serii
assert encode_serie("!AB*")=='2141115111413111111'