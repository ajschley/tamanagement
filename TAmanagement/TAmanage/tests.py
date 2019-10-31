from django.test import TestCase
from TAmanage.models import Course, User


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(courseName="CS361", isFull="False")
        Course.objects.create(courseName="CS395", isFull="True")

    def test_course_return(self):
        course1 = Course.objects.get(courseName="CS361")
        self.assertEqual(course1.courseName(), 'CS361')

    def test_course_not_full(self):
        course1 = Course.objects.get(courseName="CS361")
        self.assertFalse(course1.isFull())

    def test_course_full(self):
        course2 = Course.objects.get(courseName="CS395")
        self.assertTrue(course2.isFull())
