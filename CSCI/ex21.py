def csv_to_matrix(filename):
    fp = open(filename, 'r')
    list1 = [' ']
    list2 = []
    lines = fp.read()
    lines = lines.split('\n')
    for i in range(len(lines)):
        list1.append(lines[i].split(','))
    list1.pop(0)
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list1[i][j]=int(list1[i][j])
    return list1
    fp.close()
