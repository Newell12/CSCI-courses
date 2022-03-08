def largest():
    max=0
    val=1
    while(val!=0):
        val=int(input("Enter a number: ", ))
        if val>max:
            max=val
    return max
