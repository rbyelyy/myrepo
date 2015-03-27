# coding=utf-8
import sys


def sum_of_numbers_in_file(path):
    """
    Sum of company_name_for_converting.txt in the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [int(i) for i in infile]


if __name__ == "__main__":
    assert sys.argv[1] is not None, "Please set the path to the file."
    print sum(sum_of_numbers_in_file(path=sys.argv[1]))