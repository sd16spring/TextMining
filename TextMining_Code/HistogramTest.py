import pickle
import collections
from collections import deque
import string
import matplotlib.pyplot as plt
import matplotlib.artist as art



""" Importing Pickled Text"""
input_file = open('oscar_wilde_full.pickle','r')
reloaded_copy_of_wilde_texts = pickle.load(input_file)
# ________________________________________________________
input_file = open('ts_eliot_full.pickle','r')
reloaded_copy_of_eliot_texts = pickle.load(input_file)

# ________________________________________________________
input_file = open('lincoln_speeches.pickle','r')
reloaded_copy_of_lincoln_speeches = pickle.load(input_file)


""" Text Format Processing"""
wilde_text_nopunct = reloaded_copy_of_wilde_texts.translate(string.maketrans("",""), string.punctuation) # eliminates all punctuation
wilde_text_lower = wilde_text_nopunct.lower()									# converting all words to lowercase
words_wilde = wilde_text_lower.split()											# splitting text into words
# __________________________________________________________________________________________________________________________________
eliot_text_nopunct = reloaded_copy_of_eliot_texts.translate(string.maketrans("",""), string.punctuation) # eliminates all punctuation
eliot_text_lower = eliot_text_nopunct.lower()									# converting all words to lowercase
words_eliot = eliot_text_lower.split()											# splitting text into words
# __________________________________________________________________________________________________________________________________
lincoln_text_nopunct = reloaded_copy_of_lincoln_speeches.translate(string.maketrans("",""), string.punctuation) # eliminates all punctuation
lincoln_text_lower = lincoln_text_nopunct.lower()								# converting all words to lowercase
words_lincoln = lincoln_text_lower.split()										# splitting text into words

def histogram(words):
    """ Function that returns the frequency of all words in a text
    >>> print histogram(['how','many', 'times', 'times', 'times', 'can','i', 'type', 'type', 'times'])
    [1, 1, 1, 1, 2, 4]
    """
    t = dict()																	# initialize dictionary
    for word in words:															# check for each word in text
        t[word] = 1 + t.get(word, 0)											# count the number of times the word appears in the dic
    ordered_t = collections.OrderedDict(sorted(t.items(), key=lambda t: t[1]))	# creates a list of the frequencies of words in order (greatest --> least)
    return ordered_t.values()													# returns list of frequencies


y = histogram(words_lincoln)														# sets variable y equal to output of histogram()

n = len(histogram(words_lincoln))													# sets variable n equal to the length of the histogram list

def x_axis_pts(n):
	""" Creates a x-axis for the plot by taking length
	 of histogram and assigning an index to each value

	>>> print x_axis_pts(5)
	[0, 1, 2, 3, 4]
	"""
	x_axis = []																	# intitializes empty list
	for i in range(n):															# loops through indexes until it reaches n
		x_axis.append(i)														# adds the index number to the ith term in the list
	return x_axis 																# returns list of numbers up to n

x = x_axis_pts(n)																# this sequence essentially reverses the list
d = deque(x)
x = deque(reversed(d))


""" Plot the frequency of words"""

plt.loglog(x, y)																# plotting frequency on a log-log scale
plt.ylabel('word')
plt.xlabel('frequency')
plt.title("Speeches/Letters")
plt.show()

if __name__ == "__main__":
    import doctest
    doctest.testmod()