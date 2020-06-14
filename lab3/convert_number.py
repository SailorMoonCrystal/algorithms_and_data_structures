# author Kristina Alekseyenko


def convert_to_decimal(number, num_system):
    decimal = 0
    value = "0123456789abcdefghijklmnopqrstuwvxyz"
    for N in number:
        decimal *= num_system
        n = 0
        while N.lower() != value[n]:
            n += 1
        decimal += n
    return decimal


def convert_from_decimal(decimal, num_system):
    number = ""
    value = "0123456789abcdefghijklmnopqrstuwvxyz"
    while decimal > 0:
        n = decimal % num_system
        number = str(value[int(n)])+number
        decimal //= num_system
    return number



