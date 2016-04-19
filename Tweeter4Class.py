from pattern.web import *
from pattern.en import *
from math import *
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from keys import api_username, api_key
tls.set_credentials_file(api_username, api_key)


def search_and_measure_sentiment(inputs):
    """ This function takes in a list of strings as input and returns
    a certain amount of the most recent tweets that are linked to the inputed
    search terms. For each collection of tweets, the function calculates the
    average polarity and subjectivity and returns these two values in the form
    of two tupled lists. 
    ********This is a significant change from my MP3 code because
    it combines the search and measure_sentiment functions into one to easily
    make the function capable of taking in any number of inputs and calculates
    the average subjectivity in addition to the average polarity.
    """
    t = Twitter()
    i = None
    team_polarities = []
    team_sentiments = []
    index = 0
    for x in inputs: 
        sum_pol = [0]*(len(inputs))
        sum_sent = [0]*(len(inputs))
        total_tweets = 0
        polarity_average = [0]*(len(inputs))
        sentiment_average = [0]*(len(inputs))
        for tweet in t.search(x, start = i, count = 5):
            # print tweet.text
            total_tweets += 1
            polarity = sentiment(tweet.text.encode("utf-8")) 
            # if polarity[1] > .5:
            #   pass
            # else:
            sum_pol[index] += polarity[0]
            sum_sent[index] += polarity[1]
            i = tweet.id
        polarity_average[index] = sum_pol[index]/total_tweets
        # print polarity_average[index]
        sentiment_average[index] = sum_sent[index]/total_tweets
        team_polarities.append(polarity_average[index])
        team_sentiments.append(sentiment_average[index])
        # index assignment for next input
        index += 1 

    return team_polarities, team_sentiments
    # print team_polarities, team_sentiments

def plot(inputs):
    """This function takes in a list of strings as input, calls the 
    search_and_measure_sentiment function with this input, and 
    plots the average polarity and subjectivity of each search term
    on a double bar, interactive graph using the Plotly API. This 
    function is intended to be used as a tool that visualizes the 
    predictions of sports tournaments (or other competitions) based 
    on current twitter opinions and also visualizes the validity of
    the predictions using the subjectivity scales.
    ***** This is a significant upgrade from MP3 that used MatPlotLib
    to create a static graph of the polarity of the search terms without 
    comparing the validity of the predictions using subjectivity values.
    """
    polarities = search_and_measure_sentiment(inputs)

    trace1 = go.Bar(
        x=inputs,
        y=polarities[0],
        name='Average Polarity (-1.0 to +1.0)',
        marker=dict(
            color='rgb(55, 83, 109)'
        )
    )
    trace2 = go.Bar(
        x=inputs,
        y = polarities[1],
        name='Average Subjectivity (0.0 to 1.0)',
        marker=dict(
            color='rgb(26, 118, 255)'
        )
    )
    data = [trace1, trace2]
    layout = go.Layout(
        title='Winner Predictions based on Public Opinion',
        xaxis=dict(
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        yaxis=dict(
            title='Sentiment Scale',
            titlefont=dict(
                size=16,
                color='rgb(107, 107, 107)'
            ),
            tickfont=dict(
                size=14,
                color='rgb(107, 107, 107)'
            )
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0.0
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='winner_predictions.html')

if __name__ == "__main__":
    # example plot of NBA Playoff predictions and how accurate they might be (based
    # on average subjectivity of tweets for each team)
    plot(["Clippers", "Spurs", "Heat", "Cavaliers", "Thunder", "Warriors", "Hawks"])