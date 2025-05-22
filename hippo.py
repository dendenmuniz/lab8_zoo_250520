from herbivore import Herbivore
import random

class Hippo(Herbivore):
    actions = [
        {"behavior": "is swimming in the water.", "energy": "-", "value": 2},
        {"behavior": "is wallowing in the mud.", "energy": "-", "value": 3},
        {"behavior": "is yawning wide, showing off their massive jaws.", "energy": "-", "value": 0},
    ]
    def __init__(self, name, age, energy_level, favorite_food):
        super().__init__(name, age, "hippo", energy_level, favorite_food, 8, "honk")

    def display_behavior(self):
        act = self.actions[random.randint(0,2)]
        print(act)
        if act["energy"] == "+":
            self.energy_level += act["value"]
        else:
            self.energy_level -= act["value"]
        return f"{self.name} {act.behavior}"

    def sleep(self):
        return(f"{self.name} sinks into the water and sleeps peacefully, surfacing to breathe without waking up.")
        
    def make_sound(self):
        return f"{self.name} {self.sound} loudly as it emerged from the water!!!"
    
    def __str__(self):
        return (f"Say hello to {self.name}, a {self.age}-year-old {self.specie} with an energy level of {self.energy_level}. \nHippos like {self.name} can weigh over 1,500 kilograms, and still spend hours swimming or dozing in the water. Their favorite treat? {self.favorite_food}, of course.”")