'''This script is a text miner that summarizes word statistics from books from gutenburg'''
from pattern.web import *
from pattern.fr import *
from pattern.en import *
import pickle 
import string
import os 
import shutil
from math import *
from numpy import *


# pickle_files=['Austen-Emma.pickle', 'Austen-Love_and_friendship.pickle', 
# 'Austen-Persuasion.pickle', 'Austen-Sense_and_sensibility.pickle', 
# 'Bronte-Wuthering_heights.pickle', 'Dickens-A_tale_of_two_cities.pickle', 
# 'Dickens-Great_expectations.pickle', 'Sand-La_mare_au_Diable.pickle', 
# 'prince.pickle']
# 20 books from git hub!
pickle_files=['Austen-Emma.pickle', 'Austen-Love_and_friendship.pickle', 'Austen-Persuasion.pickle', 
'Austen-Sense_and_sensibility.pickle', 'Bronte-Wuthering_heights.pickle', 'Dickens-A_tale_of_two_cities.pickle',
 'Dickens-Great_expectations.pickle', 'Sand-Andre.pickle', 'Sand-Correspondance1.pickle', 
 'Sand-Correspondance2.pickle','Sand-Correspondance3.pickle', 'Sand-Correspondance4.pickle', 'Sand-Correspondance5.pickle', 
 'Sand-Elle_et_lui.pickle', 'Sand-La_mare_au_Diable.pickle', 'Sand-Le_petit_fadette.pickle', 'Sand-Pauline.pickle', 
 'Sand-contes_une_grand_mere.pickle', 'Sand-hiver_a_majorque.pickle', 'prince.pickle']

file_names=[pickle_files[i].replace('.pickle','') for i in range(len(pickle_files))]
print file_names

texts=[]
for i,name in enumerate(pickle_files):
	input_file=open(name,'r')
	texts.append(pickle.load(input_file))
	input_file.close()

#to check, get
# for text in texts:
# 	print len(text)

text_Emma=texts[0]
text_Love_and_friendship=texts[1]
text_Persuation=texts[2]
text_Sense_and_sensibility=texts[3]
text_Wuthering_heights=texts[4]
text_A_tale_of_two_cities=texts[5]
text_Great_expectations=texts[6]
text_La_mare_au_diable=texts[7]
text_Prince=texts[8]


def str_to_words(text,is_gutenburg=True):
	'''
	This function takes in a pickle loaded string, removes its header 
	and split the text into a list of lower case words. 

	In french, the split words can be compound like 'j'ai'
	'''
	#Get rid of heading:
	if is_gutenburg:
		# marker='CHAPTER I'
		# header_end_position=text.index(marker)+len(marker)
		# content=text[header_end_position+1:]
		sections=text.split('***')
		content=max(sections, key=len)

	else: #This means that it's the little prince text
		content=text[60:] 

	Words=content.split()
	New_Words=[]
	for i,word in enumerate(Words):
		word=word.strip(string.punctuation+string.whitespace+'*')
		word=word.lower()
		New_Words.append(word) 
	return New_Words 

def str_to_sentences(text,is_gutenburg=True):
		'''
		This function takes in a pickle loaded string, removes its header 
		and split the text into a list of sentences. 
		'''
		if is_gutenburg:
			# marker='START OF THIS PROJECT GUTENBERG EBOOK'
			# header_end_position=text.index(marker)+len(marker)
			# content=text[header_end_position+1:]
			sections=text.split('***')
			content=max(sections, key=len)
		else: #This means that it's the little prince text
			content=text[60:] 
		content=content.replace('chapitre','')
		content=content.replace('?','.').replace('!','.').replace(';','.').replace('Mr.','').replace('Mrs.','')
		Sentences=content.split('.')
		# New_Sentences=[]
		# for i,word in enumerate(Words):
		# 	word=word.strip(string.punctuation+string.whitespace)
		# 	word=word.lower()
		# 	New_Words.append(word) 
		return Sentences 

# print str_to_sentences(text,False)[:30]

def histogram(Words):
	'''
	This function takes a list of words and returns a dictionary with
	(unique word and its frequency) as key-value pairs 
	'''
	d = dict()    
	for c in Words:
	    d[c]=d.get(c,0)+1
	return d 

def most_frequent(Words):
	'''
	This function takes a list of words and returns a list of tuples
	containing each unique word and it's frequency
	'''
	d=histogram(Words)
	t=d.items() #t is a list of tuples 
	for index,pair in enumerate(t):
	    t[index]=(pair[1],pair[0])
	t.sort(reverse=True)
	for index, pair in enumerate(t):
	    t[index]=(pair[1],pair[0])
	return t

# print 'GE has', len(most_frequent(Words_GE)), 'words'

# print 'Emma has', len(most_frequent(Words_Emma)), 'words'

# print 'The most frequent words in Emma are', most_frequent(Words_Emma)[:10]

#get a lists of words for each text:
List_of_words=[]
for i,text in enumerate(texts):
	if i==len(texts)-1: # only the last text prince.pickle is not from gutenburg
		List_of_words.append(str_to_words(text, is_gutenburg=False))
	else:
		List_of_words.append(str_to_words(text))
length_of_texts=[len(x) for x in List_of_words]

# print 'total number of words used for each text is', length_of_texts
# [file_names[i]+': '+str(length_of_texts[i]) for i in range(20)]

#get a list of sentences for each text: 
List_of_Sentences=[]
for i,text in enumerate(texts):
	if i==len(texts)-1: # only the last text prince.pickle is not from gutenburg
		List_of_Sentences.append(str_to_sentences(text, is_gutenburg=False))
	else:
		List_of_Sentences.append(str_to_sentences(text))

Sentences_Prince= List_of_Sentences[18]
# print Sentences_Emma

values=[]
for sentence in Sentences_Prince:
	values.append(sentiment(sentence))
# print values 

mean_positivity=sum([x[0] for x in values])*1.0/len(values)
mean_subjectivity=sum([x[1] for x in values])*1.0/len(values)

print 'sentiment of all sentences in little prince is', (mean_positivity,mean_subjectivity)
print 'sentiment of entire entire little prince is', sentiment(texts[18])


#get the number of unique words used for each text: 
num_words_used=[]
for i,item in enumerate(List_of_words):
	words_used=len(most_frequent(item))
	num_words_used.append(words_used)

# print 'number of unique words used for each text is', num_words_used

# [file_names[i]+': '+str(num_words_used[i]) for i in range(20)]

# This vocabulary richness (ratio of unique words to total length is a pretty bad measurement, cause longer texts perform much worse' 
# Vocabulary_richness=[num_words_used[i]*1.0/length_of_texts[i] for i in range(20)]

# print text.string.encode('utf8')