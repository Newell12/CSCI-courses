def sum_common(list1,list2):
    count = 0
    if len(list1)==0:
        return count
    elif list1[0] in list2:
        count +=list1[0]
        list1.pop(0)
        return count + sum_common(list1,list2)
    else:
        list1.pop(0)
        return count + sum_common(list1,list2)
