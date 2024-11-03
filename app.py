from flask import Flask, jsonify, request
from fetch import fetch_article
from sentiment import analyze_wikipedia_article
from consts import Endpoints, Keys

app = Flask(__name__)

@app.route(Endpoints.API)
def analyze_article():
    title = request.args.get(Keys.title)

    if not title:
        return jsonify({'error': 'title is required'}), 400

    article = fetch_article(title)
    print(f"Fetched article")
    #analyzed = analyze_wikipedia_article(article)

    return article

if __name__ == "__main__":
    app.run()   