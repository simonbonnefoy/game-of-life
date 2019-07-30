#!/usr/bin/env python

import numpy as np
import math
import time
''' Script to launch the famous game of life'''

def display_grid_of_life(grid):
    output = format_grid_output(grid)
    sep = ''
    size = len(grid[1])
    for i in range(0, len(grid[0])):
        sep += '-'
    print(sep)
    print('\r%s\n' %output, end= '',  flush=True)
    #print('Display grid of life')
    #for x in range(0, len(grid)):
    #    for y in range(0, len(grid)):
    #        if y != len(grid) -1:
    #            print(' '+ str(grid[x][y]) + ' ',end='', flush=True)
    #        else:
    #            print(' '+ str(grid[x][y]) + ' ')
        

def format_grid_output(grid):
    #print('Display grid of life')
    output_of_life = ''
    for x in range(0, len(grid)):
        for y in range(0, len(grid)):
            if y != len(grid) -1:
                output_of_life += str(grid[x][y]) 
            elif y == len(grid) -1 and x != len(grid) -1 :
                output_of_life += str(grid[x][y]) + '\n'
            else:
                output_of_life += str(grid[x][y]) + '' 

    return str(output_of_life)

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
    for x in range(0, len(grid)):
        for y in range(0, len(grid)):
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


if __name__=='__main__':
    print('playing the game of life!')
    #Set the size of the grid (square)
    size = 15 

    #Initialize the grid of the game of life
    grid  = init_grid(size)

    while True:
        try:
            display_grid_of_life(grid)
            grid = cells_evolution(grid)
            time.sleep(1)
        except KeyboardInterrupt:
            print('Exiting the game of life!')
            exit(0)
