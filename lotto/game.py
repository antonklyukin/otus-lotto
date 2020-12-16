#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from .card import Card, Barrel


class Player:
    __type = str()
    __name = str()
    __card = list()

    def __init__(self, player_type, player_name):
        self.__type = player_type
        self.__name = player_name
        self.__card = Card()

    @property
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def card(self):
        return self.__card


class Game:
    __barrels = Barrel.generate_list_of_barrels()
    __players = []
    __round = 0

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, new_players):
        self.__players = new_players

    @property
    def barrels(self):
        return self.__barrels

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, new_round):
        self.__round = new_round


    def __init__(self):
        print('Добро пожаловать в игру лото!')
        number_of_players = 0
        while True:
            print('_________________________________________')
            print(f'Количество игроков в игре (не более 6): {len(self.__players)}')
            print('_________________________________________')
            print("Выберете тип добавляемого игрока: ")
            answer = input('1 - Человек, 2 - Компьютер \n(q - Выйти из программы, s - Начать игру)\n').strip()
            print('=' * 41 + '\n')

            if number_of_players == 6:
                print('Максимальное количество игроков.\nИгра начинается!')
                break

            if answer == '1':
                number_of_players += 1
                player = Player('Human', f'Игрок {number_of_players}. Человек')
                self.add_player(player)
                print(f'Создан {player.name}')

            elif answer == '2':
                number_of_players += 1
                player = Player('Computer', f'Игрок {number_of_players}. Компьютер')
                self.add_player(player)
                print(f'Создан {player.name}')

            elif answer == 'q':
                print('Вы вышли из программы. До свидания!')
                sys.exit()
            elif answer == 's':
                if number_of_players == 1:
                    print('Игроков должно быть не менее 2-х.\nВыберете еще одного!')
                    continue
                break
            else:
                print('Неправильный ввод. Повторите попытку. \n')
                continue

    def add_player(self, player):
        self.__players.append(player)

