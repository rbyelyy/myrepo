# coding=utf-8
import sys
import collections

def read_from_file(path):
    """
    Sum of numbers in the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [i for i in infile]

def convert_characters():
    """
    Sum of numbers in the file
    :rtype : object
    """
    digits_set = [
        '-**----*--***--***---*---****--**--****--**---**-B',
        '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
        '*--*---*---**---**--****-***--***----*---**---***-',
        '*--*---*--*-------*----*----*-*--*--*---*--*----*-',
        '-**---***-****-***-----*-***---**---*----**---**--',
        '--------------------------------------------------'
    ]
    return digits_set


if __name__ == "__main__":
    a = []
    b = read_from_file('/Users/rbyelly/Downloads/sandbox/myrepo/codeeval/numbers')
    for i in b:
        for j in str(i):
            a.append(int(j))

    for n in a:
        for m in convert_characters():
            print m[(((4 * (n + 1)) + n) - 4):((4 * (n + 1)) + n)]




