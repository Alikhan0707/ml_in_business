from django.db import models

class Stopwords(models.Model):

    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word


class Articles(models.Model):

    text = models.TextField()
    rubric = models.CharField(max_length=255)

    def __str__(self):
        return self.text