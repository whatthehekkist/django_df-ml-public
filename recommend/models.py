from django.db import models


class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=1000)
    movie_image = models.ImageField("영화 이미지", upload_to="recommend/thumbnails", blank=True, null=True)

    # def __str__(self):
    #     return self.name
