
from animal import Animal


class ZooGuide:
    def __init__(self, name, age, experience_years, favorite_animal):
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.favorite_animal = favorite_animal

    def present_theirself(self):
        return (f"Hi there! I’m {self.name}, your guide today. After {self.experience_years} years here, I have a soft spot for {self.favorite_animal}s. \nI’ll be guiding you through our Zoo this morning, so get ready for some splashes and surprises.\n")

    def present_animals(self, animals_list):
        print('Those are ours animals:')
        for key, animal in animals_list.items():
            if isinstance(animal, Animal):
                print(f"{key}. {animal.specie}")
            else:
                if isinstance(animal[0], Animal):
                    print(f"{key}. {animal[0].specie}")
