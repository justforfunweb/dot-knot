import numpy as np
import random
from pandas import *

class gridTester:
    def __init__(self , rows , columns , dots , grid):
        self.rows = rows
        self.columns = columns
        self.dots = dots
        self.grid = grid
        
    def grid_print(self , grid):
        grid = np.array(grid)
        print(DataFrame(grid))
        
    def place_dots(self , dots_positions):
        for items in dots_positions:
            for item in items:
                self.grid[item[0]][item[1]] = 'x'
        
    def generate_dots_positions(self):
        dots_positions = []
        for _ in range(self.dots):
            dot_placements = []
            
            dot_placements.append(random.randint(3,10))
            dot_placements.append(random.randint(3,10))
            
            dots_positions.append(dot_placements)
            
        print(dots_positions)
        
        return dots_positions
            


def makeGrid(rows , columns):
    
    grid = [[0]*rows]*columns
    
    return np.array(grid)

if __name__ == "__main__":
    rows = random.randint(3,10)
    columns = random.randint(3,10)
    
    number_of_dots = int(input("Enter the number of dots: "))
    
    grid = makeGrid(rows , columns)
    
    board = gridTester(rows , columns , number_of_dots , grid)
    
    dots_positions = board.generate_dots_positions()
    
    print(dots_positions)
    
    # board.place_dots(dots_positions)
    
    # board.grid_print(grid)