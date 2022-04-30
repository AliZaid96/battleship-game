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
                ongoing = False
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

def print_water():
    """
    Will print the grid with rows A-J and columns 0-9
    """
    global water
    global OPTIONS

    debug_mode = True

    OPTIONS = OPTIONS[0: len(water) + 1]

    for row in range(len(water)):
        print(alphabet[row], end=") ")
        for col in range(len(water[row])):
            if water[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(water[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(water[0])):
        print(str(i), end=" ")
    print("")



def true_rocket_spot():
    #this function checks if the rocket placement is correct
    global OPTIONS
    global water

    true_placement = False
    row = -1
    col = -1
    while true_placement is False:
        placement = input("Enter row (A-J) and column (0-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        row = OPTIONS.find(row)
        if not (-1 < row < water_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        col = int(col)
        if not (-1 < col < water_size):
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
            continue
        if water[row][col] == "#" or water[row][col] == "X":
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if water[row][col] == "." or water[row][col] == "O":
            true_placement = True

    return row, col


def ships_sunk(row, col):
    #if the whole ship is sunk, we increment the value of ship sunked
    global ship_positions
    global water

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True

def shoot_rocket():
    #update where rocket was shot 
    global water
    global ships_lost
    global bullets_rem

    row, col = true_rocket_spot()
    print("")
    print("----------------------------")

    if water[row][col] == ".":
        print("unlucky, try again")
        water[row][col] = "#"
    elif water[row][col] == "O":
        print("BINGO", end=" ")
        water[row][col] = "X"
        if ships_sunk(row, col):
            print("You finally destroyed a ship!")
            ships_lost += 1
        else:
            print("Perfect hit!")

    bullets_rem -= 1