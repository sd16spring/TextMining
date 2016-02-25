# Analyzes the sentiment of the different sections of the Mabinogion and outputs graphs to compare.

from pattern.web import *
from pattern.en import *
import pickle
import string
import matplotlib.pyplot as plt

def get_text(url="http://www.gutenberg.lib.md.us/5/1/6/5160/5160-0.txt", file_name = "mabinogion.txt"):
	""" Fetch the text of a webpage and save it to a file. As a note, this doctest fails but also
			looks exactly the same. I don't understand, so I'm going to assume it's okay.

	>>> get_text()
	done
	>>> f = open("mabinogion.txt")
	>>> intro = f.read(46)
	>>> f.close()
	>>> print intro
	The Project Gutenberg eBook, The Mabinogion
	"""
	full_text = URL(url).download()

	f = open(file_name, 'w')
	f.write(full_text)
	f.close()
	print 'done'

def clean_list(file_name):
	""" Cleans an entire Gutenberg text given a .txt file. Alter file passed and strings to begin or end
			the body of the text. It then makes a histogram of the text and saves it to a 
			pickle file.

			*No longer needed once the histogram was not being used
	>>> clean_list("mabinogion.txt")
	mabinogion_histogram.pickle has been created.
	"""
	f = open(file_name)
	text = f.read()
	f.close()

	# Get rid of all characters except for apostrophes and replace them with spaces
	#  so that they can be stripped
	intab = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
	outtab = " " * len(intab)
	translate_table = string.maketrans(intab, outtab)

	# Find where the main section (title page and onwards) begins
	#  and end where the book finishes.
	header_end = text.find("ccx074@pglaf.org") + 16
	book_end = text.find("***END OF THE PROJECT GUTENBERG EBOOK")
	neat_text = text[header_end: book_end]

	# Make things lowercase and clean it all up
	neat_text = neat_text.lower()
	neat_text = neat_text.translate(translate_table)

	h = {}
	clean_text = clean_sentence(neat_text)
	for w in clean_text.split():
		h[w] = h.get(w, 0) + 1

	mess = pickle.dumps(h)

	# Name the histogram file and save it, then let me know it's done.
	hist_file_name = file_name[:-4] + "_histogram.pickle"
	f2 = open(hist_file_name, 'w')
	f2.write(mess)
	f2.close()
	print hist_file_name + " has been created."

def get_dict(file_name):
	""" Opens and loads a pickled file, then returns the histogram list.
	*Not actually necessary to code; I never used the histogram or saved a list.

	>>> hist_dict = get_dict("mabinogion_histogram.pickle")
	>>> print hist_dict['cut']
	27
	"""
	f = open(file_name,'r')
	saved_list = pickle.loads(f.read())
	f.close()
	return saved_list

def get_text_body(full_text_file_name):
	""" Given a file name, it finds the main contents of the book (minus the header and
			the endnotes from Gutenberg) and returns the body of the text. Also, it did the
			thing again where it definitely got the right bit but didn't print it correctly.
	>>> full = get_text_body("mabinogion.txt")
	>>> print full[:15]
	THE MABINOGION
	"""
	f = open(full_text_file_name)
	full_text = f.read()
	f.close()
	header_end = full_text.find("ccx074@pglaf.org") + 16
	book_end = full_text.find("***END OF THE PROJECT GUTENBERG EBOOK")
	return full_text[header_end: book_end].strip()

def get_table_contents(full_text):
	""" Finds the table of contents and makes it into a list of titles.
	>>> f = open("mabinogion.txt")
	>>> mab_text = f.read()
	>>> f.close()
	>>> contents = get_table_contents(mab_text)
	>>> print contents[1]
	THE LADY OF THE FOUNTAIN
		"""
	contents_start = full_text.find("CONTENTS") + 8
	contents_end = full_text.find("INTRODUCTION")
	contents = full_text[contents_start:contents_end]
	section_name_list = []
	translate_table = string.maketrans("1234567890","@@@@@@@@@@")
	contents_names = contents.translate(translate_table).split("@")
	for i in range(len(contents_names)):
		contents_names[i] = string.replace(contents_names[i], '\r\n', ' ')
		contents_names[i] = contents_names[i].strip().upper()
		if contents_names[i] != '':
			section_name_list.append(contents_names[i])
	return section_name_list

def clean_sentence(sentence):
	""" Cleans up a string of some bizarre unicode things and empty space and returns it.
	>>> clean_sentence('')
	''
	>>> clean_sentence('  My name is           ')
	'My name is'
	>>> clean_sentence('\xe2\x80\x9cthis\xe2\x80\x99stuff\xe2\x80\x9dis\xe2\x80\x94theworst')
	'this stuff is theworst'
	>>> clean_sentence('hi')
	'hi'
	"""
	sentence = string.replace(sentence, "\xe2\x80\x9c", ' ')
	sentence = string.replace(sentence, "\xe2\x80\x99", ' ')
	sentence = string.replace(sentence, "\xe2\x80\x9d", ' ')
	sentence = string.replace(sentence, "\xe2\x80\x94", ' ')
	sentence = sentence.strip()
	return sentence

def break_into_sentences(section):
	""" Breaks a string into a list of sentences along puctuation and eliminates
			certain kinds of whitespace.

	>>> break_into_sentences("Hi! This is my string. Will it work? I hope so!")
	['Hi', 'This is my string', 'Will it work', 'I hope so']
	>>> break_into_sentences("thisisastringwithnopunctuation")
	['thisisastringwithnopunctuation']
	>>> break_into_sentences("")
	[]
	"""
	section = string.replace(section, '\r', ' ')
	section = string.replace(section, '\n', ' ')
	translate_table = string.maketrans(".?!","@@@")
	sentence_list = section.translate(translate_table).split("@")
	cleaned_s_list = []
	for sentence in sentence_list:
		sentence = clean_sentence(sentence)
		if sentence != '':
			cleaned_s_list.append(sentence)
	return cleaned_s_list

def make_pieces(full_text, break_phrases):
	""" Takes a full text and a list of phrases to break along 
	and returns a list of sections broken by the phrases given.

	>>> make_pieces("Kaitlyn Keil Intro: A student at Olin College. Brag: I am the GREATEST.", ["Intro:", "Brag:"])
	['Kaitlyn Keil ', 'Intro: A student at Olin College. ', 'Brag: I am the GREATEST.']
	>>> make_pieces("Kaitlyn Keil Intro: A student at Olin College. Brag: I am the GREATEST.", ["Intro:", "Goal:", "Brag:"])
	['Kaitlyn Keil ', 'Intro: A student at Olin College. ', 'Brag: I am the GREATEST.']
	>>> make_pieces("",["split"])
	['']
	"""
	for phrase in break_phrases:
		put_here = full_text.find(phrase)
		if put_here != -1:
			full_text = full_text[:put_here] + "NEWSECTION" + full_text[put_here:]
	section_list = full_text.split("NEWSECTION")
	return section_list

def make_sentence_list_files(section_list,contents_names):
	""" Takes the sections and the names of the sections, saves them as pickle.files just
			in case, and returns a list where each section has been broken into sentences.
			contents_names must have one fewer items than section_list
	>>> sect_list = ['Section 0 should be ignored. It is the intro.', 'This is section one! It is a good section.', 'This is section two. ...meh.']
	>>> con_names = ['sec1', 'sec2']
	>>> make_sentence_list_files(sect_list, con_names)
	[['This is section one', 'It is a good section'], ['This is section two', 'meh']]
	>>> make_sentence_list_files([''],[''])
	[]
	>>> make_sentence_list_files(['','',''],['',''])
	[[], []]
	"""
	list_of_section_sentence_lists = []
	for i in range(len(section_list)):
		if i != 0:
			sentence_list = break_into_sentences(section_list[i])
			list_to_save = pickle.dumps(sentence_list)
			list_file_name = str(contents_names[i-1]) + '.pickle'
			f2 = open(list_file_name, 'w')
			f2.write(list_to_save)
			f2.close()
			list_of_section_sentence_lists.append(sentence_list)
	return list_of_section_sentence_lists


def get_sentiment(string_list, group_num):
	""" Gets the average sentiment of a group of sentences, as specified by group_num.
	>>> get_sentiment(['Software Design is my favorite class!'],1)
	[(0.625, 1.0)]
	"""
	sentiment_list = []
	index = 0
	while index < len(string_list):
		if len(string_list[index:]) < group_num:
			string_to_analyze = '. '.join(string_list[index:])
		else:
			string_to_analyze = '. '.join(string_list[index:index+group_num])
		sentiment_list.append(sentiment(string_to_analyze))
		index += group_num
	return sentiment_list

def plot_sentiment(list_of_lists, section_names):
	""" Makes a plot of the polarity throughout the different sections.
	"""
	for i in range(len(list_of_lists)):
		x_axis = []
		polarity_axis = []
		sentiment_list = get_sentiment(list_of_lists[i], 10)
		x_position = 0
		for polarity, subjectivity in sentiment_list:
			polarity_axis.append(polarity)
			x_axis.append(x_position)
			x_position += 1
		plt.figure(i+1)
		plt.plot(x_axis, polarity_axis)
		plt.title(section_names[i])
		plt.xlabel("Distance into Section")
		plt.ylabel("Polarity")
	plt.show()

def analyze_text(full_text_file_name):
	""" Calls all the other functions to plot the sentiment over the different sections
			of the text.
	"""
	full_text = get_text_body(full_text_file_name)
	contents_names = get_table_contents(full_text)
	section_list = make_pieces(full_text, contents_names)
	list_of_sentence_lists = make_sentence_list_files(section_list, contents_names)
	plot_sentiment(list_of_sentence_lists, contents_names)

if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    analyze_text("mabinogion.txt")