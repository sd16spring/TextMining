import pickle
''' 
Downloads Texts from Project Gutenberg and writes to pickle files. 

Done as function declarations so that you can call each text individually, 
because running every one each time may time out access to Project Gutenberg.
'''
def pickle_this(filename, url, start_word=None):
	'''Creates a pickled file from the url given at the specified filename.

	Takes parameters:
	filename - filename to write to, including .pickle extension, as string)
	url - url to download from, as a string)
	start_word - optional word to start transcription at
	'''
	text = URL(url).download()
	f = open(filename,'w')
	if not start_word==None:
		f = f[f.find(start_word):]
	pickle.dump(text, f)
	f.close()

	
##Uncomment to call functions as necessary.
# pickle_this('some_text_file.pickle', 'http://www.gutenberg.org/ebooks/730.txt.utf-8')
# pickle_this('wizard_of_oz.pickle', 'http://www.gutenberg.org/cache/epub/55/pg55.txt')
# pickle_this('hamlet.pickle','http://www.gutenberg.org/cache/epub/1524/pg1524.txt', start_word='SCENE.')
# pickle_this('romeo.pickle', 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt', start_word='SCENE.')
# pickle_this('lear.pickle', 'http://www.gutenberg.org/cache/epub/1128/pg1128.txt', start_word='Scene:')
# pickle_this('caesar.pickle', 'http://www.gutenberg.org/cache/epub/1120/pg1120.txt', start_word='SCENE:')
