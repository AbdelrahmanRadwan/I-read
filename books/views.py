from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateBookForm
from .models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


# write the names of all books in the data base
def ListBookView(request):
    all_books = Book.objects.all()
    template = loader.get_template('AllBooks.html')
    context = \
        {
            'all_books': all_books,
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


def UpdateBookView(request, id):

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

    # checking if the form filled well, then we will save the record
    instance = get_object_or_404(Book,id=id)
    instance.delete()
    return redirect('books:home')

