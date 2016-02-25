#Reddit Buzz Miner

#The purpose of this script is to find the most common words in a reddit post, filter out
#common particles such as "the", "a", etc, and then determine what percent of the post
#comments are the buzzwords.  Then compare the buzz of each post.
#I choose to ignore sticky posts to simply add complexity and also in a sense a bit more
#feel for what is trending outside of moderator sticky.  
from pattern.en import *
import praw
r = praw.Reddit(user_agent='Reddit_Post_Buzz_Miner')

#Apparently subreddits can only have a maximum of two stickied posts.  I assumed there could be
#more, but this makes my life easier.  So I just search 3 top posts. 

subreddit = r.get_subreddit('fireemblem') #Gets the subreddit of interest. 
hotlist_generator = subreddit.get_hot(limit=3) #Gets the top 3, including or not including stickies
hotlist = []
for x in hotlist_generator:
	hotlist.append(x)
#The following are the individual cases for sticky identification.
#Either the first, second, or third submissions are not sticky.	
if (hotlist[0] == subreddit.get_sticky(bottom=True)) and \
(hotlist[1] == subreddit.get_sticky(bottom=False)):
	top = hotlist[2] #1st and 2nd are sticky
elif hotlist[1] != subreddit.get_sticky(bottom=False):
	top = hotlist[1] #only 1st is sticky
else:
	top = hotlist[0] #1st is not sticky

top.replace_more_comments(0,1) #Should get rid of "more_comment" objects
comments = top.comments #List of comments (cannot specify number yet).  

#for x in comments:
#	if x.replies != None: #Replies are important.  Had I more time I would follow it to the end.
#		comments.append(x.replies)
#	elif x = None: #In case the comment is deleted.  
#		comments.remove(x)


flat_comments = praw.helpers.flatten_tree(comments) 
#Flattening makes an unordered list of comments.
#Apparently it also includes replies

if len(flat_comments) > 200:
	flat_comments = flat_comments[0:200] #cuts the total list to 200.

buzz = dict()

for comment in flat_comments: #This will put all the commments in buzz. 
	text = comment.body.split() #The text attribute of comment.body
	for word in text:
		if word not in buzz:
			buzz[word] = 1
		else: 
			buzz[word] += 1

sorted_list = []
not_helpful_words = ['a', 'the', 'to', 'I', 'and', 'you', 'is', 'for', 'it', 'of']
#list of not helpful words, i.e. particles, etc.  At this point, manually updated.
#Future work could include noun detection.  

for word in buzz:
	if word not in not_helpful_words:
		sorted_list.append((buzz[word], word))

sorted_list.sort(reverse=True) #sort the list

top10 = sorted_list[0:10]
print top10 #the buzzwords delivered.  




	