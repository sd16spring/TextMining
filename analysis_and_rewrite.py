'''Markov analysis of 2 Jane Austen novels used to create a chapter of a novel in the style of Jane Austen'''
import random

pref = ()
suff = {}

def markov(file_name, order = 2):
	'''Maps all possible words (suffixes) that follow a phrase (prefix) in a dictionary. order
	is the number of words in the prefix

	example: {(word1, word2):[suffix1, suffix2, suffix3]'''
	fp = open(file_name)
	for line in fp:
		for word in line.rstrip().split():
			store_word(word.replace('_', ''), order) #italicized words appeared as _word_, which annoyed me
	fp.close
def store_word(word, order = 2):
	'''creates a prefix of length order and then adds suffix values to the keys. This doctest is very sensitive so I had to comment it out while calling 
	my markov function to create a chapter
	# >>> store_word('A')
	# >>> store_word('B')
	# >>> print suff
	# {}
	# >>> store_word('C')
	# >>> print suff
	# {('A', 'B'): ['C']}

		'''
	global pref	#this variable can be referenced outside of this function
	if len(pref) < order:	#if the pref tuple is shorter than the order specified
		pref += (word,)
		return	#ends the function
	try:
		suff[pref].append(word)	#adds word to suffix list
	except:
		suff[pref] = [word]	#initializes a new key in suff

	pref = new_pref(pref, word)
	

def new_pref(tup, word):
	'''creates a new tuple from the original by removing the first element and adding a new word to the end
	>>> new_pref(('word1', 'word2', 'word3'), 'word4')
	('word2', 'word3', 'word4')
	'''
	new = tup[1:] + (word,)	
	return new

def make_title(title_words):
	'''Jane Austen novel titles are known for following the formula "Word 1 and Word 2" ie: "Love and Friendship", 
	"Pride and Prejudice" so I thought my randomly generated book could use a random Jane Austen-y title as well. I put together a list of suitable
	words, both from actual novel titles and not. The function returns a title made up of two randomly chosen words from this list'''
	first_word = random.choice(title_words)	
	second_word = random.choice(title_words)
	title = first_word + ' and ' + second_word
	return title.upper() + '\n by Jane Austen'

def new_text(title_words = [], n = 1000):
	'''Creates the text of the book with a random title and chapter number. If a list is provided, the function can skip using words that do not make 
	sense in the text such as CHAPTER. However, using an excluded words list decreases the word count.
	'''
	while True:
		first_word = random.choice(suff.keys())
		if suff.get(first_word)[0] == suff.get(first_word)[0].upper():
			start = first_word
			break
	title = make_title(title_words)
	passage = title + '\n\n Chapter ' + str(random.randint(1, 25)) + '\n \n'
	for i in range(n):
		suffixes = suff.get(start)
		if suffixes == None:
			new_text(n-i)
			return
		word = random.choice(suffixes)
		if word in exclude_list:
			continue
		passage = passage + ' ' + word
		start = new_pref(start, word)
	return passage

exclude_list = ['CHAPTER']	#it is really fun to see what happens when common words are excluded such as 'the'. 
titles = ['Love', 'Friendship', 'Sense', 'Sensibility', 'Pride', 'Prejudice', 'Romance', 'Marriage', 'Fortune', 'Patience', 'Prudence']
file_list = ['complete_ja_book_only.txt']	#I only included one file in this list because it contains the complete works of JA, but I can easily add more files

for book in file_list:
	markov(book, 2)

chapter = str(new_text(titles, 100))
f = open('ja_chapter.txt', 'w')
f.write(chapter)
f.close


if __name__ == '__main__':
	import doctest
	doctest.testmod()