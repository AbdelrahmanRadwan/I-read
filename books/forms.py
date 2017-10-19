from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = [
            "Author_Name", "Title", "Category", "Number_of_Pages",
        ]

