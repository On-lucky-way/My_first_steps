import collections

garden = collections.namedtuple('garden', ['green', 'tree'])
g = garden(10,2)
print(g[0]+g[1])
print(g.tree+g.green)
print(g[1])

from typing import NamedTuple

class Garden(NamedTuple):
    name: str
    icolor: str
garden = Garden('Tree','green')
print(garden[0:2])