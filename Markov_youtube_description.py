""" Text mining project: finds the descriptions of Youtube videos using BeautifulSoup and makes a new description using Markov analyis """ 
from bs4 import BeautifulSoup
import requests
import string
import random
import pickle
import doctest

"""
Youtube Descriptions
"""

def yt_description(youtube_id):
	"""Returns the youtube description of a video.
	>>> yt_description('KenrpZ1oxfU')
	["Republican candidate weighs in on Israeli-Palestinian conflict, trade with China, 9/11 Commission and Iraq War on 'Hannity'"]
	>>> yt_description('SWl3xfSqOIY')
	["On 'Hannity,' presidential candidate responds to negative ads, talks feud with pope, illegal immigration"]
	"""
	printed_description = [] #list that holds Youtube description
	html = requests.get('https://www.youtube.com/watch?v={}'.format(youtube_id))
	soup = BeautifulSoup(html.text, "lxml")
	description = soup.find('p',id= 'eow-description') #finds the description in a YouTube video

	printed_description.append(str(description.get_text())) #converts description to only text and appends it to an empty list
	return printed_description

def combine_descriptions(video_ids):
	"""Combines descriptions of different youtube videos into one list
	>>> combine_descriptions(['KenrpZ1oxfU','SWl3xfSqOIY'])
	["Republican candidate weighs in on Israeli-Palestinian conflict, trade with China, 9/11 Commission and Iraq War on 'Hannity'", "On 'Hannity,' presidential candidate responds to negative ads, talks feud with pope, illegal immigration"]
	"""
	combined_descriptions = [] #list that holds the combined YouTube video descriptions
	for video_id in video_ids:
		combined_descriptions += yt_description(video_id) #combines descriptions into one list
	return combined_descriptions

"""
Markov analysis
"""

prefix = ()
suffix_map = {}

def Markov_file(filename,order):
	for line in filename:
		for word in line.strip().split():
			store_words(word,order)

def store_words(word, order):
	global prefix
	if len(prefix)<order:
		prefix = prefix + (word,)
		return
	try:
		suffix_map[prefix].append(word)
	except KeyError:
		suffix_map[prefix] = [word] # makes a prefix if there are none

	prefix = shift(prefix, word)

def random_text(n):
    start = random.choice(suffix_map.keys()) #chooses random prefix 
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None: # if we get to  the end of the text, start again
            random_text(n-i)
            return

        word = random.choice(suffixes)
        print word,
        start = shift(start, word)

def shift(tup,word):
	return tup[1:] + (word,) #makes a new tuple by removing head and adding word to the end

if __name__ == '__main__':
	doctest.testmod()
	Markov_file(combine_descriptions(['eCXSpllybUM','IPkHW0mA8O4','Rhp7oamdVow','jMkDv8O_yoA','se9iaOX8bgc','I4cXVxCrqPc','ckzGe3w-gOI','Oc7DWPGb18k','zwK9iqkLOpc','KenrpZ1oxfU']),2)
	random_text(50)