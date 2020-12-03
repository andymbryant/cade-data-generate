from random import choice, randint
from container import Container
from action import Action

first_names = ['Patriot', 'Smart', 'Freedom', 'Foreign', 'Green', 'Blue',
               'Red', 'Center', 'Angry', 'Open', 'Liberal', 'Conservative']
second_names = ['Eagle', 'Morning', 'News', 'Gazette',
                'Correspondent', 'Group', 'Bugle', 'Truth', 'Interpreter', 'Mind', 'Thinker']

def generate_name():
    return f'{choice(first_names)}{choice(second_names)}'

def generate_actions(num):
    return [Action() for _ in range(num)]

class Venue(Container):
    def __init__(self, **kwargs):
        super().__init__()
        self._name = kwargs.get('name', generate_name())
        self._actions = kwargs.get('actions', generate_actions(randint(5,10)))

    @property
    def actions(self):
        return self._actions

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "name": self.name,
            "actions": [action.serialize() for action in self.actions]
        }
