from cytoolz import groupby  # type: ignore
from cytoolz.dicttoolz import valmap  # type: ignore
from cytoolz.itertoolz import first  # type: ignore
from requests import Response

from config.config import board_id, triage_list_id
from config.manager_actions import SimpleCard, archive_all_triage_cards, move_card_to_backlog
from trello.trello_actions import get_cards_from_board, get_cards_from_list


def get_cards_already_in_project():
    triage_cards, board_cards_already_in_project = get_current_status()

    cards_in_triage_already_in_board = list(
        filter(
            lambda card: card["name"]
            in map(lambda card: card["name"], board_cards_already_in_project),
            triage_cards,
        )
    )

    return cards_in_triage_already_in_board


def get_current_status():
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

    return triage_cards, board_cards_already_in_project


def get_suitable_cards() -> list[SimpleCard]:
    triage_cards, board_cards_already_in_project = get_current_status()

    suitable_cards_by_name = sorted(
        list(
            filter(
                lambda card: card["name"]
                not in map(lambda card: card["name"], board_cards_already_in_project),
                triage_cards,
            )
        ),
        key=lambda card: card["name"],
    )

    suitable_cards: list[SimpleCard] = list(
        valmap(first, groupby("name", suitable_cards_by_name)).values()  # type: ignore cytoolz doesn't export types
    )

    return suitable_cards


suitable_cards = get_suitable_cards()
suitable_cards_to_backlog: list[Response] = list(
    map(move_card_to_backlog, map(lambda card: card["id"], suitable_cards))
)

archive_all_triage_cards()

print(list(suitable_cards_to_backlog))
