from sticker import Stickers

try:
    range = xrange
except:
    pass

B = 3 # number of bags
A = 3 # number of types objects
K = B + A # number of bits in the strand
C = [[1, 2], [1], [3]] # objects of each bag
s = Stickers(K, B) # library (K, B)
s.init('T0') # initializes in tube T0

# marks the types of objects present
for i in range(B):
    s.separate(i, 'T0', 'Ton', 'Toff')
    for j in range(0, len(C[i])):
        s.set('Ton', B + C[i][j] - 1)
    s.combine('Ton', 'Toff', 'T0')

# discards the sequences that lack all types of objects
for i in range(B, B + A):
    s.separate(i, 'T0', 'T0', 'Tbad')
    s.discard('Tbad')

# separates the strands in tubes according to the amount of bags
for i in range(B):
    for j in range(i, -1, -1):
        Tj = 'T' + str(j)
        # tube_on = tube_aux, tube_off = Tj
        s.separate(i + 1, Tj, 'tube_aux')
        Tj_plus1 = 'T' + str(j + 1)
        # Tj_plus1 = Tj_plus1 + 'tube_aux'
        s.combine(Tj_plus1, 'tube_aux')

for a in range(B, 0, -1):
    tube_name = 'T' + str(a)
    if s.tubes.get(tube_name):
        print(tube_name, s.tubes[tube_name])
        break
