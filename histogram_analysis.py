from pattern.web import *
import pickle
import string
from bokeh.charts import Bar, output_file, show
from pandas import *

''' Download Texts and write to files

oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
#write Oliver Twist to a file
f = open('some_text_file.pickle','w')
pickle.dump(oliver_twist_full_text, f)
f.close()

wizard_of_oz_full_text = URL('http://www.gutenberg.org/cache/epub/55/pg55.txt').download()
#write OWizard of Oz to a file
f = open('wizard_of_oz.pickle','w')
pickle.dump(wizard_of_oz_full_text, f)
f.close()

hamlet_full_text = URL('http://www.gutenberg.org/cache/epub/1524/pg1524.txt').download()
hamlet_full_text = hamlet_full_text[hamlet_full_text.find('SCENE.'):]
f = open('hamlet.pickle','w')
pickle.dump(hamlet_full_text, f)
f.close()

romeo_full_text = URL('http://www.gutenberg.org/cache/epub/1112/pg1112.txt').download()
romeo_full_text = romeo_full_text[romeo_full_text.find('SCENE.'):]
f = open('romeo.pickle','w')
pickle.dump(romeo_full_text, f)
f.close()

lear_full_text = URL('http://www.gutenberg.org/cache/epub/1128/pg1128.txt').download()
lear_full_text = lear_full_text[lear_full_text.find('Scene:'):]
f = open('lear.pickle','w')
pickle.dump(lear_full_text, f)
f.close()

caesar_full_text = URL('http://www.gutenberg.org/cache/epub/1120/pg1120.txt').download()
caesar_full_text = caesar_full_text[caesar_full_text.find('SCENE:'):]
f = open('caesar.pickle','w')
pickle.dump(caesar_full_text, f)
f.close()
'''
#Make string copies of books 
#oliver_file = open('some_text_file.pickle','r')
#copy_of_oliver_twist = pickle.load(oliver_file)

#wizard_file = open('wizard_of_oz.pickle','r')
#copy_of_wizard_of_oz = pickle.load(wizard_file)

hamlet_file = open('hamlet.pickle','r')
copy_of_hamlet = pickle.load(hamlet_file)

romeo_file = open('romeo.pickle','r')
copy_of_romeo = pickle.load(romeo_file)

lear_file = open('lear.pickle','r')
copy_of_lear = pickle.load(lear_file)

caesar_file = open('caesar.pickle','r')
copy_of_caesar = pickle.load(caesar_file)

def most_frequent(s):
    """ returns dictionary of top 15 words in each book and their percentage-frequencies
    if chose to return 'rtrn': returns list of words in decreasing order based on frequency of appearances in a string"""
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
    rtrn = []
    i = 0
    top15 = {}
    for frequency, word in wordList:
        rtrn.append(word)
        if i < 50:
        	i += 1
        	top15[word] = 100.0*frequency/totalWords
        	#print '%s %s' %(100.0*frequency/totalWords, word)
        else:
        	break
    return top15


#print 'Top 15 Words Used in Oliver Twist:'
#top15_oliver = most_frequent(copy_of_oliver_twist)

#print 'Top 15 Words Used in Wizard of Oz:'
#top15_wizard = most_frequent(copy_of_wizard_of_oz)

#print 'Top 15 Words Used in Hamlet:'
top15_hamlet = most_frequent(copy_of_hamlet)

#print 'Top 15 Words Used in Romeo and Juliet:'
top15_romeo = most_frequent(copy_of_romeo)

#print 'Top 15 Words Used in King Lear:'
top15_lear = most_frequent(copy_of_lear)

#print 'Top 15 Words Used in Julius Caesar:'
top15_caesar = most_frequent(copy_of_caesar)


#create a set of all of the words most frequently used across all of the plays
all_words = []
for word in top15_hamlet:
	all_words.append(word)
for word in top15_romeo:
	all_words.append(word)
for word in top15_lear:
	all_words.append(word)
for word in top15_caesar:
	all_words.append(word)

all_words_set = set(all_words) #removes duplicates
all_words = list(all_words_set)
all_words.sort()
plays = ['Hamlet','Romeo','Lear', 'Caesar']
#print all_words

#create a dataframe
df = DataFrame(0, index=all_words, columns=plays)

for i in range(-1,len(all_words)):
	#print i
	#print all_words[i]
	#print top15_hamlet.get(all_words[i], 0)
	df.loc[all_words[i]]['Hamlet'] = top15_hamlet.get(all_words[i], 0)
	df.loc[all_words[i]]['Romeo'] = top15_romeo.get(all_words[i], 0)
	df.loc[all_words[i]]['Lear'] = top15_lear.get(all_words[i], 0)
	df.loc[all_words[i]]['Caesar'] = top15_caesar.get(all_words[i], 0)

	df.set_value(i, 'Hamlet', top15_hamlet.get(all_words[i], 0))
	df.set_value(i, 'Romeo', top15_romeo.get(all_words[i], 0))
	df.set_value(i, 'Lear', top15_lear.get(all_words[i], 0))
	df.set_value(i, 'Caesar', top15_caesar.get(all_words[i], 0))
dupl_df = df.ix[:all_words[-1]]
print
print 'Most common words in each play by percentage-frequencies'
#print dupl_df

#Pickle the dataframe to a text file
f = open('pandaframe.pickle','w')
pickle.dump(dupl_df, f)
f.close()

panda_file = open('pandaframe.pickle','r')
copy_of_df = pickle.load(panda_file)
print copy_of_df

''' Attempted to make a bar graph using Panda dataframes...but didn't have enough time and needed actual sleep
'''
#Make a bar chart from the dataframe
#p = Bar(copy_of_df, label='Word', values='Percentage of Book', agg='Word Frequency', group='play', title="Most Used Words in Shakespeare by Play", legend='top_right')

#output_file("bar.html")

#show(p)