from django.shortcuts import render
from django.views import View
from .models import User
from Lab12 import forms


# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, 'index.html', {"one" : request.session.get("count", "not found")})

    def post(self, request):
        name = request.POST.get("name", "no one")
        count = request.session.get("count", 0)
        count = count + 1
        return render(request, 'index.html', {"count":count})


class Registration(View):

    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        newUser = User(
            email=request.post.get("email"),
            username=request.post.get("username"),
            password=request.post.get("password"),
        )
        print("test2112")
        print(newUser.email)
        request.session[newUser] = newUser
        newUser.save()
        return render(request, 'registration.html', {"form": forms.CreateUser, "newUser": newUser})#"email":newUser.email, "username":newUser.username, "password":newUser.password})


class Users(View):

    def get(self, request):
        return render(request, 'users.html')

    def post(self, request):
        return render(request, 'users.html')


class Gifts(View):

    def get(self, request):
        return render(request, 'gifts.html')

    def post(self, request):
        return render(request, 'gifts.html')
