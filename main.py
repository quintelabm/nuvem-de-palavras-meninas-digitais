# Tutorial from https://www.datacamp.com/tutorial/wordcloud-python

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

text = 'Maria Luiza Anna Julia Barbara Liamara Priscila Thais Cecilia Josiane Ada '

# Create and generate a word cloud image:
wordcloud = WordCloud(background_color="white",max_font_size=50, max_words=100).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcount.png")