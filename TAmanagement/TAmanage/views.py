from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .models import Course


# Create your views here.
class Home(View):
    loggedIn = False

    def get(self, request):
        if Home.loggedIn:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    def post(self, request):

        if not Home.loggedIn:
            commandInput = request.POST["command"]
            try:
                user = User.objects.get(userEmail=commandInput)
            except:
                response = "Invalid Login"
                return render(request, 'login.html', {"message": response})
            commandInput = request.POST["command2"]
            if user.userPassword == commandInput:
                Home.loggedIn = True
                response = "Logged In Successfully"
                return render(request, 'index.html', {"message": response})
            else:
                response = "Invalid Login"
                return render(request, 'login.html', {"message": response})
        else:
            # yourInstance = User()
            commandInput = request.POST["command"]
            if commandInput == 'logout':
                response = "Successful logout."
                return render(request, 'login.html', {"message": response})
            elif commandInput == 'listCourses':
                courseList = Course.objects.all()
                response = "Courses: "
                i = 0
                for course in courseList:
                    if i == 0:
                        response += course.courseName()
                    else:
                        response += ", " + course.courseName()
                    i += 1
            elif commandInput == 'listUsers':
                userList = User.objects.all()
                response = "Users: "
                i = 0
                for user in userList:
                    if i == 0:
                        response += user.username()
                    else:
                        response += ", " + user.username()
                    i += 1
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
