#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from .game import Game, Player


def no_barrels_in_stock(game: Game):
    if len(game.barrels) == 0:
        return True


def play_round(game: Game):
    if len(game.players) == 1:
        return (1, game.players.pop())

    game.round += 1

    print(f'Раунд {game.round}')

    if no_barrels_in_stock(game):
        return -1

    barrel = game.barrels.pop()
    print(f'Вытянут бочонок {barrel}')

    round_players = game.players[:]  # Cнимаем копию со списка игроков, чтобы изменять его в цикле

    for i, player in enumerate(round_players):

        if len(game.players) == 1:
            return 1

        # print('-' * 30 + '\n')
        print(f'Количество игроков в игре: {len(game.players)} \n')
        print(f'Осталось бочонков: {len(game.barrels)} \n')
        print(f'Вытянут бочонок с номером {barrel.number}\n')
        # print('-' * 30 + '\n')
        print(f'Ход игрока {player.name}\n')
        print(f'Карточка:')

        player.card.print()

        if player.type == 'Human':
            player_answer = input('Зачеркнуть клетку? (y/n)').lower().strip()
            if (player_answer == 'y' and not player.card.is_in_card(barrel)
                    or player_answer != 'y' and player.card.is_in_card(barrel)):
                print(f'ИГРОК {player.name} ПРОИГРАЛ!\n')

                if len(game.players) > 1:
                    game.players = [item for item in game.players if item.name != player.name]
                else:
                    return 1
                continue

            else:
                if player.card.is_in_card(barrel):
                    player.card.cross_number(barrel)
                    print(f'Бочонок {barrel.number} поставлен!')
                    if game.barrels:
                        barrel = game.barrels.pop()
                    continue
                if player.card.all_numbers_are_crossed():
                    return (1, player)
                continue

        elif player.type == "Computer":
            if player.card.is_in_card(barrel):
                player.card.cross_number(barrel)
                print(f'Бочонок {barrel.number} поставлен!')
                if game.barrels:
                    barrel = game.barrels.pop()
                continue
            if player.card.all_numbers_are_crossed():
                return (1, player)

    return 0


game = Game()
players = game.players
print('Игра до первого победителя или последнего проигравшего началась!')
while True:
    result = play_round(game)
    if result == 0:
        continue

    elif result == -1:
        print('====================')
        print('Бочонки закончились!')
        print('Выиграет тот, кто больше зачеркнул: \n')
        winners_list = []
        results_list = []

        for player in players:
            print(f'Игрок {player.name} зачеркнул {player.card.count_crossed_numbers()} цифр\n')
            results_list.append(player.card.count_crossed_numbers())
        max_result = max(results_list)
        for player in players:
            if player.card.count_crossed_numbers() == max_result:
                winners_list.append(player.name)

        print('ИГРА ЗАКОНЧЕНА!\nПОБЕДИТЕЛЬ:\n')
        for winner in winners_list:
            print(winner + '\n')
        break

    else:
        print(f'ИГРА ЗАКОНЧЕНА!\nПОБЕДИТЕЛЬ - {players.pop().name}')
        break
