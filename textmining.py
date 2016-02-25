# searching for Black Lives Matter using Google:
"""
This code searches Google for the top results containing "Black Lives Matter" and processes and plots that data using sentiment analysis.  
@author: Apurva Raman
    apurvaraman.github.com

"""
#import statements
from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt
import numpy as np
import pickle

def search_google(myString, startSearch, endSearch, urlFile, resultsFile):

    """
    This function searches Google for a given string.
    It starts searching at int startSearch and ends the search at int endSearch.
    (the maximum number of querys in 24 hours is 100.)
    It also pickles the list of results and dumps them in a file with name resultsFile (String).

    This function does not return a value. It just creates a pickled file.
    """

    urls = []               #for storing urls
    results = []            #for storing results

    g = Google(license = 'AIzaSyAoce1FyLBFaehlsvQjlZdHHoVGTcfC0iA', throttle = 0.5, language = None)
    # license key, 
    #throttle is the time between requests (0.5 s is reccommended throttle for Google)
    #restriction for Result.language (for Google translate)

    for startPage in range(startSearch, endSearch):
        for result in g.search('MyString',
                type = SEARCH,                          #searching google
                start = startPage,                      #location of start of search
                count = 10,                             #results per page (default at 10)
                size = None,                            #size is for images, we don't want to deal with that right now
                cached = True):                         #just a backup for pickle 
            urls = urls + [result.url]
            results = results + [plaintext(result.text)]
            #print urls
            #print results

    # Save data to a pickled file

    myurls = open(urlFile, 'w')
    pickle.dump(urls, myurls)
    myurls.close()

    myresults = open(resultsFile, 'w')
    pickle.dump(results, myresults)
    myresults.close()

def get_sentiment(myResults):
    """
    Takes in the pickled results file name and performs sentiment analysis on each result. 
    Calls load_pickled_file
    Returns a list of sentiment analysis results.
    """
    sentimentList = [] #creates a list to hold each sentiment

    results = (load_pickled_file(myResults)) #loads the file
    #print results
    resultsFinalIndex = len(results) #finds the final index to run through
    #print len(results)
    for i in range(0, resultsFinalIndex): #runs through each result in the list
         sentimentList += [sentiment(results[i])] 
         #each sentiment is a tuple with the 0 index value as polarity and 1 index as subjectivity
    return sentimentList

def get_polarity_subjectivity(myResults):

    """
    Takes in the pickled results file name
    Calls get_sentiment
    Returns a list with the polarity of each result, the average polarity, 
    the subjectivity of each result, and the average subjectivity
    """

    sentimentList = get_sentiment(myResults)

    polarityList = [item[0] for item in sentimentList]
    subjectivityList = [item[1] for item in sentimentList]

    avgPolarity = average_list(polarityList)
    avgSubjectivity = average_list(subjectivityList)

    sentimentData = [[polarityList], [avgPolarity], [subjectivityList],[avgSubjectivity]]
    return sentimentData

def average_list(myList):
    """
    Finds the average of the elements in a list. 
    """

    return sum(myList)/float(len(myList))

def plot_polarity(myResults):
    """
    Plots the polarity of the data against its index.  
    Takes in the pickled results file name
    calls get_polarity_subjectivity
    Calls plot_list to plot the polarity
    Returns nothing
    """

    sentimentData = get_polarity_subjectivity(myResults)
    polarityList = sentimentData[0]
    plot_list(polarityList)

def plot_subjectivity(myResults):
    """
    Plots the subjectivity of the data against its index.  
    Takes in the pickled results file name.
    Calls get_polarity_subjectivity
    Calls plot_list to plot the subjectivity.
    Returns nothing.
    """
    
    sentimentData = get_polarity_subjectivity(myResults)
    subjectivityList = sentimentData[2]
    plot_list(subjectivityList)

def plot_list(myList):
    """
    Plots list myList. 
    Formatted so it can handle the list with polarities or the list with subjectivities.
    Returns nothing.
    """

    myList = [j for i in myList for j in i]
    indexList = range(len(myList))
    plt.plot(myList)
    plt.show()

def load_pickled_file(myFile):
    """
    This function loads a pickled file. Takes in string with the file name.
    Returns the corresponding list.
    """
    input_file = open(myFile,'r')
    reloaded_copy_of_texts = pickle.load(input_file)
    return reloaded_copy_of_texts

#plot_subjectivity('results.pickle')

#myResults = load_pickled_file('results.pickle')
#print myResults[0]
#print sentiment(myResults[0])
#print myResults[1]
#print sentiment(myResults[1])

