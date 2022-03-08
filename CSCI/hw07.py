def complement(strand):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    compstrand = ''
    for i in range(len(strand)):
        if strand[i]=='A':
            compstrand+='T'
        elif strand[i]=='T':
            compstrand+='A'
        elif strand[i]=='C':
            compstrand+='G'
        elif strand[i]=='G':
            compstrand+='C'
    return compstrand
    #TODO - Fill out the documentation and write this function


def longest_common(first, second):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    longest = ''
    length = 0
    for i in range(len(first)):
        for j in range(i,len(first)):
            # print(first[i:j+1])
            if first[i:j+1] in second:
                if len(first[i:j+1])>length:
                    longest = first[i:j+1]
                    length = len(first[i:j+1])
    return longest
    #TODO - Fill out the documentation and write this function


def spam_score(spam_file, not_file, word):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    spamcount=0
    not_spamcount=0
    seperate = []
    fp_spam = open(spam_file)
    spam = fp_spam.readlines()
    spam = [line.strip() for line in spam]
    fp_spam.close()
    fp_not = open(not_file)
    not_spam = fp_not.readlines()
    not_spam = [line.strip() for line in not_spam]
    fp_not.close()
    word = word.lower()
    for i in range(len(spam)):
        spam[i]=spam[i].lower()
        seperate = spam[i].split()
        for j in range(len(seperate)):
            if seperate[j]==word:
                spamcount+=1
    for i in range(len(not_spam)):
        not_spam[i]=not_spam[i].lower()
        seperate = not_spam[i].split()
        for j in range(len(seperate)):
            if seperate[j]==word:
                not_spamcount+=1
    return spamcount-not_spamcount
    #TODO - Fill out the documentation and finish this function


def spam_check(spam_file, not_file, email):
    '''
    Purpose:
    Parameter(s):
    Return Value:
    '''
    score=0
    seperate= []
    seperate = email.split()
    print(seperate)
    for i in range(len(seperate)):
        print(seperate[i].lower())
        print(spam_score(spam_file,not_file,seperate[i].lower()))
        score+=spam_score(spam_file,not_file,seperate[i].lower())
        # print(score)
    if score>0:
        return True
    else:
        return False

    #TODO - Fill out the documentation and write this function
