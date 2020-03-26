class Pokemon:
    def __init__(self, name: str, level: int, type: str):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = self.level * 50
        self.current_health = self.max_health
        self.knocked_out = False
        self.attack_power = self.level * 10

    def __repr__(self):
        return f"{self.name} is currently level {self.level}, is {self.type} type and has {self.current_health} of {self.max_health} maximum health"

    def lose_health(self, amount: int):
        if self.current_health - amount > 0:
            self.current_health -= amount
            print(f"{self.name} now has {self.current_health} of {self.max_health} maximum health")
        else:
            self.knocked_out = True
            self.current_health = 0
            print(f"{self.name} was knocked out")

    def heal(self, amount: int):
        if self.current_health + amount < self.max_health:
            self.current_health += amount
        else:
            self.current_health = self.max_health

        if self.current_health > 0:
            self.knocked_out = False
        print(f"{self.name} now has {self.current_health} of {self.max_health} maximum health")

    def attack(self, target):
        if self.type == target.type:
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power} damage")
            target.lose_health(self.attack_power)
        if self.type == "Fire" and target.type == "Grass":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power *2} damage")
            target.lose_health(self.attack_power * 2)
        if self.type == "Fire" and target.type == "Water":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power /2} damage")
            target.lose_health(self.attack_power / 2)

        if self.type == "Water" and target.type =="Fire":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power *2} damage")
            target.lose_health(self.attack_power * 2)
        if self.type == "Water" and target.type == "Grass":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power /2} damage")
            target.lose_health(self.attack_power / 2)

        if self.type == "Grass" and target.type == "Water":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power *2} damage")
            target.lose_health(self.attack_power * 2)
        if self.type == "Grass" and target.type == "Fire":
            print(f"{self.name} attacked {target.name} and caused him {self.attack_power /2} damage")
            target.lose_health(self.attack_power / 2)
