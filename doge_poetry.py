""" TITLE: MINI-PROJECT 3
	NAME: EMILY YEH
	DATE: MARCH 12, 2016
	DESCRIPTION: Generates a poem using words from Shakespeare's texts (which I mined from Project Gutenberg's website).
	ADDITIONAL NOTES: I added a 'clean_gutenberg_text' function, added more prepositions to my list, made the final 'poem' function loopable (so it is a little more readable now), and added a bunch of fun new functions! Now, you can choose to feed doge a treat to get happy poems! If you don't feed doge a treat, then doge generates a sad poem!
"""

from pattern.en import sentiment
from string import *
from random import *

def clean_gutenberg_text(file_name):
	""" Cleans up text from a Gutenberg text file.
	"""
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
	return long_lines

def get_word_list(text):
	""" Strips punctuation and whitespace.  Returns a list of the words used in the book as a list. All words are converted to lower case.
	"""
	modified_text = text.lower()
	modified_text = modified_text.translate(None, punctuation)
	words = modified_text.split()
	new_list = [item for item in words]
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
	blank = [i for i in word]
	if blank[-2:] == j:
		rhymes.append(word)
		return rhymes
	else:
		pass

def poem(text, n, stanzas):
	""" Where the magic happens! Takes a text (in this case, Shakespeare, but it can be anything) and a value for the number of words to retrieve, and spits out a doge-ified poem. The poem almost certainly will not make sense, but that's supposed to be a feature, not a bug.
	"""
	word_list = get_top_n_words(get_word_list(clean_gutenberg_text(text)), n)

	for x in word_list:
		rhymes_with_wow(x)

	prepositions = ["above", "across", "after", "at", "upon", "under", "beneath", "over", "beyond", "past", "of", "to", "with", "without", "from", "underneath", "about", "against", "along", "among", "around", "down", "during", "except", "for", "in", "inside", "into", "like", "near", "off", "on", "since", "toward", "through", "upon", "within"]
	i = randint(120, n) # Will give a list of mostly nouns
	j = randint(2, len(prepositions)-1) # Will give a random preposition
	k = randint(8, 120) # Will give mostly personal pronouns, articles, etc.
	r = randint(2, len(rhymes)-1) # Will give a word that rhymes (ish) with wow

	poem = "MINI-PROJECT 3: DOGE WRITES POETRY!\n\n"
	poem += "TITLE: {} {}'s {} {}\n\n".format(word_list[0], word_list[i-200], word_list[i-400], word_list[i-600])

	for y in range(stanzas):
		poem += "{} {}, {} {}, {} {}\n".format(word_list[y], word_list[i-(7*y)], word_list[y], word_list[i-1-(7*y)], word_list[y], word_list[i-2-(7*y)])
		poem += "{} {}, {}, {}\n".format(prepositions[j-y], word_list[i-3-(97*y)], word_list[i-4-(97*y)], rhymes[r-y])
		poem += "{} {}, {} {}, {} {}\n".format(word_list[k-y], word_list[i-5-(47*y)], word_list[k-1-y], word_list[i-6-(47*y)], word_list[k-2-y], word_list[i-7-(47*y)])
		poem += "much {}, very {}, wow\n\n".format(word_list[i-8-(47*y)], word_list[i-9-(5*y)])
		# Why such wonky numbers? Well, 7, 47, and 97 are all prime numbers, so I thought that if I used them, it'd be less likely for the indices to overlap.

	poem += "how did doge do? (such poetry) (many wurdz) (((wow)))\n"
	return poem

def positive_sentiment(text, n, stanzas):
	""" Return an AWESOME poem! Because you gave doge a treat!
	"""
	generated_poem = poem(text, n, stanzas)
	poem_sentiment = sentiment(generated_poem)[0]
	if poem_sentiment > 0:
		polarity = poem_sentiment
	else:
		while poem_sentiment <= 0:
			generated_poem = poem(text, n, stanzas) # Continue generating poems until we get one with a positive polarity
			if sentiment(generated_poem)[0] > 0:
				polarity = sentiment(generated_poem)[0]
				break
	response = "doge's poem... was... AWESOME!!!!!! yayayayay"
	generated_poem += "happiness rating (-1 to +1): {}\n{}\n".format(polarity, response)
	return generated_poem

def negative_sentiment(text, n, stanzas):
	""" Return a sad poem... because you didn't give doge a treat...
	"""
	generated_poem = poem(text, n, stanzas)
	poem_sentiment = sentiment(generated_poem)[0]
	if poem_sentiment < 0:
		polarity = poem_sentiment
	else:
		while poem_sentiment >= 0:
			generated_poem = poem(text, n, stanzas) # Continue generating poems until we get one with a positive polarity
			if sentiment(generated_poem)[0] < 0:
				polarity = sentiment(generated_poem)[0]
				break
	response = "doge's poem...\nwas...\nnot gud... because sad doge is still sad...\ntry feeding doge a treat!"
	generated_poem += "happiness rating (-1 to +1): {}\n{}\n".format(polarity, response)
	return generated_poem

def poem_and_treat(text, n, stanzas):
	""" Allows user to give doge a treat in order to make the poem have a positive polarity (in other words, an awesome poem). Alternatively, if doge is not given a treat, the poem will have a negative polarity (in other words, a sad poem).
	"""
	treat = raw_input("Give doge a treat? (y/n) ") # Feed doge a treat!
	if treat == "y":
		treat_poem = "\nTREAT!!!!!!!1!!!ONE!!!!!\nDOGE WILL MAKE AWESOME POEM!!! FOR TREAT!!!!!!\n\n" + positive_sentiment(text, n, stanzas)
	else:
		treat_poem = "\ntreat? treat??? no...?\nsad doge is sad...\n\n" + negative_sentiment(text, n, stanzas)
	return treat_poem

print poem_and_treat("Shakespeare.txt", 10000, 2)