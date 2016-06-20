"""Main module for calculating
"""

class Schedule(object):
    """

    schedule = {
        "name" : "schedule1",
        "periods" : {
            1 : {
                "time" : "9AM",
                "courses" : ["English 7", "Math 8", ...]
            }
            2 : {
                "time" : "10AM"
                "courses"["English 6", "Math 6", ...]
            }
        }
        "course" : {
            "XX0" : {
                "instructor" : "Alice"
                "students" : ["Bob", "Charles", ...]
            },
            "XX1" : {
                "instructor" : "Phil",
                "students" : ["Loni", ...]
            },
            ...,
        },
        "instructors" : {
            "ZZ0" : {
                "name" : "Bob",
                ""
            }


        }
        "students" : {
            "YY0" : {
                "name" : "Alice",
                "required" : [...]
                "desired" : [...]
            },

        }



        "days" : {
            "Monday" : {
                1 : {
                    "time" : "9AM",
                    "courses" : [{
                        "period" : 1,
                        "teacher" : "Bob",
                        "subject" : "Math",
                        "students" : ["Alice", "Charles", ...]
                        },
                        {
                        "period" : 1,
                        "teacher" : "Alice",
                        "subject" : "Science",
                        "students" : ["Alice", "Charles", ...]
                        }, ...]
                    },
                "period2" : {

                    }
            },
            "Tuesday" : {

            }
        }
    }
    """
    def __init__(self, *days):
        self.


    def add(self)
