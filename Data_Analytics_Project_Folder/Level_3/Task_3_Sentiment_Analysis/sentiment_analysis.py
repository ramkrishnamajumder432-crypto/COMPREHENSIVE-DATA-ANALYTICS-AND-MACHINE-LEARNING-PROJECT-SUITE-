
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob

df = pd.read_csv("3) Sentiment dataset.csv")

df["Text"] = df["Text"].astype(str)

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Predicted_Sentiment"] = df["Text"].apply(get_sentiment)

print(df["Predicted_Sentiment"].value_counts())

plt.figure(figsize=(6,5))
df["Predicted_Sentiment"].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.savefig("sentiment_distribution.png")

text = " ".join(df["Text"])

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("wordcloud.png")

print("Sentiment Analysis completed")
