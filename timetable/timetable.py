from .day import Day

class TimeTable(object):
    """ Object that contains a Timetable to construct schedules. This object
    describes the days in week, periods in day, courses in period, and
    instructors in periods.

    This object is passed into a schedule object along with a student list
    object. The scheduler object will match students to a TimeTable object.

    Arguments
    ---------
    *Days : optional arguments

    Metadata
    --------
    timetable = {
        "Days" : [
            {
                "id" : "DAY000001",
                "name" : "Monday"
                "Periods" : [
                    "PER0000001",
                    "PER0000002",
                    "PER0000003",
                    ...
                ]
            },
            {
                "id" : "DAY000002",
                "name" : "Tuesday"
                "Periods" : [
                    "PER0000004",
                    "PER0000005",
                    "PER0000006",
                    ...
                ]
            }
        ],
        "Periods" : [
            {
                "id" : "PER0000001",
                "time" : "9AM",
                "Courses" : [
                    "COU000001",
                    "COU000002",
                    ...
                ],

            },
            {
                "id" : "PER0000002",
                "time" : "10AM",
                "Courses" : [
                    "COU000003",
                    "COU000004",
                    ...
                ],

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
    def __init__(self, *Days):
        self._contents = {}
        for Day in Days:
            self.add(Day)

    @property
    def days(self):
        """Get dictionary of Day objects. """
        return self._contents

    def add(self, day):
        """Add Day object to TimeTable.
        """
        self._assign_id(day)
        setattr(self, day.id, day)
        self._contents[day.id] = day

    @staticmethod
    def _check_type(item):
        """ Check that the item is a Day object.
        """
        if item.__class__ != "Day":
            raise Exception("""Argument must be a Day object!""")

    def _assign_id(self, day):
        """Assigns an `id` to a Day object.
        """
        # Check that argument is actually a Day object
        self._check_type(day)
        # If the day doesn't already have an ID, give it one
        if hasattr(day, "id") is False:
            prefix = "DAY"
            number = 0
            new_id = prefix + "%06d" % number
            while new_id in self._contents.keys():
                number += 1
                new_id = prefix + "%06d" % number
            self.day.add(id=new_id)
        # If ID exists in day, check that it isn't in this object already
        else:
            if day.id in self._contents:
                raise Exception("""A Day object with the same ID already exists
                in the timetable object.
                """)

    def rm(self, id):
        """Remove Day with `id` from timetable.
        """
        delattr(self, id)
        del self._contents[id]
