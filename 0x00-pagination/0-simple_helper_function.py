#!/usr/bin/env python3
"""Pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range
    """
    offset = (page - 1) * page_size
    end = offset + page_size
    return (offset, end)
