# Day 2: Dive!

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Read (and possibly pre-process) input
moves = []
with open(sys.argv[1]) as f:
  for line in f:
    command, value = line.strip().split()
    moves.append((command, int(value)))

# ------------------------------------------------------------------------------
# Part 1

position = 0
depth = 0

for cmd, value in moves:
  if cmd == "forward":
    position += value
  elif cmd == "down":
    depth += value
  elif cmd == "up":
    depth -= value

print("Part 1:", position * depth)

# ------------------------------------------------------------------------------
# Part 2

position = 0
depth = 0
aim = 0

for cmd, value in moves:
  if cmd == "forward":
    position += value
    depth += aim*value
  elif cmd == "down":
    aim += value
  elif cmd == "up":
    aim -= value

print("Part 2:", position*depth)
