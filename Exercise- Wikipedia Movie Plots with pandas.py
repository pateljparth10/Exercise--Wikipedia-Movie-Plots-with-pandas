from multiprocessing.reduction import duplicate
import pandas as pd

movies = pd.read_csv("wiki_movie_plots_deduped.csv")

# How many records are in this dataset?
print(len(movies))

# What columns are in this DataFrame?
print(movies.columns)

# How many columns are there?
print(movies.shape)

# How many non-null observations are there in each column?
print(movies.info())

# What are the last 8 records of the dataset? Use a function
print(movies.tail(8))

# What are the last 8 records of the dataset? Use indexing
legnth_of_movies = len(movies) - 8
print(movies[legnth_of_movies:])

# What are the first 5 records of the dataset? Use a function.
print(movies.head())

# What are the first 5 records of the dataset? Use indexing.
top_5_movies_list = len(movies)-5
print(movies[:-top_5_movies_list])

# What are the top 5 listed genres?
top_5_genres = movies["Genre"].value_counts().nlargest()
print(top_5_genres)

# Who are the top 5 directors?
top_5_directors = movies["Director"].value_counts().nlargest()
print(top_5_directors)

# What are the counts for origin/ethnicity?
count_of_origin = movies["Origin/Ethnicity"].value_counts()
print(count_of_origin)

# Are there any titles that are duplicated?
duplicate_titles = movies["Title"].value_counts().nlargest()
print(duplicate_titles)

# What is the most popular year?
most_popular_movie_year = movies["Release Year"].value_counts().nlargest(1)
print(most_popular_movie_year)