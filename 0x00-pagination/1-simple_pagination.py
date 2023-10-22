#!/usr/bin/env python3
"""Implement a method named get_page that takes two ints
arguments page with default value 1 and page_size with
 default value 10.

You have to use this CSV file (same as the one presented
at the top of the project)
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the
dataset correctly and return the appropriate page of the
dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset,
an empty list should be returned"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return a tuple of size two containing a start index
and an end index corresponding to the range of indexe
s to return
in a list for those particular pagination parameters"""
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """constructor for class"""
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
        """takes two integer arguments page with default value 1
and page_size with default value 10."""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        indices = index_range(page, page_size)
        dataset = self.dataset()
        start_idx = indices[0]
        end_idx = indices[1]
        try:
            result = [elem for elem in dataset[start_idx:end_idx]]
        except IndexError:
            result = []
        return result
