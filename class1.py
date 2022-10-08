from itertools import product
from pprint import pprint

def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)

    return count/max(len(s1), len(s2)) > 0.6

class Person:

    def __init__(self, name=None, age=None, height=None):
        self.name = name
        self.age = age
        self.height = height

    def __eq__(self, obj):
        return (obj.name == None or self.name == None or compare(obj.name, self.name)) \
            and (obj.height == None or self.height == None or abs(obj.height - self.height) < 6)

    def __repr__(self):
        return f"Person('{self.name}', {self.age}, {self.height})"

def search_height(self, obj):
    return (obj.height < self.height)


to_search = [
    Person('Нташа', 18, 160),
    Person(height=120),
    Person(name='Нташа'),
]

height_to_search = Person(height=160)

people = [
    Person('Егор', 25, 170),
    Person('Сандра', 18, 159),
    Person('Степан', 30, 180),
    Person('Дима', 19, 161),
    Person('Руслан', 27, 183),
    Person('Наташа', 18, 155),
]
print('Рост больше 160:')
for y in people:
    if search_height(y, height_to_search):
        print(y)

print('Нечеткий поиск: ')
for p1, p2 in product(people, to_search):
    print(p1, p2, p1 == p2)