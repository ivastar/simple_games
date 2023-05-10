# Python code to implement Conway's Game Of Life
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting up the values for the grid
ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):

    """returns a grid of NxN random values"""

def addGlider(i, j, grid):

    """
    A glider is a pattern that moves across the grid as it evolves.
    
    Add a glider with top left cell at (i, j)"""
    
    glider = np.array([[0, 0, 255],
                    [255, 0, 255],
                    [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N):

    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            # THIS IS WHERE THE MAGIC HAPPENS

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# main() function
def main():

    # parse arguments
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)

    args = parser.parse_args()
    
    # set grid size, use parameter N above
        
    # initialize grid, use randomGrid above

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                frames = 10,
                                interval=updateInterval,
                                save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()
