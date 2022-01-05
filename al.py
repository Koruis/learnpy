# coding=utf-8
import random


class User:
    def __init__(self, fn, ln, couty):
        self.first_name = fn
        self.last_name = ln
        self.country = couty
        self.login_attempts = 0

    def describe_user(self):
        print("Following User info")
        print("User name: " + self.first_name + self.last_name)
        print("User Country: " + self.country)

    def greet_user(self):
        print("Hello! " + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts -= 1


class Admin(User):
    def __init__(self, fn, ln, couty, lst):
        super().__init__(fn, ln, couty)
        self.privileges = lst[:]

    def show_privileges(self):
        print("Admin " + self.first_name + self.last_name + " can: ")
        for l in self.privileges:
            print(l)


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(random.randint(1, self.sides))