import random
import pickle
import string

def markhov(book, suffix_dict):
	# Take a book as a string and a dictionary of prefixes mapped to suffixes
	# and update the dictionary (memoization) with the prefixes and suffixes in the book
	order = 2
	suffix_dict['__order'] = order 										   # Packs up the order into the result
	words = book.strip().split(' ')    									   # Strip out punctuation and leading/trailing whitespace, then split it based on spaces
	i = 0
	while i < len(words)-1:												   # My comments said to switch this to a more efficient strip, but it's what makes my 
		if len(words[i])>0:												   # code special; I count punctuation as words. This particular method is a pretty useful
			last = words[i][len(words[i])-1]							   # way to account for mutating a list as I iterate through it.
			if last in string.punctuation:
				words[i] = words[i][:len(words[i])-1]
				words.insert(i+1, last)
				i+=1
		i+=1

	for i in range(order):												   # Iterate through the different starting positions
		for k in range(i, len(words)-order, order):						   # Go through each set of order words starting at i
			prefix = ' '.join(words[k:k+order])							   
			suffix = words[k+order]
			suffix_dict[prefix] = suffix_dict.get(prefix, []) + [suffix]

def open_files():
	# Loads books, which are a list of strings.
	input_file = open('dickens_texts.pickle','r')
	books = pickle.load(input_file)
	return books

def save_files(suffix_dict):
	# Pickles your prefix dict
	f = open('dictionary.pickle', 'w')
	pickle.dump(suffix_dict, f)
	f.close()

books = open_files()
suffix_dict = {}
for book in books:
	markhov(book, suffix_dict)
save_files(suffix_dict)