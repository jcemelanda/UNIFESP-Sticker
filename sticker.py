from __future__ import print_function
from itertools import product
class Stickers:
    '''
    Sticker DNA computation implementation in Python
    '''
    def __init__(self, k, l):
        '''
        Startsa Stickers class

        k -> the number of bits in the strand
        l -> bit number for the actual data
        '''
        self.tubes = {}
        self.k = k
        self.l = l

    def init(self, tube_name):
        '''
        Creates atube containing all the binary combinations
        for the l first bits of each strand, and fils with zeros

        tube_name -> label for the tube that will be created
        '''
        tube = []
        for i in product(*[(0, 1)] * self.l):
            tube.append(list(i) + [0] * (self.k-self.l))
            self.tubes[tube_name] = tube
        print('init:\t', self.tubes)

    def set(self, tube, bit):
        '''
        Sets the bit passed for every strand in the tube to one

        tube -> the tube label
        bit -> the bit position in the strand
        '''
        for strand in self.tubes[tube]:
            strand[bit] = 1
        print('set:\t', self.tubes)

    def clear(self, tube, bit):
        '''
        Sets the bit passed for every strand in the tube to zero

        tube -> the tube label
        bit -> the bit position in the strand
        '''
        for strand in self.tubes[tube]:
            strand[bit] = 0
        print('clear:\t', self.tubes)

    def separate(self, bit, tube_origin, tube_on, tube_off=None):
        '''
        Separates the tube into two tubes, depending on the value of the
        passed bit assingning the strand to tube_on if 1 and tube_off if 0.

        If no tube_off is passed, it'll be the original tube

        bit -> the position of the desired bit
        tube_origin -> the tube from where the strands are taken
        tube_on -> the tube where the on strands are placed
        tube_off -> the tube where the off strands are placed
        '''

        tube1 = []
        tube2 = []
        for strand in self.tubes[tube_origin]:
            if strand[bit]:
                tube1.append(strand)
            else:
                tube2.append(strand)

        if tube_off == None:
            tube_off = tube_origin
        else:
            del(self.tubes[tube_origin])

        self.tubes[tube_on] = tube1
        self.tubes[tube_off] = tube2

        print('sep:\t', self.tubes)

    def combine(self, tube1, tube2, tube_destination=None):
        '''
        Combines twoo tubes into one other tube.
        If the destination is not passed, the combination goes to the first tube

        tube1 -> First tube to combine
        tube2 -> Second tube to combine
        tube_destination -> destination tube for the combination
        '''
        t1 = self.tubes[tube1] if tube1 in self.tubes else []
        t2 = self.tubes[tube2] if tube2 in self.tubes else []

        result_tube = t1 + t2

        if tube2 in self.tubes:
            del(self.tubes[tube2])

        if tube_destination == None:
            tube_destination = tube1
        else:
            del(self.tubes[tube1])
        self.tubes[tube_destination] = result_tube

        print('comb:\t', self.tubes)

    def discard(self, tube):
        '''
        Discards a tube and all its contents

        tube -> the tube label
        '''
        if tube in self.tubes:
            del(self.tubes[tube])
        print('disc:\t', self.tubes)

    def display(self):
        '''
        Shows the tubes of the system
        '''
        print('\t', self.tubes)


if __name__ == '__main__':
    s = Stickers(5, 2)
    s.init(0)
    s.set(0, 2)
    s.clear(0, 2)
    s.separate(1, 0, 1, 2)
    s.separate(0, 1, 0)
    s.combine(0, 1)
    s.combine(0, 2, 0)
    s.display()
