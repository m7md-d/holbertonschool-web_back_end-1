#!/usr/bin/env python3
"""Provide a helper function for computing pagination index ranges."""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return the start and end indexes for a page of items."""
    total = page * page_size
    return (total - page_size, total)
