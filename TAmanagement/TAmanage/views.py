from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Course


# Create your views here.
def index(request):
    myQuery = Course.objects.all()
    context = {'myCourses': myQuery}
    return render(request, "main/index.html", context)


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'main/index.html')

    def post(self, request):
        yourInstance = Course()
        commandInput = request.POST["command"]
        if commandInput:
            response = yourInstance.command(commandInput)
        else:
            response = ""
        return render(request, 'main/index.html', {"message": response})
