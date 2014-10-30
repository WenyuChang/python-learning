__author__ = 'wenychan'


class MyListNode:
    def __init__(self, value=None, next=None, pre=None, random=None):
        self._value = value
        self._next = next
        self._pre = pre
        self._random = random

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value