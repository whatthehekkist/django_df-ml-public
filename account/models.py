from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class User(AbstractUser):
    user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField("profile image", upload_to="account/profile",
                                      blank=True)
    short_description = models.TextField('description', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        constraints = [UniqueConstraint(fields=["username"], name="user_username_unq")]