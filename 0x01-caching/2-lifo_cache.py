#!/usr/bin/env python3
"""LIFO Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Defines a caching system that uses the LIFO Caching style
    """
    def __init__(self):
        """Initializes a LIFOCaching instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds item to the self.cache_data structure,
        using the LIFO Caching algorithm
        """
        cache_count = len(self.cache_data)
        if key is None or item is None:
            return None
        if cache_count == BaseCaching.MAX_ITEMS:
            cache_keys = list(self.cache_data.keys())
            discarded_item_key = cache_keys[cache_count - 1]  # Last item added
            self.cache_data.pop(discarded_item_key)
            print("DISCARD: {}".format(discarded_item_key))
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value corresponding to @key in self.cache_data
        """
        fetched_data = self.cache_data.get(key)
        return fetched_data
