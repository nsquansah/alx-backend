#!/usr/bin/env python3
"""FIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that uses FIFO caching algorithm
    """
    def __init__(self):
        """Initializes the class instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds item to the self.cache_data structure,
        using the FIFO Caching algorithm
        """
        if key is None or item is None:
            return None
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            cache_keys = list(self.cache_data.keys())
            discarded_item_key = cache_keys[0]
            discarded_item = self.cache_data.pop(discarded_item_key)
            print("DISCARD: {}".format(discarded_item_key))
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value corresponding to @key in self.cache_data
        """
        fetched_data = self.cache_data.get(key)
        return fetched_data
