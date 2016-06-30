from .base import BaseContainerHandler
from .period import Period

class Day(BaseContainerHandler):
    """Day object for managing all periods in day.

    Arguments
    ---------
    name : str
        name of the day (i.e. Monday, etc.)
    *Periods : optional args
        Period object to add to the day
    **attrs : optional keyword arguments
        Attributes to add to the

    Metadata
    --------
    day = {
        "id" : "DAY000001",
        "name" : "Monday"
        "Periods" : [
            {
                "id" : "PER0000001",
                "time" : "9AM",
                "Courses" : [
                    "COU000001",
                    "COU000002",
                    ...
                ]
            },
            {
                "id" : "PER0000002",
                "time" : "10AM",
                "Courses" : [
                    "COU000003",
                    "COU000004",
                    ...
                ]
            },
        ]
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
    def __init__(self, name, *Periods, **attrs):
        super(Day, self).__init__(name=name, *Periods, **attrs)

    @property
    def periods(selfs):
        """Get periods in day.
        """
        return self._contents

    @property
    def _prefix(self):
        return "DAY"

    @property
    def _child_type(self):
        return Period
