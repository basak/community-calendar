#!/usr/bin/python

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import codecs
import sys

import vobject


def merge_timezones(combined_calendar, calendar_with_timezones):
    for timezone_item in calendar_with_timezones.vtimezone_list:
        combined_calendar.add(timezone_item)


def merge_events(combined_calendar, calendar_with_events):
    for event_item in calendar_with_events.vevent_list:
        combined_calendar.add(event_item)


def merge(filenames, timezone_file):
    combined_calendar = vobject.iCalendar()

    with codecs.open(timezone_file, encoding='utf-8') as f:
        merge_timezones(combined_calendar, vobject.readOne(f))

    for filename in filenames:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            merge_events(combined_calendar, vobject.readOne(f))

    return combined_calendar.serialize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--timezone-file', default='timezones.ics')
    parser.add_argument('source_ics_file', nargs='+')
    args = parser.parse_args()
    print(
        merge(args.source_ics_file, timezone_file=args.timezone_file),
        end=''
        )
