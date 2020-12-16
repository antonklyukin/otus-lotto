import pytest
from lotto.card import Card, Barrel
from lotto.game import Player


@pytest.fixture(scope="function")
def get_new_card_by_row():
    card_by_row = [[8, 17, 28, 36, 41, 0, 0, 0, 0], [3, 0, 22, 0, 42, 0, 60, 79, 0], [7, 0, 0, 0, 47, 0, 63, 71, 86]]
    return card_by_row


@pytest.fixture(scope="function")
def get_new_crossed_card_by_row():
    card_by_row = [[-1, -1, -1, -1, -1, 0, 0, 0, 0], [-1, 0, -1, 0, -1, 0, -1, -1, 0], [-1, 0, 0, 0, -1, 0, -1, -1, -1]]
    return card_by_row


@pytest.fixture(scope="function")
def get_new_partially_crossed_card_by_row():
    card_by_row = [[8, -1, 28, 36, 41, 0, 0, 0, 0], [-1, 0, 22, 0, -1, 0, 60, 79, 0], [-1, 0, 0, 0, -1, 0, 63, -1, 86]]
    return card_by_row


def test_all_numbers_are_crossed_crossed(get_new_crossed_card_by_row):
    card = Card()
    card.row = get_new_crossed_card_by_row
    assert card.all_numbers_are_crossed() == True


def test_all_numbers_are_crossed_not_crossed(get_new_card_by_row):
    card = Card()
    card.row = get_new_card_by_row
    assert card.all_numbers_are_crossed() != True


def test_all_numbers_are_crossed_partially_crossed(get_new_partially_crossed_card_by_row):
    card = Card()
    card.row = get_new_partially_crossed_card_by_row
    assert card.all_numbers_are_crossed() != True


def test_cross_number(get_new_card_by_row):
    card = Card()
    barrel_1 = Barrel(8)
    barrel_2 = Barrel(60)
    card.row = get_new_card_by_row
    card.cross_number(barrel_1)
    card.cross_number(barrel_2)
    assert (card.row[0][0], card.row[1][6]) == (-1, -1)


def test_is_in_card_barrel_in_card(get_new_card_by_row):
    card = Card()
    barrel = Barrel(28)
    card.row = get_new_card_by_row
    assert card.is_in_card(barrel) == True


def test_is_in_card_barrel_not_in_card(get_new_card_by_row):
    card = Card()
    barrel = Barrel(90)
    card.row = get_new_card_by_row
    assert card.is_in_card(barrel) != True


def test_count_cross_numbers(get_new_partially_crossed_card_by_row):
    card = Card()
    card.row = get_new_partially_crossed_card_by_row
    assert card.count_crossed_numbers() == 6


def test_generate_list_of_barrels():
    assert len(Barrel.generate_list_of_barrels()) == 90


def test_get_unique_numbers_list_length():
    assert len(Card.get_unique_numbers_list(0, 10, 10)) == 10

def test_player_class_name_setter():
    player = Player('Human', 'Игрок 1')
    player.name = 'Игрок 2'
    assert player._Player__name == 'Игрок 2'
