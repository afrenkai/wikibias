from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from fetch import fetch_article
from consts import Sentiment
import json

sia = SentimentIntensityAnalyzer()

def analyze_wikipedia_article(text: str):
    paragraphs = text.split('\n\n')
    
    results = {}
    
    for paragraph in paragraphs:
        sentiment = sia.polarity_scores(paragraph)
        if sentiment["compound"] >= Sentiment.pos_threshold or sentiment["compound"] <= Sentiment.neg_threshold:  
            results[paragraph] = sentiment["compound"]

    return json.dumps(results, sort_keys=False)
    
print(analyze_wikipedia_article(fetch_article("Donald Trump")))