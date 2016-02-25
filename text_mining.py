""" For the text mining project. Finds the 10 most common words over 5 letters
    in two texts, and returns respective dictionaries with those words and the
    number of occurances. Then returns a list the longest words in common.

    @author Elizabeth Sundsmo 2/25/16
"""
import pickle
import string
from operator import itemgetter #, attrgetter

# Load data from a file (will be part of your data processing script)
input_file = open('phoenix_and_carpet_texts.pickle','r')
reloaded_copy_of_phoenix_texts = pickle.load(input_file)

# Load data from a file (will be part of your data processing script)
input_file = open('nature_myths_texts.pickle','r')
reloaded_copy_of_nature_texts = pickle.load(input_file)


def obtain_text():
    """ DO NOT RUN THIS FUNCTION WITHIN THIS SCRIPT-- TERMINAL PYTHON.

        THIS FUNCTION IS RUN ONLY TO OBTAIN NEW TEXTS; MODIFY CONTENTS.
        Pulls text from specified source and saves it to computer with 
        specified name for future use.
    """
    pass

def create_dict(text):
    """ REFERENCES FILES CREATED IN obtain_text(); MODIFY CONTENTS.
        Given a text string, copies all words into a list, then all the words 
        from the text into a dictionary, and increments respective key values 
        to track word occurances.
    """
    #On/Off case sensitivity
    text = text.lower() 

    #handy one liner that splits words apart via whitespace, and 
    #removes punctuation. Results in list of words.
    word_list = [s.strip(string.punctuation) for s in text.split()]
    
    d = dict()
    for word in word_list:
        d[word] = d.get(word, 0) +1
    return d

    
def most_common(dictionary, w_len, d_len):
    """ Returns a list of the most common words, minimum word length
        and maximum list length specified by function input.
    """
    occurance_ranking = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
    
    long_common = []
    for w, o in occurance_ranking:
        if len(w) >= w_len:
            long_common.append([w, o])

    if len(long_common) <= d_len:
        return long_common
    else:
        return long_common[:d_len]


def shared_words(d1, d2):
    """ Given two dictionaries, returns a list of words the dictionaries have 
        common, sorted by length. 
    """
    shared_keys = []
    d1_keys= d1.keys()
    i=0
    while i < len(d1):
        if d1_keys[i] in d2.keys():
            shared_keys.append(d1_keys[i])
        i+=1

    sorted_shared = sorted(shared_keys, key = len, reverse=True)

    if len(sorted_shared) > 20 :
        return sorted_shared[:20]
    return sorted_shared[0:]

def analyze_text():
    """ Uses above functions to compare two texts: returns dictionaries of
        the most commonly occuring words, as well as the longest words in 
        common.
    """

    text1 = create_dict(reloaded_copy_of_phoenix_texts[1700:len(reloaded_copy_of_phoenix_texts)-18770])
    text2 = create_dict(reloaded_copy_of_nature_texts[6222:len(reloaded_copy_of_nature_texts)-18770])

    common_words_text1 = most_common(text1, 7, 10)
    common_words_text2 = most_common(text2, 7, 10)

    shared=shared_words(text1, text2)

    print 'Common words in text 1: ' +str(common_words_text1)
    print 'Common words in text 2: ' + str(common_words_text2)
    print 'Long shared words: '+ str(shared[0:])


analyze_text()