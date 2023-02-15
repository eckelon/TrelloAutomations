# type: ignore
import logging
from itertools import chain, starmap
from typing import Any, Callable, Iterable

from toolz import curry, get
from toolz.curried import assoc
from toolz.curried import compose as B
from toolz.curried import do, join, keyfilter, merge

trace = do(print)
flat_merge = B(merge, chain)


def render_list(iterable: map) -> list:
    return list(iterable)


@curry
def K(value, _):
    return value


def zip_tuple(element: tuple) -> list:
    return list(zip(*element))


dict_of = assoc({})


def key_join(left_key, left_seq, right_key, right_seq):
    return starmap(merge, join(left_key, left_seq, right_key, right_seq))


@curry
def tuple_key_join(left_key, right_key, target):
    left_seq, right_seq = target
    return key_join(left_key, left_seq, right_key, right_seq)


@curry
def pick(desired, d):
    return keyfilter(lambda k: k in desired, d)


@curry
def tap(f, x):
    f(x)
    return x


def log_info(value):
    return tap(lambda x: print(x), value)


@curry
def get_list(key: str, default_list: list):
    return lambda target: get(key, target, default_list)


@curry
def get_string(key: str, default_string: str):
    return lambda target: get(key, target, default_string)


@curry
def equals(destiny: Any):
    return lambda target: target == destiny


@curry
def includes(destiny: Iterable, target: Any) -> bool:
    return target in destiny


def to_list(target: Iterable[Any]) -> list[Any]:
    return list(target)
