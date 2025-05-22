from carnivore import Carnivore
import random


class Penguin(Carnivore):
    actions = [
        {"behavior": "is swimming in the water.", "energy": "-", "value": 2},
        {"behavior": "is slading on the ice.", "energy": "-", "value": 1},
        {"behavior": "is splashing water with its flippers.",
            "energy": "-", "value": 3},
    ]

    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food,
                         hunting_style, fang_length, "penguin", "squawk", True)
        self.visitor_food = "fish"

    def display_behavior(self):
        act = self.actions[random.randint(0, 2)]
        if act["energy"] == "+":
            self.energy_level += act["value"]
        else:
            self.energy_level -= act["value"]
        return f"{self.name} {act["behavior"]}"

    def be_feed(self):
        self.energy_level += 1
        print("chirp chirp gulp!")
        print(f"{self.name} chirps excitedly and gulps their food.")

    def __str__(self):
        return (f"{self.name} is a {self.specie}, {self.age} years old with an energy level of {self.energy_level}. \nTheir favorite food is {self.favorite_food}, and they’re excellent swimmers who can dive deep to catch their meals.")
