""" TITLE: MINI-PROJECT 3
	NAME: EMILY YEH
	DATE: MARCH 12, 2016
	DESCRIPTION: Generates a poem using words from Shakespeare's texts (which I mined from Project Gutenberg's website).
	ADDITIONAL NOTES: Sorry this is late! Since everyone else was working on this during the two weeks I was in the hospital, I thought that it would probably be okay if I worked on it during the week of spring break, after Mini-Project 4 was over. Thanks for your patience and understanding!
"""

from string import *
from random import *

def get_word_list(file_name):
	""" Strips punctuation and whitespace.  Returns a list of the words used in the book as a list. All words are converted to lower case.
	"""
	new_list = []

	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	end_line = 0
	while lines[curr_line].find('["Small Print" V.12.08.93]') == -1:
		curr_line += 1
	while lines[end_line].find("End of the Project Gutenberg EBook") == -1:
		end_line -= 1
	lines = lines[curr_line + 1:end_line] # Cleaning up the text

	long_lines = ''.join(str(e) for e in lines)
	long_lines = long_lines.replace("<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM\nSHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS\nPROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE\nWITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE\nDISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS\nPERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED\nCOMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY\nSERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>", "")
	long_lines = long_lines.lower()
	long_lines = long_lines.translate(None, punctuation)

	words = long_lines.split()
	for item in words:
		new_list.append(item)

	return new_list

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently occurring words, ordered from most to least frequently occurring.
	"""
	word_counts = dict()
	for word in word_list:
		word_counts[word] = 1 + word_counts.get(word,0)

	words_list = word_counts
	sorted_list = sorted(words_list.items(), key = lambda x: x[1])
	final_list = []

	i = -1
	while i > ((-1 * n) - 1):
		final_list.append(sorted_list[i])
		i -= 1

	list_without_numbers = [x[0] for x in final_list]

	return list_without_numbers

rhymes = []

def rhymes_with_wow(word):
	""" Takes a word and checks to see if it rhymes with wow by checking if the last two letters are 'o' and 'w'. (Note: Some words that end in -ow don't actually rhyme with wow, but that's okay.)
	"""
	j = ['o', 'w']
	blank = []
	for i in word:
		blank.append(i)
	if blank[-2:] == j:
		rhymes.append(word)
		return rhymes
	else:
		pass

def poem(text, n):
	""" Where the magic happens! Takes a text (in this case, Shakespeare, but it can be anything) and a value for the number of words to retrieve, and spits out a doge-ified poem. The poem almost certainly will not make sense, but that's supposed to be a feature, not a bug.
	"""
	word_list = get_top_n_words(get_word_list(text), n)

	for x in word_list:
		rhymes_with_wow(x)

	prepositions = ["above", "across", "after", "at", "upon", "under", "beneath", "over", "beyond", "past", "of", "to", "with", "without", "from"]
	i = randint(120, n) # Will give a list of mostly nouns
	j = randint(2, len(prepositions)-1) # Will give a random preposition
	k = randint(8, 120) # Will give mostly personal pronouns, articles, etc.
	r = randint(2, len(rhymes)-1) # Will give a word that rhymes (ish) with wow

	poem = "mini-project 3: doge writes poetry!\n\n"
	poem += "title: {} {}'s {} {}\n\n".format(word_list[0], word_list[i-200], word_list[i-400], word_list[i-600])

	# Stanza 1
	poem += "{} {}, {} {}, {} {}\n".format(word_list[0], word_list[i], word_list[0], word_list[i-1], word_list[0], word_list[i-2])
	poem += "{} {}, {}, {}\n".format(prepositions[j], word_list[i-3], word_list[i-4], rhymes[r])
	poem += "{} {}, {} {}, {} {}\n".format(word_list[k], word_list[i-5], word_list[k-1], word_list[i-6], word_list[k-2], word_list[i-7])
	poem += "much {}, very {}, wow\n\n".format(word_list[i-8], word_list[i-9])

	# Stanza 2
	poem += "{} {}, {} {}, {} {}\n".format(word_list[1], word_list[i-10], word_list[1], word_list[i-11], word_list[1], word_list[i-12])
	poem += "{} {}, {}, {}\n".format(prepositions[j-1], word_list[i-13], word_list[i-14], rhymes[r-1])
	poem += "{} {}, {} {}, {} {}\n".format(word_list[k-3], word_list[i-15], word_list[k-4], word_list[i-16], word_list[k-5], word_list[i-17])
	poem += "so {}, such {}, wow\n\n".format(word_list[i-18], word_list[i-19])

	# Stanza 3
	poem += "{} {}, {} {}, {} {}\n".format(word_list[9], word_list[i-20], word_list[9], word_list[i-21], word_list[9], word_list[i-22])
	poem += "{} {}, {}, {}\n".format(prepositions[j-2], word_list[i-23], word_list[i-24], rhymes[r-2])
	poem += "{} {}, {} {}, {} {}\n".format(word_list[k-6], word_list[i-25], word_list[k-7], word_list[i-26], word_list[k-8], word_list[i-27])
	poem += "much {}, VERY {}, wow".format(word_list[i-28], word_list[i-29])

	return poem

print poem("Shakespeare.txt", 10000)