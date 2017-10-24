from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from pyelasticsearch import ElasticSearch
from elasticsearch_dsl import Search
from elasticsearch import helpers, Elasticsearch
from collections import defaultdict
from time import time
import requests
import json
import pprint
import csv

# write the names of all books in the data base
def ListBookView(request):
    client = Elasticsearch()
    my_search = Search(using=client)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    all_books = Book.objects.all()
    query = request.GET.get("q")
    template = loader.get_template('AllBooks.html')

    if query:


        #all_books =all_books.filter(Title__icontains=query)
        all_books = es.search(index="books", body={"query": {"match_all": {}}})


        pprint.pprint(all_books['hits'])

    context = \
        {
            'all_books': all_books,
            'request':request,
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
    if not request.user.is_superuser:
        raise Http404
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


def UpdateBookView(request, id):
    if not request.user.is_superuser:
        raise Http404
    # checking if the form filled well, then we will save the record
    instance = get_object_or_404(Book,id=id)
    form = CreateBookForm(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    # template to be rendered
    template = loader.get_template(
        'FormsTemplates/UpdateBookFormTemplate.html')
    # html map of definitions
    context = {
        "instance": instance,
        "form": form,
    }
    return HttpResponse(template.render(context, request))

def DeleteBookView(request, id):
    if not request.user.is_superuser:
        raise Http404
    # checking if the form filled well, then we will save the record
    instance = get_object_or_404(Book,id=id)
    instance.delete()
    return redirect('books:home')

def LikeBookView(request, id):
    selected_book = get_object_or_404(Book, id=id)
    current_user = User.objects.get(id=request.user.id)

    if current_user in selected_book.Users.all():
        selected_book.Users.remove(request.user)
    else:
        selected_book.Users.add(request.user)
    selected_book.save()
    return redirect('books:home')
