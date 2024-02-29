import streamlit as st
import dill
from sklearn.neighbors import NearestNeighbors
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from musaic1 import fetch_similar
from plotting import make_word_cloud
#from plotting import plot_wells

def app():
    
    st.title('Musaic')
    
    track_name = st.text_input('track_name')
    artist_name = st.text_input('artist_name')
    ###display similar tracks
    similar = fetch_similar(track_name, artist_name)
    st.dataframe(similar)
    
    index = similar.index[(similar['track_name']==track_name) & (similar['artist_name']==artist_name)].tolist()[0]
       
    wc = make_word_cloud(int(index))
    # Plot the WordCloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    
    st.pyplot(fig)

if __name__ == '__main__':
    app()