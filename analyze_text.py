"""
This code is meant to compare two adventure stories, The Wizard of Oz and
The Adventures of Robin Hood.

As a form of comparison, this code prints a list of the top ten words and
the number of times they occur  for each text and a list of the top twenty 
longest shared words.

The input is .pickle files of the author's works, obtained through
get_text.py

The output is three lists: most common words in Wizard, most common words in
Robin Hood, and longest shared words.

@AUTHOR: REBECCA PATTERSON 02-25-16

"""
#import packages that are used
import pickle
import string

#first load the data files with the texts
input_file = open('wizard_of_oz_text.pickle','r')
copy_of_wizard_texts = pickle.load(input_file)
input_file = open('robin_hood_text.pickle','r')
copy_of_robin_hood_texts = pickle.load(input_file)

def create_dictionary(text):
    """ Creates a dictionary of words and their number of occurances
    for each text.

    input: string of text
    output: dictionary. key=word, value= word count

    The string of text is converted into a list of individual words.
    These words are then added to a dictionary where the key is the 
    word and the value is the number of occurances of that word.
    """
    #create list of words in string
    text_list = [x.strip(string.punctuation) for x in text.split()]
    #standardize words by making all lower case
    word_list=[]
    i=0
    while i<len(text_list):
        word= text_list[i]
        word_lower= word.lower()
        word_list.append(word_lower)
        i+=1   
    #make empty dictionary, fill with key=word, value=word count
    d= dict()
    for word in word_list:
        d[word]= d.get(word, 0)+1
    return d         

def top_ten(dictionary):
    """
    input: a dictionary with words for keys and would count for values

    output: a list containing 10 key/value pairs with the highest values
    and key length >4 from the input dictionary
    """
    #list with count before the word for elements in dictionary with word
    #longer than 4 letters
    word_count= []
    for word in dictionary:
        if len(word)>4:
            word_count.append((dictionary[word], word))

    #sort list in order of decreasing value
    word_count.sort(reverse=True)

    #rewrite with word before count
    word_first= []
    for count, word in word_count:
        word_first.append((word, count))

    #create list of top ten occuring words
    top= word_first[0:10]   

    return top

def common_words(dictionary1, dictionary2):
    """
    input: two dictionaries

    output: a list of the twenty longest words that the dictionaries have
    in common
    """
    #create empty lists
    words1= []
    words2= []
    common= []
    #make lists or words from each dictionary
    for word in dictionary1:
        words1.append(word)
    for word in dictionary2:
        words2.append(word)
    #make a list of all words shared in two lists
    i=0
    while i<len(words1):
        if words1[i] in words2:
            common.append(words1[i])
            i+=1
        else:
            i+=1
    #sort in decreasing order of length
    longest= sorted(common, key=len, reverse=True)
    most_common= longest[0:20]
    return most_common

def compare_books(text1, text2):
    """ Compares the two chosen texts.

    input: the texts from the data files
    output: two dictionaries and a text_list,

    """
    wizard_dict= create_dictionary(text1)
    robin_hood_dict= create_dictionary(text2)

    wizard_top= top_ten(wizard_dict)
    robin_hood_top= top_ten(robin_hood_dict)

    shared_words= common_words(wizard_dict, robin_hood_dict)

    print "Top Ten Words in Wizard of Oz "+ str(wizard_top)
    print "Top Ten Words in Robin Hood "+ str(robin_hood_top)
    print "Twenty Longest Shared Words "+ str(shared_words)    

#specified lengths to ignore text from gutenburg
compare_books(copy_of_wizard_texts[519:len(copy_of_wizard_texts)-18748], copy_of_robin_hood_texts[488:len(copy_of_robin_hood_texts)-18769])