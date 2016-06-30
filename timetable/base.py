__doc__ = """
Base module for TimeTable package.
"""

CONTENTS = {
    "TimeTable" : "Day",
    "Day" : "Period",
    "Period" : "Course",
    "Course" : "Instructor",
    "StudentList" : "Student"
}

PREFIX = {
    "Day" : "DAY",
    "Period" : "PER",
    "Course" : "COU",
    "Student" : "STU",
    "Instructor" : "INS"
}

def BaseHandler(object):
    """ Object that manages atttribute data.
    """
    def __init__(self, **attrs):
        self._attrs = {}
        self.addattr(**attrs)

    def addattr(self, **attrs):
        """ Add attribute to Handler
        """
        for key, value in attrs.items():
            self._attrs[key] = value
            setattr(self, key, value)

    def rmattr(self, *attrs):
        """ Remove attribute from Handler.
        """
        for attribute in attrs:
            del self._attrs[attribute]
            delattr(self, attribute)

class BaseContainerHandler(BaseHandler):
    """ Handler inherited by most objects in this package. Manages
    addition/removal of subobjects.
    """
    def __init__(self, *items, **attrs):
        super(BaseContainerHandler, self).__init__(**attrs)
        self._contents = {}
        self.add(*items)

    @property
    def _type_exception_message(self):
        return """And object already exists in contents with the same ID."""

    @staticmethod
    def _check_type(item):
        """ Check that the item is an expected object.
        """
        if item.__class__ != CONTENTS[self.__class__]:
            raise Exception("Argument must be a " + \
                CONTENTS[self.__class__]+ " object!")

    def _assign_id(self, prefix, item):
        """Assigns an `id` to object, with a given prefix.
        """
        # Check that argument is an expected object
        self._check_type(item)
        # If the object doesn't already have an ID, give it one
        if hasattr(item, "id") is False:
            number = 0
            new_id = prefix + "%06d" % number   # 9-character ID
            while new_id in self._contents.keys():
                number += 1
                new_id = prefix + "%06d" % number
            self.item.addattr(id=new_id)
        # If ID exists in object, check that it isn't in this object already
        else:
            if item.id in self._contents:
                raise Exception(self._type_exception_message)

    def add(self, item):
        """Add object to Handler.
        """
        self._assign_id(item)
        setattr(self, item.id, item)
        self._contents[item.id] = item

    def rm(self, id):
        """Remove object with `id` from Handler.
        """
        delattr(self, id)
        del self._contents[id]
