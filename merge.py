#!/usr/bin/python

from __future__ import print_function
from __future__ import unicode_literals

import argparse
import codecs
import sys

import vobject


def merge(filenames):
    combined_calendar = vobject.iCalendar()
    for filename in filenames:
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            toplevel = vobject.readOne(f)
            for item in toplevel.vevent_list:
                combined_calendar.add(item)
    return combined_calendar.serialize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source_ics_file', nargs='+')
    args = parser.parse_args()
    print(merge(args.source_ics_file), end='')
