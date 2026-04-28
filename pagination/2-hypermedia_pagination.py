#!/usr/bin/env python3
"""Provide a helper function for computing pagination index ranges."""

import csv
import math
from typing import List, Dict, Any, Optional


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return the start and end indexes for a page of items."""
    total = page * page_size
    return (total - page_size, total)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset as a list of rows."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the page data for the given page and page_size."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        wanted_page = self.dataset()

        if not wanted_page:
            return []
        return wanted_page[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a hypermedia pagination dictionary for the given page."""
        data_len = len(self.dataset())
        total_pages = math.ceil(data_len / page_size)
        data = self.get_page(page, page_size)
        if page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1

        if page - 1 < 0:
            prev_page = None
        else:
            prev_page = page - 1
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
