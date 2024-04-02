#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents a Least Frequently Used (LFU) caching mechanism
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, key):
        """Reorders the items in the cache based on the frequency of access.
        """
        # Find the index and frequency of the key
        for i, (k, freq) in enumerate(self.keys_freq):
            if k == key:
                break
        else:
            return

        # Increase the frequency and reorder
        freq += 1
        self.keys_freq.pop(i)
        while i > 0 and self.keys_freq[i - 1][1] <= freq:
            i -= 1
        self.keys_freq.insert(i, (key, freq))

    def put(self, key, item):
        """Adds an item to the cache.
        """
        if key is None or item is None:
            return

        # If the key exists, update its value and reorder
        if key in self.cache_data:
            self.cache_data[key] = item
            self.__reorder_items(key)
            return

        # Evict the least frequently used item if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            lfu_key, _ = self.keys_freq.pop()
            del self.cache_data[lfu_key]
            print("DISCARD:", lfu_key)

        # Add the new item and its frequency
        self.cache_data[key] = item
        self.keys_freq.append((key, 0))

    def get(self, key):
        """Retrieves an item from the cache using its key.
        """
        if key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
