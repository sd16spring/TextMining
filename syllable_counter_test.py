""" This will take a string 
	Count how many syllables it has 
	And return that number of syllables

	A syllable is: 
	a vowel a e i o u y 
	two vowels: ee, ea, oo, oi, ou, ai, ie

	It is not: 
	e at the end of a word
"""
def syllable_counter(string):
	#This only works assuming all words (strings) have a space after them. 
	i = 0 # index of while loop 
	counter = 0 # counter of syllables
	vowels = ['a','e','i','o','u','y','e '] # what are vowels
	diphthongs = ['ee', 'ei', 'ea', 'oo', 'oi', 'oy', 'ou', 'ai', 'ie'] #what are diphthongs
	while i < len(string)-1:
		char = string[i]
		next_char = string[i+1]
		if char in vowels: # if char is a vowel 
			if char + next_char in diphthongs: 
				#char = char + next_char 
				#if char in diphthongs:
				counter =  counter + 1
			elif char + next_char == 'e ': #if the e is at the end of the word
				return counter # do not add to the syllable counter, end of word
			else: 
				counter = counter + 1
		i = i + 1
	return string, counter


	#look forward to next char 

	#if two letter = 1 syllable 

print syllable_counter('founde ') 



