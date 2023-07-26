#!/usr/bin/env python3
"""LFU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Creates a caching system using the LFU caching algorithm"""

    def __init__(self):
        """Initializes a LFUCache instance"""
        super().__init__()
        self.__cache_freq = {key: 0 for key in self.cache_data.keys()}

    def put(self, key, item):
        """
        Adds item to the self.cache_data structure,
        using the MRU Caching algorithm
        """
        if key is None or item is None:
            return None
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            freq_count = len(self.__cache_freq)
            # Get key for least frequently used item from @self.__cache_freq
            lfu_item_keys = list(self.__cache_freq.keys())
            lfu_item_values = list(self.__cache_freq.values())
            # Find index of the lowest value in the lfu_item_values list
            lfu_item_idx = lfu_item_values.index(min(lfu_item_values))
            # Get key of lfu in self.__cache_freq dictionary
            lfu_item_key = lfu_item_keys[lfu_item_idx]
            self.cache_data.pop(lfu_item_key)
            self.__cache_freq.pop(lfu_item_key)
            print("DISCARD: {}".format(lfu_item_key))

        if key not in self.__cache_freq:
            self.__cache_freq[key] = 0

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value corresponding to @key in self.cache_data
        """
        item = self.cache_data.get(key)
        # Increase the value tracking the number of times data was accessed
        if item is not None:
            self.__cache_freq[key] += 1

        return item
