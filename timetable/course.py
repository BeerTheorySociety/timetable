"""Module for managing course objects
"""

from .base import BaseContainerHandler

class Course(BaseContainerHandler):
    """Course object. Holds all the information about

    Arguments
    ---------
    subject : str
        subject of course
    teacher : str
        instructors name
    period : int
        period of the day

    Attributes
    ----------
    teacher : str
        Name of teacher
    period : int
        Period in the day
    students : dict
        Dictionary with students' names mapped to student objects

    Metadata
    --------
    course = {
        "id" : "COU000001",
        "name" : "Math 7"
        "Instructor" : "INS000001",
    }
    """
    def __init__(self, name, *Teacher):
        super(Course, self).__init__(name=name, *Teacher)
