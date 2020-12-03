from base import Base
from actor import Actor
from random import choice
from datetime import datetime

def generate_random_name():
    return 'test'

class Event(Base):
    def __init__(self, action, actor, venue):
        super().__init__()
        self._name = generate_random_name()
        self._action = action
        self._actor = actor
        self._venue = venue

    @property
    def action(self):
        return self._action

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
            "action": self.action.serialize(),
            "actor": self.actor.serialize(),
            "venue": self.venue.serialize()
        }
