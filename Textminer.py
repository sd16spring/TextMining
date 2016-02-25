'''This program finds all of the Olinsider articles and downloads them to find the sentiment of the articles'''

import doctest
import string
import re
import unicodedata
import numpy as np
import matplotlib.pyplot as plt
from pattern.web import *
from os.path import exists
from bs4 import BeautifulSoup
from pickle import dump, load
from pattern.en import *

months = {  'january':1,
			'february':2,
			'march':3,
			'april':4,
			'may':5,
			'june':6,
			'july':7,
			'august':8,
			'september':9,
			'october':10,
			'november':11,
			'december':12
		}

folder = 'Data/'

def save_data(dat, filename):
	''' This function takes in data and a file name

		It opens up the file, and uses pickle to dump the data into the file before closing it.
	'''
	outfile = open(folder + filename, 'wb')
	dump(dat, outfile)
	outfile.close()

def get_data(filename):
	''' This function takes a filename and tries to opon the file

		If it can't open the file, it will return None
		Otherwise, it will return the unpickled data from within the file
	'''
	try:
		infile = open(folder + filename, 'rb')
		dat = load(infile)
		infile.close()
		return dat
	except:
		return None

def mine_olinsider(url):
	''' This function takes the end part of an Olin website url

		It creates a file name from the given url uses get_data to check if the file exists

		If it does not exist, it will download the webpage sourcecode and save the data
		Otherwise, it will return what it got from get_data
		'''
	filename = 'Data'+url.replace('/', '')+'.dat'
	if get_data(filename) == None:
		print('getting data')
		x = URL('http://www.olin.edu'+url).download()
		save_data(x, filename)
		return x
	else:
		x = get_data(filename)
		return x

def mine():
	''' This function goes through the Olinsider to get the articles and returns their sourcecodes in a list
	
		It downloads the sourcecode for the mainpage if it doesn't already exist and then parses it to get the urls for the articles by month
		It then goes through and downloads the sourcecode for the articles by month if they don't already exist and then parses it for the urls for the articles
		It then goes through and downloads the sourcecode for the articles if they don't already exist and returns a list of the sourcecode of the articles
	'''
	#getting the main Olinsider page
	url = '/blog/the-olinsider/'
	main_page = mine_olinsider(url)
	dat = main_page.split('\"')
	month_urls = []
	#searching through the mainpage source code to find the articles by month urls
	for d in dat:
		if '/blog/the-olinsider/by-date' in d:
			month_urls.append(d.split('::')[1])
	intermediate = []
	posturls = []
	#getting the articles by month sourcecodes
	for url in month_urls:
		intermediate.append(mine_olinsider(url))
	for i in intermediate:
		s = i.split('\"')
		#searching through the by month sourcecodes for the article urls
		for url in s:
			if '/blog/the-olinsider/post/' in url:
				h = url.replace('#disqus_thread', '')
				posturls.append(h)
	#removing repeated urls
	posturls = set(posturls)
	post_source = []
	#getting the article sourcecode
	for url in posturls:
		post_source.append(mine_olinsider(url))
	return post_source

def filter_unicode(source):
	''' This function goes through a string and removes all unicode characters from strings in a list and returns the list of strings

		>>> filter_unicode([unicodedata.lookup("sailboat")+'hello'])
		[u'hello']
	'''
	filtered = []
	printable = set(string.printable)
	for sourcecode in source:
		filtered.append(filter(lambda x: x in printable, sourcecode))
	return filtered

def filter_old(source, search):
	''' This function filters through the old style of posts where the article text was stored in dividers
		It is also used to get the date from the new and old posts
	'''
	divs = []
	data = []
	soup = BeautifulSoup(source, "lxml")
	div = soup.find_all('div')
	for d in div:
		if str(d) not in divs:
			divs.append(str(d))
	for div in divs:
		soup2 = BeautifulSoup(div, "lxml")
		tag = soup2.div
		try:
			if tag['class'] in search:
				for t in tag.contents:
					soup = BeautifulSoup(str(t), 'lxml')
					#removes all html that is still in the post
					all_text = ''.join(soup.findAll(text=True))
					data.append(all_text)
		except:
			'''Not a date or post'''
	return data

def filter_new(source):
	''' This function filters through the new style of posts where the article text is stored in paragraphs
		It calls filter_old to get the date from the article which is still stored in dividers
	'''
	divs = []
	data = []
	data.append(filter_old(source, [['blog-post-date']])[0])
	soup3 = BeautifulSoup(source, "lxml")
	div = soup3.find_all('p')
	for d in div:
		if str(d) not in divs:
			divs.append(str(d))
	for div in divs:
		soup4 = BeautifulSoup(div, "lxml")
		tag = soup4.p
		try:
			if tag['class'] == ['MsoNormal']:
				for t in tag.contents:
					soup = BeautifulSoup(str(t), 'lxml')
					#removes all html that is still in the post
					all_text = ''.join(soup.findAll(text=True))
					if all_text not in data:
						data.append(all_text)
		except:
			'''Not a date or post'''
	return data

def update_data(data, filename):
	''' This function checks if the filtered, processed data is up to date

		up to date meaning that there are no new articles

		If the data is not up to date, it will open up all the articles and process them again
		If the data is up to date, it will return the previously stored data
	'''
	prev_posts = get_data(filename)
	if prev_posts == None:
		prev_posts = []
	if len(data) != len(prev_posts):
		posts = []
		for dat in data:
			if 'MsoNormal' in dat:
				posts.append(filter_new(dat))
			else:
				posts.append(filter_old(dat, [['blog-post-date'],['blog-post-body']]))
		save_data(posts, 'Filtered_Posts.dat')
		return posts
	else:
		return prev_posts

def parse_date(date):
	''' This function takes a date and puts it into a list of month-day-year and turns the string month into an int

		>>> parse_date('April 23, 2013')
		[4, 23, 2013]
	'''
	date = date.replace(',', '')
	date = date.split(' ')
	date[0] = months[date[0].lower()]
	date[1] = int(date[1])
	date[2] = int(date[2])
	return date

def process_posts(posts):
	''' This function goes through a list of lists of dates and posts and removes all unnecessary stuff from posts such as numbers, punctuation, most unnecessary whitespace and newlines
		It also removes all dates that do not have an associated post

		It returns a list of lists of dates that have gone through parse_date and posts
		eg: [[date1, post1], [date2, post2], ect...]

		>>> process_posts([['April 23, 2013', 'Hello239014 there!!'], ['May 13, 2007']])
		[[[4, 23, 2013], 'Hello there']]
	'''
	real_posts = []
	for post in posts:
		if len(post) <= 1:
			continue
		date = parse_date(post[0])
		post = post[1:]
		s = ''
		for sub in post:
			s += sub
		s = s.replace('\n', '')
		s = ''.join([i for i in s if not i.isdigit()])
		s = re.split('[?,!-<>]', s)
		article = ''
		for chain in s:
			chain = chain.strip()
			article += chain +' '
		real_posts.append([date, article.strip()])
	return real_posts

def get_sentiment(posts):
	''' This function takes in a list posts and returns 2 lists of the polarity and subjectivity, respectively'''
	polarity = []
	subjectivity = []
	for post in real_posts:
		sent = sentiment(post[1])
		polarity.append(sent[0])
		subjectivity.append(sent[1])
	return polarity, subjectivity

def process_dates(posts, polarity, subjectivity):
	''' This function takes in a list of posts, polarity, and subjectivity

		It gets the dates from the posts and returns a list of the year, month, polarity, and subjectivity of each post
	'''
	dates = []
	for post in posts:
		dates.append(post[0])
	for i in range(len(dates)):
		dates[i] = [dates[i][2], dates[i][0], polarity[i], subjectivity[i]]
	return dates

if __name__ == '__main__':
	doctest.testmod()
	source = mine()
	filtered_posts = filter_unicode(source)
	posts = update_data(filtered_posts, 'Filtered_Posts.dat')
	real_posts = process_posts(posts)
	polarity, subjectivity = get_sentiment(real_posts)
	date_data = process_dates(real_posts, polarity, subjectivity)
	date_data = sorted(date_data)
	rang = date_data[-1][0] - date_data[0][0]
	
	# Scatter plot of the data
	plt.scatter(polarity, subjectivity, marker = '*', color = 'g')
	plt.axis([-1, 1, 0, 1])
	plt.grid(True)
	plt.xlabel('Polarity (Negative to Positive)')
	plt.ylabel('Subjectivity (Objective to Subjective)')
	plt.title('Polarity vs Subjectivity for Olinsider posts')
	plt.savefig('ScatterPlot.eps')
	plt.clf()

	years = []
	for i in range(rang+1):
		months = []
		for date in date_data:
			if date[0] == i + date_data[0][0]:
				months.append(date[1:])
		years.append(sorted(months))

	bymonth = []
	for year in years:
		mon = []
		for i in range(1,13):
			counter = 0
			polarity = 0
			subjectivity = 0
			for month in year:
				if month[0] == i:
					polarity += month[1]
					subjectivity += month[2]
					counter +=1
			if counter > 0:
				mon.append([float(polarity/counter), float(subjectivity/counter)])
			else:
				mon.append([0, 0])
		bymonth.append(mon)

	# Scatter plot over time of the data
	avg_pol = []
	avg_sub = []
	for year in bymonth:
		for month in year:
			avg_pol.append(month[0])
			avg_sub.append(month[1])
	pol = plt.scatter(range(len(avg_pol)), avg_pol, marker = '*', color = 'g')
	sub = plt.scatter(range(len(avg_pol)), avg_sub, marker = 'o', color = 'b')
	plt.axis([0, len(avg_pol), 0, 1])
	plt.xticks(np.arange(0, len(avg_pol)+1, 12))
	plt.xlabel('Months since the first Olinsider post')
	plt.ylabel('Subjectivity/Positivity')
	plt.title('Polarity and Subjectivity vs time for Olinsider posts')
	plt.legend((pol, sub), ('Average Positivity', 'Average Subjectivity'), scatterpoints = 1, loc = 'upper center')
	plt.savefig('ScatterOverTime.eps')
	plt.clf()

	# Bar graph of the data
	n = 9
	ind = np.arange(12)
	width = 1./(1+n)
	colors = ['#000000', '#FE2E2E', '#FF8000', '#FFFF00', '#74DF00', '#01DFA5', '#00BFFF', '#0101DF', '#8904B1', '#DF0174']
	labels = range(2007,2017) 
	ticks = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	pol_bymonth = []
	sub_bymonth = []
	for year in bymonth:
		mon = []
		mon2 = []
		for month in year:
			mon.append(month[0])
			mon2.append(month[1])
		pol_bymonth.append(mon)
		sub_bymonth.append(mon2)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	for year in range(len(pol_bymonth)):
		ax.bar(ind+year*width, pol_bymonth[year], width, color = colors[year], label = str(labels[year]))
	plt.xticks(ind+n/2.*width, ticks)
	ax.tick_params(axis='x', labelsize=8)
	plt.gcf().subplots_adjust(right=0.85)
	plt.xlabel('Month')
	plt.ylabel('Positivity')
	plt.title('Average Polarity for a given month and year')
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.set_size_inches(9, 5)
	fig.savefig('PolarityBar.eps')
	plt.clf()

	fig = plt.figure()
	ax = fig.add_subplot(111)
	for year in range(len(sub_bymonth)):
		ax.bar(ind+year*width, sub_bymonth[year], width, color = colors[year], label = str(labels[year]))
	plt.xticks(ind+n/2.*width, ticks)
	ax.tick_params(axis='x', labelsize=8)
	plt.gcf().subplots_adjust(right=0.85)
	plt.xlabel('Month')
	plt.ylabel('Subjectivity')
	plt.title('Average Subjectivity for a given month and year')
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.set_size_inches(9, 5)
	fig.savefig('SubjectivityBar.eps')
	plt.clf()