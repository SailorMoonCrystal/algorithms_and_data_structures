# author Kristina Alekseyenko

from convert_number import convert_from_decimal


def encode_serie(input):
    res = ''
    asciis = str_to_ascii(input)
    binaries = ascii_to_binary(asciis)
    temp = binaries[0]
    count = 0
    for i in binaries:
        if i == temp:
            count += 1
        else:
            res += str(count)
            temp = i
            count = 1
    res += str(count)
    return res


def str_to_ascii(input):
    res = []
    for symb in input:
        res.append(ord(symb))
    return res


def ascii_to_binary(input):
    res = ''
    res_bin = ''
    zeroes = 0
    for num in input:
        res_bin += convert_from_decimal(num, 2)
        while zeroes < (8-len(res_bin)):
            res += '0'
            zeroes += 1
        res += res_bin
        res_bin, zeroes = '', 0
    return res


def decimalTo8Binary(num):
    res = ''
    if num > 1:
        decimalTo8Binary(num // 2)
        res += str(num % 2)
    return res

