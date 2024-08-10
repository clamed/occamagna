class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]
oldest_person = max(people, key=lambda person: person.age)
print(oldest_person.name)  # Output: "Bob"
