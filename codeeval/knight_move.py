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
        return [i.rstrip() for i in f]


def knight_moves(positions):
    """
    Return movement of the knights
    :rt
    ype : object
    """
    elements_not_in_range = []
    knight_movement = []
    chars_for_movement = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    movement_prediction = {}
    for i in positions:
        l = list(i)

        # get all possible directions
        movement_prediction['d_up'] = str(int(l[1]) + 2)
        movement_prediction['d_down'] = str(int(l[1]) - 2)
        movement_prediction['c_up'] = chr(ord(l[0]) + 2)
        movement_prediction['c_down'] = chr(ord(l[0]) - 2)

        # get all possible movements codes
        if movement_prediction['c_up'] in chars_for_movement:
            knight_movement.append(movement_prediction['c_up'] + str(int(l[1])+1))
            knight_movement.append(movement_prediction['c_up'] + str(int(l[1])-1))
        if movement_prediction['c_down'] in chars_for_movement:
            knight_movement.append(movement_prediction['c_down'] + str(int(l[1])+1))
            knight_movement.append(movement_prediction['c_down'] + str(int(l[1])-1))
        if 1 <= int(movement_prediction['d_up']) <= 8:
            knight_movement.append(chr(ord(l[0]) - 1) + movement_prediction['d_up'])
            knight_movement.append(chr(ord(l[0]) + 1) + movement_prediction['d_up'])
        if 1 <= int(movement_prediction['d_down']) <= 8:
            knight_movement.append(chr(ord(l[0]) - 1) + movement_prediction['d_down'])
            knight_movement.append(chr(ord(l[0]) + 1) + movement_prediction['d_down'])

        # filter movements vs valid ranges
        for i in knight_movement:
            if i[0] not in chars_for_movement:
                elements_not_in_range.append(i)
            if not 1 <= int(i[1]) <= 8:
                elements_not_in_range.append(i)

        s_move =set(knight_movement)
        s_del = set(elements_not_in_range)

        print " ".join(str(x) for x in sorted(s_move.difference(s_del)))

        elements_not_in_range = []
        knight_movement = []

if __name__ == "__main__":
    list_of_words = read_from_file(sys.argv[1])
    knight_moves(list_of_words)

