#!/usr/bin/env python3
"""Pagination
"""
from typing import Tuple, Dict, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range
    """
    offset = (page - 1) * page_size
    end = offset + page_size
    return (offset, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """Retrieves a page of a data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        offset, end = index_range(page, page_size)
        data = self.dataset()
        if offset > len(data):
            return []
        return data[offset:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves information about a page
        """
        page_data = self.get_page(page, page_size)
        offset, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if offset > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
