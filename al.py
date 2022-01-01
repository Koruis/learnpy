# coding=utf-8


class Zbl:
    """wow"""

    def __init__(self):
        print("zbl stablished.")
        self.name = "anana"
        self.age = 27

    def playgames(self):
        print("zbl playing games.")

    def working(self):
        print("zbl is working with python.")


person = Zbl()

person.working()

person.playgames()

print(person.age)