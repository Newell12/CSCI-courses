def donut_costs(num_donuts, membership):
    '''
    Purpose: To calculate the total cost of a customers order using provided information.
    Parameters:
        num_donuts: the integer value of donuts the customer is purchasing
        membership: a boolean value describing wether it is true that the customer is a member or false that they are a member.
    Return Value: Returns the total cost of the customer's order
    '''
    if num_donuts<=6 :
        if membership== True :
            return num_donuts*1.8
        elif membership== False :
            return num_donuts*2.0
    elif 6<num_donuts<13 :
        if membership== True :
            return num_donuts*1.575
        elif membership== False :
            return num_donuts*1.75
    elif num_donuts>=13 :
        if membership== True :
            return num_donuts*1.35
        elif membership== False :
            return num_donuts*1.5


def choose(text, optionA, optionB, optionC) :
    print(text, "A:", optionA, "B:", optionB, "C:", optionC)
    choice=input("Choose A, B or C", )
    if choice== 'A' :
        return 'A'
    elif choice== 'B' :
        return 'B'
    elif choice== 'C' :
        return 'C'
    else :
        print("Invalid option, defaulting to C")
        return 'C'


def adventure() :
    if choose("Which way1", "Left", "Right", "Straight")=="A" :
        if choose("Which way2", "Left", "Straight", "Straight")=="A" :
            if choose("Which way3", "Straight", "Right", "Left")=="A" :
                return False
            elif choose("Which way3", "Straight", "Right", "Left")=="B" :
                if choose("Which way4", "Straight", "Right", "Straight")=="A" :
                    return True
                elif choose("Which way4", "Straight", "Right", "Straight")=="B" :
                    return False
                elif choose("Which way4", "Straight", "Right", "Straight")=="C" :
                    return True
            elif choose("Which way3", "Straight", "Right", "Left")=="C" :
                return True
        elif choose("Which way2", "Left", "Straight", "Straight")=="B" :
            return True
        elif choose("Which way2", "Left", "Straight", "Straight")=="C" :
                if choose("Which way3", "Straight", "Right", "Left")=="A" :
                    return False
                elif choose("Which way3", "Straight", "Right", "Left")=="B" :
                    if choose("Which way4", "Straight", "Right", "Straight")=="A" :
                        return True
                    elif choose("Which way4", "Straight", "Right", "Straight")=="B" :
                        return False
                    elif choose("Which way4", "Straight", "Right", "Straight")=="C" :
                        return True
                elif choose("Which way3", "Straight", "Right", "Left")=="C" :
                    return True
    elif choose("Which way1", "Left", "Right", "Straight")=="B" :
        if choose("Which way4", "Straight", "Right", "Straight")=="A" :
            return True
        elif choose("Which way4", "Straight", "Right", "Straight")=="B" :
            return False
        elif choose("Which way4", "Straight", "Right", "Straight")=="C" :
            return True
    elif choose("Which way1", "Left", "Right", "Straight")=="C" :
        return False
