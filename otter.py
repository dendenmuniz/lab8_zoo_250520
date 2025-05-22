from carnivore import Carnivore
import random


class Otter(Carnivore):
    actions = [{"behavior": "is juggling small rocks with playful skill.", "energy": "-", "value": 3},
               {"behavior": "is diving and swirling underwater.",
                   "energy": "-", "value": 3},
               {"behavior": "is cracking open a shell with their favorite stone.",
                   "energy": "-", "value": 2},
               {"behavior": "is sliding down a muddy slope.",
                   "energy": "-", "value": 4}
    ]

    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food,
                         hunting_style, fang_length, "otter", "chirp", False)

    def display_behavior(self):
        act = self.actions[random.randint(0, 2)]
        if act["energy"] == "+":
            self.energy_level += act["value"]
        else:
            self.energy_level -= act["value"]
        return f"{self.name} {act["behavior"]}"

    def sleep(self):
        self.energy_level += 5
        return (f"{self.name} is holding hands with its mate while sleeping.")
