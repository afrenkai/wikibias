from flask import Flask, jsonify, request
from fetch import fetch_article
from sentiment import analyze_sentiment
from bias import analyze_bias
from consts import Endpoints, Keys

app = Flask(__name__)

@app.route(Endpoints.api)
def analyze_article():
    title = request.args.get(Keys.title)

    if not title:
        return jsonify({'error': 'title is required'}), 400

    article = fetch_article(title)
    print(f"Fetched article")
    sentiment = analyze_sentiment(article)

    return sentiment

if __name__ == "__main__":
    app.run()   