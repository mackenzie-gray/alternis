from django.db import models

class Search(models.Model):
    search_text = models.CharField(max_length=200)

# Create your models here.
