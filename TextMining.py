from pattern.web 	import*
from pattern.search import search
from pattern.en     import parsetree
import string 
import pickle


""" Downloads and Saves the Text
LittleWomenURL = URL('http://gutenberg.readingroo.ms/5/1/514/514.txt').download()
LittleWomen = plaintext(LittleWomenURL)

f_LittleWomen = open('LittleWomenDownload.txt', 'w')
f_LittleWomen.write(LittleWomen.encode('UTF-8'))
f_LittleWomen.close()
"""

""" Cleans the Downloaded Text
LittleWomenCleaned = open('LittleWomenDownload.txt', 'r').read()

exclude = set(string.punctuation)
LittleWomenCleaned = ''.join(ch for ch in LittleWomenCleaned if ch not in exclude)
LittleWomenCleaned = LittleWomenCleaned.lower()


fLW = open('LittleWomenCleaned.txt', 'w')
fLW.write(LittleWomenCleaned)
fLW.close()
"""

LW_string = open('LittleWomenCleaned.txt', 'r').read()
LW_list = LW_string.split()

def name_list(L, NL):
	"""Returns list of list of 30 words surrounding the mention of a name"""
	name_mentions_list = []
	for i in range(len(L)):
		if L[i] in NL:
			name_mentions_list.append(L[i-4:i+4])
	return name_mentions_list

Meg_names = ['margaret', 'meg']
Meg_mentions_list = name_list(LW_list, Meg_names)

Jo_names = ['josephine', 'jo']
Jo_mentions_list = name_list(LW_list, Jo_names)

Beth_names = ['beth', 'elizabeth']
Beth_mentions_list = name_list(LW_list, Beth_names)

Amy_names = ['amy']
Amy_mentions_list = name_list(LW_list, Amy_names)


def single_name_only(L, WrongNames):
	"""Returns list with name mention only if no other names are mentioned"""
	single_name_list = []
	for l in range(len(L)):
		if WrongNames not in L[l]:
			single_name_list.append(L[l])
	return single_name_list


All_Names = ['meg', 'margaret', 'jo', 'josephine', 'beth', 'elizabeth', 'amy']

Meg_only = single_name_only(Meg_mentions_list, ['jo', 'josephine', 'beth', 'elizabeth', 'amy'])
Jo_only = single_name_only(Jo_mentions_list, ['meg', 'margaret', 'beth', 'elizabeth', 'amy'])
Beth_only = single_name_only(Beth_mentions_list, ['meg', 'margaret', 'jo', 'josephine', 'amy'])
Amy_only = single_name_only(Amy_mentions_list, ['meg', 'margaret', 'jo', 'josephine', 'beth', 'elizabeth'])


def adjectives_only(L):
	adjectives = []
	for l in range(len(L)):
		current_string = " ".join(L[l])
		parts_of_speech = parsetree(current_string)
		for i in search("JJ", parts_of_speech):
			adjectives.append(str(i.string))
	return adjectives

Meg_adjectives = adjectives_only(Meg_only)
Jo_adjectives = adjectives_only(Jo_only)
Beth_adjectives = adjectives_only(Beth_only)
Amy_adjectives = adjectives_only(Amy_only)

def adjective_frequency(L):
	adjective_freq_dictionary = {}
	for l in L:
		if l in adjective_freq_dictionary:
			adjective_freq_dictionary[l] += 1
		else:
			adjective_freq_dictionary[l] = 1
	adjective_freq = adjective_freq_dictionary.items()
	return adjective_freq



Meg_adj_freq = adjective_frequency(Meg_adjectives)
Jo_adj_freq = adjective_frequency(Jo_adjectives)
Beth_adj_freq = adjective_frequency(Beth_adjectives)
Amy_adj_freq = adjective_frequency(Amy_adjectives)

def adjectives_sorted(T):
	freq_adj = []
	for adjective, freq in T:
	    freq_adj.append((freq, adjective))
	freq_adj.sort(reverse = True)
	return freq_adj


Meg_described = adjectives_sorted(Meg_adj_freq)
Jo_described = adjectives_sorted(Jo_adj_freq)
Beth_described = adjectives_sorted(Beth_adj_freq)
Amy_described = adjectives_sorted(Amy_adj_freq)




print Jo_described

""" This Pickles Stuff
f_BleakHouse = open('BleakHouseDownload.pickle','w')
pickle.dump(BleakHouseDownload,f_BleakHouse)
f_BleakHouse.close()

BleakHouse_input = open('BleakHouseDownload.pickle','r')
reloaded_BleakHouse = pickle.load(BleakHouse_input)
"""
