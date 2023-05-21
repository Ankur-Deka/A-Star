import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

grid = np.array([[0,0,0,1,0],
                 [0,1,0,1,0],
                 [0,1,0,1,0],
                 [0,1,0,0,0]])

H, W = grid.shape
def get_dist(a1, a2):
    return np.linalg.norm(np.array(a1)-np.array(a2))

start = [3, 0]
goal = [0, 4]
frontier = PriorityQueue()
frontier.put((-get_dist(start,goal), start))

node_to_parent = {tuple(start): None}
found = False
while not found and frontier.qsize():
    _, node = frontier.get()    
    print(node)
    if node == goal:
        found = True
        break
    i,j = node
    if i-1>=0 and grid[i,j]!=1 and (i-1,j) not in node_to_parent:
        frontier.put((-get_dist([i-1,j], goal), [i-1,j]))
        node_to_parent[(i-1,j)] = [i,j]
    if i+1<H and grid[i,j]!=1 and (i+1,j) not in node_to_parent:
        frontier.put((-get_dist([i+1,j], goal), [i+1,j]))
        node_to_parent[(i+1,j)] = [i,j]
    if j-1>=0 and grid[i,j]!=1 and (i,j-1) not in node_to_parent:
        frontier.put((-get_dist([i,j-1], goal), [i,j-1]))
        node_to_parent[(i,j-1)] = [i,j]
    if j+1<W and grid[i,j]!=1 and (i,j+1) not in node_to_parent:
        frontier.put((-get_dist([i,j+1], goal), [i,j+1]))
        node_to_parent[(i,j+1)] = [i,j]

path = [goal]
node = goal
while node!=start:
    node = node_to_parent[tuple(node)]
    path.append(node)

ans = np.zeros((H,W))
for node in path:
    ans[node[0], node[1]] = 1
print(ans)



