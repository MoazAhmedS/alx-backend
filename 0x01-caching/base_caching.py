#!/usr/bin/env python3
"""BaseCaching module.
"""


class BaseCaching():
    """BaseCaching defines:
      - Constants of your caching
      - Where your data are stored
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initializes the cache.
        """
        self.cache_data = {}

    def print_cache(self):
        """Prints the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Adds an item to the cache.
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """Retrieves an item from the cache using its key.
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
