#TextMining Project: KeyWord Search
#Claire Kincaid
#February 24 2016

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
	keywords_count = []
	all_keywords = dict()
	for i in keywords:
		all_keywords[i] = (word_find(data, i))
	return all_keywords


keywords = ['computer', 'assisted', 'collaborative', 'learning', 'inderdisciplinary', 'shared', 'knowledge']
rawdata = open('data.txt')
datalist = rawdata.readlines()
data = ''
for i in datalist:
	data += i 

print multi_keywords_find(data, keywords)

import doctest
doctest.testmod()