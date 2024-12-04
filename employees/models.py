from django.db import models
from django.db.models import UniqueConstraint


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        # return Employee
        # return f"{self.name} and {self.age} and {self.mobile} and {self.address}"

    # class Meta:
    #     constraints = [UniqueConstraint(fields=["username"], name="user_username_unq")]