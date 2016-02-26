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
	i = 0 
	counter = 0 # how would I increment counter in for loop to get number of sylables
	vowels = ['a','e','i','o','u','y','e '] # what are vowels
	while i < len(string):
		character = string[i]
		if character in vowels: # if char is in vowel list
			if character == 'e ': #if the e is at the end of the word
				return counter # do not add to the syllable counter
			counter = counter + 1
		i = i + 1
	return string, counter


	#look forward to next char

	#if two letter = 1 

print syllable_counter('founde ') 

# """ This will take a string 
# 	Count how many syllables it has 
# 	And return that number of syllables

# 	A syllable is: 
# 	a vowel a e i o u y 
# 	two vowels: ee, ea, oo, oi, ou, ai, ie

# 	It is not: 
# 	e at the end of a word
# """
# def syllable_counter(string):
# 	i = 0 # index of while loop 
# 	counter = 0 # counter of syllables
# 	vowels = ['a','e','i','o','u','y','e '] # what are vowels
# 	diphthongs = ['ee', 'ei', 'ea', 'oo', 'oi', 'oy', 'ou', 'ai', 'ie'] #what are diphthongs
# 	while i < len(string):
# 		character = string[i]
# 		if character in vowels: # if char is in a vowel 
# 			if character == 'e ': #if the e is at the end of the word
# 				return counter # do not add to the syllable counter
# 		counter = counter + 1
# 		i = i + 1
# 	return string, counter


# 	#look forward to next char

# 	#if two letter = 1 syllable 

# print syllable_counter('founde ') 


