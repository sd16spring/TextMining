import pickle

input_file = open("lyrics.pickle", "r") #lyrics.pickle contains the raw lyrics.  If must be parsed by line to create our needed dataset.
lyrics = pickle.load(input_file)

prob_dict = {} #this is the main dataset we will save

def main_dictionary():
    """
    main_dictionary creates our dataset.  It steps throguh the lines and calls dictionary with a list containing the words of that line
    """
    for lyric in lyrics:
        for line in lyric.split("\n"):
            dictionary(line.split(" "))

def first_words_func():
    """
    first_words_func creates a list of the first words of the lines.  We will eventually use these to start our Markov chains.
    """
    return_list = []
    for lyric in lyrics:
        for line in lyric.split("\n"):
            return_list.append(line.split(" ")[0])
    return (return_list)

def dictionary(word_list):
    """
    dictionary uses a list of words to create a markov chain dictionary.  If a word is not the last word, it will save that word as a key and use the next word as its value
    """
    word_list.append("")
    for i in range(len(word_list)-2):
        prob_dict.setdefault(word_list[i], []).append(word_list[i+1])

#make the Markov dictionary and the list of first words
main_dictionary()
first_word_list = first_words_func()

#save the Markov dictionary
f = open("prob_dict.pickle", "w")
pickle.dump(prob_dict, f)
f.close()

#save the list of first words
f2 = open("first_word_list.pickle", "w")
pickle.dump(first_word_list, f2)
f2.close()

#error checking / debugging with print statements
print "length of Markov dictionary = " + str(len(prob_dict))
print "length of list of first words = " + str(len(first_word_list))
