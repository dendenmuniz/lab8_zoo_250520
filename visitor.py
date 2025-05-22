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

    def feed_animal(self, animal, food):
        if not isinstance(animal, Animal):
            creature = random.randint(1, len(animal)-1)
            print(
                f"Here comes {animal[creature].name}! Get ready to feed them.")
            print(
                f"{self.name} is feeding {animal[creature].name} with {food}.")
            animal[creature].be_feed()
        else:
            print(f"{self.name} is feeding {animal.name} with {food}.")
            animal.be_feed()
    
    def __check_animal(animal):
        can_be_feed = False
        if isinstance(animal, Animal):
            if animal.specie:
              return animal
        else:
            pass
        

    def __check_feed_animal(animal):
        while True:
          want_feed_animal = input(f"Do you want to feed tem? (y/n) \n")
          if not want_feed_animal == "y" or not want_feed_animal == "n":
              print("Invalid answer!")
              continue
          else:
              if animal.specie == "zebra":
                  return "hay"
              elif animal.specie == "giraffe":
                  return "leafs"
              elif animal.specie == "penguin":
                  return "fish"
              break
                 

    def visit_animal(self, animal):
      if isinstance(animal, Animal):
          print(f"{self.name} is visiting the {animal.specie} in the zoo.")
          print(animal.__str__())
          print(animal.make_sound())
          if animal.specie == "zebra":
              want_feed_animal = (
                  input(f"Do you want to feed {animal.name}? (y/n) \n")).lower()
              if want_feed_animal == "y":
                  self.feed_animal(animal, "hay")
              elif not want_feed_animal == "y" or not want_feed_animal == "n":
                  print("invalid answer!")
      else:
          print(
              f"{self.name} is visiting the {animal[0].specie}s in the zoo. Here we have: \n")
          for resident in animal:
              print(resident.__str__())
              print(f"{resident.make_sound()} \n")

          want_feed_animal = (
              input(f"Do you want to feed the {animal[0].specie}s? (y/n) \n")).lower()
          if want_feed_animal == "y":
              self.feed_animal(animal, "hay")
