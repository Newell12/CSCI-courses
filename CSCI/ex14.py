def shorter_string(left, right):
    list = []
    for i in range(len(left)):
        if len(left[i])< len(right[i]):
            list.append(left[i])
        elif len(right[i])< len(left[i]):
            list.append(right[i])
        else:
            list.append('Tie')
    return list
