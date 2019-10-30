from django.shortcuts import render
from django.views import View
from .models import User
from .models import Course


# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        yourInstance = User()
        commandInput = request.POST["command"]
        if commandInput[0:5] == 'login':
            inputted = commandInput[6:]
            inputs = inputted.split(' ')
            response = yourInstance.login(inputs[0], inputs[1])
        elif commandInput == 'logout':
            response = yourInstance.logout()
        else:
            response = "Invalid Command"
        return render(request, 'index.html', {"message": response})
