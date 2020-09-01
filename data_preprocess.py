
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from  nltk.stem import SnowballStemmer
import string





### CLEANING THE CORPUS

def cleantext(data,column):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    stem=str(input("Enter what type of stemmer you need to apply to text:")).strip()
    
    if stem =="PorterStemmer":
        stemmer = PorterStemmer()
        tweets_clean = []
        for i in data[column]:
            i = str(i).lower()
            i = re.sub('\[.*?\]', '', i)
            i = re.sub('https?://\S+|www\.\S+', '', i)
            i = re.sub('<.*?>+', '', i)
            i = re.sub('[%s]' % re.escape(string.punctuation), '', i)
            i = re.sub('\n', '', i)
            i = re.sub('\w*\d\w*', '', i)
            i = re.sub(r'\$\w*', '', i)
            # remove old style retweet text "RT"
            i = re.sub(r'^RT[\s]+', '', i)
            # remove hyperlinks
            i = re.sub(r'https?:\/\/.*[\r\n]*', '', i)
            # remove hashtags
            # only removing the hash # sign from the word
            i = re.sub(r'[#@]+', '', i)
    
    
            tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                                       reduce_len=True)
            tweet_tokens = tokenizer.tokenize(i)
        
            
            
            text = [stemmer.stem(word) for word in tweet_tokens if word not in set(stopwords.words('english'))]
            text = ' '.join(text)
            tweets_clean.append(text)
    

    
        return tweets_clean
    
    
    elif stem =="SnowballStemmer":
        stemmer = SnowballStemmer("english")
        tweets_clean = []
        for i in data[column]:
            i = str(i).lower()
            i = re.sub('\[.*?\]', '', i)
            i = re.sub('https?://\S+|www\.\S+', '', i)
            i = re.sub('<.*?>+', '', i)
            i = re.sub('[%s]' % re.escape(string.punctuation), '', i)
            i = re.sub('\n', '', i)
            i = re.sub('\w*\d\w*', '', i)
            i = re.sub(r'\$\w*', '', i)
            # remove old style retweet text "RT"
            i = re.sub(r'^RT[\s]+', '', i)
            # remove hyperlinks
            i = re.sub(r'https?:\/\/.*[\r\n]*', '', i)
            # remove hashtags
            # only removing the hash # sign from the word
            i = re.sub(r'[#@]+', '', i)
    
    
            tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                                       reduce_len=True)
            tweet_tokens = tokenizer.tokenize(i)
        
            
            
            text = [stemmer.stem(word) for word in tweet_tokens if word not in set(stopwords.words('english'))]
            text = ' '.join(text)
            tweets_clean.append(text)
    

    
        return tweets_clean
    
    elif stem =="WordNetLemmatizer":
        stemmer = WordNetLemmatizer()
        tweets_clean = []
        for i in data[column]:
            i = str(i).lower()
            i = re.sub('\[.*?\]', '', i)
            i = re.sub('https?://\S+|www\.\S+', '', i)
            i = re.sub('<.*?>+', '', i)
            i = re.sub('[%s]' % re.escape(string.punctuation), '', i)
            i = re.sub('\n', '', i)
            i = re.sub('\w*\d\w*', '', i)
            i = re.sub(r'\$\w*', '', i)
            # remove old style retweet text "RT"
            i = re.sub(r'^RT[\s]+', '', i)
            # remove hyperlinks
            i = re.sub(r'https?:\/\/.*[\r\n]*', '', i)
            # remove hashtags
            # only removing the hash # sign from the word
            i = re.sub(r'[#@]+', '', i)
    
    
            tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                                       reduce_len=True)
            tweet_tokens = tokenizer.tokenize(i)
        
            
            
            text = [stemmer.lemmatize(word) for word in tweet_tokens if word not in set(stopwords.words('english'))]
            text = ' '.join(text)
            tweets_clean.append(text)
    

    
        return tweets_clean
    
    else:
        print("Your desired stemmer is not in the dictionary:PorterStemmer,WordNetLemmatizer,SnowballStemmer")
        
    