from turtle import *


#
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


def triangle(size, filled=False):
    if filled:
        color("black", "yellow")
        begin_fill()
    for _ in range(3):
        forward(size)
        left(120)

    if filled:
        end_fill()


def carre(size, filled=False):
    if filled:
        color("black", "blue")
        begin_fill()
    for _ in range(4):
        forward(size)
        left(90)

    if filled:
        end_fill()


def hexagone(size, filled=False):
    if filled:
        color("black", "red")
        begin_fill()
    for _ in range(6):
        forward(size)
        left(60)

    if filled:
        end_fill()


carre(100, True)
triangle(300, True)
hexagone(100, True)
