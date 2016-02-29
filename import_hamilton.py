"""this is the file i'll use to import/download all of the hamilton lyrics
into text files"""

# packages are useful
from bs4 import BeautifulSoup
import requests
from lxml import html


def find_links(soup):
    """this function takes in an html file and returns a list of the
    links within the html file."""
    list_o_links = []
# this iterates through all links in the html file and appends them to a list
    for link in soup.find_all('a'):
        list_o_links.append('http://www.themusicallyrics.com/' + link.get('href'))
# and the list gets returned
    return list_o_links


def cull_links(beginning_url, list_urls):
    """this function takes in the beginning of a URL and a list of URLs and
    returns a list of URLs that begin with the beginning_url."""
    new_list_urls = []
# iterates through the list of URLs; if an item contains the desired URL,
# appends the item to the new list of URLs.
    for x in list_urls:
        if beginning_url in x:
            new_list_urls.append(x)
    return new_list_urls


def file_names(list_of_links, base_name):
    n = len(list_of_links)
    names_list = []
    for i in range(n):
        names_list.append(base_name + '_' + str(i) + '.txt')
    return names_list


def save_files(list_of_links, list_of_names):
    for i in range(len(list_of_links)):
        song = requests.get(list_of_links[i])
        text_file = open(list_of_names[i], "w")
        text_file.write(song.content)
        text_file.close

# i can get the html of the page i want
url_source = requests.get('http://www.themusicallyrics.com/h/351-hamilton-the-musical-lyrics.html')
# i can save it in a file
text_file = open('url_page.txt', 'w')
text_file.write(url_source.content)
text_file.close

# this lets me use BeautifulSoup because i want to
soup = BeautifulSoup(url_source.content, 'lxml')

# this uses the find_links function and defines which links i want
some_urls = find_links(soup)
useful_url = '/351-hamilton-the-musical-lyrics/'

# this makes a list of links and a base name for naming the files i create
list_of_links = cull_links(useful_url, some_urls)
base_name = 'hamilton'

# this is a list of names for the files i create
names_list = file_names(list_of_links, base_name)

# me doing the save_files thing manually to debug
# song = requests.get(list_of_links[0])
# text_file = open(names_list[0], "w")
# text_file.write(song.content)
# text_file.close

# this uses the save_files function to get all the things i want
save_files(list_of_links, names_list)

####### here is where the actual code stops

# print file_names([1, 2, 3, 4, 5, 6], 'hamilton')

# alexander_hamilton = URL('http://www.themusicallyrics.com/h/351-hamilton-the-musical-lyrics/3706-alexander-hamilton-lyrics.html').download()
# text_file = open("hamilton_1.txt", "w")
# text_file.write(alexander_hamilton)
# text_file.close

# soup = BeautifulSoup(lyrics, "html.parser")

# some_urls = find_links(soup)

# print find_links(soup)

# how to do get an html file of a lyrics page
# soup = BeautifulSoup(lyrics, "html.parser")
# text_file = open("Output.txt", "w")
# text_file.write(soup.prettify().encode("UTF-8"))
# text_file.close()
