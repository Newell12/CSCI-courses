def countE(str):
    count = 0
    if len(str)==0:
        return count
    elif str[0]=='e':
        count+=1
        return count + countE(str[1:])
    else:
        return count + countE(str[1:])
def min_es2(string_list2):
    new_list = []
    if len(string_list2)==0:
        return new_list
    else:
        new_list.append(countE(string_list2[0]))
        string_list2.pop(0)
        new_list += min_es2(string_list2)
        return new_list
    return new_list

def min_es(string_list):
    print(string_list)
    copy_list = string_list.copy()
    print(string_list)
    new_list2 = min_es2(copy_list)
    print(string_list)
    minimum = min(new_list2)
    print(string_list)
    dex = new_list2.index(minimum)
    print(string_list)
    return string_list[dex]
