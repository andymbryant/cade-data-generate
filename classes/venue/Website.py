from classes.venue.Venue import Venue
from classes.Platform import Platform

web = Platform('web')

class Website(Venue):
    def __init__(self, name):
        super().__init__(platform=web, category='site')
        self._name = name

    @property
    def name(self):
        return self._name
