from pattern.web import *
import json,pickle,string

API_KEY = 'AIzaSyCc8GEicGpLlHY6l3PjyeNWVhP2rloC5z0'
API_BASE = 'https://www.googleapis.com/youtube/v3/'
CATEGORY_IDS = [1,2,10,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
	37,38,39,40,41,42,43,44]#store all the categories that exist, taken empirically
							#from the api

#grabs the most popular videos of all time
#test data
# url_test = API_BASE+'search?part=snippet&maxResults=50&order=viewCount&relevanceLanguage=en&type=video&key='+API_KEY

# x =open('test.json','w')
# x.write(URL(url_test).download())
# x.close()

# #taking the test data we wrote, reading in the json, finding each video id and writing all comments to one file.
# data = json.load(open('test.json'))
# commentOut = open('comments.txt','w')
# comments = []

# for i in range(len(data['items'])):
# 	idString = data['items'][i]['id']['videoId']
# 	threadURL = API_BASE+'commentThreads?part=snippet&videoId='+idString+'&textFormat=plainText&key='+API_KEY
# 	threads = json.loads(URL(threadURL).download())['items']
# 	for j in range(len(threads)):
# 		c=threads[j]['snippet']['topLevelComment']['snippet']['textDisplay']
# 		if c.endswith('\\ufeff'):
# 			c=c[:-6]
# 		comments.append(c)
# 		if int(threads[j]['snippet']['totalReplyCount']) > 0:
# 			childURL = API_BASE+'comments?part=snippet&parentId='+threads[j]['snippet']['topLevelComment']['id']+'&textFormat=plainText&key='+API_KEY
# 			print childURL
# 			children = json.loads(URL(childURL).download())['items']
# 			for k in range(len(children)):
# 				childC=children[k]['snippet']['textDisplay']
# 				if childC.endswith('\\ufeff'):
# 					childC=childC[:-6]
# 				comments.append(childC)
# print comments
# pickle.dump(comments,commentOut)

# #parse comments
# readComments = pickle.load(open('comments.txt'))
# allWords = []

# for c in readComments:
# 	s = c.encode('ascii','ignore')
# 	for w in s.split():
# 		allWords.append(w.strip(string.punctuation))
# print allWords



def getComments(idString):
	"""Gets the first 20 parent comments on a video with a given id string, and the first 
		20 replies to each of those comments"""
	allComments = []
	#get parent comments
	threadURL = API_BASE+'commentThreads?part=snippet&videoId='+idString+'&textFormat=plainText&key='+API_KEY
	#print threadURL
	try:
		threads = json.loads(URL(threadURL).download())['items']
		for j in range(len(threads)):
			c=threads[j]['snippet']['topLevelComment']['snippet']['textDisplay'].encode('ascii','ignore')
			if c.endswith('\\ufeff'):
				c=c[:-6] #cut off \ufeff on comments
			allComments.append(c)
			#if there are comment replies on parent comments
			if int(threads[j]['snippet']['totalReplyCount']) > 0:
				childURL = API_BASE+'comments?part=snippet&parentId='+threads[j]['snippet']['topLevelComment']['id']+'&textFormat=plainText&key='+API_KEY
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
		urlCategory = API_BASE+'search?part=snippet&maxResults=50&videoCategoryId='+str(vidCat)+'&order=viewCount&relevanceLanguage=en&type=video&key='+API_KEY

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