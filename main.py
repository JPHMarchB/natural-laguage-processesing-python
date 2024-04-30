import validators
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from newspaper import Article
from tkinter import simpledialog


URL =''

user_url = simpledialog.askstring("Sentiment Finder", "What piece of text would you like analyzed? (Enter a valid URL): ")

valid_data = validators.url(user_url)

if valid_data:
    URL = user_url
else:
    print("URL is invalid, try again!")
    exit()
    

article = Article(URL)

article.download()
article.parse()
article.nlp()

# Variable to check your own text sentiment
with open("my_text.txt", "r") as f :
    text = f.read()

# Article simplifier
TEXT = article.summary

# Using Vader/NLTK
SIA = SentimentIntensityAnalyzer()
sia_scores = SIA.polarity_scores(TEXT) # Replace text w/ TEXT or text variable

# Using TextBlob
blob = TextBlob(TEXT) # Replace text w/ TEXT or text variable
blob_sentiment = blob.sentiment

print("Sentiment Scores:", blob_sentiment)
print("Sentiment Scores:", sia_scores)
