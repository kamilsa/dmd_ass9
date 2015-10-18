__author__ = 'kamil'


class bucket:
    __size = 5

    def __init__(self):
        self.m = {}
        self.d = 0

    def full(self):
        return len(self.m) > self.__size

    def put(self, k, v):
        self.m[k] = v

    def get(self, k):
        return self.m.get(k)


class EH:
    def __init__(self):
        self.gd = 0  # global depth
        p = bucket()
        self.pp = [p]

    def get_page(self, k):
        h = hash(k)
        p = self.pp[h & (( 1 << self.gd) - 1)]
        return p

    def put(self, k, v):
        p = self.get_page(k)
        if p.full() and p.d == self.gd:
            self.pp = self.pp + self.pp
            self.gd += 1

        if p.full() and p.d < self.gd:
            p.put(k, v);
            p1 = bucket()
            p2 = bucket()
            for k2 in p.m.keys():
                v2 = p.m[k2]
                h = k2.__hash__()
                h = h & ((1 << self.gd) - 1)
                if (h | (1 << p.d) == h):
                    p2.put(k2, v2)
                else:
                    p1.put(k2, v2)
            l = []
            for i in range(0, len(self.pp)):
                if self.pp[i] == p:
                    l.append(i)
            for i in l:
                if i | ( 1 << p.d) == i:
                    self.pp[i] = p2

                else:
                    self.pp[i] = p1

            p1.d = p.d + 1
            p2.d = p1.d
        else:
            p.put(k, v)

    def get(self, k):
        p = self.get_page(k)
        return p.get(k)