import pandas as pd

# Read in track metadata with genre labels
tracks = pd.read_csv('datasets/fma-rock-vs-hiphop.csv')

# Read in track metrics with the features
echonest_metrics = pd.read_json('datasets/echonest-metrics.json', precise_float=True)

# Merge the relevant columns of tracks and echonest_metrics
echo_tracks = echonest_metrics.merge(tracks[['genre_top', 'track_id']], on='track_id')

# Inspect the resultant dataframe
echo_tracks.info()

# We typically want to avoid using variables that have strong correlations with each other -- hence avoiding feature redundancy -- for a few reasons:
# To keep the model simple and improve interpretability (with many features, we run the risk of overfitting).
# When our datasets are very large, using fewer features can drastically speed up our computation time.
# To get a sense of whether there are any strongly correlated features in our data, we will use built-in functions in the pandas package.

# Create a correlation matrix
corr_metrics = df.corr()
corr_metrics.style.background_gradient()
