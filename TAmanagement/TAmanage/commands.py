from .models import *
import shlex


class Commands:
    def __init__(self):
        self.cmdList = []
        self.addCmd(Role.Administrator, "Create Course", "/createCourse")
        self.addCmd(Role.Administrator, "Create User", "/createUser")
        self.addCmd(Role.Administrator, "Edit Course", "/editCourse")
        self.addCmd([Role.Administrator, Role.Instructor, Role.TA], "Edit Profile", "/editProfile")
        self.addCmd([Role.Administrator, Role.Instructor, Role.TA], "List Courses", "/listCourses")
        self.addCmd([Role.Administrator, Role.Instructor, Role.TA], "List Users", "/listUsers")
        self.addCmd(Role.Administrator, "Edit User", "/editUser")

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
    def __init__(self, currentUserEmail=None):
        u = User.objects.filter(email=currentUserEmail).first()
        self.currentUser = u

    def executeCommand(self, cmdstring: str) -> str:
        try:
            cmd = shlex.split(cmdstring)
        except:
            return 'Badly formatted command'

        worker = {
            'create': {
                'course': self.create_course,
                'user': self.create_user,
            },
            'edit': {
                'course': self.edit_course,
                'user': self.edit_user,
            },
            'list': {
                'courses': self.list_courses,
                'users': self.list_users,
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

    def list_courses(self, cmd: [str]):
        if not self.currentUser:
            return 'Need to be logged in to list courses'
        if len(cmd) != 0:
            return 'Invalid number of parameters'
        courses = Course.objects.all()
        return courses

    def list_users(self, cmd: [str]):
        if not self.currentUser:
            return 'Only an Administrator or Instructor can list users'
        if len(cmd) != 0:
            return 'Invalid number of parameters'
        users = User.objects.all()
        return users

    def edit_course(self, cmd: [str]):
        if not self.currentUser or not self.currentUser.has_role(Role.Administrator):
            return 'Only an Administrator can edit a course'
        if len(cmd) < 1 or len(cmd) > 5:
            return 'Invalid number of parameters'
        c = Course.objects.get(name=cmd[0])
        valid_dates = {"M", "T", "W", "R", "F", "S"}
        if c:
            c.location = cmd[1]
            c.startTime = cmd[2]
            c.endTime = cmd[3]
            c.save()
            for ch in cmd[4]:
                if valid_dates.intersection(ch):
                    continue
                else:
                    return 'Invalid date(s)'
            c.dates = cmd[4]
        else:
            return 'Course does not yet exist'
        c.save()
        return 'Course updated'

    def edit_profile(self, cmd: [str]):
        u = self.currentUser
        if u:
            u.resume = cmd[1]
            u.schedule = cmd[2]
            u.preferences = cmd[3]
        u.save()
        return 'Profile updated'

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

    def edit_user(self, cmd: [str]):
        if not self.currentUser or not self.currentUser.has_role(Role.Administrator):
            return 'Only an Administrator can edit a user'
        if len(cmd) < 1:
            return 'Invalid number of parameters'
        valid_dates = {"M", "T", "W", "R", "F", "S"}
        u = User.objects.filter(email=cmd[0])
        if u:
            u.firstName = cmd[1]
            u.lastName = cmd[2]
            u.phone = cmd[3]
            u.address = cmd[4]
            u.officeHours = cmd[5]
            u.save()
            for ch in cmd[6]:
                if valid_dates.intersection(ch):
                    continue
                else:
                    return 'Invalid date(s)'
            u.officeHoursDates = cmd[6]
            u.officeLocation = cmd[7]
        else:
            return 'User does not exist'
        u.save()
        return 'User updated'

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
