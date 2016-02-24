""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	MINING SONG LYRICS FOR AN ARTIST

	@author: Gaby Clarke

"""

import string
from pattern.web import *
import os
import math



def formatSpaces(string):
	""" formats string to musixmatch's format (-'s for spaces, removes trailing whitespace) 

		artist: unformatted string
		returns: formatted string
	"""

	formatted = string.rstrip()
	formatted = formatted.replace(' ', '-')

	return formatted


def getArtistPages(artist):
	""" takes an artist and generates all artist pages populated with songs 

		unformattedArtist: artist name
		generates: artist pages '___#.txt'
	"""

	if not os.path.isdir('./{}'.format(artist)):
		os.mkdir('./{}'.format(artist))

	i = 0
	while True:
		i += 1

		artistPageName = './{}/{}-{}.txt'.format(artist, artist, i)
		if os.path.isfile(artistPageName):
			pass

		url = 'https://www.musixmatch.com/artist/{}/{}'.format(artist, i)
		artistPage = URL(url).download()
		content = plaintext(artistPage)

		f = open(artistPageName, 'w')
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
	
	artistPage = './{}/{}.txt'.format(artist, artist)
	if os.path.isfile(artistPage):
		pass

	concatenated = open(artistPage, 'a')
	files = [f for f in os.listdir('./{}'.format(artist)) if '.txt' in f]

	for file in files:
		content = cleanUpArtistPage(artist, file)
		concatenated.write(content)
	
	concatenated.close()

	return artistPage



def cleanUpArtistPage(artist, fileName):
	""" takes an artist page and returns the unformatted song list from that page
		
		fileName: '___.txt'
		generates: file with unformatted song list
	"""

	f = open('./{}/{}'.format(artist, fileName), 'r+')
	content = f.read()
	i = content.find('* 01')
	j = content.rfind('editors')
	f.close()
	return content[i:j]


def getSongList(artist, artistPage):
	"""
		artist: formatted artist name
		artistPage: concatenated artist page ('formattedArtist.txt')
	"""
	
	songListName = './{}/{}-Songs.txt'.format(artist, artist)
	if os.path.isfile(songListName):
		pass

	f = open(artistPage, 'r')
	songList = open(songListName, 'a')
	
	content = f.read()
	content = content.split('\n')
	content = [i for i in content if i != '' and i != 'Add lyrics']

	for i in range(len(content)):
		if '* ' in content[i]:
			song = content[i+1]
			songList.write(song+'\n')

	f.close()
	songList.close()

	return songListName


def getSongPages(artist, songList):
	f = open(songList, 'r')
	for song in f:
		if '(' not in song and 'emix' not in song:

			songName = formatSpaces(song)
			fileName = './{}/{}.{}.txt'.format(artist, artist, songName)

			if not os.path.isfile(fileName):
			
				url = 'https://www.musixmatch.com/lyrics/{}/{}'.format(artist, songName)
				songPage = URL(url).download()
				content = plaintext(songPage)

				g = open(fileName, 'w')
				g.write(content.encode("UTF-8"))
				g.close()
				cleanUpSongPage(fileName)

	f.close()


def cleanUpSongPage(fileName):
	""" takes the song page and returns the unformatted lyrics
		
		fileName: '___.txt'
		generates: file with unformatted lyrics
	"""

	f = open(fileName, 'r')
	content = f.read()
	i = content.find('Translate lyrics')
	j = content.rfind('Writer(s)')
	lyrics = content[i+17:j]
	f.close()

	g = open(fileName, 'w')
	g.write(lyrics)
	g.close()


def getArtistData(unformattedArtist):
	artist = formatSpaces(unformattedArtist)
	
	getArtistPages(artist)
	artistPage = concatenateArtistPages(artist)
	songList = getSongList(artist, artistPage)
	getSongPages(artist, songList)



if __name__ == "__main__":
	getArtistData('Broken Bells')


