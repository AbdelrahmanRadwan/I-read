from __future__ import unicode_literals
from django.shortcuts import render
from .forms import CreateBookForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from accounts.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Author, Book
from django.template import loader
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View

# write the names of all books in the data base
def ListBookView(request):
    all_books = Book.objects.all()
    template = loader.get_template('AllBooks.html')
    context = \
        {
            'all_books': all_books,
        }
    return HttpResponse(template.render(context, request))


# emails of all the boooks authors in the data base
def ListAuthorView(request):
    all_authors = User.objects.filter(author=True)
    template = loader.get_template('AllAuthors.html')
    context = \
        {
            'all_authors': all_authors,
        }
    return HttpResponse(template.render(context, request))


def DetailsBookView(Request, id):
    specific_Book = Book.objects.get(pk=id)
    template = loader.get_template('Book.html')
    context = \
        {
            'Book': specific_Book,
        }
    return HttpResponse(template.render(context, Request))


# the view which enables the user to add a book
def CreateBookView(request):
    # checking if the form filled well, then we will save the record
    form = CreateBookForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    # template to be rendered
    template = loader.get_template(
        'FormsTemplates/CreateBookFormTemplate.html')
    # html map of definitions
    context = {
        "form": form
    }
    # sending the request
    return HttpResponse(template.render(context, request))


'''
# the view that enables the users to edit book
def view_home(Request):
    #all_authors = Author.objects.all()
    all_books = Book.objects.all()
    template = loader.get_template('Home.html')
    context = \
    {
        #'all_authors' : all_authors,
        'all_books' : all_books,
    }
    return HttpResponse(template.render(context, Request))


def view_author(Request, view_author):
    #specific_Author = Author.objects.get(pk =view_author)
    template = loader.get_template('Author.html')
    context = \
        {
        #    'Author' : specific_Author,
        }
    return HttpResponse(template.render(context, Request))




def DeleteBookView(request, id):

    pass

'''




# Create your views here.
def view_home(Request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    template = loader.get_template('Author/Home.html')
    context = \
        {
            'all_authors': all_authors,
            'all_books': all_books,
        }
    return HttpResponse(template.render(context, Request))


def view_author(Request, view_author):
    specific_Author = Author.objects.get(pk=view_author)
    template = loader.get_template('Author/Author.html')
    context = \
        {
            'Author': specific_Author,
        }
    return HttpResponse(template.render(context, Request))


def view_book(Request, view_book):
    specific_Book = Book.objects.get(pk=view_book)
    template = loader.get_template('Author/Book.html')
    context = \
        {
            'Book': specific_Book,
        }
    return HttpResponse(template.render(context, Request))


