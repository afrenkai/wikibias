import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fetch import fetch_article
from consts import Sentiment, Keys, JSON

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str):
    paragraphs = text.split('\n\n')
    
    results = {JSON.sentiment_key: []}
    total_sentiment = 0
    
    for paragraph in paragraphs:
        sentiment = sia.polarity_scores(paragraph)
        sentiment_score = sentiment[Sentiment.sentiment_key] 
        confidence = abs(sentiment_score) 
        
        if sentiment_score >= Sentiment.pos_threshold:
            sentiment_type = JSON.type_positive_value
        elif sentiment_score <= Sentiment.neg_threshold:
            sentiment_type = JSON.type_negative_value
        else:
            continue 

        results[JSON.sentiment_key].append({
            JSON.text_key: paragraph,
            JSON.confidence_key: confidence,
            JSON.type_key: sentiment_type
        })
        
        total_sentiment += sentiment_score
        
    # overall_sentiment = total_sentiment / len(paragraphs) if paragraphs else 0
    
    # results[JSON.sentiment_key] = overall_sentiment
    
    return json.dumps(results, sort_keys=False, indent=2)

print(analyze_sentiment(fetch_article("Donald Trump")))
