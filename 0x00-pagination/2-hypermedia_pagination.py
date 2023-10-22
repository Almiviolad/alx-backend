#!/usr/bin/env python3
"""Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary."""
from typing import Tuple
import csv
import math
from typing import List, Dict, Union
import math


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

    def get_hyper(self,
                  page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        """takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer"""
        dataset = self.dataset()
        page_content = self.get_page(page, page_size)
        page_length = len(page_content)
        dataset_length = len(dataset)
        total_pages = math.ceil(len(dataset) / page_size)
        if (page < total_pages and page >= 1):
            next_page = page + 1
        else:
            next_page = None
        if (page > 1):
            prev_page = page - 1
        else:
            prev_page = None

        result = {'page_size': page_length, 'page': page, 'data': page_content,
                  'next_page': next_page, 'prev_page': prev_page,
                  'total_pages': total_pages}
        return result
