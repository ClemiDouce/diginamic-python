import random


class Tile:
    x: int = 0
    y: int = 0
    value = "0"
    showed: bool = True

    def __init__(self, x, y, value=""):
        if value:
            self.value = value
        self.x = x
        self.y = y

    def __str__(self):
        # if self.showed:
        #     return str(self.value)
        # else:
        #     return "H"
        return f"{self.x}:{self.y}"


class Map:

    def __init__(self):
        self.tile_list: list[list[Tile]] = []
        self.mine_count: int = 0
        self.map_size = 0

    def generate_mine_position(self, mine_number):
        rand_pos = set()
        while len(rand_pos) < mine_number:
            rand_pos.add((random.randint(0, self.map_size - 1), random.randint(0, self.map_size - 1)))
        return list(rand_pos)

    def generate_map(self, map_size: int):
        self.map_size = map_size
        self.tile_list = [[Tile(i, j) for i in range(map_size)] for j in range(map_size)]
        mine_pos = self.generate_mine_position(10)
        for pos in mine_pos:
            self.tile_list[pos[0]][pos[1]].value = "X"
        self.assign_cell_value()
        self.affiche_map()

    def check_coords(self, coord):
        if coord[0] < 0 or coord[0] >= self.map_size:
            return False
        elif coord[1] < 0 or coord[1] >= self.map_size:
            return False
        else:
            return True

    def get_tile_value(self, x, y):
        return self.tile_list[y][x].value

    def get_tile_neighbour(self, tile):
        coords = [(tile.y + new_y, tile.x + new_x) for new_y in range(-1, 2) for new_x in range(-1, 2)]
        coords.remove((tile.y, tile.x))
        coords = list(filter(self.check_coords, coords))
        return coords

    def affiche_map(self):
        for i in self.tile_list:
            for index, tile in enumerate(i):
                if index == len(i) - 1:
                    print(tile.value, end="\n")
                else:
                    print(tile.value, end="")

    def assign_cell_value(self):
        for ligne in self.tile_list:
            for tile in ligne:
                if tile.value == "X":
                    continue
                neighbours = self.get_tile_neighbour(tile)
                total_values = [1 if self.get_tile_value(t[1], t[0]) == "X" else 0 for t in neighbours]
                tile.value = sum(total_values)


my_map = Map()
my_map.generate_map(10)
# my_map.affiche_map()
