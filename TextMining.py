"""
TextMining.py counts the adjectives (as determined by Pattern, which is a bit iffy) used most frequently to describe each of the four main characters in Little Women

Software Design 2016 - Olin College of Engineering

@author: March Saper
"""
from pattern.web    import*
from pattern.search import search
from pattern.en     import parsetree 
import pickle
import pylab 


def surrounding_words(L, Names, Wrongs):
    """Returns lists of words surrounding the mention of a name only if no other character names are mentioned

    >>> surrounding_words(['one', 'short', 'day', 'in', 'the', 'emerald', 'city'], ['kristin', 'idina'], ['bob'])
    []
    >>> surrounding_words(['sharing', 'one', 'wonderful', 'one', 'short', 'day', 'the', 'wizard', 'will', 'see', 'you', 'edna'], ['idina', 'edna'], ['kristin', 'chrystal'])
    [['one', 'wonderful', 'one', 'short', 'day', 'the', 'wizard', 'will', 'see', 'you']]
    >>> surrounding_words(['sharing', 'one', 'wonderful', 'one', 'short', 'day', 'the', 'wizard', 'will', 'see', 'kristin', 'idina'], ['edna', 'idina'], ['kristin', 'chrystal'])
    []
    """


    
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
    """Returns lists of adjecives present in input lists.

    >>> adjectives([['big', 'white', 'tall', 'dog'], ['bat', 'tall']])
    ['big', 'white', 'tall', 'tall']
    >>> adjectives([['march'], ['yes', 'i', 'know', 'its', 'almost', 'march']])
    []
    """

    adjs = []
    for l in range(len(L)):
        current_string = " ".join(L[l])
        parts_of_speech = parsetree(current_string)     
        for i in search("JJ", parts_of_speech):     # Search the parsed string for adjectives
            adjs.append(str(i.string))

    return adjs



def frequency(L):
    """Returns tuples of adjectives and their frequency in input lists.

    >>> frequency(['potatoe', 'potatoe', 'potatoe'])
    [(3, 'potatoe')]
    >>> frequency([])
    []
    """

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
    """Takes the text of a book, a character's name, and the names of other characters. 
    Returns tuples of the most commonly used adjectives to describe the character.
    As the this only calls three doctested functions I decided to skip a doctest for this function.
    """

    Mentions = surrounding_words(L, N, W)
    Adjectives = adjectives(Mentions)
    Freq_Adjectives = frequency(Adjectives)

    return Freq_Adjectives



def bar_graph(T, L):
    """Takes a list of tuples containing frequency and corresponding word.
    Returns a bar graph of top ten most common words and their frequency.
    There is no doctest for this function because how would you even test this.
    """

    Frequency = []
    Adjective = []
    for f, a in T:
        Frequency.append(f)
        Adjective.append(a)
    
    x = range(9)
    y = Frequency[:9]
    f = pylab.figure()
    ax = f.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(Adjective[:10])
    pylab.title(L)
    pylab.show()



if __name__ == '__main__':
    import doctest
    doctest.testmod()
      
    LW_load = (open('LittleWomen.pickle', 'r'))
    LW = pickle.load(LW_load)
    LW = LW.split()

    All_Names = ['meg', 'margaret', 'jo', 'josephine', 'beth', 'elizabeth', 'amy']

    Meg = archetype(LW, All_Names[:2], All_Names[2:])
    Jo = archetype(LW, All_Names[2:4], All_Names[:2] + All_Names[4:])
    Beth = archetype(LW, All_Names[4:6], All_Names[:4] + All_Names[6:])
    Amy = archetype(LW, All_Names[6:], All_Names[:6])

    bar_graph(Meg, "Meg's Adjectives")
    bar_graph(Jo, "Jo's Adjectives")
    bar_graph(Beth, "Beth's Adjectives")
    bar_graph(Amy, "Amy's Adjectives")