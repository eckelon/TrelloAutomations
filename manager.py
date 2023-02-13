from requests import request

import os

trello_api_key = os.environ['TRELLO_API_KEY']
trello_api_token = os.environ['TRELLO_API_TOKEN']

triage_id = os.enenviron['triage_list_id']
board_id = os.enenviron['board_id']


get_triage_cards_url = f'https://api.trello.com/1/lists/{triage_id}/cards'
get_board_cards_url = f'https://api.trello.com/1/boards/{board_id}/cards'

query = {
  'key': trello_api_key,
  'token': trello_api_token
}

headers = {
  "Accept": "application/json"
}

triage_cards_response = request( "GET", get_triage_cards_url, params=query, headers=headers ).json()
board_cards_response = request("GET", get_board_cards_url, params=query, headers=headers).json()

triage_cards_ids = map(lambda card: card['id'], triage_cards_response)
triage_cards_names = map(lambda card: card['name'], triage_cards_response)

# print(list(triage_cards_names))

board_cards_without_triage = filter(lambda card: card['id'] not in triage_cards_ids , board_cards_response)
print(list(board_cards_without_triage))


# duplicated_cards = filter(lambda card: card['name'] in triage_cards_names, board_cards_without_triage)

# print(list(duplicated_cards))