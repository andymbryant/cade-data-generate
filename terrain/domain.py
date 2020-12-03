from random import choice, randint
from container import Container
from venue import Venue

first_names = ['People', 'Friends', 'World', 'Community', 'Group', 'Neighbor', 'Cool', 'Crowd', 'Business']
second_names = ['Share', 'Connect', 'Talker', 'Chat', 'Bridge', 'Link', 'Party', 'Band', 'Meet']

def generate_random_name():
    return f'{choice(first_names)}{choice(second_names)}'

class Domain(Container):
    def __init__(self, **kwargs):
        super().__init__()
        self._name = kwargs.get('name', generate_random_name())

    @property
    def venues(self):
        return self._venues

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "name": self.name,
        }
