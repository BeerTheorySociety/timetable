"""
"""

from .people import Student

class StudentList(object):
    """ Container object with all Student Objects that need to fit a TimeTable
    object.
    """
    @property
    def students(self):
        """Get dictionary of Student objects. """
        return self._contents

    def add(self, student):
        """Add Student object to StudentList.
        """
        self._assign_id(student)
        setattr(self, student.id, student)
        self._contents[student.id] = student

    @staticmethod
    def _check_type(item):
        """ Check that the item is a Student object.
        """
        if item.__class__ != "Student":
            raise Exception("""Argument must be a Student object!""")

    def _assign_id(self, student):
        """Assigns an `id` to a Student object.
        """
        # Check that argument is actually a Student object
        self._check_type(student)
        # If the Student doesn't already have an ID, give it one
        if hasattr(student, "id") is False:
            prefix = "STU"
            number = 0
            new_id = prefix + "%06d" % number
            while new_id in self._contents.keys():
                number += 1
                new_id = prefix + "%06d" % number
            self.student.add(id=new_id)
        # If ID exists in Student, check that it isn't in this object already
        else:
            if student.id in self._contents:
                raise Exception("""A Student object with the same ID already exists
                in the StudentList object.
                """)

    def rm(self, id):
        """Remove Student with `id` from timetable.
        """
        delattr(self, id)
        del self._contents[id]
