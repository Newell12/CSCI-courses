def div37(start,stop):
    list = []
    if start > stop:
        return list
    if start <= stop and start % 3 == 0 or start % 7 == 0:
        list.append(start)
        print(start)
        list += div37(start+1, stop)
        return list
    elif start <= stop:
        print(start)
        list+= div37(start+1, stop)
        return list
    else:
        return list
