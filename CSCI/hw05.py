def pair_sum(num_list,target):
    '''
    Purpose: To return a count of the number of pairs of distinct numbers from a list that sum to the given target
    Parameter(s):
        num_list: The provided list of numbers to be checked for pairs
        target: The provided integer to be checking for pairs that sum to
    Return Value: The count of the total amount of distinct pairs that sum to the given target
    '''
    count=0
    for i in range(len(num_list)):
        for f in range(i+1, len(num_list)):
            if num_list[i]+num_list[f]==target :
                count+=1
    return count

def similarity_measure(survey1, survey2):
    '''
    Purpose: To determine the percentage of positions in two lists that are exact matches
    Parameter(s):
        survey1: The first list of integers to be compared
        survey2: The second list of integers to be compared
    Return Value: The percentage of positions in survey1 and survey2 that are exact matches
    '''
    count = 0.0
    percent = 0.0
    if len(survey1)==len(survey2):
        for i in range(len(survey1)):
            if survey1[i]==survey2[i]:
                count+=1
        if count!=0.0:
            percent = count/len(survey1)
    return percent

def similarity_report(survey_list, threshold):
    '''
    Purpose: To return a list containing all pairs of surveys from list survey_list whose similarity measure is above the given threshold
    Parameter(s):
        survey_list: A list containing survey lists to be compared
        threshold: An indicated similarity measure for the lists to be measured by
    Return Value: A list of the pairs of surveys whose similarity measure is above the given threshold
    '''
    pairs = []
    for i in range(len(survey_list)):
        for f in range(i+1, len(survey_list)):
            if similarity_measure(survey_list[i], survey_list[f])>threshold :
                pairs.append([survey_list[i], survey_list[f]])
    return pairs
