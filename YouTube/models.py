from django.db import models

# Create your models here.


class YouTubeSearcher(models.Model):
    Searcher_Email=models.EmailField()

    def __repr__(self):
        return self.Searcher_Email