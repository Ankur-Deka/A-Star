from collections import OrderedDict
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt


def get_grid():
    return np.array([[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,1,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,1,0,0],
                     [0,0,1,0,0,1,1,1,1,1,1,1,1,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])


# 0: traversible, white
# 1: blocked, black
# 2: exploring, cyan translucent
# 3: done exploring, cyan
# 4: start, red
# 5: goal, green
# 6: path, blue
grid_colors = [colors.to_rgba("white"),
               colors.to_rgba("black"),
               colors.to_rgba("cyan") - np.array([0,0,0,0.8]),
               colors.to_rgba("cyan"),
               colors.to_rgba("red"),
               colors.to_rgba("green"),
               colors.to_rgba("blue")]
cell_type_codes = dict([("traversible", 0),
                  ("blocked", 1),
                  ("exploring", 2),
                  ("done_exploring", 3),
                  ("start", 4),
                  ("goal", 5),
                  ("path", 6),])
grid_cmap = colors.ListedColormap(grid_colors)

def viz_grid(grid_state):
    plt.clf()
    plt.imshow(grid_state, cmap=grid_cmap, vmin = 0, vmax = len(grid_colors))


if __name__ == "__main__":
    grid = get_grid()
    viz_grid(grid)
    plt.show()


def get_dist(a1, a2):
    return np.linalg.norm(np.array(a1)-np.array(a2))
