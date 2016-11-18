# coding=utf-8
import urllib2
import re
import csv
import os
import sys


def download_nasdaq_company_list(file_name, url):
    """
    Download file with up to date NASDAQ company names 
    """
    response = urllib2.urlopen(url)
    with open(file_name, 'w') as f:
        f.write(response.read())


def get_dirty_company_list(file_name):
    """
    Read 'dirty' company names from file into list
    """
    with open(file_name, 'r') as f:
        return f.readlines()


def levenshtein(word_one, word_two):
    """
    Figure out difference between two sequences. (Based on 'Levenshtein distance')
    """
    if len(word_one) < len(word_two):
        return levenshtein(word_two, word_one)

    # len(word_one) >= len(word_one)
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


def hamming_distance(word_one, word_two):
    """Return the Hamming distance between equal-length sequences"""
    if len(word_one) != len(word_two):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(word_one, word_two))


def convert_nasdaq_data_to_dict(file_name):
    """
    Convert company name and ticker from NASDAQ file into dict
    """
    res = {}
    with open(file_name, 'r') as f:
        for line in f:
            sliced_data = re.split(' - |\|', line)[:2]
            if isinstance(sliced_data[1], str) and sliced_data[1] is not None:
                res[sliced_data[0]] = sliced_data[1]
        return res


def clean_up_string(str):
    """
    Remove all non alphabetic and numeric chars from the string. Make string lowercase.
    """
    str = str.lower()
    str = re.sub(r'\W+', '', str)
    return str


def create_clean_csv(mydict):
    """
    Create CSV file with company name and tickers 
    """
    writer = csv.writer(open('create_clean_csv.csv', 'wb'))
    for key, value in mydict.items():
        writer.writerow([key, value])


def delete_tmp_file():
    """
    Delete tmp files (NASDAQ)
    """
    os.remove('company_name_from_nasdaq')


if __name__ == "__main__":
    nasdaq_url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
    nasdaq_file_name = 'company_name_from_nasdaq'

    dirty_file_name = 'company_name_for_converting'
    result = {}
    ticker_and_company = {}

    # Download and clean up data from NASDAQ
    download_nasdaq_company_list(nasdaq_file_name, nasdaq_url)
    get_company_tickers_from_nasdaq = convert_nasdaq_data_to_dict(nasdaq_file_name)

    # Get dirty company names
    company_list_for_covert = get_dirty_company_list(dirty_file_name)

    for dirty_company_name in company_list_for_covert:
        dirty_company_name = clean_up_string(dirty_company_name)
        for key, value in get_company_tickers_from_nasdaq.items():
            value = clean_up_string(value)

            # Hamming algorithm
            if len(dirty_company_name) == len(value):
                f = hamming_distance(dirty_company_name, value)
                if f < 4:
                    ticker_and_company[key] = f
                    break
            else:
                # Leventstein algorithm
                f = levenshtein(dirty_company_name, value)
                ticker_and_company[key] = f
                if f < 3:
                    break

        min_val = min(ticker_and_company.itervalues())
        ticker = [k for k, v in ticker_and_company.iteritems() if v == min_val]
        result[ticker[0]] = get_company_tickers_from_nasdaq[ticker[0]]
        create_clean_csv(result)
    delete_tmp_file()








