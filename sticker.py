from __future__ import print_function
from itertools import product
class Stickers:
    def __init__(self, k, l):
        self.tubes = {}
        self.k = k
        self.l = l

    def init(self, tube_name):
        tube = []
        for i in product(*[(0, 1)] * self.l):
            tube.append(list(i) + [0] * (self.k-self.l))
            self.tubes[tube_name] = tube
        print('init:\t', self.tubes)

    def set(self, tube, bit):
        for strand in self.tubes[tube]:
            strand[bit] = 1
        print('set:\t', self.tubes)

    def clear(self, tube, bit):
        for strand in self.tubes[tube]:
            strand[bit] = 0
        print('clear:\t', self.tubes)

    def separate(self, bit, tube_origin, tube_on, tube_off=None):

        tube1 = []
        tube2 = []
        for strand in self.tubes[tube_origin]:
            if strand[bit]:
                tube1.append(strand)
            else:
                tube2.append(strand)

        if not tube_off:
            tube_off = tube_origin
        else:
            del(self.tubes[tube_origin])

        self.tubes[tube_on] = tube1
        self.tubes[tube_off] = tube2

        print('sep:\t', self.tubes)

    def combine(self, tube1, tube2, tube_destination=None):

        result_tube = self.tubes[tube1] + self.tubes[tube2]
        del(self.tubes[tube2])
        if not tube_destination:
            tube_destination = tube1
        else:
            del(self.tubes[tube1])
        self.tubes[tube_destination] = result_tube

        print('comb:\t', self.tubes)

    def display(self):
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
