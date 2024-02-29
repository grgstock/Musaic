import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def make_word_cloud(index):
    tags = pd.read_pickle('tags_200000.pkl')
    tags_for_word_cloud = tags['tags'][index]
    tag_string = ''
    for tag in tags_for_word_cloud:
        tag_string += tag['count']*(tag['name'] + ' ')
    
    wc = WordCloud(width = 300, height = 300).generate(tag_string)
    return wc
   

# # Remove the axis and display the data as image

# #plt.imshow(wc, interpolation = "bilinear")
# plt.imshow(wc)

# def generate_wordcloud(text):
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot()