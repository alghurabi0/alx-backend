#!/usr/bin/env python3
"""Pagination function returns indexes"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    firstIdx = (page-1) * page_size
    secondIdx = ((page-1) * page_size) + page_size
    return (firstIdx, secondIdx)
