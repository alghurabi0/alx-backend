#!/usr/bin/env python3
"""Basic Dictionary Cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Basic cache implementation"""
    def put(self, key, item):
        """put method for the cache system"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            pass
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_added = list(self.cache_data.keys())[-1]
            del self.cache_data[last_added]
            print(f"DISCARD: {last_added}")
        self.cache_data[key] = item

    def get(self, key):
        """get method for the cache system"""
        if key is None:
            return None
        res = self.cache_data.get(key)
        if res is None:
            return None
        return res
