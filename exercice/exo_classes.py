class MaClass:
    x = 23
    y = x + 5

    def affiche(self):
        z = 42
        print(f"Z={z} / X={self.x} / Y={self.y}")


class Vector2:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def affiche(self):
        print(f"X:{self.x} | Y:{self.y}")

    def __add__(self, other):
        return {"x": self.x + other.x, "y": self.y + other.y}


test = MaClass()
test.affiche()

vec = Vector2()
vec2 = Vector2(10, 20)
vec3 = Vector2(20, 40)

print(vec)
print(vec2)

print(vec3 + vec2)
