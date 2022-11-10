from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

import process

# loading model and tokenizer

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# sentiment analysis

encoded_tweets = tokenizer(process.preprocess(), return_tensors='pt')
output = model(**encoded_tweets)
scores = output[0][0].detach().numpy()
scores = softmax(scores)
for i in range(len(scores)):
    l = labels[i]
    s = scores[i]
    print(l, s)
