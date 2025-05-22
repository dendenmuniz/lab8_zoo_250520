from herbivore import Herbivore
import random


class Zebra(Herbivore):
    actions = [
        {"behavior": "is galloping across the enclosure with energy.",
            "energy": "-", "value": 4},
        {"behavior": "is grazing peacefully in the sun.", "energy": "+", "value": 1},
        {"behavior": "is flicking its tail to chase away flies.",
            "energy": "-", "value": 1},
        {"behavior": "is snorting and stomping lightly.", "energy": "-", "value": 2},
        {"behavior": "is rubbing its head against a tree trunk.",
            "energy": "-", "value": 2},
        {"behavior": "is rolling playfully in the dust.", "energy": "-", "value": 3},
    ]

    def __init__(self, name, age, energy_level, favorite_food):
        super().__init__(name, age, "zebra", energy_level, favorite_food, 8, "whinny", True)
        self.visitor_food = "hay"

    def graze(self):
        self.energy_level += self.grazing_time * 2
        return (f"{self.name} is grazing for {self.grazing_time} hours.")

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
        print("munch... munch... *snort*")
