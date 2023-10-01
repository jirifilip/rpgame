import pytest

from rpgame.utils import create_2d_list
from rpgame.utils import stringify_2d_list


@pytest.fixture
def matrix():
    yield [
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]


def test_create_2d_list_filled_with_None():
    matrix = create_2d_list(1, 1)

    expected_matrix = [[None]]
    assert matrix == expected_matrix


def test_create_2d_list_filled_with_value():
    matrix = create_2d_list(2, 3, fill=" ")

    expected_matrix = [
        [" ", " "],
        [" ", " "],
        [" ", " "],
    ]
    assert matrix == expected_matrix


def test_stringify_2d_list(matrix):
    assert stringify_2d_list(matrix) == "abcdef"


def test_stringify_2d_list_with_row_separators(matrix):
    assert stringify_2d_list(matrix, row_separator="\n") == "abc\ndef"


def test_stringify_2d_list_with_column_separators(matrix):
    assert stringify_2d_list(matrix, column_separator="-") == "a-b-cd-e-f"


def test_stringify_2d_list_with_row_and_column_separators(matrix):
    assert stringify_2d_list(matrix, row_separator=".", column_separator="x") == "axbxc.dxexf"
