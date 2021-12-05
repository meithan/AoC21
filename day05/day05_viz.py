# Viz for Day 5: Hydrothermal Venture

import sys

import matplotlib.colors as mcolors
from PIL import Image
import numpy as np

# ==============================================================================

# Read (and possibly pre-process) input
lines = []
with open("day05.in") as f:
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

pixels = np.zeros((1000, 1000, 3), dtype=np.uint8)
color1 = tuple(int(x*255) for x in mcolors.to_rgb("purple"))
color2 = tuple(int(x*255) for x in mcolors.to_rgb("limegreen"))
for (x,y), count in grid2.items():
  if count == 0:
    pixels[x,y] = (0,0,0)
  elif count == 1:
    pixels[x,y] = color1
  elif count >= 2:
    pixels[x,y] = color2

img = Image.fromarray(pixels, "RGB")

if "--save" in sys.argv:
  img.save("day05.png")
else:
  img.show()
