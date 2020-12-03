from classes.action.Action import Action

class HashtagLatch(Action):
    def __init__(self, hashtag, actor):
        super().__init__()
        self._hashtag = hashtag
        self._actor = actor

    @property
    def hashtag(self):
        return self._hashtag

    @property
    def actor(self):
        return self._actor
