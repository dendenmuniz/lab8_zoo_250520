from animal import Animal
from lion import Lion
from hippo import Hippo
from giraffe import Giraffe
from zebra import Zebra
from penguin import Penguin
from otter import Otter
from visitor import Visitor
from zooGuide import ZooGuide
import random


def trigger_display_behavior(animal):
    if random.choice([True, False]):
      if not isinstance(animal, Animal):
          creature = random.randint(1, len(animal)-1)
          print(animal[creature].display_behavior())
      else:
          print(animal.display_behavior())


def distribute_food(animals):
    for animal in animals:
        food = animal.favorite_food
        print(f"Zookeeper is feeding {animal.name} with {food}.")
        animal.eat(food)


def check_energy_levels(animals):
    for animal in animals:
        if animal.energy_level < 50:
            print(f"{animal.name} needs more food and sleep!")
        else:
            print(f"{animal.name} is well-fed and happy!")

def main():
    lion = Lion("Alex", 5, 80, "steak", "stalk", 5)
    penguins = [
        Penguin("Skipper", 4, 90, "krill sushi", "swim", 2),
        Penguin("Kowalski", 3, 60, "ice-cold anchovy deluxe", "swim", 2),
        Penguin("Rico", 4, 85, "secret stash of squid rings", "swim", 2),
        Penguin("Private", 2, 70, "frozen sardine popsicle", "swim", 2)
    ]
    otter = [
        Otter("Otto", 4, 60, "rock-smashed mussels", "dive", 3),
        Otter("Nora", 4, 70, "seaweed salad", "dive", 3),
        Otter("Mochi", 2, 80, "clam chowder", "dive", 3),
        Otter("Pebbles ", 1, 75, "sea cucumber sushi", "dive", 3)
    ]
    zebra = Zebra("Marty", 4, 60, "crunchy haysticks")
    hippo = Hippo("Gloria", 6,  70, "riverbank salad")
    giraffe = [
        Giraffe("Melman", 7,  75, "acacia leaf wrap"),
        Giraffe("Gigi", 5,  80, "tall tree salad"),
        Giraffe("Maximus", 6,  80, "tender twigs"),
    ]

    zoo_animals = {1: lion, 2: penguins,
                   3: otter, 4: zebra, 5: hippo, 6: giraffe}
    
    zoo_guide = ZooGuide("John", 32, 4, "otters")

    print("Welcome to The Madagascar zoo!")
    print("If you want to quit, type 'exit'.")
    name = input("What's your name? \n")
    age =  input("What's your age? \n")
    visitor = Visitor(name, age)
    
    print(f"Welcome {visitor.name}! \nLet's start your visit.")
    print(zoo_guide.present_theirself())
    zoo_guide.present_animals(zoo_animals)

    continue_tour = True
    while continue_tour:
        user_input = input(
        "which animal do you want to visit now? (enter the corresponding number) \n")
        if user_input.lower() == "exit":
            print("Thanks for your visit!")
            break
        elif not user_input.isnumeric():
            print(f"Please enter a valid number")
        elif int(user_input) in zoo_animals:
          visiting_animal = int(user_input)
          visitor.visit_animal(zoo_animals[visiting_animal])
          trigger_display_behavior(zoo_animals[visiting_animal])
        else:
          print("Number invalid!")  


main()
