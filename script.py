import itertools
import json
from random import randint
from classes.Platform import Platform
from classes.actor.Actor import Actor
from classes.venue.Hashtag import Hashtag
from classes.venue.Website import Website
from classes.venue.FacebookGroup import FacebookGroup
from classes.action.CreateAccount import CreateAccount
from classes.action.PostContent import PostContent
from classes.action.HashtagLatch import HashtagLatch
from classes.action.PostContent import PostContent
from classes.action.ThreadJack import ThreadJack

flatten = itertools.chain.from_iterable

terrain = {
    'name': 'cybersocial_1',
    'dimensions': [1000,1000]
}

platform_names = ['Facebook', 'web', 'Twitter']

# Venues
hashtags = ['#USNavy', '#USSWasp', '#USSGravely', '#teamranger', '#NATO', '#StrongerTogether', '#EU!', '#HATO']
twitter_venues = [Hashtag(value) for value in hashtags]

website_names = ['Nato.int', 'garryc29rus.ru', 'Daanlucas.ua', 'vitaliyvas2.ua', 'Strategybin.com']
web_vanues = [Website(name) for name in website_names]

facebook_groups = ['garryc29rus', 'vitaliyvas2', 'Nato', 'Strategybin', 'Daanlucas']
facebook_venues = [FacebookGroup(name) for name in facebook_groups]

# Actors
actor_names = ['igor stanis', 'john smith', 'mary jane', 'alex smith', 'yuri gaslov', 'alex petrovski', 'sara yeltsin']
actors = [Actor(name) for name in actor_names]

# Actions
actions = []

for hashtag in twitter_venues:
    actor_idx = randint(0, len(actors)-1)
    actor = actors[actor_idx]
    hl = HashtagLatch(hashtag, actor)
    actions.append(hl)


# events = []
# for _ in range(100):
#     action_i = randint(0,len(actions))
#     action = actions[action_i]

#     actor_i = randint(0,len(actors))
#     actor = actors[actor_i]

#     venue_i = randint(0,len(venues))
#     venue = venues[venue_i]

#     events.append(Event(action, actor, venue))

# events_json = [event.toJSON() for event in events]

data = {
    "terrain": terrain,
    "actions": actions
}

with open('./output/data1.json', 'w') as f:
    json.dump(data, f)
