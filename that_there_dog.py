import pprint

class MyDog:


    def __init__(self, breed, name, age, color, is_asleep=False):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.is_asleep = is_asleep

    def walk(self):
        return print(f"{self.name} is walking!")

    def eat(self):
        return print(f"{self.name} is eating food!")

    def sleep(self):
        self.is_asleep = True
        return print(f"{self.name} is sleeping!")

    def wake_up(self):
        self.is_asleep = False
        return print (f"{self.name} is waking up!")


zelda = MyDog("Labrador", "Zelda", 7, "Yellow")
cynder = MyDog("Miniature Pincher", "Cynder", 16, "Tan")

zelda.walk()
zelda.sleep()

cynder.eat()
cynder.sleep()

zelda.wake_up()
zelda.eat()

pprint.pprint(dir(zelda))
pprint.pprint(dir(cynder))
