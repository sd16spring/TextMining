import pickle

input_file = open("lyrics.pickle", "r")
lyrics = pickle.load(input_file)

for lyric in lyrics:
    print lyric
