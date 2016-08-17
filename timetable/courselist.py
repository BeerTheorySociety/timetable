
from .handlers import ContainerHandler
from .course import Course

class CourseList(ContainerHandler):
    """ Container object for a set of Courses.
    """
    def __init__(self, *Courses, **attrs):
        super(CourseList, self).__init__(*Courses, **attrs)

    @property
    def courses(self):
        """Get dictionary of Student objects. """
        return self._contents

    @property
    def _child_type(self):
        return Course
