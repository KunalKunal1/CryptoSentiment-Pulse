import pytest
from src.nlp_engine import analyze_sentiment

def test_sentiment_positive():
    text = "Bitcoin is hitting an all time high, amazing!"
    score, label, _ = analyze_sentiment(text)
    assert score > 0
    assert "Positive" in label

def test_sentiment_negative():
    text = "The market crashed terribly today."
    score, label, _ = analyze_sentiment(text)
    assert score < 0
    assert "Negative" in label