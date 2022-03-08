def caps_second(fname):
        fp1 = open(fname, 'r')
        newname = 'caps_'+fname
        fp2 = open(newname, 'w')
        file = fp1.read()
        list = []
        list = file.split('\n')
        list[1]= list[1].upper()
        for i in range(len(list)):
            fp2.write(list[i])
            fp2.write('\n')
        fp1.close()
        fp2.close()
