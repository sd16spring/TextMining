"""
Serena Chen
Clustering.py
Clusters comments. This file has two types of clustering: my dumb implementation, and kmeans form scikit-learn.
kmeans is used in Anaylsis.py
"""
import Analysis
import nltk
import string
import pandas as pd
from numpy import arange
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

#empirically determining my own stop words because if I use the built in stop words,
#it will filter out too many words
#...youtube has a small vocabulary
STOP_WORDS = """is and the this in it a to of like i my you that
    be was were very so would video me he she have where really
    are they ok but much go our we will their for your at from
    these if when on her all up too do just got over so can by out
    how his him her am else such had with vid even with ever or
    as an a did them has im i'm should could would what their those
    off u """
def tokenizeAndStem(comment, returnRaw = False):
    """
    Takes a comment and returns a list stemmed words and numbers
    Stemming: stripping prefixes and suffixes and leaving the root: ex. running and runner will both 
    become run.
    if returnRaw is True, it will return the unstemmed versions of the words also, in the 
    format (rawList, stemmedList)
    """
    #stemming--taking the root of each word, so 'running' and 'runner' will be grouped together
    stemmer = nltk.stem.snowball.SnowballStemmer('english')

    tokens = []
    #take every word
    for c in comment.split():
        #remove leading and trailing whitespace and punctuation
        stripped = c.strip(string.whitespace+string.punctuation).lower()
        #if there is still word in the word
        if len(stripped)>0:
            tokens.append(stripped)
    #stem all the tokens
    #numbers will be unharmed
    stem = [stemmer.stem(s) for s in tokens]
    if returnRaw:
        return tokens, stem
    return stem

def kMeans(commentList, numClusters, numDefiningWords, fName = 'clusters.txt'):
    """A smarter implementation of k means clustering, with the help of a clustering tutorial (thanks Paul!)"""
    #compiling a list of all the words and the stemmed versions
    wordList = []
    cleanWordList = []
    for comment in commentList:
        raw, stemmed = tokenizeAndStem(comment, returnRaw=True)
        wordList+=raw
        cleanWordList+=stemmed
    #use pandas dataframe to be able to look up the stemmed version and get one of the full versions
    stemToWord = pd.DataFrame({'words':wordList}, index=cleanWordList)

    #create a tfidf matrix
    #tfidf matrix is a matrix where the columns are the commetnts and the rows are the words or groups of words
    #tfidf then applies inverse document frequency to weight the words: unique words are weighted more, comment
    #words are weighted less
    #max_df and min_df are maximum and minimum percents. Each term/word has to show up between the min and max percents
    #of the comments to be considered in the final weighting
    tfidfMaker = TfidfVectorizer(max_df=.8, max_features=200000,
                                 min_df=0.001, stop_words=tokenizeAndStem(STOP_WORDS),
                                 use_idf=True, tokenizer=tokenizeAndStem, ngram_range=(1,1))
    #get the actual matrix
    tfidfMatrix = tfidfMaker.fit_transform(commentList)
    print tfidfMatrix.shape
    #get the words that the rows of the matrix represent
    tfidfTerms = tfidfMaker.get_feature_names()
    print tfidfTerms[:20]

    #actual clustering using sklearn kmeans
    km = KMeans(n_clusters=numClusters)
    km.fit(tfidfMatrix)
    #what cluster each comment belongs to
    clusterAssignment = km.labels_.tolist()
    print clusterAssignment[:20]
    clusterFrame = pd.DataFrame({"index":list(range(len(commentList))), "comment":commentList, "cluster":clusterAssignment}, index = clusterAssignment)
    # print clusterFrame
    #grouping ranks by their cluster
    grouped = clusterFrame['index'].groupby(clusterFrame["cluster"])
    print grouped.count()

    #determine the most common words for each cluster
    #i'm not sure what cluster_centers_ is so I'm not sure what this does
    #it seems to work in the tutorial though, so I'm going to use it
    #someone please explain?
    orderCentroids = km.cluster_centers_.argsort()[:, ::-1] #reverse each row; argsort creates an np.array that replaces values with the index that that element
                                                            #has to be at in order to sort that row
    #number of words to show per cluster .encode('utf-8', 'ignore')
    f = open(fName, 'w')
    for i in range(numClusters):
        f.write("Cluster:\n")
        #i took this from the tutorial too; i don't know what orderCentroids is so I don't know what this does either
        f.write("Most Frequent: "+str([stemToWord.ix[tfidfTerms[index].split(' ')].values.tolist()[0][0]  for index in orderCentroids[i, :numDefiningWords]]))
        f.write("\n")
        f.write("Number of Comments: "+str(grouped.count()[i])+"\n")
    f.close()


#Beginnings of dumb clustering
class Cluster:
    """Defines a cluster with comments and a set of the most frequent words"""
    def __init__(self, cluster1=None, cluster2=None):
        """ Creates a new Cluster. Either creates an empty cluster or a cluster Using the data 
            in the 2 given clusters"""
        self.comments = []
        self.frequency = {}
        self.mostFreq = set()
        self.THRESHOLD = 15

        if cluster1!=None:
            self.comments+=cluster1.comments
            self.addFreqs(cluster1.frequency)
        if cluster2!=None:
            self.comments+=cluster2.comments
            self.addFreqs(cluster2.frequency)
        self.setMostFreq()

    def setMostFreq(self):
        """Find the most frequent words and makes a new list"""
        self.mostFreq.clear()
        sortedList = sorted(self.frequency.items(), key=lambda x:x[1])
        for i in range(min(self.THRESHOLD, len(sortedList))):
            self.mostFreq.add(sortedList[i][0])

    def addFreqs(self, freqDict):
        """Adds two dictionaries together, essentially. Mostly a helper method to update
            the frequencies of all the words"""
        for k, v in freqDict.items():
                self.frequency[k]=self.frequency.get(k, 0)+v

    def addComment(self, comment, frequencyDict):
        """Adds a new comment to the list of comments, and updates the necessary attributes"""
        self.comments.append(comment)
        self.addFreqs(frequencyDict)
        self.setMostFreq()

    def addCluster(self, other):
        """Adds all the comments and frequencies of the previous cluster to the new cluster"""
        self.comments+=other.comments
        self.addFreqs(other.frequency)
        self.setMostFreq()

    def intersectPercent(self, other):
        """See by how much this cluster's most frequent words intersects with 
            the other cluster's most frequent words"""
        intersect = len(self.mostFreq & other.mostFreq)
        return float(intersect)/min(len(self.mostFreq), len(other.mostFreq))

    def numComments(self):
        """ Returns the number of comments in this Cluster"""
        return len(self.comments)

    def __str__(self):
        """Returns a string representation of this cluster"""
        return "Cluster:\nMost Frequent: {}\nNumber of Comments: {}".format(str(self.mostFreq), self.numComments())

def dumbClustering(wordList, fName = 'clusters.txt'):
    """
    Clusters by starting each comment as it's own cluster, and seeing which other clusters
    have a lot of words in common with it
    No stemming, all words are included
    It's pretty bad, really.
    """
    #make clusters
    allClusters = []
    for c in wordList:
        tempCluster = Cluster()
        freqTuple = Analysis.wordFrequency([c])
        if len(freqTuple) == 0:
            continue
        freqDict = {}
        for w, f in freqTuple:
            freqDict[w] = f 
        tempCluster.addComment(c, freqDict)
        allClusters.append(tempCluster)
    #play with these values
    start = 1.0
    mid = .6
    end = .3
    step = -1.0/15

    #combine clusters
    dumbClusterStep(start, mid, step, allClusters)

    singleClusters = Cluster()
    for j in range(len(allClusters)-1, -1, -1):
        if allClusters[j].numComments() <= 5:
            singleClusters.addCluster(allClusters[j])
            del allClusters[j]
    allClusters.append(singleClusters)

    dumbClusterStep(mid, end, step, allClusters)

    f = open(fName, 'w')
    for c in allClusters:
        f.write(str(c)+'\n')
    f.close()

def dumbClusterStep(start, end, step, allClusters):
    """
    For all the thresholds in the range specified, combines clusters that intersect
    above that threshold percentage
    """
    for threshold in arange(start, end, step):
        i=0
        while i<len(allClusters):
            current = allClusters[i]
            for j in range(len(allClusters)-1, i, -1): #iterate backwards through the list, from the end to i+1
                if current.intersectPercent(allClusters[j])>=threshold: #100% match
                    current.addCluster(allClusters[j])
                    del allClusters[j]
            i+=1
        print 'Num Clusters', len(allClusters)

if __name__ == '__main__':
    #Testing the Cluster Class
    # c1 = Cluster()
    # c2 = Cluster()
    # print c1
    # c1.addComment("hello", {"hello":1})
    # c1.addComment("good bye", {"good":1, "bye":1})
    # print c1
    # c2.addComment("wow", {"wow":1})
    # c2.addComment("can you please stop", {"can":1, "you":1, "please":1, "stop":1})
    # print c2
    # c1.addCluster(c2)
    # print c1
    # print c1.frequency
    # print c2
    # print c1.intersectPercent(c2)

    #Testing kMeans
    comments = ["hi there who's watching this in 2015?!", "first", "i saw this before it was cool", "This is such a great song", "I saw this back in 2007 when it first came out"]
    kMeans(comments, 2, 3, fName='_test.txt')

