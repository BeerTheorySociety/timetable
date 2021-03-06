"""This module contains all people objects involved in planning a schedule.
"""
from .handlers import Handler

class Student(Handler):
    """ Student object

    Arguments
    ---------
    name : str
        name of student
    required : list
        list of required courses for student
    desired : list
        list of favored electives chosen by student

    Attributes
    ----------
    satisfied : bool
        True is all required courses are found in schedule
    schedule : dict
        mapping period of day to course object
    courses : dict
        mapping subject to course object
    happiness : float
        score for *happiness*, determined by some external scoring function

    Metadata
    --------
    student = {
        "id" : "XX00000000"
        "name" : "Alice",
        "satisfied": True,
        "happiness" : 0.5,
        "required" : [
            "Math 8",
            "English 7",
            ...
        ],
        "desired" : [
            "Cooking",
            "Band",
            ...
        ],
        "schedule" : {
            1 : "Math 8",
            2 : "English 7",
            ...
        }
    }
    """
    def __init__(self, name, required, desired, **attrs):
        # Initialize required attributes.
        super(Student, self).__init__(
            name=name,
            required=required,
            desired=desired,
            **attrs
        )
        self.happiness = 0

    @property
    def satisfied(self):
        """Is the student's required set of classes satisfied."""
        satisfied = True
        for r in self.required:
            if r not in self.courses:
                satisfied = False
                break
        return satisfied

    @property
    def _prefix(self):
        return "STU"

    def add_course(course):
        """Add a course to the student's schedule
        """

    def rm_course(course_id):
        """
        """

class Instructor(Handler):
    """

    Metadata
    --------
    instructor = {
        "id" : "INS000001",
        "name" : "Bob",
    }

    """
    def __init__(self, name, **attrs):
        super(Instructor, self).__init__(name=name, **attrs)

    @property
    def _prefix(self):
        return "INS"
