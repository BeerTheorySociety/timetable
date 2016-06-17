class Day(object):
    """Day object for managing all periods in day.

    Metadata
    --------
    day = {
        "name" : "Monday",
        "periods" : {
            1 : "9AM",
            2 : "10AM",
            ...
        }
    }
    """
    def __init__(self, name, *periods):
        self._periods = {}
        for period in periods:
            self.add(period)

    def add(self, period):
        """Add period to day.
        """
        self._periods[period.number] = period
        setattr(self, period.number, period)

    def rm(self, period):
        """Remove period from day.
        """
        del self._period[period.number]
        delattr(self, period.number)
