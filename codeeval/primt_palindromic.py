# coding=utf-8
import math


def is_primary_trivial_division(n):
    """
    Trial division algorithm for primary numbers
    Complexity: O(n1/2log2n)
    :param n: number for verification
    :return: primary if true and 0 if false
    """
    mod = int(math.sqrt(n))
    for _ in xrange(2, mod + 1):
        if n % _ == 0:
            return 0
    return n


def palindrome_number(n):
    """
    Check if number is PALINDROME
    :rtype : Boolean
    """
    n_list = map(int, str(n))
    n_half = len(n_list) / 2
    if n_half == 1:
        if n_list[-1:] == n_list[:1]:
            return True
        else:
            return False
    for k, v in enumerate(n_list):
        a = n_list[k]
        b = n_list[-(k + 1)]
        if b != a:
            return False
        if k > n_half:
            return True


if __name__ == "__main__":
    #trivial division
    i = 8
    division_numbers = [2, 3, 5, 7]
    while len(division_numbers) < 100:
        if is_primary_trivial_division(i) != 0:
            if palindrome_number(i):
                division_numbers.append(i)
        i += 1
    for key, value in enumerate(division_numbers):
        if value >= 1000:
            print division_numbers[key-1]
            break
