from sticker import Stickers
from itertools import permutations

try:
    range = xrange
except:
    pass

s = Stickers(5, 5)
s.init(0)
for e in permutations(range(5), 2):
    s.separate(e[0], 0, 1, 2)
    s.separate(e[1], 1, 3, 4)
    s.discard(3)
    s.combine(2, 4, 0)
for i in range(4):
    for j in range(i, -1, -1):
        s.separate(i+1, j, j+1)
        s.combine(j+1, j+1)
for a in range(5, 0, -1):
    if a in s.tubes:
        s.display()
        break
