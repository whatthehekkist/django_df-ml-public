from django.db.models import Case, When
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from recommend.dbconn import fetch_dataframe_from_table
from recommend.models import Movies
from django.template.loader import render_to_string
import pandas as pd


def recommend_view(request):
    if request.user.is_authenticated:
        return render(request, 'recommend/index.html')
    return redirect(reverse("account:login"))


def movies_view(request):
    # fetch popular_movies
    pop_movies = fetch_dataframe_from_table('popular_movies', "postgres")

    # extract 20 movie_id from pop_movies
    pop_movies_ids = pop_movies.sort_values('mean').iloc[:20, 1].to_list()

    # set sort base by mapping a specific order (pos) to each movie ID
    preserved_order = Case(*[When(movie_id=movie_id, then=pos) for pos, movie_id in enumerate(pop_movies_ids)])

    # ORM query that filters movies with movie IDs included in the pop_movies_ids
    # sort the result in the order defined by preserved_order then
    pop_movies_data = Movies.objects.filter(movie_id__in=pop_movies_ids).order_by(preserved_order)
    # print("pop_movies_data ------\n", pop_movies_data[0].title)
    print("pop_movies_data ------\n")
    for movie in pop_movies_data:
        print(movie.title)

    context = {
        "movies": pop_movies_data
    }
    movies_html = render_to_string("recommend/movies.html", context)
    return JsonResponse({'movies_html': movies_html})


def customers_view(request, model):
    user_id = request.user.user_id  # 143 for user1 set by superuser

    # fetch data frame by model one at a time
    df = pd.DataFrame()
    if model == "svd_model":
        df = fetch_dataframe_from_table(model, "postgres")
    elif model == "nmf_model":
        df = fetch_dataframe_from_table(model, "postgres")
    elif model == "mf_model":
        df = fetch_dataframe_from_table(model, "postgres")

    # fetch customers
    customers = fetch_dataframe_from_table("customers", "postgres")

    # extract ids current user has watched
    movie_ids_watched = customers[customers['user_id'] == user_id]["movie_ids"].str.split(",").explode().astype(
        int).tolist()
    print("movie_ids_watched ------\n", movie_ids_watched)

    # extract movie ids that prediction model (the field predicted_rating in current model) returns
    recommend_movie_ids = df[df["user_id"] == user_id].sort_values("predicted_rating", ascending=False)
    recommend_movie_ids = recommend_movie_ids.iloc[:100, 1].to_list()
    print("recommend_movie_ids ------\n", recommend_movie_ids)

    # extract movie ids excluding movie_ids_watched which current user has already watched
    remaining_movie_ids = [movie_id for movie_id in recommend_movie_ids if movie_id not in movie_ids_watched]
    remaining_movie_ids = remaining_movie_ids[:20]

    # convert remaining_movie_ids into int
    remaining_movie_ids = list(map(int, remaining_movie_ids))
    print(f"Remaining movie IDs: {remaining_movie_ids}")

    # check if remaining_movie_ids is empty and return with message then
    if not remaining_movie_ids:
        print("No remaining movie IDs to recommend.")
        return JsonResponse({'customers_html': "<p>No movie recommendations available</p>"})

    # set sort base by mapping a specific order (pos) to each movie ID
    # sort the result in the order defined by preserved_order then
    preserved_order = Case(*[When(movie_id=movie_id, then=pos) for pos, movie_id in enumerate(remaining_movie_ids)])
    recommend_movie_data = Movies.objects.filter(movie_id__in=remaining_movie_ids).order_by(preserved_order)

    # check recommend_movie_data exists. If not, return with message
    if not recommend_movie_data.exists():
        print(f"No movies found for IDs: {remaining_movie_ids}")
        return JsonResponse({'customers_html': "<p>No movie recommendations available</p>"})

    # movies to recommend exist
    for movie in recommend_movie_data:
        print(f"Recommended movie: {movie.title}")

    # make recommend_movie_data as context
    context = {
        "customers": recommend_movie_data
    }

    # render
    customers_html = render_to_string("recommend/customers.html", context)
    return JsonResponse({'customers_html': customers_html})


