import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 10
life = 255
dead = 0
val =[life, dead]

grid = np.random.choice(val, n*n, p=[0.2, 0.8]).reshape(n, n)

def draw(data):
  global grid
  newGrid = grid.copy()
  for i in range(n):
    for j in range(n):
      total = (grid[i, (j-1)%n] + grid[i, (j+1)%n] +
               grid[(i-1)%n, j] + grid[(i+1)%n, j] +
               grid[(i-1)%n, (j-1)%n] + grid[(i-1)%n, (j+1)%n] +
               grid[(i+1)%n, (j-1)%n] + grid[(i+1)%n, (j+1)%n])/255
      if grid[i, j]  == life:
        if (total < 2) or (total > 3):
          newGrid[i, j] = dead
      else:
        if total == 3:
          newGrid[i, j] = life
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, draw, interval=50,
                              save_count=50)
plt.show()