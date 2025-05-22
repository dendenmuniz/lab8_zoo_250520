from carnivore import Carnivore

class Otter(Carnivore):
    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food, hunting_style, fang_length, "otter", "chirp")
        
    def display_behavior(self):
        self.energy_level -= 2
        return f"{self.name} is floating on its back in the water."
    
    def sleep(self):
        self.energy_level += 5
        return(f"{self.name} is holding hands with its mate while sleeping.")
        
    
    