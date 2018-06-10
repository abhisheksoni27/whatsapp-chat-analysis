import re
import matplotlib.pyplot as plt
import numpy as np
import indicoio
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentient_analyzer = SentimentIntensityAnalyzer()

indicoio.config.api_key = '26837191c44dd6a7560a688e3307920d'


def cleanText(filename, ownerName="Abhishek Soni"):

    chat = open(filename)
    personName = filename.split('.')[0]
    chatText = chat.read()
    pattern = "(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s)(\w+)(\s\w+)?(:)"

    regex = re.compile(pattern, flags=re.M)

    clean = regex.sub("", chatText)
    lines = []
    for line in clean.splitlines():
        lines.append(line.strip())

    return lines


linesList = cleanText('innaya.txt')
neutral, negative, positive = 0, 0, 0

for sentence in linesList[0:1]:
    scores = sentient_analyzer.polarity_scores(sentence)
    scores.pop('compound', None)
    maxAttribute = max(scores, key=lambda k: scores[k])
    if maxAttribute == "neu":
        neutral += 1
    elif maxAttribute == "neg":
        negative += 1
    else:
        positive += 1

total = neutral + negative + positive
print("Negative: {0}% | Neutral: {1}% | Positive: {2}%".format(
    negative*100/total, neutral*100/total, positive*100/total))
