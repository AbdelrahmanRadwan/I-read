from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    Author_Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=15)
    Number_of_Pages = models.IntegerField()
    #the users who favorite this book
    Users = models.ManyToManyField(
        User,
        related_name='book_favourites',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.Title + "book, "+self.Category+"field";

