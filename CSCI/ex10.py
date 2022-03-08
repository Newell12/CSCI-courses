def expo(x,y):
    prod = 1
    i=0
    f=0
    while i<y:
        total = 0
        i+=1
        # print("i", i)
        f=0
        while f<x:
            f+=1
            total += prod
            # print("f", f)
            # print("total", total)
        prod = total
    return prod
