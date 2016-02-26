import indicoio
import pickle
from constants import API_KEY

def analyze_comments(archetype):
    """Analyze a list of comments and print the average sentiment, according to Indico."""

	f = open('{}_comments.pickle'.format(archetype.lower()), 'r')
    stored_comments = pickle.load(f)

    indicoio.config.api_key = API_KEY #configure indico API

    def get_avg_sentiment(comment):
		comment_sentences = filter(lambda string: any(c.isalpha() for c in string), comment.split('. '))
		sentiments = [indicoio.sentiment(comment) for comment in comment_sentences]
		try:
			avg_sentiment = sum(sentiments) / len(sentiments)
		except:
			return 0.5
		return avg_sentiment

    all_sentiments = [get_avg_sentiment(comment) for comment in stored_comments]
    all_average = sum(all_sentiments) / len(all_sentiments)
    print 'Average sentiment about {}: '.format(archetype) + str(all_average)

decks = ['Miracles', 'Shardless', 'Storm', 'Delver']

if __name__ == '__main__':
	for deck in decks:
		analyze_comments(deck)
	analyze_comments('Eldrazi')
