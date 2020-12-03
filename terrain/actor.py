from base import Base
from random import randint, choice

names = ['Alicia Kenny', 'Harvir Vo', 'Maksim Charlton', 'Jaiden Mclaughlin', 'Opal Rojas', 'Aaliyah Gibson',
         'Sanaa Rangel', 'Aleksander Melendez', 'Troy Smyth', 'Zaina Lancaster']

def get_name():
    return choice(names)


def get_random_ip():
    return ".".join(map(str, (randint(0, 255) for _ in range(4))))


def get_random_country():
    countries = ['Ukraine', 'Russia', 'Serbia',
                 'Belarus', 'Estonia', 'Latvia', 'Bulgaria']
    num = randint(0, len(countries)-1)
    return countries[num]


class Actor(Base):
    def __init__(self, **kwargs):
        super().__init__()
        self._name = kwargs.get('name', get_name())
        self._ip = {
            "actual": get_random_ip(),
            "mask": get_random_ip()
        }
        self._country = get_random_country()

    @property
    def ip(self):
        return self._ip

    @property
    def country(self):
        return self._country

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "name": self.name,
            "ip": self.ip,
            "country": self.country
        }
