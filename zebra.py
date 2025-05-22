from herbivore import Herbivore

class Zebra(Herbivore):
    def __init__(self, name, age, energy_level, favorite_food):
        super().__init__(name, age, "zebra", energy_level, favorite_food, 8, "whinny")

    def graze(self):
        self.energy_level += self.grazing_time * 2
        return (f"{self.name} is grazing for {self.grazing_time} hours.")
          
    def display_behavior(self):
        self.energy_level -= 3
        return f"{self.name} is running in its enclosure."
    
    def sleep(self):
        print(f"{self.name} go in its shelter to sleep.")
        return super().sleep()
    
    def be_feed(self):
        self.energy_level += 1
        print("munch... munch... *snort*")