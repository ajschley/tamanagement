from ApplicationFrameworkAcceptanceTests import ApplicationFrameworkAcceptanceTests
import unittest


class TestCreateCourse(unittest.TestCase):

    def test_empty(self):
        ApplicationFrameworkAcceptanceTests.createCourse(self, "course1")  # Where there are no courses.
        assert"Course added."

    def test_proper(self):
        ApplicationFrameworkAcceptanceTests.createCourse(self, "course2")  # Where there is one non-conflicting course.
        assert"Course added."

    def test_conflicting(self):
        ApplicationFrameworkAcceptanceTests.createCourse(self, "course2")  # Where there is a conflicting course.
        assert"Conflicting course found, could not add."


if __name__ == '__main__':
    unittest.main()
