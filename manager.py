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

triage_cards_ids = map(lambda card: card["id"], triage_cards_response)
triage_cards_names = map(lambda card: card["name"], triage_cards_response)

board_cards_without_triage = filter(
    lambda card: card["id"] not in triage_cards_ids, board_cards_response
)

duplicated_cards = filter(
    lambda card: card["name"] in triage_cards_names, board_cards_without_triage
)
