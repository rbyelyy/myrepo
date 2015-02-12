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


def collect_big_digit(number_for_printing):
    collecting_tmp_var = []
    for line in convert_characters():
        collecting_tmp_var.append(line[(((4 * (number_for_printing + 1)) + number_for_printing) - 4):(
            (4 * (number_for_printing + 1)) + number_for_printing)] + '-')
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
        t = []
        t.append(collect_big_digit(3))
        t.append(collect_big_digit(6))
        t.append('\n')
        t.append(collect_big_digit(7))
        t.append(collect_big_digit(8))

        print t


        # for line in tmp_formated_number:
        # for m in convert_characters():
        #         for n in tmp_formated_number:
        #             if isinstance(n, int):
        #                 final_number += m[(((4 * (n + 1)) + n) - 4):((4 * (n + 1)) + n)] + '-'
        #         print final_number
        #         final_number = ''
        #     print '\n'





