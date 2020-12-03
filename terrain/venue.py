from random import choice, randint
from container import Container

first_names = ['Patriot', 'Smart', 'Freedom', 'Foreign', 'Green', 'Blue',
               'Red', 'Center', 'Angry', 'Open', 'Liberal', 'Conservative']
second_names = ['Eagle', 'Morning', 'News', 'Gazette',
                'Correspondent', 'Group', 'Bugle', 'Truth', 'Interpreter', 'Mind', 'Thinker']

def generate_name():
    return f'{choice(first_names)}{choice(second_names)}'

class Venue(Container):
    def __init__(self, domain):
        super().__init__()
        self._name = generate_name()
        # self._domain = kwargs.get('domain', None)
        self._domain = domain

    @property
    def domain(self):
        return self._domain

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "name": self.name,
            "domain": self.domain.serialize()
        }
