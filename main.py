# Tutorial from https://www.datacamp.com/tutorial/wordcloud-python

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import cv2

import matplotlib.pyplot as plt

# string com todas as palavras
text = 'MeninasDigitais UFJF MeninasDigitais UFJF MeninasDigitais UFJF MeninasDigitais UFJF Ada Lovelace Sophie Wilson Barbara Liamara Adele \
    Goldberg Anita Borg Annie Easley Carol Shaw Cecilia R. Aragon Dilma Menezes \
    Elizabeth Feinler FeiFei Li Frances Allen Gabriela Ochoa Gracie \
    Hopper Heng Ji Henriette Avram Ida Rhodes Jean Sammet Jeannette \
    Wing Jetty Kleijn Joan Clarke Joy Buolamwini Juliana Freire Katherine \
    Johnson Kathleen Booth Lenore Blum Linnyer Beatrys Margaret Hamilton Maria \
    Volpe Mary Wilkes Kenneth Keller Radia Perlman Steve Shirley \
    Tawanna Dillahunt Timnit Gebru Valéria de Paiva Wei Wang Yanxi Liu Hedy \
    Lamarr Leanne Pittsford Souza Rika Ciminieri Lynn Conway Danielle \
    Bunten Berry Angelica Ross Karin Breitman Sílvia Amélia Bim Karen da Silva \
    Figueiredo Medeiros Ribeiro Luciana Bolan Frigo Luísa Cecília Thaís Anna \
    Júlia Isadora Josiane Priscila Ada Lovelace Sophie Wilson Barbara Liamara \
    Adele Goldberg Anita Borg Easley Carol Shaw Cecilia R. Aragon Dilma Menezes \
    Elizabeth Feinler Fei-Fei Li Frances Gabriela Ochoa Gracie Hopper Heng Ji \
    Henriette Avram Ida Rhodes Jean Sammet Jeannette Wing Jetty Kleijn Joan Clarke \
    Joy Buolamwini Juliana Freire Katherine Johnson Kathleen Booth Lenore Blum \
    Linnyer Beatrys Margaret Hamilton Volpe Wilkes Kenneth Keller Radia Perlman \
    Steve Shirley Tawanna Dillahunt Timnit Gebru Valéria de Paiva Wei Wang Yanxi \
    Liu Hedy Lamarr Leanne Pittsford Annie Souza Rika Ciminieri Lynn Conway \
    Danielle Bunten Berry Angelica Ross Karin Breitman Sílvia Amélia Bim Karen \
    da Silva Figueiredo Medeiros Ribeiro Luciana Bolan Frigo Luísa Cecília \
    Thaís Anna Júlia Isadora Josiane Priscila Nina daHora Mel Bel Ale Alessandreia \
    Regina Fernanda Lorenza Anna Julia Maria Isa '

#md_mask = np.array(Image.open("img/logo_bw.png"))
img = cv2.imread('img/logo_.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, 0)
copy_img = img.copy()
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(copy_img,contours,-1,(0,0,255),2)
plt.imshow(copy_img)
plt.xticks([])
plt.yticks([])
plt.savefig("teste.png", dpi=600)
#titles = ['original','contours']
#imgs = [img, copy_img]
#for i in range (2):
#    plt.subplot(1,2,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.title(titles[i])
#    plt.imshow(imgs[i])
#plt.savefig("teste.png")

# usa o arquivo gerado 
md_mask = np.array(Image.open("teste.png"))
# print(md_mask)

#def transform_format(val):
#    if val == 0:
#        return 255
#    else:
#        return 1
    
# Transform your mask into a new one that will work with the function:
#transformed_mask = np.ndarray((md_mask.shape[0],md_mask.shape[1]), np.int32)
#print(transformed_mask)
#for i in range(len(md_mask)):
 #   transformed_mask[i] = list(map(transform_format, md_mask[i]))

#print(transformed_mask)

# Create and generate a word cloud image:
wordcloud = WordCloud(mask=md_mask,contour_width=2,                    
                      contour_color='darkred',background_color="black",
                      max_font_size=200, max_words=1000,colormap='Reds').generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcount.png", dpi=600,transparent=True)