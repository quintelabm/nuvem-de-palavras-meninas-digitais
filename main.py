# Tutorial from https://www.datacamp.com/tutorial/wordcloud-python

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

text = 'Maria Luiza Anna Julia Barbara Liamara Priscila Thais Cecilia Josiane Ada '

md_mask = np.array(Image.open("img/logo_bw.png"))
#print(md_mask)

def transform_format(val):
    if val == 0:
        return 255
    else:
        return 1
    
# Transform your mask into a new one that will work with the function:
transformed_mask = np.ndarray((md_mask.shape[0],md_mask.shape[1]), np.int32)
#print(transformed_mask)
for i in range(len(md_mask)):
    transformed_mask[i] = list(map(transform_format, transformed_mask[i]))

#print(transformed_mask)

# Create and generate a word cloud image:
wordcloud = WordCloud(mask=transformed_mask,contour_width=3,                    
                      contour_color='firebrick',background_color="white",max_font_size=50, max_words=1000).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcount.png")