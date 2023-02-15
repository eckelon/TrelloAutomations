import json

board_cards_path = "./examples/board_cards.json"

with open(board_cards_path) as board_cards_file:
    board_cards = json.load(board_cards_file)
