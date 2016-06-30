"""
"""

from .base import BaseContainerHandler

class StudentList(BaseContainerHandler):
    """ Container object with all Student Objects that need to fit a TimeTable
    object.
    """
    def __init__(self, *Students, **attrs):
        super(StudentList, self).__init__(*Students, **attrs)

    @property
    def students(self):
        """Get dictionary of Student objects. """
        return self._contents
