class Animal:
    def __init__(self, name, age, specie, sound, energy_level, visitor_can_feed = False):
        self.name = name
        self.age = age
        self.specie = specie
        self.sound = sound
        self.energy_level = energy_level
        self.visitor_can_feed = visitor_can_feed

    def eat(self):
        print(f"{self.name} is eating.")
        self.energy_level += 1

    def sleep(self):
        print(f"{self.name} is sleeping.")
        self.energy_level += 5

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")
