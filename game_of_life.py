#!/usr/bin/env python

import numpy as np
import math
import time
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 
''' Script to launch the famous game of life'''


def check_neighbours_sum(grid, x, y):
    size = len(grid[1])
    sum = 0

    if x > 0:
        sum += grid[x-1][y]
    if x < len(grid)-1:
        sum += grid[x+1][y]
    if y > 0:
        sum += grid[x][y-1]
    if y < len(grid)-1:
        sum += grid[x][y+1]
    if x > 0 and y > 0 :
        sum += grid[x-1][y-1]
    if x < len(grid)-1 and y > 0:
        sum += grid[x+1][y-1]
    if x > 0 and y < len(grid)-1:
        sum += grid[x-1][y+1]
    if x < len(grid)-1 and y < len(grid)-1:
        sum += grid[x+1][y+1]

    return sum

def check_cell_lives(live,sum_neighbours):
    '''Check if the cell lives depending on the number of live neighbours'''

    if live:
        if 1 < sum_neighbours <4:
           # print('The cell lives!')
            return 1
        else:
           # print('The cell will not live!')
            return 0

    else:
        if sum_neighbours == 3:
            #print('The cell lives!')
            return 1
        else:
            #print('The cell will not live!')
            return 0

    
def cells_evolution(grid):
    '''compute the evolution of a cell
    depending on its state and the number of neighbours alive'''

    new_game = np.full((size,size),0)
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid[0])):
            sum_neighbours = check_neighbours_sum(grid, x, y)
            new_game[x][y] = check_cell_lives(grid[x][y],sum_neighbours)
            
    return new_game
            
def init_grid(size):
    '''Initializing the grid of the game of life'''

    #initialize the grid to a numpy array 
    grid = np.full((size,size),1)
    for i in range(0, len(grid)):
        for k in range(0, len(grid)):
            if (i+k)%2==0:
                grid[i][k]=0

    return grid


def update(i):
    global grid
    new_grid = cells_evolution(grid)
    im.set_array(new_grid)
    grid = new_grid
    return im


if __name__=='__main__':
    print('playing the game of life!')
    #Set the size of the grid (square)
    size = 17 

    #Initialize the grid of the game of life
    global grid  
    grid = init_grid(size)

    fig = plt.figure()
    im = plt.imshow(grid)
    try:
        ani = animation.FuncAnimation(fig, update, interval=200)
        plt.show()
    except KeyboardInterrupt:
        print('Exiting the game of life!')
        exit(0)
