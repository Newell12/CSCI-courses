def collatz(n):
    sum = 0
    if n == 1:
        sum +=n
        return sum
    elif n % 2 != 0:
        sum+=n
        print(n)
        n = n*3+1
        sum += collatz(n)
        return sum
    elif n % 2 == 0:
        sum+=n
        print(n)
        n = n//2
        sum+=collatz(n)
        return sum
    return sum

def remove(alist):
    string = ''
    if len(alist)==0:
        alist = alist
        return string
    else:
        if alist[-1]>0:
            string += str(alist[-1])+' '
            alist = alist[0:-1]
        else:
            alist = alist[0:-1]
        string+=remove(alist)
        return string

def palindrome(pal):
    if len(pal)<=1:
        return True
    return pal[0]==pal[len(pal)-1] and palindrome(pal[1:len(pal)-1])

def is_pos_reversible(alist):
    string1 = remove(alist)
    print(string1)
    list1 = string1.split(' ')
    list1 = list1[0:-1]
    print(list1)
    return palindrome(list1)


def all_subsets(items):
    new_list = []
    if len(items) == 0:
        return new_list
    else :
        new_list = []
        sub_list = all_subsets(items[0:-1])
        new_list+=sub_list
        new_list.append([items[-1]])
        for i in range(len(sub_list)):
            # print(sub_list[i])
            # print(items[-1])
            new_list.append(sub_list[i]+[items[-1]])
        return new_list
    return new_listS
