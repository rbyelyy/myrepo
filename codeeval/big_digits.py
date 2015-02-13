# coding=utf-8
import sys
import collections
import re
import string


def read_from_file(path):
    """
    Sum of numbers in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


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


def convert_to_big_digit(str_of_numbers):
    collecting_tmp_var = []
    line_counter = ''
    for line in convert_characters():
        for i in str_of_numbers:
            i = i.translate(None, ' -.:')
            i = int(i)
            line_counter += line[(((4 * (i + 1)) + i) - 4):((4 * (i + 1)) + i)] + '-'
        collecting_tmp_var.append(line_counter)
        line_counter = ''
    return collecting_tmp_var


def prepare_data_from_file():
    tmp_formated_number = []
    file_content = read_from_file('/Users/rbyelly/Downloads/sandbox/myrepo/codeeval/numbers')
    for k, v in enumerate(file_content):
        file_content[k] = v[:-1]
        for i in v:
            if '\n' not in i:
                tmp_formated_number.append(int(i))
            else:
                tmp_formated_number.append(i)

    return tmp_formated_number

if __name__ == "__main__":

        file_content = read_from_file('/Users/rbyelly/Downloads/sandbox/myrepo/codeeval/numbers')
        for i in file_content:
            if '\n' in i:
                i = i[:-1]
            elif '-' or '.' or '_':
                i = i.translate(None, ' -.:')
            for k in convert_to_big_digit(i):
                    print k




        # for line in tmp_formated_number:
        # for m in convert_characters():
        #         for n in tmp_formated_number:
        #             if isinstance(n, int):
        #                 final_number += m[(((4 * (n + 1)) + n) - 4):((4 * (n + 1)) + n)] + '-'
        #         print final_number
        #         final_number = ''
        #     print '\n'





