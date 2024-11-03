from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from fetch import fetch_article
sia = SentimentIntensityAnalyzer()

def analyze_wikipedia_article(title, positive_threshold=0.5, negative_threshold=-0.5):
    page = fetch_article(title)
    
    sentences = sent_tokenize(page.text)
    
    analysis_results = []
    sentiment_type = ""
    for sentence in sentences:
        sentiment = sia.polarity_scores(sentence)
        if sentiment['compound'] > 0:
            sentiment_type = 'positive'
        elif sentiment['compound'] < 0:
            sentiment_type = 'negative'
        else:
            sentiment_type = 'neutral'
        analysis_results