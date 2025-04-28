from model import predict_sentiment

def test_predict_positive():
    assert predict_sentiment("I am happy today") == "positive"
def test_predict_negative():
    assert predict_sentiment("I feel sad") == "negative"
# test de commentaire test_model
def test_predict_neutral():
    assert predict_sentiment("The sky is blue") == "neutral"