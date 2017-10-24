from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'es_index_name', 'es_type_name', 'es_mapping'
)
class Book(models.Model):
    Author_Name = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Number_of_Pages = models.IntegerField()
    #the users who favorite this book
    Users = models.ManyToManyField(
        User,
        related_name='book_favourites',
        null=True,
        blank=True
    )
    class Meta:
        es_index_name = 'books'
        es_type_name = 'Book'
        es_mapping = {
            'properties': {
                'Author_Name': {'type': 'text'},
                'Title': {'type': 'text'},
                'Category': {'type': 'text'},
                'Number_of_Pages': {'type': "long"},
                'Users': {
                    'type': 'object',
                    'properties': {
                        'Number_of_Pages': {'type': "long"},
                        'name': {'type': 'text'},
                        'email': {'type': 'text'},
                    }
                },
            }
        }


    def __str__(self):
        return self.Title + "book, "+self.Category+"field";


    def es_repr(self):
        data={
            "Author_Name":self.Author_Name,
            "Title":self.Title,
            "Category": self.Category,
            "Number_of_Pages": self.Number_of_Pages,
            "Users":{
                #"pk": self.Users.pk,
                "name": self.Users.name,
                #"email": self.Users.email,
            },
        }
        return data

