from classes.action.Action import Action

class CreateAccount(Action):
    def __init__(self, platform):
        super().__init__()
        self._platform = platform

    @property
    def platform(self):
        return self._platform
