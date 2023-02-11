import numpy as np
from pandas import *

class gridFunc:
    def __init__(self , rows : int , columns : int , dots : int , grid : list) -> None:
        self.rows = rows
        self.columns = columns
        self.dots = dots
        self.grid = grid
        
    def print_grid_spacing(self , grid : list) -> None:
        grid = np.array(grid)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))
        
    def print_grid_dataframe(self , grid : list) -> None :
        print(DataFrame(grid))
        
    