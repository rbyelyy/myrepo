# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import Counter
import sys


def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    ll = []
    with open(path, 'r') as infile:
        for _ in infile:
            ll.append([int(i) for i in _.strip().split(',')])
        return ll


def get_major(input_list):
    # first dict element is number and second is occupancy
    max_occurrence = Counter(input_list).most_common(1)[0]
    if max_occurrence[1] >= len(input_list) / 2:
        return max_occurrence[0]
    else:
        return None

if __name__ == "__main__":
    ll = read_from_file(sys.argv[1])
    if len(ll) <= 40:
        for _ in ll:
            print(get_major(_))
