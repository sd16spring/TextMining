"""
TextMining.py downloads a copy of Little Women and counts the words used most frequently to describe each of the four main characters.

Software Design 2016 - Olin College of Engineering

@author: March Saper
"""
from pattern.web    import*
from pattern.search import search
from pattern.en     import parsetree
import string 
import pickle

""" Download, Cleans, and Saves the Text
LittleWomenURL = URL('http://gutenberg.readingroo.ms/5/1/514/514.txt').download()
LittleWomen = plaintext(LittleWomenURL)

exclude = set(string.punctuation)
LittleWomen = ''.join(ch for ch in LittleWomen if ch not in exclude)
LittleWomen = LittleWomen.lower()
print LittleWomen

f = open('LittleWomenWorking.txt', 'w')
f.write(LittleWomen.encode('UTF-8'))
f.close()
"""


def surrounding_words(L, Names, Wrongs):
    """Returns lists of words surrounding the mention of a name only if no other character names are mentioned"""

    
    name_mentions = []
    for i in range(len(L)):
        if L[i] in Names:
            name_mentions.append(L[i-10:i])
            i += 10
    one_only = []
    for m in range(len(name_mentions)):
        if all(w not in name_mentions[m] for w in Wrongs):
            one_only.append(name_mentions[m])

    return one_only
    

def adjectives(L):
    """Returns lists of adjecives present in input lists"""

    adjs = []
    for l in range(len(L)):
        current_string = " ".join(L[l])
        parts_of_speech = parsetree(current_string)     
        for i in search("JJ", parts_of_speech):     # Search the parsed string for adjectives
            adjs.append(str(i.string))

    return adjs


def frequency(L):
    """Returns tuples of words and their frequency in input lists"""

    freq = {}
    for l in L:
        if l in freq:
            freq[l] += 1
        else:
            freq[l] = 1
    adj_freq = freq.items()
    freq_adj = []
    for adj, freq in adj_freq:
        freq_adj.append((freq, adj))
    freq_adj.sort(reverse = True)

    return freq_adj


def archetype(L, N, W):
    """Takes the text of a book, a character's name, and the names of other characters.  Returns tuples of the most commonly used adjectives to describe the character"""

    Mentions = surrounding_words(L, N, W)
    Adjectives = adjectives(Mentions)
    Freq_Adjectives = frequency(Adjectives)

    return Freq_Adjectives


LW = (open('LittleWomenCleaned.txt', 'r').read()).split()

All_Names = ['meg', 'margaret', 'jo', 'josephine', 'beth', 'elizabeth', 'amy']

Meg = archetype(LW, All_Names[:2], All_Names[2:])





# """ This Pickles Stuff
# f_BleakHouse = open('BleakHouseDownload.pickle','w')
# pickle.dump(BleakHouseDownload,f_BleakHouse)
# f_BleakHouse.close()

# BleakHouse_input = open('BleakHouseDownload.pickle','r')
# reloaded_BleakHouse = pickle.load(BleakHouse_input)
# """
