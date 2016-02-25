import string
import random
import pickle
from pickle import dump, load
from text_processing import processing_file, any_lowercase

def process_file(filename):
    hist = dict()
    fp = processing_file(filename)
    
    for line in fp.split('\n'):
        process_line(line, hist)

    return hist


def process_line(line, hist):
    #gets rid of white space and punctuation and puts words into a dictionary
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        
        hist[word] = hist.get(word, 0) + 1


def word_count(hist):
    '''total number of words in the dictionary of story'''
    return sum(hist.values())

def diff_words(hist):
    '''total number of different words'''
    return len(hist)

def word_freq(hist):
    t = []
    for word, count in hist.iteritems():
        t.append((count, word))
        t.sort(reverse = True)
    #print t

    res = []
    for count, word in t[0:len(hist)]:
        res.append(word)
    print res[0:100]
    return res
        
def random_word_list(hist):
    length = random.randint(8, 20)
    sentence = []
    print length
    for i in range(length):
        sentence.append(random.choice(word_freq(hist)))
    print sentence


from bisect import bisect


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    words = []
    freqs = []
    total_freq = 0

    # make a list of words and a list of cumulative frequencies
    for word, freq in hist.items():
        total_freq += freq
        words.append(word)
        freqs.append(total_freq)

    # choose a random value and find its location in the cumulative list
    x = random.randint(0, total_freq-1)
    index = bisect(freqs, x)
    print words[index]

def subtract(d1, d2, d3):
   '''does the comparing between the dictionaries'''
   res = dict()
   for key in d1:
        if key not in d2:
            if key not in d3:
                res[key] = d1[key]
   return res
    

def story_comparison(filename, d1, d2, d3):
    '''find the difference between the stories: what words only appear in one of the fairytale books?'''
    fp = open(filename, 'w')

    difference = subtract(d1, d2, d3)
   
    return word_freq(difference)
    fp.write(new_word_list)
    fp.close()
    

input_file = open('grimm_fairytales.pickle','r')
reloaded_copy_of_texts = pickle.load(input_file)

list_stories = ['grimm_fairytales.txt', 'scottish_fairytales.txt']

hist1 = process_file('grimm_fairytales.txt')
hist2 = process_file('scottish_fairytales.txt')
hist3 = process_file('japanese_fairytales.txt')

list_hists = [hist1, hist2, hist3]

        


story_comparison('grimm_.txt', hist1, hist2, hist3)
story_comparison('scottish.txt', hist2, hist1, hist3)
story_comparison('japan.txt', hist3, hist2, hist1)

