"""
Serena Chen
ReadFiles.py
Reads in comments from the youtube api of the most popular youtube videos in each youtube category, writes them to files.
"""
from pattern.web import *
import json,pickle,string

keyFile = open('apikey.txt')
API_KEY = keyFile.readLine()
keyFile.close()
API_BASE = 'https://www.googleapis.com/youtube/v3/'
CATEGORY_IDS = [1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
	37,38,39,40,41,42,43,44]#store all the categories that exist, taken empirically
							#from the api

def getComments(idString):
	"""Gets the first 20 parent comments on a video with a given id string, and the first 
		20 replies to each of those comments"""
	allComments = []
	#get parent comments
	threadURL = '{}commentThreads?part=snippet&videoId={}&textFormat=plainText&key={}'.format(API_BASE, idString, API_KEY)
	#print threadURL
	try:
		threads = json.loads(URL(threadURL).download())['items']
		for j in range(len(threads)):
			c=threads[j]['snippet']['topLevelComment']['snippet']['textDisplay'].encode('ascii','ignore')
			if c.endswith('\\ufeff'):
				c=c[:-6] #cut off \ufeff on comments, some unicode end of line that I want to clean out
			allComments.append(c)
			#if there are comment replies on parent comments
			if int(threads[j]['snippet']['totalReplyCount']) > 0:
				childURL = '{}comments?part=snippet&parentId={}&textFormat=plainText&key={}'.format(API_BASE, threads[j]['snippet']['topLevelComment']['id'], API_KEY)
				children = json.loads(URL(childURL).download())['items']
				for k in range(len(children)):
					childC=children[k]['snippet']['textDisplay'].encode('ascii','ignore')
					if childC.endswith('\\ufeff'):
						childC=childC[:-6]
					allComments.append(childC)
	except HTTP403Forbidden:
		pass #comments are disabled
	return allComments



if __name__=='__main__':
	#grabs comments from 50 potential video categories; only writes a file if the category exists
	for vidCat in CATEGORY_IDS:
		urlCategory = '{}search?part=snippet&maxResults=50&videoCategoryId={}&order=viewCount&relevanceLanguage=en&type=video&key={}'.format(API_BASE, vidCat, API_KEY)

		videos = json.loads(URL(urlCategory).download())
		#write to file
		x =open('cat'+str(vidCat)+'.txt','w')
		pickle.dump(videos,x)
	#Write a different comments file for each 
	for vidCat in CATEGORY_IDS:
		data = pickle.load(open('cat'+str(vidCat)+'.txt'))

		commentOut = open('comments'+str(vidCat)+'.txt','w')
		comments = []

		for i in range(len(data['items'])):
			idString = data['items'][i]['id']['videoId']
			#print idString
			comments+=getComments(idString)
		print comments
		pickle.dump(comments,commentOut)