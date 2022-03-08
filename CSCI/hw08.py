def count_votes(csvfile,candidate):
    try:
        fp = open(csvfile,'r')
        count1 = 0
        count2 = 0
        count3 = 0
        storage = []
        fp.readline()
        for line in fp:
            storage = line.split(',')
            storage[3]= storage[3].replace('\n','')
            if storage[1]==candidate:
                count1+=1
            elif storage[2]==candidate:
                count2+=1
            elif storage[3]==candidate:
                count3+=1
        return [count1,count2,count3]
        fp.close()
    except FileNotFoundError:
        return 'None'

def remove_candidate(csvfilein, csvfileout, candidate):
    fp = open(csvfilein,'r')
    fp2 = open(csvfileout, 'w')
    count = 0
    storage = []
    storagestring = ''
    storagestring2 = ''
    storagelist2 = []
    for line in fp:
        storage = line.split(',')
        # print(storage)
        if len(storage)==4:
            storage[3]= storage[3].replace('\n','')
        if len(storage)>=2:
            if storage[1]==candidate:
                storage[1]= ''
                count+=1
                # print(count)
        if len(storage)>=3:
            # print('Troy')
            if storage[2]==candidate:
                storage[2]=''
                count+=1
                # print(count)
        if len(storage)==4:
            if storage[3]==candidate:
                storage[3]= ''
                count+=1
                # print(count)
        for i in range(len(storage)):
            if i<(len(storage)-1):
                storagestring +=storage[i]+','
            else:
                storagestring += storage[i]+'\n'
        storagelist2 = storagestring.split(',')
        print(storagelist2)
        for i in range(len(storagelist2)):
            if storagelist2[i]!='' and i!=(len(storagelist2)-1):
                storagestring2+=storagelist2[i]+','
            elif storagelist2[i]!='':
                storagestring2+=storagelist2[i]
        # print(storagestring)
        # storagestring2.replace('\n','')
        print(storagestring2)
        fp2.write(storagestring)
        storagestring2 = ''
        storagestring = ''
    fp.close()
    fp2.close()
    return count

def ranked_choice_full(csvfile, candidate_list):
    winner = ''
    count = 1
    new_name = csvfile
    old_new_name = csvfile
    length = len(candidate_list)
    while(count <length):
        fp = open(new_name,'r')
        fullfile = fp.read()
        fullfilelist = fullfile.split('\n')
        totalvotes = len(fullfilelist)-2
        fiftypercent= totalvotes//2
        # print(fiftypercent)
        mincount = 100000000000
        minname = ''
        storagelist = []
        for i in range(len(candidate_list)):
            storagelist = count_votes(csvfile,candidate_list[i])
            # print(storagelist[0])
            if storagelist[0]>=fiftypercent:
                return candidate_list[i]
            elif storagelist[0]<mincount:
                mincount = storagelist[0]
                minname = candidate_list[i]
        old_new_name = new_name
        new_name = 'round'+str(count)+'_' + csvfile
        count+=1
        # print(count)
        # print(minname)
        spot = candidate_list.index(minname)
        candidate_list.remove(minname)
        # print(candidate_list)
        fp.close()
        # print(new_name)
        remove_candidate(old_new_name, new_name, minname)
