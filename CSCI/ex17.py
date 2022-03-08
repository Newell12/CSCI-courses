def triple_sum(num_lst):
    count = 0
    for i in range(len(num_lst)):
        for f in range(i+1, len(num_lst)):
            for j in range(f+1, len(num_lst)):
                if (num_lst[i]+num_lst[f]+num_lst[j])==13:
                    print(num_lst[i], num_lst[f], num_lst[j])
                    count+=1
    return count
