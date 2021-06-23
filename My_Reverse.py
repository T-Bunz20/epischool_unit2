def my_reverse(l):
    output = []
    i = len(l) - 1
    while i > -1:
        output.append(l[i])
        i -= 1
    return output