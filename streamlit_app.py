# General Libraries
import pandas as pd

# Model deployment
import streamlit as st

recommender_pool_df = pd.read_csv('spotify_s3g3_rec_pool.csv')
recommender_pool_df = recommender_pool_df.sort_values('track_name')
recommender_pool_df['track_names_with_artist'] = recommender_pool_df['track_name'] + ' by ' + recommender_pool_df['artist_name']
recommender_pool_df = recommender_pool_df.drop_duplicates(subset=['track_names_with_artist'])
options = recommender_pool_df['track_names_with_artist'].to_list()

st.title("OPM Genre & Tracks Recommender")
st.caption("by: Team Swifthrees")
st.image("https://img.freepik.com/free-vector/musical-pentagram-sound-waves-notes-background_1017-33911.jpg?w=1800&t=st=1698402872~exp=1698403472~hmac=5c67bc8bbf36f092b5ffb32a69f8ac13d10d9e76c53dc69b88f87b0aacb7cee5")
st.divider()

choice = st.selectbox(
    "Select Track Name: ", options = options)

if st.button("Submit", type="primary"):
    track = recommender_pool_df.loc[recommender_pool_df['track_names_with_artist'] == choice]
    predicted_genre = track['predicted_genre'].values[0]
    recommended_tracks = recommender_pool_df[(recommender_pool_df['predicted_genre'] == predicted_genre) & (recommender_pool_df['track_names_with_artist'] != choice) & (recommender_pool_df['predicted_genre_proba'] >= 0.5)].sort_values('predicted_genre_proba', ascending=False)
    recommended_tracks_sample = recommended_tracks.sample(n=10)

    st.divider()
    st.markdown("<h5>Predicted Genre: </h5>", unsafe_allow_html = True)
    st.info(predicted_genre.upper())
    st.markdown("<br><h5>Similar Songs: </h5>", unsafe_allow_html = True)
    for track in recommended_tracks_sample['track_names_with_artist'][:10]:
    	st.info("\t🎵 " + track)
