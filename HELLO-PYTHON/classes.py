### clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson()) 

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Gelo", "Figueroa")
print(my_person.name)
print(my_person.full_name)
my_person.walk()
