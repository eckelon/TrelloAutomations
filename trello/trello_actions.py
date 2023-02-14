from config.config import backlog_list_id, triage_list_id
from trello.api_connector import do_delete, do_get, do_put

get_triage_cards_url = f"https://api.trello.com/1/lists/{triage_list_id}/cards"


def get_cards_from_list(list_id: str) -> list:
    url = f"https://api.trello.com/1/lists/{list_id}/cards"
    return do_get(url)


def get_cards_from_board(board_id: str) -> list:
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    return do_get(url)


def delete_card(card_id: str) -> dict:
    print(f"deleting card {card_id}...")
    url = f"https://api.trello.com/1/cards/{card_id}"
    return do_delete(url)


def delete_cards(card_ids: list) -> list:
    return list(map(delete_card, card_ids))


def move_card_to_backlog(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    return do_put(url, {"idList": backlog_list_id})
