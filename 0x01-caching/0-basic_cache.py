#!/usr/bin/python3
from base import BaseCaching


class BasicCache(BaseCaching):
    """child caching module"""

    def put(self, key, item):
        """assign value to key"""
        if (key or item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """return value associated to key"""
        keylist = self.cache_data.keys()
        if (key is None or key not in keylist):
            return (None)
        return (self.cache_data.get(key))
