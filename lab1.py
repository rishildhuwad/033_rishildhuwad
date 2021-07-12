import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

nltk.download('twitter_samples')
all_positive_tweets=twitter_samples.strings('positive_tweets.json')
all_negative_tweets=twitter_samples.strings('negative_tweets.json')

print('number of positive tweets:',len(all_positive_tweets))
print('number of negative tweets:',len(all_negative_tweets))

print('\ntype of all positive tweets is:',type(all_positive_tweets))
print('\ntype of a tweet entry is:',type(all_negative_tweets[0]))

fig=plt.figure(figsize=(5,5))

labels='ML-BSB-Lec','ML-HAP-Lec','ML-HAP-Lab'
sizes=[40,35,25]
plt.pie(sizes,labels=labels,autopct='%.2f%%',
    shadow=True,startangle=90)
plt.axis('equal')
plt.show()
#2nd pie chart
fig=plt.figure(figsize=(5,5))

labels='Positives','Negative'
sizes=[len(all_positive_tweets),len(all_negative_tweets)]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',
    shadow=True,startangle=90)
plt.axis('equal')
plt.show()
#looking at raw text
print('\033[92m'+all_positive_tweets[random.randint(0,5000)])
print('\033[91m'+all_negative_tweets[random.randint(0,5000)])