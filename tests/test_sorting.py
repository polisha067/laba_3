from typing import Sequence

import pytest

from src.sorting import (
    bucket_sort,
    bubble_sort,
    counting_sort,
    heap_sort,
    quick_sort,
    radix_sort,
    sort_with_key,
)


def _assert_sorted(func, values: Sequence[int]) -> None:
    assert func(values) == sorted(values)


def test_basic_integer_sorts() -> None:
    data = [5, 2, 3, 1, 4, 0, -1]
    for algo in (bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort):
        _assert_sorted(algo, data)


def test_bucket_sort_floats() -> None:
    floats = [0.15, 0.99, 0.5, 0.51, 0.2]
    assert bucket_sort(floats) == sorted(floats)


def test_sort_with_key_and_cmp() -> None:
    items = ["aa", "b", "ccc"]
    assert sort_with_key(items, key=len) == ["b", "aa", "ccc"]

    def reverse_length(first: str, second: str) -> int:
        return len(second) - len(first)

    assert sort_with_key(items, cmp=reverse_length) == ["ccc", "aa", "b"]


def test_radix_invalid_base() -> None:
    with pytest.raises(ValueError):
        radix_sort([1, 2, 3], base=1)

