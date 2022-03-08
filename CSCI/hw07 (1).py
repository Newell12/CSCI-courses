def complement(strand):
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

def longest_common(first,second):
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

def 
