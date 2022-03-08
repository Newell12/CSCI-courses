def capitalize_last(phrase):
    newlist = []
    newphrase = ''
    store = ''
    finalphrase = ''
    newlist = phrase.split()
    for i in range(len(newlist)):
        newlist[i] = newlist[i].lower()
        store = newlist[i][(len(newlist[i])-1):]
        store = store.upper()
        newphrase = newlist[i][:-1]
        newlist[i] = newphrase+store
        finalphrase+=newlist[i]
        if i!=(len(newlist)-1):
            finalphrase+=' '
    return finalphrase
