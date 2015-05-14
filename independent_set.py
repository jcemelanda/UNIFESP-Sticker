from sticker import Stickers
from itertools import permutations

try:
    range = xrange
except:
    pass

s = Stickers(5, 5)
s.init(0)
edges = ((0, 4), (4, 1), (1, 3), (3, 2))
for e in edges:
    s.separate(e[0], 0, 1)
    s.separate(e[1], 1, 2, 3)
    s.combine(0, 3)

for i in range(1, 5):
    s.discard(i)

for i in range(5):
    for j in range(i, -1, -1):
        s.separate(i, j, -(j+1))
        s.combine(j+1, -(j+1))

for a in range(5, 0, -1):
    if s.tubes.get(a):
        print(a, s.tubes[a])
        break
