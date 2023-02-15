from typing import Any, Callable, Iterator, Type, TypedDict

from cytoolz import complement  # type: ignore
from cytoolz import curry  # type: ignore
from cytoolz import compose_left as pipe  # type: ignore
from cytoolz.curried import compose as B  # type: ignore
from cytoolz.curried import filter, first, flip, groupby, map, valmap  # type: ignore

from config.config import board_id, triage_list_id
from manager.manager_actions import archive_all_triage_cards, move_card_to_backlog
from trello.trello_actions import get_cards_from_board, get_cards_from_list
from utils.fp.func_utils import equals, get_string, includes, log_info, to_list

Card = dict[str, Any]
BoardStatus = TypedDict(
    "BoardStatus",
    {
        "all_cards": list[Card],
        "triage_cards": list[Card],
        "project_cards": list[Card],
    },
)

BoardTasks = TypedDict(
    "BoardTasks",
    {
        "cards_to_be_added": list[Card],
        "cards_to_delete": list[Card],
    },
)


get_id_list = get_string("idList")("")
get_name = get_string("name")("")
get_id = get_string("id")("")
is_triage_list = equals(triage_list_id)
card_in_triage = B(is_triage_list, get_id_list)
card_in_project = B(complement(is_triage_list), get_id_list)

get_triage_cards = filter(card_in_triage)
get_project_cards = filter(card_in_project)


def get_board_status(all_cards: list[Card]) -> BoardStatus:
    return {
        "all_cards": all_cards,
        "triage_cards": list(get_triage_cards(all_cards)),
        "project_cards": list(get_project_cards(all_cards)),
    }


@curry
def cards_have_name(
    cards: list[Card],
    name: str,
) -> bool:
    return pipe(map(get_name), to_list, flip(includes)(name))(cards)


@curry
def name_in_triage_and_project(
    project_cards: list[Card], triage_cards: list[Card]
) -> bool:
    return B(cards_have_name(project_cards), get_name)(triage_cards)  # type: ignore


def get_cards_to_archive(status: BoardStatus) -> Iterator[dict[str, Any]]:
    return filter(name_in_triage_and_project(status["project_cards"]))(status["triage_cards"])  # type: ignore


def get_new_cards(status: BoardStatus) -> Iterator[dict[str, Any]]:
    return pipe(
        filter(
            complement(name_in_triage_and_project(status["project_cards"]))  # type: ignore
        ),
        groupby("name"),
        valmap(first),
        lambda grouped: grouped.values(),
    )(status["triage_cards"])


def get_board_tasks(status: BoardStatus) -> BoardTasks:
    return valmap(to_list)(
        {
            "cards_to_be_added": get_new_cards(status),
            "cards_to_delete": get_cards_to_archive(status),
        }
    )
