import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tags = pd.read_pickle('tags_200000.pkl')




tag_string = ''
for tag in tags_for_word_cloud:
    tag_string += tag['count']*(tag['name'] + ' ')
tag_string


wc = WordCloud(width = 300, height = 300).generate(tag_string)

# Remove the axis and display the data as image
plt.axis("off")
plt.imshow(wc)

# plt.show()