"""This will synthesis text based on four books in the Twilight Series by Stephanie Myers"""

"""Max Schommer"""
import pickle
import random
import time


def inner_dictionary(book_cleaner, prefix_length):
	"""
	This creates a dictionary with a mapping from a prefix length(in words) to a list of possible suffixes. 
	"""
	inner_dict = {}

	for i in range(len(book_cleaner)-prefix_length - 1):
		key = tuple(book_cleaner[i: i + prefix_length])
		
		if key in inner_dict:
			myvalue = inner_dict[key]
			my_word = [book_cleaner[i+prefix_length]]
			inner_dict[key] = myvalue +my_word 
			
		else:
			mylist = [book_cleaner[i+ prefix_length]]
			inner_dict[key] = mylist
			
	return inner_dict

def book_cleaner():
	"""
	Opens books, combines them into a single string, and then breaks them into a list of all words. 
	"""
	twilight = list_maker('twilight.txt')
	new_moon = list_maker('new_moon.txt')
	eclipse = list_maker('eclipse.txt')
	breaking_dawn = list_maker('breaking_dawn.txt')
	heart_of_darkness = list_maker('heart_of_darkness.txt')
	hhgttg = list_maker('hhgttg.txt') #Hitch Hikers Guide to the Galaxy
	superbook = twilight + heart_of_darkness +hhgttg#This is the list that the markov chanin uses as its dataset. Combine any books here and that is the resulting dataset.
	
	return superbook

def list_maker(filename):
	"""
	Creates a list of words from a text file, keeping punctuation in tact. 
	"""
	bookraw = open(filename, 'r')
	bookstring = ''
	for line in bookraw:
		bookstring = bookstring + line
	bookstring = bookstring.replace("\n", " ")
	booklist = list(bookstring)
	return booklist

def find_suffix(prefix, list_of_words):
	"""
	This will find all suffixes that could follow a particular prefix, and output a list of all suffixes. 
	"""
	following_words = []
	prefix_length = len(prefix)
	for j in range(len(list_of_words)-prefix_length):
		if tuple(list_of_words[j:j+prefix_length]) == prefix:
			following_words.append(list_of_words[j+prefix_length])
	return following_words



def markov_synthethis(length, textlist, prefix_length, book_dict):
	"""
	Generates a string of word length 'length' by randomly selecting one of the list's words after a pair of words.
	"""
	new_paragraph = ''  #This is the string of the chapter.

	pickle_me_dictionary = book_dict
	upperCase = False
	while upperCase == False:    # This makes sure the paragraph starts with an uppercase letter. 
		rndnum = random.randint(0, len(textlist)-prefix_length)
		mypair = textlist[rndnum:rndnum + prefix_length]
		textgen = mypair
		if mypair[0][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			upperCase = True

	for i in range(length):      #This creates the main text.
		search_for_me = tuple(mypair)
		possible_suffixes = (pickle_me_dictionary[search_for_me])
		rand_suff_int = random.randint(0, len(possible_suffixes) - 1)
		
		suffix = [possible_suffixes[rand_suff_int]]

		textgen = textgen + suffix
		mypair = textgen[-prefix_length:]

	endPunctuation = False

	while endPunctuation == False:   #Waits until the end letter is a period, question mark, or exclamation mark.
		search_for_me = tuple(mypair)
		possible_suffixes = (pickle_me_dictionary[search_for_me])
		rand_suff_int = random.randint(0, len(possible_suffixes) - 1)
		
		suffix = [possible_suffixes[rand_suff_int ]]

		
		textgen = textgen + suffix
		mypair = textgen[-prefix_length:]
		if suffix[0][-1] in ".?!":   #Makes sure a paragraph ends with end punctuation.
			endPunctuation = True

	print_string = ""
	for i in range(len(textgen)):    #Tries to translate unicode into english
		try:
			textgen[i] = (textgen[i].decode('unicode_escape').encode('ascii','ignore'))
		except UnicodeDecodeError:
			pass
	for word in textgen:
		print_string += word
	new_paragraph += "\n" + "    "+  print_string   #Outputs the book, this output can be piped into a text file using the terminal.
	return new_paragraph


def book_maker(chapters, prefix_length):
	"""This is the main function. Call this with a number of chapters, and a prefix length"""
	book_dict = inner_dictionary(book_cleaner(), prefix_length)

	new_book = ''
	for i in range(chapters):
		new_book += "\n" + "Chapter" + " " + str(i+1) + "\n"
		for i in range(10000/300):     #Creates Chapters
			wordsInParagraph = random.randint(100, 500)
			new_book += markov_synthethis(wordsInParagraph, book_cleaner(), prefix_length, book_dict)

	return new_book


print book_maker(13, 8)
