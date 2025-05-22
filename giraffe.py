from herbivore import Herbivore
import random


class Giraffe(Herbivore):
    actions = [
        {"behavior": "stretches its neck to reach the tallest leaves.",
            "energy": "+", "value": 4},
        {"behavior": "swings its neck playfully.", "energy": "-", "value": 5},
        {"behavior": "is slowly chewing its food.", "energy": "+", "value": 2},
    ]

    def __init__(self, name, age, energy_level, favorite_food):
        super().__init__(name, age, "giraffe", energy_level, favorite_food, 8, "snort", True)
        self.visitor_food = "leafs"

    def display_behavior(self):
        act = self.actions[random.randint(0, 2)]
        if act["energy"] == "+":
            self.energy_level += act["value"]
        else:
            self.energy_level -= act["value"]
        return f"{self.name} {act["behavior"]}"

    def sleep(self):
        print(f"{self.name} go in its shelter to sleep.")
        return super().sleep()

    def be_feed(self):
        self.energy_level += 1
        print(
            f"{self.name} gently pulls leaves from their hand with a long, purple tongue.")
        print("munch... rustle rustle...")
