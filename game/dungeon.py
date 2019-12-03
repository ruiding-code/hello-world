import random
from dungeon_helpers import get_directions, get_directions_message, get_next_coordinate

class Player():
    def __init__(self, name): # constructor takes in one argument
        self.name = name # attributes
        self.health = 10 # initial attribute for health
    
    def get_name(self):
        return self.name # self.get_name() returns name attribute
    
    def get_health(self):
        return self.health # self.get_health() returns health attribute
    
    def set_health(self, health):
        # self.set_health(health_value) sets self.health to health_value
        if type(health) != int or health < 0:
            # health must be both positive and of type int
            # raise ValueError if one of those fails
            raise ValueError("Health value must be a positive integer.")
        self.health = health
        # runs this line only if we have a valid input of health

class Dungeon():
    def __init__(self, map_filename, num_traps):
        # constructor takes in 2 arguments
        self.dungeon_map = self.read_map_file(map_filename)
        # defines .dungeon_map attribute as a list of lists
        if len(self.dungeon_map) != len(self.dungeon_map[0]):
            # needs equal number of lists as characters in each list to be n x n grid
            raise ValueError("Dungeon map must be a square grid!")
        if len(self.dungeon_map) < 4:
            # minimum size of the grid is 4 x 4
            raise ValueError("Grid should be at least 4x4.")
        valid_characters = ("x", "T", "*")
        # only these characters should be present in the list of lists
        characters = []
        # starts a comprehensive list of all the characters in all the lists
        count = 0
        # starts the count of empty spaces at 0
        for row in self.dungeon_map:
            for character in row:
                if character not in valid_characters:
                    raise ValueError("Invalid characters in dungeon map!")
                characters.append(character)
                if character == "*":
                    count += 1
        if "T" not in characters:
            raise ValueError("There is no treasure in dungeon map.")
        if count < num_traps or num_traps < 0:
            raise ValueError("Invalid number of traps!")
        self.num_traps = num_traps # only executes this line if no errors were previously raised
        self.add_traps() # calls add_traps method
        # adds traps in random coordinates with "*"
    
    def read_map_file(self, filename):
        file = open(filename, "r") # opens the txt file in read mode
        list_of_lines = file.readlines()
        # list of strings making up the lines of the txt file, with \n at the end of each
        list_of_rows = []
        # starts an empty list of rows to be appended to
        for line in list_of_lines:
            row = list(line.rstrip("\n"))
            # strips the \n to the right and makes a list out of the characters in each line
            list_of_rows.append(row)
            # appends list row to the list_of_rows
        file.close() # closes the file
        return list_of_rows # list_of_rows is a list of lists
    
    def get_coords_of_empty_spaces(self):
        coords_of_empty_spaces = []
        # starts an empty list of the coords of the empty spaces "*"
        for row_index in range(len(self.dungeon_map)):
            # iterates through each list
            for col_index in range(len(self.dungeon_map)):
                # number of rows = number of columns
                # iterates through each character in the current iterated list
                if self.dungeon_map[row_index][col_index] == "*":
                    x = row_index
                    # x = index of the row
                    y = col_index
                    # y = index of the column
                    coord = (x, y) # coord is a tuple storing 2 values
                    coords_of_empty_spaces.append(coord)
                    # appends the coord to the list of coords
        return coords_of_empty_spaces
                   
    def get_char_at(self, coord):
        x, y = coord
        # unpacking tuple, assigning local variables x and y
        return self.dungeon_map[x][y]
        # returns the character at that coordinate
    
    def visit_square(self, coord, player):
        # takes in the coord too visit and the player
        character = self.get_char_at(coord)
        # returns the character at the entered coord
        if character == "^":
            player.set_health(player.get_health()-1)
            # gets the current health value of the player, substracts 1
            # sets the new health value of the player to that value
        if player.get_health() == 0:
            # if value of health goes to 0
            print("No more health. Game over!")
            return True # game over, lose
        elif character == "T":
            print("You have found the treasure. You win!")
            return True # game over, win
        else:
            return False
            # as long as the player has not won or lost, the game continues
    
    def enter(self, player):
        cur_coord = self.get_starting_coordinate()
        num_moves = 0
        
        while True:
            game_over = self.visit_square(cur_coord, player)
            if game_over:
                break # end of game
            
            print(get_directions_message(self.dungeon_map, cur_coord))
            chosen_direction = input("Where would you like to go?\n>")
            valid_directions = get_directions(self.dungeon_map, cur_coord)
            if chosen_direction not in valid_directions:
                print("Invalid direction.")
                continue
            
            cur_coord = get_next_coordinate(cur_coord, chosen_direction)
            num_moves += 1
    
    def get_starting_coordinate(self):
        empty_spaces = self.get_coords_of_empty_spaces()
        return random.choice(empty_spaces)
    
    def add_traps(self):
        coords_of_empty_spaces = self.get_coords_of_empty_spaces()
        while self.num_traps > 0:
            coord = random.choice(coords_of_empty_spaces)
            self.dungeon_map[coord[0]][coord[1]] = '^'
            coords_of_empty_spaces.remove(coord)
            self.num_traps -= 1

name = input("Please enter player name:\n> ")
player = Player(name)
dungeon = Dungeon("d1.txt", 4)
dungeon.enter(player)
