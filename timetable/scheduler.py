"""The Scheduler class is where all the magic happens. This object manages the
scheduling algorithm which matches a StudentList and constraints to a TimeTable
object and its constraints.

Fitting/optimizing methods are run by this class. Students schedules are
changed through this class.
"""

class Scheduler(object):
    """
    """
    def __init__(self, TimeTable, StudentList, function):
        self.TimeTable = TimeTable
        self.StudentList = StudentList
        self.function = function

    def swap(self):
        pass

    def optimize(self):
        pass
