#Joseph Lee
#Text Mining Project for Software Design
#This document contains the code used to compare word frequencies between the 
#Douay Rheims bible and the third revision of the Koran.  The goal was to look for
#possible similarities between the two religions

#Helper functions:
import pickle


def strip_punc(string):
	from string import punctuation
	return ''.join(c for c in string if c not in punctuation)#return a string without any punctuation


def histogram(list_of_words):
    d = dict()
    for word in list_of_words:
        d[word]=d.get(word,0)+1#   This function creates a dictionary of all the words in the string and the number of times they appear
    return d

def sort_most_frequent(d):
    t = []
    for word, frequency in d.iteritems():
        t.append((frequency, word))#      This creates a list of all the items in the dictionary h
    t.sort(reverse=True)
    return t




#_________________________________________________________________________________________________________________________________________
#Create a sorted list of words and word frequencies for the Douay Rheims Bible

def import_douay_rheims_bible():
	input_file = open('douay_rheims_bible.pickle','r')
	reloaded_copy_of_texts = pickle.load(input_file)
	return reloaded_copy_of_texts


def generate_sorted_list_bible():
	book=import_douay_rheims_bible()
	book1=book.partition('*** START OF THIS PROJECT GUTENBERG EBOOK THE HOLY BIBLE ***')[2]# only looks at everything past the start
	book1_nopunc=str.lower(strip_punc(book1))
	words_in_book1=book1_nopunc.split()
	histogram_of_words_in_book1=histogram(words_in_book1)
	word_frequency_list=sort_most_frequent(histogram_of_words_in_book1)
	return (word_frequency_list,words_in_book1)


def save_douay_rheims_bible_data(word_frequency_list):#		ran once when data was first generated
	f = open('douay_rheims_bible_data.pickle','w')
	pickle.dump(word_frequency_list,f)
	f.close()
	print "douay_rheims_bible_data has been saved"
	return
#______________________________________________________________________________________________________________________________________________
#			Now do virtually the same thing for the Koran


def import_koran():
	input_file = open('koran.pickle','r')
	reloaded_copy_of_texts = pickle.load(input_file)
	return reloaded_copy_of_texts

def generate_sorted_list_koran():
	book=import_koran()
	book1=book.partition('*** START OF THE PROJECT GUTENBERG EBOOK, THE KORAN ***')[2]# only looks at everything past the start
	book1_nopunc=str.lower(strip_punc(book1))
	words_in_book1=book1_nopunc.split()
	histogram_of_words_in_book1=histogram(words_in_book1)
	word_frequency_list=sort_most_frequent(histogram_of_words_in_book1)
	return (word_frequency_list,words_in_book1)

def save_koran_data(word_frequency_list):#		Ran once when data was first generated
	f = open('the_koran_data.pickle','w')
	pickle.dump(word_frequency_list,f)
	f.close()
	print "the_koran_data has been saved"
	return

#_________________________________________________________________________________________________________________________________
#  Now on to the analysis section:


class tf_idf:#			 Class for performing tf idf comparisons
  def __init__(self):
    self.documents = []# defaults to an empty list
    self.corpus_dict = {}# initializes with empty dictionary for the corpus dictionary

  def addDocument(self, doc_name, list_of_words_in_document):
    doc_dict = {}#	creates an empty dictionary for the document
    for word in list_of_words_in_document:
      doc_dict[word] = doc_dict.get(word, 0.0) + 1.0#   this creates a histogram of all the words in the document
      self.corpus_dict[word] = self.corpus_dict.get(word, 0.0) + 1.0# this adds all the words in the document to the corpus dictionary for weighting later on

    length = float(len(list_of_words_in_document))# calculates the length of the list of words in the document for normalization
    for k in doc_dict:#								needs to be a float so that it actually does floating point division
      doc_dict[k] = doc_dict[k] / length# this is where the normalization occurs
    self.documents.append([doc_name, doc_dict])# stores everything nicely with the name and the normalized document dictionary

  def similarities(self, list_of_words_to_compare):

    comparison_dict = {}
    for word in list_of_words_to_compare:
    	comparison_dict[word] = comparison_dict.get(word, 0.0) + 1.0#  creates a histogram of all the words in the list of words to compare

    length = float(len(list_of_words_to_compare))#  length for normalization
    for k in comparison_dict:
      comparison_dict[k] = comparison_dict[k] / length# normalizes everything in the comparision dictionary

    simularities = []
    for document in self.documents:
        score = 0.0# initial simularity score is 0.0 (needs to be a float!)
        doc_dict = document[1]#   pulls the doc_dict from self.documents
        for k in comparison_dict:
    	    if doc_dict.has_key(k):
    	        score += (comparison_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
        simularities.append([document[0], score])

    return simularities


douay_rheims_data=generate_sorted_list_bible()
word_frequency_list_bible=douay_rheims_data[0]
list_of_words_bible=douay_rheims_data[1]

the_koran_data=generate_sorted_list_koran()
word_frequency_list_koran=the_koran_data[0]
list_of_words_koran=the_koran_data[1]
#save_douay_rheims_bible_data(word_frequency_list_bible) # this saved the raw word counts to a pickle file
#save_koran_data(word_frequency_list_koran)  #			   this saved the raw word counts to a pickle file


def data_set_1():#  Goes through all the words in the bible and does a tf idf analysis for each
	table = tf_idf()
	table.addDocument("Douay Rheims Bible", list_of_words_bible)
	table.addDocument("The Koran", list_of_words_koran)
	words_tested={}
	for word in list_of_words_bible:
		if word in words_tested:
			pass
		else:
			words_tested[word]=word
			print word
			print table.similarities(word)

def data_set_2():#  Goes through all the words in the Koran and does a tf idf analysis for each
	table = tf_idf()
	table.addDocument("Douay Rheims Bible", list_of_words_bible)
	table.addDocument("The Koran", list_of_words_koran)
	words_tested={}
	for word in list_of_words_koran:
		if word in words_tested:
			pass
		else:
			words_tested[word]=word
			print word
			print table.similarities(word)

data_set_1()
data_set_2()
#input_file = open('douay_rheims_bible_data.pickle','r')
#print pickle.load(input_file)
#input_file = open('the_koran_data.pickle','r')
#print pickle.load(input_file)


#Note to self - it might be interesting to explore what happens if I add a bunch of random books to the corpus list
#I think that might make the comparison weighted more accurately

#Another note to self - based on the data, I think I probably didn't successfully remove everything that wasn't part of
#the ebook...there's probably some junk at the end as well.
#also it would be interesting to write some code that take out numbers, or if the list is all numbers, removes that element of the list entirely.
#by removing punctuation and then spliting off of white space, I'm getting things like "servant66" etc.