from itertools import product
from pprint import pprint

#Описать классом ваши личные данные:

class Person:
    def __init__(self, name, age, address, gender, height, weight):
        self.name, self.age, self.address, self.gender, self.height, self.weight = name, age, address, gender, height, weight
        self.key = (name, address, gender)

    def __repr__(self):
        return "Person('%s', %s, '%s', '%s', %s, %s)" % (self.name, self.age, self.address, self.gender, self.height, self.weight)

sergey = Person("Сергей", 20, "Ленина, 26, 69", 'Mужской', 180, 66)

people = {
    sergey.key: sergey,
}
pprint(people[sergey.key])
pprint(people)

#Реализовать поиск по полям (рост > 120, имя Наташа) + нечеткий поиск

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
    Person('Нташа', 19, 120),
    Person(height=120),
    Person(name='Нташа'),
]

height_to_search = Person(height=120)

people = [
    Person('Егор', 25, 119),
    Person('Сандра', 18, 110),
    Person('Степан', 30, 180),
    Person('Дима', 19, 115),
    Person('Руслан', 27, 183),
    Person('Наташа', 18, 124),
]
print('Рост больше 120:')
for y in people:
    if search_height(y, height_to_search):
        print(y)

print('Нечеткий поиск: ')
for p1, p2 in product(people, to_search):
    print(p1, p2, p1 == p2)