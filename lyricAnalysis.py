import string
import math
import numpy as np
import matplotlib.pyplot as plt

data = dict()

def makeLyrics(fileName):
	""" 
		returns: a list of strings of lines of lyrics
	"""
	f = open(fileName, 'r')
	content = f.read()
	content = content.split('\n')
	content = [i for i in content if i != '' and i != 'Translate lyrics']
	f.close()
	return content

def analyzeLyrics(fileName):
	lyrics = makeLyrics(fileName)
	dictionary = dict()
	for i in lyrics:
		words = cleanUpLyrics(i)
		histogram(words, dictionary) # assign to a variable, or put into list?
	print dictionary


def cleanUpLyrics(s):
	""" takes an unformatted string and returns a list of lowercase words without
		punctuation

		s: a string
		returns: a formatted list of words in the string
	"""

	s = s.lower()

	for char in string.punctuation:
		if char != "'":
			s = s.replace(char, '')

	wordList = s.split()
	return wordList


def histogram(wordList, d):
	""" takes a list of words and returns a dictionary with each word as a key to the number
		of times the word appears in the list

		wordList: a list of words
		d: dictionary to store histogram in
		returns: dictionary (word and frequency)
	"""

	for word in wordList:
		d[word] = d.get(word, 0) + 1
	return d


def cosineSimilarity(d1, d2):
	""" adapted from http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python

		d1, d2: dictionaries of lyrics characterized by word frequencies
	"""

	intersection = set(d1.keys()) & set(d2.keys())
	numerator = sum([d1[i] * d2[i] for i in intersection])

	sum1 = sum([d1[i]**2 for i in d1.keys()])
	sum2 = sum([d2[i]**2 for i in d2.keys()])
	denominator = math.sqrt(sum1) * math.sqrt(sum2)

	if not denominator: # if denominator == 0, we divide by 0
		return 0.0
	else:
		return float(numerator) / denominator


d1 = {'cat': 1, 'dog': 2, 'parrot': 2}
d2 = {'cat': 1, 'dog': 2, 'rabbit': 1}
d3 = {'rat': 1, 'dog': 3, 'parrot': 2}
d4 = {'cat': 1, 'rabbit': 3, 'parrot': 2}
d = {'d1': d1, 'd2': d2, 'd3': d3, 'd4': d4}


if __name__ == "__main__":
	analyzeLyrics('The-High-Road.txt')
	# print cosineSimilarity(d1,d2)


# r = np.arange(0, 3.0, 0.01)
# theta = 2 * np.pi * r

# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r, color='r', linewidth=3)
# ax.set_rmax(2.0)
# ax.grid(True)

# ax.set_title("A line plot on a polar axis", va='bottom')
# plt.show()