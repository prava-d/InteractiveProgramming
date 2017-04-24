"""
Author: Minju
"""

import twitter
import pickle
from pathlib import Path

consumer_key = 'B8wAGC920QYKPl7ivFSLu1bDj'
consumer_secret = 'RPiyW9BpVRldlvXnQuRy2jVosKJxpnbHecYGtL5u5Sx3tllAEB'
access_token = '838329122-pQUHuiSRqQ9MnXer7clyzVgQPSIIKUo56jLbzBmn'
access_token_secret = 'CMWwMm3n62lhx51MIor3SKhd5yLQ0IAfO2IgxOyeq9lAD'


def get_trump_tweets():
    '''Gets Trump tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('trumptwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('trumptwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@realDonaldTrump', 'trumptwitters.pickle',
                        '796130213826621440')


def get_clinton_tweets():
    '''Gets Clinton tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('clintontwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('clintontwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@HillaryClinton', 'clintontwitters.pickle',
                        '796123724479164416')


def get_tim_kaine_tweets():
    '''Gets Tim Kaine tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('kainetwitters.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('kainetwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@SenKaineOffice', 'kainetwitters.pickle',
                        '796162901539164160')


def get_mike_pence():
    '''Gets MIke Pence tweets either from the pickle file or
    if that doesn't exist, the Twitter API'''
    my_file = Path('pencetwitter.pickle')
    if my_file.is_file():
        # Load data from a file (will be part of your data processing script)
        input_file = open('pencetwitters.pickle', 'rb')
        reloaded_copy_of_texts = pickle.load(input_file)
        return reloaded_copy_of_texts
    else:
        retrieve_tweets('@mike_pence', 'pencertwitter.pickle',
                        '822447933899599872')


def retrieve_tweets(name, filename, idnum):
    '''Retrieves tweets from the given screen name that were published
    before the given id from the twitter API and stores them in the
    given file'''

    api = twitter.Api(consumer_key, consumer_secret,
                      access_token,
                      access_token_secret)

    tweets = api.GetUserTimeline(screen_name=name, count=199, max_id=idnum)
    for status in tweets:
        # Print the ID and the date published for each Tweet
        print(status.id)
        print(status.created_at)
    tweets = [s.text for s in tweets]
    # Save data to a file
    f = open(filename, 'wb')
    pickle.dump(tweets, f)
    f.close()
