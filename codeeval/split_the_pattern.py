# coding=utf-8
import sys

def read_from_file(path):
    """
    Sum of company_name_for_converting.txt in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


if __name__ == "__main__":
    file_content = read_from_file(sys.argv[1])
    for i in file_content:
        i = i.translate(None, '\n').split(' ')
        if '+' in i[1]:
            element_position = i[1].index('+')
            print int(i[0][element_position:]) + int(i[0][0:element_position])
        else:
            element_position = i[1].index('-')
            print int(i[0][0:element_position]) - int(i[0][element_position:])



