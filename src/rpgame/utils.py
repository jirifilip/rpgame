from typing import Any, List


def create_2d_list(width: int, height: int, fill: Any = None) -> List[List[Any]]:
    return [
        [fill for _ in range(width)]
        for _ in range(height)
    ]


def stringify_2d_list(
        list_to_stringify: List[List[Any]],
        row_separator: str = "",
        column_separator: str = "") -> str:
    return row_separator.join([
        column_separator.join(column_list) for column_list in list_to_stringify
    ])
