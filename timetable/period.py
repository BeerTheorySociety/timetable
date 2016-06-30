"""
"""

from .course import Course

class Period(object):
    """Period object, containing data about all classes during this period of day.

    Arguments
    ---------
    number : int
        period number of day
    *courses : (optional)
        option arguments which must be course objects describing the courses offered
        during this period.

    Attributes
    ----------
    number : int
        period number in day.
    time : string
        time of day
    courses : dict
        Dictionary with subjects mapped to course object (containing all student
        imformation as well.)
    *course : course objects
        These are flexible attributes named after courses


    Metadata
    --------
    period = {
        "id" : "PER0000001",
        "time" : "9AM",
        "Courses" : [
            {
                "id" : "COU000001",
                "name" : "Math 7"
                "Instructor" : "INS000001",
            },
            {
                "id" : "COU000002",
                "name" : "Science 8"
                "Instructor" : "INS000002",
            }
        ],
        "Instructors" : [
            {
                "id" : "INS000001",
                "name" : "Bob",
            },
            {
                "id" : "INS000002",
                "name" : "Alice"
            }
        ]
    }
    """
    def __init__(self, time, *courses, **attrs):
        self.number = number
        self.time = time
        self._contents = {}
        self._attrs = {}
        self.add(*courses)
        self.addattr(**attrs)

    @staticmethod
    def _check_type(item):
        """ Check that the item is a Course object.
        """
        if item.__class__ != "Course":
            raise Exception("""Argument must be a Period object!""")

    def _assign_id(self, course):
        """Assigns an `id` to a Course object.
        """
        # Check that argument is actually a Course object
        self._check_type(course)
        # If the course doesn't already have an ID, give it one
        if hasattr(course, "id") is False:
            prefix = "PER"
            number = 0
            new_id = prefix + "%06d" % number
            while new_id in self._contents.keys():
                number += 1
                new_id = prefix + "%06d" % number
            self.course.add(id=new_id)
        # If ID exists in Course, check that it isn't in this object already
        else:
            if period.id in self._contents:
                raise Exception("""A Course object with the same ID already exists
                in the Course object.
                """)

    def add(self, *courses):
        """Add course to period."""
        for course in courses:
            self._courses[course.subject] = course
            setattr(self, course.subject, course)

    def rm(self, course):
        """Remove course from period."""
        del self._courses[course.subject]
        delattr(self, course.subject)
