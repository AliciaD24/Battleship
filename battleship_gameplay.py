# =======================================================================================================================================

# Author: Alicia Durcheva
# Title: Batttleships
# Description: Battleships is a strategy type guessing game for two players. It is played using grids on which each player's fleet of ships are marked. The locations of the fleets are concealed from the other player. Players alternate turns "firing missiles" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

# =======================================================================================================================================


import battleship_functions
import generating_boats
import summative_board

if __name__ == "__main__":
    name = battleship_functions.introduction_pvc()
    computer_fleet = generating_boats.generate_fleet()
    player_fleet = battleship_functions.get_player_fleet()

    player_hit_coordinates = []
    computer_hit_coordinates = []

    while len(computer_fleet) > 0 and len(player_fleet) > 0:
        while True:
            player_missile = battleship_functions.get_missile_coordinate_from_player(player_hit_coordinates)
            if battleship_functions.player_or_comp_ship_hit(computer_fleet, player_missile, "computer"):
                ship_index = battleship_functions.ship_index_in_fleet_using_coor(player_missile, computer_fleet)
                battleship_functions.check_coordinate_in_fleet_or_ship_and_remove(computer_fleet, player_missile)
                if battleship_functions.is_ship_sunk(ship_index, computer_fleet, "computer"):
                    battleship_functions.remove_ship(ship_index, computer_fleet)
                    print(f"{len(computer_fleet)} enemy ships left!")
                    if len(computer_fleet) == 0:
                        break
            else:
                print("You missed! Your missile did not hit any enemy ships.\n")
                break
        
        while True:    
            computer_missile = battleship_functions.random_new_missile_coordinate(computer_hit_coordinates)
            if battleship_functions.player_or_comp_ship_hit(player_fleet, computer_missile, "player"):
                ship_index = battleship_functions.ship_index_in_fleet_using_coor(computer_missile, player_fleet)
                battleship_functions.check_coordinate_in_fleet_or_ship_and_remove(player_fleet, computer_missile)
                if battleship_functions.is_ship_sunk(ship_index, player_fleet, "player"):
                    for coordinate in generating_boats.ship_surrounding_coordinates(player_fleet[ship_index]):
                        computer_hit_coordinates.append(coordinate)
                    battleship_functions.remove_ship(ship_index, player_fleet)
                    print(f"{len(player_fleet)} of your ships still stand!")
                    if len(player_fleet) == 0:
                        break
            else:
                print(f"A missle was fired at {battleship_functions.num_coordinate_to_letter(computer_missile)} and missed your ships!\n")
                break

    if len(computer_fleet) == 0:
        print(f"CONGRATULATIONS {name}! You destroyed all 10 boats in the enemy fleet!")
    elif len(player_fleet) == 0:
        print(f"All 10 of your ships have been sunk {name}! Better luck next time!")