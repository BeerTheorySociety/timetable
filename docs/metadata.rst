Metadata Architecture
=====================

This page defines the metadata format for each object in
the ```timetable``` package. This format will remain constant even if
the API changes drastically. This ensures backwards compatibility

Course
------
::

    {
        "id" : "COU000001",
        "name" : "Math 7",
        "description" : "",
        "instructor" : "",
        "period" : 1,
        "day" : "Monday",
        "time" : "9am"
    }

Student
-------
::

    {
        "id" : "STU000001",
        "name" : "Alice",
        "grade" : 7,
        "required" : [
            "Math 7",
            "English 8",
        ],
        "preferred" : [
            "Band",
            "Physical Education"
        ],
        ""
        "happiness" : 1.0,
        "schedule" : [
            {
                "id" : "COU000001",
                "name" : "Math 7",
                "description" : "",
                "instructor" : "",
                "period" : 1,
                "day" : "Monday",
                "time" : "9am"
            },
        ],
    }

CourseList
----------

StudentList
-----------
