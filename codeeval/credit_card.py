# coding=utf-8

"""
REAL FAKE
CHALLENGE DESCRIPTION:

The police caught a swindler with a big pile of credit cards. Some of them are stolen and some are fake.
 It would take too much time to determine which ones are real and which are fake, so you need to write a program
 to check credit cards.
To determine which credit cards are real, double every third number starting from the first one, add them together,
and then add them
to those figures that were not doubled. If the total sum of all numbers is divisible by 10 without remainder,
then this credit card is real.
"""


def read_from_file(path):
    """
    Read from file
    :param path: path to the file
    :rtype : object
    """
    with open(path, 'r') as infile:
        return [_.replace('\n', '') for _ in infile]


def retunr_cards(text_from_file):
    """
    Return text lines
    :rtype : object
    """
    return text_from_file


if __name__ == "__main__":
    text_from_file = read_from_file('t.txt')
    every_third_number = [sum([int(_) for _ in j]) * 2 for j in [list(_.replace(' ', '')[::2]) for _ in text_from_file]
                          if len(j) <= 16]
    every_second_number = [sum([int(_) for _ in j]) for j in [list(_.replace(' ', '')[1::2]) for _ in text_from_file]
                           if len(j) <= 16]
    credit_card_reminder_check = ([sum(_) % 10 for _ in zip(every_second_number, every_third_number)])
    for i in credit_card_reminder_check:
        if i == 0:
            print('Real')
        else:
            print('Fake')
