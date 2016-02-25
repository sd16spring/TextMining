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


# def histogram(wordList, d):
# 	""" takes a list of words and returns a dictionary with each word as a key to the number
# 		of times the word appears in the list

# 		wordList: a list of words
# 		d: dictionary to store histogram in
# 		returns: dictionary (word and frequency)
# 	"""

# 	for word in wordList:
# 		d[word] = d.get(word, 0) + 1
# 	return d


# def cosineSimilarity(d1, d2):
# 	""" adapted from http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python

# 		d1, d2: dictionaries of lyrics characterized by word frequencies
# 	"""

# 	intersection = set(d1.keys()) & set(d2.keys())
# 	numerator = sum([d1[i] * d2[i] for i in intersection])

# 	sum1 = sum([d1[i]**2 for i in d1.keys()])
# 	sum2 = sum([d2[i]**2 for i in d2.keys()])
# 	denominator = math.sqrt(sum1) * math.sqrt(sum2)

# 	if not denominator: # if denominator == 0, we divide by 0
# 		return 0.0
# 	else:
# 		return float(numerator) / denominator


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
	return averageSentiment(dictionary)


def averageSentiment(d):
	""" takes a dictionary and returns average of dictionary values

		d: a dictionary
		returns: average of dictionary values
	"""
	avg = sum(d.values()) / len(d)
	return avg


# def averageArtistSentiment(d):
# 	""" takes a dictionary of form song : averageSongSentiment and finds the average
# 		sentiment for all songs by the artist

# 		d: dictionary of song sentiments
# 		returns: average sentiment
# 	"""

# 	pass


def analyzeAllLyrics(artist):
	songs = dict()
	files = [f for f in os.listdir('./{}/Songs'.format(artist)) if '.txt' in f]
	for file in files:
		songName = file.split('.')[1]
		polarity = analyzeLyrics(artist, file)
		songs[songName] = remapInterval(polarity, -1, 1, 0, 1)

	data = dict()
	data['songs'] = songs
	data[artist] = averageSentiment(songs)

	return data


def compare(artist, d):
	avg = d.get(artist)
	print avg
	songs = d.get('songs')
	comparison = dict()

	for song in songs:
		comparison[song] = abs(avg - songs.get(song))

	return comparison


def plot(artist):
	data = analyzeAllLyrics(artist)
	print compare(artist, data)






if __name__ == "__main__":
	# analyzeAllLyrics('Broken-Bells')
	plot('Broken-Bells')


# r = np.arange(0, 3.0, 0.01)
# theta = 2 * np.pi * r

# ax = plt.subplot(111, projection='polar')
# ax.plot(theta, r, color='r', linewidth=3)
# ax.set_rmax(2.0)
# ax.grid(True)

# ax.set_title("A line plot on a polar axis", va='bottom')
# plt.show()