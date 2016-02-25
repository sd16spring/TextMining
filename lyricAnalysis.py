""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	ANALYZING SONG LYRICS FOR AN CHOSEN ARTIST

	@author: Gaby Clarke

"""

import string
import math
import os
from pattern.en import sentiment
# import numpy as np
# import matplotlib.pyplot as plt


def makeLyrics(artist, fileName):
	""" 
		returns: a list of strings of lines of lyrics
	"""
	f = open('./{}/Songs/{}'.format(artist, fileName), 'r')
	content = f.read()
	content = content.split('\n')
	content = [i for i in content if i != '' and i != 'Translate lyrics']
	f.close()
	return content


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


def remapInterval(val, inputIntervalStart, inputIntervalEnd, outputIntervalStart, outputIntervalEnd):
    """ Given an input value in the interval [inputIntervalStart,
        inputIntervalEnd], return an output value scaled to fall within
        the output interval [outputIntervalStart, outputIntervalEnd].

        Function from ComputationalArt Project.

        val: the value to remap
        inputIntervalStart: the start of the interval that contains all
                              possible values for val
        inputIntervalEnd: the end of the interval that contains all possible
                            values for val
        outputIntervalStart: the start of the interval that contains all
                               possible output values
        outputIntervalEnd: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval
        >>> remapInterval(0.5, 0, 1, 0, 10)
        5.0
        >>> remapInterval(5, 4, 6, 0, 2)
        1.0
        >>> remapInterval(5, 4, 6, 1, 2)
        1.5
    """
    inputDelta = inputIntervalEnd - inputIntervalStart
    inputPosition = float(val - inputIntervalStart) / inputDelta
    outputDelta = outputIntervalEnd - outputIntervalStart
    outputPosition = outputIntervalStart + (inputPosition * outputDelta)
    return outputPosition


def analyzeLyrics(artist, fileName):
	lyrics = makeLyrics(artist, fileName)
	dictionary = dict()
	index = 0
	for i in lyrics:
		# words = cleanUpLyrics(i)
		# histogram(words, dictionary) # assign to a variable, or put into list?
		dictionary[index] = sentiment(i)[0]
		index += 1
	return averageSongSentiment(dictionary)


def analyzeAllLyrics(artist):
	# content = makeLyrics('./Broken-Bells/Broken-Bells.Vaporize.txt')
	# print content
	# print sentiment(content[0])
	# one = analyzeLyrics('./Broken-Bells/Broken-Bells.Vaporize.txt')
	# two = analyzeLyrics('./Broken-Bells/Broken-Bells.Windows.txt')
	# print one

	# # print averageSongSentiment(one), averageSongSentiment(two)
	dictionary = dict()
	files = [f for f in os.listdir('./{}/Songs'.format(artist)) if '.txt' in f]
	print files
	for file in files:
		polarity = analyzeLyrics(artist, file)
		dictionary[file] = remapInterval(polarity, -1, 1, 0, 1)

	print dictionary

	# print cosineSimilarity(one, two)





def averageSongSentiment(d):
	avg = sum(d.values()) / len(d)
	return avg


def averageArtistSentiment():
	pass


# d1 = {'cat': 1, 'dog': 2, 'parrot': 2}
# d2 = {'cat': 1, 'dog': 2, 'rabbit': 1}
# d3 = {'rat': 1, 'dog': 3, 'parrot': 2}
# d4 = {'cat': 1, 'rabbit': 3, 'parrot': 2}
# d = {'d1': d1, 'd2': d2, 'd3': d3, 'd4': d4}

# d5 = {1: (0.0), 2: (1,5)}
# d6 = {1: (0.0), 2: (1,5)}


if __name__ == "__main__":
	# analyzeLyrics('The-High-Road.txt')
	analyzeAllLyrics('Broken-Bells')
	# print cosineSimilarity(d5,d6)


# r = np.arange(0, 3.0, 0.01)
# theta = 2 * np.pi * r

# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r, color='r', linewidth=3)
# ax.set_rmax(2.0)
# ax.grid(True)

# ax.set_title("A line plot on a polar axis", va='bottom')
# plt.show()