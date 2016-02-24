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
		titles.append(shake_list[place-(i-3):place-5]) #the integers adjust it to not include Willy Shake's by-line, or the year
	return titles

def all_dictionaries(shake_list,cast_locations,titles):
	
	dictionaries=[]
	for j in range(len(cast_locations)):
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
	while not 'SCENE' in shake_list[i] and not 'Scene' in shake_list[i]: #'Scene' always comes at the start of the play
		current_character=[]
		while not shake_list[i]=='ENDLINE':
			current_character.append(shake_list[i])
			i=i+1
		keywords=identify_names(current_character)
		print keywords
		for word in keywords:
			print word
			d[word]=d.get(word, current_character)
			print current_character
		i+=1
		if i-cast_locations[play_number]>=500: #catches if it missed the word scene and just kept iterating through the whole play
			print shake_list[i]
			raise ValueError('Cast finder went for too long')
	d['title']=titles[play_number] #adds the play's title as an entry in the dictionary with the key 'title'
	if d['LEONATUS']==['POSTHUMUS', 'LEONATUS,', 'a', 'gentleman,', 'husband', 'to', 'Imogen']:
		print 'Successfully assigned!'
	else:
		print 'NOT Successfully assigned'
	return d

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
		if len(word)>3:
			keywords=keywords+(word,)
	for word in description: #if a word in the description is in all caps, adds it too
	 	if word.isupper():
	 		keywords=keywords+(word,)
	return keywords




shake_list=create_word_list(complete_shakespeare)

clean_copyright(shake_list)

cast_locations=find_casts(shake_list)

titles=find_titles(shake_list,cast_locations)

d=create_cast_dictionary(shake_list,cast_locations,titles,5)

print d['POSTHUMUS']
print d['LEONATUS']

#print all_dictionaries(shake_list,cast_locations,titles)

#print identify_names(['Tybalt,','nephew','to','Lady','Capulet'] )

