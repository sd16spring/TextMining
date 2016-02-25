"""

This program will look at all of the lyrics within an album and produce a randomly generated song based on a markov analysis of the collected lyrics

"""

from bs4 import BeautifulSoup
import requests
import pickle
import random
import sys

# Pickling data uses a lot of recursion
sys.setrecursionlimit(3000)

# Global Variables
suffix_map = {}
prefix = ()

"""

Pickling Functions

These function are purposed to save data collected from various urls and then load them for reading

"""

# Function to pickle a file with a given url and name
def pickle_data(url, name):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, "lxml")
	pickle.dump(soup, open(name, "w"))

# Pickles all songs within the album list
def get_all_song_data(url_list, file_name):
	index = 1
	for link in url_list:
		name = str(file_name) + str(index) + '.pickle'
		index += 1
		pickle_data(link, name)

# Loads the pickled data with "file_name"
def get_loaded_data(file_name):
	input_file = open(file_name, 'r')
	reloaded_copy_of_texts = pickle.load(input_file)
	return reloaded_copy_of_texts

"""

Parsing Functions

These functions use BeautifulSoup to look through the webpage source code to find links and lyrics

"""

# Parses through pickled data and extracts all the urls that lead to songs within a specific album
def get_album_links(data, album):
	album_page = data
	album_page_links = album_page.find_all("a", class_= "title")
	song_links = []
	# Goes through each link with the tag a and the class title
	for link in album_page_links:
	 	if album in link['title']:
	 		# if the album name is in the item with a song link append this link to the song list
	 		song_links.append((link.get('href')))
	return song_links

def get_lyrics(file_name):
	data = get_loaded_data(file_name)
	verse_tags = data.find_all("p", class_='verse')
	lyrics = []
	all_words = []

	# gets all of the lyrics in tags that have class = 'verse'
	for tags in verse_tags:
		lyrics.append(tags.get_text())

	# Formats all individual words into a list
	for x in lyrics:
		all_words += x.split()

	final_all_words = clean_lyrics(all_words)

	return final_all_words

def clean_lyrics(lyrics_list):
	new_list = []

	# Gets rid of any words in parenthesis or brackets
	for word in lyrics_list:
		if word[0] != '[' and word[-1] != ']' and word[0] != '(' and word[-1] != ')':
			new_list.append(word)

	# Gets rid of any words with punctuation and turns them all lowercase
	final_list = []
	for word in new_list:
		if word[-1] not in "!,.?:":
			final_list.append(word.lower())

	return final_list

# Gets all the lyrics from the pickled song files and complies them into one large list
def get_album_lyrics(album_length, file_name):
	compiled_lyrics = []
	index = 1
	for x in range(0, album_length):
		name = str(file_name) + str(index) + '.pickle'
		index += 1
		compiled_lyrics += get_lyrics(name)

	return compiled_lyrics

"""

Markov Analysis Functions

These functions store prefixes with corresponding suffixes into a dictionary which is accessed to produce a random order of prefixes with suffixes

"""

# Proccesses each word within the large lyrics list
def process_lyrics(lyrics, order=2):
	for word in lyrics:
		process_word(word, order)

# Modifies global dictionary and adds prefixes to the keys with their corresponding suffix values
def process_word(word, order=2):
	global prefix
	if len(prefix) < order:
		prefix += (word,)
		return

	try:
		suffix_map[prefix].append(word)
	except KeyError:
		suffix_map[prefix] = [word]

	prefix = shift(prefix, word)

# Forms a new tuple by removing the head and adding word to the tail
def shift(t, word):
	return t[1:] + (word,)

# Generates random words from suffix_map
def random_words(n):
	start = random.choice(suffix_map.keys())
	for i in range(n):
		suffixes = suffix_map.get(start, None)
		word = random.choice(suffixes)
		print word,
		start = shift(start, word)

"""

Generate Lyrics Based on Album Lyrics

This function takes in a url and album to produce a randomly generated song

"""

# The parameter pickle = False allows user to choose to not pickle the data if the data has already been pickled
def generate_new_song(url, artist, album, number_of_words, pickle = False):

	url_artist = url
	artist_name = str(artist) + ".pickle"
	song_prefix = str(artist) + "_song"

	if pickle:
		pickle_data(url_artist, artist_name)

	data_artist = get_loaded_data(artist_name)
	artist_song_urls = get_album_links(data_artist, album)

	if pickle:
		get_all_song_data(artist_song_urls, song_prefix)

	all_lyrics_artist = get_album_lyrics(len(artist_song_urls), song_prefix)

	process_lyrics(all_lyrics_artist, 3)
	random_words(number_of_words)

"""

Variable Declaration and Main Function Implementation

"""

# CHANGE pickle TO TRUE IF THIS IS THE FIRST TIME RUNNING THE CODE
first_time = False

url_adele = 'http://www.metrolyrics.com/adele-albums-list.html'
adele = 'Adele'
album_adele = "25"

url_queen = 'http://www.metrolyrics.com/queen-albums-list-5.html'
queen = 'Queen'
album_queen = "Greatest Hits"

url_bieber = 'http://www.metrolyrics.com/justin-bieber-albums-list-2.html'
bieber = 'Bieber'
album_bieber = "My Worlds Acoustic"

url_swift = 'http://www.metrolyrics.com/taylor-swift-albums-list.html'
swift = 'Swift'
album_swift = "1989"

url_beetles = 'http://www.metrolyrics.com/beatles-albums-list-8.html'
beetles = 'Beetles'
album_beetles = "Abbey Road"

# Average number of words in a song
number_of_words = random.randint(159, 300)

generate_new_song(url_adele, adele, album_adele, number_of_words, first_time)
suffix_map = {}
prefix = ()
print "\n\n\n\n\n"
generate_new_song(url_queen, queen, album_queen, number_of_words, first_time)
suffix_map = {}
prefix = ()
print "\n\n\n\n\n"
generate_new_song(url_bieber, bieber, album_bieber, number_of_words, first_time)
suffix_map = {}
prefix = ()
print "\n\n\n\n\n"
generate_new_song(url_swift, swift, album_swift, number_of_words, first_time)
suffix_map = {}
prefix = ()
print "\n\n\n\n\n"
generate_new_song(url_beetles, beetles, album_beetles, number_of_words, first_time)