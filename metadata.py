# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:10:04 2021

@author: Satish Narasimhan
"""
import credentials as c
import tweepy
import pandas as pd
import numpy as np

def config():
    #OAuth object handles the keys
    auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
    auth.set_access_token(c.access_key, c.access_secret)
  
    # Calling api for authentication with keys provided
    api = tweepy.API(auth)
    return api

def getTweets(handle):
    # Instantiate an extractor object which will first authenticate and then extract tweets 
    extractor = config()
    
    # tweet count limit = 200
    # Use api object to obtain tweets for the handle
    tweets = extractor.user_timeline(screen_name=handle, count = 200)
    return tweets
        
def recentTweets(handle):
    
    tweets = getTweets(handle)    
    print("Number of tweets extracted: {}.\n".format(len(tweets)))
    
    print("5 recent tweets:\n")
    for tweet in tweets[:5]:
        print(tweet.text)
        print()

def metadata(handle):
    tweets = getTweets(handle)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
      
    data['len(char)']  = np.array([len(tweet.text) for tweet in tweets])
    data['Id']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    
    return data
 
def metadataPrint(handle):
    data = metadata(handle)
    print(data.head(5))
     
def metadataStats(handle):
    data = metadata(handle)
    
    # Extract some basic statistical info from the tweets viz.
    # Mean length of tweets, Avg. number of tweets, Max. likes, Max. retweets 
    mean = np.mean(data['len(char)'])
    print("The mean length of tweets: {0:.2f}".format(mean))
    
    # Average number of tweets per day (for the tweets extracted)
    nt = len(data['Tweets'])
    maxi = max(data['Date'])
    mini = min(data['Date'])
    diff = abs(maxi - mini).days
    avg = nt / diff
    print("The average no. of tweets per day: {0:.2f}".format(avg))

    
    fav_max = np.max(data['Likes'])
    rt_max  = np.max(data['RTs'])
    
    fav = data[data.Likes == fav_max].index[0]
    rt  = data[data.RTs == rt_max].index[0]
    
    # Max favourites:
    print("The tweet with most likes is: \n{}".format(data['Tweets'][fav]))
    print("Number of likes: {}".format(fav_max))
    print("{} characters.\n".format(data['len(char)'][fav]))
    
    # Max Retweets:
    print("The tweet with most retweets is: \n{}".format(data['Tweets'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len(char)'][rt]))
    
    if (data['Tweets'][fav] == data['Tweets'][rt]):
        print("The tweet with the maximum likes is the one which has been retweeted the most")
        
def timeSeries(handle):
    data = metadata(handle)
    
    # We create time series for the tweets:
    tlen = pd.Series(data=data['len(char)'].values, index=data['Date'])
    
    # Lengths of tweets plotted against time:
    tlen.plot(figsize=(16,4), color='r');
    
def likes_vs_retweets(handle):
    data = metadata(handle)
    
    # Number of likes and retweets plotted against time:
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])
    
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True);
    
def mediaSource(handle):
    data = metadata(handle)
    sources = []
    percent = np.zeros(len(sources))

    for source in data['Source']:
        for index in range(len(sources)):
            if source == sources[index]:
                percent[index] += 1
                pass

    percent /= 100

    # Pie chart:
    pie_chart = pd.Series(percent, index=sources, name='Sources')
    pie_chart.plot.pie(fontsize=11, autopct='%.2f', figsize=(6, 6));
    
