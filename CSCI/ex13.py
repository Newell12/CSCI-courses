def collatz(n):
    list = []
    list.append(n)
    while(n!=1):
        if n%2==0 :
            n=n//2
            list.append(n)
        elif n%2==1 :
            n = (n*3)+1
            list.append(n)
    return list
