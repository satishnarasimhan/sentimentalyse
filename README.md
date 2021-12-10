# sentimentalyse

This project / activity is centered on sentimental analysis of tweets from a handle or discussion around a hashtag on Twitter.
It makes use of Twitter's tweepy and TextBlob Python packages. 
Tweepy helps gather and enumerate the data from the tweets or hashtags.
TextBlob provides a simple API for diving into common natural language processing (NLP) tasks. TextBlob provides the ability to handle part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, word inflection, spell correction, etc. 
In this project, we wil look to use only the sentiment analysis feature to determine the polarity of an opinion i.e. positive, negative or neutral

Collating these, a summarized result is obtained:
Tweets                                                    len(char)       RTs     Sentiment
---------------------------------------------------------------------------------------------
1  Deep space missions will need to generate more...        140  ...       35         1
2  RT @Space_Station: Three visitors are adapting...        139  ...       81         0
3  RT @astro_matthias: Meet the #Astrobee free-fl...        144  ...       50         1
4  Check out the Spanish language translation of ...        140  ...       23        -1
5  Attention reporters: sign up to join a call wi...        140  ...       24         0

--------------------------------------
Summary:
--------------------------------------
Percentage of positive tweets: 46.00%
Percentage of neutral tweets: 45.50%
Percentage of negative tweets: 8.50%
