# Day 9: Smoke Basin

from queue import Queue
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
height = []
with open(sys.argv[1]) as f:
  for line in f:
    height.append([int(n) for n in line.strip()])

nx = len(height)
ny = len(height[0])

# ------------------------------------------------------------------------------
# Part 1

shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_lowpoint(i, j):
  for dx,dy in shifts:
    ni = i + dx
    nj = j + dy
    if 0 <= ni < nx and 0 <= nj < ny:
      if height[i][j] >= height[ni][nj]:
        return False
  return True

lows = []
total_risk = 0
for i in range(nx):
  for j in range(ny):
    if is_lowpoint(i, j):
      lows.append((i,j))
      total_risk += 1 + height[i][j]
 
print("Part 1:", total_risk)

# ------------------------------------------------------------------------------
# Part 2

def find_basin(low):
  Q = Queue()
  Q.put(low)
  basin = set()
  while not Q.empty():
    i,j = Q.get()
    basin.add((i,j))
    for dx,dy in shifts:
      ni = i + dx
      nj = j + dy
      if 0 <= ni < nx and 0 <= nj < ny:
        if height[ni][nj] != 9 and height[ni][nj] > height[i][j]:
          if (ni,nj) not in basin:
            Q.put((ni,nj))
  return basin

sizes = []
for low in lows:
  basin = find_basin(low)
  sizes.append(len(basin))

sizes.sort(reverse=True)
ans2 = sizes[0] * sizes[1] * sizes[2]

print("Part 2:", ans2)
