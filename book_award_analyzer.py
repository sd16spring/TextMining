from bs4 import BeautifulSoup
import urllib2, sys, re
from HTMLParser import HTMLParser
import indicoio
indicoio.config.api_key = '1b3a2e80bc0395cfe488c1bdceea85d9'
import matplotlib.pyplot as plt




class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def wiki_summary(title):   
    """
    takes a string of a book title and returns a wikipedia summary of that book
    title: a string that is a book title
    returns: a wikipedia summary of that book in string form

    """
    special_case = ['_For_', '_The_', '_A_', '_In_','_Of_','_On_','_From_','_Is_', "'S", "Novel","_To_"]  
    special_case_replace = ['_for_', '_the_', '_a_', '_in_','_of_','_on_','_from_','_is_',"'s", "novel","_to_"]                                                                            
    title = title.replace(" ", "_")
    title = title.strip(" ").title()
    title_extra = "_(novel)"
  
    site = "http://en.wikipedia.com/wiki/" + title
  
 
    for i in range (0, len(special_case)):
        if str(special_case[i]) in site:
            site = site.replace(str(special_case[i]),str(special_case_replace[i])) 
    
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site,headers=hdr)
    page = urllib2.urlopen(req)

    soup = BeautifulSoup(page, 'html.parser')

    if soup.find(id="Plot") == None and soup.find(id="Plot_summary") == None \
    and soup.find(id="Synopsis") == None and soup.find(id="Summary") == None:
        site = "http://en.wikipedia.com/wiki/" + title + title_extra
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(site,headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
  
    
    plot_location_1 = str(soup.find(id="Plot"))
    plot_location_2 = str(soup.find(id="Plot_summary"))
    plot_location_3 = str(soup.find(id="Synopsis"))
    plot_location_4 = str(soup.find(id="Summary"))


    body = str(soup.body)
    if plot_location_1 in body:
    	index = body.index(plot_location_1)
    elif plot_location_2 in body:
    	index = body.index(plot_location_2)
    elif plot_location_3 in body:
    	index = body.index(plot_location_3)
    elif plot_location_4 in body:
    	index = body.index(plot_location_4)
    else:
    	return ""


    plot_loc = body[index:]
    index_para_start = plot_loc.index("<p>")
    index_para_end = plot_loc.index("<h2>")

    unstripped = str(plot_loc[index_para_start:index_para_end])

    stripped = stripHTMLTags(unstripped)
    strippedd = stripBrackets(stripped)
    return stripCaptions(strippedd)

def stripHTMLTags(html):
    """ removes html syntax from text
        html: a string with html syntax in it
        returns: a string stripped of html syntax

    """ 

    html = re.sub(r'<{1}br{1}>', '\n', html)
    s = MLStripper()
    s.feed(html)
    text = s.get_data()
    if "External links" in text:
        text, sep, tail = text.partition('External links')
    if "External Links" in text:
        text, sep, tail = text.partition('External Links')
    text = text = text.replace("See also","\n\n See Also - \n")
    text = text.replace("*","- ")
    text = text.replace(".", ". ")
    text = text.replace("  "," ")
    text = text.replace("""   /
        / """, "")
    return text

def stripBrackets(text):
    """ removes brackets with a number between 1 and 100 between them from text
        text: a string to modify
        returns: the input string without brackets
    """
    for i in range(100):
        text = text.replace("[" + str(i) + "]","")
    return text

def stripCaptions(text):
    """ removes paragraphs in a string shorter than 40 characters
        text: a string in paragraph form
        returns: a string stripped of paragraphs shorter than 40 characters
    """
    paragraphs = text.split("\n")
    new_paragraphs = []

    for paragraph in paragraphs:
        if len(paragraph) > 40:
            new_paragraphs.append(paragraph)
    return '\n\n'.join(new_paragraphs)

if __name__ == "__main__":
    sentiment = []
    books = ['The Man with the Golden Arm', 'From here to eternity', 'invisible man',\
     'the adventures of augie march', \
    'The Moviegoer','The Centaur',
    'Herzog',
    'The Fixer',
    'them',
    'Augustus_(Williams_novel)',
    'The World According to Garp',
    'White Noise',
    'Middle Passage',
    'The Shipping News',
    'A Frolic of His Own',
    'Cold Mountain',
    'The Corrections',
    'Three Junes',
    'Europe Central',
    'Tree of Smoke',
    'Let the Great World Spin',
    'The Round House',
    'The Good Lord Bird',]


    for i in books:
       
        summary = (wiki_summary(i))
        sentiment.append((indicoio.sentiment(str(summary))))

    axes = plt.gca()
    plt.title('Sentiment of National Book Award Winners (Fiction)')
    plt.ylabel('Sentiment')
    plt.xlabel('Books (in Chronological Order)')
    axes.set_xlim([0,22])
    axes.set_ylim([0,1]) 
    plt.plot(sentiment)
    plt.show()
    #print summary
    #print(indicoio.sentiment(str(summary)))


