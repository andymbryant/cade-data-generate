import json

class Event:
    # composed of actor, action, setting
    def __init__(self, action, actor, venue):
        self._action = action
        self._actor = actor
        self._venue = venue

    @property
    def action(self):
        return self._action

    @property
    def actor(self):
        return self._actor

    @property
    def venue(self):
        return self._venue

    @property
    def platform(self):
        return self.venue.platform


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
