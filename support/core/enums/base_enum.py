from functools import lru_cache
from operator import attrgetter
from enum import unique, Enum


@unique
class BaseEnum(Enum):

    @classmethod
    @lru_cache(None)
    def values(cls):
        return tuple(map(attrgetter('value'), cls))

    @classmethod
    @lru_cache(None)
    def names(cls):
        return tuple(map(attrgetter('name'), cls))

    @classmethod
    @lru_cache(None)
    def items(cls):
        return tuple(zip(cls.values(), cls.names()))

    @classmethod
    @lru_cache(None)
    def revert_items(cls):
        return tuple(zip(cls.names(), cls.values()))

    @classmethod
    @lru_cache(None)
    def members(cls):
        return dict(cls.items())

    @classmethod
    @lru_cache(None)
    def revert_members(cls):
        return dict(cls.revert_items())

    @classmethod
    @lru_cache(None)
    def exclude_values(cls, items):
        return tuple(set((map(attrgetter('value'), cls))) - set(items))
