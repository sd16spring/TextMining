from pattern.web import *
import pickle
import string
from bokeh.charts import Bar, output_file, show
from pandas import *

'''
BEFORE RUNNING: 
Be sure to have pickled copies of each of the books in the same folder. 
Obtain these pickled copies of books by running functions as necessary in pickle_file_creation.py
'''
plays = ['Hamlet','Romeo','Lear', 'Caesar'] #list of names of plays. This order must be consistent in all following aggregated lists.
pickled_filenames = ['hamlet.pickle','romeo.pickle','lear.pickle','caesar.pickle']

#Make string copies of books and add them into a list of copies of the books
copy_of_texts = []
for i in pickled_filenames:
	with open(i, 'r') as f:
		copy_of_texts.append(pickle.load(f))

def most_frequent(s):
	''' returns dictionary of top 15 words in each book and their percentage-frequencies
	if chose to return 'total_top': returns list of words in decreasing order based on frequency of appearances in a string
	'''
	s = s.lower()
	s = s.translate(string.maketrans('',''), string.punctuation)
	totalWords = len(s)
	d = {}
	for word in s.split():
		d[word] = d.get(word, 0)+1
	wordList = []
	for word in d:
		wordList.append((d[word], word))
	wordList.sort(reverse=True)
	total_top = []
	i = 0
	top15 = {}
	for frequency, word in wordList[:50]:
		total_top.append(word)
		top15[word] = 100.0*frequency/totalWords
	return top15

def merge_lists(partial_lists):
	#create a set of all of the words most frequently used across all of the plays
	all_words = []
	for i in partial_lists: #concatenates lists into one
		all_words+=i
	all_words_set = set(all_words) #removes duplicates
	all_words = list(all_words_set) #turns back into a list
	all_words.sort() #alphabetically sorts list of all words
	return all_words

top15_lists = [most_frequent(i) for i in copy_of_texts]
all_words = merge_lists(top15_lists)

#create a dataframe
df = DataFrame(0, index=all_words, columns=plays)

for i in range(-1,len(all_words)):
	for j in range(0,len(plays)):
		df.loc[all_words[i],plays[j]] = top15_lists[j].get(all_words[i], 0)
		df.set_value(i, plays[j], top15_lists[j].get(all_words[i], 0))

dupl_df = df.ix[:all_words[-1]]
print
print 'Most common words in each play by percentage-frequencies'
print dupl_df

#Pickle the dataframe to a text file
# with open('pandaframe.pickle','w') as f:
# 	pickle.dump(dupl_df, f)

# with open('pandaframe.pickle','r') as panda_file:
# 	copy_of_df = pickle.load(panda_file)

''' Attempted to make a bar graph using Panda dataframes...but didn't have enough time and needed actual sleep
'''
#Make a bar chart from the dataframe
#p = Bar(copy_of_df, label='Word', values='Percentage of Book', agg='Word Frequency', group='play', title="Most Used Words in Shakespeare by Play", legend='top_right')

#output_file("bar.html")

#show(p)