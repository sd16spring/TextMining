""" This program is an extension of the Text Mining mini project I did on the
text in our Facebook group chat. It synthesizes a semi-interactive group chat
exchange """
import message_scrape as ms
import random
import pickle
import datetime

def start_chat(trained_dict):
    print 'Welcome to the 2015 Comrades Markov chat!\nPress ENTER to get started!'
    while True:
        raw_input()
        print create_msg(trained_dict)

def train(message_block):
    """This method will use a dictionary full of lists to capture every token
    that could come after any given token in a set"""
    tokens = message_block.split()
    td = {token:[] for token in tokens}
    for i in range(len(tokens) - 1):
        td[tokens[i]].append(tokens[i+1])
    return td


def create_msg(t_dict):
    """this function creates a message by adding on messages from the training set
    until it reaches a newline character"""
    _run = True
    msg = ''
    last = ''
    nxt = ''
    while _run:
        if not last:
            #pick a random value from a random key
            nxt = random.choice(t_dict[random.choice(t_dict.keys())])
        else:
            #pick a random value from the last key
            nxt = random.choice(t_dict[last])
        if nxt == '|':
            _run = False
            nxt = '\n'
        #update step
        msg += nxt + " "
        last = nxt

        if msg == "\n ":
            msg = ':thumbs-up:\n'
    return str(datetime.datetime.now().time()) +' > '+ msg

if __name__ == '__main__':
    #check if we've already trained this thing
    try:
        f = open('t_dict.txt', 'r+')
        t_dict = pickle.load(f)
    except IOError:
        f = open('t_dict.txt', 'w')
        #scrape the messages
        block = ms.get_msgs('messages.htm', 'DEFAULT')
        text = ms.strip_markov(block)
        #train the data structure
        t_dict = train(text)
        pickle.dump(t_dict, f)
    #start the chatbot
    start_chat(t_dict)
