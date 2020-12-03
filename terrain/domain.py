from random import choice, randint
from container import Container
from venue import Venue

first_names = ['People', 'Friends', 'World', 'Community', 'Group', 'Neighbor', 'Cool', 'Crowd', 'Business']
second_names = ['Share', 'Connect', 'Talker', 'Chat', 'Bridge', 'Link', 'Party', 'Band', 'Meet']

def generate_random_name():
    return f'{choice(first_names)}{choice(second_names)}'

def generate_random_venues():
    return [Venue() for _ in range(randint(8, 14))]

class Domain(Container):
    def __init__(self, **kwargs):
        super().__init__()
        self._name = kwargs.get('name', generate_random_name())
        self._venues = kwargs.get('venues', generate_random_venues())

    @property
    def venues(self):
        return self._venues

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "name": self.name,
            "dimensions": self.dimensions,
            "venues": [venue.serialize() for venue in self.venues]
        }
