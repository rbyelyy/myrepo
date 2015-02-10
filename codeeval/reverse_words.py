# coding=utf-8
import sys


def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [_.replace('\n', '').split(' ') for _ in infile]


def reverse_words(words_list):
    """
    Return reversed list of words
    :rtype : object
    """
    return [reversed(_) for _ in [_ for _ in words_list]]


if __name__ == "__main__":
    list_of_words = read_from_file(sys.argv[1])
    n = reverse_words(words_list=list_of_words)
    accumulation = ''
    for i in n:
        for j in i:
            accumulation += j + ' '
        print accumulation
        accumulation = ''

