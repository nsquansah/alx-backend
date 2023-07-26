#!/usr/bin/env python3
"""Implementing Simple Pagination"""
import csv
import math
from typing import List, Tuple, Union


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns paginated items as List
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        pages = []
        page_range = index_range(page, page_size)
        if (page_range is not None):
            start = page_range[0]
            end = page_range[1]
            dataset = self.dataset()
            try:
                pages = [dataset[i] for i in range(start, end)]
            except IndexError:
                pass

        return pages
