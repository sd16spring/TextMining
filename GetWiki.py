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

	filename = language + '_us_file.txt'

	wiki = Wikipedia(language = dict_lang[language][0])

	article = wiki.search(title)
	article_text = article.plaintext()

	article_file = open(filename, 'w')
	article_file.write(article_text.encode("UTF-8"))

	article_file.close

def open_text(language):
	"""
		Opens the appropriate plaintext file and runs a histogram, creating a dictionary with every non-trivial word that appears and its frequency in the article.
		Outputs a tuple of the original list and the complete sorted version.
	"""
	filename = language + '_us_file.txt'
	if language in dict_lang:
		common_words = set(stopwords.words(language.lower()))
	else:
		common_words = []

	hist = {}

	with open(filename, 'r') as f:
		filetext  = [line.translate(None, string.punctuation).lower() for line in f]
		for line in filetext:
			for word in line.split():
				if word == dict_lang[language][1]:
					sorted_filetext = sorted(hist, key = hist.__getitem__, reverse = True)
					return  (sorted_filetext, hist)
				elif word not in common_words:
					if not word.isdigit():
						if word in hist:
							hist[word] += 1
						else:
							hist[word] = 1
	return
language = 'Hungarian'

get_text(language, 'United_States')
sorted_filetext, hist = open_text(language)

for i in range(1,10):
	print "{}	{}".format(sorted_filetext[i], hist[sorted_filetext[i]])