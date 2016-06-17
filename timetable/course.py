"""Module for managing course objects
"""
class Course(object):
    """ Course object. Holds all the information about

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
        "period" : 1,
        "teacher" : "Bob",
        "subject" : "Math",
        "students" : [
            "Alice",
            "Charles"
        ]
    }


    """
    def __init__(self, subject, teacher, period):
        self.teacher = teacher
        self.period = period
        self.subject = subject
        self._students = {}

    @property
    def size(self):
        """Get class size
        """
        return len(self._students)

    @property
    def names(self):
        """Return list of student names.
        """
        return list(self._students.keys())

    def add(self, student):
        """Add student to course.
        """
        self._students[student.name] = student

    def rm(self, student):
        """Remove student from course.
        """
        del self._students[student.name]
