import StringIO
import unittest

import vobject

import merge


LONDON_TIMEZONE = """BEGIN:VCALENDAR
PRODID:-//God//Human beta//EN
VERSION:2.0
BEGIN:VTIMEZONE
TZID:Europe/London
BEGIN:DAYLIGHT
TZOFFSETFROM:+0000
TZOFFSETTO:+0100
TZNAME:BST
DTSTART:19810329T010000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0100
TZOFFSETTO:+0000
TZNAME:GMT
DTSTART:19961027T020000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE
END:VCALENDAR
"""


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.cal = vobject.iCalendar()

    def test_merge_event(self):
        cal2 = vobject.iCalendar()
        cal2.add('vevent')
        cal2.vevent.add('summary').value = "Test"
        merge.merge_events(self.cal, cal2)
        self.assertEqual(self.cal.vevent_list, cal2.vevent_list)

    def test_merge_timezone(self):
        cal2 = vobject.readOne(StringIO.StringIO(LONDON_TIMEZONE))
        merge.merge_timezones(self.cal, cal2)
        self.assertEqual(self.cal.vtimezone.tzid.value, "Europe/London")
