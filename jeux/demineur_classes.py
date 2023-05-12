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
        self.affiche_map()
        # self.assign_cell_value()

    def check_coords(self, coord):
        if coord[0] < 0 or coord[0] >= self.map_size:
            return False
        elif coord[1] < 0 or coord[1] >= self.map_size:
            return False
        else:
            return True

    def get_tile_value(self, x, y):
        cell = next((el for el in self.tile_list if el.x == x and el.y == y), None)
        if cell is not None:
            return cell.value

    def get_tile_neighbour(self, tile):
        neighbour_pos = [(tile.x + x, tile.y + y) for x in range(-1, 2) for y in range(-1, 2)]
        neighbour_pos.remove((tile.x, tile.y))
        return list(filter(self.check_coords, neighbour_pos))

    def affiche_map(self):
        # print(self.tile_list)
        for i in self.tile_list:
            for tile in i:
                print(tile)

    def assign_cell_value(self):
        for tile in self.tile_list:
            if tile.value != "X":
                neighbours = list(filter(lambda t: (t.x, t.y) in self.get_tile_neighbour(tile), self.tile_list))
                total_value = sum([1 if tile.value == "X" else 0 for tile in neighbours])
                print(total_value, tile)
                tile.value = total_value


my_map = Map()
my_map.generate_map(10)
# my_map.affiche_map()
