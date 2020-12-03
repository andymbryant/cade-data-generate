from classes.venue.Venue import Venue
from classes.Platform import Platform

twitter = Platform('Twitter')

class Hashtag(Venue):
    def __init__(self, value):
        super().__init__(platform=twitter, category='hashtag')
        self._value = value

    @property
    def value(self):
        return self._value
