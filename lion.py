from carnivore import Carnivore
import random


class Lion(Carnivore):
    actions = [
        {"behavior": "is surveying the area with a calm gaze.",
            "energy": "-", "value": 0},
        {"behavior": "is pacing slowly along the fence.", "energy": "-", "value": 2},
        {"behavior": "is grooming their mane lazily.", "energy": "-", "value": 1},
        {"behavior": "is tearing into a chunk of meat.", "energy": "+", "value": 4},
    ]

    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food,
                         hunting_style, fang_length, "lion", "roar", False)

    def __str__(self):
        return (f"Meet {self.name}, a proud {self.specie} at {self.age} years old. \nWith an energy level of {self.energy_level}, they prefer to hunt using a {self.hunting_style} approach. \nTheir favorite meal? {self.favorite_food}. And just look at those fangs — measuring {self.fang_length} cm!")

    def display_behavior(self):
        act = self.actions[random.randint(0, 2)]
        if act["energy"] == "+":
            self.energy_level += act["value"]
        else:
            self.energy_level -= act["value"]
        return f"{self.name} {act["behavior"]}"
