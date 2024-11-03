from nltk.sentiment.vader import SentimentIntensityAnalyzer
from psycopg.generators import fetch

from fetch import fetch_article
sia = SentimentIntensityAnalyzer()

def analyze_wikipedia_article(title, positive_threshold=0.5, negative_threshold=-0.5):
    page = fetch_article(title)

    paragraphs = page.text.split("\n\n")

    analysis_results = []
    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip():
            sentiment = sia.polarity_scores(paragraph)
            analysis_results.append({
                "paragraph": paragraph,
                "sentiment": sentiment,
                "highlight": sentiment['compound'] >= positive_threshold or sentiment['compound'] <= negative_threshold
            })

    for result in analysis_results:
        if result["highlight"]:
            sentiment_type = "Positive" if result["sentiment"]["compound"] >= positive_threshold else "Negative"
            print(f"\n** {sentiment_type} Paragraph Detected **\n")
            print(result["paragraph"])
            print(f"Sentiment Score: {result['sentiment']['compound']}")
        else:
            print("\nNeutral Paragraph:\n")
            print(result["paragraph"])
            print(f"Sentiment Score: {result['sentiment']['compound']}")
