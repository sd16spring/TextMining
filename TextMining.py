"""
Finds the relevant words associated with the main motifs in the novel

@author: Kevin Guo
"""
from pattern.en import *
import matplotlib.pyplot as plt
import pickle
import re
from pattern.web import *
import nltk
from nltk.corpus import wordnet as wn
import numpy as np


def pickle_files(text):
    """
    Pickle all files
    """
    for i in range(5):
        name = 'pickle' + str(i) + '.txt'
        pickle.dump(text,open(name,'w'))

def create_dictionary(words):
    """
    Create a dictionary given a list of words
    
    >>> create_dictionary(['bug','bug','chess'])
    {'bug': 2, 'chess': 1}
    """
    #initialize dictionary
    dictionary = dict()

    #creates a histogram of words given
    for word in words:
        if(word not in dictionary):
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    return dictionary

def read_main_dictionary():
    """
    Create and modify dictionary for the main text to remove words that are implausible matches
    """    
    #read file
    a = open("Text1.txt")
    #make all characters in file lowercase
    book = a.read().lower()
    a.close()
    #remove all characters that are not alphabetical
    book = re.sub('[^a-z]', ' ', book)
    words = book.split()
    #histogram for main dictionary
    dictionary = create_dictionary(words)
    #modify dictionary by frequency of words
    threshold(dictionary,.02,.002)
    return dictionary

def create_dictionary_list():
    """
    Create dictionaries for other texts by the same author
    """
    #open text files
    b = open("Text2.txt")
    c = open("Text3.txt")
    d = open("Text4.txt")
    e = open("Text5.txt")

    #move texts into histogram
    book2 = b.read().lower()
    b.close()
    book2 = re.sub('[^a-z]', ' ', book2)
    words2 = book2.split()
    dictionary2 = create_dictionary(words2)

    book3 = c.read().lower()
    c.close()
    book3 = re.sub('[^a-z]', ' ', book3)
    words3 = book3.split()
    dictionary3= create_dictionary(words3)

    book4 = d.read().lower()
    d.close()
    book4 = re.sub('[^a-z]', ' ', book4)
    words4 = book4.split()
    dictionary4 = create_dictionary(words4)

    book5 = e.read().lower()
    e.close()
    book5 = re.sub('[^a-z]', ' ', book5)
    words5 = book5.split()
    dictionary5= create_dictionary(words5)

    return [dictionary2, dictionary3, dictionary4, dictionary5]

def threshold(dictionary,upper_threshold_percent,lower_threshold_percent):
    """
    Remove entries from the dictionary that have a frequency which is not within the desired range
    """
    length = len(dictionary)
    #convert percentages to numerical threshold
    upper_threshold = upper_threshold_percent*length
    lower_threshold = lower_threshold_percent*length
    #remove entries that are not in the range
    for x,y in dictionary.items():
        if y > upper_threshold or y <= lower_threshold:
            del(dictionary[x])

def alphabetical(dictionary):
    """
    Returns list of most common words in alphabetical order
    """
    #create empty list
    lst = []
    #inputs keys of dictionary into a list
    for x,y in dictionary.items():
        lst.append(x)
    #sort list by alphabetical order
    lst.sort()
    return lst

def most_common(dictionary):
    """
    Returns list of most common words sorted by frequency
    """
    #create empty tuple
    tupl = []
    #reverses dictionary inside a tuple
    for x,y in dictionary.items():
        tupl.append((y,x))
    #sort tuple by frequency of words
    tupl.sort()
    
    lst = []
    #create a list sorted by frequency of words
    for x,y in tupl:
        lst.append(y)
    return lst

def subtract_dictionaries(threshold):
    """
    Removes an entry from the main dictionary if the number of appearances of that word is relatively the same as 
    the number of appearances in other books (this would identify which words are commonly used by the author
    compared to those which are actually significant)

    Receives a threshold that indicates significance of word required to remain in dictionary.
    """
    #creates list of dictionaries of words in other books
    dictionary_list = create_dictionary_list()
    #creates dictionary for somewhat filtered words in main book
    main_dictionary = read_main_dictionary()

    #iterate through each book in the list of books
    for i in range(len(dictionary_list)):
        for word,freq in dictionary_list[i].items():
            for x,y in main_dictionary.items():
                #test if the frequency of each word in the main text is significant relative to the frequency of that word in other texts
                if(x == word and float(y)/freq < threshold):
                    #remove insignificant words
                    del main_dictionary[x]

    return main_dictionary

def motif_sentiment(lst):
    """
    Unused code which returns sentiments of individual words
    """
    sentiment_dictionary = dict()
    for word in lst:
        sentiment_dictionary[word] = sentiment(word)
    return sentiment_dictionary

def plot_texts(dictionary):
    """
    Plots the words in a bar graph in order of frequency for easier visualization
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ## the data
    N = len(dictionary)
    tup = []
    lstx = []
    lsty = []

    #sort words by frequency
    for x,y in dictionary.items():
        tup.append((y,x))
    tup.sort(reverse=True)

    for y,x in tup:
        lstx.append(x)
        lsty.append(y)

    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.35                     # the width of the bars

    ## the bars
    rects1 = ax.bar(ind, lsty, width, color='blue')
    # # axes and labels
    ax.set_xlim(-width,len(ind)+width)
    ax.set_ylim(0,200)
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of most common themes')
    ax.set_xticks(ind+width)
    xtickNames = ax.set_xticklabels(lstx)
    plt.setp(xtickNames, rotation=90, fontsize=8)

    plt.show()

if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    motifs =  subtract_dictionaries(1.0)
    plot_texts(motifs)
    # print motif_sentiment(motifs)
    # word = wn.synset('beer.n.01')
    # print word.hypernyms()

    # print sentiment(motifs)
    # plot_texts(motifs)
    # print alphabetical(subtract_dictionaries(1.0))


    #Test code for natural language processing
    # a = alphabetical(subtract_dictionaries(1.0))
    # print a
    # text = nltk.Text(a)
    # text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    # print text


    # temp = dict()
    # for i in range(len(a)):
    #     for j in range(len(a)-i):
    #         if(text.similar(dict[i])
    # print text.similar('gold')