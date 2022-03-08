def nested_double(nested_list):
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            nested_list[i][j] = (nested_list[i][j]*2)
    return nested_list
