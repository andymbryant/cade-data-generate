from classes.Base import Base
from random import randint

def get_random_ip():
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))

def get_random_country():
    countries = ['Ukraine', 'Russia', 'Serbia', 'Belarus', 'Estonia']
    num = randint(0, len(countries)-1)
    return countries[num]

class Actor(Base):
    def __init__(self, name):
        super().__init__()
        self._name = name
        self._ip_actual = get_random_ip()
        self._ip_mask = get_random_ip()
        self._country = get_random_country()

        @property
        def name(self):
            return self._name
        @property
        def ip_actual(self):
            return self._ip_actual

        @property
        def ip_mask(self):
            return self._ip_mask

        @property
        def country(self):
            return self._country