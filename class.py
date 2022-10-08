from pprint import pprint

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

