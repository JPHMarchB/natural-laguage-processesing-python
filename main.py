from textblob import TextBlob
from newspaper import Article
from nltk.sentiment import SentimentIntensityAnalyzer


URL ='https://en.wikipedia.org/wiki/ISDN'

article = Article(URL)

article.download()
article.parse()
article.nlp()

TEXT = article.summary
# print(TEXT)

# Using Vader/NLTK
SIA = SentimentIntensityAnalyzer()
sentiment_scores = SIA.polarity_scores(TEXT)

# Using TextBlob
blob = TextBlob(TEXT)
sentiment = blob.sentiment.polarity # -1 to 1

print(sentiment)
print("Sentiment Scores:", sentiment_scores)