""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	MINING SONG LYRICS FOR AN ARTIST

	@author: Gaby Clarke

"""

import string
from pattern.web import *
import os



def formatSpaces(artist):
	""" formats artist name to musixmatch's format (-'s for spaces) 

		artist: unformatted artist name
		returns: formatted artist name
	"""
	return artist.replace(' ', '-') 


def getArtistPages(unformattedArtist):
	""" takes an artist and generates all artist pages populated with songs 

		unformattedArtist: artist name
		generates: artist pages '___#.txt'
	"""

	artist = formatSpaces(unformattedArtist)

	i = 0
	while True:
		i += 1
		url = 'https://www.musixmatch.com/artist/{}/{}'.format(artist, i)
		artistPage = URL(url).download()
		content = plaintext(artistPage)

		f = open('{}{}.txt'.format(artist, i), 'w')
		f.write(content.encode("UTF-8"))
		f.close()

		if '* 15' not in content:
			break


def concatenateArtistPages(artist):
	""" parses current directory for all files containing artist name and concatenates
		those artist pages into one cleaned-up page

		artist: formatted artist name
		generates: concatenated artist page
	"""
	
	concatenated = open('{}.txt'.format(artist), 'a')
	files = [f for f in os.listdir('.') if os.path.isfile(f) and '{}'.format(artist) in f and f != '{}.txt'.format(artist)]
	for file in files:
		if file == files[-1]:
			content = cleanUpLastArtistPage(file)
		else:
			content = cleanUpArtistPage(file)
		concatenated.write(content)
	
	concatenated.close()


def cleanUpArtistPage(fileName):
	""" takes an artist page and returns the unformatted song list from that page
		
		fileName: '___.txt'
		generates: file with unformatted song list
	"""

	f = open(fileName, 'r+')
	content = f.read()
	i = content.find('* 01')
	j = content.rfind('Load more')
	f.close()
	return content[i:j]


def cleanUpLastArtistPage(fileName):
	""" takes the last artist page and returns the unformatted song list from that page
		
		fileName: '___.txt'
		generates: file with unformatted song list
	"""

	f = open(fileName, 'r+')
	content = f.read()
	i = content.find('* 01')
	j = content.rfind('editors')
	f.close()
	return content[i:j]


def getSongList(unformattedArtist, artist, artistPage):
	"""
		artist: formatted artist name
		artistPage: concatenated artist page ('formattedArtist.txt')
	"""
	f = open(artistPage, 'r')
	songList = open(artist + 'Songs.txt', 'a')
	
	content = f.read()
	content = content.split('\n')
	content = [i for i in content if i != '' and i != 'Add lyrics']

	for i in range(len(content)):
		if '* ' in content[i]:
			song = content[i+1]
			songList.write(song+'\n')

	# print content.index('')
	# for i in content:
	# 	content.remove('')
	# print content

	# for i in range(len(f)):
	# 	if unformattedArtist in line:
	# 		song = f[i - 1]
	# 		songList.write(song)

	# lines = [line for line in f]
	# for line in lines[2::6]:
	# 	song = line
	# 	songList.write(song)
	f.close()
	songList.close()

	### THIS WORKS BUT IT'S SUPER SLOW... I ABORT ONLY TO FIND THE COMPLETE FILE
	### ALSO, RETURNS LINES NOT IN F... WTF?

def getSongPage(artist, songList):
	f = open(songList, 'r')
	# songs = [song for song in f]
	# for song in songs:
	for song in f:
		songName = formatSpaces(song)
		url = 'https://www.musixmatch.com/artist/{}/{}'.format(artist, songName)
		songPage = URL(url).download()
		content = plaintext(songPage)

		g = open('{}.txt'.format(songName), 'w')
		g.write(content.encode("UTF-8"))
		g.close()
		break



def cleanUpLyrics(s):
	""" takes an unformatted string and returns a list of lowercase words without
		punctuation

		string: a string
		returns: a formatted list of words in the string
	"""

	string = string.lower()

	for char in string.punctuation:
		if char != "'":
			string = string.replace(char, '')

	wordList = string.split()
	return wordList


def histogram(wordList):
	""" takes a list of words and returns a dictionary with each word as a key to the number
		of times the word appears in the list

		wordList: a list of words
		returns: dictionary (word and frequency)
	"""

	d = dict()
	for word in wordList:
		d[word] = d.get(word, 0) + 1
	return d



if __name__ == "__main__":
	import doctest
	# doctest.testmod()

	# getArtistPages('Broken Bells')
	# concatenateArtistPages('Broken-Bells')
	getSongList('Broken Bells', 'Broken-Bells', 'Broken-Bells.txt')
	# getSongPage('Broken-Bells', 'Broken-BellsSongs.txt')

