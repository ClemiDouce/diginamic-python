import random


def create_tab(size):
    return [random.randint(1, 1000) for i in range(size)]


def pouet():
    pass


print(create_tab(20))
