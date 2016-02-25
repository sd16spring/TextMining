import random
'''This program takes as an input a variety of texts, and outputs a list of the most used words
    in each text, as well as a comparison between the texts.
    Author: Anna Buchele'''

def wordcounter(document):
    """Takes as input a .txt document, and removes punctuation, capitalization, and turns the document into a list of words.
    Then, it finds the frequency each word is used. It returns a dictionary with a key for each word used, and the value as 
    the number of times the word is used in the book."""
    f=''
    for word in document:
        f= f+word
    a= f.replace(".", "")
    a= a.replace(",", "")
    a=a.replace("'","")
    a=a.replace('"','')
    a=a.replace(':','')
    a=a.replace('?','')
    a=a.replace(';','')
    a=a.replace('!','')
    a=a.replace('-','')
    a=a.replace('*','')
    a=a.replace("/", '')
    a=a.replace('\'','')
    a=a.replace('\xe2\x80\x94','')
    a=a.replace('\xe2\x80\x99','')
    a=a.replace('\xe2\x80\x9c','')
    a=a.replace('\xe2\x80\x9d','')
    a=a.lower()
    l=a.split()
    wordscount=dict()
    for word in l:
        val= wordscount.get(word,0)
        wordscount[word]=val+1
            
    wordssort= sorted(wordscount,key=wordscount.__getitem__,reverse=True)
    return wordssort


def textimport(startdecade, enddecade):
    """Takes as input a start decade, end decade to be analyzed and imports the most popular texts from that period
    into the library, and then runs wordcounter on it. Returns the wordcount of each decade between the decades input."""
    analyses= []
    if startdecade <= 1899:
        return None
    elif startdecade > 1970:
        return None
    else:
        for x in range (((enddecade-startdecade)+10)/10):
            decade = startdecade + 10*x
            if decade == 1900:
                b1900 = open('anne.txt', 'r')
                analyses+= [wordcounter(b1900)]
            elif decade == 1910:
                b1910 = open('secretgarden.txt', 'r')
                analyses+= [wordcounter(b1910)]
            elif decade == 1920:
                b1920 = open('gatsby.txt', 'r')
                analyses+= [wordcounter(b1920)]               
            elif decade == 1930:
                b1930 = open('gonewiththewind.txt', 'r')
                analyses+= [wordcounter(b1930)]               
            elif decade == 1940:
                b1940 = open('1984.txt', 'r')
                analyses+= [wordcounter(b1940)]                
            elif decade == 1950:
                b1950 = open('f451.txt', 'r')
                analyses+= [wordcounter(b1950)]
            elif decade == 1960:
                b1960 = open('mockingbird.txt', 'r')
                analyses+= [wordcounter(b1960)]
            elif decade == 1970:
                b1970 = open('hitchhiker.txt', 'r')
                analyses+= [wordcounter(b1970)]
            else:
                return None
    return analyses


def analize(startdecade,enddecade,numwords):
    """Takes as input a decade to start analyzation, a decade to end it, and the number of words of each book
    to be analyzed. It then takes the dictionary of values and makes a new nested list of the top X number of words 
    to be analyzed for each book. Then, for each word in each book, it counts the number of other books studied in which
    the word is in the top X most used words. Then, for each subset of words (words in the top X most used words in:
        every book, every book but one, 4-6 books, 2-3 books, and only one book) it finds which books the word was
    used so frequently in. It prints a few strings that says what each data strand is, and then outputs the data."""
    top20 = []
    similar = {}
    different = []
    frequencies = textimport(startdecade,enddecade)
    numdecades= ((enddecade-startdecade)+10)/10
    for x in range (numdecades):
        eachbook = frequencies[x]
        eachbook20 = eachbook[:numwords]
        top20 += [eachbook20]
    for x in range (numdecades):
        for y in range (numwords):
            book = top20[x]
            word = book[y]
            val=similar.get(word,0)
            val=val+1
            similar[word]=val

    similar2 = sorted(similar.items(),key=operator.itemgetter(1), reverse=True)
    allbooks=[]
    almostallbooks=[]
    onlyonebook=[]
    mostbooks=[]
    fewbooks=[]
    for a in similar:
        if similar[a] == numdecades:
            allbooks+=[a]
        elif similar[a] == (numdecades-1):
            almostallbooks+=[a]
        elif similar[a]== 1:
            onlyonebook+=[a]
        elif 6 >= similar[a] >= 4:
            mostbooks+=[a]
        elif similar[a]== 2 or 3:
            fewbooks += [a]
        else:
            print 'ERROR!'

    almostall={}
    almostdec={}
    for a in almostallbooks:
        for x in range (numdecades):
            testbook=top20[x]
            dec= (10*x)+1900
            if a in testbook:
                pass
            else:
                almostall[a]=(10*x)+1900
                v=almostdec.get(dec,0)
                almostdec[dec]=v+1
    most={}
    mostdec={}
    for a in mostbooks:
        for x in range (numdecades):
            dec= (10*x)+1900            
            testbook=top20[x]
            if a in testbook:
                if a in most:
                    p=[]
                    p+= [most[a]]
                    p+= [dec]
                    most[a]= p
                    v=mostdec.get(dec,0)
                    mostdec[dec]=v+1
                else:
                    most[a]= dec
                    v=mostdec.get(dec,0)
                    mostdec[dec]=v+1
            else:
                pass
    one={}
    onedec={}
    for a in onlyonebook:
        for x in range (numdecades):
            dec= (10*x)+1900 
            testbook=top20[x]
            if a in testbook:
                one[a] =(10*x)+1900
                v=onedec.get(dec,0)
                onedec[dec]=v+1

    few={}
    fewdec={}
    for a in fewbooks:
        for x in range (numdecades):
            dec= (10*x)+1900 
            testbook=top20[x]
            if a in testbook:
                if a in few:
                    p=[]
                    p+= [few[a]]
                    p+= [(10*x)+1900]
                    few[a]= p
                    v=fewdec.get(dec,0)
                    fewdec[dec]=v+1
                else:
                    few[a]= (10*x)+1900
                    v=fewdec.get(dec,0)
                    fewdec[dec]=v+1
            else:
                pass
    for x in range (numdecades):
        #testing to make sure all the numbers add up right
        dec= (10*x) + 1900
        allb= len(allbooks)
        alm= almostdec.get(dec,0)
        mo= mostdec.get(dec,0)
        o=onedec.get(dec,0)
        f=fewdec.get(dec,0)
        val= allb + (15-alm) + mo + o + f
        if val == 100:
            pass
        else:
            print 'PROBLEM'


    print "these words were in the %d most frequently used words of every book studied" %(numwords)
    print allbooks
    print 'count='+str(len(allbooks))
    print "the books studied were each the most popular book of their decade, from %d to %d" %(startdecade,enddecade)

    print "these words were in the %d most frequently used words of every book studied except one" %(numwords)
    print almostall
    print almostdec

    print "these words were in the %d most frequently used words of between 4 and 6 of the 8 books studied" %(numwords)
    print most
    print mostdec

    print "these words were in the %d most frequently used words of 2 or 3 of the 8 books studied" %(numwords)
    print few
    print fewdec

    print "these words were in the %d most frequently used words of only one book studied" %(numwords)
    print one
    print onedec

import operator
analize(1900,1970,100)
