from sticker import Stickers

s = Stickers(3, 2)
s.init(0)
s.separate(0,0,1)
s.separate(1,1,3)
s.separate(1,0,2)
s.combine(1,2)
s.set(1,s.l)
s.combine(0,3)
s.combine(0,1)
s.display()
