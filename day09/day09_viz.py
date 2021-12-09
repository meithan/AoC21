# Day 9: Smoke Basin

import random
from queue import Queue
import sys

from PIL import Image
import matplotlib.colors as mcolors
import numpy as np

# ==============================================================================

# Generate color palette for digits 0 to 9
def gen_pallete(color, n):
  h, _, _ = mcolors.rgb_to_hsv(mcolors.to_rgb(color))
  s = 1
  vs = np.linspace(0.0, 1.0, n)
  colors = [mcolors.hsv_to_rgb((h,s,v)) for v in vs]
  colors = [(r*255, g*255, b*255) for r,g,b in colors]
  return colors

if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
height = []
with open(sys.argv[1]) as f:
  for line in f:
    height.append([int(n) for n in line.strip()])

nx = len(height)
ny = len(height[0])

# Plot clean map
binning = 10
nxim = nx*binning
nyim = ny*binning
pixels = np.zeros((nxim, nyim, 3), dtype=np.uint8)
palette = gen_pallete("cyan", 10)
for ii in range(nxim):
  for jj in range(nyim):
    i = ii // binning
    j = jj // binning
    pixels[ii,jj] = palette[height[i][j]]

img = Image.fromarray(pixels, "RGB")

if "--save" in sys.argv:
  img.save("day09_map1.png")
else:
  img.show()

# Plot basins
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
for i in range(nx):
  for j in range(ny):
    if is_lowpoint(i, j):
      lows.append((i,j))
 
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

basins = []
for low in lows:
  basin = find_basin(low)
  basins.append(basin)

binning = 10
nxim = nx*binning
nyim = ny*binning
pixels = np.zeros((nxim, nyim, 3), dtype=np.uint8)
pixels[:,:] = (255, 255, 255)
# base_colors = ["cyan", "violet", "coral", "palegreen", "orange"]
base_colors = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462','#b3de69','#fccde5','#d9d9d9']
for basin in basins:
  palette = gen_pallete(random.choice(base_colors), 9)
  for i,j in basin:
    for di in range(binning):
      for dj in range(binning):
        ii = binning*i + di
        jj = binning*j + dj
        pixels[ii,jj] = palette[height[i][j]]

img = Image.fromarray(pixels, "RGB")

if "--save" in sys.argv:
  img.save("day09_map2.png")
else:
  img.show()
