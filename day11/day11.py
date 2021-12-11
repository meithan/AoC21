# Day 11: Dumbo Octopus

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
energy = []
with open(sys.argv[1]) as f:
  for line in f:
    energy.append([int(x) for x in line.strip()])

# ------------------------------------------------------------------------------
# Part 1

neighs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

nx = len(energy)
ny = len(energy[0])

def show():
  for row in energy:
    print("".join([str(x) for x in row]))
  print()

def evolve():
  
  to_flash = set()
  for i in range(nx):
    for j in range(ny):
      energy[i][j] += 1
      if energy[i][j] > 9:
        to_flash.add((i,j))

  has_flashed = set()  
  while len(to_flash) > 0:
    i, j = to_flash.pop()
    has_flashed.add((i,j))
    for di,dj in neighs:
      ni = i + di
      nj = j + dj
      if 0 <= ni < nx and 0 <= nj < ny and (ni,nj) not in has_flashed:
        energy[ni][nj] += 1
        if energy[ni][nj] > 9:
          to_flash.add((ni,nj))
    energy[i][j] = 0

  return len(has_flashed)

flashes = 0
for step in range(1,100+1):
  flashes += evolve()
# show()

print("Part 1:", flashes)

# ------------------------------------------------------------------------------
# Part 2

while True:
  count = evolve()
  step += 1
  if count == (nx*ny):
    break

print("Part 2:", step)
