""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	ANALYZING SONG LYRICS FOR AN CHOSEN ARTIST

	@author: Gaby Clarke

"""

import string
import os
from pattern.en import sentiment

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from pylab import *



def makeLyrics(artist, fileName):
	""" reads a song file and generates a list containing lines of lyrics as strings

		artist: artist name
		fileName: song file name
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


def remapInterval(val, inputIntervalStart, inputIntervalEnd, outputIntervalStart, 
					outputIntervalEnd):
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


def averageSentiment(d):
	""" takes a dictionary and returns average of dictionary values

		d: a dictionary
		returns: average of dictionary values
	"""
	
	avg = sum(d.values()) / len(d)
	return avg


def analyzeLyrics(artist, fileName):
	""" given a song file, analyzes song lyrics using Pattern's sentiment tool for
		language polarity, and returns the average polarity of all lyrics in the 
		song

		artist: artist name
		fileName: song file name
		returns: average polarity of all lyrics in that song (value in range -1:1)
	"""

	lyrics = makeLyrics(artist, fileName)
	dictionary = dict()
	index = 0
	for i in lyrics:
		dictionary[index] = sentiment(i)[0]
		index += 1
	return averageSentiment(dictionary)


def analyzeAllLyrics(artist):
	""" takes an artist name and analyzes all songs by that artist for polarity of
		sentiments expressed in that song lyrically

		artist: artist name
		returns: dictionary of polarity sentiment analysis for all songs, as well as
		the average polarity of all songs
	"""

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
	""" takes the dictionary of polarity analysis for all songs and the average polarity
		of all those songs and finds the absolute value of the difference between the 
		polarity of each song and the average (ie, how different each song is from the average)

		artist: artist name
		d: dictionary of polarity sentiment analysis for all songs, as well as
		the average polarity of all songs (from analyzeAllLyrics)
		returns: dictionary of differences
	"""

	avg = d.get(artist)
	print avg
	songs = d.get('songs')
	comparison = dict()

	for song in songs:
		comparison[song] = abs(avg - songs.get(song))

	return comparison


def plot(artist):
	""" uses matplotlib's scatter to plot each song by the given artist on a polar 
		plot, where the r-component of the position is the difference between the 
		polarity of that song and the average polarity of that artist's songs

		artist: artist name
		generates: polar plot of all songs by that artist according to the polarity
		of the lyrics
	"""

	data = analyzeAllLyrics(artist)
	comparison = compare(artist, data)

	ax = plt.subplot(111, projection='polar')

	ax.grid(True)
	ax.set_xticklabels(['', '', '', '', '', '', '', ''])
	ax.set_yticklabels(['', '', '', '', '', '', '', ''])
	

	deltaTheta = 2 * np.pi / len(comparison)
	index = 0


	for song in comparison:
		r = comparison.get(song)
		theta = index * deltaTheta
		c = scatter(theta, r, s=100, linewidth=0, label='Broken Bells')
		
		index += 1

	show()



if __name__ == "__main__":
	# plot('Broken-Bells')

