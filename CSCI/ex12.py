def get_nth(str_list, n):
    choice = str_list[n-1]
    char = choice[n-1]
    str = ''
    for i in range(n):
        str += char
    return str
