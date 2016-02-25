from pattern.en import *
import string
from text_processing import processing_file, any_lowercase

def sentiments(filename):
	'''returns a tuble (polarity, subjectivity) polarity: positive to negative, subjectivity: objetive to subjective'''
	w = processing_file(filename)
	print sentiment(w)

#print sentiment('My dogs are cute, but yours are not.') 

def modalities(filename):
	w = processing_file(filename)
	p = parse(w, lemmata=True)
	p = Sentence(w)
	print modality(p)
	#print mood(w)


def define(sentence):
	
	for word in sentence.split():
		word = word.strip(string.punctuation)
		word = singularize(word)
		try:
			b = wordnet.synsets(word)[0]
			print word + ' :' + b.gloss
		except:
			print word + ': no definition available'

#pprint(parse(s, relations=True, lemmata=True))
#print modality(s)
#sentiments('scottish_fairytales.txt')
#sentiments('grimm_fairytales.txt')
#sentiments('japanese_fairytales.txt')
#sentiments('norwegian_fairytales.txt')
#print sentiment('dogs are not animals')
#define('I like dogs.')
sentiments('grimm_fairytales.txt')
sentiments('scottish_fairytales.txt')
sentiments('japanese_fairytales.txt')