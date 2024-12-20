# Importing Pandas
import pandas as pd

# Creating a sample DataFrame for movie data
movie_data = {
    "Title": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    "Genre": ["Action", "Drama", "Action", "Comedy", "Drama"],
    "Director": ["Director X", "Director Y", "Director X", "Director Z", "Director Y"],
    "Release_Date": ["2020-05-15", "2019-07-20", "2021-06-10", "2018-08-25", "2020-03-05"],
    "Budget": [50, 30, 45, 20, None],  # One missing value
    "Box_Office": [150, 100, 120, 60, 0],  # One underperforming movie
    "Rating": [8.5, 7.8, 8.2, None, 6.5],  # One missing rating
    "Runtime": [120, 135, 110, 95, 130],
}

# Convert to DataFrame
movies_df = pd.DataFrame(movie_data)

# Save to CSV locally
movies_df.to_csv("movies_data_sample.csv", index=False)

print("CSV file 'movies_data_sample.csv' generated successfully!")