from pprint import pprint
class NewInt(int):
    def __add__(self, x):
        return super().__add__(x+1)

y = NewInt(int(input()))
z = y + 2
pprint(z)
