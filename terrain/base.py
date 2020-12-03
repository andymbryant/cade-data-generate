from uuid import uuid4

class Base:
    def __init__(self, **kwargs):
        self._id = int(str(uuid4().int)[-6:])
        self._name = kwargs.get('name', 'default_container_name')

    @property
    def name(self):
        return self._name

    @property
    def class_name(self):
        return self.__class__.__name__.lower()

    @property
    def id(self):
        return self._id
