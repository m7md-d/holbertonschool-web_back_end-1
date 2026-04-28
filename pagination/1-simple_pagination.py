#!/usr/bin/env python3
"""Provide a helper function for computing pagination index ranges."""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return the start and end indexes for a page of items."""
    total = page * page_size
    return (total - page_size, total)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        wanted_page = self.dataset()

        if not wanted_page:
            return []
        return wanted_page[index[0] : index[1]]
