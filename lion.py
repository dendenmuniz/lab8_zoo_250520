from carnivore import Carnivore

class Lion(Carnivore):
    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length):
        super().__init__(name, age, energy_level, favorite_food, hunting_style, fang_length, "lion", "roar" )
        

    def roar(self):
        return f"{self.name} is roaring!!!"
    
    def hunt(self):
        self.energy_level -= 5
        return f"{self.name} is hunting rabbits in its vivarium."
    
    def __str__(self):
        return (f"Meet {self.name}, a proud {self.specie} at {self.age} years old. \nWith an energy level of {self.energy_level}, they prefer to hunt using a {self.hunting_style} approach. \nTheir favorite meal? {self.favorite_food}. And just look at those fangs — measuring {self.fang_length} cm!")
    
    def display_behavior(self):
        return f"{self.name} is patrolling its territory."