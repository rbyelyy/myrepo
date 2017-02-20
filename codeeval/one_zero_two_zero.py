# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
            ll.append([int(i) for i in _.strip().split(' ')])
        return ll


def find_number_zero(input_number):
    """
    Our agent uncovered a global criminal money-laundering network that used offshore companies to defraud international
    organizations of total $1,000,000,000! The agent changes his location each hour, but he manages to send us the code
    that we need to decipher.
    Deciphering code includes many stages, and you are taking part in one of them. Therefore, your task is the
    following: you have two numbers – the first one is the number of zeros in a binary code and the second one shows
    the range from 1 to this number, where you have to find these zeros.
    For example, for the given numbers 2 and 4, you convert all numbers from 1 to 4 inclusive into the binary system.
    As a result, you get 1, 10, 11, and 100. As the first given number is 2, this means that we are looking for
    numbers with two zeros, so only 100 suits us. Hence, the result will be 1: there is only one number with two zeros.
    :param input_number:
    :return: int
    """
    return len([_ for _ in map(bin, range(1, input_number[1] + 1)) if str(_)[2:].count('0') == input_number[0]])


if __name__ == "__main__":
    ll = read_from_file(sys.argv[1])
    for _ in ll:
        print(find_number_zero(_))
