from typing import Any

from examples.examples import board_cards
from manager.manager import (
    BoardStatus,
    BoardTasks,
    cards_have_name,
    get_board_status,
    get_board_tasks,
)


def test_board_status() -> None:
    board_status: BoardStatus = get_board_status(board_cards)
    triage_cards: list[dict[str, Any]] = board_status["triage_cards"]
    all_cards: list[dict[str, Any]] = board_status["all_cards"]
    project_cards: list[dict[str, Any]] = board_status["project_cards"]

    assert len(triage_cards) == 8
    assert len(all_cards) == 22
    assert len(project_cards) == 14
    assert len(project_cards) + len(triage_cards) == len(all_cards)


def test_board_tasks() -> None:
    board_status: BoardStatus = get_board_status(board_cards)
    board_tasks: BoardTasks = get_board_tasks(board_status)

    cards_to_archive: list[dict[str, Any]] = board_tasks["cards_to_delete"]
    cards_to_be_added: list[dict[str, Any]] = board_tasks["cards_to_be_added"]

    assert len(cards_to_archive) == 3
    assert len(cards_to_be_added) == 2


def test_cards_have_name() -> None:
    assert cards_have_name(board_cards)("Foo") is True  # type: ignore
    assert cards_have_name(board_cards)("WrongName") is False  # type: ignore
