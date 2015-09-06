# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys


def read_file():
    with open(sys.argv[1]) as fp:
        return fp.readlines()

if __name__ == "__main__":
    lines = filter(None, [i.replace('\n', '') for i in read_file()])

    for i in lines:
        print i.lower()
