# author Kristina Alekseyenko


def read_from_file(file_name):
    result=[]
    with open(file_name, 'r') as f:
        x = f.read().split(",")
    for i in range(0,len(x)):
        result.append(x[i])
    return result
