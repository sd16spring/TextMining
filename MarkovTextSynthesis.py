"""This will synthesis text based on four books in the Twilight Series by Stephanie Myers"""

"""Max Schommer"""
import pickle
import random
from multiprocessing import Pool


def book_cleaner():
	"""
	Opens four books, combines them into a single string, and then breaks them into a list of all words. 
	"""
	twilight = list_maker('twilight.txt')
	new_moon = list_maker('new_moon.txt')
	eclipse = list_maker('eclipse.txt')
	breaking_dawn = list_maker('breaking_dawn.txt')
	superbook = twilight + new_moon + eclipse + breaking_dawn
	return superbook

def list_maker(filename):
	"""
	Creates a list of words from a text file, keeping punctuation in tact. 
	"""
	bookraw = open(filename, 'r')
	bookstring = ''
	for line in bookraw:
		bookstring = bookstring + line
	bookstring = bookstring.replace("\n", "")
	booklist = bookstring.split()
	return booklist
	






def dictionary_mapper(mylist, prefix_length):
	"""
	Makes a dictionary mapping a pair of words with a list of all words that could follow that word.
	This will output that dictionary that the key is a word and the value is a list of all words that come after that word.
	"""
	prob_map = {}
	# booklist = book_cleaner()
	for i in range(len(mylist)-2):
		key = tuple(mylist[i:i+2])
		value = []
		for j in range(len(mylist)-2):
			if tuple(mylist[j:j+2]) == key:
				value.append(mylist[j+2])
		prob_map[key] = value 
	return prob_map




def markov_synthethis(length, textlist):
	"""
	Generates a string of word length 'length' by randomly selecting one of the list's words after a pair of words.
	"""
	pickle_me_dictionary = pickle.load(open("markov_dictionary.p", "rb"))
	# pickle_me_dictionary = {('lol', 'rofl'):['omg', 'wut']}
	rndnum = random.randint(0, len(textlist)-2)
	mypair = textlist[rndnum:rndnum +2]
	textgen = mypair
	for i in range(length):
		search_for_me = (mypair[0], mypair[1])
		# print search_for_me[0], search_for_me[1]
		possible_suffixes = (pickle_me_dictionary[search_for_me])
		rand_suff_int = random.randint(0, len(possible_suffixes) - 1)
		
		suffix = [possible_suffixes[rand_suff_int ]]
		
		textgen = textgen + suffix
		mypair = textgen[-2:]
	print_string = ""
	for word in textgen:
		print_string += " " + word
	print print_string



# markov_dictionary = dictionary_mapper(list_maker('twilight.txt'))
# pickle.dump(markov_dictionary, open("markov_dictionary.p", "w"))
for i in range(13):
	print "\n" + "Chapter" + " " + str(i+1) + "\n"
	markov_synthethis(10000, list_maker('twilight.txt'))