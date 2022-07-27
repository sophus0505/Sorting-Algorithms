from functools import total_ordering
import numpy as np 

@total_ordering
class CountCompares:
    def __init__(self, elem):
        self.elem = elem
        self.compares = 0

    def reset(self):
        self.compares = 0

    def __eq__(self, other):
        return self.elem == other.elem

    def __lt__(self, other):
        self.compares += 1
        if not isinstance(self, CountCompares):
            print("cock")
        return self.elem < other.elem

    def __repr__(self):
        return self.elem.__repr__()

    def int(self):
        return self.elem

    @property
    def length(self):
        if self.elem == 0:
            return 1
        return int(np.log10(self.elem)) + 1


  

