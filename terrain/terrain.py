from container import Container
from domain import Domain

def generate_domains(num):
    return [Domain() for _ in range(num)]

class Terrain(Container):
    def __init__(self, **kwargs):
        super().__init__()

    # @property
    # def domains(self):
    #     return self._domains

    def serialize(self):
        return {
            "id": self.id,
            "type": self.class_name,
            "dimensions": self.dimensions,
        }
