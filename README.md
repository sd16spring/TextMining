# TextMining

## Overview
As a player of Magic: the Gathering, I was interested in analyzing the community's opinions of different popular decks. In particular, one very recently discovered deck (known as "Eldrazi") has been the subject of some controversydue to its sudden popularity and power level. I did aggregated sentiment analysis of comments on posts about particular decks, then compared them to comments about the Eldrazi deck. 

## Implementation
###textmining.py
The first half of my code uses the Praw package to grab the most recent 100 posts in a given Magic-related subreddit, then filter those posts into a list if the title includes mention of a particular deck. The entire comment tree is then flattened into a list of strings, which is pickled and written to a file. One possible design decision that I decided not to pursue would have been to do some sorting of original comments and replies to comments. However, it would have been a difficult distinction to make with regards to the exact relevance of certain levels of comments, so I decided to just use all of them. 
###analysis.py
The second module looks for a file with comments about a given deck, then unpickles it to the original list. Because sentiment analysis on particularly large strings tends to be unreliable, I split each comment into individual sentences. I then did some basic filtering to remove strings without words by checking if they contained letters. Since Indico doesn't care about non-alphabetic characters, I didn't bother to clean up the strings beyond that. Finally, I averaged the sentiments of each sentence in each comment, then averaged the comments.

## Results
I scraped comments relating to four different classic Magic decks to use as a benchmark, then from posts about the Eldrazi deck. 
```
Average sentiment about Miracles: 0.468114394113
Average sentiment about Shardless: 0.432950678235
Average sentiment about Storm: 0.458152381391
Average sentiment about Delver: 0.491417681612
Average sentiment about Eldrazi: 0.422164683039
```
The number for Shardless is somewhat unreliable, since I only found one post, but the rest of the decks hover around neutral sentiment (slightly below neutral, but Magic players tend to be a salty bunch). As I had hoped, comments about the Eldrazi deck were noticeably, if not substantially, more negative on average than comments about the other decks.

## Reflection
Exchanging data with external sources worked well. The process of using the Reddit API was pretty seamless, although the restriction of only making one API call every two seconds was somewhat inhibiting, and the Indico API was even easier to implement. Since the majority of data processing was done with simple generators and filtering, I did the majority of unit testing in the command line with the APIs. The biggest challenge was in dealing with empty (deleted?) comments, which I eventually sorted out with exception handling and assigned a neutral sentiment value so as to not affect the averages. On the whole this project was definitely scoped according to the amount of time I was able to allocate to it, so it was less ambitious than it could have been. If I were to do it again I would have done more things with the data, like filtering the posts into a larger range of categories and more carefully analyzing comments in relation to each other.
