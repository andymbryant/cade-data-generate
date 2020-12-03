from classes.Base import Base

class Venue(Base):
    def __init__(self, platform=None, category=None):
        self._platform = platform
        self._category = category

    @property
    def platform(self):
        return self._platform

    @property
    def category(self):
        return self._category
