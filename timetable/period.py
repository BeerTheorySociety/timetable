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
    courses : dict
        Dictionary with subjects mapped to course object (containing all student
        imformation as well.)

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
    def __init__(self, number, *courses):
        self.number = number
        self._courses = {}

        for course in courses:
            self._courses[course.subject] = course
