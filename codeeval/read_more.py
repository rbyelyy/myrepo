# coding=utf-8

"""
CHALLENGE DESCRIPTION:

You are given a text. Write a program which outputs its lines according to the following rules:

If line length is ≤ 55 characters, print it without any changes.
If the line length is > 55 characters, change it as follows:
Trim the line to 40 characters.
If there are spaces ‘ ’ in the resulting string, trim it once again to the last space (the space should be trimmed too).
Add a string ‘... <Read More>’ to the end of the resulting string and print it.
INPUT SAMPLE:

The first argument is a file. The file contains a text.

Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Two1thousand1verses1is1a1great many1-1very,1very1great1many.
Tom's mouth watered for the apple, but he stuck to his work.

Amy Lawrence was proud and glad, and she...
Tom exhibited.
Amy Lawrence was proud and glad, and... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but... <Read More>
"""

import sys


def read_from_file(path) -> list:
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [_.replace('\n', '') for _ in infile]


def return_lines(text_from_file):
    """
    Return text lines
    :rtype : object
    """
    return text_from_file


if __name__ == "__main__":
    text_from_file = read_from_file(sys.argv[1])
    for _ in text_from_file:
        if not len(_) > 55:
            print(_)
        else:
            trim_str = _[:40]
            get_space_char_index = trim_str.rfind(' ')
            if get_space_char_index == -1:
                print(trim_str + '... <Read More>')
            else:
                print(trim_str[:get_space_char_index].rstrip() + '... <Read More>')
