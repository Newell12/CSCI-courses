def mystery(num_ls):
    diff = 0
    for x in num_ls:
        for y in num_ls:
            if (x-y) > diff:
                diff = x-y
    return diff

def mystery2(num_ls):
    num_ls.sort()
    diff = num_ls[1]-num_ls[0]
    minel = num_ls[0]
    for i in range(1, len(num_ls)):
        if num_ls[i]<minel:
            minel = num_ls[i]
        if num_ls[i]-minel > diff:
            diff = num_ls[i]-minel
    return diff
