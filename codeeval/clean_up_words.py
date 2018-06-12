# coding=utf-8

"""
CLEAN UP THE WORDS
CHALLENGE DESCRIPTION:

You have a list of words. Letters of these words are mixed with extra symbols, so it is hard to define the beginning and end of each word. Write a program that will clean up the words from extra numbers and symbols.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with a list of words: letters
are both lowercase and uppercase, and are mixed with extra symbols.

For example:



1
2
3
(--9Hello----World...--)
Can 0$9 ---you~
13What213are;11you-123+138doing7
OUTPUT SAMPLE:

Print the cleaned up words separated by spaces in lowercase letters.

For example:



1
2
3
hello world
can you
what are you doing
CONSTRAINTS:

Print the words separated by spaces in lowercase letters.
The length of a test case together with extra symbols can be in a range from 10 to 100 symbols.
The number of test cases is 40.
"""


def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [_.replace('\n', '') for _ in infile]


def remove_numbers(text_string):
    print(text_string)


if __name__ == "__main__":
    # text_from_file = read_from_file(sys.argv[1])
    # cleaned_lines = ([re.sub('[^a-zA-Z]+', ' ', i).strip().lower() for i in text_from_file])
    # for i in cleaned_lines:
    #     print(i)
    f = ['f', 'r']
    f.append(['4'])

    print(f)
