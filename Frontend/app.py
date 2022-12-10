from flask import Flask,render_template,request
import math
from Backend import main,classification

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',data=[0,0,0])

@app.route("/result",methods=["GET", "POST"])
def result():
    query = request.form['query']
    no_tweets = request.form['no_tweets']
    main.get_tweets(query,int( no_tweets))
    negative,neutral,positive = classification.classify() 
    n1 = math.floor( negative*100)
    n3 = math.floor(positive*100)
    n2 = math.floor(neutral*100)

    print(n1,n2,n3)
    return render_template('index.html',data=[n1,n2,n3])

