import re
import pickle
import string
from string import digits
from nltk.corpus import stopwords

"""
Parse through already downloaded movie scripts/subtitles to reduce to only words
"""

def edited_file_name(movie_script):	
	"""
	Ensure new movie file name is clear

	>>> edited_file_name('StarWars.srt')
	StarWars_edited.txt

	>>> edited_file_name('BTTF.srt')
	BTTF_edited.txt
	"""

	movie_clear = movie_script.replace('.srt', '')
	return '%s' % movie_clear + '_edited.txt'

def edit_all(movie_list):
	"""
	Edit all movie names and all movie subtitles in movie_list
	Increase efficiency
	"""

	for movie in movie_list:
		edit_script(movie)
		new_name = edited_file_name(movie)
		hist = process_script(new_name)

def edit_script(movie_script):
	"""
	Edit original movie subtitles to extract any unnecessary text
	Save as new file
	"""

	new_name = edited_file_name(movie_script)

	original_script = file(movie_script)				# name variable to original version of movie script

	new_script = open(new_name, 'w')					# open new file for writing
	for line in original_script:						# read through original script
		line = line.translate(None, digits)				# remove numbers (0123456789)
		line = re.sub('<.*?>', '', line)				# remove any text between '<>', including the symbols themselves (if text on screen)


		if '-->' not in line and 'Subtitle' not in line and '()' not in line and '^' not in line:		# further parse to reduce to scripted words only
			new_script.write(line)						# write edited lines onto new file
	new_script.close()									# close file

def process_script(file_name):
	"""
	Opens edited script for further parsing
	"""

	hist = dict()
	f1_script = open(file_name)
	for line in f1_script:
		process_line(line, hist)
	return hist

def process_line(line, hist):
	"""
	Reads words in edited script to further extract unnecessary characters
	"""

	stop = set(stopwords.words('english'))				# sets up to remove most common boring words (ex: 'the', 'at', 'me', etc)
	line = line.replace('-', ' ')						# replace hyphens with spaces

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)		# remove punctuation and redundant whitespace
		word = word.lower()								# make all letters lowercase to avoid technical difficulties
		if word not in stop:							# filter out stopwords
			return word
		else:
			pass

		hist[word] = hist.get(word, 0) + 1				# observe frequency of words

# def most_common(hist):								# sorts hist by frequency of words (largest to smallest) instead of by word itself
# 	t = []
# 	for key,value in hist.items():
# 		t.append((value,key))

# 	t.sort(reverse = True)
# 	return t

# def print_most_common(hist, num=10):					# prints out most common words
# 	t = most_common(hist)
# 	print 'The most common words are:'
# 	for freq,word in t[:num]:
# 		print word, '\t', freq



#edit_script('StarWars.srt')
#hist = process_script('blahblah.txt')
#print_most_common(hist, 30)


movies1 = ['StarWars.srt', 'TheGodfather.srt', 'TheMatrix.srt', 'Rocky.srt', 'JurassicPark.srt', 'KillBill1.srt', 'LOTR1.srt', 'ForrestGump.srt']
movies2 = ['Frozen.srt', 'HSM.srt', 'Mulan.srt', 'HarryPotter1.srt', 'FindingNemo.srt', 'Up.srt', 'BTTF.srt']
edit_all(movies1)
edit_all(movies2)