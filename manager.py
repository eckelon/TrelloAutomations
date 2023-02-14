from config.config import board_id, triage_list_id
from trello.trello_actions import (
    delete_cards,
    get_cards_from_board,
    get_cards_from_list,
)


def get_cards_already_in_project():
    board_cards = list(
        map(
            lambda card: {"name": card["name"], "id": card["id"]},
            get_cards_from_board(board_id),
        )
    )

    triage_cards = list(
        map(
            lambda card: {"name": card["name"], "id": card["id"]},
            get_cards_from_list(triage_list_id),
        )
    )

    board_cards_already_in_project = list(
        map(
            lambda card: {"name": card["name"], "id": card["id"]},
            filter(lambda card: card not in triage_cards, board_cards),
        )
    )

    card_names_in_project = list(
        map(lambda card: card["name"], board_cards_already_in_project)
    )

    cards_in_triage_already_in_board = list(
        filter(lambda card: card["name"] in card_names_in_project, triage_cards)
    )

    return cards_in_triage_already_in_board


def delete_duplicated_cards():
    duplicated_card_ids = list(
        map(lambda card: card["id"], get_cards_already_in_project())
    )

    delete_cards(duplicated_card_ids)


delete_duplicated_cards()
