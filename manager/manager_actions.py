from typing import TypedDict

from requests import Response

from config.config import backlog_list_id, triage_list_id
from trello.trello_actions import (archive_all_cards_in_list, delete_card,
                                   move_card_to_list)


def delete_cards(card_ids: list[str]) -> list[Response]:
    return list(map(delete_card, card_ids))


def archive_all_triage_cards() -> Response:
    return archive_all_cards_in_list(triage_list_id)


def move_card_to_backlog(card_id: str) -> Response:
    return move_card_to_list(card_id, backlog_list_id)
