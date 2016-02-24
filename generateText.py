# generateText.py generates the lyrics using Markov chains

import urllib
import pickle
import random

#first open the probability_dictionary and the list of first words
i1 = open("prob_dict.pickle", "r")
prob_dict = pickle.load(i1)

i2 = open("first_word_list.pickle", "r")
first_word_list = pickle.load(i2)

def generate_line(max_words,first_word_list):
    """
    Generate_line will create a line of randomly generated Tupac lyric.
    
    max_words sets the limit for the number of words in a line
    first_word_list contains a list of first words
    """
    word  = random.choice(first_word_list) #first pick a first word.  This is the first word in the lyric.
    return_line = "" #create the line that we will return.  type = string
    return_line += word #add the first word to the line

    for i in range(max_words): #range(max_words) will restrict the maximum number of words
        if word != "": #word will be an empty string if we have reached the end of the Markov chain
            word = random.choice(prob_dict.get(word,[""])) #the next word is randomly picked based on the current word, else default empty string
            return_line += " " + word #add the word to the string

    return return_line

def generate_lyrics(number_verses, max_words_line):
    """
    generate_lyrics will generate lyrics given a number of verses
    """
    line_list = []
    for i in range(number_verses):
        for i in range(4):
            line_list.append(generate_line(max_words_line, first_word_list))
        line_list.append("")
    return line_list

header = ["SofDes TextMining - Markov Tupac Lyrics - Nathan Yee", ""] #create header for first line

rap = generate_lyrics(4, 10) #generate lyrics 

joined = header + rap #join the header and the lyrics

for line in joined: #print all the text, if you want to save add > <filename.txt>
    print line
