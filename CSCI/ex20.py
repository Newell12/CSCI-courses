def get_quotes(text):
    store = ''
    newlist = []
    count = 0
    for i in range(len(text)):
        if text[i]=='"' and count==0:
            count+=1
        elif text[i]!='"' and count == 1:
            store += text[i]
        elif text[i]=='"' and count==1:
            count=0
            newlist.append(store)
            store = ''
    return newlist
