# Day 5: Hydrothermal Venture

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read (and possibly pre-process) input
lines = []
with open(sys.argv[1]) as f:
  for line in f:
    parts = line.strip().split("->")
    x1, y1 = (int(x) for x in parts[0].split(","))
    x2, y2 = (int(x) for x in parts[1].split(","))
    lines.append((x1,y1,x2,y2))

# ------------------------------------------------------------------------------
# Parts 1 and 2

grid1 = {}
grid2 = {}
for x1,y1,x2,y2 in lines:
    x,y = x1,y1
    dx = 0 if x1 == x2 else (+1 if x1 < x2 else -1)
    dy = 0 if y1 == y2 else (+1 if y1 < y2 else -1)
    while True:
      if x1 == x2 or y1 == y2:
        if (x,y) not in grid1:
          grid1[(x,y)] = 0
        grid1[(x,y)] += 1
      if (x,y) not in grid2:
        grid2[(x,y)] = 0
      grid2[(x,y)] += 1
      if (x,y) == (x2,y2):
        break
      x += dx
      y += dy

count1 = [x >= 2 for x in grid1.values()].count(True)
count2 = [x >= 2 for x in grid2.values()].count(True)

print("Part 1:", count1)
print("Part 2:", count2)
