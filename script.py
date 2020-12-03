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

# Create one terrain
# Create 4 random domains
# Create 200 random venues
# Create 2000 random actions
# Create 100 random people
# Create events that link action with venue

terrain = Terrain([1000,1000])
domains = [Domain() for _ in range(4)]
print(domains)

# with open('./output/data1.json', 'w') as f:
#     json.dump(data, f)
