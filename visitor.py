import random
from animal import Animal


class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name}, Age: {self.age} is visiting the zoo.")

    def visit(self, animal):
        print(f"{self.name} is visiting {animal.name} in the zoo.")

    def _get_one_animal(self, animal):
        choosed = random.randint(0, len(animal)-1)
        return choosed

    def _feed_more(self):
        return random.choice([True, False])

    def feed_animal(self, animal):
        if not isinstance(animal, Animal):
            creature = self._get_one_animal(animal)
            print(
                f"Here comes {animal[creature].name}! Get ready to feed them.")
            print(
                f"{self.name} is feeding {animal[creature].name} with {animal[creature].visitor_food}.")
            animal[creature].be_feed()
            check_feed_more = self._feed_more()
            if check_feed_more == True:
                if self._check_feed_animal() == 'y':
                    self.feed_animal(animal)
        else:
            print(f"{self.name} is feeding {animal.name} with {animal.visitor_food}.")
            animal.be_feed()

    def _check_feed_animal(self):
        global continue_tour
        while True:
            want_feed_animal = input(
                f"Do you want to feed them? (y/n) \n").strip()
            if want_feed_animal == "y" or want_feed_animal == "n":
                return want_feed_animal
            elif want_feed_animal == "exit":
                continue_tour = False
                break
            else:
                print("Invalid answer!")
                continue

    def visit_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} is visiting the {animal.specie} in the zoo.")
            print(animal.__str__())
            print(animal.make_sound())
            if animal.visitor_can_feed:
                if self._check_feed_animal() == 'y':
                    self.feed_animal(animal)
        else:
            print(
                f"{self.name} is visiting the {animal[0].specie}s in the zoo. Here we have: \n")
            for resident in animal:
                print(resident.__str__())
                print(f"{resident.make_sound()} \n")
            if animal[0].visitor_can_feed:
                if self._check_feed_animal() == 'y':
                    self.feed_animal(animal)
