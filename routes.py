from flask import Blueprint, request, jsonify
from sentiment import analyze_wikipedia_article

bp = Blueprint('routes', __name__)

@bp.route('/sentiment', methods = ['GET'])
def sentiment():
    title = request.args.get('title')

    if not title:
        return jsonify({'error': 'title is required'}), 400

    res = analyze_wikipedia_article(title)
    return jsonify(res)
