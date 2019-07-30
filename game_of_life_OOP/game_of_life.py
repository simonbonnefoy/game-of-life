#!/usr/bin/env python

import numpy as np
import math
import time

class GameOfLife:
    def __init__(self, size):
        self.size = size

    def display_grid_of_life(self):
        output = self.format_grid_output()
        sep = ''
        for i in range(0, self.size):
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
            
    
    def format_grid_output(self):
        output_of_life = ''
        for x in range(0, self.size):
            for y in range(0, self.size):
                if y != self.size -1:
                    output_of_life += str(self.grid[x][y]) 
                elif y == self.size -1 and x != self.size -1 :
                    output_of_life += str(self.grid[x][y]) + '\n'
                else:
                    output_of_life += str(self.grid[x][y]) + '' 
    
        return str(output_of_life)
    
    def check_neighbours_sum(self, x, y):
        sum = 0
    
        if x > 0:
            sum += self.grid[x-1][y]
        if x < self.size-1:
            sum += self.grid[x+1][y]
        if y > 0:
            sum += self.grid[x][y-1]
        if y < self.size-1:
            sum += self.grid[x][y+1]
        if x > 0 and y > 0 :
            sum += self.grid[x-1][y-1]
        if x < self.size-1 and y > 0:
            sum += self.grid[x+1][y-1]
        if x > 0 and y < self.size-1:
            sum += self.grid[x-1][y+1]
        if x < self.size-1 and y < self.size-1:
            sum += self.grid[x+1][y+1]
    
        return sum
    
    def check_cell_lives(self, live,sum_neighbours):
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
    
        
    def cells_evolution(self):
        '''compute the evolution of a cell
        depending on its state and the number of neighbours alive'''
    
        new_game = np.full((self.size,self.size),0)
        for x in range(0, len(self.grid[0])):
            for y in range(0, len(self.grid[0])):
                sum_neighbours = self.check_neighbours_sum(x, y)
                new_game[x][y] = self.check_cell_lives(self.grid[x][y],sum_neighbours)
                
        return new_game
                
    
    
    
    
    def init_grid(self):
        '''Initializing the grid of the game of life'''
    
        #initialize the grid to a numpy array 
        self.grid = np.full((self.size,self.size),1)
        for i in range(0, len(self.grid)):
            for k in range(0, len(self.grid)):
                if (i+k)%2==0:
                    self.grid[i][k]=0
    

    def run(self):

        while True:
            try:
                self.display_grid_of_life()
                self.grid = self.cells_evolution()
                time.sleep(1)
            except KeyboardInterrupt:
                print('Exiting the game of life!')
                exit(0)
