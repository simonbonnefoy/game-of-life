import numpy as np
import math
import time
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

class GameOfLife:
    def __init__(self, size, model):
        self.size = size
        self.model = model
    
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
    
        #if the pulsar mode is set
        if self.model == 'pulsar':
            self.grid = np.zeros((17, 17))
            self.grid[2, 4:7] = 1
            self.grid[4:7, 7] = 1
            self.grid += self.grid.T
            self.grid += self.grid[:, ::-1]
            self.grid += self.grid[::-1, :]
            self.size = 17

        #default initialization
        else:
            self.grid = np.full((self.size,self.size),1)
            for i in range(0, len(self.grid)):
                for k in range(0, len(self.grid)):
                    if (i+k)%3==0:
                        self.grid[i][k]=0
    

    def update(self, i):

        new_grid = self.cells_evolution()
        self.im.set_array(new_grid)
        self.grid = new_grid
        return self.im

    def run(self):

        fig = plt.figure()
        self.im = plt.imshow(self.grid)
        try:
            ani = animation.FuncAnimation(fig, self.update, interval=200)
            plt.show()
        except KeyboardInterrupt:
            print('Exiting the game of life!')
            exit(0)
