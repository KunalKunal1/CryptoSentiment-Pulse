from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
    """
    Analyzes text and returns a sentiment score (-1.0 to 1.0)
    and a label.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        label = "Positive 🚀"
        color = "green"
    elif polarity < -0.1:
        label = "Negative 📉"
        color = "red"
    else:
        label = "Neutral 😐"
        color = "gray"
        
    return polarity, label, color

def process_news_sentiment(news_list):
    """
    Takes a list of headlines and returns a DataFrame with analysis.
    """
    results = []
    for news in news_list:
        score, label, _ = analyze_sentiment(news)
        results.append({'Headline': news, 'Score': score, 'Sentiment': label})
    
    return pd.DataFrame(results)