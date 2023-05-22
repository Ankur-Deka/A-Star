from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

from utils import get_dist, get_grid, viz_grid, cell_type_codes

grid = get_grid()
speed = 1000
H, W = grid.shape

start = [H-1, 0]
goal = [0, W-1]
grid_state = deepcopy(grid)
grid_state[start[0], start[1]] = cell_type_codes["start"]
grid_state[goal[0], goal[1]] = cell_type_codes["goal"]
viz_grid(grid_state)
plt.pause(1/speed)

frontier = PriorityQueue()
frontier.put((get_dist(start,goal), start))

node_to_parent = {tuple(start): None}
found = False
while not found and frontier.qsize():
    _, node = frontier.get()    
    print(node)
    if node == goal:
        found = True
        break
    i,j = node
    if i-1>=0 and grid[i-1,j]!=1 and (i-1,j) not in node_to_parent:
        frontier.put((get_dist([i-1,j], goal), [i-1,j]))
        grid_state[i-1, j] = cell_type_codes["exploring"]
        node_to_parent[(i-1,j)] = [i,j]
    if i+1<H and grid[i+1,j]!=1 and (i+1,j) not in node_to_parent:
        frontier.put((get_dist([i+1,j], goal), [i+1,j]))
        grid_state[i+1, j] = cell_type_codes["exploring"]
        node_to_parent[(i+1,j)] = [i,j]
    if j-1>=0 and grid[i,j-1]!=1 and (i,j-1) not in node_to_parent:
        frontier.put((get_dist([i,j-1], goal), [i,j-1]))
        grid_state[i, j-1] = cell_type_codes["exploring"]
        node_to_parent[(i,j-1)] = [i,j]
    if j+1<W and grid[i,j+1]!=1 and (i,j+1) not in node_to_parent:
        frontier.put((get_dist([i,j+1], goal), [i,j+1]))
        grid_state[i, j+1] = cell_type_codes["exploring"]
        node_to_parent[(i,j+1)] = [i,j]

    # viz
    grid_state[node[0], node[1]] = cell_type_codes["done_exploring"]
    grid_state[start[0], start[1]] = cell_type_codes["start"]
    grid_state[goal[0], goal[1]] = cell_type_codes["goal"]
    viz_grid(grid_state)
    plt.pause(1/speed)
plt.clf()

if found:
    path = [goal]
    node = goal
    while node!=start:
        node = node_to_parent[tuple(node)]
        path.append(node)

    ans = np.zeros((H,W))
    for node in path:
        ans[node[0], node[1]] = 1
        grid_state[node[0], node[1]] = cell_type_codes["path"]
    grid_state[start[0], start[1]] = cell_type_codes["start"]
    grid_state[goal[0], goal[1]] = cell_type_codes["goal"]
    print(ans)
    plt.close()
    viz_grid(grid_state)
    plt.show()



