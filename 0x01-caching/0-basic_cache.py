#!/usr/bin/env python3
"""Basic Dictionary Cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        res = self.cache_data.get(key)
        if res is None:
            return None
        return res
