#!/usr/bin/python3
"""Least Frequently Used caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """retrieving items from a dictionary with a LFU"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.ds = dict()

    def put(self, key, item):
        """ Add an item in the cache """
        if(key is None or item is None):
            return

        if(len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS
           and key not in self.cache_data.keys()):
            lfu_key = min(self.ds, key=self.ds.get)
            del self.cache_data[lfu_key]
            del self.ds[lfu_key]
            print("DISCARD:", lfu_key)
        if(key in self.cache_data.keys()):
            self.ds[key] += 1
        else:
            self.ds[key] = 1
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if(key is None or key not in self.cache_data.keys()):
            return
        self.ds[key] += 1
        return self.cache_data.get(key)
