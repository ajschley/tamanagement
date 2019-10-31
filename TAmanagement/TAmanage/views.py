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
        elif commandInput[0:12] == 'createCourse':
            inputted = commandInput[13:]
            inputs = inputted.split(' ')
            yourInstance2 = Course(name=inputs[0], startTime=inputs[1], endTime=inputs[2], dates=inputs[3])
            yourInstance2.save()
            response = yourInstance2.courseName() + ' was created.'
        elif commandInput[0:10] == 'createUser':
            inputted = commandInput[11:]
            inputs = inputted.split(' ')
            yourInstance3 = User(userEmail=inputs[0], userPassword=inputs[1], user_type=inputs[2])
            yourInstance3.save()
            response = yourInstance3.username() + ' was created.'
        else:
            response = "Invalid Command"
        return render(request, 'index.html', {"message": response})
