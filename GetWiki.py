# -*- coding:utf-8 -*-
from pattern.web import *
import os
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

"""
	This program takes a language and a Wikipedia article title as an input. It then outputs the top ten most common words within that article, first
	checking to see if they're significant (eg: not articles or prepositions, etc.)

	This program supports English, Swedish, Portugese, Hungarian, Finnish, Turkish, German, Dutch, Norwegian, Spanish, Russian, Danish, & Italian.

	The language dictionary is a global because it's referenced in both get_text() and open_text(). It's a lot easier to reference and edit as a global.
"""

dict_lang = {'English':['en', 'references'], 'Swedish':['sv', 'referenser'], 'Portuguese':['pt', 'referências'], 'Hungarian':['hu', 'források'], 'Finnish':['fi', 'lähteet'], \
	'Turkish':['tr', 'kaynakça'], 'German':['de', 'anmerkungen'], 'Dutch':['nl', 'referenties'], 'Norwegian':['nb', 'referanser'], \
	'Spanish':['es', 'referencias'], 'Russian':['ru', 'Примечания'.lower()], 'Danish':['da', 'referencer'], 'Italian':['it', 'bibliografia']}

def get_text(language, title):
	"""
		Finds the Wikipedia article in the specified language, then writes it into a plaintext .txt file. (Language_us_file.txt)
	"""

	filename = language + '_us_file.txt' #Creates filename of eventual wiki text file in language "language."

	wiki = Wikipedia(language = dict_lang[language][0]) #Opens wiki in language "language", referencing dict_lang for the appropriate language code

	article = wiki.search(title) #Finds the right article by seaching wiki for the title
	article_text = article.plaintext()

	article_file = open(filename, 'w')
	article_file.write(article_text.encode("UTF-8")) #Creates file "Language_us_file.txt," writes in plaintext of wiki article.
	article_file.close

def open_text(language):
	"""
		Opens the appropriate plaintext file and runs a histogram, creating a dictionary with every non-trivial word that appears and its frequency in the article.
		Terminates when it detects that it has read the entire article and reached the bibliography. ("Reference" section.)
		Outputs a tuple of the original list and the complete sorted version.
	"""
	filename = language + '_us_file.txt' #Creates filename of eventual wiki text file in language "language."
	if language in dict_lang: #Checks if stopwords supports this language. Stopwords contains a library of common articles/prepositions/trash words in a couple languages.
		common_words = set(stopwords.words(language.lower()))
	else:
		common_words = []

	hist = {}

	with open(filename, 'r') as f:
		filetext  = [line.translate(None, string.punctuation).lower() for line in f] #Strips punctuation from the file plaintext and makes everything lowercase for processing
		for line in filetext:
			for word in line.split():
				if word == dict_lang[language][1]: #If the end of the wikipedia article (eg: the "References") is reached, the function terminates and returns the sorted histogram. 
					sorted_filetext = sorted(hist, key = hist.__getitem__, reverse = True) #Sorting the list of all words in the article by their frequency. Most frequent = first.
					return  (sorted_filetext, hist)
				elif word not in common_words:
					if not word.isdigit(): #Is the "word" actually a word, or a number?
						if word in hist: #Is the word in the histogram already?
							hist[word] += 1 #increase word occurence frequency by one
						else:
							hist[word] = 1 #word frequency equals 1
	return

language = 'Hungarian' #The language of choice
title = 'United_States' #The article title of choice

get_text(language, title)
sorted_filetext, hist = open_text(language)

for i in range(1,10):
	print "{}	{}".format(sorted_filetext[i], hist[sorted_filetext[i]]) #Print the top ten words and their frequencies.