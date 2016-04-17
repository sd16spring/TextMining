from pattern.web import *
import pickle 
from pattern.en import tokenize 
import random 

class Nonet_Gen(): 
	def __init__(self,url,syllables,command=False):
		self.url = url 
		self.command = command
		self.raw_text = [] 
		self.clean_text = [] 
		self.sentance = [] 
		self.syllables = syllables
		self.sentance_syllable_counter = 0 


	def get_raw_text(self):
		""" gutenberg_text_gather take a text from gutenberg url
			and stores it to a file. It only pulls from gutenberg 
			when given the command True. By default the command is False. 
			This function outputs self.raw_text, which 
			is a tokenized text file of my gutenberg book. 
		""" 
		if self.command: # If I tell it to load data from url
			buddhist_psalm_text = URL(self.url).download()

			# Save data to a file (will be part of your data fetching script)
			f = open('buddhist_psalm_text.pickle','wb')
			pickle.dump(buddhist_psalm_text,f)
			f.close()

		# Load data from a file (will be part of your data processing script)
		input_file = open('buddhist_psalm_text.pickle','rb')
		# Use pattern to break string of text in to a list of strings where each string is a sentace 
		self.raw_text = tokenize(pickle.load(input_file),) 

	
	def get_clean_text(self):
		""" Input: output form sentance_break (a list of sentance strings)
			Output: a list of strings cleaned of excess text before and after body text 
		"""
		index = 0
		stop = 0
		start = 0

		for sentance in self.raw_text:
			if "* * * END OF THIS PROJECT GUTENBERG EBOOK BUDDHIST PSALMS * * *" in sentance: # this is where psamls stop
				stop = index
				self.clean_text = self.raw_text[0:stop]
			index = index + 1
		for sentance in self.raw_text:
			if "NORTHBROOK SOCIETY, 21 CROMWELL ROAD, KENSINGTON, S.W." in sentance: #  this is where psalms start
				start = index
				self.clean_text = self.raw_text[start:stop]
			index = index + 1
	
	def get_syllable_counter(self,string): 
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

	def get_sentance_syllable_count(self,sentance,syllables): 
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
		self.sentance_syllable_counter = 0 # initiating sentance syllable counter 
		current_sentance = '' # initiating current_sentance string 
		for word in sentance:
			self.sentance_syllable_counter += self.get_syllable_counter(word) #add syllables in sentace 
			if self.sentance_syllable_counter == syllables:
				current_sentance += word # adding together my phrase
				return current_sentance # actually a phrase of the sentance
			elif self.sentance_syllable_counter > syllables: # because I count by words, sometimes a word will push the syllable count over
				return "Failed, try again (error: syllable count too high)" # if this happens I return and error
			elif self.sentance_syllable_counter < syllables: # sometimes a sentance might not have enough syllables
				current_sentance += word
				continue # if that happens move on 
		return "Failed, try again (error: syllable count too low"

	def get_nonet(self): 
		""" Selects random sentances from text list 
			Evaluates number of syllables in text by calling sentance_eval
			Increments number to syllables from syllable_value (9 for a nonet) to 0 
			Input: text
			Output: final poem 
		"""
		f = open('final_nonets.txt','a') # open a file to write to 
		syllable_value = self.syllables
		self.get_raw_text()
		self.get_clean_text()
		while syllable_value > 0: 
			sentance = random.choice(self.clean_text) # select a random sentance from text list
			phrase = self.get_sentance_syllable_count(sentance,syllable_value) # create a phrase with syllable_value x 
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
	nonent = Nonet_Gen(current_URL,9,command=True)
	nonent.get_nonet() 








