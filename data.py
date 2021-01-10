
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.sentiment.vader import  SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()


def analyze(sentence):
    """ analyzes a sentence and return the sentiment of it  """
    
    score = analyzer.polarity_scores(sentence)
    if score['compound'] >= 0.05 and score['pos'] - score['neg'] >= 0.1:
        return 'pos'  

    elif score['compound'] <= -0.05 and score['neg'] - score['pos'] >= 0.1:
        return 'neg'

    else:
        return 'neu'