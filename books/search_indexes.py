from haystack import indexes
from .models import Book
from django.db import models


class BookIndex(indexes.SearchField, indexes.Indexable):
    fields = ["Author_Name",
              "Title",]
    Author_Name = indexes.CharField(document=True, use_template=True)
    Title = indexes.CharField(model_attr='Title')


    def get_model(selfs):
        return Book




