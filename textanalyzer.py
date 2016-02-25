'''This script is a text miner that summarizes word statistics from books from gutenburg and other texts. 
It can handle English and French texts, but handles English texts much better than French texts. 
Author: Xiaozheng Xu
'''
import matplotlib.pyplot as plt
from pattern.web import *
import pattern.fr
import pattern.en
import pickle 
import string
import os 
import shutil
from math import *
from numpy import *

#set up files: can probably also use a automated loop here:
pickle_files=['Austen-Emma.pickle', 'Austen-Love_and_friendship.pickle', 'Austen-Persuasion.pickle', 
'Austen-Sense_and_sensibility.pickle', 'Bronte-Wuthering_heights.pickle', 'Dickens-A_tale_of_two_cities.pickle',
 'Dickens-Great_expectations.pickle', 'judy_november_chopin.txt','Sand-Andre.pickle', 'Sand-Correspondance1.pickle', 
 'Sand-Correspondance2.pickle','Sand-Correspondance3.pickle', 'Sand-Correspondance4.pickle', 'Sand-Correspondance5.pickle', 
 'Sand-Elle_et_lui.pickle', 'Sand-La_mare_au_Diable.pickle', 'Sand-Le_petit_fadette.pickle', 'Sand-Pauline.pickle', 
 'Sand-contes_une_grand_mere.pickle', 'Sand-hiver_a_majorque.pickle', 'prince.pickle']


English_file_names=[pickle_files[i].replace('.pickle','').replace('.txt','') for i in range(8)]
French_file_names=[pickle_files[i].replace('.pickle','') for i in range(8,21)]

English_texts=[] #there are 8 english texts including my own novel in this directory
for i,name in enumerate(pickle_files[:7]):
	input_file=open(name,'r')
	English_texts.append(pickle.load(input_file))
	input_file.close()
with open('judy_november_chopin.txt','r') as myfile:
	English_texts.append(myfile.read().replace('\n',''))

French_texts=[] #there are 13 french texts, the first 12 are by George Sand and the last is the little prince 
for i,name in enumerate(pickle_files[8:]):
	input_file=open(name,'r')
	French_texts.append(pickle.load(input_file))
	input_file.close()


def str_to_words(text,is_gutenburg=True):
	'''
	This function takes in a pickle loaded string, removes its header 
	and split the text into a list of lower case words. 

	In french, the split words can be compound like 'j'ai'
	'''
	#Get rid of heading:
	if is_gutenburg:
		sections=text.split('***') #gutenburg projects start with a ***
		content=max(sections, key=len)

	else: #This means that it's the little prince text or my own novel
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
		and split the text into a list of sentences. pattern.en.tokenize can do the same thing. 
		'''
		if is_gutenburg:
			sections=text.split('***')
			content=max(sections, key=len)
		else: #This means that it's the little prince text or my own
			content=text[60:] 
		content=content.replace('chapitre','')
		content=content.replace('?','.').replace('!','.').replace(';','.').replace('Mr.','Mr').replace('Mrs.','Mrs')
		Sentences=content.split('.')
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
	containing all unique word and their frequencies from most frequent to least.
	'''
	d=histogram(Words)
	t=d.items() #t is a list of tuples 
	for index,pair in enumerate(t):
	    t[index]=(pair[1],pair[0])
	t.sort(reverse=True)
	for index, pair in enumerate(t):
	    t[index]=pair[1],pair[0]
	return t

def sentiment_analysis(text,lang,is_gutenburg=True):
		'''
		This function returns a list of values (as the third returned result) of sentiment tuples for all the sentences in text using pattern's sentiment(). 
		It returns the mean positivity value and mean subjectivity value as the first and second returned results. 
		'''
		List_of_Sentences=str_to_sentences(text)
		values=[]
		if lang=='en':
			for sentence in List_of_Sentences:
				values.append(pattern.en.sentiment(sentence))
		elif lang=='fr':
			for sentence in List_of_Sentences:
				values.append(pattern.fr.sentiment(sentence))
		values=[n for n in values if n[0]!=0] # strip the ones with 0,0 - which means the computer cannot detect the positivity
		mean_positivity=sum([x[0] for x in values])*1.0/len(values)
		mean_subjectivity=sum([x[1] for x in values])*1.0/len(values)
		return (mean_positivity,mean_subjectivity,values)

def plot_histogram_sentiment(dataset,filename):
	'''
	This function plots a list of sentiment tuples (the values in sentiment analysis) 
	as a histogram of the positivity value and a histogram of the subjectivity value
	'''
	fig, axes = plt.subplots(1,2,figsize=(12,4))
	positivity=[n[0] for n in dataset]
	axes[0].hist(positivity,bins=50)
	axes[0].set_title("Sentiment analysis positivity histogram "+filename)
	axes[0].set_xlim(min(positivity), max(positivity))
	axes[0].set_ylabel("Number fo sentences in range")
	axes[0].set_xlabel("Positivity value")

	subjectivity=[n[1] for n in dataset]
	axes[1].hist(subjectivity,bins=50)
	axes[1].set_title("Sentiment analysis subjectivity histogram "+filename)
	axes[1].set_xlim(min(subjectivity), max(subjectivity))
	axes[1].set_ylabel("Number fo sentences in range")
	axes[1].set_xlabel("Subjectivity value")
	plt.show()

def plot_histogram_sentences(dataset,filename):
	'''
	This function plots a histogram of a list of sentence lengths. 	
	'''
	fig, axes = plt.subplots()
	axes.hist(dataset,bins=50)
	axes.set_title("Sentence length histogram: "+filename)
	axes.set_xlim(min(dataset), 400)
	axes.set_ylabel("Number fo sentences in range")
	axes.set_xlabel("Sentence length in characters")
	plt.show()

#The following code plots the sentences histograms 
dataset=str_to_sentences(English_texts[7])
dataset=[len(sentence) for sentence in dataset]
dataset=[n for n in dataset if n<400]
plot_histogram_sentences(dataset,'My_novel')

def compare_similarity(text1,text2):
	'''
	This function compares the similarity between two texts by doing a cosine similarity on their word list histograms. 

	text1 and text2 are strings of text.
	'''
	w1=str_to_words(text1)
	w2=str_to_words(text2)
	d1=histogram(w1)
	d2=histogram(w2)
	dot_product=0
	for key in d1:
		product=d1[key]*d2.get(key,0)
		dot_product+=product
	length1=sqrt(sum([x**2 for x in d1.values()]))
	length2=sqrt(sum([x**2 for x in d2.values()]))
	result=dot_product/1.0/length1/length2
	return result

def print_compare_my_text_with(mytextnumber,filenames,collection):
	'''
	This function generates a text file which list the similarity of mytext compared to all other texts in collection 

	mytextnumber is the index of mytext in collection
	collection is a list of texts (in this script, English_texts and French_texts)
	filenames is a list of file names with indices corresponding to the collection texts. 
	'''
	f=open('/home/xiaozheng/Softdes/TextMining/text_summaries/'+filenames[mytextnumber]+'_text_similarity.txt','w+')
	for i,text in enumerate(collection):
		score=compare_similarity(collection[mytextnumber],collection[i])
		
		f.write('{}{}{:6.4f}{}{}{}'.format(filenames[mytextnumber],' is ',score,' similar to ',
			filenames[i],'\n\n'))
	f.close()

print_compare_my_text_with(6,English_file_names,English_texts)

def generate_summary_statistics(collection,filenames,lang='en'):
	'''
	This function generates several text files containing the summary statistics of texts in a collection,
	regarding their words, sentences and sentiment analysis.

	collection is a list of texts (in this script, English_texts and French_texts)
	filenames is a list of file names with indices corresponding to the collection texts. 
	lang here is only defined as either 'en' or 'fr' (English or French)
	'''
	for i,text in enumerate(collection):
		if i==len(collection): is_gutenburg=False
		else: is_gutenburg=True
		length_of_text=len(text)
		#get word statistics
		List_of_words=str_to_words(text,is_gutenburg)
		Total_words=len(List_of_words)
		Num_unique_words=len(set(List_of_words))
		frequent_words100=most_frequent(List_of_words)[:100]
		#get sentences statistics:
		List_of_Sentences=str_to_sentences(text,is_gutenburg)
		Num_sentences=len(List_of_Sentences)
		avg_sentence_length=length_of_text/Num_sentences
		#Get sentiment statistics
		if lang=='en':
			sent_whole_text=pattern.en.sentiment(text)
		elif lang=='fr':
			sent_whole_text=pattern.fr.sentiment(text)
		mean_sent=sentiment_analysis(text,lang)[0:2]
		f=open('/home/xiaozheng/Softdes/TextMining/text_summaries/'+filenames[i]+'_summary.txt','w')
		f.write('This text is '+ filenames[i]+' \n')
		f.write('This text contains '+str(Total_words)+ ' words\n')
		f.write('The author uses '+str(Num_unique_words)+' Unique words\n')
		f.write('The most frequent 100 words are: \n'+str(frequent_words100).replace("'",'')+'\n') #replace('(','').replace(')','')
		f.write('There are roughly '+str(Num_sentences)+ ' sentences\n')
		f.write('The average sentence contains '+str(avg_sentence_length)+ ' Characters\n')
		f.write('{}{:.3f}{}{:6.3f}{}'.format('The average sentiment value of all sentences is ',
		mean_sent[0],',',mean_sent[1],'\n'))
		f.write('Sentiment is positivity from -1 to 1 and subjectivity from 0 to 1\n')
		f.write('{}{:.3f}{}{:6.3f}{}'.format('The sentiment for the whole text is ',sent_whole_text[0],',',sent_whole_text[1], '\n'))
		f.close()

# generate_summary_statistics(French_texts,French_file_names,lang='fr')
# generate_summary_statistics(English_texts,English_file_names,lang='en')