'''a program that creates new files containing a 
pickled version of Jane Austen's novels Emma and Pride and Prejudice. Mini Project 3'''

import pattern.web 
import pickle 

# pride_and_prejudice_text = pattern.web.URL('http://www.gutenberg.org/cache/epub/1342/pg1342.txt').download()
# emma_text = pattern.web.URL('http://www.gutenberg.org/cache/epub/158/pg158.txt').download()
# complete_jane_austen_text = pattern.web.URL('http://www.gutenberg.org/cache/epub/31100/pg31100.txt').download()

def book_only(file_name):
	'''saves only the novel portion of a Gutenberg book without the introduction
	and conclusion'''
	f = open(file_name, 'r')
	novel = pickle.load(f)
	f.close
	file_name_new = file_name.strip('.txt') + '_book_only.txt'
	f_new = open(file_name_new, 'w')
	flag = False
	for line in novel.split('\n'):
		if line.startswith('*** START'):
			flag = True
		elif line.startswith('*** END'):
			break
		if flag==True:
			f_new.write(line)
	f_new.close


def make_file(file_name, book):
	'''creates a new file for each book and saves the pickled book. 
	This avoids the problem of reaching the download limit on Project Gutenberg's website'''
	f = open(file_name, 'w')
	pickle.dump(book, f)
	f.close()
	

# make_file('pride_and_prejudice.txt', pride_and_prejudice_text)
# make_file('emma.txt', emma_text)
# make_file('complete_ja.txt', complete_jane_austen_text)
# # book_only('pride_and_prejudice.txt')
# # book_only('emma.txt')
# book_only('complete_ja.txt')