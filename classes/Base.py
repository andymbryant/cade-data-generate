from uuid import uuid1

class Base:
    def __init__(self):
        self._id = uuid1().int

    @property
    def id(self):
        return self._id
