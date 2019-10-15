import datetime


class CourseTime:
    """
    Contains a start time, end time, and day(s) of the week.
    """
    def __init__(self, time):
        if not isinstance(time, str):
            raise TypeError
        l = time.split()
        start = l[0]
        end = l[1]
        days = l[2]
        return

    """
    Returns online if class is online, otherwise a string containing start, end, and days. No post-conditions.
    """
    def __str__(self):
        return "online"

    """
    Returns the stored time of the class as a datetime.time object, or midnight if it is an online class. No post-conditions.
    """
    def __start__(self):
        return None

    """
    Returns the stored time of the class as a datetime.time object, or midnight if it is an online class. No post-conditions.
    """
    def __end__(self):
        return None

    """
    True if it is online, false if not. No post-conditions.
    """
    def __isOnline__(self):
        return False

    """
    Returns true if there is an overlap, false if not. No post-conditions.
    """
    def __isOverlap__(self, time):
        return False
