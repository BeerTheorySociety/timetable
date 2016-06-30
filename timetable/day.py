from .period import Period

class Day(object):
    """Day object for managing all periods in day.

    Metadata
    --------
    day = {
        "name" : "Monday",
        "periods" : {
            "PER0000001" : "9AM",
            2 : "10AM",
            ...
        }
    }
    """
    def __init__(self, name, *Periods):
        self._contents = {}
        for Period in Periods:
            self.add(period)

    @property
    def periods(selfs):
        """Get periods in day.
        """
        return self._contents

    @staticmethod
    def _check_type(item):
        """ Check that the item is a Period object.
        """
        if item.__class__ != "Period":
            raise Exception("""Argument must be a Period object!""")

    def _assign_id(self, period):
        """Assigns an `id` to a Period object.
        """
        # Check that argument is actually a Day object
        self._check_type(period)
        # If the day doesn't already have an ID, give it one
        if hasattr(day, "id") is False:
            prefix = "PER"
            number = 0
            new_id = prefix + "%06d" % number
            while new_id in self._contents.keys():
                number += 1
                new_id = prefix + "%06d" % number
            self.period.add(id=new_id)
        # If ID exists in day, check that it isn't in this object already
        else:
            if period.id in self._contents:
                raise Exception("""A Day object with the same ID already exists
                in the timetable object.
                """)

    def add(self, period):
        """Add period to day.
        """
        self._assign_id(period)
        self._contents[period.number] = period
        setattr(self, period.number, period)

    def rm(self, id):
        """Remove period from day.
        """
        del self._contents[id]
        delattr(self, id)
