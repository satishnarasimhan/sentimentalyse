# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:44:59 2021

@author: Satish Narasimhan
"""
import metadata as m
import sentimentalyse as s
import hashlyse as h

if __name__ == '__main__':
  
    # The twitter handle of the user whose tweets are to be extracted
    #twitter_handle = "SubhadipNandy16"
        
    #m.getTweets(twitter_handle) 
    #m.recentTweets(twitter_handle)
    #m.metadataPrint(twitter_handle)
    #m.metadataStats(twitter_handle)
    #m.timeSeries(twitter_handle)
    #m.likes_vs_retweets(twitter_handle)
    #m.mediaSource(twitter_handle)
    #s.presentation(twitter_handle)
    
    # The hashtag that you need to retrieve the associated tweets
    hashtag = ""
    num = 200
    date_since = "2021-05-15" #2021-05-15
    
    h.get_tweets_by_hashtag(hashtag, date_since, num)
    s.present_downloaded_csv(hashtag)
    