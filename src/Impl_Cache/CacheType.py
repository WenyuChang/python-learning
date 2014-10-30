__author__ = 'wenychan'

from enum import Enum


class CacheType(Enum):
    # Discards the least recently used items first.
    LRU = 'Least_Recently_Used'

    # Discards, in contrast to LRU, the most recently used items first.
    MRU = 'Most_Recently_Used'

    # Counts how often an item is needed. Those that are used least often are discarded first.
    LFU = 'Least_Frequently_Used'


if __name__ == '__main__':
    print CacheType.LRU
    print CacheType.LFU