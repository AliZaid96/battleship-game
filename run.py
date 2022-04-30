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
    #Based on direction will call helper method to try and place a ship on the grid
    global water_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return ship_on_water(start_row, end_row, start_col, end_col)