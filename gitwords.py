import csv
import string
import pickle
import operator
# with open('./pull_request_comments.csv', 'rU') as f:
#     reader = csv.reader(f, dialect=csv.excel_tab_)
#     for row in reader:
#         print row[4]''

# def get_data():
#     with open('./pull_request_comments.csv', 'r') as f:
#         print([row for row in csv.reader(f.read().splitlines())])

# get_data()
def get_data():
    '''
    This function takes a CSV of all the data recorded by github about pull request comments
    and writes a file 'gittext' with only the text of the comments
    '''
    i = 0
    f = open('gittext', 'w')
    reader = csv.reader(open('./pull_request_comments.csv', 'rU'), delimiter=',')
    for row in reader:
        i = 0.0
        for column in row:
            i += 1
            if i/5 ==1:
                f.write(column)
# get_data()
def count_words():
    '''
    This file takes the gittext file containing all of the pull request comments 
    and dumps a pickle of the a dictionary containing the wordcount of every word
    '''
        text = open('./gittext','r').read()
        text = string.lower(text)
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = string.replace(text, ch, ' ')
        words = string.split(text)

        counts = {}
        for w in words:
            counts[w] = counts.get(w,0) + 1

        items = counts.items()
        items.sort()
        for i in range(10):
            print "%-10s%5d" % items[i] 

        f = open('./wordcount', 'w')
        pickle.dump(counts,f)
        f.close()

#count_words()
def sort_dict():
    '''
    This function sorts the dictionary by word count from greatest to least.
    In the command line, when called, it is piped into a file that will be processed for analysis.
    '''
    inf = open('./wordcount', 'r')
    data = pickle.load(inf)
    sorted_data = sorted(data.items(), key=operator.itemgetter(1), reverse = True)
    outf = open('./sortedwordcounts' , 'w')
    pickle.dump(sorted_data,outf)
    for i in range(10):
        print i, sorted_data[i]

sort_dict()