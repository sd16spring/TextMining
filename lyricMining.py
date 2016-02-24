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
		url = 'https://www.musixmatch.com/artist/{}/{}'.format(artist, i)
		artistPage = URL(url).download()
		content = plaintext(artistPage)

		f = open('./{}/{}-{}.txt'.format(artist, artist, i), 'w')
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

	concatenated = open(artistPage, 'a')
	# files = [f for f in os.listdir('./{}/'.format(artist)) if os.path.isfile(f) and './{}/{}'.format(artist, artist) in f and f != './{}/{}.txt'.format(artist, artist)]
	# files = [f for f in os.listdir('.') if './{}'.format(artist) in f and f != './{}/{}.txt'.format(artist, artist)]
	files = [f for f in os.listdir('./{}'.format(artist)) if '.txt' in f]
	print files

	for file in files:
		content = cleanUpLastArtistPage(artist, file)
		# if file == files[-1]:
		# 	content = cleanUpLastArtistPage(artist, file)
		# else:
		# 	content = cleanUpArtistPage(artist, file)
		concatenated.write(content)
	
	concatenated.close()

	print 'made concatenatedArtistPage'

	return artistPage


# def cleanUpArtistPage(artist, fileName):
# 	""" takes an artist page and returns the unformatted song list from that page
		
# 		fileName: '___.txt'
# 		generates: file with unformatted song list
# 	"""

# 	f = open('./{}/{}'.format(artist, fileName), 'r+')
# 	content = f.read()
# 	i = content.find('* 01')
# 	j = content.rfind('Load more')
# 	f.close()
# 	return content[i:j]


def cleanUpLastArtistPage(artist, fileName):
	""" takes the last artist page and returns the unformatted song list from that page
		
		fileName: '___.txt'
		generates: file with unformatted song list
	"""

	f = open('./{}/{}'.format(artist, fileName), 'r+')
	content = f.read()
	i = content.find('* 01')
	j = content.rfind('editors')
	f.close()
	print content[i:j]
	return content[i:j]


def getSongList(artist, artistPage):
	"""
		artist: formatted artist name
		artistPage: concatenated artist page ('formattedArtist.txt')
	"""
	# f = open('./{}/{}'.format(artist, artistPage), 'r')
	f = open(artistPage, 'r')
	songListName = './{}/{}-Songs.txt'.format(artist, artist)
	songList = open(songListName, 'a')
	print 'made songList'
	
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
		songName = formatSpaces(song)
		url = 'https://www.musixmatch.com/lyrics/{}/{}'.format(artist, songName)
		songPage = URL(url).download()
		content = plaintext(songPage)

		fileName = './{}/{}.{}.txt'.format(artist, artist, songName)
		g = open(fileName, 'w')
		g.write(content.encode("UTF-8"))
		g.close()
		cleanUpSongPage(fileName)
		break

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
	lyrics = content[i:j]
	f.close()

	g = open(fileName, 'w')
	g.write(lyrics)
	g.close()
	# return content[i:j]


def getArtistData(unformattedArtist):
	artist = formatSpaces(unformattedArtist)
	
	# getArtistPages(artist)
	artistPage = concatenateArtistPages(artist)
	songList = getSongList(artist, artistPage)
	# getSongPages(artist, songList)



if __name__ == "__main__":
	# getArtistPages('Broken Bells')
	# concatenateArtistPages('Broken-Bells')
	# getSongList('Broken Bells', 'Broken-Bells', 'Broken-Bells.txt')
	# getSongPage('Broken-Bells', 'Broken-BellsSongs.txt')
	# formatSpaces('The High Road ')
	getArtistData('Broken Bells')


