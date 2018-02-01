# example class

class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    #returns a string representation of self
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

    def intersect(self, other):
        assert type(other) == type(self)
        res = intSet()
        for item in other.vals:
            if self.member(item):
                res.vals.append(item)
        return res

    def __len__(self):
        return len(self.vals)

s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
# print(s)
s.member(3)
s.remove(3)
print(s.__str__())
