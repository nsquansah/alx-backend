#!/usr/bin/env python3
"""MRU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Defines a caching system that uses the MRU caching algorithm
    """
    def __init__(self):
        """Initializes an MRUCache instance"""
        super().__init__()
        self.__queue = list(self.cache_data.keys())

    def put(self, key, item):
        """
        Adds item to the self.cache_data structure,
        using the MRU Caching algorithm
        """
        cache_count = len(self.cache_data)
        queue_count = len(self.__queue)
        if key is None or item is None:
            return None
        if cache_count == BaseCaching.MAX_ITEMS:
            discarded_item_key = self.__queue[queue_count - 1]  # Last item
            self.__queue.remove(discarded_item_key)
            self.cache_data.pop(discarded_item_key)
            print("DISCARD: {}".format(discarded_item_key))

        self.cache_data[key] = item
        if key in self.__queue:
            self.__queue.remove(key)
        self.__queue.append(key)  # Add key of item to start of list

    def get(self, key):
        """Retrieves the value corresponding to @key in self.cache_data
        """
        if key in self.__queue:
            self.__queue.remove(key)
            self.__queue.append(key)
        return self.cache_data.get(key)
