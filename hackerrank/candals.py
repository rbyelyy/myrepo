# -*- coding: utf-8 -*-
"""
You are in-charge of the cake for your niece's birthday and have decided the cake
will have one candle for each year of her total age. When she blows out the candles,
she’ll only be able to blow out the tallest ones. Your task is to find out how many candles
she can successfully blow out.

For example, if your niece is turning  years old, and the cake will have  candles of height , , , , she
will be able to blow out candles successfully, since the tallest candle is of height  and there are  such candles.

Complete the function birthdayCakeCandles that takes your niece's age and an integer array containing
height of each candle as input, and return the number of candles she can successfully blow out.
"""
from __future__ import print_function

import os


#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(ar):
    ar.sort(reverse=True)
    return ar.count(ar[:1][0])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = (birthdayCakeCandles(ar))

    f.write(str(result) + '\n')

    f.close()
