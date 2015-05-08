# coding=utf-8
import sys
import itertools

def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        f = infile.readlines()
        return [i.rstrip(' ') for i in f]


def knight_moves(positions):
    """
    Return direction
    """
    a = None
    b = None
    for i in positions:
        line = i.replace(" ", "")
        if line[0] == line[2] and line[1] == line[3]:
            print 'here'
        elif line[0] == line[2]:
            if line[1] < line[3]:
                print 'N'
            else:
                print 'S'
        elif line[1] == line[3]:
            if line[0] < line[2]:
                print 'E'
            else:
                print 'W'
        else:
            if int(line[0]) > int(line[2]) :
                a = 'W'
            else:
                a = 'E'
            if int(line[1]) > int(line[3]):
                b = 'S'
            else:
                b = 'N'
        print a + b



if __name__ == "__main__":
    list_of_words = read_from_file('ttt.txt')
    knight_moves(list_of_words)

