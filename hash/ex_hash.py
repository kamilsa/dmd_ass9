from page import page
import pickle
__author__ = 'kamil'


class EH:
    def __init__(self, filename):
        self.filename = filename
        self.gd = 0
        # p = Page()
        self.pp = [0]

    def get_page(self, k):
        h = hash(k)
        offset = self.pp[h & (( 1 << self.gd) - 1)]
        p = page(self.filename, offset)
        return p

    def put(self, k, v):
        p = self.get_page(k)
        if p.fit(v) == False and p.d == self.gd:
            self.pp = self.pp + self.pp
            self.gd += 1

        if p.fit(v) == False and p.d < self.gd:
            # p.put(k, v);
            p1 = page('temp1.txt', 0)
            p2 = page('temp2.txt', 0)
            for k2 in p.key_list:
                v2 = p.get(k2)
                h = k2.__hash__()
                h = h & ((1 << self.gd) - 1)
                if (h | (1 << p.d) == h):
                    p2.insert(v2)
                else:
                    p1.insert(v2)
            h = k.__hash__()
            h = h & ((1 << self.gd) - 1)
            if h | (1 << p.d) == h:
                p2.insert(v)
            else:
                p1.insert(v)
            l = []
            for i in range(0, len(self.pp)):
                if self.pp[i] == p._page_offset:
                    l.append(i)
            print(l)

            p1.setDoubling(p.d + 1)
            p2.setDoubling(p1.d)
            for i in l:
                if (i | ( 1 << p.d) == i):
                    self.pp[i] = i*500
                    to_put = p2.fetch()
                    f = open(self.filename, 'r+')
                    f.seek(self.pp[i])
                    f.write(to_put)
                    f.close()
                else:
                    self.pp[i] = i*500
                    to_put = p1.fetch()
                    f = open(self.filename, 'r+')
                    f.seek(self.pp[i])
                    f.write(to_put)
                    f.close()

            open('temp1.txt', 'w').close()
            open('temp2.txt', 'w').close()
            # p1.d = p.d + 1
            # p2.d = p1.d
        else:
            p.insert(v)

    def get(self, k):
        p = self.get_page(k)
        return p.get(k)