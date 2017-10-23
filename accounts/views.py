from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'Author/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'];
            password = form.cleaned_data['password'];
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password= password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Book:Home_')
        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Author.objects.filter(user=request.user)
                return render(request, 'Author/Home.html')#, {'albums': albums})
            else:
                return render(request, 'Author/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Author/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Author/login.html')



def ListUserView(request):
    all_users = User.objects.all()
    query = request.GET.get("q")
    template = loader.get_template('AllUsers.html')

    if query:
        all_users =all_users.filter(Title__icontains=query)
    context = \
        {
            'all_users': all_users,
            'request':request,
        }
    return HttpResponse(template.render(context, request))
