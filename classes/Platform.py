from classes.Base import Base

class Platform(Base):
    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    # def venues(self):
    #     return self._venues

    # def add_venue(self, venue):
    #     self._venues.append(venue)
