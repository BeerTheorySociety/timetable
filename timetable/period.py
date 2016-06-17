"""
"""
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
        "number" : 1,
        "courses" : [
            "Math 7",
            "English 8",
            ...
        ]
    }
    """
    def __init__(self, number, time, *courses):
        self.number = number
        self.time = time
        self._courses = {}

        for course in courses:
            self.add(course)

    def add(self, course):
        """Add course to period."""
        self._courses[course.subject] = course
        setattr(self, course.subject, course)

    def rm(self, course):
        """Remove course from period."""
        del self._courses[course.subject]
        delattr(self, course.subject)
