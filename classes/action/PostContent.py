from classes.action.Action import Action

class PostContent(Action):
    '''Content is posted by an actor in a venue. Includes the type of content and its cateogory.'''
    def __init__(self, content_type, category):
        super().__init__()
        self._content_type = content_type
        self._category = category

    @property
    def content_type(self):
        return self._content_type

    @property
    def category(self):
        return self._category
