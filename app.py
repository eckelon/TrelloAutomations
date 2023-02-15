from argparse import ArgumentParser, Namespace

from config.config import board_id, triage_list_id
from manager.manager import (
    BoardStatus,
    BoardTasks,
    Card,
    get_board_status,
    get_board_tasks,
    get_id,
)
from manager.manager_actions import move_card_to_backlog
from trello.trello_actions import (
    archive_all_cards_in_list,
    delete_card,
    get_cards_from_board,
)
from utils.fp.func_utils import to_list

allowed_actions: list[str] = ["triage"]

parser = ArgumentParser(description="Foo bar")
parser.add_argument(
    "action", metavar="Action", type=str, help=f"Action to perform: {allowed_actions}"
)

args: Namespace = parser.parse_args()
action: str = args.action


def triage():
    all_cards: list[Card] = get_cards_from_board(board_id)
    board_status: BoardStatus = get_board_status(all_cards)
    tasks: BoardTasks = get_board_tasks(board_status)

    for card in tasks["cards_to_be_added"]:
        move_card_to_backlog(card["id"])

    for card in tasks["cards_to_delete"]:
        delete_card(card["id"])

    archive_all_cards_in_list(triage_list_id)


if action == "triage":
    triage()
