from django.urls import path
from recommend import views

app_name = "recommend"
urlpatterns = [
    path('', views.recommend_view, name='index'),
    path('movies/', views.movies_view, name='movies'),
    path('customers/<str:model>/', views.customers_view, name='customers'),
]