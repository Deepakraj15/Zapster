from flask import Flask,render_template,request

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
    print(negative,neutral,positive)
    return render_template('index.html',data=[negative,neutral,positive])

