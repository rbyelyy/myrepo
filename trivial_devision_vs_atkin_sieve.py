# coding=utf-8
import math
import itertools


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


def equation_level_calculation(element_x, element_y):
    """
    Apply equation to income values
    :type element_y: int
    """
    a = 4 * pow(element_x, 2) + pow(element_y, 2)
    b = 3 * pow(element_x, 2) + pow(element_y, 2)
    c = 3 * pow(element_x, 2) - pow(element_y, 2) if element_x > element_y else None
    return [a, b, c]


def create_pairs_of_numbers(n):
    """
    1. All prime from 1 to n
    2. Taking all possible numbers  x, y, where x<=sqrt(n) и y<=sqrt(n).Ex: (1,1), (1,2),…,
    (1,sqrt(n)), (2,1), (2,2),…, (sqrt(n),sqrt(n)).

    :rtype : list
    """
    x_y_limit = list(range(1, int(math.sqrt(n)) + 1))
    x_y_pairs = list(itertools.product(x_y_limit, repeat=2))
    return x_y_pairs


def pow_range(n):
    """
    On the last phase we are checking that prime number do not have mod 0 for pow(x,2)  for all numbers from
    5 до sqrt(n).
    :rtype : list
    """
    a = int(math.sqrt(n))
    return [pow(pow_from_5_to_sqrt_n, 2) for pow_from_5_to_sqrt_n in range(4, a + 1)
            if is_primary_trivial_division(pow_from_5_to_sqrt_n)]


def check_number_in_pow_range(number_for_checking, pow_range_list):
    for pow_i in pow_range_list:
        if number_for_checking % pow_i == 0:
            return True
    return False


def division_mod_twelve(result_of_equation, n):
    pow_range_list = pow_range(n)
    filtered_value = [False] * (n + 1)
    for three_digit_list in result_of_equation:
        for key, value in enumerate(three_digit_list):
            if value is not None:
                if key == 0 and value % 12 in (1, 5):
                    if not check_number_in_pow_range(value, pow_range_list) and value < n:
                        filtered_value[value] = not filtered_value[value]
                elif key == 1 and value % 12 == 7:
                    if not check_number_in_pow_range(value, pow_range_list) and value < n:
                        filtered_value[value] = not filtered_value[value]
                elif key == 2 and value % 12 == 11:
                    if not check_number_in_pow_range(value, pow_range_list) and value < n:
                        filtered_value[value] = not filtered_value[value]
    return filtered_value


def is_primary_atkin(n):
    """
    Implementation of Sieve of Atkin
    :rtype : list
    """
    primes = []
    x_y_pairs = create_pairs_of_numbers(n)
    result_of_applying_equation = [equation_level_calculation(pair[0], pair[1]) for pair in x_y_pairs]
    bool_prime = division_mod_twelve(result_of_applying_equation, n)

    for k, v in enumerate(bool_prime):
        if v:
            primes.append(k)
    return [2, 3] + primes


if __name__ == "__main__":
    # trivial division
    i = 8
    division_numbers = [2, 3, 5, 7]
    while len(division_numbers) < 1000:
        if is_primary_trivial_division(i) != 0:
            division_numbers.append(i)
        i += 1

    # atkin method
    print sum(division_numbers)
    print sum(is_primary_atkin(7920))




