import generating_boats as boats
import battleship_functions as game

# boats.generate_all_coordinates()
assert(boats.generate_all_coordinates()) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)] # Prints all 100 coordinates on the Battleship map

# boats.find_two_consecutive_coordinates(coordinate_list)
assert(boats.find_two_consecutive_coordinates([(1, 2), (2, 3), (2, 5), (4, 7), (4, 8), (4, 9), (5, 9)])) == [(4, 7), (4, 8)] # Found first two consecutive coordinates
assert(boats.find_two_consecutive_coordinates([(2, 2), (2, 4), (2, 6), (4, 7), (4, 9), (5, 9)])) == [(4, 9), (5, 9)] # Found first two consecutive coordinates


# boats.generate_ship(size, available_coordinates)
# Randomizing function therefore exact output cannot be predicted.

# boats.is_positive(ship)
assert(boats.is_positive([(5, 2), (5, 3), (5, 4), (5, 5)])) == True # All coordinates are positive
assert(boats.is_positive([(7, 2), (-7, 3), (7, 4)])) == False # Not all coordinates are positive

# boats.less_than_10(ship)
assert(boats.less_than_10([(2, 3), (2, 4), (2, 5), (2, 6)])) == True # All coordinates are less than 10
assert(boats.less_than_10([(5, 9), (15, 8), (5, 7)])) == False # Not all coordinates are less than 10

# boats.ship_append(fleet, num, length, available_coordinates)
# Randomizing function therefore exact output cannot be predicted.

# boats.generate_fleet()
# Randomizing function therefore exact output cannot be predicted.

# boats.ship_surrounding_coordinates(ship)
assert(boats.ship_surrounding_coordinates([(8, 10), (9, 10), (10, 10)])) == [(8, 9), (8, 11), (9, 10), (7, 10), (9, 9), (7, 9), (9, 11), (7, 11), (10, 10), (8, 10), (10, 9), (10, 11), (11, 10), (11, 9), (11, 11)] # Found all coordinates surrounding ship coordinates including the coordinates of the ship itself

# boats.append_if_coordinate_not_in_list(coordinate, the_list)
assert(boats.append_if_coordinate_not_in_list((9, 4), [(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)])) == None # Does not append anything and returns None
assert(boats.append_if_coordinate_not_in_list((9, 1), [(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)])) == None # Appends the coordinate and returns None
# There is no return statement therefore the function will always return None

# boats.clear_surroundings(fleet, ship)
assert(boats.clear_surroundings([[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)]], [(3, 8), (3, 9)])) == True # Found that the ship's coordinates or any of the coordinates surrounding a ship are not already in the fleet
assert(boats.clear_surroundings([[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)]], [(2, 10), (3, 10)])) == False # Found that the ship's coordinates or any of the coordinates surrounding a ship are already in the fleet.

# boats.coordinate_not_in_fleet(coordinate, fleet)
assert(boats.coordinate_not_in_fleet((9, 1), [[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)], [(3, 8), (3, 9)]])) == False # Found that the coordinate is in the fleet
assert(boats.coordinate_not_in_fleet((1, 1), [[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)], [(3, 8), (3, 9)]])) == True # Found that the coordinate is not in the fleet



# game.guess_coordinate_formatting_validation(prompt)
# Requires user input therefore exact output cannot be predicted.

# game.valid_coordinate(coor)
assert(game.valid_coordinate(("A9"))) == True # Valid coordinate
assert(game.valid_coordinate(("J17"))) == None # Invalid coordinate
assert(game.valid_coordinate(("s10"))) == None # Invalid coordinate
assert(game.valid_coordinate(("d5"))) == True # Valid coordinate
assert(game.valid_coordinate(("L15"))) == None # Invalid coordinate

# game.letter_coordinate_to_num(coor)
assert(game.letter_coordinate_to_num("A9")) == (1, 9) 
assert(game.letter_coordinate_to_num("d5")) == (4, 5)
assert(game.letter_coordinate_to_num("j3")) == (10, 3)
assert(game.letter_coordinate_to_num("I2")) == (9, 2)
assert(game.letter_coordinate_to_num("c5")) == (3, 5)
# Switched all coordinates from letter to number version

# game.num_coordinate_to_letter(coor)
assert(game.num_coordinate_to_letter((1, 9))) == "A9"
assert(game.num_coordinate_to_letter((4, 5))) == "D5"
assert(game.num_coordinate_to_letter((10, 3))) == "J3"
assert(game.num_coordinate_to_letter((9, 2))) == "I2"
assert(game.num_coordinate_to_letter((3, 5))) == "C5"
# Switched all coordinates from number to letter version


# game.check_coordinate_in_fleet_or_ship_and_remove(fleet, coordinates)
assert(game.check_coordinate_in_fleet_or_ship_and_remove([[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)], [(3, 8), (3, 9)]], (1, 10))) == [[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(2, 1)], [(3, 8), (3, 9)]] # Found that the coordinate is in the fleet and removed it
assert(game.check_coordinate_in_fleet_or_ship_and_remove([[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)], [(3, 8), (3, 9)]], (9, 9))) == [[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(1, 10), (2, 1)], [(3, 8), (3, 9)]] # Found that the coordinate is in the fleet and removed it

# game.ship_index_in_fleet_using_coor(coordinate, fleet)
assert(game.ship_index_in_fleet_using_coor((10, 10), [[(9, 8), (9, 7), (9, 6), (9, 5), (9, 4)], [(5, 2), (5, 3), (5, 4), (5, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)], [(5, 9), (5, 8), (5, 7)], [(8, 10), (9, 10), (10, 10)], [(7, 2), (7, 3), (7, 4)], [(7, 6), (7, 7)], [(9, 1), (9, 2)], [(2, 2), (2, 1)], [(3, 8), (3, 9)]])) == 4 # Found the index of the ship based on the coordinate
assert(game.ship_index_in_fleet_using_coor((10, 10), [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]])) == None # The coordinate is not in the fleet therefore no index to return

# game.is_ship_sunk(ship_index, fleet, player_or_comp)
assert(game.is_ship_sunk(4, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], "player")) == None # Player ship was not sunk
assert(game.is_ship_sunk(4, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(8, 5), (8, 4), (8, 3)], [], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], "player")) == True # Player ship was sunk
assert(game.is_ship_sunk(2, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(6, 6), (6, 5), (6, 4), (6, 3)], [], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], "computer")) == True # Computer ship was sunk
assert(game.is_ship_sunk(5, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], "computer")) == None # Computer ship was not sunk

# game.remove_ship(ship_index, fleet)
assert(game.remove_ship(4, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]])) == [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), 
(1, 2)], [(4, 5), (4, 6)]] # Removed the ship at index 4
assert(game.remove_ship(7, [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]])) == [[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]] # Removed the ship at index 7

# game.introduction_pvc()
# Requires user input therefore exact output cannot be predicted.

# game.get_player_fleet()
# Requires user input therefore exact output cannot be predicted.

#game.get_ship(name, size, num)
# Requires user input therefore exact output cannot be predicted.

# game.consecutive_coordinates(ship)
assert(game.consecutive_coordinates([(10, 3), (10, 4), (10, 5), (10, 6)])) == True # Found that all coordinates are consecutive

# game.player_ship_append(player_fleet, num, name, size)
# Requires user input therefore exact output cannot be predicted.

# game.random_new_missile_coordinate(computer_hit_coordinates)
# Randomizing function therefore exact output cannot be predicted.

# game.get_missile_coordinate_from_player(player_hit_coordinates)
# Requires user input therefore exact output cannot be predicted.

# game.player_or_comp_ship_hit(fleet, missile, player_or_comp)
assert(game.player_or_comp_ship_hit([[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], (8, 10), "player")) == True # Found that a player ship was hit
assert(game.player_or_comp_ship_hit([[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], (10, 10), "player")) == None # Player ship was not hit
assert(game.player_or_comp_ship_hit([[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], (6, 3), "computer")) == True # Found that computer ship was hit
assert(game.player_or_comp_ship_hit([[(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], [(10, 3), (10, 4), (10, 5), (10, 6)], [(6, 6), (6, 5), (6, 4), (6, 3)], [(4, 8), (4, 9), (4, 10)], [(8, 5), (8, 4), (8, 3)], [(8, 10), (7, 10), (6, 10)], [(4, 3), (4, 2)], [(7, 8), (6, 8)], [(1, 1), (1, 2)], [(4, 5), (4, 6)]], (10, 10), "computer")) == None # Computer ship was not hit

# game.is_missile_in_ship(missile, ship, player_or_comp)
assert(game.is_missile_in_ship((8, 10), [(8, 10), (7, 10), (6, 10)], "player")) == True # Missile at given coordinate is in the ship
assert(game.is_missile_in_ship((10, 10), [(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)], "player")) == None # Missile at given coordinate is not in the ship
assert(game.is_missile_in_ship((6, 3), [(6, 6), (6, 5), (6, 4), (6, 3)], "computer")) == True # Missile at given coordinate is in the ship
assert(game.is_missile_in_ship((10, 10), [(10, 3), (10, 4), (10, 5), (10, 6)], "computer")) == None # Missile at given coordinate is not in the ship