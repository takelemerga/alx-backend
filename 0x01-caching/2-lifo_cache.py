#!/usr/bin/python3
"""child module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """extends base class"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """assign value to key"""
        keylist = list(self.cache_data.keys())
        if (key or item is not None):
            if(len(self.cache_data) + 1 <= BaseCaching.MAX_ITEMS):
                self.cache_data[key] = item
            else:
                self.cache_data.pop(keylist[len(keylist) - 1])
                print("DISCARD", keylist[len(keylist) - 1])
                self.cache_data[key] = item

    def get(self, key):
        """return value associated to key"""
        keylist = self.cache_data.keys()
        if (key is None or key not in keylist):
            return (None)
        return (self.cache_data.get(key))
