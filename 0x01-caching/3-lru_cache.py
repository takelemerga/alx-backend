#!/usr/bin/python3
"""child class module"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """extends base class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign value to key"""
        keylist = list(self.cache_data.keys())
        if (key or item is not None):
            if(len(self.cache_data) + 1 <= BaseCaching.MAX_ITEMS):
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                lru_key, value = self.cache_data.popitem(True)
                print("{}:{}".format("DISCARD", lru_key))
                '''self.cache_data[key] = item'''
                '''self.cache_data.move_to_end(key, last=False)'''

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
