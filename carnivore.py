from animal import Animal


class Carnivore(Animal):
    def __init__(self, name, age, energy_level, favorite_food, hunting_style, fang_length, specie, sound, visitor_can_feed):
        super().__init__(name, age, specie, sound, energy_level, visitor_can_feed)
        self.favorite_food = favorite_food
        self.hunting_style = hunting_style
        self.fang_length = fang_length

    def eat(self):
        self.energy_level += 10
        return f"{self.name} is eating meat."

    def hunt(self):
        self.energy_level -= 5
        return f"{self.name} is hunting."

    def make_sound(self):
        return f"{self.name} {self.sound}!!!"

    def sleep(self):
        return super().sleep()

    def __str__(self):
        return (f"{self.name} is a {self.specie}, {self.age} years old with an energy level of {self.energy_level}. \nThey prefer a {self.hunting_style} hunting style and enjoy feasting on {self.favorite_food}. Their impressive fangs measure {self.fang_length} cm.")

    def display_behavior(self):
        raise NotImplementedError("Subclasses must implement this method.")
