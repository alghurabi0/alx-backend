#!/usr/bin/env python3
"""Pagination function returns indexes"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Pagination helper function"""
    firstIdx = (page-1) * page_size
    secondIdx = page * page_size
    return (firstIdx, secondIdx)
