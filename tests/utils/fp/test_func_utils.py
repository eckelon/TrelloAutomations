# type: ignore
from utils.fp.func_utils import (
    equals,
    includes,
    key_join,
    render_list,
    tuple_key_join,
    zip_tuple,
)


def test_map_to_list():
    example = [1, 2, 3]
    changed_example = map(lambda x: x * 2, example)
    result = render_list(changed_example)
    assert type(result) == list
    assert result == [2, 4, 6]


def test_zip_tuple():
    example = ([{"id": 1}, {"id": 2}], [{"name": "foo"}, {"name": "bar"}])
    desired_result = [({"id": 1}, {"name": "foo"}), ({"id": 2}, {"name": "bar"})]
    assert zip_tuple(example) == desired_result


def test_keyjoin():
    left_example = [{"id": 1, "name": "foo"}, {"id": 2, "name": "bar"}]
    right_example = [{"id": 1, "age": 37}, {"id": 2, "age": 42}]
    should_be = [
        {"id": 1, "name": "foo", "age": 37},
        {"id": 2, "name": "bar", "age": 42},
    ]
    assert list(key_join("id", left_example, "id", right_example)) == should_be


def test_tuple_keyjoin():
    tuple_example = (
        [{"id": 1, "name": "foo"}, {"id": 2, "name": "bar"}],
        [{"id": 1, "age": 37}, {"id": 2, "age": 42}],
    )
    should_be = [
        {"id": 1, "name": "foo", "age": 37},
        {"id": 2, "name": "bar", "age": 42},
    ]
    assert list(tuple_key_join("id", "id", tuple_example)) == should_be


def test_equals() -> None:
    target1: str = "foo"
    destiny1: str = "foo"
    target2: str = "bar"
    destiny2: str = "baz"

    target3: int = 3
    destiny3: int = 3
    target4: int = 3
    destiny4: int = 5

    assert equals(destiny1)(target1) is True
    assert equals(destiny2)(target2) is False
    assert equals(destiny3)(target3) is True
    assert equals(destiny4)(target4) is False


def test_includes() -> None:
    target1: str = "foo"
    destiny1: list[str] = ["foo", "bar"]
    target2: str = "baz"
    destiny2: list[str] = ["foo", "bar"]

    target3: int = 3
    destiny3: list[int] = [1, 2, 3]
    target4: int = 5
    destiny4: list[int] = [1, 2, 3]

    assert includes(destiny1)(target1) is True
    assert includes(destiny2)(target2) is False
    assert includes(destiny3)(target3) is True
    assert includes(destiny4)(target4) is False
