import json
from random import choice
from terrain import Terrain
from venue import Venue
from domain import Domain
from actor import Actor
from action import Action
from event import Event

terrain = Terrain()
domains = [Domain() for _ in range(4)]

venues = []
for _ in range(200):
    domain = choice(domains)
    new_venue = Venue(domain)
    venues.append(new_venue)

actors = [Actor() for _ in range(100)]

events = []
for _ in range(2000):
    action = Action()
    actor = choice(actors)
    venue = choice(venues)
    new_event = Event(action, actor, venue)
    events.append(new_event)

data = {
    "scenario": {
        "name": "cybersocial1",
    },
    "data": {
        "terrain": terrain.serialize(),
        "domains": [d.serialize() for d in domains],
        "venues": [v.serialize() for v in venues],
        "actors": [a.serialize() for a in actors],
        "events": [e.serialize() for e in events]
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f)

