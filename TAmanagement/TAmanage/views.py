from django.http import HttpResponse
from django.views import View
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
            context['text'] = "Welcome to the TA Management App."

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


class EditCourse(View):

    def get(self, req):
        template = loader.get_template('editCourse.html')
        context = {}
        cname = req.GET.get('courseName', '')
        c = Course.objects.get(name=cname)

        form = EditCourseForm()
        form.initial['name'] = c.name
        form.initial['dates'] = c.dates
        form.initial['location'] = c.location
        form.initial['startTime'] = c.startTime
        form.initial['endTime'] = c.endTime

        context['form'] = form
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        ch = CommandWorker(req.session['current_user'])
        context['courses'] = ch.executeCommand(f'list courses')
        return HttpResponse(template.render(context, req))

    def post(self, req):
        form = EditCourseForm(req.POST)
        template = loader.get_template('editCourse.html')
        context = {}
        if form.is_valid():
            ch = CommandWorker(req.session['current_user'])
            context['out'] = ch.executeCommand(f'edit course "{form.cleaned_data["name"]}" '
                                               f'"{form.cleaned_data["location"]}" '
                                               f'"{form.cleaned_data["startTime"]}" '
                                               f'"{form.cleaned_data["endTime"]}" '
                                               f'"{form.cleaned_data["dates"]}" ')

            context['form'] = EditCourseForm()
        else:
            context['form'] = form
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        ch = CommandWorker(req.session['current_user'])
        context['courses'] = ch.executeCommand(f'list courses')
        return HttpResponse(template.render(context, req))


class EditProfile(View):

    def get(self, req):
        template = loader.get_template('form.html')
        context = {}
        context['form'] = EditProfileForm()
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        return HttpResponse(template.render(context, req))

    def post(self, req):
        form = EditProfileForm(req.POST)
        template = loader.get_template('form.html')
        context = {}
        if form.is_valid():
            ch = CommandWorker(req.session['current_user'])
            context['out'] = ch.executeCommand(f'edit profile "{form.cleaned_data["resume"]}" '
                                               f'"{form.cleaned_data["schedule"]}" '
                                               f'"{form.cleaned_data["preferences"]}" ')

            context['form'] = EditProfileForm()
        else:
            context['form'] = form
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        return HttpResponse(template.render(context, req))


class ListCourses(View):

    def get(self, req):
        template = loader.get_template('table.html')
        context = {}
        ch = CommandWorker(req.session['current_user'])
        context['cmds'] = cmds.getCmds(req.session['current_role'])
        context['courses'] = ch.executeCommand(f'list courses')
        return HttpResponse(template.render(context, req))


class ListUsers(View):

    def get(self, req):
        template = loader.get_template('userTable.html')
        context = {}
        ch = CommandWorker(req.session['current_user'])
        context['users'] = ch.executeCommand(f'list users')
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
            context['out'] = ch.executeCommand(
                f'create user "{form.cleaned_data["email"]}" "{form.cleaned_data["password"]}"')
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

    def post(self, req):
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
