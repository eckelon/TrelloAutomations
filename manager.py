from requests import request

from config.config import api_key, board_id, token, triage_list_id

get_board_cards_url = f"https://api.trello.com/1/boards/{board_id}/cards"
get_triage_cards_url = f"https://api.trello.com/1/lists/{triage_list_id}/cards"

query = {"key": api_key, "token": token}
headers = {"Accept": "application/json"}

triage_cards_response = request(
    "GET", get_triage_cards_url, params=query, headers=headers
).json()

board_cards_response = request(
    "GET", get_board_cards_url, params=query, headers=headers
).json()

board_cards = map(
    lambda card: {"name": card["name"], "id": card["id"]}, board_cards_response
)
triage_cards = map(
    lambda card: {"name": card["name"], "id": card["id"]}, triage_cards_response
)

board_cards_not_in_triage = map(
    lambda card: card["name"],
    filter(lambda card: card not in triage_cards, board_cards),
)

cards_ids_in_triage_already_in_board = list(
    map(
        lambda card: card["id"],
        filter(lambda card: card["name"] in board_cards_not_in_triage, triage_cards),
    )
)
# Let's delete duplicated cards
for card_id in cards_ids_in_triage_already_in_board:
    deleted = request(
        "DELETE",
        f"https://api.trello.com/1/cards/{card_id}",
        params=query,
        headers=headers,
    ).json()

    print(deleted)
