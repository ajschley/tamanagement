from django.test import TestCase
from .models import Course, User, CourseCreation


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="CS361", isCourseFull=False)
        Course.objects.create(name="CS395", isCourseFull=True)

    def test_course_return(self):
        course1 = Course.objects.get(name="CS361")
        self.assertEqual(course1.courseName(), 'CS361')

    def test_course_not_full(self):
        course1 = Course.objects.get(name="CS361")
        self.assertFalse(course1.isFull())

    def test_course_full(self):
        course2 = Course.objects.get(name="CS395")
        self.assertTrue(course2.isFull())

