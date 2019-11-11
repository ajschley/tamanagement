from .models import *
import shlex


class Commands:
    def __init__(self):
        self.cmdList = []
        self.addCmd(Role.Administrator, "Create Course", "/createCourse")
        self.addCmd(Role.Administrator, "Create User", "/createUser")
        # self.addCmd([Role.Instructor, Role.TA], "Edit User", "/editUser")




    def addCmd(self, cmdrole: Role, cmdtxt, cmdurl):
        if isinstance(cmdrole, list):
            for i in cmdrole:
                cmd = {"cmdRole": i, "cmdTxt": cmdtxt, "cmdUrl": cmdurl}
                self.cmdList.append(cmd)
        else:
            cmd = {"cmdRole": cmdrole, "cmdTxt": cmdtxt, "cmdUrl": cmdurl}
            self.cmdList.append(cmd)

    def getCmds(self, forrole: Role):
        cmdList = []
        for i in self.cmdList:
            if i["cmdRole"] == forrole:
                cmdList.append(i)
        return cmdList

class CommandWorker:
    def __init__(self, currentUserEmail = None):
        u = User.objects.filter(email=currentUserEmail).first()
        self.currentUser = u

    def executeCommand(self, cmdstring: str) -> str:
        try:
            cmd = shlex.split(cmdstring)  # don't split quoted substrings
        except:
            return 'Badly formatted command'

        worker = {
            'create': {
                'course': self.create_course,
                'user': self.create_user,
            },
            'login': self.login,
            'logout': self.logout,
        }
        while type(worker) is dict:
            try:
                worker = worker[cmd[0].lower()]
            except Exception as e:
                return 'Not a valid command'
            cmd.pop(0)
        try:
            return worker(cmd)
        except Exception as e:
            return 'error - %s' % e

    def create_course(self, cmd: [str]):
        if not self.currentUser or not self.currentUser.has_role(Role.Administrator):
            return 'Only an Administrator can create a course'
        if len(cmd) != 1:
            return 'Invalid number of parameters'
        c = Course.objects.filter(name=cmd[0])
        if c:
            return 'Course already exists'
        c = Course(name=cmd[0])
        c.save()
        return 'Course added'

    def create_user(self, cmd: [str]):
        if not self.currentUser or not self.currentUser.has_role(Role.Administrator):
            return 'Only an Administrator can create a user'
        if len(cmd) != 2:
            return 'Invalid number of parameters'
        u = User.objects.filter(email=cmd[0])
        if u:
            return 'User already exists'
        u = User(email=cmd[0], password=cmd[1])
        u.save()
        return 'User added'

    def list_courses(self, cmd: [str]):
        if not self.currentUser:
            return 'Need to be logged in to list courses'
        if len(cmd) != 0:
            return 'Invalid number of parameters'
        courses = Course.objects.all()
        courseList = ""
        for c in courses:
            courseList += (c.name + '\n')
        return courseList

    def login(self, cmd: [str]):
        if len(cmd) != 2:
            return 'Invalid number of parameters'
        try:
            u = User.objects.get(email=cmd[0])
        except Exception:
            return 'Given email does not belong to an existing user'
        if u.password != '':
            if u.password == cmd[1]:
                self.currentUser = u
                return 'Logged in as %s' % cmd[0]
            else:
                return 'Invalid credentials'
        else:
            u.password = cmd[1]
            u.save()
            return 'Logged in as %s, your new password has been saved' % cmd[0]

    def logout(self, cmd: [str]):
        if len(cmd) != 0:
            return 'Invalid number of parameters'
        if not self.currentUser:
            return 'No user is logged in'
        self.currentUser = None
        return 'Logged out'
