from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .models import Course


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
        # Simon: login code
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
                user.setLoginState(True)
                return render(request, 'index.html', {"message": response})
            else:
                response = "Invalid Login"
                return render(request, 'login.html', {"message": response})
        else:
            # yourInstance = User()
            commandInput = request.POST["command"]
            # Simon: logout command
            if commandInput == 'logout':
                response = "Successful logout."
                User.objects.get(userEmail=User.userEmail).setLoginState(False)
                return render(request, 'login.html', {"message": response})
            # Simon: listCourses command
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
            # Simon: listUsers command
            elif commandInput == 'listUsers':
                userList = User.objects.all()
                response = "Users: "
                i = 0
                for user in userList:
                    if i == 0:
                        response += user.userEmail
                    else:
                        response += ", " + user.userEmail
                    i += 1
            # Simon: createCourse command
            elif commandInput[0:12] == 'createCourse':
                inputted = commandInput[13:]
                inputs = inputted.split(' ')
                yourInstance2 = Course(name=inputs[0], startTime=inputs[1], endTime=inputs[2], dates=inputs[3])
                yourInstance2.save()
                response = yourInstance2.courseName() + ' was created.'
            # Simon: createUser command
            elif commandInput[0:10] == 'createUser':
                inputted = commandInput[11:]
                inputs = inputted.split(' ')
                yourInstance3 = User(userEmail=inputs[0], userPassword=inputs[1], user_type=inputs[2])
                yourInstance3.save()
                response = yourInstance3.userEmail + ' was created.'
            # Chris: Help command
            elif commandInput == 'help':
                response = "Commands: "
                commandList = ('logout', 'listCourses', 'listUsers', 'createCourse', 'createUser', 'help')

                for command in commandList:
                    response += command + "\n"

            else:
                response = "Invalid Command"
            return render(request, 'index.html', {"message": response})
