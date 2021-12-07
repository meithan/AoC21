# Day 7:

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input

with open(sys.argv[1]) as f:
  positions = [int(x) for x in f.readline().strip().split(",")]

# ------------------------------------------------------------------------------
# Part 1

min_pos = min(positions)
max_pos = max(positions)

def find_cost(target):
  cost = 0
  for x in positions:
    cost += abs(x-target)
  return cost

best_pos = None
best_cost = None
for p in range(min_pos, max_pos+1):
  c = find_cost(p)
  if best_cost is None or c < best_cost:
    best_pos = p
    best_cost = c

print("Part 1:", best_cost)

# ------------------------------------------------------------------------------
# Part 2

def find_cost2(target):
  cost = 0
  for x in positions:
    N = abs(x-target)
    cost += N*(N+1)//2
  return cost

best_pos = None
best_cost = None
for p in range(min_pos, max_pos+1):
  c = find_cost2(p)
  if best_cost is None or c < best_cost:
    best_pos = p
    best_cost = c

print("Part 2:", best_cost)
