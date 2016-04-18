# Markov Text Synthesis
# David Papp
"""
Changes:
- Paramaterized URL to import from. 
- Choose whether to read text in from URL or pickle file
- Cleaned up the dictionary creation by using the .get and .split function
- Increased the efficiency of stripping text by using .translate
- Removed all functions that generated Markov text by degree.
- Added comments and improved docstrings.
"""
import pickle
import praw
import random
import string
import re

def import_data(URL_path, from_file):
	"""
	If from_file is false, data is read from given URL into a .pickle file. This only has to be done once.
	Otherwise, the contents of the existing .pickle file are loaded into a string, which is returned.
	"""
	if not from_file:
		from pattern.web import *
		pride_and_prejudice_text = URL(URL_path).download()
		f = open('pride_and_prejudice.pickle', 'w')
		#store text in a .pickle file for future use.
		pickle.dump(pride_and_prejudice_text,f)
		f.close()
	input_file = open('pride_and_prejudice.pickle', 'r')
	return pickle.load(input_file)

def markov_text_synthesis_by_word(text):
	"""
	Creates a nested dictionary of words, the words that follow those words,
	and the number of times the these words follow the previous words.
	"""
	#put the words into a list
	words = text.split()
	storage = dict()

	previous_word = ""
	for word in words:
		#if this word has not occured yet, create an empty dictionary for it.
		if previous_word not in storage:
			storage[previous_word] = dict()

		#If this word has not followed the previous one, it is added to the dictionary.
		#Otherwise, increment the number of occurances by 1.	
		storage[previous_word][word] = storage[previous_word].get(word, 0) + 1

		#updates previous_word
		previous_word = word

	return storage

def display_dictionary(storage, probability_storage):
	"""
	Displays the words found in the text and the frequency at which other
	words follow them.
	"""
	print "Letters: "
	total = 0
	for i in storage:
		print "\n After the word", i
		print "------------------------------------------"
		for j in storage[i]:
			print i, "->" , j, storage[i][j], "times, with frequency", probability_storage[i][j]
			total += storage[i][j]

def convert_to_probability(storage):
	"""
	Returns a new dictionary based on another dictionary but with the relative probability
	of each word following another word (instead of frequency). The probabilities are 
	cumulative so that choosing one based on a random number is convenient.
	"""
	#create a new dictionary to copy into
	probability_storage = dict()
	for i in storage:
		probability_storage[i] = dict()

		#adds up occurances of different words after each word, then divides by total occurances to get probability
		total = 0.0
		for j in storage[i]:
			total += storage[i][j]
		previous = 0.0

		#copies probabilities into new dictionary
		for j in storage[i]:
			probability_storage[i][j] = previous + storage[i][j] / total
			previous = probability_storage[i][j]

	return probability_storage

def generate_text(storage, length):
	#choose a word randomly to start with
	sequence = random.choice(storage.keys())

	previous_sequence = sequence
	for j in range(length):
		#choose word from dictionary based on their probabilities
		rand = random.random()
		for i in storage[previous_sequence]:
			if rand <= storage[previous_sequence][i]:
				#add word to sequence
				sequence += " " + str(i)
				previous_sequence = str(i)
				break
	return sequence

def strip_text(text):
	"""
	Strips the text of all punction, including line breaks.
	Now uses string.translate, which is much faster than the previously
	used string.replace.
	"""
	return text.translate(string.maketrans("",""), string.punctuation).lower()

def generate(URL, from_file, length):
	#loads the text into a string
	reloaded_copy_of_texts = import_data(URL, from_file)

	#strips the text of unwanted punctuation, linebreaks, etc...
	stripped_reloaded_copy_of_texts = strip_text(reloaded_copy_of_texts)

	#create a dictionary of the frequencies of words following different words
	storage = markov_text_synthesis_by_word(stripped_reloaded_copy_of_texts)

	#creates a new dictionary with the relative probability of words following each other
	probability_storage = convert_to_probability(storage)

	#optional: display created dictionaries
	display_dictionary(storage, probability_storage)

	#returns generated text
	return generate_text(probability_storage, length)

if __name__ == '__main__':
	#First argument is the URL.
	#Second argument is whether the text should be downloaded or read from a pickle file.
	#Third argument is the desired length of the output.

	URL_path = 'http://www.gutenberg.org/cache/epub/1342/pg1342.txt'
	print generate(URL_path, True, 1000)
