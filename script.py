"""
This is a python script that analyzes the positivity of a subreddit by running sentiment analysis on the title of the subreddit's 'hot' posts
"""

import praw
from pattern.en import *
from numpy import mean

r = praw.Reddit(user_agent='my_app')

def get_titles(subreddit):
    '''
        Takes string subreddit as a subreddit to search for.
        Returns a list of titles of first 100 current hot posts
    '''
    submissions = r.get_subreddit(subreddit).get_hot(limit=100)
    posts = [str(submission) for submission in submissions]
    processed_posts = []
    for post in posts:
        processed_posts.append(post.translate(None, '0123456789:')) #deletes all numbers and colons to get rid of upvote nums
    return processed_posts

def get_comments(subreddit,n):
    '''
        Takes string subreddit as a subreddit to search for.
        Returns a list containing n number of comments from that subreddit
    '''
    comments_object = r.get_subreddit(subreddit).get_comments(limit=n)
    comments = []
    for comment in praw.helpers.flatten_tree(comments_object): #iterate through all comments in a comment tree (including replies)
        comments.append(str(comment))
    return comments

def get_sentiments(data):
    '''
        Given a list of strings which represent post titles or comments, return an average sentiment value of the subreddit
    '''
    sentiments = []
    for entry in data:
        sentiment_value = sentiment(entry)
        if abs(sentiment_value[0]) < 0.1:
            continue #don't include this value because it means sentiment analysis wasn't significant
        else:
            sentiments.append(sentiment_value[0])
    return mean(sentiments)

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

subreddits = ['aww','nba','science','nottheonion','worldnews']
#print order_subreddit(subreddits)

print get_sentiments(get_comments('aww',100))
print get_sentiments(get_comments('nba',100))
print get_sentiments(get_comments('science',100))
print get_sentiments(get_comments('nottheonion',100))
print get_sentiments(get_comments('worldnews',100))
