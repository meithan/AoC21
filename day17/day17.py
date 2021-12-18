# Day 17: Trick Shot

from math import sqrt, ceil
import re
import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
with open(sys.argv[1]) as f:
  for line in f:
    x1, x2, y1, y2 = re.match("target area: x=([-0-9]+)\.\.([-0-9]+), y=([-0-9]+)\.\.([-0-9]+)", line.strip()).groups()
    x1, x2, y1, y2 = (int(x) for x in (x1, x2, y1, y2))

def simulate(vx0, vy0):

  x, y, = 0, 0
  vx, vy = vx0, vy0
  ymax = float("-inf")
  trajec = [(0,0)]
  while True:
    
    x += vx
    y += vy
    if vx != 0:
      vx += -1 if vx > 0 else +1
    vy -= 1

    trajec.append((x,y))

    if x1 <= x <= x2 and y1 <= y <= y2:
      return True, trajec

    if x > x2 or y < y1:
      return False, trajec

# ------------------------------------------------------------------------------
# Parts 1 and 2

# Determine search range of x velocity
vx_min = int(ceil((sqrt(8*x1+1)-1)/2))
vx_max = x2

# Set search range for y velocity
vy_min = -100
vy_max = 100

best_y = float("-inf")
best_vs = None
solutions = []

for vx in range(vx_min, vx_max+1):
  for vy in range(vy_min, vy_max):
    hit_target, trajec = simulate(vx, vy)
    if hit_target:
      solutions.append((vx,vy))
      xs, ys = zip(*trajec)
      if max(ys) > best_y:
        best_y = max(ys)
        best_vs = vx,vy
        # print(f"new max height: {best_y}")
        # plot_trajec(trajec)

print("Part 1:", best_y)
print("Part 2:", len(solutions))
