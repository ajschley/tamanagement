from django.shortcuts import render

from TAmanage.models import User, Course
from TAmanage.views import Home


def input(commandInput, password=None):
    if not Home.loggedIn:
        print("test2")
        try:
            user = User.objects.get(userEmail=commandInput)
        except:
            print("test3")
            response = "Invalid Login"
            return response
        if user.userPassword == password:
            print("test")
            Home.loggedIn = True
            response = "Logged In Successfully"
            user.setLoginState(True)
            return response
        else:
            print("test4")
            response = "Invalid Login"
            return response
    else:
        if commandInput == 'logout':
            response = "Successful logout."
            User.objects.get(userEmail=User.userEmail).setLoginState(False)
            return response;
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
            return response
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
            return response
        # Simon: createCourse command
        elif commandInput[0:12] == 'createCourse':
            inputted = commandInput[13:]
            inputs = inputted.split(' ')
            yourInstance2 = Course(name=inputs[0], startTime=inputs[1], endTime=inputs[2], dates=inputs[3])
            yourInstance2.save()
            response = yourInstance2.courseName() + ' was created.'
            return response
        # Simon: createUser command
        elif commandInput[0:10] == 'createUser':
            inputted = commandInput[11:]
            inputs = inputted.split(' ')
            yourInstance3 = User(userEmail=inputs[0], userPassword=inputs[1], user_type=inputs[2])
            yourInstance3.save()
            response = yourInstance3.userEmail + ' was created.'
            return response
        # Chris: Help command
        elif commandInput == 'help':
            response = "Commands: "
            commandList = ('logout', 'listCourses', 'listUsers', 'createCourse', 'createUser', 'help')

            for command in commandList:
                response += command + "\n"
            return response
        else:
            response = "Invalid Command"
            return response
