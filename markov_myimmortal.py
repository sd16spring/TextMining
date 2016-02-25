'''From Allen Downey's markov analysis, which I modified to fit my purpose.

AN: Stop flamming my program ok! If u flam dis dat means ur a prep'''
import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename, 'r')

    for line in fp:
        for word in line.rstrip().split():
            process_word(word, order)


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words; 
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    textstring = ''
    # choose a random prefix (not weighted by frequency)
    start = random.choice(suffix_map.keys())
    
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        textstring += str(word) + ' '
        start = shift(start, word)
    return textstring


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)

if __name__ == '__main__':
	process_file('my_immortal122new.txt', 2)
	text = random_text(400)
	f = open('my_immortalmarkovgenerated.txt','w')
	f.write(text)
	f.close()
    

