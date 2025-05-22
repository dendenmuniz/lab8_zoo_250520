from carnivore import Carnivore

class Penguin(Carnivore):
    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food, hunting_style, fang_length, "penguin", "squawk", True)
        
    def swim(self):
        self.energy_level -= 2
        return f"{self.name} is swimming in the water."
    
    def display_behavior(self):
        self.energy_level -= 1
        return f"{self.name} is sliding on the ice."
    
    def splash(self):
        self.energy_level -= 3
        return f"{self.name} is splashing water with its flippers."
    
    def be_feed(self):
        self.energy_level += 1
        print("chirp chirp gulp!")
        print(f"{self.name} chirps excitedly and gulps their food.")
    
    def __str__(self):
        return (f"{self.name} is a {self.specie}, {self.age} years old with an energy level of {self.energy_level}. \nTheir favorite food is {self.favorite_food}, and they’re excellent swimmers who can dive deep to catch their meals.")
    
            