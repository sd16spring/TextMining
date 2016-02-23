import pickle
import random

i1 = open("prob_dict.pickle", "r")
prob_dict = pickle.load(i1)

i2 = open("first_word_list.pickle", "r")
first_word_list = pickle.load(i2)

def generate_line(max_words,first_word_list):
    word  = random.choice(first_word_list)
    return_line = ""
    return_line += word

    for i in range(max_words):
        if word != "":
            word = random.choice(prob_dict.get(word,[""]))
        return_line += " " + word

    return return_line

def generate_lyrics(number_verses):
    line_list = []
    for i in range(number_verses):
        for i in range(4):
            line_list.append(generate_line(10,first_word_list))
        line_list.append("")
    return line_list

rap = generate_lyrics(4)

for line in rap:
    print line
