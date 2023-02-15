from typing import Any

from requests import Response

from trello.api_connector import do_delete, do_get, do_post, do_put


def get_cards_from_list(list_id: str) -> Any:
    url = f"https://api.trello.com/1/lists/{list_id}/cards"
    return do_get(url)


def get_cards_from_board(board_id: str) -> Any:
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    return do_get(url)


def delete_card(card_id: str) -> Response:
    print(f"deleting card {card_id}...")
    url = f"https://api.trello.com/1/cards/{card_id}"
    return do_delete(url)


def move_card_to_list(card_id: str, list_id: str):
    url = f"https://api.trello.com/1/cards/{card_id}"
    return do_put(url, {"idList": list_id})


def archive_all_cards_in_list(list_id: str) -> Response:
    url = f"https://api.trello.com/1/lists/{list_id}/archiveAllCards"
    return do_post(url, {})
