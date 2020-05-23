# author Kristina Alekseyenko


def find_seq(seq, arr):
    seq_index = []
    j, i = 0, 0
    while i <= len(arr)-len(seq):
        while j < len(seq) and arr[i] == seq[j]:
            i, j = i+1, j+1
            if j == len(seq):
                seq_index.append(i-len(seq))
                i, j = i-1, 0
        i, j = i+1-j, 0
    return seq_index
