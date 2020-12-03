# from abc import ABC, abstractmethod

from classes.Base import Base
from datetime import datetime


class Action(Base):
    def __init__(self, actor=None, venue=None):
        self._date = datetime.now()
        self._actor = actor
        self._venue = venue

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @property
    def actor(self):
        return self._actor

    @property
    def venue(self):
        return self._venue

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "test": 'test'
        }
