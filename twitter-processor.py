from pattern.web import *
import pickle

# license = 'LVv4FWooXMX7dNuS36kgMTAw2'

tweetlist = []
t = Twitter()
i = None
for j in range(5):
    for tweet in t.search('the walking dead', start=i, count=50):
        #sometimes tweets contain characters that we can't print,
        #so this will ignore errors
        try: 
            tweetlist.append(tweet.text)
            print tweet.text
        except:
            continue
        else:
            print #add a space to make output more readable
            i = tweet.id


# Save data to a file (will be part of your data fetching script)
f = open('walking_dead_tweets.pickle','w')
pickle.dump(tweetlist,f)
f.close()

# Load data from a file (will be part of your data processing script)
# input_file = open('walking_dead_tweets','r')
# reloaded_copy_of_texts = pickle.load(input_file)

# print tweetlist