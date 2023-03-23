#!/usr/bin/python3
"""child module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ extends base class"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """assign value to key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            keylist = list(self.cache_data.keys())
            self.cache_data.pop(keylist[0])
            print("{}:{}".format("DISCARD", keylist[0]))

    def get(self, key):
        """return value associated to key"""
        keylist = self.cache_data.keys()
        if (key is None or key not in keylist):
            return (None)
        return (self.cache_data.get(key))
