import pickle
''' 
Downloads Texts from Project Gutenberg and writes to pickle files. 

Done as function declarations so that you can call each text individually, 
because running every one each time may time out access to Project Gutenberg.
'''

def oliver():
	oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
	f = open('some_text_file.pickle','w')
	pickle.dump(oliver_twist_full_text, f)
	f.close()

def wizard():
	wizard_of_oz_full_text = URL('http://www.gutenberg.org/cache/epub/55/pg55.txt').download()
	f = open('wizard_of_oz.pickle','w')
	pickle.dump(wizard_of_oz_full_text, f)
	f.close()

def hamlet():
	hamlet_full_text = URL('http://www.gutenberg.org/cache/epub/1524/pg1524.txt').download()
	hamlet_full_text = hamlet_full_text[hamlet_full_text.find('SCENE.'):]
	f = open('hamlet.pickle','w')
	pickle.dump(hamlet_full_text, f)
	f.close()

def romeo():
	romeo_full_text = URL('http://www.gutenberg.org/cache/epub/1112/pg1112.txt').download()
	romeo_full_text = romeo_full_text[romeo_full_text.find('SCENE.'):]
	f = open('romeo.pickle','w')
	pickle.dump(romeo_full_text, f)
	f.close()

def lear():
	lear_full_text = URL('http://www.gutenberg.org/cache/epub/1128/pg1128.txt').download()
	lear_full_text = lear_full_text[lear_full_text.find('Scene:'):]
	f = open('lear.pickle','w')
	pickle.dump(lear_full_text, f)
	f.close()

def caesar():
	caesar_full_text = URL('http://www.gutenberg.org/cache/epub/1120/pg1120.txt').download()
	caesar_full_text = caesar_full_text[caesar_full_text.find('SCENE:'):]
	f = open('caesar.pickle','w')
	pickle.dump(caesar_full_text, f)
	f.close()

##Uncomment to call functions as necessary.
#oliver()
#wizard()
#hamlet()
#romeo()
#lear()
#caesar()

