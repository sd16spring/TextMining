"""
Kevin Zhang, Software Design Spring 2016

My own code used to test histogram algorithms on my twitchchat data. It finds the most common words used on a particular streamer's stream.

Integrated into the code, the analyze function can be done in real-time with each message that is sent on twitch chat.

The sentiment function happens at the end and evaluates the total sentiment polarity of everything that was said on twitch chat during the period this was run to determine how positive 
a streamer's messages are, a maybe? indication of a streamer's trolliness/popularity.
"""

import pickle
from pattern.en import *



def analyze():
	file = open("twitchchat","r")

	#realfile = pickle.load(file) #pickle failed cuz of unicode problems.

	mostcommon = {}

	rawlist = []
	rawlist = file.read().split(" ")  #this is get rid of article and common words.


	baddictionary = 'yet, just, well, me, thats, does, still, put, want, im, got, stop, dont, too, should, the, of, and, a, to, in, is, you, that, it, he, was, for, on, are, as, with, his, they, i, at, be, this, have, from, or, one, had, by, word, but, not, what, all, were, we, when, your, can, said, there, use, an, each, which, she, do, how, their, if, will, up, there, about, out, many, then, them, these, so, some, her, would, make, like, him, into, time, has, look, two, more, write, go, see, number, no, way, could, people, my, than, first, water, been, call, who, oil, its, now, find, long, down, day, did, get, come, made, may, part'
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

	for item in res:    #gets rid of spaces
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

	print output   #prints the top 10 most popular words 


def sentiments(twitchchat):
	sentimental = sentiment(twitchchat)   #uses pattern's sentiment analysis to calculate how troll or nice the chat is
	print "This streamer has a sentiment polarity of " + str(sentimental[0]) + " and it is believed that this number is " + str(sentimental[1]*100) + "% subjective."
	#print sentimental