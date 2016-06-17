"""This module contains all people objects involved in planning a schedule.
"""
class Student(object):
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
    def __init__(self, name, required, desired):
        # Initialize required attributes.
        self.addattr(name=name,
            required=required,
            desired=desired
        )
        self._schedule = {}
        self.happiness = 0
        self.satisfied = False


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
    def schedule(self):
        """Get the students courses."""
        return self._schedule

    @property
    def courses(self):
        """Return mapping of subject to course object"""
        return dict([(course.subject, course) for course self._schedule.values()])

    @property
    def attrs(self):
        """Get attributes of student"""
        return self._attrs

    def addattr(self, **kwargs):
        """Add attributes to student object
        """
        for key, value in kwargs.items():
            self._attrs[key] = value
            setattr(self, key, value)

    def rmattr(self, *args):
        """Remove attributes from student object."""
        for key in args:
            del self._attrs[key]
            delattr(self, key)

    def add(self, course):
        """Add a course to period of the day
        """
        self._schedule[course.period] = course

    def rm(self, period):
        """
        """
        del self._schedule[course.period] = course


class Teacher(object):
    """
    """
    def __init__(self, **kwargs):
        self._schedule = {}
