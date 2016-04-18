import random
import pickle
import string

def make_book(suffix_dict):
	# Returns a list of words that form a new book.
	depth = 100
	order = suffix_dict['__order']

	prefix = random.choice(suffix_dict.keys())           						# Chooses a seed prefix
	new_text = prefix.split(' ')
	for i in range(depth):
		if prefix not in suffix_dict.keys():
			prefix = random.choice(suffix_dict.keys())
		suffix = random.choice(suffix_dict[prefix])
		new_text.append(suffix)
		prefix = prefix.split(' ')[order-1] + ' ' + suffix

	return new_text

def polish_book(new_text):
	# Takes a list from make_book and turns it into a book as a string with certain errors removed
	finished_work = []
	for i in range(len(new_text)):
		if new_text[i] in string.punctuation:
			if i ==0 or finished_work[i-1] in string.punctuation:                # Don't start with punctuation, don't do double punctuation.
				finished_work.append('')
			else:																 # No spaces between words and their punctuation
				finished_work.append(new_text[i])
		elif i == len(new_text)-1:												 # Always end your book with a period!
			finished_work.append(' ' + new_text[i] + '.')
		elif i == 0:															 # Don't start with a space!
			finished_work.append(new_text[i])
		else:
			finished_work.append(' ' + new_text[i])
	return ''.join(finished_work).strip()

dict_file = open('dictionary.pickle', 'r')
suffix_dict = pickle.load(dict_file)
dict_file.close()

new_book = polish_book(make_book(suffix_dict))

book_file = open('new_dickens_book', 'w')
book_file.write(new_book)
book_file.close()