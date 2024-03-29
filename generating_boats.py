import random

# --- COORDINATE ORIENTATION ---
#   1 2 3 4 5 6 7 8 9 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

#ships 2, 2, 2, 2, 3, 3, 3, 4, 4, 5
# 5 - Carrier
# 4 - Battleship
# 3 - Submarine
# 2 - Destroyer

def generate_all_coordinates():
    """() -> list
    Returns all 100 coordinates on the Battleship map in the form of a list."""
    all_coordinates = []
    for x in range(1, 11):
        for y in range(1, 11):
            coordinate = x, y
            all_coordinates.append(coordinate)
    return all_coordinates
            
def find_two_consecutive_coordinates(coordinate_list):
    """(list) -> list
    Finds and returns two coordinates that are consecutive out of a given list if there are any.
    """
    xvalues = []
    yvalues = []
    for coordinate in coordinate_list:
        xvalues.append(int(coordinate[0]))
        yvalues.append(int(coordinate[1]))
    
    for value in xvalues:
        index = xvalues.index(value)
        xcount = xvalues.count(value)
        if xcount > 1:
            difference = yvalues[index+1] - yvalues[index]
            if abs(difference) == 1:
                return [coordinate_list[index], coordinate_list[index+1]]
        
    for value in yvalues:
        index = yvalues.index(value)
        ycount = yvalues.count(value)
        if ycount > 1:
            difference = xvalues[index+1] - xvalues[index]
            if abs(difference) == 1:
                return [coordinate_list[index], coordinate_list[index+1]]

        
def generate_ship(size, available_coordinates):
    """(int, list) -> list
    Randomly generates a ship that has all positive coordinates and which all coordinates are on the 10x10 Battleship map.
    """
    while True:
        if len(available_coordinates) < 20:
            ship = find_two_consecutive_coordinates(available_coordinates)
            return ship
        else:
            starting_coor = random.choice(available_coordinates)
            orientation = random.randint(0, 1) # 0 is horizontal and 1 is vertical
            ship = []
            coors = starting_coor
            if orientation == 0:
                right_left = random.randint(0, 1) # 0 is right and 1 is left
                if right_left == 0:
                    for coor in range(size):
                        coors = coors[0] + 1, coors[1]
                        ship.append(coors)
                elif right_left == 1:
                    for coor in range(size):
                        coors = coors[0] - 1, coors[1]
                        ship.append(coors)
            elif orientation == 1:
                up_down = random.randint(0, 1) # 0 is up and 1 is down
                if up_down == 0:
                    for coor in range(size):
                        coors = coors[0], coors[1] - 1
                        ship.append(coors)
                elif up_down == 1:
                    for coor in range(size):
                        coors = coors[0], coors[1] + 1
                        ship.append(coors)
                    
            if is_positive(ship) and less_than_10(ship):
                    return ship

def is_positive(ship):   
    """(list) -> bool
    Checks if all coordinates in a ship are positive.
    """
    positive = True
    for coordinates in ship:
        for value in coordinates:
            if value <= 1:
                positive = False
    return positive
                

def less_than_10(ship):
    """(list) -> bool
    Checks if all coordinates in a ship are equal to or less than 10.
    """
    less_than_10 = True
    for coordinates in ship:
        for value in coordinates:
            if value > 10:
                less_than_10 = False
    return less_than_10

def ship_append(fleet, num, length, available_coordinates):
    """(list, int, int, list) -> list
    If the coordinates surrounding a ship are clear and not occupied, appends the ship to the fleet.
    """
    for boat in range(num):
        while True:
            ship = generate_ship(length, available_coordinates)
            if ship is None:
                print("Could not generate enemy fleet, trying again.")
                break
            if clear_surroundings(fleet, ship):
                fleet.append(ship)
                surroundigCoordinates = ship_surrounding_coordinates(ship)
                for coordinate in surroundigCoordinates:
                    if coordinate in available_coordinates:
                        available_coordinates.remove(coordinate)
                break
    
    return fleet


def generate_fleet():
    """() -> list
    Randomly generates a fleet of 10 ships where 1 is 5 coordinates long, 2 are 4 coordinates long, 3 are 3 coordinates long, and 4 are 2 coordinates long. No coordinates from different ships are overlapping or touching and all coordinates are on the 10x10 Battleship map.
    """
    while True:
        available_coordinates = generate_all_coordinates()
        fleet = []
        fleet = ship_append(fleet, 1, 5, available_coordinates)
        fleet = ship_append(fleet, 2, 4, available_coordinates)
        fleet = ship_append(fleet, 3, 3, available_coordinates)
        fleet = ship_append(fleet, 4, 2, available_coordinates)
        if len(fleet) == 10:
            return fleet
        
def ship_surrounding_coordinates(ship):
    """(list) -> list
    Gathers all coordinates surrounding a ship including the coordinates of the ship itself and returns them in a list.
    """
    surrounding_coordinates = []
    for coordinates in ship:
        up = coordinates[0], coordinates[1] - 1         
        down = coordinates[0], coordinates[1] + 1        
        right = coordinates[0] + 1, coordinates[1]
        left = coordinates[0] - 1, coordinates[1]

        top_right = coordinates[0] + 1, coordinates[1] - 1
        top_left = coordinates[0] - 1, coordinates[1] - 1
        bottom_right = coordinates[0] + 1, coordinates[1] + 1
        bottom_left = coordinates[0] - 1, coordinates[1] + 1
            
        append_if_coordinate_not_in_list(up, surrounding_coordinates)
        append_if_coordinate_not_in_list(down, surrounding_coordinates)
        append_if_coordinate_not_in_list(right, surrounding_coordinates)
        append_if_coordinate_not_in_list(left, surrounding_coordinates)
        append_if_coordinate_not_in_list(top_right, surrounding_coordinates)
        append_if_coordinate_not_in_list(top_left, surrounding_coordinates)
        append_if_coordinate_not_in_list(bottom_right, surrounding_coordinates)
        append_if_coordinate_not_in_list(bottom_left, surrounding_coordinates)
        
    return surrounding_coordinates

def append_if_coordinate_not_in_list(coordinate, the_list):
    """(tuple, list) -> None
    If the coordinate is not in the list, the coordinate is appended to the list.
    """
    if coordinate not in the_list:
        the_list.append(coordinate)
        

def clear_surroundings(fleet, ship):
    """(list, list) -> bool
    Checks if a ship's coordinates or any of the coordinates surrounding a ship are already in the fleet.
    """
    ship_surroundings = ship_surrounding_coordinates(ship)
    for coordinate in ship_surroundings:
        if not coordinate_not_in_fleet(coordinate, fleet):
            return False
                          
    return True

def coordinate_not_in_fleet(coordinate, fleet):
    """(tuple, list) -> bool
    Checks if a coordinate is not in the fleet. Returns False if the coordinate is in the fleet.
    """
    for ship in fleet:
        if coordinate in ship:
            return False
        
    return True