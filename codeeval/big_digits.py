# coding=utf-8
import sys


def read_from_file(path):
    """
    Sum of company_name_for_converting.txt in the file
    :rtype : object
    """

    with open(path, 'r') as infile:
        return [_ for _ in infile]


def convert_characters():
    """
    Sum of company_name_for_converting.txt in the file
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
    """
    Convert integer into 5*6 cli pixels
    :rtype : object
    """
    number_lines = []
    line_counter = ''
    for line in convert_characters():
        for slice_position in str_of_numbers:
            slice_position = int(slice_position)
            line_counter += line[(((4 * (slice_position + 1)) + slice_position) - 4):(
                (4 * (slice_position + 1)) + slice_position)] + '-'
        number_lines.append(line_counter)
        line_counter = ''
    return number_lines


def prepare_data_from_file(path):
    """
    Read from file and format data
    :rtype : object
    :param path: Path to the file
    :return: Filtered and formatted data from file
    """
    tmp_formatted_number = []
    content_of_file = read_from_file(path)
    for k, v in enumerate(content_of_file):
        content_of_file[k] = v[:-1]
        for _ in v:
            if '\n' not in _:
                tmp_formatted_number.append(int(i))
            else:
                tmp_formatted_number.append(i)

    return tmp_formatted_number


if __name__ == "__main__":
    file_content = read_from_file(sys.argv[1])
    for i in file_content:
        i = i.translate(None, '"\'>+-.:\n')
        for digit in convert_to_big_digit(i):
            assert isinstance(digit, str)
            print digit
