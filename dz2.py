class kit:
    def __init__(self, name=None, age=None, laps=None):
        self.name = name
        self.age = age
        self.laps = laps
    def __str__(self):
        return f"Привіт мене звати {self.name} я {self.yearOfBirdth()} року народження. \nСкільки в мене лап - {self.laps}"
    def yearOfBirdth(self):
        return 2022 - self.age
kitByba = kit(name = "Byba", age=2, laps=4)
print(kitByba)
