import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to check if a block can be placed at a specific position
def can_place_block(grid, block, x, y):
    block_height, block_width = len(block), len(block[0])
    # Check if the block fits within the grid boundaries
    if x + block_height > len(grid) or y + block_width > len(grid[0]):
        return False
    
    # Check if the block overlaps with any existing blocks
    for i in range(block_height):
        for j in range(block_width):
            if block[i][j] == 1 and grid[x + i][y + j] == 1:
                return False
    return True

# Function to place a block on the grid
def place_block(grid, block, x, y):
    block_height, block_width = len(block), len(block[0])
    new_grid = [row[:] for row in grid]  # Make a copy of the grid
    for i in range(block_height):
        for j in range(block_width):
            if block[i][j] == 1:
                new_grid[x + i][y + j] = 1
    return new_grid

# Function to eliminate full rows from the grid
def eliminate_full_rows(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]  # Keep non-full rows
    rows_removed = len(grid) - len(new_grid)  # Number of rows removed
    # Add empty rows at the top to maintain the same grid size
    new_grid = [[0] * len(grid[0])] * rows_removed + new_grid
    return new_grid, rows_removed

# Function to evaluate all possible placements for a set of blocks
def evaluate_block_placements(grid, blocks):
    best_grid = None
    best_score = -1
    for block in blocks:
        block_height, block_width = len(block), len(block[0])
        for x in range(len(grid) - block_height + 1):  # Possible x positions
            for y in range(len(grid[0]) - block_width + 1):  # Possible y positions
                if can_place_block(grid, block, x, y):
                    new_grid = place_block(grid, block, x, y)
                    new_grid, rows_removed = eliminate_full_rows(new_grid)
                    # Maximize row elimination
                    if rows_removed > best_score:
                        best_score = rows_removed
                        best_grid = new_grid
    return best_grid, best_score

# Function to simulate the game with given blocks
def block_blast_game(grid, blocks):
    # Evaluate all possible placements for the given blocks
    best_grid, best_score = evaluate_block_placements(grid, blocks)
    return best_grid, best_score

# Function to plot the grid using matplotlib
def plot_grid(grid):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, len(grid[0]), 1))
    ax.set_yticks(np.arange(0, len(grid), 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect('equal')

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            color = 'black' if grid[i][j] == 1 else 'white'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))
    
    plt.grid(True)
    plt.show()

# Example of how to use the algorithm

# Initialize an empty grid (5x5 grid, all cells are 0)
grid_size = 5
grid = [[0] * grid_size for _ in range(grid_size)]

# Example blocks (shapes that can be placed on the grid)
block1 = [
    [1, 1],
    [1, 1]
]

block2 = [
    [1, 1, 1]
]

block3 = [
    [1, 0],
    [1, 1],
    [1, 0]
]

blocks = [block1, block2, block3]

# Simulate one turn of the game
best_grid, best_score = block_blast_game(grid, blocks)

# Display the results
print("Best Score:", best_score)

# Plot the updated grid
plot_grid(best_grid)

# Optional: Pause the game and let user interact
time.sleep(2)  # Pauses for 2 seconds before showing the next step
