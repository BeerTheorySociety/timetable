"""Main module for calculating an optimal schedule from a timetable

Each object in Schedule class has a unique ID. First three characters in the ID
describe the type of object. Last 6 characters are a unique number to identify
the object.


"""
ID_PREFIX = {
    Student : "STU",
    Instructor : "INS",
    Course : "COU",
    Period : "PER",
    Day : "DAY"
}

class Scheduler(object):
    """ 
    """
    def __init__(self, *days):
        self.contents = {}

    def _assign_id(self, item):
        """Assign a unique ID to the object given.

        ID keys
        -------
        `STU` : Student object
        `INS` : Instructor object
        `COU` : Course object
        `PER` : Period object
        `DAY` : Day object
        """
        pass


    def timetable(self):
        """ Add a timetable.
        """

    def studentlist(self):
        """
        """

    def add(self, item):
        """
        """
