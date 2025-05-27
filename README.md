# MovieRecommendationSystem
Overview
This is a content-based movie recommendation system that suggests movies similar to a given movie based on their content. The system uses text vectorization techniques and similarity measures to find movies that are close in terms of description or attributes.

How It Works
The system extracts textual features from movies (such as plot summary, genres, or other metadata).

Text data is transformed into numerical vectors using the Bag of Words model.

The similarity between movies is calculated using Cosine Similarity (or cosine distance) on these vectors.

Given a movie, the system recommends movies that are most similar based on their content.

Features
Content-based filtering (no user ratings required).

Uses cosine similarity for accurate similarity scoring.

Efficient vectorization using Bag of Words.

Easily extendable to other text features.

Usage
Load the preprocessed data and similarity matrix (similarity.pkl).

Input a movie title to get recommendations.

Checkout the live demo here!
https://movierecommendationsystem-bjzugynyxabvdw7ljoutda.streamlit.app/

Receive a list of movies ranked by similarity.

Requirements
Python 3.x

Libraries: numpy, pandas, scikit-learn (for vectorization and similarity calculation)
