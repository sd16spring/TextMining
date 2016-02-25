# Saves Alice in Wonderland and Through the Looking Glass as text files and pickles files


# Required Imports
from pattern.web import *
import pickle
import re, math
from collections import Counter

def pickle_simple_text(text_file_name, pickle_file_name):
    """
    Saving a simple text file as a pickle file to use as a text case
    """

    f2 = open(text_file_name, 'r')
    s2 = f2.read()
    f2.close()

    word_dictionary = {}
    for words in s2.split():
        word_dictionary[words] = word_dictionary.get(words, 0) + 1 # stores the number of times each word is used
    # print word_dictionary

    # pickling the text file
    pickle_file = open(pickle_file_name, 'w')
    name = pickle.dumps(word_dictionary)
    pickle_file.write(name)
    pickle_file.close()

    input_file = open(pickle_file_name, 'r') # saving and naming pickled file 
    sh4 = input_file.read()
    input_file.close
    pickled_file_name = pickle.loads(sh4)

# print(pickle_simple_text('pickle_test.txt', 'hopefully_pickled.txt'))

def pickle_url(url, text_file_name, pickle_file_name):
    """
    Given a url as an input, this function makes two files: a text file and a pickle file

    If an error occurs the website might be blocking the code

    """
    # Downloading and Saving text into a file
    url_text = URL(url).download() # downloads plain text from url
    f = open(text_file_name, 'w') # saves into a text file
    f.write(url_text)
    f.close

    f2 = open(text_file_name, 'r')
    s2 = f2.read()
    f2.close()

    word_dictionary = {}
    for words in s2.split():
        word_dictionary[words] = word_dictionary.get(words, 0) + 1 # stores the number of times each word is used
    # print word_dictionary

    # pickling the text file
    pickle_file = open(pickle_file_name, 'w')
    name = pickle.dumps(word_dictionary)
    pickle_file.write(name)
    pickle_file.close()

    input_file = open(pickle_file_name, 'r') # saving and naming pickled file 
    sh4 = input_file.read()
    input_file.close
    pickled_file_name = pickle.loads(sh4)


#print(pickle_url("http://www.gutenberg.org/cache/epub/51247/pg51247.txt", 'test.txt', 'pickle_test.txt'))
#print(pickle_url("http://www.gutenberg.org/cache/epub/19033/pg19033.txt", 'alice1.txt', 'pickle_alice1.txt'))
#print(pickle_url('http://www.gutenberg.lib.md.us/1/12/12.txt', 'glass.txt', 'pickle_glass.txt'))

def count_pronouns(pickle_file, search_word_list):
    """
    given a pickle file and a list of words (in this case pronouns), this function finds the number of times each word appears in the list 
    and encapsulates the word and the number of time it appears in a tuple. 

    >>> count_pronouns('hopefully_pickled.txt', ['I', 'we', 'us', 'our', 'me', 'a', 'an', 'he', 'she', 'they', 'it', 'you'])
    [('I', 1), ('we', 0), ('us', 0), ('our', 0), ('me', 0), ('a', 0), ('an', 0), ('he', 0), ('she', 0), ('they', 0), ('it', 2), ('you', 0)]

    """
    final_word_list = [] # defines an empty list that will be appended with tuples
    var = pickle.load(open(pickle_file,'r')) # gives a variable name to the information in the pickle file

    for word in search_word_list: # loops through each word in the search_word_list and records the word and number of times in a tuple that gets added to final_word_list
        try:
            tup = (word, var[word])
            final_word_list.append(tup)
        except: # if the word is not in the pickle file, it gets a zero (prevents an error from appearing)
            tup = (word, 0)
            final_word_list.append(tup)
    return final_word_list

# print(count_pronouns('pickle_glass.txt', ['I', 'we', 'us', 'our', 'me', 'a', 'an', 'he', 'she', 'they', 'it', 'you']))
# print(count_pronouns('pickle_alice1.txt', ['I', 'we', 'us', 'our', 'me', 'a', 'an', 'he', 'she', 'they', 'it', 'you']))
# print(count_pronouns('hopefully_pickled.txt', ['I', 'we', 'us', 'our', 'me', 'a', 'an', 'he', 'she', 'they', 'it', 'you']))


def count_emotion_words(pickle_file, positive_words, negative_words):
    """
    Counts the number of a random list of emotion words in a given pickle file. Sorts into two tuple: positive words and negative words

    >>> count_emotion_words('hopefully_pickled.txt', ['great', 'love', 'open', 'live', 'good', 'beautiful', 'nice', 'happy'], ['angry', 'mean', 'confused', 'helpless', 'ugly', 'afraid', 'hurt', 'unpleasant'])
    [('positive words', 0), ('negative words', 0)]

    Since I made this pickle file purposely simple, I can easily count the words and verify that this result is correct.
    """

    positive_count = 0
    negative_count = 0

    var = pickle.load(open(pickle_file,'r')) # gives a variable name to the information in the pickle file

    for word in positive_words:
        try:
            positive_count += var[word]
        except: # if the word is not in the pickle file, it gets a zero (prevents an error from appearing)
            positive_count += 0
    positive_tuple = ('positive words', positive_count)

    for word in negative_words:
        try:
            negative_count += var[word]
        except: # if the word is not in the pickle file, it gets a zero (prevents an error from appearing)
            negative_count += 0
    negative_tuple = ('negative words', negative_count)

    combined_list = [positive_tuple, negative_tuple]
    return combined_list


# print(count_emotion_words('pickle_glass.txt', ['great', 'love', 'open', 'live', 'good', 'beautiful', 'nice', 'happy'], ['angry', 'mean', 'confused', 'helpless', 'ugly', 'afraid', 'hurt', 'unpleasant']))
# print(count_emotion_words('pickle_alice1.txt', ['great', 'love', 'open', 'live', 'good', 'beautiful', 'nice', 'happy'], ['angry', 'mean', 'confused', 'helpless', 'ugly', 'afraid', 'hurt', 'unpleasant']))
# print(count_emotion_words('hopefully_pickled.txt', ['great', 'love', 'open', 'live', 'good', 'beautiful', 'nice', 'happy'], ['angry', 'mean', 'confused', 'helpless', 'ugly', 'afraid', 'hurt', 'unpleasant']))

def total_words(pickle_file):
    """
    calculates the total number of words in a file

    >>> total_words('hopefully_pickled')
    17

    Since I pickled my own simple text file, I can count the words and know that this answer is correct.
    """
    word_count = 0
    file1 = pickle.load(open(pickle_file,'r'))
    for word in file1:
        word_count += file1[word] # loops through each words and adds the number associated with that word to word_count
    return word_count

# print(total_words('pickle_glass.txt'))
# print(total_words('pickle_alice1.txt'))
# print(total_words('hopefully_pickled.txt'))

def cosine_similarity(text_file1, text_file2):
    """
    returns the cosine similarity between two text files

    >>> cosine_similarity('glass.txt', 'pickle_test.txt')
    0.0417587356569

    With the random pickled text file, I can logically test the acuracy of the cosine similarity function. 
    The chance of the author using similar language is high, giving a high cosine similarity value.
    The chance of a random series of words and Through the looking glass being similar are very low--verifing the function
    """

    # makes the two texts into varibales, then strings
    first_text = open(text_file1,'r')
    first_text_string = first_text.read()
    second_text = open(text_file2, 'r')
    second_text_string = second_text.read()

    # Stores the strings in to another variable
    text = [first_text_string, second_text_string]

    #Splits the strings into a list of words
    first_list = text[0].split(' ')
    second_list = text[1].split(' ')

    # Makes the lists of words into vectors and stores the vectors into a variable
    first_vector = Counter(first_list) #histogram - occurances of words
    second_vector = Counter(second_list)
    vector = [first_vector, second_vector]

    # calculates the cosine similarity 
    shared_words = set(vector[0].keys()) & set(vector[1].keys())
    numerator = sum([vector[0][x] * vector[1][x] for x in shared_words])
    sum1 = sum([vector[0][x]**2 for x in vector[0].keys()])
    sum2 = sum([vector[1][x]**2 for x in vector[1].keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# print(cosine_similarity('glass.txt', 'alice1.txt'))
# print(cosine_similarity('glass.txt', 'pickle_test.txt'))