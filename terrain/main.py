import json
from random import choice
from terrain import Terrain
from venue import Venue
from domain import Domain
from actor import Actor
from action import Action

# t = Terrain()

# data = t.serialize()
# with open('data.json', 'w') as f:
    # json.dump(data, f)

domains = []
for i in range(4):
    args = {
        "venues": []
    }
    domains.append(Domain())

actors = []
domains = []
venues = []

def generate_random_actions(num_actions):
    # Generate actions
    return [Action() for i in range(num_actions)]

def generate_terrain_from_actions(actions=[]):
    args = {
        "actions": actions
    }
    return Terrain(args)

# This simulates processing raw data into CADE format
actions = generate_random_actions(100)

# This simulates creating a map from that CADE data
terrain = generate_terrain_from_actions(actions)


