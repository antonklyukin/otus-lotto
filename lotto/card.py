#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class Barrel:
    __number = int()

    def __init__(self, number=None):
        if not number:
            self.__number == random.randint(1, 90)
        else:
            self.__number = number

    @staticmethod
    def generate_list_of_barrels():
        number_list = [x for x in range(0, 90)]
        random.shuffle(number_list)
        list_of_barrels = [Barrel(number) for number in number_list]

        return list_of_barrels

    @property
    def number(self):
        return self.__number

    def __repr__(self):
        return str(self.__number)

    def __str__(self):
        return str(self.__number)


class Card:
    __number_of_non_zero_numbers_in_row = 5
    __number_of_rows = 3
    __number_or_columns = 9

    __card_by_row = []

    def __init__(self):
        self.__card_by_row = self.generate()

    def generate(self):
        # Формируем список списков(колонок) карточки
        card_by_column = [[] for element in range(9)]

        # Заполняем колонки карточки уникальными цифрами поразрядно
        for column_number in range(self.__number_or_columns):
            left_border, right_border = Card.get_range_borders_list_by_column(column_number)
            card_by_column[column_number] = Card.get_unique_numbers_list(left_border, right_border,
                                                                         self.__number_of_rows)

        # Преобразуем список по колонкам в список по строкам
        card_by_row = list(zip(*card_by_column))

        # Разрежаем нулями строки карточки
        card_by_row = [
            Card.discharge_row(list(row), self.__number_or_columns, self.__number_of_non_zero_numbers_in_row) for row
            in card_by_row]

        return card_by_row

    def is_in_card(self, barrel: Barrel):
        # Стоит ли бочонок с таким номером на карте?
        in_card = False
        card = self.__card_by_row
        for row in card:
            for element in row:
                if element == barrel.number:
                    in_card = True
                    break
            if in_card:
                break
        return in_card

    def cross_number(self, barrel: Barrel):
        # Поставить бочонок (зачеркнуть цифру)
        number_is_crossed = False
        for i, row in enumerate(self.__card_by_row):
            for j, element in enumerate(row):
                if element == barrel.number:
                    self.__card_by_row[i][j] = -1
                    number_is_crossed = True
                    break
            if number_is_crossed:
                break

    def all_numbers_are_crossed(self):
        # Вся карточка заполнена?
        crossed_numbers_counter = 0
        for i, row in enumerate(self.__card_by_row):
            for j, element in enumerate(row):
                if element == -1:
                    crossed_numbers_counter += 1
        if crossed_numbers_counter == 15:
            return True
        else:
            return False

    def count_crossed_numbers(self):
        crossed_numbers_counter = 0
        for i, row in enumerate(self.__card_by_row):
            for j, element in enumerate(row):
                if element == -1:
                    crossed_numbers_counter += 1
        return crossed_numbers_counter

    def print(self):

        card = self.__card_by_row

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

    @property
    def row(self):
        return self.__card_by_row

    @row.setter
    def row(self, new_card_by_row):
        self.__card_by_row = new_card_by_row

    @staticmethod
    def get_unique_numbers_list(left_border, right_border, required_count_of_numbers):
        unique_numbers_list = set()
        while len(unique_numbers_list) < required_count_of_numbers:
            unique_numbers_list.add(random.randint(left_border, right_border))
        return list(unique_numbers_list)

    @staticmethod
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

    @staticmethod
    def discharge_row(row, number_of_columns, number_of_non_zero_numbers_in_row):
        number_of_zeroes_in_row = number_of_columns - number_of_non_zero_numbers_in_row
        set_of_zero_positions = set()
        while len(set_of_zero_positions) != number_of_zeroes_in_row:
            column = random.randint(0, 8)
            set_of_zero_positions.add(column)

        for position in set_of_zero_positions:
            row[position] = 0

        return row


if __name__ == '__main__':
    my_list = Barrel.generate_list_of_barrels()
    print(my_list)
