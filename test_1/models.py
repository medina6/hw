from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=70)

class Comment(models.Model):
    best_comment = models.CharField(max_length=40)
    worst_comment = models.CharField(max_length=50)
