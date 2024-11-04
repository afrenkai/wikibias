from flask import Flask, jsonify, request
from sentiment import analyze_sentiment
from bias import analyze_bias
from consts import Endpoints, Keys
from fetch import fetch_article

app = Flask(__name__)

@app.route(Endpoints.sentiment, methods = ['GET'])
def sentiment():
    title = request.args.get(Keys.title)

    if not title:
        return jsonify({'error': 'title is required'}), 400

    article = fetch_article(title)

    return analyze_sentiment(article)

@app.route(Endpoints.bias, methods = ['GET'])
def bias():
    title = request.args.get(Keys.title)
    
    if not title:
        return jsonify({'error': 'title is required'}), 400
    
    article = fetch_article(title)

    return analyze_bias(article)