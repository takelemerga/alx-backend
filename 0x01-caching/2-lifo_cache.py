#!/usr/bin/python3
"""child module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """extends base class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign value to key"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if(len(self.cache_data) + 1 <= BaseCaching.MAX_ITEMS):
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """return value associated to key"""
        keylist = self.cache_data.keys()
        if (key is None or key not in keylist):
            return (None)
        return (self.cache_data.get(key))
