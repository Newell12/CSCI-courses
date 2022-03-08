import math
import random
def skein_counts(stitch_counts):
    '''
    Purpose: To return a dictionary with keys being colors of the thread and values being number of skeins needed to complete the project.
    Parameter(s):
        stitch_counts: a dictionary with keys being colors of the thread and values being the number of stitches needed of that color
    Return Value: a dictionary with keys being colors of the thread and values being number of skeins needed to complete the project
    '''
    new_dict = {}
    for key in stitch_counts:
        value = math.ceil(stitch_counts.get(key)/1800)
        # print(value)
        new_dict[key]=value
    return new_dict

def follows(word_list):
    '''
    Purpose: to generate a dictionary with keys being the words in word_list and values being a list of each individual word that directly follows the word that is the key
    Parameter(s):
        word_list: a list of words
    Return Value: a dictionary with keys being the words in word_list and values being a list of each individual word that directly follows the word that is the key
    '''
    new_dict = {}
    for i in range(len(word_list)-1):
        if word_list[i] in new_dict:
            new_dict.get(word_list[i]).append(word_list[i+1])
        else:
            new_dict[word_list[i]]=[word_list[i+1]]
    return new_dict

def autofill(follows_dict,current):
    '''
    Purpose: to suggest a list of words to potentially follow current in a randomly generated sentence
    Parameter(s):
        follows_dict: a dictionary with keys being the words in word_list and values being a list of each individual word that directly follows the word that is the key
        current: a single word
    Return Value: If current word appears in follows_dict then return the list of words that is the value corresponding to the current word key in follows_dict. If current word is not in follows_dict return a list of all the keys in follows_dict.
    '''
    if current in follows_dict:
        return follows_dict.get(current)
    else:
        new_list= []
        for key in follows_dict:
            new_list.append(key)
        return new_list

def random_sentence(fname, length):
    '''
    Purpose: To read in a file and create a random sentence of the given length based on the contents of the file.
    Parameter(s):
        fname: a string containing the name of the file to open.
        length: an integer representing how many words to include in the random sentence
    Return Value: Returns a string containing randomized words based on the file.
    '''
    fp = open(fname,'r')
    file = fp.read()
    file_list = file.split()
    # print(file_list)
    file_dict = follows(file_list)
    start_word = random.choice(file_list)
    sentence = start_word + ' '
    new_word = ''
    for i in range(length-1):
        new_word = random.choice(autofill(file_dict,start_word))
        sentence += new_word + ' '
        start_word = new_word
    return sentence
