import pandas as pd

movies_data = pd.read_csv('/Users/premkumarkandanmeena/Documents/python/100days_python_bootcamp/python/'
                          'practise_exercises/Exercise_02/Data/movies_data_sample.csv')

pd.set_option('display.max_columns', None)
movies_data[['Budget', 'Box_Office', 'Rating']] = movies_data[['Budget', 'Box_Office', 'Rating']].fillna(0)
print(movies_data)

movies_data.loc[:, ['Budget', 'Box_Office', 'Rating']] = (movies_data[['Budget', 'Box_Office', 'Rating']]
                                                          .apply(pd.to_numeric, errors="coerce"))
movies_data.loc[:, 'Release_Date'] = movies_data['Release_Date'].apply(pd.to_datetime, errors="coerce")

movies_data['Profit'] = movies_data['Box_Office'] - movies_data['Budget']

movies_data.loc[movies_data['Box_Office'] < movies_data['Budget'], 'Box_Office'] = (movies_data['Budget'])

# Group by 'Genre' and aggregate both Rating and Box_Office
movies_data_by_genre_collection = movies_data.groupby('Genre').agg(
    Average_Rating=('Rating', 'mean'),   # Average Rating
    Total_Box_Office=('Box_Office', 'sum')  # Total Box Office
).reset_index()
print('movies_data_by_genre_collection')
print(movies_data_by_genre_collection)
movies_data_by_rating = movies_data.loc[movies_data['Rating'] >= 8]

top_5_profitable_movies = movies_data.sort_values('Profit', ascending=False).head(5).reset_index(drop=True)
print(top_5_profitable_movies)

# Find the Most Common Director
most_common_director = movies_data['Director'].value_counts().idxmax()
director_movie_count = movies_data['Director'].value_counts().max()

print(f"The Most Common Director: {most_common_director} with {director_movie_count} movies")

# Extract the Year from Release_Date
movies_data['Year'] = movies_data['Release_Date'].dt.year

# Group by Year and Calculate Total Box Office
yearly_box_office = movies_data.groupby('Year')['Box_Office'].sum().reset_index()

# Find the Year with the Highest Box Office Total
highest_box_office_year = yearly_box_office.loc[yearly_box_office['Box_Office'].idxmax()]

print("Year with the Highest Box Office Total:")
print(highest_box_office_year)