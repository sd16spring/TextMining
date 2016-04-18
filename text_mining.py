# Markov Text Synthesis
# David Papp
import pickle
import praw
import random
import string
import re

def import_data():
	"""
	Reads data from given URL into a .pickle file. This only has to be done once.
	The contents of the .pickle file are then loaded into a string, which is returned.

	"""


	"""from pattern.web import *
	pride_and_prejudice_text = URL('http://www.gutenberg.org/cache/epub/1342/pg1342.txt').download()
	f = open('pride_and_prejudice.pickle','w')
	pickle.dump(pride_and_prejudice_text,f)
	f.close()"""

	# Load data from a file (will be part of your data processing script)
	input_file = open('pride_and_prejudice.pickle','r')
	return pickle.load(input_file)

def markov_text_synthesis_by_degree(degree, text):
	"""
	This function chooses the degree (number of letters) by which text is analyzed.
	For example, a degree of 3 would mean that the program looks at the last 3 characters
	to generate the next character.
	It will then create a nested dictionary of the character sequences, the letters that
	follow those sequences, and the number of times the letters occur after the sequences.
	Many of the words produced will be gidderish, but still interesting.
	"""

	storage = dict()
	next_letters = text[degree:degree*2].lower()
	for i in range(0, len(text) - degree):
		letters = text[i:i + degree].lower()
		if letters not in storage:
			storage[letters] = dict()
		next_letters = text[i + degree:i + degree + 1].lower()
		if next_letters not in storage[letters]:
			storage[letters][next_letters] = 1
		storage[letters][next_letters] += 1
	return storage

def markov_text_synthesis_by_word(text):
	"""
	Creates a nested dictionary of words, the words that follow those words,
	and the number of times the these words follow the previous words.
	"""

	storage = dict()
	index = 0
	while index < len(text):
		end_index = text.find(' ', index, len(text))
		if end_index < 0:
			break
		word = text[index:end_index]
		if word not in storage:
			storage[word] = dict()
		next_word_end_index = text.find(' ', end_index + 1, len(text))
		if next_word_end_index < 0:
			break
		next_word = text[end_index + 1:next_word_end_index]
		if next_word not in storage[word]:
			storage[word][next_word] = 1
		storage[word][next_word] += 1
		index = end_index + 1
	return storage

def display_dictionary(storage, probability_storage):
	"""
	Displays the dictionary in a logical way.
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
	of each word following another word. The probabilities are cumulative so that
	choosing one based on a random number is convenient.
	"""
	probability_storage = dict()
	for i in storage:
		if i not in probability_storage:
			probability_storage[i] = dict()

		total = 0.0
		for j in storage[i]:
			total += storage[i][j]
		previous = 0.0
		for j in storage[i]:
			if j not in probability_storage[i]:
				probability_storage[i][j] = previous + storage[i][j] / total
				previous = probability_storage[i][j]
	return probability_storage


def generate_text_by_degree(degrees, storage, length):
	"""
	Creates a Markov sequence string of a specified length in which each consecutive letter
	is determined based on the probability of the previous letters (the number of letters
	from which decision is made is determined by the degree).
	"""
	sequence = random.choice(storage.keys())
	previous_sequence = sequence
	for j in range(length):
		rand = random.random()
		for i in storage[previous_sequence]:
			if rand <= storage[previous_sequence][i]:
				sequence += str(i)
				previous_sequence = sequence[-degrees::]
				break
	return sequence

def generate_text_by_word(storage, length):
	"""
	Creates a Markov sequence string of a specified length in which each consecutive word
	 is determined based on the probability of the previous word.
	"""

	sequence = random.choice(storage.keys())
	previous_sequence = sequence

	for j in range(length):
		rand = random.random()
		for i in storage[previous_sequence]:
			if rand <= storage[previous_sequence][i]:
				sequence += " " + str(i)
				previous_sequence = str(i)
				break
	return sequence

def strip_text(text):
	"""
	Strips the text of all punction, including line breaks.
	"""

	stripped_text = re.sub(r'[^\w\s]','', text).lower()
	stripped_text = stripped_text.replace('_', '')
	stripped_text = stripped_text.replace('\n', ' ').replace('\r', '')
	return stripped_text

def generate_by_degree():
	""" 
	Main code for doing Markov-text synthesis by degree.
	"""
	reloaded_copy_of_texts = import_data()
	stripped_reloaded_copy_of_texts = strip_text(reloaded_copy_of_texts)
	degrees = 50
	length = 100
	storage = markov_text_synthesis_by_degree(degrees, stripped_reloaded_copy_of_texts)
	probability_storage = convert_to_probability(storage)
	#print stripped_reloaded_copy_of_texts
	#print display_dictionary(storage, probability_storage)
	print generate_text_by_degree(degrees, probability_storage, length)

def generate_by_word():
	"""
	Main code for doing Markov-text synthesis by word. Preferred function.
	""" 

	reloaded_copy_of_texts = import_data()
	stripped_reloaded_copy_of_texts = strip_text(reloaded_copy_of_texts)
	storage = markov_text_synthesis_by_word(stripped_reloaded_copy_of_texts)
	probability_storage = convert_to_probability(storage)
	#print stripped_reloaded_copy_of_texts
	#print display_dictionary(storage, probability_storage)
	print generate_text_by_word(probability_storage, 50)

generate_by_word()
