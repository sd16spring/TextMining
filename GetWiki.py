from pattern.web import *
import os
import string

def get_text():

	enwiki = Wikipedia('English')
	title = 'United_States'


	en_us = enwiki.search(title)
	en_us_text = en_us.plaintext()

	en_us_file = open('en_us_file.txt', 'w')
	en_us_file.write(en_us_text.encode("UTF-8"))

	en_us_file.close

def open_text():
	common_words_en = ['the', 'that', 'of', 'and', 'or', 'in', 'to', 'a', 'an', 'is', 'are', 'were', 'was', 'by', 'for', 'as', 'has', 'have', 'had', 'on', 'at', 'with', 'from', 'it', 'its', 'also', 'which', 'while']
	# common_words_ch = ['那']
	hist = {}

	with open('en_us_file.txt', 'r') as f:
		filetext  = [line.translate(None, string.punctuation).lower() for line in f]
		for line in filetext:
			for word in line.split():
				if word not in common_words_en:
					if not word.isdigit():
						if word in hist:
							hist[word] += 1
						else:
							hist[word] = 1
	sorted_filetext = sorted(hist, key = hist.__getitem__, reverse = True)

	for i in range(1,25):
		print "{}	{}".format(sorted_filetext[i], hist[sorted_filetext[i]])

open_text()