#!/usr/bin/python3
"""basic cache odule"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """child caching module"""

    def put(self, key, item):
        """assign value to key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item   

    def get(self, key):
        """return value associated to key"""
        keylist = self.cache_data.keys()
        if (key is None or key not in keylist):
            return (None)
        return (self.cache_data.get(key))
