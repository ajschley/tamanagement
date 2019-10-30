from django.test import TestCase
from models import Course, User


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(courseName="CS361", isFull="False")

    def test_course_return(self):
        course1 = Course.objects.get(name="CS361")
        self.assertEqual(course1.coursename(), 'CS361')
