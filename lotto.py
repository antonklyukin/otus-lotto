#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def get_barrel():
    return random.randint(1, 90)


def fill_card():
    number_of_non_zero_numbers_in_row = 5
    number_of_rows = 3
    number_or_columns = 9

    card_by_column = [[] for element in range(9)]

    for column_number in range(number_or_columns):
        left_border, right_border = get_range_borders_list_by_column(column_number)
        card_by_column[column_number] = get_unique_numbers_list(left_border, right_border, number_of_rows)

    card_by_row = list(zip(*card_by_column))

    discharged_card_by_row = [discharge_row(list(row), number_or_columns, number_of_non_zero_numbers_in_row) for row in
                              card_by_row]

    return discharged_card_by_row


def get_unique_numbers_list(left_border, right_border, required_count_of_numbers):
    unique_numbers_list = set()
    while len(unique_numbers_list) < required_count_of_numbers:
        unique_numbers_list.add(random.randint(left_border, right_border))
    return list(unique_numbers_list)


def get_range_borders_list_by_column(column):
    range_borders_tuple = tuple()
    if column == 0:
        range_borders_tuple = (1, 9)
    if column == 1:
        range_borders_tuple = (10, 19)
    if column == 2:
        range_borders_tuple = (20, 29)
    if column == 3:
        range_borders_tuple = (30, 39)
    if column == 4:
        range_borders_tuple = (40, 49)
    if column == 5:
        range_borders_tuple = (50, 59)
    if column == 6:
        range_borders_tuple = (60, 69)
    if column == 7:
        range_borders_tuple = (70, 79)
    if column == 8:
        range_borders_tuple = (80, 90)

    return range_borders_tuple


def discharge_row(row, number_of_columns, number_of_non_zero_numbers_in_row):
    number_of_zeroes_in_row = number_of_columns - number_of_non_zero_numbers_in_row
    set_of_zero_positions = set()
    while len(set_of_zero_positions) != number_of_zeroes_in_row:
        column = random.randint(0, 8)
        set_of_zero_positions.add(column)

    for position in set_of_zero_positions:
        row[position] = 0

    return row


def draw_card(card):
    empty_number = 0
    crossed_number = -1

    delimiter = '--------------------------'
    printout = delimiter + '\n'

    for row_list in card:
        for number in row_list:
            if number == empty_number:
                printout += '  '
            elif number == crossed_number:
                printout += ' -'
            elif number < 10:
                printout += f' {str(number)}'
            else:
                printout += str(number)

            printout += ' '

        printout += '\n'

    print(printout + delimiter)


card = fill_card()

print(card)

draw_card(card)

# print(check_card_for_column_duplicates(card))
