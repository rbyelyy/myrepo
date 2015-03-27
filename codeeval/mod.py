# coding=utf-8
import sys
a = 22
q = 2
b = 5


def read_from_file(path):
    """
    Sum of company_name_for_converting.txt in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


def recursion_get_mod(n, m):
    """
    Recursion till n >= m
    :rtype : object
    """
    assert isinstance(n, int)
    assert isinstance(m, int)
    assert n is not 0
    n -= m
    if n >= m:
        n = recursion_get_mod(n, m)
    return n


def handle_elements(n, m):
    """
    Handle case when n < m
    :param n: integer
    :param m: integer
    :return: integer
    """
    assert isinstance(n, int)
    assert isinstance(m, int)
    if n < m:
        return n
    else:
        return recursion_get_mod(n, m)


if __name__ == "__main__":
    file_content = read_from_file(sys.argv[1])
    for i in file_content:
        i = i.translate(None, '\n').split(',')
        print handle_elements(int(i[0]), int(i[1]))


