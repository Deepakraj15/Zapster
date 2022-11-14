from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

from Backend import process

def classify():
        
    # loading model and tokenizer

    roberta = "cardiffnlp/twitter-roberta-base-sentiment"
    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    # sentiment analysis

    encoded_tweets = tokenizer(process.preprocess(), return_tensors='pt')
    output = model(**encoded_tweets)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    returnlist=[]
    for i in range(len(scores)):
        s = scores[i]
        returnlist.append(s)
    return returnlist