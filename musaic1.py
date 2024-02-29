import os
import sys
import pandas as pd
import dill
from sklearn.neighbors import NearestNeighbors

def fetch_similar(track_name, artist_name):
    
    with open('nn_features_200000.pkd', 'rb') as f:
        features = dill.load(f)
    with open('nn_model_200000.pkd', 'rb') as f:
        nn_just_track_tags = dill.load(f)
    
    tags = pd.read_pickle('tags_200000.pkl')
    
    index = tags.index[(tags['track_name']==track_name) & (tags['artist_name']==artist_name)]
    
    dists, indices = nn_just_track_tags.kneighbors(features[index])
    
    return tags.iloc[indices[0]][['track_name','artist_name','tags_list']]

if __name__ == '__main__':
    track_name = str(sys.argv[1])
    artist_name = str(sys.argv[2])
    print(fetch_similar(track_name, artist_name))