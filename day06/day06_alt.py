# Day 6: Lanternfish
# Alternate version with an actual smart solution, doh!

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
with open(sys.argv[1]) as f:
  start_timers = [int(x) for x in f.readline().strip().split(",")]

# Initialize counts of fishes by internal timer
fishes = [0]*9
for t in start_timers:
  fishes[t] += 1

def simulate_day():
  zeros = fishes[0]
  for i in range(8):
    fishes[i] = fishes[i+1]
  fishes[8] = zeros
  fishes[6] += zeros

# ------------------------------------------------------------------------------
# Parts 1 and 2

for day in range(1,256+1):
  simulate_day()
  if day == 80:
    ans1 = sum(fishes)
  if day == 256:
    ans2 = sum(fishes)

print("Part 1:", ans1)
print("Part 2:", ans2)
