"""this contains the code and functions to parse the lyrics from the text files
"""

# let's import some useful things
from bs4 import BeautifulSoup

# here is the functions i will use


def make_a_soup(filename):
    """opens the file, defines a variable as the file, and returns it
    """
    current_song = open(filename)
    important = current_song.read()
    current_song.close
    return important


def find_lyrics(soup):
    """finds the section of the html file that contains the lyrics
    turns it into a list
    turns that into one string
    """
    start = soup.find('</em>') + 5
    end = soup[start:].find('</p>')
    new_soup = soup[start:end]
    list_lyrics = new_soup.split('<br />')
    string_lyrics = ' '.join([x for x in list_lyrics])
    return string_lyrics


def tuples_of_lyrics(string_o_lyrics):
    """takes in a string of lyrics
    splits it by '  ' (every time the character speaking/singing changes)
    splits each of those into a tuple ('CHARACTER', 'Lyrics')
    returns a list of tuples
    """
    list_of_strings_of_lyrics = string_o_lyrics.split('  ')
    list_of_tuples = []
    for x in list_of_strings_of_lyrics:
        if x:
            avocado = tuple(x.split(': '))
            list_of_tuples.append(avocado)
    return list_of_tuples


def names(number_of_songs, base_name):
    n = number_of_songs
    names_list = []
    for i in range(n):
        names_list.append(base_name + '_' + str(i) + '.txt')
    return names_list


def filenames(number_of_songs, base_name):
    n = number_of_songs
    names_list = []
    for i in range(n):
        names_list.append(base_name + '_' + str(i) + '.html')
    return names_list


def assign_names(number_of_songs, base_name_name, base_name_file):
    names_list = names(number_of_songs, base_name_name)
    filenames_list = filenames(number_of_songs, base_name_file)
    for i in range(len(names_list)):
        x = tuples_of_lyrics(find_lyrics(make_a_soup(filenames_list[i])))
    return names_list

names_list = names(46, 'hamilton_lyrics')
filenames_list = filenames(46, 'hamilton')
lyric = []
for i in range(46):
    lyric.append(tuples_of_lyrics(find_lyrics(make_a_soup(filenames_list[i]))))
n = 9
# print ''
# print names_list[n]
# print ''
print lyric[n]

soup = make_a_soup('hamilton_9.html')

start = soup.find('</em>') + 5
end = soup[start:].find('</p>')
new_soup = soup[start:end]
list_lyrics = new_soup.split('<br />')
string_lyrics = ' '.join([x for x in list_lyrics])
# print start
# print end
# print soup[start:end]
# if lyric[n][2]=None:
#     print '...'

assign_names(46, 'hamilton_lyrics', 'hamilton')

# print tuples_of_lyrics(find_lyrics(make_a_soup('hamilton_0.html')))
