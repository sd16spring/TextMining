"""
Kevin Zhang, Software Design Spring 2016

My own code used to test histogram algorithms on my twitchchat data. It finds the most common words used on a particular streamer's stream.

Integrated into the code, the analyze function can be done in real-time with each message that is sent on twitch chat.

The sentiment function happens at the end and evaluates the total sentiment polarity of everything that was said on twitch chat during the period
this was run to determine how positive a streamer's messages are, a maybe? indication of a streamer's trolliness/popularity.

In addition, there are a lot of helper functions at the end for sentiment analysis to aid in text visualization and clustering.
"""

import pickle
import numpy as np
from pattern.en import *
import indicoio


indicoio.config.api_key = '79c1863461910aa764b6e9165916ddeb'



global mostcommon       									#dictionary that holds all the words taken from the streamer

mostcommon = {}


def analyze():
	"""
	Finds the top 10 most used words in the chat and prints them out
	Also returns the data used for the visualization
	"""

	file = open("twitchchat","r")

	#realfile = pickle.load(file)							 #pickle failed cuz of unicode problems.

	

	rawlist = []
	rawlist = file.read().split(" ")  						#this is get rid of article and common words.


															#giant list of common words, to be excluded to filter for unique words
	baddictionary = 'much, through, ever, whats, yet, just, well, me, thats, does, still, put, want, im, got, stop, dont, too, should, the, of, and, a, to, in, is, you, that, it, he, was, for, on, are, as, with, his, they, i, at, be, this, have, from, or, one, had, by, word, but, not, what, all, were, we, when, your, can, said, there, use, an, each, which, she, do, how, their, if, will, up, there, about, out, many, then, them, these, so, some, her, would, make, like, him, into, time, has, look, two, more, write, go, see, number, no, way, could, people, my, than, first, water, been, call, who, oil, its, now, find, long, down, day, did, get, come, made, may, part'
	badwords = baddictionary.split(", ")

	rawlist = [word for word in rawlist if word not in badwords]


	for word in rawlist:
			mostcommon[word] = mostcommon.get(word, 0) + 1   #I use the DSU method to get the histogram for the most popular words used in the chat

	sortinglist = []

	for word, freq in mostcommon.items():
		sortinglist.append((freq, word))

	sortinglist.sort(reverse=True)

	res = []

	for freq, word in sortinglist:
		res.append(word)

	for item in res:   										 #gets rid of spaces
		if item == ' ' or item == '':
			res.remove(item)

															# fancy printing of the top 10

	output = ''
	output = 'Top 10 \n'
	if len(res) < 10:
		for i in range(len(res)):
			output +=  '{}. '.format(i+1) + res[i] + '\n'
	else:
		for i in range(10):
			output += '{}. '.format(i+1) + res[i] + '\n'		

	print output  									 		#prints the top 10 most popular words 


def sentiments(twitchchat):
	"""
	Prints the sentiment of the whole duration the program was open. 
	"""

	sentimental = indicoio.sentiment_hq(twitchchat)   					#uses pattern's sentiment analysis to calculate how troll or nice the chat is
	print "This streamer has a sentiment polarity of " + str(sentimental) 

def wordsentiment(words):
	"""
	returns the sentiment of the inputted phrase
	"""
	if words == '':         			                  	    #sometimes after filtering the individual phrase has nothing left, this is to account for that
		sentiments = 0
	else:	
		sentiments = indicoio.sentiment_hq(words)				#using indico's API because pattern's is bad


	return sentiments

def findfreq(word):
	"""
	returns the frequency of the word from the mostcommon dictionary
	"""

	if word in mostcommon:
		return mostcommon[word]
	else:
		return 0

def make_array():
	"""
	takes the dictionary and returns it as a numpy array of arrays
	used for text clustering
	"""
	result =  np.ndarray(shape=(len(mostcommon), 2))			#create a general numpy array, a giant array the size of the dictionary each consisting of a length 2 array
	count = 0
	for word in mostcommon:										
		result[count][0] = wordsentiment(word)					#assigns the first and second value of the arrays in the numpy array to be the items in the dictionary
		result[count][1] = mostcommon[word]
		count+=1												#gets through all the words in the dictionary and assigns them correctly via a counter

	return result	


