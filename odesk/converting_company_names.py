# coding=utf-8
import urllib2
import re
import csv
import os
import sys


def download_nasdaq_company_list(file_name, url):
    response = urllib2.urlopen(url)
    with open(file_name, 'w') as f:
        f.write(response.read())


def get_dirty_company_list(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def levenshtein(word_one, word_two):
    if len(word_one) < len(word_two):
        return levenshtein(word_two, word_one)

    # len(s1) >= len(s2)
    if len(word_two) == 0:
        return len(word_one)

    previous_row = range(len(word_two) + 1)
    for i, c1 in enumerate(word_one):
        current_row = [i + 1]
        for j, c2 in enumerate(word_two):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def convert_data_to_dict(file_name):
    res = {}
    with open(file_name, 'r') as f:
        for line in f:
            sliced_data = re.split(' - |\|', line)[:2]
            if isinstance(sliced_data[1], str) and sliced_data[1] is not None:
                res[sliced_data[0]] = sliced_data[1]
        return res


def clean_up_string(str):
    str = str.lower()
    str = re.sub(r'\W+', '', str)
    return str


def create_clean_csv(mydict):
    writer = csv.writer(open('create_clean_csv.csv', 'wb'))
    for key, value in mydict.items():
        writer.writerow([key, value])


if __name__ == "__main__":
    result = {}
    ticker_and_company = {}
    download_nasdaq_company_list('company_name_from_nasdaq',
                                 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt')
    company_list_for_covert = get_dirty_company_list('company_name_for_converting')

    get_company_tickers_from_nasdaq = convert_data_to_dict('company_name_from_nasdaq')

    for dirty_company_name in company_list_for_covert:
        dirty_company_name = clean_up_string(dirty_company_name)
        for key, value in get_company_tickers_from_nasdaq.items():
            value = clean_up_string(value)
            f = levenshtein(dirty_company_name, value)
            ticker_and_company[key] = f
        min_val = min(ticker_and_company.itervalues())
        ticker = [k for k, v in ticker_and_company.iteritems() if v == min_val]
        result[ticker[0]] = get_company_tickers_from_nasdaq[ticker[0]]
        create_clean_csv(result)









