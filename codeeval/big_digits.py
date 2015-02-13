# coding=utf-8
import sys


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
    number_lines = []
    line_counter = ''
    for line in convert_characters():
        for slice_position in str_of_numbers:
            slice_position = int(slice_position)
            line_counter += line[(((4 * (slice_position + 1)) + slice_position) - 4):((4 * (slice_position + 1)) + slice_position)] + '-'
        number_lines.append(line_counter)
        line_counter = ''
    return number_lines


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
        file_content = read_from_file(sys.argv[1])
        for i in file_content:
            i = i.translate(None, '"\'-.:\n')
            for digit in convert_to_big_digit(i):
                    print digit







