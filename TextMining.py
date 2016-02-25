"""
TextMining.py counts the adjectives (as determined by Pattern, which is a bit iffy) used most frequently to describe each of the four main characters in Little Women by Louisa May Alcott.

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
    """Returns a list of adjecives present in input lists.

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



def unique_adjectives(L, AllElse):
    """Returns a list of adjectives unique to the character.

    >>> unique_adjectives(['big', 'tall', 'short'], ['short', 'white', 'black'])
    ['big', 'tall']
    >>> unique_adjectives(['tall', 'short'], ['tall', 'short', 'white'])
    []
    """

    unique_adjs = []
    for a in range(len(L)):
        if L[a] not in AllElse:
            unique_adjs.append(L[a])
    
    return unique_adjs




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



def adj_finder(L, N, W):
    """Takes the text of a book, a character's name, and the names of other characters. 
    Returns all adjectives used in proximity to the character.
    As the this only calls doctested functions I decided to skip a doctest for this function.
    """

    Mentions = surrounding_words(L, N, W)
    Adjectives = adjectives(Mentions)
    
    return Adjectives



def frequency_unique_adjs(L, AllElse):
    """Takes a list of adjectives used to describe a single character as well as all characters.
    Returns tuples of the most frequently used adjectives only used to describe one character.
    As this only calls doctested functions I decided to skip the doctest for this function too.
    """

    unique_adjs = unique_adjectives(L, AllElse)
    unique_freq_adj = frequency(unique_adjs)

    return unique_freq_adj




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


    Meg_a = adj_finder(LW, All_Names[:2], All_Names[2:])
    Jo_a = adj_finder(LW, All_Names[2:4], All_Names[:2] + All_Names[4:])
    Beth_a = adj_finder(LW, All_Names[4:6], All_Names[:4] + All_Names[6:])
    Amy_a = adj_finder(LW, All_Names[6:], All_Names[:6])
    

    Meg_u = frequency_unique_adjs(Meg_a, Jo_a + Beth_a + Amy_a)
    Jo_u = frequency_unique_adjs(Jo_a, Meg_a + Beth_a + Amy_a)
    Beth_u = frequency_unique_adjs(Beth_a, Meg_a + Jo_a + Amy_a)
    Amy_u = frequency_unique_adjs(Amy_a, Meg_a + Jo_a + Beth_a)


    bar_graph(Meg_u, "Meg's Unique Adjectives")
    bar_graph(Jo_u, "Jo's Unique Adjectives")
    bar_graph(Beth_u, "Beth's Unique Adjectives")
    bar_graph(Amy_u, "Amy's Unique Adjectives")