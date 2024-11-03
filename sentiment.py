from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from fetch import fetch_article
from consts import Sentiment, Keys
import json

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    paragraphs = text.split('\n\n')
    
    results = {}
    results[Keys.sentiment] = 0
    total_sentiment = 0
    
    for paragraph in paragraphs:
        sentiment = sia.polarity_scores(paragraph)
        total_sentiment += sentiment[Sentiment.sentiment_key]

        if sentiment[Sentiment.sentiment_key] >= Sentiment.pos_threshold or sentiment[Sentiment.sentiment_key] <= Sentiment.neg_threshold:  
            results[paragraph] = sentiment[Sentiment.sentiment_key]

    total_sentiment /= len(paragraphs)
    results[Keys.sentiment] = total_sentiment

    return json.dumps(results, sort_keys=False)
    
# print(analyze_sentiment(fetch_article("Donald Trump")))