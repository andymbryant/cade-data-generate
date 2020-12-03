from base import Base

class Container(Base):
    def __init__(self, **kwargs):
        super().__init__()
        self._dimensions = kwargs.get('dimensions', [1000, 1000])

    @property
    def dimensions(self):
        return self._dimensions
