from sticker import Stickers

s = Stickers(3, 2)
s.init(0)
#Separates the strands by the first bit
s.separate(0,0,1)
#Separates the strands with on first bit by the second bit
s.separate(1,1,3)
#Separates the strands with off first bit by the second bit
s.separate(1,0,2)
#Joins the strands with different values for first and second bit
s.combine(1,2)
#Sets the third bit to one
s.set(1,s.l)
#Joins all the strands in tube 0
s.combine(0,3)
s.combine(0,1)
#Shows the result tube
s.display()
