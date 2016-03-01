import urllib
import urllib2
import pickle

#url =
#s = urllib.urlopen(url).read()
#print 's', len(s)
#print s[:80]"""

from pattern.web import *
#enormous_room_full_text = URL('http://net.lib.byu.edu/~rdh7/wwi/memoir/cummings/roomTC.htm').download()
#print oliver_twist_full_text

url = ''
f = urllib2.urlopen(url)
lyrics = [f.read()]

# Save data to a file (will be part of your data fetching script)
f = open('kpop.pickle','w')
pickle.dump(lyrics,f)
f.close()

# Load data from a file (will be part of your data processing script)
input_file = open('kpop.pickle','r')
bad_taste = pickle.load(input_file)
input_file.close()
print bad_taste
#f = open('dickens.txt', 'w')
#print f
#f.write(s)
#f.close()
#print 'done'

#f2 = open('dickens.txt','r')
#s2 = f2.read()
#f2.close()
#print 's2', len(s2)
#print 's2 =', s2[:80]
#print recycled_trash
