from django.http import JsonResponse
from django.shortcuts import render
from recommend.dbconn import fetch_dataframe_from_table
from collections import Counter


def genre_distribution_view(request):
    return render(request, 'chart/genre_distribution_view.html')


def pop_chart_view(request):
    pop_movies = fetch_dataframe_from_table('popular_movies', "postgres")
    movies = fetch_dataframe_from_table("movies", "postgres")

    # extract 20 of movie_id from pop_movies
    pop_movies_ids = pop_movies.sort_values('mean').iloc[:20, 1].to_list()
    # print("pop_movies_ids ----\n", pop_movies_ids)

    # Extract genre information of movies corresponding to popular movie IDs.
    # Results are saved in DataFrame format containing only genre.
    # (Extract a new DataFrame with only the genres of movies included in pop_movies_ids filtered.)
    filtered_movies = movies[movies['movie_id'].isin(pop_movies_ids)][['genre']]
    # print("filtered_movies ----\n", filtered_movies)

    # collect string in the data frame above, split by ',' and make each string as a single row.
    all_genres = filtered_movies['genre'].apply(lambda x: x.split(',')).explode()
    # print("all_genres ----\n", all_genres)

    # covert into list
    all_genres = all_genres.tolist()

    # trim all_genres and count genre
    cleaned_genres = [genre.strip() for genre in all_genres]
    # print("cleaned_genres ----\n", cleaned_genres)

    genre_data = Counter(cleaned_genres)
    # print("genre_data ----\n", genre_data)

    return JsonResponse(genre_data)


def cust_chart_view(request):
    user_id = request.user.user_id
    # print(type(user_id))

    customers = fetch_dataframe_from_table('customers', "postgres")
    movies = fetch_dataframe_from_table("movies", "postgres")

    # get movie genre info a specific user_id has
    user_movie_ids = customers[customers['user_id'] == user_id]['movie_ids'].apply(
        lambda x: [int(movie_id) for movie_id in x.split(',')]  # split by , and convert into int
    )
    # print("****", user_genres)

    # convert into list
    user_genre_list = user_movie_ids.explode().tolist()
    # print("*****", user_genre_list[:10])

    # Extract a DataFrame containing only movies that correspond to the user's preferred genre
    filtered_movies = movies[movies['movie_id'].isin(user_genre_list)]
    # print(filtered_movies)

    # collect string in the data frame above, split by ',' and make each string as a single row.
    all_genres = filtered_movies['genre'].apply(lambda x: x.split(',')).explode()
    print(all_genres)

    # convert into list
    all_genres = all_genres.tolist()

    # trim all_genres and count genre
    cleaned_genres = [genre.strip() for genre in all_genres]
    genre_data = Counter(cleaned_genres)

    return JsonResponse(genre_data)


def svd_chart_view(request):
    user_id = request.user.user_id
    svd_matrix = fetch_dataframe_from_table("svd_model", "postgres")
    svd_movie_ids = svd_matrix[svd_matrix["user_id"] == user_id].sort_values("predicted_rating", ascending=False)
    svd_movie_ids = svd_movie_ids.iloc[:100, 1].to_list()
    # print(svd_movie_ids)

    movies = fetch_dataframe_from_table("movies", "postgres")

    # Extract a new DataFrame with the genres of movies included in svd_movie_ids filtered.
    filtered_movies = movies[movies['movie_id'].isin(svd_movie_ids)][['genre']]

    # collect string in the data frame above, split by ',' and make each string as a single row.
    all_genres = filtered_movies['genre'].apply(lambda x: x.split(',')).explode()

    # covert into list
    all_genres = all_genres.tolist()

    # trim all_genres and count genre
    cleaned_genres = [genre.strip() for genre in all_genres]
    genre_data = Counter(cleaned_genres)

    return JsonResponse(genre_data)


def nmf_chart_view(request):
    user_id = request.user.user_id
    nmf_matrix = fetch_dataframe_from_table("nmf_model", "postgres")
    nmf_movie_ids = nmf_matrix[nmf_matrix["user_id"] == user_id].sort_values("predicted_rating", ascending=False)
    nmf_movie_ids = nmf_movie_ids.iloc[:100, 1].to_list()
    # print(svd_movie_ids)
    movies = fetch_dataframe_from_table("movies", "postgres")

    # Extract a new DataFrame with the genres of movies included in nmf_movie_ids filtered.
    filtered_movies = movies[movies['movie_id'].isin(nmf_movie_ids)][['genre']]

    # collect string in the data frame above, split by ',' and make each string as a single row.
    all_genres = filtered_movies['genre'].apply(lambda x: x.split(',')).explode()

    # covert into list
    all_genres = all_genres.tolist()

    # trim all_genres and count genre
    cleaned_genres = [genre.strip() for genre in all_genres]
    genre_data = Counter(cleaned_genres)

    return JsonResponse(genre_data)


def mf_chart_view(request):
    user_id = request.user.user_id
    mf_matrix = fetch_dataframe_from_table("mf_model", "postgres")
    mf_movie_ids = mf_matrix[mf_matrix["user_id"] == user_id].sort_values("predicted_rating", ascending=False)
    mf_movie_ids = mf_movie_ids.iloc[:100, 1].to_list()
    # print(svd_movie_ids)

    movies = fetch_dataframe_from_table("movies", "postgres")

    # Extract a new DataFrame with the genres of movies included in mf_movie_ids filtered.
    filtered_movies = movies[movies['movie_id'].isin(mf_movie_ids)][['genre']]

    # collect string in the data frame above, split by ',' and make each string as a single row.
    all_genres = filtered_movies['genre'].apply(lambda x: x.split(',')).explode()

    # covert into list
    all_genres = all_genres.tolist()

    # trim all_genres and count genre
    cleaned_genres = [genre.strip() for genre in all_genres]
    genre_data = Counter(cleaned_genres)

    return JsonResponse(genre_data)
