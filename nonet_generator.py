""" My Nonet Generator

	What it will do:
	Import a text from Gutenberg 
	Make a Nonet
	(first iteration)
	1st line: contain 9 syllables
	2nd line: contain 8 syllables 
	3rd line: contain 7 syllables 
	...
	9th line: contain 1 syllable

"""

from pattern.en import parsetree
from pattern.en import tag
from pattern.en import pprint

def word_eval(string)
	pprint(parsetree(string, relations = True))
	for word, pos in tag(string):
		if pos == "NN":
			print word

def gutenberg_text_gather(current_URL):

	from pattern.web import *
	buddhist_psalm_text = URL(current_URL).download()
	print buddhist_psalm_text

	# Save data to a file (will be part of your data fetching script)
	f = open('buddhist_psalm_text.pickle','w')
	pickle.dump(all_texts,f)
	f.close()

	# Load data from a file (will be part of your data processing script)
	input_file = open('buddhist_psalm_text.pickle','r')
	reloaded_copy_of_texts = pickle.load(input_file)


def make_dictionary():
	# make dictionary with index, forward, preface, introduction, apendix, all that stuff removed
	# strip all peroids
	pass

def generate_line(text):

	# evaluate text for phrases with 9 syllables that begin with an article or a proper noun
	# use subject of first phrase to determine line 2 with 8 syllables
	# use adj of line 2 to determine line 3 with 7 syllables
	# then randomly choose a search parameter for all following lines with corresponding syllables
	# until final line 9, choose noun randomly
	# return a tuple of all the lines

	# cannot trunkate words
	# do not have to start at begining of sentance
	pass

def build_nonet(tuple_of_lines): 
 	# deconstruct tuple into nonet 
 	# return nonet 
 	pass


print gutenberg_text_gather(current_URL)

