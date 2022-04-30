import random
import time

#global variables here
water = [[]]
water_size = 10
ships_num = 2
bullets_rem = 40
game_lost = False
ships_lost = 0
ship_positions = [[]]
OPTIONS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_water_and_place_ship(start_row, end_row, start_col, end_col):
    #checks a spot to place the ships
    global water
    global ship_positions

    ongoing = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if water[r][c] != ".":
                all_valid = False
                break
    if ongoing:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                water[r][c] = "O"
    return ongoing

def ship_on_water(row, col, direction, length):
    #ships will be placed based on direction
    global water_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= water_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= water_size:
            return False
        end_row = row + length

    return ship_on_water(start_row, end_row, start_col, end_col)

def create_water():
    """
    Will create a 10x10 water and randomly place down ships
    of different sizes in different directions
    """
    global water
    global water_size
    global ships_num
    global ship_positions

    random.seed(time.time())

    rows, cols = (water_size, water_size)

    water = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        water.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != ships_num:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if ship_on_water(row, col, direction, length)(random_row, random_col, direction, water_size):
            num_of_ships_placed += 1
            