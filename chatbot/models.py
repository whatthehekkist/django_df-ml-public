from django.db import models


class ChatModel(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
