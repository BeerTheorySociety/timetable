import nose.tools as tools
import timetable as tt

class TestTimeTable():

    def setUp(self):
        self.timetable = tt.TimeTable()

    def test_add_bad_item(self):
        """Tests whether adding a bad item to TimeTable object raises exception."""
        not_a_day = tt.period.Period("9am")
        tools.assert_raises(Exception, self.timetable.add, time=not_a_day)

    def test_add(self):
        """Test that adding a Day to Timetable checks out."""
        day = tt.day.Day(name="Monday")
        self.timetable.add(day)
        tools.assert_equal(len(self.timetable.contents), 1)
