# author Kristina Alekseyenko

#Porównuje dlugosc dwoch ciagow znakow
def compare(str1, str2):
    if len(str1) > len(str2):
        return True
    elif len(str1) < len(str2):
        return False
    else:  #Jesli dlugosc jest taka sama, porównuje alfabetycznie
        return str1 > str2 
