__author__ = 'wenychan'

from abc import ABCMeta
from abc import abstractmethod


class Refresher(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def refresh(self):
        pass
