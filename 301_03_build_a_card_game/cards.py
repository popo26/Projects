import random

class Joker():
    def __init__(self):
        pass

class Club():
    def __init__(self):
        self.num = {"club": random.randint(1,14)}
        print(self.num)

    # def __str__(self):
    #     return f"This card is {self.num.keys()} {self.num.values()}"

class Diamond(Club):
    def __init__(self):
        super().__init__()
        self.num = {"diamond": random.randint(1,14)}

class Heart():
    def __init__(self):
        pass

class Spade():
    def __init__(self):
        pass