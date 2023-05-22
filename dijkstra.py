from collections import OrderedDict
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt


from utils import get_dist, get_grid, viz_grid, cell_type_codes

grid = get_grid()
speed = 1000
H, W = grid.shape

start = (H-1, 0)
goal = (0, W-1)
grid_state = deepcopy(grid)
grid_state[start[0], start[1]] = cell_type_codes["start"]
grid_state[goal[0], goal[1]] = cell_type_codes["goal"]
viz_grid(grid_state)
plt.pause(1/speed)

frontier = OrderedDict([(start, (0, None)),])
dists = np.array([[np.inf] * W for _ in range(H)])
dists[start[0],start[1]] = 0
done_nodes = dict()
found = False

def update_frontier_dist(node, parent, parent_dist, frontier, grid_state):
    cur_dist, _ = frontier.get(node, (np.inf, None))
    if parent_dist + 1 < cur_dist:
        frontier[node] = (parent_dist + 1, parent)
    grid_state[node[0], node[1]] = cell_type_codes["exploring"]

while not found and len(frontier):
    frontier_dists = [v[0] for v in list(frontier.values())]
    min_id = np.argmin(frontier_dists)
    node = list(frontier.keys())[min_id]
    dist, _ = frontier[node]
    
    print(f"Current node: {node}")


    done_nodes[node] = frontier[node]
    del frontier[node]

    if node == goal:
        found = True
        break

    i,j = node
    if i-1>=0 and grid[i-1,j]!=1 and (i-1,j) not in done_nodes:
        update_frontier_dist((i-1,j), (i,j), dist, frontier, grid_state)

    if i+1<H and grid[i+1,j]!=1 and (i+1,j) not in done_nodes:
        update_frontier_dist((i+1,j), (i,j), dist, frontier, grid_state)

    if j-1>=0 and grid[i,j-1]!=1 and (i,j-1) not in done_nodes:
        update_frontier_dist((i,j-1), (i,j), dist, frontier, grid_state)
        
    if j+1<W and grid[i,j+1]!=1 and (i,j+1) not in done_nodes:
        update_frontier_dist((i,j+1), (i,j), dist, frontier, grid_state)
        
    
    # viz
    grid_state[node[0], node[1]] = cell_type_codes["done_exploring"]
    grid_state[start[0], start[1]] = cell_type_codes["start"]
    grid_state[goal[0], goal[1]] = cell_type_codes["goal"]
    viz_grid(grid_state)
    plt.pause(1/speed)

if found:
    path = [goal]
    node = goal
    while node!=start:
        _, node = done_nodes[node]
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



