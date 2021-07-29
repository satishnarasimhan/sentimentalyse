# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:16:17 2021

@author: Satish Narasimhan
"""

import metadata as m
import re
import numpy as np
from textblob import TextBlob
import pandas as pd

def cleanup(tweet):
        
    '''
    Use regex to clean up the text in the tweet of links, special characters
    This is essential as each tweet will need to be analysed using the TextBlob
    Each tweet will then be associated with a polarity
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyse(tweet):
    '''
    Use TextBlob to assign a polarity to a tweet
    '''
    analysis = TextBlob(cleanup(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def processing(handle):
    
    data = m.metadata(handle)
    # Create a column with the result of the analysis
    data['Sentiment'] = np.array([ analyse(tweet) for tweet in data['Tweets'] ])
    
    return data
     
def presentation(handle):
    data = processing(handle)
    
    # Print the updated dataframe with the new column showing the sentiment
    print(data.head(5))
    
    # Categorisation of the tweets as positive, negative and neutral

    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] < 0]
    
    print("Percentage of positive tweets: {0:.2f}%".format(len(pos_tweets)*100/len(data['Tweets'])))
    print("Percentage of neutral tweets: {0:.2f}%".format(len(neu_tweets)*100/len(data['Tweets'])))
    print("Percentage of negative tweets: {0:.2f}%".format(len(neg_tweets)*100/len(data['Tweets'])))
    
    # Save metadata to a CSV file
    path = ''
    filename = handle + '.csv'
    csvfile = (path+filename) 
    
    data.to_csv(csvfile)
    
    print("File generated successfully")
    
def process_downloaded_csv(hashtag):
    # Creating DataFrame using pandas
    data_ht = pd.DataFrame(columns=['username', 'description', 'location', 'following',
                               'followers', 'totaltweets', 'retweetcount', 'Tweets', 'hashtags'])
    
    path = ''
    filename = hashtag + '.csv'
    csvfile = (path+filename)  
    
    # Read the CSV file
    data_ht = pd.read_csv(csvfile)
   
    # Create a column with the result of the analysis
    data_ht['Sentiment'] = np.array([ analyse(tweet) for tweet in data_ht['Tweets'] ])
    
    return data_ht

def present_downloaded_csv(hashtag):
    data = process_downloaded_csv(hashtag)
    
    # Print the updated dataframe with the new column showing the sentiment
    # print(data.head(5))
    
    # Categorisation of the tweets as positive, negative and neutral

    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['Sentiment'][index] < 0]
    
    print("Analysis for hashtag: #" + hashtag)
    print("Percentage of positive tweets: {0:.2f}%".format(len(pos_tweets)*100/len(data['Tweets'])))
    print("Percentage of neutral tweets: {0:.2f}%".format(len(neu_tweets)*100/len(data['Tweets'])))
    print("Percentage of negative tweets: {0:.2f}%".format(len(neg_tweets)*100/len(data['Tweets'])))
    

    
    
    


    
