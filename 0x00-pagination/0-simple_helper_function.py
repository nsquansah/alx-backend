#!/usr/bin/env python3
"""Module for Task_0, defines a function `index_range`"""
from typing import Tuple, Union


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    """Returns a tuple of size two containing a start and end index of items
    Args:
        page (int): the current page
        page_size (int): the number of items in each page
    Returns:
        A tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters, or None if an invalid parameter
        is passed.
    """
    if (page < 1):
        return None

    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return (start_index, end_index)
