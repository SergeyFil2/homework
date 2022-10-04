from pprint import pprint
class Person:
    def __init__(self, name, age, address, gender):
        self.name, self.age, self.address, self.gender = name, age, address, gender
        self.key = (name, address)

    def __repr__(self):
        return "Person('%s', '%s', '%s', '%s')" % (self.name, self.age, self.address)


sergey = Person("Сергей", 20, "Ленина, 26, 69")

people = {
    sergey.key: sergey,
}
pprint(people)
pprint(people[sergey.key])
pprint(people)