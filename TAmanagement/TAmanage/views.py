from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.template import loader
from .commands import *
from .forms import *

# Create your views here.

worker = CommandWorker()
cmds = Commands()


class Home(View):
    def get(self, req):
        template = loader.get_template('index.html')
        context = {}

        if 'current_role' in req.session:
            context['cmds'] = cmds.getCmds(req.session['current_role'])

        else:
            context['cmds'] = []

        return HttpResponse(template.render(context, req))

    def post(self, req):
        template = loader.get_template('index.html')
        context = {}
        if 'current_role' in req.session:
            context['cmds'] = cmds.getCmds(req.session['current_role'])

        return HttpResponse(template.render(context, req))



class CreateCourse(View):
    def get(self, req):
        template = loader.get_template('form.html')
        context = {}
        context['form'] = CreateCourseForm()
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        return HttpResponse(template.render(context, req))

    def post(self, req):
        form = CreateCourseForm(req.POST)
        template = loader.get_template('form.html')
        context = {}
        if form.is_valid():
            ch = CommandWorker(req.session['current_user'])
            context['out'] = ch.executeCommand(f'create course "{form.cleaned_data["name"]}"')
            context['form'] = CreateCourseForm()
        else:
            context['form'] = form
        context['cmds'] = cmds.getCmds(req.session['current_role'])

        return HttpResponse(template.render(context, req))


class CreateUser(View):

    def get(self, req):
        template = loader.get_template('form.html')
        context = {}
        context['form'] = CreateUserForm()
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        return HttpResponse(template.render(context, req))

    def post(self, req):
        form = CreateUserForm(req.POST)
        template = loader.get_template('form.html')
        context = {}
        if form.is_valid():
            ch = CommandWorker(req.session['current_user'])
            context['out'] = ch.executeCommand(f'create user "{form.cleaned_data["email"]}" "{form.cleaned_data["password"]}"')
            context['form'] = CreateUserForm()
        else:
            context['form'] = form
        context['cmds'] = cmds.getCmds(req.session['current_role'])

        return HttpResponse(template.render(context, req))


class Login(View):

    def get(self, req):
        template = loader.get_template('form.html')
        context = {}
        context['form'] = LoginForm()

        if 'current_role' in req.session:
            context['cmds'] = cmds.getCmds(req.session['current_role'])
        else:
            context['cmds'] = []
        return HttpResponse(template.render(context, req))

    # this function is so gross because of the extra cases for logging in vs normal commands
    def post(self, req):
        print("**************\n")
        form = LoginForm(req.POST)
        if form.is_valid():
            out = worker.executeCommand(f'login {form.cleaned_data["email"]} "{form.cleaned_data["password"]}"')
            if out.startswith('Logged in as'):
                template = loader.get_template('index.html')
                context = {}
                context['out'] = out
                req.session['current_user'] = form.cleaned_data['email']
                u = User.objects.filter(email=form.cleaned_data['email']).first()
                req.session['current_role'] = u.role
            if 'current_role' in req.session:
                context['cmds'] = cmds.getCmds(req.session['current_role'])
            else:
                context['cmds'] = []

            return HttpResponse(template.render(context, req))


class Logout(View):
    def get(self, req):
        template = loader.get_template('index.html')
        context = {}
        req.session['current_user'] = None
        req.session['current_role'] = None
        context['form'] = None
        context['cmds'] = []

        return HttpResponse(template.render(context, req))

    def post(self, req):
        template = loader.get_template('index.html')
        if req.session['current_user']:
            out = 'Successfully logged out'
        else:
            out = 'You must be logged in to log out'
        context = {}
        context['out'] = out
        req.session['current_user'] = None
        req.session['current_role'] = None
        context['cmds'] = cmds.addCmd(req.session['current_role'])
        return HttpResponse(template.render(context, req))
