#simple file to print lyrics.pickle
#this file is not needed in the pipeline of the program

import pickle

input_file = open("lyrics.pickle", "r")
lyrics = pickle.load(input_file)

for lyric in lyrics:
    print lyric
