def to_indexes(string):
    dict = {}
    for ch in string:
        dict[ch]= []
    for i in range(len(string)):
        dict[string[i]].append(i)
    return dict
