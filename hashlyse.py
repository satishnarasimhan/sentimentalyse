# -*- coding: utf-8 -*-
"""
Created on Sat May 22 13:07:05 2021

@author: Satish Narasimhan
"""
import metadata as m
import tweepy
import pandas as pd

# function to display data of each tweet
def print_tweets_from_hashtag(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Description:{ith_tweet[1]}")
    print(f"Location:{ith_tweet[2]}")
    print(f"Following Count:{ith_tweet[3]}")
    print(f"Follower Count:{ith_tweet[4]}")
    print(f"Total Tweets:{ith_tweet[5]}")
    print(f"Retweet Count:{ith_tweet[6]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")

def get_tweets_by_hashtag(hashtag, date_since, num):
    # Instantiate an extractor object which will first authenticate and then extract tweets 
    extractor = m.config()
    
    # tweet count limit = 200
    # Use Cursor() to obtain tweets for the handle
    #tweets = extractor.user_timeline(screen_name=handle, count = 200)
    tweets = tweepy.Cursor(extractor.search
                              ,q = hashtag
                              ,lang = "en"
                              ,tweet_mode = 'extended').items(num)
    
    list_of_tweets = [tweet for tweet in tweets]
    #print (list_of_tweets)
    
    # Creating DataFrame using pandas
    data_ht = pd.DataFrame(columns=['username', 'description', 'location', 'following',
                               'followers', 'totaltweets', 'retweetcount', 'Tweets', 'hashtags'])
    # Maintain count of tweets
    i = 1  
      
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_of_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
          
        # Retweets can be distinguished by a retweeted_status attribute,
        # in case it is an invalid reference, except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text  
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
          
        # Append all the extracted info into the hashtag dataframe
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        data_ht.loc[len(data_ht)] = ith_tweet
        
        # Print tweets
        # print_tweets_from_hashtag(i, ith_tweet)
        i += 1
    
    # Save the tweets generated for the hashtag 
    path = ''
    fileName = hashtag + '.csv'
    csvFile = (path+fileName) 

    data_ht.to_csv(csvFile)

    print("File generated successfully")

            
    
    