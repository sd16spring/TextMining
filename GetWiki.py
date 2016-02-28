# -*- coding:utf-8 -*-
from pattern.web import *
import os
import string

def get_text():
	language = 'English'
	title = 'United_States'
	filename = 'en_us_file.txt'

	wiki = Wikipedia(language)

	en_us = wiki.search(title)
	en_us_text = en_us.plaintext()

	en_us_file = open(filename, 'w')
	en_us_file.write(en_us_text.encode("UTF-8"))

	en_us_file.close

def open_text():
	common_words_en = ['the', 'that', 'of', 'and', 'or', 'in', 'to', 'a', 'an', 'is', 'are', 'were', 'was', 'by', 'for', 'as', 'has', 'have', 'had', 'on', 'at', 'with', 'from', 'it', 'its', 'also', 'which', 'while']
	# common_words_ch = ['的'，'是'在''的'，'与'，'或'，'到'，'一个'，'是'，'用“，”对“，”如“，”具有'，'从了', 为'，'有', '它'，'还'，'它'，'而']
	hist = {}

	with open('en_us_file.txt', 'r') as f:
		filetext  = [line.translate(None, string.punctuation).lower() for line in f]
		for line in filetext:
			for word in line.split():
				if word == 'references':
					sorted_filetext = sorted(hist, key = hist.__getitem__, reverse = True)
					return  (sorted_filetext, hist)
				elif word not in common_words_en:
					if not word.isdigit():
						if word in hist:
							hist[word] += 1
						else:
							hist[word] = 1
	return

sorted_filetext, hist = open_text()
for i in range(1,10):
	print "{}	{}".format(sorted_filetext[i], hist[sorted_filetext[i]])