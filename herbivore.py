from animal import Animal


class Herbivore(Animal):
    def __init__(self, name, age, specie, energy_level, favorite_food, grazing_time, sound="snort", visitor_can_feed = True):
        super().__init__(name, age, specie, sound, energy_level, visitor_can_feed)
        self.favorite_food = favorite_food
        self.grazing_time = grazing_time

    def eat(self):
        super().eat()
        return f"{self.name} is eating plants."

    def graze(self):
        self.energy_level += self.grazing_time * 3
        return (f"{self.name} is grazing for {self.grazing_time} hours.")

    def make_sound(self):
        return f"{self.name} {self.sound}!!!"

    def hide(self):
        return f"{self.name} is hiding from visitors."

    def sleep(self):
        return super().sleep()

    def __str__(self):
        return (f"Here we have {self.name}, a {self.specie} who is {self.age} years old. \nWith an energy level of {self.energy_level}, they spend about {self.grazing_time} hours a day peacefully grazing. Their favorite snack? Definitely {self.favorite_food}.")

    def display_behavior(self):
        raise NotImplementedError("Subclasses must implement this method.")
