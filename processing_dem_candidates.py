import pickle
import string
fin1 = open('dempresidential_candidate_sanders.pickle')
fin2 = open('dempresidential_candidate_clinton.pickle')

sanders_results = pickle.load(fin1)
clinton_results = pickle.load(fin2)

#Filter out most common words here:
def process_file(filename):
	hist = dict()
	fp = open(filename)
	for line in fp:
		process_line(line, hist)
	return hist

def process_line(line, hist):
	line = line.replace('-', ' ')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()

		hist[word] = hist.get(word, 0) + 1


complete_hist_sanders = process_file('dempresidential_candidate_sanders.pickle')
complete_hist_clinton = process_file('dempresidential_candidate_clinton.pickle')

def most_common(hist):
	t = []
	#sorting:
	for key, value in hist.items(): #note: I should get familiar with the .items() method!
		t.append((value, key))
	t.sort(reverse = True)
	#eliminating common words that don't mean anything
	x = []
	for a_tuple in t:
		if a_tuple[1] not in ['the', 'of', 'and', 'but', 'b', 'from', 'which', 'would', 'when', '2010.\\n', '2006', 'you', 'said', 'to', 'have', '2007', '2007.\\n', '2015', 'we', 'are', 'in', 'a', 'by', 'an', 'or', 'who', 'be', 'it', 'this', 'was', 'at', 'his', '', 'for', 'that', 'sanders', 'hillary', 'bernie', 'clinton', 'is', 'on', '2015.\\n', 'he', 'has', 'not', 'with', 'she', 'retrieved', 'her', 'as', 'i', 'is', 'january', 'february', 'march', 'april', 'may', 'june', 'xe2\\x80\\x93', 'july', 'august', 'september', 'october', 'november', 'december']:
			x.append(a_tuple[1])

	return x

curtailed_sanders_histogram = most_common(complete_hist_sanders)
curtailed_clinton_histogram = most_common(complete_hist_clinton)

top20_sanders_most_common = curtailed_sanders_histogram[0:20]
top20_clinton_most_common = curtailed_clinton_histogram[0:20]
print "The top 20 relevant (in a political sense) words in Bernie's political wikipedia page are:" 
print  top20_sanders_most_common
print "The top 20 relevant (in a political sense) words in Hillary's political wikipedia page are:" 
print top20_clinton_most_common


def similarities(hist1, hist2):
	words_in_common = []
	for key1 in hist1:
		if (key1 not in words_in_common) and (key1 in hist2):
			words_in_common.append(key1)
	for key2 in hist2:
		if (key2 not in words_in_common) and (key2 in hist1):
			words_in_common.append(key2)
	return words_in_common

print ' '
print "The words both pages had in common are:"
print similarities(curtailed_sanders_histogram, curtailed_clinton_histogram)



fin1.close()
fin2.close()

#returns top 20 words in each political 
#def top_words(histogram):








##load data from a file
input_file = open('dempresidential_candidate_sanders.pickle', 'r')
reloaded_copy_of_texts = pickle.load(input_file)
#print reloaded_copy_of_texts
input_file.close()
