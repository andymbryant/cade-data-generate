from classes.Platform import Platform
from classes.venue.Venue import Venue

facebook = Platform('Facebook')

class FacebookGroup(Venue):
    def __init__(self, name):
        super().__init__(platform=facebook, category='group')
        self._name = name

    @property
    def name(self):
        return self._name
