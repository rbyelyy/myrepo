# coding=utf-8
import sys


def read_from_file(path):
    """
    Sum of numbers in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


if __name__ == "__main__":
    file_content = read_from_file('/Users/rbyelly/Downloads/sandbox/myrepo/codeeval/numbers')
    matrix = [i.translate(None, '\n').split(',') for i in file_content]
    print matrix