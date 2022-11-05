from django.db import models


class TVShows(models.Model):
    userName=models.CharField(max_length=150)
    password=models.CharField(max_length=500)
    confirmPassword=models.BooleanField(default=False)
