from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Home(View):
    loggedIn = False
    commandInput = ""
    commandList = ('logout', 'listCourses', 'listUsers', 'createCourse', 'createUser', 'help')

    def get(self, request):
        if Home.loggedIn:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    def post(self, request):
        from TAmanage import Command
        commandInput = request.POST["command"]
        if not Home.loggedIn:
            password = request.POST["command2"]
            response = Command.input(commandInput, password)
        else:
            response = Command.input(commandInput)
        if Home.loggedIn:
            return render(request, 'index.html', {"message": response})
        else:
            return render(request, 'login.html', {"message": response})