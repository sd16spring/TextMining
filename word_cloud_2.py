"""
Constructs word cloud from edited movie scripts/subtitles
"""

from os import path
import matplotlib.pyplot as plt
from movie_subtitles import edited_file_name, movies1, movies2

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

from scipy.misc import imread

def make_RD_WC(movie_script, image_name):
	"""
	Construct rough draft of word cloud 
	"""

	d = path.dirname(__file__)

	text = open(path.join(d, movie_script)).read()		# open and read movie script for most frequent words excluding stopwords
	
	color_WC = imread(path.join(d, image_name))			# open and read image shape/color
	wordcloud = WordCloud(background_color="white", max_words=2000, mask=color_WC, max_font_size=40, random_state=42)

	wordcloud.generate(text)							# generate word cloud

	image_colors = ImageColorGenerator(color_WC)		# specify font colors based on image colors

	plt.imshow(wordcloud.recolor(color_func=image_colors))		# recolor word cloud from default colors to image colors
	plt.axis("off")										# hide axis (numbers on x and y axis)
	plt.show()											# show final word clouds

def RD_WC_all(movie_list, image_list):
	"""
	Parse through all movie files and all image files to run code for whole list instead of one at a time
	Increase efficiency
	"""

 	for movie in movie_list:
 		i = movie_list.index(movie)						# retrieve index from movie list to retrieve correct image
 		image = image_list[i]							# retrieve corresponding image
  		RD_WC = make_RD_WC(movie, image) 				# call word cloud generator

def edit_all_names(movie_list):	
	"""
	Create new list of edited movie file names to load updated files into word cloud generator

	>>> edit_all_names(['StarWars.srt', 'BTTF.srt'])
	['StarWars_edited.txt', 'BTTF_edited.txt']
	"""

	movies_edited = []
	for movie in movie_list:
		m = edited_file_name(movie)
		movies_edited.append(m)
	return movies_edited

movies_edited_1 = edit_all_names(movies1)
movies_edited_2 = edit_all_names(movies2)

images1 = ['StarWars.jpg', 'TheGodfather.jpg', 'TheMatrix.jpg', 'Rocky.jpg', 'JurassicPark.jpg', 'KillBill1.png', 'LOTR1.jpg', 'ForrestGump.jpg']
images2 = ['Frozen.jpg', 'HSM.jpg', 'Mulan.jpg', 'HarryPotter1.jpg', 'FindingNemo.jpg', 'Up.jpg', 'BTTF.jpg']

RD_WC_all(movies_edited_1, images1)
RD_WC_all(movies_edited_2, images2)