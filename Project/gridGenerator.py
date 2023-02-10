import io, os, sys, types

import numpy as np
import random

def makeGrid():
    rows = random.randint(3,10)
    columns = random.randint(3,10)
    
    grid = [[0]*rows]*columns
    
    return np.array(grid)

if __name__ == "__main__":
    print(makeGrid())
    
