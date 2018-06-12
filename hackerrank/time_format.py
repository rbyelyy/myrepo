#!/bin/python
"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
"""
from __future__ import print_function

# !/bin/python

from __future__ import print_function

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
