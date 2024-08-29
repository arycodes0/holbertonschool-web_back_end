#!/usr/bin/env python3

""" Hypermedia pagination module. """

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a pagination system.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the
        end index corresponding to the range of items to
        return for the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int): The current page number (1-indexed).
            Must be greater than 0. page_size (int): The number
            of items per page. Must be greater than 0.

        Returns:
            List[List]: A list of rows corresponding to the
            requested page of the dataset. If the page is out
            of range, an empty list is returned.
        """
        assert isinstance(page, int) and page > 0, (
            "Page number must be a positive integer."
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer."
        )

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a page of data along with pagination metadata.

        Args:
            page (int): The current page number (1-indexed).
            Must be greater than 0. page_size (int): The number
            of items per page. Must be greater than 0.

        Returns:
            Dict[str, Any]: A dictionary containing the page size,
            current page number, data, next page number, previous
            page number, and total pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
