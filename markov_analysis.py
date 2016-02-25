import sys
import string
import random
import pickle
from pickle import dump, load
from text_processing import processing_file, any_lowercase

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    Returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    new_fp = processing_file(filename)


    for line in new_fp.split('\n'):
        
        for word in line.rstrip().split():
            process_word(word, order)
            



def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break
 


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, store up the words; 
    after that, add entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

  
    if prefix in suffix_map:
        suffix_map[prefix].append(word)
    
    else:
        
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    story = open('fairy_tales_grimm_random.txt', 'w')
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(suffix_map.keys())

    word_string = ''
    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        start = shift(start, word)
        word_string += (word) + ' '

    
    story.write(word_string)
    story.close()
        


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(name, filename='', n=1000, order=2, *args):
    
    try:
        n = int(n)
        order = int(order)
    except:
        print'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)
    


random_story = main('grimm_fairytales', 'grimm_fairytales.txt', n=1000, order= 2)


#process_file('emma.txt')
#if __name__ == '__main__':
#    main(*sys.argv)
