from game_of_life import GameOfLife

print('playing the game of life!')
#Set the size of the grid (square)
#gol = GameOfLife(15,'pulsar')
gol = GameOfLife(15,'')

#Initialize the grid of the game of life
gol.init_grid()
#run the game of life
gol.run()
