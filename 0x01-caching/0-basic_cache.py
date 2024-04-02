#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents a basic caching.
    """
    def put(self, key, item):
        """Adds an item to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache using its key.
        """
        return self.cache_data.get(key, None)
