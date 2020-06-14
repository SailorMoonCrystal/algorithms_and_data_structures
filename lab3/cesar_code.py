# author Kristina Alekseyenko

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(input, shift):
    result = ''
    for symb in input:
        if isLower(symb):
            result += alpha[(alpha.index(symb)+shift) % 26]
        elif isUpper(symb):
            result += alpha[(alpha.index(symb)+shift) % 26 + 26]
        else:
            result += symb
    return result


def decode(input, shift):
    return encode(input, -shift)


def isAlpha(symb):
    return symb in alpha


def isLower(symb):
    return isAlpha(symb) and alpha.index(symb) < 26


def isUpper(symb):
    return isAlpha(symb) and not isLower(symb)


