def awesome(val) :
    '''
    Purpose: To determine if a number is awesome which is defined as not being divisible by any two digit integer
    Parameter(s):
        val: provides the number to be checked
    Return Value: Returns True if the number is not divisible by any two digit integer and False if it is
    '''
    for i in range(10,100):
        #print(i)
        if val%i==0 :
            return False
    return True

def count_awesome(low, high):
    '''
    Purpose: To determine the amount of awesome(numbers not divisible by any two digit integer) numbers between two provided numbers being low and high inclusive
    Parameter(s):
        low: the bottom number of the range to be checked
        high: the top number of the range to be checked
    Return Value: Returns the amount of awesome(numbers not divisible by any two digit integer) within the provided range
    '''
    count = 0
    if low>high:
        return 0
    for i in range(low, high+1):
        if awesome(i)==True :
            count+=1
    return count

def rps_round(comp_move) :
    '''
    Purpose: To run a singular round of rock, paper, scissors first prompting the user to enter a choice then deciding what that move results in
    Parameter(s):
        comp_move: the move that the computer has chosen being either R, P or S
    Return Value: Returns the result of the round being C if the computer wins, P if the player wins and T in the result of a tie
    '''
    choice = input("Enter R, P or S: ", )
    while(choice!='R' and choice!='P' and choice!='S'):
        print("Invalid Move")
        choice = input("Enter R, P or S: ", )
    print("Computer selects ", comp_move)
    if(comp_move=='R' and choice=='S') or (comp_move=='P' and choice=='R') or (comp_move=='S' and choice=='P'):
        print('Computer Wins!')
        return 'C'
    elif(comp_move=='S' and choice=='R') or (comp_move=='R' and choice=='P') or (comp_move=='P' and choice=='S'):
        print('Player Wins!')
        return 'P'
    else :
        print('Tie!')
        return 'T'

def rps_game():
    '''
    Purpose: To simulate continuous rounds of rock, paper, scissors until the player wins three consecutive rounds
    Parameter(s):
        None
    Return Value: Returns the amount of rounds it took for the player to win three consecutive rounds
    '''
    wins=0
    rounds=1
    amount = 1
    total_rounds = 0
    while(wins<3):
        if rounds==1 :
            if rps_round('R')=='P' :
                wins+=1
                # print('hi1')
            else:
                # print('here1')
                wins=0
            rounds+=1
            total_rounds=((amount-1)*3)+rounds
            print('Rounds:', total_rounds-1, "- Consecutive Wins: ", wins)
        elif rounds==2 :
            if rps_round('P')=='P' :
                wins+=1
                # print('hi1')
            else:
                # print('here1')
                wins=0
            rounds+=1
            total_rounds=((amount-1)*3)+rounds
            print('Rounds:', total_rounds-1, "- Consecutive Wins: ", wins)
        elif rounds==3:
            if rps_round('S')=='P' :
                wins+=1
                # print('hi1')
            else:
                # print('here1')
                wins=0
            total_rounds=((amount-1)*3)+rounds
            print('Rounds:', total_rounds, "- Consecutive Wins: ", wins)
            amount+=1
            rounds=1
    if amount==2 and (rounds==1 or rounds==2) :
        return total_rounds
    return total_rounds-1
    
