import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
import AdditionalWords
os.chdir(sys.path[0])

text = open('jobs_description.txt', mode='r', encoding='utf-8').read()
stopwords = AdditionalWords.additionalStopWords + list(STOPWORDS)

word_cloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    height=600,
    width=800
)

word_cloud.generate(text)

word_cloud.to_file('wordcloud_jobs_description.png')