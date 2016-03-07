"""
A program to scrape the full text of Shakespeare's Hamlet, and Kendrick
Lamar's To Pimp a Butterfly (the most popular rap album of 2015), and use Markov
chain generation to combine them into a new work of art.
"""

from pattern.web import *
import doctest
import pickle
from urlparse import urljoin
from bs4 import BeautifulSoup
import requests
import sys
import string
import random

def pull_hamlet():
    """This function is a basic download-and-pickle script that pulls the full
    text of Hamlet from Gutenberg (changed to avoid old English)"""
    hamlet_full_text = URL('http://seattlecentral.edu/faculty/flepeint/java143/hw7/hamlet.text').download()
    print hamlet_full_text[:100]
    fin = open('hamlet.pickle','w')
    pickle.dump(hamlet_full_text,fin)
    fin.close()

def pull_butterfly():
    """This is much weirder. It is supposed to pull all the song lyrics off of
    Genius using the BeautifulSoup, urlparse and requests packages. This is
    code modified from stuff I found; I've been doing my best to read all the
    relevant documentation and actually parse this code myself. It took me a
    while to get this to work, but it now goes through all the relevant links
    and pulls only the lyrics."""
    BASE_URL = "http://genius.com"
    album_url = "http://genius.com/albums/Kendrick-lamar/To-pimp-a-butterfly"

    response = requests.get(album_url, headers={'User-Agent': 'Chrome/35.0.1916.153'})
    soup = BeautifulSoup(response.text, "lxml")
    # print soup
    lamar_text = ""
    for song_link in soup.select('ul.song_list > li > a'):
        link = urljoin(BASE_URL, song_link['href'])
        print link
        song_response = requests.get(link)
        song_soup = BeautifulSoup(song_response.text)
        # print song_soup
        lyrics = song_soup.find('lyrics').text.strip()
        print lyrics
        lamar_text += "\n" + lyrics
    # print lamar_text[:1000]
    fin = open('butterfly.pickle','w')
    pickle.dump(lamar_text,fin)
    fin.close()

def convert_to_txt():
    """This makes the pickling sort of useless, since I'm now writing them to
    plain text files. This way I can manually cut out some stuff I don't want
    though."""
    with open('hamlet.pickle','r') as fin:
        hamlet_text = pickle.load(fin)
        print hamlet_text
    with open('hamlet.txt','w') as fin:
        fin.write(hamlet_text)
    with open('butterfly.pickle','r') as fin:
        lamar_text = pickle.load(fin)
        print lamar_text
    with open('butterfly.txt','w') as fin:
        fin.write(lamar_text.encode('utf8'))


"""This is Allen Downey's Markov code, only slightly modified. I get how it
works and spent a lot of time on getting the data set, so I didn't really feel
the need to reimplement it."""

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
    """Generates random words from the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
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
        print word,
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else:
        process_file(filename, order)
        random_text(n)


if __name__ == '__main__':
    # pull_hamlet()
    # pull_butterfly()
    # convert_to_txt()
    main(*sys.argv)

    doctest.testmod()
