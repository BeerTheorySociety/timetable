"""
"""

from .handlers import ContainerHandler
from .course import Course

class Period(ContainerHandler):
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
        super(Period, self).__init__(time=time, *courses, **attrs)

    @property
    def course(self):
        """sGet courses in period."""
        return self._contents

    @property
    def _prefix(self):
        return "PER"

    @property
    def _child_type(self):
        return Course
