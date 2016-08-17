"""
"""

from .handlers import ContainerHandler
from .people import Student

class StudentList(ContainerHandler):
    """ Container object with all Student Objects that need to fit a TimeTable
    object.
    """
    def __init__(self, *Students, **attrs):
        super(StudentList, self).__init__(*Students, **attrs)

    @property
    def students(self):
        """Get dictionary of Student objects. """
        return self._contents

    @property
    def _child_type(self):
        return Student

    def find(self, **kwargs):
        """Find students that fit a set of arguments"""
        pass
