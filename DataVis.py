'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("TwitterData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#
# while True:
#     word = TextBlob(input(""))
#
#     print(word.polarity)
#
# # Continue your program below!

# # Textblob sample:

combinedtweets = ""

for tweet in tweetData:
    combinedtweets += tweet["text"]

tweetblob = TextBlob(combinedtweets)

wordsToFilter = []
filteredDict = dict()

for word in tweetblob.words:

    if len(word) < 3:
        continue
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:
        continue
    if len(word) < 5 and word.upper() != word:
        continue

    filteredDict[word.lower()] = tweetblob.word_counts[word.lower()]

wordcloud = WordCloud().generate_from_frequencies(filteredDict)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("on")
plt.show()

# pList = []
#
# for tweet in tweetData:
#     tb = TextBlob(tweet["text"])
#     pList.append(tb.polarity)
# #
# # print(pList)
#
# plt.hist(pList, bins = [-1.1, -.75, -.5, -.25, 0, .25, .5, .75, 1.1])
# plt.xlabel('polarity')
# plt.ylabel('# of words')
# plt.title('Polarity of Words :)')
# plt.axis([-1, 1, 0, 100])
# plt.grid(True) #boolean
# plt.show()
