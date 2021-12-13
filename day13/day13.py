# Day 13: Transparent Origami

import sys
import re

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
dots = set()
instructions = []
with open(sys.argv[1]) as f:
  for line in f:
    if "," in line:
      x, y = line.strip().split(",")
      dots.add((int(x),int(y)))
    elif "fold" in line:
      m = re.match("fold along ([xy])=([0-9]+)", line)
      dim, fold = m.groups()
      instructions.append((dim, int(fold)))

# ------------------------------------------------------------------------------
# Part 1

ans1 = None
for dim, fold in instructions:
  new_dots = set()
  for x,y in dots:
    if dim == "x":
      if x > fold:
        nx = fold - (x - fold)
        ny = y
      else:
        nx, ny = x, y
    elif dim == "y":
      if y > fold:
        nx = x
        ny = fold - (y - fold)
      else:
        nx, ny = x, y        
    new_dots.add((nx, ny))
  dots = new_dots
  if ans1 is None:
    ans1 = len(dots)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

print("Part 2:", "see plot")

import matplotlib.pyplot as plt
xs, ys = zip(*dots)
plt.figure(figsize=(10,1.5))
plt.scatter(xs, ys)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.axis("off")
plt.show()


