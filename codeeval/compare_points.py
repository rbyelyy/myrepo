# coding=utf-8
import sys

def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        f = infile.readlines()
        stripped = [i.strip() for i in f]
        print stripped
        return stripped


def compare_points(positions):
    """
    Convert from positions to directions
    """
    if positions:
        for i in positions:
            i = i.split()
            try:
                i = [int(j) for j in i]
            except ValueError:
                exit("Cannot convert to Int")
            if -10000 < (i[0] and i[1] and i[2] and i[3]) < 10000:
                if i[0] == i[2] and i[1] == i[3]:
                    print 'here'
                elif i[0] == i[2]:
                    if i[1] < i[3]:
                        print 'N'
                    else:
                        print 'S'
                elif i[1] == i[3]:
                    if i[0] < i[2]:
                        print 'E'
                    else:
                        print 'W'
                else:
                    if int(i[0]) > int(i[2]):
                        x = 'W'
                    else:
                        x = 'E'
                    if int(i[1]) > int(i[3]):
                        y = 'S'
                    else:
                        y = 'N'
                    print str(y) + str(x)


if __name__ == "__main__":
    list_of_words = read_from_file(sys.argv[1])
    compare_points(list_of_words)
