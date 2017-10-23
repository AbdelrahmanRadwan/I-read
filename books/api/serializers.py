from rest_framework import serializers
from django import forms
from books.models import Book


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = [
            "id",
            "Author_Name",
            "Title",
            "Category",
            "Number_of_Pages",
            "Users",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = [
            "id",
            "Author_Name",
            "Title",
            "Category",
            "Number_of_Pages",
            "Users",
        ]

