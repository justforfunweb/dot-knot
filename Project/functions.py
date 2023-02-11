import numpy as np
from pandas import *
import random

class gridFunc:
    def __init__(self , rows : int , columns : int , dots : int , grid : list) -> None:
        self.rows = rows
        self.columns = columns
        self.dots = dots
        self.grid = grid
        
    def print_grid_spacing(self) -> None:
        grid = np.array(self.grid)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))
        
    def print_grid_dataframe(self) -> None :
        print(DataFrame(self.grid))
        
    def generate_random_blank_grid(self , place_holder : int) -> list:
        rows = random.randint(3,10)
        columns = random.randint(3,10)
        
        grid = [[place_holder]*rows]*columns
        
        return np.array(grid)
    
    def generate_blank_gird(self , rows : int , columns : int , place_holder : int) -> list:
        grid = [[place_holder]*rows]*columns
        
        return np.array(grid)
    
    def place_dot(self , grid : list , dot_x : int , dot_y : int , place_holder : int) -> list:
        if(grid[dot_x][dot_y] == place_holder):
            grid[dot_y][dot_x] = place_holder
        else:
            grid[dot_x][dot_y] = place_holder

        return np.array(grid)
    
    def find_path(self , grid : list , start_dot_x : int , start_dot_y : int , end_dot_x : int , end_dot_y : int , place_holder : int) -> list:
        