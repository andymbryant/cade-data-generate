from base import Base
from actor import Actor
from random import choice
from datetime import datetime

# This needs the most work
# Types should be specific to the domain that it's in, e.g. hashtag latching for hashtag-centric domains like Twitter
types = [
    {
        'category': 'boost',
        'options': ['likes', 'followers'],
    },
    {
        'category': 'create',
        'options': ['account']
    },
    {
        'category': 'post',
        'options': ['adversarial_content', 'spam_content', 'in-group_favor', 'out-group_denigration', 'to_echo_chamber'],
    },
    {
        'category': 'mention',
        'options': ['legit_users']
    },
    {
        'category': 'like',
        'options': ['legit_users']
    },
    {
        'category': 'thread',
        'options': ['jack']
    },
    {
        'category': 'comment',
        'options': ['lock-step']
    },
    {
        'category': 'follow',
        'options': ['legit_users']
    },
    {
        'category': 'manipulate',
        'options': ['rank']
    }
]


def generate_random_name():
    t = choice(types)
    category = t['category']
    option = choice(t['options'])
    return f'{category}_{option}'

class Action(Base):
    # name/type
    # actor
    # domain
    def __init__(self, **kwargs):
        super().__init__()
        self._name = kwargs.get('name', generate_random_name())
        self._executed_at = kwargs.get('executed_at', datetime.now())

    @property
    def executed_at(self):
        return self._executed_at

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "executed_at": str(self.executed_at)
        }
