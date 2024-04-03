#!/usr/bin/env python3
"""Basic Dictionary Cache"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Basic cache implementation"""
    def __init__(self):
        """Init of an instance"""
        super().__init__()
        self.key_fq = OrderedDict()

    def put(self, key, item):
        """put method for the cache system"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.key_fq[key] += 1
            self.key_fq.move_to_end(key)
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            self.cache_data[key] = item
            self.key_fq[key] = 1
            self.key_fq.move_to_end(key)

    def get(self, key):
        """get method for the cache system"""
        if key is None:
            return None
        res = self.cache_data.get(key)
        if res is None:
            return None
        self.key_fq[key] += 1
        self.key_fq.move_to_end(key)
        return res

    def evict(self):
        """delete lfu element"""
        lfu = []
        lowest = 100
        for key, value in self.key_fq.items():
            if value < lowest:
                lowest = value
        for key, value in self.key_fq.items():
            if value == lowest:
                lfu.append(key)
        if lfu is not None:
            del self.cache_data[lfu[0]]
            del self.key_fq[lfu[0]]
            print(f"DISCARD: {lfu[0]}")
