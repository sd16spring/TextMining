#TextMining Project: KeyWord Search
#This script will search through a given paper or papers for the occurences of several keywords
#it will then tell the user the most relevant paper based on the maximum number of occurences of a keyword or keywords
#Claire Kincaid
#April 18, 2016 (revised for MiniProject 5)

import string

def make_data(data):
    """Takes a string, removes all punctuation, makes all letters lowercase and puts words of string into a list
    >>> make_data("I'm hilarious")
    ['im', 'hilarious']
    """
    data = data.lower() #turns all letters in string lowercase
    data = data.translate(None, string.punctuation) #strips all punctuation from string
    listdata = data.split()
    return listdata

def word_count(data):
    """Takes a string, uses make_data to turn it into an analyzable list 
    creates a dictionary that counts all words within that list
    >>> word_count("I'm hilarious")
    {'im': 1, 'hilarious': 1}
    """
    words = dict()
    for word in make_data(data):
        words[word] = words.get(word, 0) + 1
    return words

def word_find(data, keyword):
    """ Takes a string, uses word_count to create dict counting all words in string
    returns frequency of word specified as a keyword
    >>> word_find("I'm hilarious", "hilarious")
    1
    """
    hist = word_count(data)
    return hist.get(keyword, 0)

def multi_keywords_find(data, keywords):
    """ Takes a string data and a list of keywords and returns dict w/ word count of those words
    >>> multi_keywords_find("I'm hilarious", ['im', 'hilarious'])
    {'im': 1, 'hilarious': 1}
    """
    all_keywords = dict()
    for i in keywords:
        all_keywords[i] = (word_find(data, i))
    return all_keywords

def multi_paper_word_find(data, keyword):
    """takes string keyword, uses word_find to find the occurences of keyword in three datasets in a list
    returns dictionary of papers in order of highest occurences of word to lowest"""
    data_keyword = dict()
    for i in data:
        data_keyword[i] = word_find(i, keyword)
    return data_keyword

def relevance(data, keyword):
    data_keyword = multi_paper_word_find(data, keyword)
    most_relevant = max(data_keyword.get(data1, 0), data_keyword.get(data2, 0), data_keyword.get(data3, 0))
    return most_relevant


keywords = ['computer', 'assisted', 'collaborative', 'learning', 'inderdisciplinary', 'shared', 'knowledge']

rawdata1 = open('data.txt')
datalist1 = rawdata1.readlines()
data1 = ''
for i in datalist1:
    data1 += i 

rawdata2 = open('data2.txt')
datalist2 = rawdata2.readlines()
data2 = ''
for i in datalist2:
	data2 += i

rawdata3 = open('data3.txt')
datalist3 = rawdata3.readlines()
data3 = ''
for i in datalist3:
	data3 += i

data = [data1, data2, data3]

print multi_keywords_find(data1, keywords)
print relevance(data, keywords[1]

import doctest
doctest.testmod()