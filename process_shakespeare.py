import pickle
import string
# Load data from a file (will be part of your data processing script)
input_file = open('complete_shakespeare.pickle','r')
complete_shakespeare = pickle.load(input_file)
#print complete_shakespeare #lol this is fun to uncomment...

def create_word_list(complete_string):
	"""Takes a string of the complete Shakespeare and splits it into a list of words, while inserting 'ENDLINE' between lines"""
	shake_list_lines=complete_string.splitlines()
	shake_list=[]
	for line in shake_list_lines:
		inner_list=line.split()
		if not inner_list==[]:
			inner_list.append('ENDLINE')
			shake_list.append(inner_list)
	#print shake_list
	new_shake_list=[]
	for inner_list in shake_list:
		for word in inner_list:
			new_shake_list.append(word)
	return new_shake_list
	
cast_list_count=0

def clean_copyright(shake_list):
	"""Takes the works of Shakespeare, formatted as a list of words, and cleans out the copyright info. Does not return new list, rather, it modifies the existing one."""
	copyright_spots=[]
	for i in range(len(shake_list)):
		if shake_list[i] == '<<THIS':
			#print shake_list[i]
			if not shake_list[i+81] == 'MEMBERSHIP.>>': #Checks to make sure you found the whole thing - 81 corresponds to the length of the copyright info in words
				raise ValueError('Found incomplete copyright statement')
			else:
				copyright_spots.append(i)
	#has to delete starting at the back of the list, or else the indices get messed up
	copyright_spots.sort(reverse=True)		
	for spot in copyright_spots:
		del shake_list[spot:spot+82]


def find_casts(shake_list):
	"""Takes the works of Shakespeare,formatted as a list of words
	returns a list of indices for where the word Dramatis is located"""
	cast_locations=[]
	cast_list_count=0
	for i in range(len(shake_list)):
		if "Dramatis" in shake_list[i] or "DRAMATIS" in shake_list[i] :
			cast_list_count+=1
			cast_locations.append(i)
	cast_locations.append(len(shake_list)-1)
	#print cast_list_count
	return cast_locations

def find_titles(shake_list, cast_locations):
	"""Takes the works of Shakespeare formatted as a list of words, and the locations of the word Dramatis
	returns the names of the plays as lists of words"""
	titles=[]
	for place in cast_locations:
		current_word=shake_list[place]
		i=1
		while not current_word.isdigit(): #isdigit works cuz I'm finding the year the play was written, which always proceeds the title
			current_word=shake_list[place-i]
			i+=1
		title_section=shake_list[place-(i-3):place-5] #the integers adjust it to not include Willy Shake's by-line, or the year
		title=''
		for word in title_section:
			title+=(word+' ')
		titles.append(title) 
	return titles

def all_dictionaries(shake_list,cast_locations,titles):
	
	dictionaries=[]
	for j in range(len(cast_locations)-1):
		d=create_cast_dictionary(shake_list,cast_locations,titles,j)
		dictionaries.append(d)
	return dictionaries

def create_cast_dictionary(shake_list,cast_locations,titles,play_number):
	"""Takes the works of Shakespeare formatted as a list of words, and the locations of the word Dramatis, the play's titles, and which play it is
	Iterates through the word list from Dramatis until the start of the play
	Using the line seperation between characters, creates an individual list of words for each character
	Stores these lists in a dictionary where the key is a tuple of keywords from the identify names function
	returns the dictionary""" 
	d=dict()
	i=cast_locations[play_number]+3 #adjusts for 'Dramatis', 'Personae', and 'ENDLINE'
	uppers=0
	lowers=0
	while not 'SCENE' in shake_list[i] and not 'Scene' in shake_list[i]: #'Scene' always comes at the start of the play
		character_values=create_character(shake_list,i)
		#print character_values[2]
		for word in character_values[1]:
			d[word]=d.get(word,(0,0))
			if word.isupper:
				uppers+=1
			else:
				lowers+=1
			#print word
		i=character_values[0]
		# if i-cast_locations[play_number]>=500: #catches if it missed the word scene and just kept iterating through the whole play
		# 	print shake_list[i]
		# 	raise ValueError('Cast finder went for too long')
	d['TITLE']=titles[play_number] #adds the play's title as an entry in the dictionary with the key 'title'
	d['begin play']=i
	if uppers>lowers:
		d['capitals?']=True
	else:
		d['capitals?']=False
	return d

def create_character(shake_list,current_index):
	"""Takes where the current character starts and 
	returns a tuple with the word after it ends, a tuple of keywords, and a list that represents the full charcater entry"""
	character=[]
	i=current_index
	while not shake_list[i]=='ENDLINE': #creates character name
			character.append(shake_list[i])
			i=i+1
	keywords=identify_names(character) #gets the keywords from the identify names function
	new_start=i+1
	res=(new_start,keywords,character)
	return res

def identify_names(name_line):
	"""Takes a line of the cast list, and returns a tuple of the keywords that could be used to refer to that character for the rest of the play"""
	name=name_line
	description=[]
	keywords=tuple()
	for i in range(len(name_line)): #Check if line has "name" and "description" parts seperated by a comma or period. If so, split them up.
		current_word=name_line[i]
		if current_word[-1]==',' or current_word[-1]=='.':
			name=name_line[:i+1]
			description=name_line[i+1:]
			#print 'name:',
			#print name
			break
	for word in name: #adds all the longer words in the name section as keywords
		word = word.rstrip(string.punctuation)
		if len(word)>3:
			keywords=keywords+(word,)
	for word in description: #if a word in the description is in all caps, adds it too
		word = word.rstrip(string.punctuation)
		if word.isupper():
			keywords=keywords+(word,)
	return keywords

def find_lines(shake_list,cast_dictionary,cast_locations,play_number):
	"""Takes Shakespeare's works as a list, and a cast dictionary, and where the play starts in the word list and which one it is
	modifies the dictionary so that the character's names correspond to a tuple where the first entry is the number of lines in pentameter and the second is the character's total lines
	"""
	line_starts=[]
	i=cast_locations[play_number]
	if cast_dictionary['capitals?']==True: #If the play is formatted with all caps, the character's lines will start with their names
		while i < cast_locations[play_number+1]: #this finds where the lines starts
			for key in cast_dictionary: #APPARENTLY SOME OF THEM ARE NAMES FOLLOWED BY PUNCUATION SO INSTEAD OF JUST LOOKING IT UP IN THE DICTIONARY I GET TO DO THIS WHICH TAKES FOREVER
				if key in shake_list[i]:
					line_starts.append(i)
					shake_list[i]=key
			i+=1
		for j in range(len(line_starts)-1): #for all the places where lines starts, this checks each for pentameter
			line=line_starts[j]
			name=shake_list[line]
			current_character=cast_dictionary[name]
			#print name,
			#print current_character
			classiness=current_character[0]
			if is_pentameter(shake_list[(line_starts[j]):(line_starts[j+1]-1)]):
				classiness=current_character[0]+1 #increment number of classy lines if the line is pentameter
			total_lines=current_character[1]+1 #incement total number of lines regardless
			cast_dictionary[name]=(classiness,total_lines)
	if cast_dictionary['capitals?']==False: #If the play isn't formatted with all caps characters, the character's lines may start with an abbreviation of their name
		while i < cast_locations[play_number+1]:
			current_word=shake_list[i]
			previous_word=shake_list[i-1]
			if current_word[-1]=='.' and previous_word=='ENDLINE':
				for keyword in cast_dictionary:
					if current_word[:-1] in keyword:
						line_starts.append(i)
			i+=1
		for j in range(len(line_starts)-1):
			current_character=cast_dictionary[line_starts[j]]
			if is_pentameter(shake_list[(line_starts[j]):(line_starts[j+1])]):
				current_character[0]+=1 #increment number of classy lines if the line is pentameter
			current_character[1]+=1 #incement total number of lines regardless


def is_pentameter(line):
	"""Takes a character's line, and checks if it's in pentameter"""
	total_syllables=0
	#print line
	for word in line:
		if word=='ENDLINE':
			break
		total_syllables+=CountSyllables(word)
	if total_syllables==10:
		return True
	else:
		return False

def CountSyllables(word, isName=True):
	"""I wanted to use pattern to count syllables, but couldn't find any documentation for how. I grabbed this counter off GitHub instead, at https://github.com/DigTheDoug/SyllableCounter/blob/master/SyllableCounter.py"""
	vowels = "aeiouy"
	#single syllables in words like bread and lead, but split in names like Breanne and Adreann
	specials = ["ia","ea"] if isName else ["ia"]
	specials_except_end = ["ie","ya","es","ed"]  #seperate syllables unless ending the word
	currentWord = word.lower()
	numVowels = 0
	lastWasVowel = False
	last_letter = ""

	for letter in currentWord:
		if letter in vowels:
			#don't count diphthongs unless special cases
			combo = last_letter+letter
			if lastWasVowel and combo not in specials and combo not in specials_except_end:
				lastWasVowel = True
			else:
				numVowels += 1
				lastWasVowel = True
		else:
			lastWasVowel = False

		last_letter = letter

	#remove es & ed which are usually silent
	if len(currentWord) > 2 and currentWord[-2:] in specials_except_end:
		numVowels -= 1

	#remove silent single e, but not ee since it counted it before and we should be correct
	elif len(currentWord) > 2 and currentWord[-1:] == "e" and currentWord[-2:] != "ee":
		numVowels -= 1

	return numVowels


shake_list=create_word_list(complete_shakespeare)

clean_copyright(shake_list)

cast_locations=find_casts(shake_list)

titles=find_titles(shake_list,cast_locations)

all_d=all_dictionaries(shake_list,cast_locations,titles)


for i in range(len(all_d)):
	find_lines(shake_list,all_d[i],cast_locations,i)

person=raw_input('Which character would you like to see?')

for play in all_d:
	if person in play:
		current_character=play[person],
		print 'This character is in the play',
		print play['TITLE'],
		print 'and has'
		#print current_character
		another_tuple=current_character[0]
		print another_tuple[1],
		print 'total lines,',
		print another_tuple[0],
		print 'of which are in iambic pentameter.'




#HERE LIES MY UNIT TEST GRAVEARD

#d=create_cast_dictionary(shake_list,cast_locations,titles,5)

#find_lines(shake_list,d,cast_locations,5)


# print CountSyllables('POSTHUMUS')
# print CountSyllables('dagger')
# print CountSyllables('would')


#print shake_list[590865:590900]
# print d['POSTHUMUS']
# print d['LEONATUS']

#print identify_names(['Tybalt,','nephew','to','Lady','Capulet'] )

