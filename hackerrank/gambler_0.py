#!/bin/python
"""
Описание ПО Gambler1.0
Приложение должно работать на ОС Windows 10+ 64.
По запросу клиента приложение генерирует бросок стандартных шестигранных кубиков (от одного до пяти кубиков).
??Данные о количестве бросков, минимальном и максимальном количестве кубиков клиент вводит в качестве аргументов
??при запуске программы.
Приложение выводит в консоль выпавшие грани на кубиках и подсчитывает результат броска.
При подсчете порядок следования кубиков не учитывается.
Значащие грани: 1 и 5. 1 - соответствует 10 очкам, 5 - соответствует 5 очкам.
Все остальные грани не приносят очков (2,3,4,6).
Исключение - специальная комбинация: 1,2,3,4,5 = 150 очков

Примеры запуска программы:

$ ./gambler_1 5
Программа выполнит 5 бросков кубиков.


Примеры вычисления набранных очков:

1,1,5 = 25
2,4,6,6 = 0
5,1,3,5 = 20

Задача тестировщика:
1) Выявить максимально возможное количество ошибок в ПО
2) Автоматизировать процесс тестирования (финальная проверка автоматизации будет осуществляться на версии, которой нет
в приложенных файлах: gambler_3)
3) Версию gambler_0 - можно считать эталонной, остальные версии могут содержать ошибки.
"""

from __future__ import print_function

import platform
from random import randint
from typing import List


#
# Gambler emulator
#
def dices(number_throughs=None):
    thoughs = []

    try:
        if number_throughs is None:
            for i in range(randint(1, 5)):
                thoughs.append(randint(1, 6))
        else:
            if number_throughs not in range(1, 6):
                exit("Out of dice range.")
            for i in range(number_throughs):
                thoughs.append(randint(1, 6))
        return thoughs
    except TypeError:
        print("Please use Int as a type of arguments.")


def calculation(results: List[int]) -> int:
    """
    Return calculation of score for dices
    :return: results for dices calculations
    :param results: list[int]
    :rtype: int
    """
    scores = 0
    for i in results:
        if i == 1:
            scores += 10
        elif i == 5:
            scores += 5
        if results == [1, 2, 3, 4, 5]:
            scores += 150
    return scores


if __name__ == '__main__':
    if not platform.system() == 'Windows':
        print(calculation(dices(5)))
