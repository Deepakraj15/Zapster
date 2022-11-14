import pandas as pd


def preprocess():
    df = pd.read_csv('./Backend/result.csv')
    results = []

    for tweet in df['text']:
        tweet_words = []
        for word in tweet.split(' '):
            if (('@' in word) or ('#' in word )or ('http' in word) or ('https' in word) and len(word) > 1):
                word = ""

            elif (len(word) <= 1):
                continue
            tweet_words.append(word)
            while ('' in tweet_words):
                tweet_words.remove('')
        results.append(tweet_words)
    for result in results:
        output = ' '.join(result)
    return output
