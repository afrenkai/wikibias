import wikipediaapi
import nltk
from textblob import TextBlob
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
nlp = spacy.load('en_core_web_sm')

def get_wiki_article(title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(title)
    return page.text if page.exists() else None

def get_sentiment(text):
    blob = TextBlob(text)
    vader_scores = sid.polarity_scores(text)
    return {
        'textblob_polarity': blob.sentiment.polarity,
        'vader_neg' : vader_scores['neg'],
        'vader_neu' : vader_scores['neu'],
        'vader_ad' : vader_scores['ad'],
        'vader_compound' : vader_scores['compound']
    }

def entity_sentiment_analysis(text):
    doc = nlp(text)
    entity_sentiments = {}
    for ent in doc.ents:
        entity_text = ent.text



