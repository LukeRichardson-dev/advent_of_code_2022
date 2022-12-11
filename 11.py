from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Monke:
    items: list[int]
    operation: Callable
    test: int
    pos: int
    neg: int
    count: int = 0
    add: int = 0
    mul: int = 1
    pwr: int = 1
    cache: dict[int, list] = field(default_factory=dict)

    def inspect(self):
        self.count += len(self.items)

        ret = [self.inspect_one(item) for item in self.items]
        self.items = []
        return ret
    
    def inspect_one(self, item):
        if (val := self.cache.get(item)) is not None:
            return val
        ret = (self.pos if (new := (self.do_op(item)))[0] else self.neg), new[1]
        self.cache[val] = ret
        return ret
    
    def do_op(self, x):
        m = self.test
        if self.add != 0:
            return ((m - x) % m) == m - self.add, x + self.add

        if self.mul != 1:
            prod = x * self.mul
            return not (self.mul % m and x % m), prod
        
        prod = x ** 2
        return x % m == 0, prod


TEST = [
    Monke([79, 98], lambda x: x * 19, 23, 2, 3, mul=19),
    Monke([54, 65, 75, 74], lambda x: x + 6 , 19, 2, 0, add=6),
    Monke([79, 60, 97], lambda x: x ** 2, 13, 1, 3, pwr=2),
    Monke([74], lambda x: x + 3 , 17, 0, 1, add=3),
]

def cmb(monkes):

    counts = [i.count for i in monkes]

    m1 = max(counts)
    counts.remove(m1)
    m2 = max(counts)

    return m1 * m2

REAL = [
    Monke([85, 77, 77], lambda x: x * 7 , 19, 6, 7, mul=7),
    Monke([80, 99], lambda x: x * 11, 3, 3, 5, mul=11),
    Monke([74, 60, 74, 63, 86, 92, 80], lambda x: x + 8 , 13, 0, 6, add=8),
    Monke([71, 58, 93, 65, 80, 68, 54, 71], lambda x: x + 7 , 7, 2, 4, add=7),
    Monke([97, 56, 79, 65, 58], lambda x: x + 5 , 5, 2, 0, add=5),
    Monke([77], lambda x: x + 4 , 11, 4, 3, add=4),
    Monke([99, 90, 84, 50], lambda x: x ** 2, 17, 7, 1, pwr=2),
    Monke([50, 66, 61, 92, 64, 78], lambda x: x + 3 , 2, 5, 1, add=3),
]

if __name__ == '__main__':

    with open('11.txt') as f:
        inp = f.read()

    monkes = TEST.copy()
    for _ in range(2000):
        for i in monkes:
            for to, w in i.inspect():
                monkes[to].items.append(w)

    counts = [i.count for i in monkes]
    print(counts)
    print(cmb(monkes))

    monkes = REAL.copy()
    for _ in range(200):
        for i in monkes:
            for to, w in i.inspect():
                monkes[to].items.append(w)

    counts = [i.count for i in monkes]
    print(counts)
    print(cmb(monkes))