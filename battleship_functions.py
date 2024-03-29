import generating_boats
import random


letters = "abcdefghij"

def guess_coordinate_formatting_validation(prompt):
    """(str) -> tuple
    Asks for a coordinate input and validates it before returning the number version of the letter coordinate.
    """
    while True:
        coor = input(prompt)
        if valid_coordinate(coor):
            return letter_coordinate_to_num(coor)
        else:
            print("Please enter coordinates of a letter between A and J followed by a number between 1 and 10. For example: B6")
                
def valid_coordinate(coor):
    """(str) -> bool
    Checks if the coordinate is blank. If not, identify the number value of the letter and check if it is less than or equal to 10 to return True. Otherwise returns false.
    """
    if coor == "":
        return False
    elif coor[0].lower() in letters:
            if len(coor) <= 3:
                try:
                    yvalue = int(coor[1:3])
                except:
                    return False
                if yvalue <= 10:
                    return True

def letter_coordinate_to_num(coor):
    """(str) -> tuple
    Converts letter coordinates to number coordinates.
    """
    xvalue = letters.index(coor[0].lower()) + 1
    yvalue = int(coor[1:3])
    return xvalue, yvalue

def num_coordinate_to_letter(coor):
    """(tuple) -> str
    Converts number coordinates to letter coordinates.
    """
    letter = letters[int(coor[0]) - 1].upper()
    number = str(coor[1])
    return letter + number

def check_coordinate_in_fleet_or_ship_and_remove(fleet, coordinates):
    """(list, tuple) -> list
    Checks if the coordinate is in the fleet or in a ship and removes the coordinate from the fleet or ship.
    """
    for ship in fleet:
        if coordinates in ship:
            ship.remove(coordinates)
    if coordinates in fleet:
        fleet.remove(coordinates)
    return fleet            

def ship_index_in_fleet_using_coor(coordinate, fleet):
    """(tuple, list) -> int
    Finds the index of the ship in the fleet based on the given coordinate.
    """
    index = 0
    for ship in fleet:
        if coordinate in ship:
            return index
        index +=1

def is_ship_sunk(ship_index, fleet, player_or_comp):
    """(int, list, str) -> bool
    Checks if the ship attached to the index is empty (sunk) for either player or computer fleet.
    """
    if fleet[ship_index] == []:
        if player_or_comp == "player":
            print("The enemy sunk your ship!")
            return True
        elif player_or_comp == "computer":
            print("You sunk an enemy ship!")
            return True

def remove_ship(ship_index, fleet):
    """(int, list) -> list
    Removes a ship from a fleet.
    """
    fleet.remove(fleet[ship_index])
    return fleet


def introduction_pvc():
    """() -> str
    Prints a welcome and introduction message along with game guidelines and asks for player name. Returns player name.
    """
    print("WELCOME TO BATTLESHIP\n")
    name = input("Enter player name: ")
    print(f"\nWelcome to Battleships {name}!\n"
        "Your fleet is in close proximity to an enemy fleet!\n" 
        "It's up to you position your boats strategically and sink all 10 enemy boats before they get you!\n\n"      
        "The CARRIER is the biggest ship, it will take 5 hits to destroy.\n"
        "You'll need to hit the BATTLESHIP 4 times to get through the thick armour.\n"
        "Then there is a SUBMARINE that will need to be hit 3 times.\n"
        "There's a small DESTROYER that will take 2 hits, but be careful, it packs a punch!\n\n"
        "You've been given a map of the seas. Arrange your boats and start firing your missiles.\n"
        "Pick your shots carefully only one fleet will make it out alive!\n"
        f"It's all up to you now {name}, GOOD LUCK!\n"
        "---------------------------\n")
    return name

def get_player_fleet():
    """() - > list
    Asks user for a fleet of 10 ships where 1 is 5 coordinates long, 2 are 4 coordinates long, 3 are 3 coordinates long, and 4 are 2 coordinates long. No coordinates from different ships are overlapping or touching and all coordinates are on the 10x10 Battleship map. All 10 ship coordinates are returned as a list of lists.
    """
    print("Arrange your ships with at least one blank space separating them on the map.\n"
        "Enter all coordinates per ship separated by a space. For example, BATTLESHIP coordinates: B2 B3 B4 B5\n")
    player_fleet = []
    player_fleet = player_ship_append(player_fleet, 1, "CARRIER", 5)
    player_fleet = player_ship_append(player_fleet, 2, "BATTLESHIP", 4)
    player_fleet = player_ship_append(player_fleet, 3, "SUBMARINE", 3)
    player_fleet = player_ship_append(player_fleet, 4, "DESTROYER", 2)
    print("\nYour fleet has been saved and your ships arranged!\n")
    return player_fleet

def get_ship(name, size, num):
    """(str, int, int) -> list
    Gets a set of coordinates from the user and validates each coordinate to ensure they are all consecutive and in the proper format before adding them all to a ship and returning the ship coordinates.
    """
    while True:
        try:
            ship_coors = []
            coor = input(f"Enter {size} consecutive coordinates for your {name} #{num}: ")
            raw_ship_coor_list = coor.split(" ")
            if raw_ship_coor_list[-1] == "":
                raw_ship_coor_list.remove(raw_ship_coor_list[-1])
            if len(raw_ship_coor_list) == size:
                for coor in raw_ship_coor_list:
                    if valid_coordinate(coor):
                        formatted_coor = letter_coordinate_to_num(coor)
                        if formatted_coor in ship_coors:
                            print("Please do not enter duplicate coordinates.")
                            raise Exception
                        else:
                            ship_coors.append(formatted_coor)        
                    else:
                        print("Please enter coordinates of a letter between A and J followed by a number between 1 and 10. For example: B6")
                        raise Exception           
            else:
                print(f"Please enter exactly {size} coordinates.")
                raise Exception
            
            if consecutive_coordinates(ship_coors):
                return ship_coors
            else:
                print("Please enter only consecutive coordinates. Your ships can't have holes in them!")
                raise Exception
            
        except:
            pass

def consecutive_coordinates(ship):
    """(list) -> bool
    Checks if a list of coordinates are all consecutive.
    """    
    base_coor = ship[0]
    xvalues = []
    yvalues = []
    for coor in ship:
        xvalues.append(coor[0])
        yvalues.append(coor[1])
    
    if xvalues.count(base_coor[0]) == len(ship):
        for n in range(len(yvalues) - 1):
            difference = yvalues[n] - yvalues[n+1]
            if abs(difference) == 1:
                pass
            else:
                return False
        return True
             
    elif yvalues.count(base_coor[1]) == len(ship):
        for n in range(len(xvalues) - 1):
            difference = xvalues[n] - xvalues[n+1]
            if abs(difference) == 1:
                pass
            else:
                return False
        return True
        
    else:
        return False

def player_ship_append(player_fleet, num, name, size):
    """(list, int, str, int) -> list
    Gets ship coordinates from the player, checks if they are valid, ensures the surrounding coordinates of the ship coordinates are clear, then appends the ship coordinates to the player's fleet.
    """
    for boat in range(num):  
        while True:
            ship = get_ship(name, size, boat+1)
            if generating_boats.clear_surroundings(player_fleet, ship):
                player_fleet.append(ship)
                break
            else:
                print("Your ships cannot be touching or overlapping.")
    return player_fleet 

def random_new_missile_coordinate(computer_hit_coordinates):
    """(list) -> tuple
    Randomly generates a coordinate then checks if it has already been hit by a missile launched by the computer. If it has not, the coordinate is added to the hit by computer coordinates list and the coordinate is returned as a tuple.
    """
    while True:
        coordinate = []
        for axis in range(2):
            value = random.randint(1, 10)
            coordinate.append(value)
        coordinate = (coordinate[0], coordinate[1])
        if coordinate in computer_hit_coordinates:
            pass
        else:
            computer_hit_coordinates.append(coordinate)
            return coordinate
        
def get_missile_coordinate_from_player(player_hit_coordinates):
    """(list) -> tuple
    Gets a valid coordinate from the player, formats it from a letter coordinate to a number coordinate, checks if the player has already fired a missile to the coordinate and if not, adds the coordinate to the list with all the coordinates the player has fired a missile to. Returns the coordinate in number form.
    """
    while True:
        coordinate = input("Choose a coordinate to fire a missile: ")
        if valid_coordinate(coordinate):
            formatted_coor = letter_coordinate_to_num(coordinate)
            if formatted_coor in player_hit_coordinates:
                print("You've already fired a missile to this coordinate!")
            else:
                player_hit_coordinates.append(formatted_coor)     
                return formatted_coor   
        else:
            print("Please enter coordinates of a letter between A and J followed by a number between 1 and 10. For example: B6")

def player_or_comp_ship_hit(fleet, missile, player_or_comp):
    """(list, tuple, str) -> bool
    Checks if either a computer or player ship was hit.
    """
    for ship in fleet:
        if is_missile_in_ship(missile, ship, player_or_comp):
            return True
    if is_missile_in_ship(missile, fleet, player_or_comp):
        return True
        
    
def is_missile_in_ship(missile, ship, player_or_comp):
    """(tuple, list, str) -> bool
    Checks if the missile is in the fleet or in a ship. Returns True if it is.
    """
    if missile in ship:
        if player_or_comp == "player":
            print(f"One of your ships has been hit at coordinate {num_coordinate_to_letter(missile)}!")
            return True
        elif player_or_comp == "computer":
            print(f"You hit an enemy ship at coordinate {num_coordinate_to_letter(missile)}!")
            return True