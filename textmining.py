import praw
import pickle
from constants import API_KEY

def write_comments(subreddit, archetype):
	r = praw.Reddit('Text analysis on r/{}'.format(subreddit))
	subreddit = r.get_subreddit(subreddit)
	posts = subreddit.get_hot(limit=100)
	
	deck_posts = []
	print 'Posts about {}:'.format(archetype)
	
	for post in posts:
		if archetype.lower() in str(post).lower():
			print str(post).lstrip('0123456789').lstrip(': ')
			deck_posts.append(post)
	
	all_comments = []
	
	for post in deck_posts:
		for comment in praw.helpers.flatten_tree(post.comments):
			if not hasattr(comment, 'body'):
				continue
			all_comments.append(comment.body)

	f = open('{}_comments.pickle'.format(archetype.lower()), 'w')
	pickle.dump(all_comments, f)
	f.close()

decks = ['Miracles', 'Shardless', 'Storm', 'Delver']
if __name__ == '__main__':
	for deck in decks:
		write_comments('mtglegacy', deck)
	write_comments('modernmagic', 'Eldrazi')
