# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.

class Book(models.Model):
    Author_Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=15)
    Number_of_Pages = models.IntegerField()

    def __str__(self):
        return self.Title + "book, "+self.Category+"field";

