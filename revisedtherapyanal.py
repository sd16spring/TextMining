import pickle
from pattern.en import *
#this is the list of things that will be cleaned out, in the order that they 
#will be cleaned out. i determined this through trial.
badthings = ['\\n','lists.olin.edu','Anonymous rants and raves','Original',
            'Message','bounces','On Behalf Of','From','therapy','To','InReply',
            'PM','GMT','http','!','+','/','-','.',':',',','Re','RE','message',
            'Therapy','html','phpid','listinfo','mailman','olin edu','\\t','mailto',
            'From Date To Subject','To Subject','Sent','\\tmailman therapy',
            'MessageID','mailiman therapy','at Subject','ferences','Fromtherapy',
            'attherapy','Subject','Date','January','February','March','April',
            'May','June','July','August','September','October','November',
            'December','Jan','Feb','Apr','May','Jun','Jul','Aug','Sep','Oct',
            'Nov','Dec','ID','ply','On','AM','gmail','InplyIFID','InplyD',
            'Behalf Of','      ','     ','    ','   ','  ',' e ',' com ',' text ',' s ',
            ' content ',' FW ',' RF ',' Of ',' Sniffer ',' Behalf ',' CO ',' E ',' C ']

#opens and cleans the text file, first by translating extraneous symbols into
#None, and then by replacing all the bad things with spaces
old_therapyy = open('oldtherapy.txt', 'r+')
old_therapy = str(old_therapyy.read())
old_therapy = old_therapy.translate(None, '>"[]()1*23%4;56&$789#0=@_?<\'')
old_therapy = str(old_therapy.partition(' '))
for i in badthings:
    old_therapy = old_therapy.replace(i,' ')
old_therapy = old_therapy.split()
old_therapyy.close()

#same thing with the new therapy text file
new_therapyy = open('newtherapy.txt', 'r+')
new_therapy = str(new_therapyy.read())
new_therapy = new_therapy.translate(None, '>/"[]()1*23%456&$789#0,!=@+_?<\'')
new_therapy = str(new_therapy.partition(' '))
for i in badthings:
    new_therapy = new_therapy.replace(i,' ')
new_therapy = new_therapy.split()
new_therapyy.close()

# creates a dictionary with a count of the number of times a specific element
#occurs in a list
def histogram(s):
    d = dict()
    for c in s:
        if d.get(c,0)>0:
            d[c] = d[c] + 1
        else:
            d[c] = d.get(c,1) + d.get(c,0)  
    return d

#finds the items that occur most often in a list by making a histogram and
#sorting that dictionary from highest to lowest value
def most_frequent(s):
    hist = histogram(s)
    t = []
    for x, freq in hist.iteritems():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res

#start at actual nouns, after all the articles and stuff
old_words =  most_frequent(old_therapy)[23:223]
new_words =  most_frequent(new_therapy)[20:220]

#finds the words in each most frequent list that are not in the other
#and makes lists of them
unique_new = []
unique_old = []
for word in new_words:
	if word not in old_words:
		unique_new.append(word)
for word in old_words:
	if word not in new_words:
		unique_old.append(word)

#razalts
print 'Sentiment for first 200 old therapy:'+ str(sentiment(old_words))
print 'Sentiment for first 200 new therapy:'+ str(sentiment(new_words))
print unique_old
print 'Sentiment for unique old therapy:'+ str(sentiment(unique_old))
print unique_new
print 'Sentiment for unique new therapy:'+ str(sentiment(unique_new))

