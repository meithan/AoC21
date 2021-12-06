# Day 6: Lanternfish

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
fishes = []
with open(sys.argv[1]) as f:
  for line in f:
    fishes = [int(x) for x in line.strip().split(",")]

def simulate_day():
  N = len(fishes)
  for i in range(N):
    if fishes[i] == 0:
      fishes[i] = 6
      fishes.append(8)
    else:
      fishes[i] -= 1

orig_fishes = [x for x in fishes]

# ------------------------------------------------------------------------------
# Part 1

for i in range(1, 80+1):
  simulate_day()

print("Part 1:", len(fishes))

# ------------------------------------------------------------------------------
# Part 2

table = [None]*(264+1)
with open("table.txt") as f:
  for line in f:
    t, N = tuple(int(x) for x in line.strip().split())
    table[t] = N

tot_size = 0
for f in orig_fishes:
  size = table[256+(8-f)]
  tot_size += size

print("Part 2:", tot_size)
