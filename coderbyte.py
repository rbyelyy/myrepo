# coding=utf-8
import string


def FirstReverse(str):
    """
    Reversing string
    :param str: get the string as argument
    :return: reversed string
    """
    y = ''
    count = len(str) - 1
    while count >= 0:
        y = y + str[count]
        count -= 1
    str = y
    return str


def FirstFactorial(num):
    """
    Calculating factorial of the number
    :param num: Integer value
    :return: Calculated factorial of recived number
    """
    if num >= 1:
        return num * FirstFactorial(num - 1)
    else:
        return 1


def LongestWord(sent):
    """
    Calculating longest word in the string
    :param sent: string
    :return: longest word in the string
    """
    words = string.split(sent)
    max_count = 0
    for x in words:
        x = string.strip(string.strip(x, ":/["), '~!')

        if len(x) > max_count:
            max_count = len(x)
            max_word = x
    return max_word


def Equilibrium(A):
    """
    Equilibrium index of a sequence
    :param A: List of integers
    :return: Integer equilibrium index
    """
    summa = sum(A)
    leftsumma = 0
    rightsumma = 0
    previous_item = 0
    ind = []
    for index, value in enumerate(A):
        if index == 0:
            rightsumma = summa - value
            if value == rightsumma:
                ind.append(index)
        else:
            leftsumma = leftsumma + previous_item
            rightsumma = rightsumma - value
            if leftsumma == rightsumma:
                ind.append(index)
        previous_item = value
    if len(ind) == 0:
        return -1
    else:
        return int(ind[0])


def buble_sorting(A):
    """
    Sorting of sequence using buble methods
    :param A: List of integers
    """
    x = 0
    for index, value in enumerate(A):
        if index < len(A) - 1:
            if A[index] > A[index + 1]:
                tmp = A[index]
                A[index] = A[index + 1]
                A[index + 1] = tmp
                x += 1
    if x > 0:
        buble_sorting(A)
    return A


def find_max_occurance(A):
    """
    Defining value with maximum number of occurrence in sorted sequence
    :param A: List of integers
    """
    max_item_value = 0
    max_item = 0
    tmp_item_value = 0
    for index, value in enumerate(A):
        if index == 0:
            tmp_item = A[index]
            tmp_item_value += 1
        else:
            if A[index] == tmp_item:
                tmp_item_value += 1
            else:
                if tmp_item_value > max_item_value:
                    max_item_value = tmp_item_value
                    max_item = tmp_item
                    tmp_item_value = 1
                    tmp_item = A[index]
    print max_item, "width", max_item_value


def brace_counting(A):
    """
    Calculating number of closed  / unclosed braces
    :param A: String with braces
    """
    a = 0
    b = 0
    for x in A:
        if x == ')':
            a += 1
        elif x == '(':
            b += 1
    if a > b:
        print ') more then ( on', a - b
    elif a < b:
        print '( more then ) on', b - a
    else:
        print 'brackets are closed'


def absolutly_distinct_elements(A):
    """
    Calculating number of absolutely distinct elements in the sequence
    :param A: Integer sequence
    """
    el_number = 0
    for index, value in enumerate(A):
        if index == 0:
            tmp_el = abs(A[index])
            el_number += 1
        else:
            if abs(A[index]) != tmp_el:
                el_number += 1
                tmp_el = abs(A[index])
    print el_number


def find_max_distance_between_non_zero_elements(A):
    """
    Calculating maximum distance between any of element in the sequence
    :param A: sequence of integer numbers
    :return: max distance between any element in sequence
    """
    A.sort()
    min_el = min(A)
    max_el = max(A)

    if min_el == 0:
        A.remove(min_el)
        find_max_distance_between_non_zero_elements(A)
    elif max_el == 0:
        A.remove(max_el)
        max_distance = find_max_distance_between_non_zero_elements(A)
        return max_distance
    max_distance = max_el - min_el
    return max_distance


def find_max_distance_between_closest_elements(A):
    """
    Defininf maximum distance between two closest elements in the sequence
    :param A:
    :return: Maximum distance between tow non zero elements in sequence
    """
    A.sort()
    length = len(A) - 1
    for index, value in enumerate(A):
        if index == 0:
            if A[index] or A[index+1] < 0:
                max_distace = abs(A[0] - A[1])
            else:
                max_distace = abs(abs(A[0]) - abs(A[1]))
        else:
            if index != length:
                tmp_max_distance = abs(A[index] - A[index+1])
                if max_distace < (tmp_max_distance):
                    max_distace = tmp_max_distance
            else:
                return max_distace


def falling_discs(A, B):
    """
    Write a function: int falling_disks(int A[], int N, int B[], int M); that, given two zero-indexed arrays of
    integers − A. containing the internal diameters of the N rings (in top-down order), and B, containing
    the diameters of the M disks (in the order they are to be dropped) − returns the number of disks that will fit
    into the well. For example, given the following two arrays
    :param A: Sequence of cycles in well
    :param B: Sequence of disks
    :return: Number of disks which are fit into well
    """
    length = len(A) - 1
    number_of_disc = len(B) -1
    for index, value in enumerate(A):
        if index != length:
            if A[index] < A[index + 1]:
                A[index + 1] = A[index]
    A.reverse()
    print A
    j = 0
    for index, value in enumerate(A):
        if A[index] >= B[j]:
            if j == number_of_disc:
                j += 1
                return j
            j += 1
    return j


def Fibonachi(A):
    if A == 0:
        return 0
    if A == 1:
        return 1
    return Fibonachi(A-1) + Fibonachi(A-2)


def is_prime(num):
    for j in range(2, num):
        if (num % j) == 0:
            return False
    return True


def fibonachi_power(N, M):
    """
    The Fibonacci sequence is defined by the following recursive formula:
    :param N:
    :param M:
    :return: integer
    """
    x = N**M
    return Fibonachi(x)


def covered_index ( A ):
    """
    A non-empty zero-indexed array A consisting of N integers is given. The first covering prefix of array A is the
    smallest integer P such that 0 ≤ P < N and such that every value that occurs in array A also occurs
    in sequence A[0], A[1], ..., A[P].

    For example, the first covering prefix of the following 5−element array A:

    A[0] = 2  A[1] = 2  A[2] = 1
    A[3] = 0  A[4] = 1
    is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0], contains all values that occur in array A.
    :param A: list of values
    :return: index number which cover all unique digits
    """
    N = len(A)
    if N == 0: return -1
    bit = {}
    for i in range(N):
        if not A[i] in bit.keys():
            bit[A[i]] = 1
            P = i
    return P


def merge(left, right):
    """
    Merging to lists
    :param left: Left part of list
    :param right: Right part of list
    :return: Combined list
    """
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def pair_sum_even_count(A):
    """
    Lets say you have array A[0]=1 A[1]=-1 ....A[n]=x
    Then what would be the smartest way to find out the number of times when A[i]+A[j] is even where i < j

    So if we have {1,2,3,4,5} we have 1+3 1+5 2+4 3+5 = 4 pairs which are even
    :param A: Arranged sequence of integers
    :return: Amount of sums (odd, even) in sequence
    """
    sum = 0
    odd = 0
    even = 0
    for index, values in enumerate(A):
        if A[index] % 2 == 0:
            sum += even
            even += 1
        else:
            sum += odd
            odd += 1
    return sum


def dominator(A):
    max_count = 0
    tmp_max_count = 0
    A.sort()
    length = len(A) - 1
    for index, value in enumerate(A):
        if index + 1 == length:
            tmp_max_count += 2
            if tmp_max_count > max_count:
                max_count = tmp_max_count
            x = max_count/float(length)
            y = x*100
            if y >= 50:
                return y
            else: return -1
        if A[index] == A[index + 1]:
            tmp_max_count += 1
        else:
            tmp_max_count += 1
            if tmp_max_count > max_count:
                max_count = tmp_max_count
            tmp_max_count = 0



x = "{}}{}{))jfksdjfdk((((("

s = list(x)
ls = [-5, -5, -10, -200, -210, 0, 0, 0]

A = [123, 234, 567, 5, 6, 4, 3, 6, 2, 3]
A1 = [2,2,1,0,1,4,4,6]
A2 = [1,2,7,7,7]
B = [2, 2, 2, 2, 2, 2,2,2,2]

print dominator(A2)
