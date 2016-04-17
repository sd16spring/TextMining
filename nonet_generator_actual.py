""" This Mini_Project creates nonets, which a poems of a structure: 
9 syllables
8 syllabes 
...
3 syllables 
2 syllables 
1 syllable 

I use a book of Buddhist Psalms as the source text. This project randomly 
selects sentances from the psalms, evaluates their syllable count and trunates them 
at the desired count. My syllable counter is pretty basic, there are many exceptions to the 
rules that I wrote. For example I assumed any 'e' at the end of a word would be silent which means 
'the' has now syllabe count, when in fact it has one. I also included all major diphthongs in my 
rules, but there are again exceptions. However, I feel this is a good estimation seeing as 
there are masters thesis written on the topic of syllable counting. 

Enjoy the sometimes insightful, but mostly bizzare, poetry! 
"""
from pattern.web import *
import pickle 
from pattern.en import tokenize 
import random 


def gutenberg_text_gather(current_URL,command = False):
	""" gutenberg_text_gather take a text from gutenberg
		and stores it to a file. It only pulls from gutenberg 
		when given the command True. By default the command is False. 
		This function outputs reloaded_copy_of_texts, which 
		is just a text file of my gutenberg book. In this 
		case Buddhist Psalms 
	""" 

	if command: # If I tell it to laod data from url
		buddhist_psalm_text = URL(current_URL).download()

		# Save data to a file (will be part of your data fetching script)
		f = open('buddhist_psalm_text.pickle','wb')
		pickle.dump(buddhist_psalm_text,f)
		f.close()

	# Load data from a file (will be part of your data processing script)
	input_file = open('buddhist_psalm_text.pickle','rb')
	reloaded_copy_of_texts = pickle.load(input_file)
	return reloaded_copy_of_texts


def sentance_break(origin_text):
	""" Input: output text from gutenberg_text_gather
		Output: tokenized text, a list of strings 
		where the strings are the sentances 
	"""
	text = tokenize(origin_text,) # using patter to break string of text apart in to a list of strings where each string is a sentace 
	return text 


def text_clean(text): #cuts out trash text
	""" Input: output form sentance_break (a list of sentance strings)
		Output: a list of strings cleaned of excess text before and after body text 
	"""
	index = 0
	stop = 0
	start = 0

	for sentance in text:
		if "* * * END OF THIS PROJECT GUTENBERG EBOOK BUDDHIST PSALMS * * *" in sentance: # this is where psamls stop
			stop = index
			text = text[0:stop]
		index = index + 1
	for sentance in text:
		if "NORTHBROOK SOCIETY, 21 CROMWELL ROAD, KENSINGTON, S.W." in sentance: #  this is where psalms start
			start = index
			text = text[start:stop]
		index = index + 1
	return text 

def syllable_counter(string):
	""" Takes a word, and evaluates (roughly)
		the number of syllables it contains.
		This function returns number of syllables
		There must be a space after the string,
		otherwise it will break
		>>> syllable_counter('mouse ')
		1
		>>> syllable_counter('a, ')
		1
	"""
	i = 0 # index of while loop 
	counter = 0 # counter of syllables
	vowels = ['a','e','i','o','u','y','e '] # what are vowels
	diphthongs = ['ee', 'ei', 'ea', 'oo', 'oi', 'oy', 'ou', 'ai', 'ie', 'ey', 'ay'] #what are diphthongs
	index = 0 

	while string[index] != ' ': # break at space
		char = string[index] # look at each letter in string
		next_char = string[index+1] # and the letter following
		if char.isalpha():
			if char in vowels: 
				if (char + next_char in diphthongs): 
					counter = counter + 1 # count
					index = index + 1 # skips second letter in diphthong
				elif (char == 'e' and next_char == ' '): # assume if e at end of word, is not syllable
					pass # don't count
				else: 
					counter = counter + 1 # if it's a solitary vowel, add one to counter
		index = index + 1

	return counter


def sentance_eval(sentance,syllable_value):
	""" Takes a sentance, and evaluates
		the number of syllables contained in 
		each word. This function returns number of syllables
		There must be a space after the string,
		otherwise it will break
		>>> sentance_eval('Im a mouse ')
		3
		>>> syllable_counter('She is alone ')
		4
	"""
	sentance_as_list = sentance.split()  # make list of strings (words) 
	sentance = [word + ' ' for word in sentance_as_list] #now with spaces so it works in syllable_counter
	counter = 0 # initiating counter 
	current_sentance = '' # initiating current_sentance string 
	for word in sentance:
		counter += syllable_counter(word) #add syllables in sentace 
		if counter == syllable_value:
			current_sentance += word # adding together my phrase
			return current_sentance # actually a phrase of the sentance
		elif counter > syllable_value: # because I count by words, sometimes a word will push the syllable count over
			return "Failed, try again (error: syllable count too high)" # if this happens I return and error
		elif counter < syllable_value: # sometimes a sentance might not have enough syllables
			current_sentance += word
			continue # if that happens move on 
	return "Failed, try again (error: syllable count too low"

def build_nonet(text):
	""" Selects random sentances from text list 
		Evaluates number of syllables in text by calling sentance_eval
		Increments number to syllables from syllable_value (9 for a nonet) to 0 
		Input: text
		Output: final poem 
	"""

	cleaned_text = text_clean(text)
	syllable_value = 9 # for a nonet
	f = open('final_nonets.txt','a') # open a file to write to 
	while syllable_value > 0: 
		sentance = random.choice(cleaned_text) # select a random sentance from text list
		phrase = sentance_eval(sentance,syllable_value) # create a phrase with syllable_value x 
		if 'Failed' in phrase: # if the count is too high or low
			syllable_value = syllable_value # try again for another line
		else: # if the phrase has the proper syllable count
			syllable_value = syllable_value - 1 # go to next line
			poem = "".join(phrase) # formating 
			f.write(poem + '\n') 
			print poem 
	f.write('\n') 
	f.write('\n')
	f.write('\n')
	f.close()

if __name__ == "__main__":
	current_URL = 'https://www.gutenberg.org/files/7015/7015-0.txt'
	gathered_text = gutenberg_text_gather(current_URL)
	broken_sentance = sentance_break(gathered_text)
	cleaned_text = text_clean(broken_sentance)
	build_nonet(cleaned_text)

# 	import doctest
# 	doctest.testmod()
# 	doctest.run_docstring_examples(syllable_counter, globals(),verbose = True)