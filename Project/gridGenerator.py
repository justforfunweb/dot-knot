import numpy as np
import random
from pandas import *

class gridTester:
    def __init__(self , rows , columns , dots , grid):
        self.rows = rows
        self.columns = columns
        self.dots = dots * 2
        self.grid = grid
        
    def grid_print(self , grid):
        grid = np.array(grid)
        print(DataFrame(grid))
        
    def place_dots(self , dots_positions):
        for items in dots_positions:
            self.grid[items[0]][items[1]] = 'x'
                
    def generate_dots_location(self):
        dot_x = random.randint(3,10)
        dot_y = random.randint(3,10)
        
        return [dot_x , dot_y]
        
    def generate_dots_positions(self):
        dots_positions = []
        for _ in range(self.dots):
            dot_placements = []
            
            
            
        print(dots_positions)
        
        return dots_positions
            
def check_valid_number_dots(dots , rows , columns):
    if(dots > max(rows , columns)+1):
        dots = dots % ((max(rows , columns)//2)+1)
    else:
        pass
    
    return dots

def makeGrid(rows , columns):
    
    grid = [[0]*rows]*columns
    
    return np.array(grid)

if __name__ == "__main__":
    rows = random.randint(3,10)
    columns = random.randint(3,10)
    
    number_of_dots = check_valid_number_dots(int(input("Enter the number of dots: ")) , rows , columns)
    
    grid = makeGrid(rows , columns)
    
    board = gridTester(rows , columns , number_of_dots , grid)
    
    dots_positions = board.generate_dots_positions()
    
    print(dots_positions)
    
    # board.place_dots(dots_positions)
    
    # board.grid_print(grid)