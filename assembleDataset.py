import pickle

input_file = open("lyrics.pickle", "r")
lyrics = pickle.load(input_file)

prob_dict = {}

def main_dictionary():
    for lyric in lyrics:
        for line in lyric.split("\n"):
            dictionary(line.split(" "))
            #for word in line.split(" "):
            #    print word
            #print "--------------------------------------------------------------------------------"

def first_words_func():
    return_list = []
    for lyric in lyrics:
        for line in lyric.split("\n"):
            return_list.append(line.split(" ")[0])
    return (return_list)

def dictionary(word_list):
    word_list.append("")
    for i in range(len(word_list)-2):
        prob_dict.setdefault(word_list[i], []).append(word_list[i+1])

main_dictionary()
first_word_list = first_words_func()

f = open("prob_dict.pickle", "w")
pickle.dump(prob_dict, f)
f.close()

f2 = open("first_word_list.pickle", "w")
pickle.dump(first_word_list, f2)
f2.close()

print len(prob_dict)
print len(first_word_list)
