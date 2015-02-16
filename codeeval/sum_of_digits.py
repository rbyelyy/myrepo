# coding=utf-8
import sys
a = 22
q = 2
b = 5


def read_from_file(path):
    """
    Sum of numbers in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


def sum_of_digits(n):
    k = len(n[0])
    try:
        number = int(n[0])
    except (ValueError, TypeError):
        print 'Value in file is not numeric'
    total_sum = 0
    while k != 0:
        total_sum += number % 10
        number //= 10
        k -= 1
    return total_sum


if __name__ == "__main__":
    file_content = read_from_file(sys.argv[1])
    for i in file_content:
        i = i.translate(None, '\n').split(',')
        print sum_of_digits(i)


