def predict_sentiment(text: str) -> str:
    """
    Predicts the sentiment of a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: Sentiment label - "positive", "negative", or "neutral".
    """
    if not text:
        return "neutral"
    
    text = text.lower()
    
    if "happy" in text or "good" in text:
        return "positive"
    if "sad" in text or "bad" in text:
        return "negative"
    
    return "neutral"
