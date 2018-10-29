class Tup:
    def __init__(self, *args):
        self.inner = tuple(i for i in args)

    def __sub__(self, other):
        other_value = other if type(other) is tuple else other.inner
        return tuple(s - o for s, o in zip(self.inner, other_value))

    def __add__(self, other):
        other_value = other if type(other) is tuple else other.inner
        return tuple(s + o for s, o in zip(self.inner, other_value))

    def __repr__(self):
        return '(' + ', '.join(str(digit) for digit in self.inner)+')'


k = Tup(2, 3, 5, 6)
d = Tup(4, 3, 2, 1)

# print(k-d)
print('________________________\n\n\n')
print(k + (1, 2, 3, 4))
print(k)





# def __sub__(self, other):
#     if type(other) is tuple:
#         return tuple(s - o for s, o in zip(self.inner, other))
#     else:
#         return tuple(s - o for s, o in zip(self.inner, other.inner))
#
#
# def __add__(self, other):
#     other_value = other if type(other) is tuple else other.inner
#
#     return tuple(s + o for s, o in zip(self.inner, other_value))

# if type(other) is tuple:
#     return tuple(s + o for s, o in zip(self.inner, other))
# else:
#     return tuple(s + o for s, o in zip(self.inner, other.inner))