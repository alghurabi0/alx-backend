#!/usr/bin/env python3
"""Basic Dictionary Cache"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Basic cache implementation"""
    def __init__(self):
        """Init of an instance"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """put method for the cache system"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_added = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_added[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """get method for the cache system"""
        if key is None:
            return None
        res = self.cache_data.get(key)
        if res is None:
            return None
        self.cache_data.move_to_end(key)
        return res
