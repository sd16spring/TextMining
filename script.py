import praw
from pattern.en import *
import numpy

r = praw.Reddit(user_agent='my_app')

#for post in processed_posts:
#    print post, sentiment(post)

def get_titles(subreddit):
    '''
        Takes string subreddit as a subreddit to search for.
        Returns a list of titles of first 20 current hot posts
    '''
    submissions = r.get_subreddit(subreddit).get_hot(limit=100)
    posts = [str(submission) for submission in submissions]
    processed_posts = []
    for post in posts:
        processed_posts.append(post.translate(None, '0123456789:')) #deletes all numbers and colons to get rid of upvote nums
    return processed_posts

def get_sentiments(posts):
    '''
        Given a list of strings which represent post titles, return an average sentiment value of the subreddit
    '''
    sentiments = []
    for post in posts:
        sentiment_value = sentiment(post)
        if abs(sentiment_value[0]) < 0.1:
            continue #don't include this value because it means sentiment analysis wasn't successful
        else:
            sentiments.append(sentiment_value[0])
    return numpy.mean(sentiments)

def order_subreddit(subreddits):
    '''
        Given a list of strings of subreddit names, return a list of tuple (subreddit name, sentiment value) in an descending order of sentiment value.
        Most positive subreddit will come first and most negative subreddit will come last.
    '''
    result = []
    for subreddit in subreddits:
        result.append((get_sentiments(get_titles(subreddit)),subreddit))
    result.sort(reverse=True)
    
    ordered_result = []
    for sentiment_value, subreddit_title in result:
        ordered_result.append((subreddit_title, sentiment_value))
    
    return ordered_result

#print get_titles('nba')
#print 'aww: ', get_sentiments(get_titles('aww'))
#print 'nba: ', get_sentiments(get_titles('nba'))
#print 'tifu: ',get_sentiments(get_titles('tifu'))
subreddits = ['aww','nba','science','nottheonion','worldnews']
print order_subreddit(subreddits)
