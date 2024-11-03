from flask import Flask, jsonify, request
from sentiment import analyze_wikipedia_article
from consts import Endpoints

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def sentiment():
    title = request.args.get(Endpoints.API)

    if not title:
        return jsonify({'error': 'title is required'}), 400

    res = analyze_wikipedia_article(title)
    return jsonify(res)
