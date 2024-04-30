from textblob import TextBlob
from newspaper import Article


URL ='https://en.wikipedia.org/wiki/ISDN'

article = Article(URL)

article.download()
article.parse()
article.nlp()

TEXT = article.text
print(TEXT)