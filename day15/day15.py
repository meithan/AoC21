# Day 15: Chiton

from queue import PriorityQueue
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
grid = []
with open(sys.argv[1]) as f:
  for line in f:
    grid.append([int(x) for x in line.strip()])

# ------------------------------------------------------------------------------

# A* search
def A_Star(start, end, grid, NX, NY):

  def neighbors(node):
    x, y = node
    neighs = []
    if x < NX-1:
      neighs.append((x+1, y))
    if x > 0:
      neighs.append((x-1, y))
    if y < NY-1:
      neighs.append((x, y+1))
    if y > 0:
      neighs.append((x, y-1))
    return neighs

  def h(node):
    x,y = node
    return abs(x-end[0]) + abs(y-end[1])

  def build_path(node):
    path = [node]
    cost = 0
    while node in predecessor:
      cost += grid[node[0]][node[1]]
      node = predecessor[node]
      path.append(node)
    path.reverse()
    return path, cost

  queue = PriorityQueue()
  queue.put((0, start))
  predecessor = {}
  predecessor[start] = None
  past_cost = {}
  past_cost[start] = 0

  while not queue.empty():
    _, current = queue.get()
    if current == end:
      return build_path(current)
    for neigh in neighbors(current):
      next_cost = past_cost[current] + grid[neigh[0]][neigh[1]]
      if neigh not in past_cost or next_cost < past_cost[neigh]:
        past_cost[neigh] = next_cost
        predecessor[neigh] = current
        priority = next_cost + h(neigh)
        queue.put((priority, neigh))
        
# ------------------------------------------------------------------------------
# Part 1

NX = len(grid[0])
NY = len(grid)
start = (0,0)
end = (NX-1,NY-1)

path, cost = A_Star(start, end, grid, NX, NY)

print("Part 1:", cost)

# ------------------------------------------------------------------------------
# Part 2

# Build expanded grid for Part 2
NX2 = 5*NX
NY2 = 5*NY
grid2 = []
for i in range(NY2):
  grid2.append([-1]*NX2)
for i in range(NX2):
  for j in range(NY2):
    ii = i % NX
    jj = j % NY
    value = grid[ii][jj]
    value += i // NX + j // NY
    while value > 9:
      value -= 9
    grid2[i][j] = value

start = (0,0)
end2 = (NX2-1,NY2-1)
path2, cost2 = A_Star(start, end2, grid2, NX2, NY2)

print("Part 2:", cost2)
