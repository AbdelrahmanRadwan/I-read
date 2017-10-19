# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Author(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    def __str__(self):
        return str(self.Name + ' ')


class Book(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=15)
    NumberOfPages = models.IntegerField()

    def __str__(self):
        return self.Title + "book, "+self.Category+"field";


